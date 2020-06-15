# Newbe.McrMirror
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

MCR(Miscrosoft Container Registry) 加速器，助你在中国大陆急速下载 netcore 相关的 docker 镜像。

## 如何使用

存在至少三种方法进行加速：

- 使用 docker-mcr （推荐）
- 拉取阿里云上的仓库
- 使用 DockerHub 加速器

注意，无论采用什么方式，请先确保本地的 docker 已经正常可用。

### 使用 docker-mcr （推荐）

docker-mcr 是一个 dotnet core global tool，简单几步，便可以进行安装和使用。

[进入dotnet页面，下载并安装 netcore 3.1 SDK](https://dotnet.microsoft.com/download)。

安装完毕后打开控制台运行以下命令:

```bash
dotnet tool install newbe.mcrmirror -g 
```

现在，假如需要拉取 mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim ，则运行以下命令：

```bash
docker-mcr -i mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim
```

等待完成之后，便可以在本地看到已经拉取完毕的镜像。

### 使用阿里云上的仓库

规则，mcr.microsoft.com/dotnet/core/{name}:{tag} ->  registry.cn-hangzhou.aliyuncs.com/newbe36524/{name}:{tag}

例如，您可以运行以下命令:

```bash
docker pull registry.cn-hangzhou.aliyuncs.com/newbe36524/aspnet:3.1-buster-slim
docker tag newbe36524/aspnet:3.1-buster-slim mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim
```

这样你就成功的在本地得到了 mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim 镜像。

当然，你也可以直接把 registry.cn-hangzhou.aliyuncs.com/newbe36524/aspnet:3.1-buster-slim 写入到你的 Docker file 中。

### 使用 DockerHub 加速器

规则，mcr.microsoft.com/dotnet/core/{name}:{tag} -> newbe36524/{name}:{tag}

例如，您可以运行以下命令:

```bash
docker pull newbe36524/aspnet:3.1-buster-slim
docker tag newbe36524/aspnet:3.1-buster-slim mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim
```

这样你就成功的在本地得到了 mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim 镜像。

当然，你也可以直接把 newbe36524/aspnet:3.1-buster-slim 写入到你的 Docker file 中。

在此之前，请确保你正确配置了本地的加速器。

## 遇到了一下问题？

我可能会遗漏一些镜像和标记，请你在这个仓库中提交issue让我知道。

## 起因经过

将微软发布在 MCR 上的镜像同步到 DockerHub 上，以加速中国大陆的下载速度。

正如我们所知，微软在2018年五月之后，只会将相关镜像打包发布到 MCR 上。

但是，在中国大陆从 MCR 上拉取镜像简直慢得让人发指。

MCR 团队已经决定尝试一些方案为此提速，相关的讨论罗列在[这个issue中](https://github.com/microsoft/containerregistry/issues/7)。我也将会持续跟踪这个issue。

现在，我决定创建这个仓库来将 MCR 上的镜像同步到 DockerHub 以及阿里云上。直到 MCR 速度的问题得到解决。

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://www.newbe.pro"><img src="https://avatars1.githubusercontent.com/u/7685462?v=4" width="100px;" alt=""/><br /><sub><b>Newbe36524</b></sub></a><br /><a href="#infra-newbe36524" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/newbe36524/Newbe.McrMirror/commits?author=newbe36524" title="Tests">⚠️</a> <a href="https://github.com/newbe36524/Newbe.McrMirror/commits?author=newbe36524" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/LiangZugeng"><img src="https://avatars0.githubusercontent.com/u/20870130?v=4" width="100px;" alt=""/><br /><sub><b>James Liang</b></sub></a><br /><a href="#ideas-LiangZugeng" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!