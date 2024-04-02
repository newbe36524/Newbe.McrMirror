from invoke import task
import os
import json
import itertools
import shutil
import time


@task
def create_yml_v2(c):
    with open("config-v2.json", "r") as json_file:
        content = json_file.read()
    config = json.loads(content)

    def concat_image_names(g):
        parts = map(lambda i: f"          - {i['source']},{i['tag']}", g)
        return str.join("\n", parts)

    def convert_image_group_to_image_json(g, registry, namespace):
        result = {}
        for image_group_item in g:
            result[image_group_item['source']] = f"{registry}/{namespace}/{image_group_item['tag']}"
        return json.dumps(result)

    images = []
    group_max_count = 10
    for k, items in itertools.groupby(config['images'], lambda f: f['group']):
        i = 0
        group_items = []
        group_index = 0
        for item in items:
            if i < group_max_count:
                group_items.append(item)
                i = i + 1
            else:
                i = 0
                images.append({'name': f"{k}_{group_index}", 'images': group_items})
                group_index = group_index + 1
                group_items = []

        if len(group_items) > 0:
            images.append({'name': f"{k}_{group_index}", 'images': group_items})

    templates = [
        "template_aliyun.yml",
        "template_dockerhub.yml",
        "template_tencent.yml"
    ]
    registries = {
        "aliyun": (
            "registry.cn-hangzhou.aliyuncs.com", config['aliyun_namespace']
        ),
        "dockerhub": (
            "registry.hub.docker.com", config['dockerhub_namespace']
        ),
    }
    registry_jsons = {
        "aliyun": [],
        "dockerhub": [],
    }
    out_dir = "../../.github/workflows"
    image_out_dir = "./image_config"
    shutil.rmtree(image_out_dir)
    os.mkdir(image_out_dir)
    for server in registries:
        registry, namespace = registries[server]
        image_json_filenames = []
        for image in images:
            filename = f"sync_{image['name']}_to_{server}"
            image_json_filename = f"{filename}.json"
            image_json_filenames.append(image_json_filename)
            with open(os.path.join(image_out_dir, image_json_filename), "w") as image_json_file:
                image_json = convert_image_group_to_image_json(image['images'], registry, namespace)
                image_json_file.write(image_json)
        registry_jsons[server] = image_json_filenames
    with open("templace_docker_sync.yml", "r") as template_file:
        template_content = template_file.read()
        for server in registry_jsons:
            image_json_filenames = registry_jsons[server]
            all_image_str = str.join("\n", [f"          - {name}" for name in image_json_filenames])
            content = template_content \
                .replace("[ALL_IMAGE]", all_image_str) \
                .replace("[SERVER]", server)
            with open(f"{out_dir}/docker_sync_{server}.yml", 'w') as result_file:
                result_file.write(content)


@task
def create_yml(c):
    with open("config-v2.json", "r") as json_file:
        content = json_file.read()
    config = json.loads(content)

    def concat_image_names(g):
        parts = map(lambda i: f"          - {i['source']},{i['tag']}", g)
        return str.join("\n", parts)

    images = []
    group_max_count = 10
    for k, items in itertools.groupby(config['images'], lambda f: f['group']):
        i = 0
        group_items = []
        group_index = 0
        for item in items:
            if i < group_max_count:
                group_items.append(item)
                i = i + 1
            else:
                i = 0
                a = concat_image_names(group_items)
                images.append({'name': f"{k}_{group_index}", 'images': a})
                group_index = group_index + 1
                group_items = []

        if len(group_items) > 0:
            a = concat_image_names(group_items)
            images.append({'name': f"{k}_{group_index}", 'images': a})

    templates = [
        "template_aliyun.yml",
        "template_dockerhub.yml",
        "template_tencent.yml"
    ]
    out_dir = "../../.github/workflows"
    for t in templates:
        server = t.replace("template_", "").replace(".yml", "")
        for image in images:
            filename = f"sync_{image['name']}_to_{server}"
            with open(t, "r") as template_file:
                template_content = template_file.read()
            content = template_content \
                .replace("[FILE_NAME]", filename) \
                .replace("[DOCKERHUB_USERNAME]", config['dockerhub_name']) \
                .replace("[DOCKERHUB_NAMESPACE]", config['dockerhub_namespace']) \
                .replace("[ALIYUN_USERNAME]", config['aliyun_name']) \
                .replace("[ALIYUN_NAMESPACE]", config['aliyun_namespace']) \
                .replace("[TENCENTYUN_USERNAME]", config['tencentyun_name']) \
                .replace("[TENCENTYUN_NAMESPACE]", config['tencentyun_namespace']) \
                .replace("[ALL_IMAGE]", image['images'])
            with open(f"{out_dir}/docker_{filename}.yml", 'w') as result_file:
                result_file.write(content)

