# Newbe.McrMirror

Mirror for publish netcore image from MCR to dockerhub to speed up download performance in China mainland.

将微软发布在 MCR 上的镜像同步到 DockerHub 上，以加速中国大陆的下载速度。

## Details

As we all know, Microsoft only push images to MCR since May 2018. 

However, it is too slow to pull that image from MCR in China mainland.

MCR team decided to speed it up as [this issue says](https://github.com/microsoft/containerregistry/issues/7). I will tracing that issue.

Now, I setup this repository to pull MCR image and push that to DockerHub. 

In China mainland, you can use mirrors for DockerHub to pull that image, e.g. Aliyun docker mirrors.

links:

- <https://docs.microsoft.com/en-us/dotnet/architecture/microservices/net-core-net-framework-containers/official-net-docker-images>

正如我们所知，微软在2018年五月之后，只会将相关镜像打包发布到 MCR 上。

但是，在中国大陆从 MCR 上拉取镜像简直慢得让人发指。

MCR 团队已经决定尝试一些方案为此提速，相关的讨论罗列在[这个issue中](https://github.com/microsoft/containerregistry/issues/7)。我也将会持续跟踪这个issue。

现在，我决定创建这个仓库来将 MCR 上的镜像同步到 DockerHub 上。直到 MCR 速度的问题得到解决。

这样，您就可以在中国大陆使用 DockerHub 的加速器来拉取这些镜像。例如，使用阿里云加速器。

## Name Rules

Just, mcr.microsoft.com/dotnet/core/{name}:{tag} -> newbe36524/{name}:{tag}

for exmaple, you can run:

```bash
docker pull newbe36524/aspnet:3.1-buster-slim
docker tag newbe36524/aspnet:3.1-buster-slim mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim
```

That you will got that image mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim

It is ok if you want to use newbe36524/aspnet:3.1-buster-slim directly in your docker file.

Please make sure that you configure you mirror right.

规则很简单，mcr.microsoft.com/dotnet/core/{name}:{tag} -> newbe36524/{name}:{tag}

例如，您可以运行以下命令:

```bash
docker pull newbe36524/aspnet:3.1-buster-slim
docker tag newbe36524/aspnet:3.1-buster-slim mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim
```

这样你就成功的在本地得到了 mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim 镜像。

当然，你也可以直接把 newbe36524/aspnet:3.1-buster-slim 写入到你的 Docker file 中。

在此之前，请确保你正确配置了本地的加速器。

## Missing Image

Maybe I miss some tags or images, please create a issue in this repository.

我可能会遗漏一些镜像和标记，请你在这个仓库中提交issue让我知道。