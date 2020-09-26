from invoke import task
import os


@task
def info(c):
    c.run("echo info")


@task
def pull_image(c, data):
    data.split(',')
    source_image_name = data[0]
    cmd = f"docker pull {source_image_name}"
    print(cmd)
    c.run(cmd)


@task
def docker_sync_dockerhub(c, data):
    data.split(',')
    source_image_name = data[0]
    target_image_name = data[1]
    namespace = os.environ['DOCKERHUB_NAMESPACE']
    c.run(f"docker tag {source_image_name} {namespace}/{target_image_name}")
    c.run(f"docker push {namespace}/{target_image_name}")


@task
def docker_sync_aliyun(c, data):
    data.split(',')
    source_image_name = data[0]
    target_image_name = data[1]
    namespace = os.environ['ALIYUN_NAMESPACE']
    c.run(f"docker tag {source_image_name} registry.cn-hangzhou.aliyuncs.com/{namespace}/{target_image_name}")
    c.run(f"docker push registry.cn-hangzhou.aliyuncs.com/{namespace}/{target_image_name}")


@task
def docker_sync_tencent(c, data):
    data.split(',')
    source_image_name = data[0]
    target_image_name = data[1]
    namespace = os.environ['TENCENTYUN_NAMESPACE']
    c.run(f"docker tag {source_image_name} ccr.ccs.tencentyun.com/{namespace}/{target_image_name}")
    c.run(f"docker push ccr.ccs.tencentyun.com/{namespace}/{target_image_name}")