@task
def sync_aliyun(c):
    # load config
    with open("config-v2.json", "r") as json_file:
        content = json_file.read()
    config = json.loads(content)

    # create process if not exists
    if not os.path.exists("process.json"):
        with open("process.json", "w") as process_file:
            process_file.write("{}")

    # load process
    with open("process.json", "r") as process_file:
        process = json.loads(process_file.read())
    
    processed_count = len(process)
    process_percent = processed_count / len(config['images'])
    # sync
    for image in config['images']:
        source_image = image['source']
        # skip windows image
        if "windows" in source_image:
            continue
        else:
            target_image = f"registry.cn-hangzhou.aliyuncs.com/{config['aliyun_namespace']}/{image['tag']}"
            if source_image in process:
                if process[source_image] == target_image:
                    print(f"Skip {source_image} -> {target_image}")
                    continue
            print(f"Sync {source_image} -> {target_image}")
            # try to pull, if error retry after 30 seconds and retry 10 times
            try_count = 0
            while try_count < 10:
                try:
                    c.run(f"docker pull {source_image} ")
                    break
                except:
                    try_count = try_count + 1
                    print(f"Retry {try_count} times")
                    time.sleep(30)
            c.run(f"docker tag {source_image} {target_image}")      
            c.run(f"docker push {target_image}")
        process[source_image] = target_image
        processed_count = processed_count + 1
        process_percent = processed_count / len(config['images'])
        print(f"Progress: {process_percent}")
        # save process
        with open("process.json", "w") as process_file:
            process_file.write(json.dumps(process))


@task
def create_md(c):
    with open("config-v2.json", "r") as json_file:
        content = json_file.read()
    config = json.loads(content)
    md_content = "## Tags \n\n"

    def concat_image_names(g):
        parts = map(lambda image: f"- {image['source']}", g)
        images = str.join("\n", parts)
        return images

    for k, items in itertools.groupby(config['images'], lambda f: f['group']):
        tags = concat_image_names(items)
        md_content += f"### {k} \n\n {tags}\n\n"

    with open("md.md", "w") as md_file:
        md_file.write(md_content)

    # copy to /tags.md
    shutil.copy("md.md", "../../tags.md")


@task
def info(c):
    c.run("echo info")


@task
def pull_image(c, data):
    strings = data.split(',')
    source_image_name = strings[0]
    cmd = f"docker pull {source_image_name}"
    print(cmd)
    c.run(cmd)


@task
def docker_sync_dockerhub(c, data):
    strings = data.split(',')
    source_image_name = strings[0]
    target_image_name = strings[1]
    namespace = os.environ['DOCKERHUB_NAMESPACE']
    c.run(f"docker tag {source_image_name} {namespace}/{target_image_name}")
    c.run(f"docker push {namespace}/{target_image_name}")


@task
def docker_sync_aliyun(c, data):
    strings = data.split(',')
    source_image_name = strings[0]
    target_image_name = strings[1]
    namespace = os.environ['ALIYUN_NAMESPACE']
    c.run(
        f"docker tag {source_image_name} registry.cn-hangzhou.aliyuncs.com/{namespace}/{target_image_name}")
    c.run(
        f"docker push registry.cn-hangzhou.aliyuncs.com/{namespace}/{target_image_name}")


@task
def docker_sync_tencent(c, data):
    strings = data.split(',')
    source_image_name = strings[0]
    target_image_name = strings[1]
    namespace = os.environ['TENCENTYUN_NAMESPACE']
    c.run(
        f"docker tag {source_image_name} ccr.ccs.tencentyun.com/{namespace}/{target_image_name}")
    c.run(
        f"docker push ccr.ccs.tencentyun.com/{namespace}/{target_image_name}")
