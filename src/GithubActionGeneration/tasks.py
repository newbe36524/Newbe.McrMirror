from invoke import task
import os
import json
import itertools


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
    c.run(f"docker tag {source_image_name} registry.cn-hangzhou.aliyuncs.com/{namespace}/{target_image_name}")
    c.run(f"docker push registry.cn-hangzhou.aliyuncs.com/{namespace}/{target_image_name}")


@task
def docker_sync_tencent(c, data):
    strings = data.split(',')
    source_image_name = strings[0]
    target_image_name = strings[1]
    namespace = os.environ['TENCENTYUN_NAMESPACE']
    c.run(f"docker tag {source_image_name} ccr.ccs.tencentyun.com/{namespace}/{target_image_name}")
    c.run(f"docker push ccr.ccs.tencentyun.com/{namespace}/{target_image_name}")
