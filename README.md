# Newbe.McrMirror

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-8-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

MCR(Miscrosoft Container Registry) 加速器，助你在中国大陆急速下载 netcore 相关的 docker 镜像。

## 如何使用

存在至少三种方法进行加速：

- 使用 docker-mcr （推荐）
- 拉取国内服务器上的镜像
- 使用 DockerHub 加速器

注意，无论采用什么方式，请先确保本地的 docker 已经正常可用。

### 使用 docker-mcr （推荐）

docker-mcr 是一个 dotnet core global tool，简单几步，便可以进行安装和使用。

[进入 dotnet 页面，下载并安装 netcore 3.1 SDK](https://dotnet.microsoft.com/download)。

安装完毕后打开控制台运行以下命令:

```bash
dotnet tool install newbe.mcrmirror -g
```

现在，假如需要拉取 mcr.microsoft.com/dotnet/aspnet:3.1-buster-slim ，则运行以下命令：

```bash
docker-mcr -i mcr.microsoft.com/dotnet/aspnet:3.1-buster-slim
```

等待完成之后，便可以在本地看到已经拉取完毕的镜像。

您可以运行 `docker-mcr --help` 来查看更多的参数配置方式。

如果您曾经安装过 newbe.mcrmirror ,您需要使用`dotnet tool update newbe.mcrmirror -g`命令来进行升级，确保最佳的体验。

### 拉取国内服务器上的镜像

加速的本质是因为我将镜像推送到了国内的服务器，目前在以下服务器均存在镜像:

- 阿里云 registry.cn-hangzhou.aliyuncs.com/newbe36524
- 腾讯云 ccr.ccs.tencentyun.com/mcr_newbe36524

以下以阿里云为例进行说明，假设需要拉取 mcr.microsoft.com/dotnet/aspnet:3.1-buster-slim

[点击此处打开配置文件](https://gitee.com/yks/Newbe.McrMirror/raw/master/src/GithubActionGeneration/config-v2.json)，搜索 mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim 会找到以下节点

```json
{
  "tag": "aspnet:3.1-buster-slim",
  "source": "mcr.microsoft.com/dotnet/aspnet:3.1-buster-slim"
}
```

则说明在国内镜像的 tag 为 aspnet:3.1-buster-slim。

则拼接上面的前缀，则得到地址 registry.cn-hangzhou.aliyuncs.com/newbe36524/aspnet:3.1-buster-slim

然后，为了不修改默认的 Dockerfile 您可以运行以下命令:

```bash
docker pull registry.cn-hangzhou.aliyuncs.com/newbe36524/aspnet:3.1-buster-slim
docker tag registry.cn-hangzhou.aliyuncs.com/newbe36524/aspnet:3.1-buster-slim mcr.microsoft.com/dotnet/aspnet:3.1-buster-slim
```

这样你就成功的在本地得到了 mcr.microsoft.com/dotnet/aspnet:3.1-buster-slim 镜像。

当然，你也可以直接把 registry.cn-hangzhou.aliyuncs.com/newbe36524/aspnet:3.1-buster-slim 写入到你的 Docker file 中。

### 使用 DockerHub 加速器

我也将镜像推送到了 dockerhub ，所以正常来说，在中国大陆使用 dockerhub 加速器也可以达到加速的效果。

规则，mcr.microsoft.com/dotnet/{name}:{tag} -> newbe36524/{name}:{tag}

例如，您可以运行以下命令:

```bash
docker pull newbe36524/aspnet:3.1-buster-slim
docker tag newbe36524/aspnet:3.1-buster-slim mcr.microsoft.com/dotnet/aspnet:3.1-buster-slim
```

这样你就成功的在本地得到了 mcr.microsoft.com/dotnet/aspnet:3.1-buster-slim 镜像。

当然，你也可以直接把 newbe36524/aspnet:3.1-buster-slim 写入到你的 Docker file 中。

在此之前，请确保你正确配置了本地的加速器。

## 遇到了一点问题？

所有已经被支持的镜像全部罗列在本文档下方，我可能会遗漏一些镜像和标记，请你在这个仓库中提交 issue 让我知道。

## 起因经过

将微软发布在 MCR 上的镜像同步到 DockerHub 上，以加速中国大陆的下载速度。

正如我们所知，微软在 2018 年五月之后，只会将相关镜像打包发布到 MCR 上。

但是，在中国大陆从 MCR 上拉取镜像简直慢得让人发指。

MCR 团队已经决定尝试一些方案为此提速，相关的讨论罗列在[这个 issue 中](https://github.com/microsoft/containerregistry/issues/7)。该 Issue 已经关闭了。不过我们仍然会继续更新相关的镜像。如果您在拉取时还是存在问题，则可以继续使用本项目提供的镜像。

现在，我决定创建这个仓库来将 MCR 上的镜像同步到 DockerHub 以及阿里云上。直到 MCR 速度的问题得到解决。

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://www.newbe.pro"><img src="https://avatars1.githubusercontent.com/u/7685462?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Newbe36524</b></sub></a><br /><a href="#infra-newbe36524" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/newbe36524/Newbe.McrMirror/commits?author=newbe36524" title="Tests">⚠️</a> <a href="https://github.com/newbe36524/Newbe.McrMirror/commits?author=newbe36524" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/LiangZugeng"><img src="https://avatars0.githubusercontent.com/u/20870130?v=4?s=100" width="100px;" alt=""/><br /><sub><b>James Liang</b></sub></a><br /><a href="#ideas-LiangZugeng" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/fisherwei"><img src="https://avatars0.githubusercontent.com/u/214470?v=4?s=100" width="100px;" alt=""/><br /><sub><b>fisherwei</b></sub></a><br /><a href="#ideas-fisherwei" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/newbe36524/Newbe.McrMirror/issues?q=author%3Afisherwei" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/hongliuyi"><img src="https://avatars0.githubusercontent.com/u/33167076?v=4?s=100" width="100px;" alt=""/><br /><sub><b>hongliuyi</b></sub></a><br /><a href="https://github.com/newbe36524/Newbe.McrMirror/issues?q=author%3Ahongliuyi" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/zengzhengrong"><img src="https://avatars0.githubusercontent.com/u/23110784?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Zzr</b></sub></a><br /><a href="#ideas-zengzhengrong" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="http://www.minicraft.top"><img src="https://avatars.githubusercontent.com/u/39231698?v=4?s=100" width="100px;" alt=""/><br /><sub><b>TONY_All</b></sub></a><br /><a href="#ideas-TONY-All" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://ddddddddd.top"><img src="https://avatars.githubusercontent.com/u/43628016?v=4?s=100" width="100px;" alt=""/><br /><sub><b>FangPengbo</b></sub></a><br /><a href="#ideas-FangPengbo" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.cnblogs.com/weihanli"><img src="https://avatars.githubusercontent.com/u/7604648?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Weihan Li</b></sub></a><br /><a href="#ideas-WeihanLi" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Tags

### sdk

- mcr.microsoft.com/dotnet/sdk:3.1
- mcr.microsoft.com/dotnet/sdk:3.1-alpine
- mcr.microsoft.com/dotnet/sdk:3.1-alpine3.13
- mcr.microsoft.com/dotnet/sdk:3.1-alpine3.14
- mcr.microsoft.com/dotnet/sdk:3.1-bionic
- mcr.microsoft.com/dotnet/sdk:3.1-bionic-arm32v7
- mcr.microsoft.com/dotnet/sdk:3.1-bionic-arm64v8
- mcr.microsoft.com/dotnet/sdk:3.1-bullseye
- mcr.microsoft.com/dotnet/sdk:3.1-bullseye-arm32v7
- mcr.microsoft.com/dotnet/sdk:3.1-bullseye-arm64v8
- mcr.microsoft.com/dotnet/sdk:3.1-buster
- mcr.microsoft.com/dotnet/sdk:3.1-buster-arm32v7
- mcr.microsoft.com/dotnet/sdk:3.1-buster-arm64v8
- mcr.microsoft.com/dotnet/sdk:3.1-focal
- mcr.microsoft.com/dotnet/sdk:3.1-focal-arm32v7
- mcr.microsoft.com/dotnet/sdk:3.1-focal-arm64v8
- mcr.microsoft.com/dotnet/sdk:3.1.415
- mcr.microsoft.com/dotnet/sdk:3.1.415-alpine3.13
- mcr.microsoft.com/dotnet/sdk:3.1.415-alpine3.14
- mcr.microsoft.com/dotnet/sdk:3.1.415-bionic
- mcr.microsoft.com/dotnet/sdk:3.1.415-bionic-arm32v7
- mcr.microsoft.com/dotnet/sdk:3.1.415-bionic-arm64v8
- mcr.microsoft.com/dotnet/sdk:3.1.415-bullseye
- mcr.microsoft.com/dotnet/sdk:3.1.415-bullseye-arm32v7
- mcr.microsoft.com/dotnet/sdk:3.1.415-bullseye-arm64v8
- mcr.microsoft.com/dotnet/sdk:3.1.415-buster
- mcr.microsoft.com/dotnet/sdk:3.1.415-buster-arm32v7
- mcr.microsoft.com/dotnet/sdk:3.1.415-buster-arm64v8
- mcr.microsoft.com/dotnet/sdk:3.1.415-focal
- mcr.microsoft.com/dotnet/sdk:3.1.415-focal-arm32v7
- mcr.microsoft.com/dotnet/sdk:3.1.415-focal-arm64v8
- mcr.microsoft.com/dotnet/sdk:5.0
- mcr.microsoft.com/dotnet/sdk:5.0-alpine
- mcr.microsoft.com/dotnet/sdk:5.0-alpine-amd64
- mcr.microsoft.com/dotnet/sdk:5.0-alpine3.13
- mcr.microsoft.com/dotnet/sdk:5.0-alpine3.13-amd64
- mcr.microsoft.com/dotnet/sdk:5.0-alpine3.14
- mcr.microsoft.com/dotnet/sdk:5.0-alpine3.14-amd64
- mcr.microsoft.com/dotnet/sdk:5.0-bullseye-slim
- mcr.microsoft.com/dotnet/sdk:5.0-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/sdk:5.0-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/sdk:5.0-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/sdk:5.0-buster-slim
- mcr.microsoft.com/dotnet/sdk:5.0-buster-slim-amd64
- mcr.microsoft.com/dotnet/sdk:5.0-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/sdk:5.0-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/sdk:5.0-focal
- mcr.microsoft.com/dotnet/sdk:5.0-focal-amd64
- mcr.microsoft.com/dotnet/sdk:5.0-focal-arm32v7
- mcr.microsoft.com/dotnet/sdk:5.0-focal-arm64v8
- mcr.microsoft.com/dotnet/sdk:5.0-windowsservercore-ltsc2022
- mcr.microsoft.com/dotnet/sdk:5.0.403
- mcr.microsoft.com/dotnet/sdk:5.0.403-alpine3.13
- mcr.microsoft.com/dotnet/sdk:5.0.403-alpine3.13-amd64
- mcr.microsoft.com/dotnet/sdk:5.0.403-alpine3.14
- mcr.microsoft.com/dotnet/sdk:5.0.403-alpine3.14-amd64
- mcr.microsoft.com/dotnet/sdk:5.0.403-bullseye-slim
- mcr.microsoft.com/dotnet/sdk:5.0.403-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/sdk:5.0.403-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/sdk:5.0.403-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/sdk:5.0.403-buster-slim
- mcr.microsoft.com/dotnet/sdk:5.0.403-buster-slim-amd64
- mcr.microsoft.com/dotnet/sdk:5.0.403-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/sdk:5.0.403-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/sdk:5.0.403-focal
- mcr.microsoft.com/dotnet/sdk:5.0.403-focal-amd64
- mcr.microsoft.com/dotnet/sdk:5.0.403-focal-arm32v7
- mcr.microsoft.com/dotnet/sdk:5.0.403-focal-arm64v8
- mcr.microsoft.com/dotnet/sdk:5.0.403-windowsservercore-ltsc2022
- mcr.microsoft.com/dotnet/sdk:6.0
- mcr.microsoft.com/dotnet/sdk:6.0-alpine
- mcr.microsoft.com/dotnet/sdk:6.0-alpine-amd64
- mcr.microsoft.com/dotnet/sdk:6.0-alpine-arm32v7
- mcr.microsoft.com/dotnet/sdk:6.0-alpine-arm64v8
- mcr.microsoft.com/dotnet/sdk:6.0-alpine3.14
- mcr.microsoft.com/dotnet/sdk:6.0-alpine3.14-amd64
- mcr.microsoft.com/dotnet/sdk:6.0-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/sdk:6.0-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/sdk:6.0-bullseye-slim
- mcr.microsoft.com/dotnet/sdk:6.0-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/sdk:6.0-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/sdk:6.0-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/sdk:6.0-focal
- mcr.microsoft.com/dotnet/sdk:6.0-focal-amd64
- mcr.microsoft.com/dotnet/sdk:6.0-focal-arm32v7
- mcr.microsoft.com/dotnet/sdk:6.0-focal-arm64v8
- mcr.microsoft.com/dotnet/sdk:6.0-windowsservercore-ltsc2022
- mcr.microsoft.com/dotnet/sdk:6.0.100
- mcr.microsoft.com/dotnet/sdk:6.0.100-alpine3.14
- mcr.microsoft.com/dotnet/sdk:6.0.100-alpine3.14-amd64
- mcr.microsoft.com/dotnet/sdk:6.0.100-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/sdk:6.0.100-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/sdk:6.0.100-bullseye-slim
- mcr.microsoft.com/dotnet/sdk:6.0.100-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/sdk:6.0.100-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/sdk:6.0.100-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/sdk:6.0.100-focal
- mcr.microsoft.com/dotnet/sdk:6.0.100-focal-amd64
- mcr.microsoft.com/dotnet/sdk:6.0.100-focal-arm32v7
- mcr.microsoft.com/dotnet/sdk:6.0.100-focal-arm64v8
- mcr.microsoft.com/dotnet/sdk:6.0.100-windowsservercore-ltsc2022
- mcr.microsoft.com/dotnet/sdk:latest

### runtime-deps

- mcr.microsoft.com/dotnet/runtime-deps:3.1
- mcr.microsoft.com/dotnet/runtime-deps:3.1-alpine
- mcr.microsoft.com/dotnet/runtime-deps:3.1-alpine-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:3.1-alpine3.13
- mcr.microsoft.com/dotnet/runtime-deps:3.1-alpine3.13-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:3.1-alpine3.14
- mcr.microsoft.com/dotnet/runtime-deps:3.1-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:3.1-bionic
- mcr.microsoft.com/dotnet/runtime-deps:3.1-bionic-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:3.1-bionic-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:3.1-bullseye-slim
- mcr.microsoft.com/dotnet/runtime-deps:3.1-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:3.1-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:3.1-buster-slim
- mcr.microsoft.com/dotnet/runtime-deps:3.1-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:3.1-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:3.1-focal
- mcr.microsoft.com/dotnet/runtime-deps:3.1-focal-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:3.1-focal-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-alpine3.13
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-alpine3.13-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-alpine3.14
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-bionic
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-bionic-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-bionic-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-bullseye-slim
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-buster-slim
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-focal
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-focal-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:3.1.21-focal-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:5.0
- mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine
- mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine-amd64
- mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine3.13
- mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine3.13-amd64
- mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine3.13-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine3.13-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine3.14
- mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine3.14-amd64
- mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:5.0-bullseye-slim
- mcr.microsoft.com/dotnet/runtime-deps:5.0-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/runtime-deps:5.0-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:5.0-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:5.0-buster-slim
- mcr.microsoft.com/dotnet/runtime-deps:5.0-buster-slim-amd64
- mcr.microsoft.com/dotnet/runtime-deps:5.0-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:5.0-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:5.0-focal
- mcr.microsoft.com/dotnet/runtime-deps:5.0-focal-amd64
- mcr.microsoft.com/dotnet/runtime-deps:5.0-focal-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:5.0-focal-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-alpine3.13
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-alpine3.13-amd64
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-alpine3.13-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-alpine3.13-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-alpine3.14
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-alpine3.14-amd64
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-bullseye-slim
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-buster-slim
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-buster-slim-amd64
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-focal
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-focal-amd64
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-focal-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:5.0.12-focal-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:6.0
- mcr.microsoft.com/dotnet/runtime-deps:6.0-alpine
- mcr.microsoft.com/dotnet/runtime-deps:6.0-alpine-amd64
- mcr.microsoft.com/dotnet/runtime-deps:6.0-alpine-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:6.0-alpine-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:6.0-alpine3.14
- mcr.microsoft.com/dotnet/runtime-deps:6.0-alpine3.14-amd64
- mcr.microsoft.com/dotnet/runtime-deps:6.0-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:6.0-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:6.0-bullseye-slim
- mcr.microsoft.com/dotnet/runtime-deps:6.0-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/runtime-deps:6.0-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:6.0-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:6.0-focal
- mcr.microsoft.com/dotnet/runtime-deps:6.0-focal-amd64
- mcr.microsoft.com/dotnet/runtime-deps:6.0-focal-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:6.0-focal-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:6.0.0
- mcr.microsoft.com/dotnet/runtime-deps:6.0.0-alpine3.14
- mcr.microsoft.com/dotnet/runtime-deps:6.0.0-alpine3.14-amd64
- mcr.microsoft.com/dotnet/runtime-deps:6.0.0-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:6.0.0-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:6.0.0-bullseye-slim
- mcr.microsoft.com/dotnet/runtime-deps:6.0.0-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/runtime-deps:6.0.0-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:6.0.0-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:6.0.0-focal
- mcr.microsoft.com/dotnet/runtime-deps:6.0.0-focal-amd64
- mcr.microsoft.com/dotnet/runtime-deps:6.0.0-focal-arm32v7
- mcr.microsoft.com/dotnet/runtime-deps:6.0.0-focal-arm64v8
- mcr.microsoft.com/dotnet/runtime-deps:latest

### runtime

- mcr.microsoft.com/dotnet/runtime:3.1
- mcr.microsoft.com/dotnet/runtime:3.1-alpine
- mcr.microsoft.com/dotnet/runtime:3.1-alpine-arm64v8
- mcr.microsoft.com/dotnet/runtime:3.1-alpine3.13
- mcr.microsoft.com/dotnet/runtime:3.1-alpine3.13-arm64v8
- mcr.microsoft.com/dotnet/runtime:3.1-alpine3.14
- mcr.microsoft.com/dotnet/runtime:3.1-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/runtime:3.1-bionic
- mcr.microsoft.com/dotnet/runtime:3.1-bionic-arm32v7
- mcr.microsoft.com/dotnet/runtime:3.1-bionic-arm64v8
- mcr.microsoft.com/dotnet/runtime:3.1-bullseye-slim
- mcr.microsoft.com/dotnet/runtime:3.1-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime:3.1-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime:3.1-buster-slim
- mcr.microsoft.com/dotnet/runtime:3.1-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime:3.1-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime:3.1-focal
- mcr.microsoft.com/dotnet/runtime:3.1-focal-arm32v7
- mcr.microsoft.com/dotnet/runtime:3.1-focal-arm64v8
- mcr.microsoft.com/dotnet/runtime:3.1.21
- mcr.microsoft.com/dotnet/runtime:3.1.21-alpine3.13
- mcr.microsoft.com/dotnet/runtime:3.1.21-alpine3.13-arm64v8
- mcr.microsoft.com/dotnet/runtime:3.1.21-alpine3.14
- mcr.microsoft.com/dotnet/runtime:3.1.21-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/runtime:3.1.21-bionic
- mcr.microsoft.com/dotnet/runtime:3.1.21-bionic-arm32v7
- mcr.microsoft.com/dotnet/runtime:3.1.21-bionic-arm64v8
- mcr.microsoft.com/dotnet/runtime:3.1.21-bullseye-slim
- mcr.microsoft.com/dotnet/runtime:3.1.21-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime:3.1.21-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime:3.1.21-buster-slim
- mcr.microsoft.com/dotnet/runtime:3.1.21-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime:3.1.21-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime:3.1.21-focal
- mcr.microsoft.com/dotnet/runtime:3.1.21-focal-arm32v7
- mcr.microsoft.com/dotnet/runtime:3.1.21-focal-arm64v8
- mcr.microsoft.com/dotnet/runtime:5.0
- mcr.microsoft.com/dotnet/runtime:5.0-alpine
- mcr.microsoft.com/dotnet/runtime:5.0-alpine-amd64
- mcr.microsoft.com/dotnet/runtime:5.0-alpine-arm32v7
- mcr.microsoft.com/dotnet/runtime:5.0-alpine-arm64v8
- mcr.microsoft.com/dotnet/runtime:5.0-alpine3.13
- mcr.microsoft.com/dotnet/runtime:5.0-alpine3.13-amd64
- mcr.microsoft.com/dotnet/runtime:5.0-alpine3.13-arm32v7
- mcr.microsoft.com/dotnet/runtime:5.0-alpine3.13-arm64v8
- mcr.microsoft.com/dotnet/runtime:5.0-alpine3.14
- mcr.microsoft.com/dotnet/runtime:5.0-alpine3.14-amd64
- mcr.microsoft.com/dotnet/runtime:5.0-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/runtime:5.0-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/runtime:5.0-bullseye-slim
- mcr.microsoft.com/dotnet/runtime:5.0-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/runtime:5.0-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime:5.0-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime:5.0-buster-slim
- mcr.microsoft.com/dotnet/runtime:5.0-buster-slim-amd64
- mcr.microsoft.com/dotnet/runtime:5.0-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime:5.0-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime:5.0-focal
- mcr.microsoft.com/dotnet/runtime:5.0-focal-amd64
- mcr.microsoft.com/dotnet/runtime:5.0-focal-arm32v7
- mcr.microsoft.com/dotnet/runtime:5.0-focal-arm64v8
- mcr.microsoft.com/dotnet/runtime:5.0-windowsservercore-ltsc2022
- mcr.microsoft.com/dotnet/runtime:5.0.12
- mcr.microsoft.com/dotnet/runtime:5.0.12-alpine3.13
- mcr.microsoft.com/dotnet/runtime:5.0.12-alpine3.13-amd64
- mcr.microsoft.com/dotnet/runtime:5.0.12-alpine3.13-arm32v7
- mcr.microsoft.com/dotnet/runtime:5.0.12-alpine3.13-arm64v8
- mcr.microsoft.com/dotnet/runtime:5.0.12-alpine3.14
- mcr.microsoft.com/dotnet/runtime:5.0.12-alpine3.14-amd64
- mcr.microsoft.com/dotnet/runtime:5.0.12-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/runtime:5.0.12-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/runtime:5.0.12-bullseye-slim
- mcr.microsoft.com/dotnet/runtime:5.0.12-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/runtime:5.0.12-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime:5.0.12-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime:5.0.12-buster-slim
- mcr.microsoft.com/dotnet/runtime:5.0.12-buster-slim-amd64
- mcr.microsoft.com/dotnet/runtime:5.0.12-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime:5.0.12-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime:5.0.12-focal
- mcr.microsoft.com/dotnet/runtime:5.0.12-focal-amd64
- mcr.microsoft.com/dotnet/runtime:5.0.12-focal-arm32v7
- mcr.microsoft.com/dotnet/runtime:5.0.12-focal-arm64v8
- mcr.microsoft.com/dotnet/runtime:5.0.12-windowsservercore-ltsc2022
- mcr.microsoft.com/dotnet/runtime:6.0
- mcr.microsoft.com/dotnet/runtime:6.0-alpine
- mcr.microsoft.com/dotnet/runtime:6.0-alpine-amd64
- mcr.microsoft.com/dotnet/runtime:6.0-alpine-arm32v7
- mcr.microsoft.com/dotnet/runtime:6.0-alpine-arm64v8
- mcr.microsoft.com/dotnet/runtime:6.0-alpine3.14
- mcr.microsoft.com/dotnet/runtime:6.0-alpine3.14-amd64
- mcr.microsoft.com/dotnet/runtime:6.0-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/runtime:6.0-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/runtime:6.0-bullseye-slim
- mcr.microsoft.com/dotnet/runtime:6.0-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/runtime:6.0-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime:6.0-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime:6.0-focal
- mcr.microsoft.com/dotnet/runtime:6.0-focal-amd64
- mcr.microsoft.com/dotnet/runtime:6.0-focal-arm32v7
- mcr.microsoft.com/dotnet/runtime:6.0-focal-arm64v8
- mcr.microsoft.com/dotnet/runtime:6.0-windowsservercore-ltsc2022
- mcr.microsoft.com/dotnet/runtime:6.0.0
- mcr.microsoft.com/dotnet/runtime:6.0.0-alpine3.14
- mcr.microsoft.com/dotnet/runtime:6.0.0-alpine3.14-amd64
- mcr.microsoft.com/dotnet/runtime:6.0.0-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/runtime:6.0.0-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/runtime:6.0.0-bullseye-slim
- mcr.microsoft.com/dotnet/runtime:6.0.0-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/runtime:6.0.0-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/runtime:6.0.0-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/runtime:6.0.0-focal
- mcr.microsoft.com/dotnet/runtime:6.0.0-focal-amd64
- mcr.microsoft.com/dotnet/runtime:6.0.0-focal-arm32v7
- mcr.microsoft.com/dotnet/runtime:6.0.0-focal-arm64v8
- mcr.microsoft.com/dotnet/runtime:6.0.0-windowsservercore-ltsc2022
- mcr.microsoft.com/dotnet/runtime:latest

### aspnet

- mcr.microsoft.com/dotnet/aspnet:3.1
- mcr.microsoft.com/dotnet/aspnet:3.1-alpine
- mcr.microsoft.com/dotnet/aspnet:3.1-alpine-arm64v8
- mcr.microsoft.com/dotnet/aspnet:3.1-alpine3.13
- mcr.microsoft.com/dotnet/aspnet:3.1-alpine3.13-arm64v8
- mcr.microsoft.com/dotnet/aspnet:3.1-alpine3.14
- mcr.microsoft.com/dotnet/aspnet:3.1-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/aspnet:3.1-bionic
- mcr.microsoft.com/dotnet/aspnet:3.1-bionic-arm32v7
- mcr.microsoft.com/dotnet/aspnet:3.1-bionic-arm64v8
- mcr.microsoft.com/dotnet/aspnet:3.1-bullseye-slim
- mcr.microsoft.com/dotnet/aspnet:3.1-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/aspnet:3.1-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/aspnet:3.1-buster-slim
- mcr.microsoft.com/dotnet/aspnet:3.1-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/aspnet:3.1-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/aspnet:3.1-focal
- mcr.microsoft.com/dotnet/aspnet:3.1-focal-arm32v7
- mcr.microsoft.com/dotnet/aspnet:3.1-focal-arm64v8
- mcr.microsoft.com/dotnet/aspnet:3.1.21
- mcr.microsoft.com/dotnet/aspnet:3.1.21-alpine3.13
- mcr.microsoft.com/dotnet/aspnet:3.1.21-alpine3.13-arm64v8
- mcr.microsoft.com/dotnet/aspnet:3.1.21-alpine3.14
- mcr.microsoft.com/dotnet/aspnet:3.1.21-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/aspnet:3.1.21-bionic
- mcr.microsoft.com/dotnet/aspnet:3.1.21-bionic-arm32v7
- mcr.microsoft.com/dotnet/aspnet:3.1.21-bionic-arm64v8
- mcr.microsoft.com/dotnet/aspnet:3.1.21-bullseye-slim
- mcr.microsoft.com/dotnet/aspnet:3.1.21-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/aspnet:3.1.21-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/aspnet:3.1.21-buster-slim
- mcr.microsoft.com/dotnet/aspnet:3.1.21-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/aspnet:3.1.21-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/aspnet:3.1.21-focal
- mcr.microsoft.com/dotnet/aspnet:3.1.21-focal-arm32v7
- mcr.microsoft.com/dotnet/aspnet:3.1.21-focal-arm64v8
- mcr.microsoft.com/dotnet/aspnet:5.0
- mcr.microsoft.com/dotnet/aspnet:5.0-alpine
- mcr.microsoft.com/dotnet/aspnet:5.0-alpine-amd64
- mcr.microsoft.com/dotnet/aspnet:5.0-alpine-arm32v7
- mcr.microsoft.com/dotnet/aspnet:5.0-alpine-arm64v8
- mcr.microsoft.com/dotnet/aspnet:5.0-alpine3.13
- mcr.microsoft.com/dotnet/aspnet:5.0-alpine3.13-amd64
- mcr.microsoft.com/dotnet/aspnet:5.0-alpine3.13-arm32v7
- mcr.microsoft.com/dotnet/aspnet:5.0-alpine3.13-arm64v8
- mcr.microsoft.com/dotnet/aspnet:5.0-alpine3.14
- mcr.microsoft.com/dotnet/aspnet:5.0-alpine3.14-amd64
- mcr.microsoft.com/dotnet/aspnet:5.0-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/aspnet:5.0-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/aspnet:5.0-bullseye-slim
- mcr.microsoft.com/dotnet/aspnet:5.0-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/aspnet:5.0-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/aspnet:5.0-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim
- mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim-amd64
- mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/aspnet:5.0-focal
- mcr.microsoft.com/dotnet/aspnet:5.0-focal-amd64
- mcr.microsoft.com/dotnet/aspnet:5.0-focal-arm32v7
- mcr.microsoft.com/dotnet/aspnet:5.0-focal-arm64v8
- mcr.microsoft.com/dotnet/aspnet:5.0-windowsservercore-ltsc2022
- mcr.microsoft.com/dotnet/aspnet:5.0.12
- mcr.microsoft.com/dotnet/aspnet:5.0.12-alpine3.13
- mcr.microsoft.com/dotnet/aspnet:5.0.12-alpine3.13-amd64
- mcr.microsoft.com/dotnet/aspnet:5.0.12-alpine3.13-arm32v7
- mcr.microsoft.com/dotnet/aspnet:5.0.12-alpine3.13-arm64v8
- mcr.microsoft.com/dotnet/aspnet:5.0.12-alpine3.14
- mcr.microsoft.com/dotnet/aspnet:5.0.12-alpine3.14-amd64
- mcr.microsoft.com/dotnet/aspnet:5.0.12-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/aspnet:5.0.12-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/aspnet:5.0.12-bullseye-slim
- mcr.microsoft.com/dotnet/aspnet:5.0.12-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/aspnet:5.0.12-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/aspnet:5.0.12-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/aspnet:5.0.12-buster-slim
- mcr.microsoft.com/dotnet/aspnet:5.0.12-buster-slim-amd64
- mcr.microsoft.com/dotnet/aspnet:5.0.12-buster-slim-arm32v7
- mcr.microsoft.com/dotnet/aspnet:5.0.12-buster-slim-arm64v8
- mcr.microsoft.com/dotnet/aspnet:5.0.12-focal
- mcr.microsoft.com/dotnet/aspnet:5.0.12-focal-amd64
- mcr.microsoft.com/dotnet/aspnet:5.0.12-focal-arm32v7
- mcr.microsoft.com/dotnet/aspnet:5.0.12-focal-arm64v8
- mcr.microsoft.com/dotnet/aspnet:5.0.12-windowsservercore-ltsc2022
- mcr.microsoft.com/dotnet/aspnet:6.0
- mcr.microsoft.com/dotnet/aspnet:6.0-alpine
- mcr.microsoft.com/dotnet/aspnet:6.0-alpine-amd64
- mcr.microsoft.com/dotnet/aspnet:6.0-alpine-arm32v7
- mcr.microsoft.com/dotnet/aspnet:6.0-alpine-arm64v8
- mcr.microsoft.com/dotnet/aspnet:6.0-alpine3.14
- mcr.microsoft.com/dotnet/aspnet:6.0-alpine3.14-amd64
- mcr.microsoft.com/dotnet/aspnet:6.0-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/aspnet:6.0-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/aspnet:6.0-bullseye-slim
- mcr.microsoft.com/dotnet/aspnet:6.0-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/aspnet:6.0-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/aspnet:6.0-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/aspnet:6.0-focal
- mcr.microsoft.com/dotnet/aspnet:6.0-focal-amd64
- mcr.microsoft.com/dotnet/aspnet:6.0-focal-arm32v7
- mcr.microsoft.com/dotnet/aspnet:6.0-focal-arm64v8
- mcr.microsoft.com/dotnet/aspnet:6.0-windowsservercore-ltsc2022
- mcr.microsoft.com/dotnet/aspnet:6.0.0
- mcr.microsoft.com/dotnet/aspnet:6.0.0-alpine3.14
- mcr.microsoft.com/dotnet/aspnet:6.0.0-alpine3.14-amd64
- mcr.microsoft.com/dotnet/aspnet:6.0.0-alpine3.14-arm32v7
- mcr.microsoft.com/dotnet/aspnet:6.0.0-alpine3.14-arm64v8
- mcr.microsoft.com/dotnet/aspnet:6.0.0-bullseye-slim
- mcr.microsoft.com/dotnet/aspnet:6.0.0-bullseye-slim-amd64
- mcr.microsoft.com/dotnet/aspnet:6.0.0-bullseye-slim-arm32v7
- mcr.microsoft.com/dotnet/aspnet:6.0.0-bullseye-slim-arm64v8
- mcr.microsoft.com/dotnet/aspnet:6.0.0-focal
- mcr.microsoft.com/dotnet/aspnet:6.0.0-focal-amd64
- mcr.microsoft.com/dotnet/aspnet:6.0.0-focal-arm32v7
- mcr.microsoft.com/dotnet/aspnet:6.0.0-focal-arm64v8
- mcr.microsoft.com/dotnet/aspnet:6.0.0-windowsservercore-ltsc2022
- mcr.microsoft.com/dotnet/aspnet:latest

### server

- mcr.microsoft.com/mssql/server:2017-CU1-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU10-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU11-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU12-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU13-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU14-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU15-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU16-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU17-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU18-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2017-CU19-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2017-CU2-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU20-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2017-CU21-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2017-CU22-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2017-CU23-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2017-CU24-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2017-CU3-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU4-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU5-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU6-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU7-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU8-ubuntu
- mcr.microsoft.com/mssql/server:2017-CU9-ubuntu
- mcr.microsoft.com/mssql/server:2017-GA-ubuntu
- mcr.microsoft.com/mssql/server:2017-GDR-ubuntu
- mcr.microsoft.com/mssql/server:2017-latest
- mcr.microsoft.com/mssql/server:2019-CU1-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2019-CU10-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2019-CU10-ubuntu-18.04
- mcr.microsoft.com/mssql/server:2019-CU10-ubuntu-20.04
- mcr.microsoft.com/mssql/server:2019-CU11-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2019-CU11-ubuntu-18.04
- mcr.microsoft.com/mssql/server:2019-CU11-ubuntu-20.04
- mcr.microsoft.com/mssql/server:2019-CU12-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2019-CU12-ubuntu-18.04
- mcr.microsoft.com/mssql/server:2019-CU12-ubuntu-20.04
- mcr.microsoft.com/mssql/server:2019-CU13-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2019-CU13-ubuntu-18.04
- mcr.microsoft.com/mssql/server:2019-CU13-ubuntu-20.04
- mcr.microsoft.com/mssql/server:2019-CU2-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2019-CU3-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2019-CU3-ubuntu-18.04
- mcr.microsoft.com/mssql/server:2019-CU4-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2019-CU4-ubuntu-18.04
- mcr.microsoft.com/mssql/server:2019-CU5-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2019-CU5-ubuntu-18.04
- mcr.microsoft.com/mssql/server:2019-CU6-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2019-CU6-ubuntu-18.04
- mcr.microsoft.com/mssql/server:2019-CU8-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2019-CU8-ubuntu-18.04
- mcr.microsoft.com/mssql/server:2019-CU9-ubuntu-18.04
- mcr.microsoft.com/mssql/server:2019-GA-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2019-GDR1-ubuntu-16.04
- mcr.microsoft.com/mssql/server:2019-latest
- mcr.microsoft.com/mssql/server:latest

### jdk

- mcr.microsoft.com/java/jdk:11-zulu-alpine
- mcr.microsoft.com/java/jdk:11-zulu-centos
- mcr.microsoft.com/java/jdk:11-zulu-debian10
- mcr.microsoft.com/java/jdk:11-zulu-debian8
- mcr.microsoft.com/java/jdk:11-zulu-debian9
- mcr.microsoft.com/java/jdk:11-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:11-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jdk:11u1-zulu-alpine
- mcr.microsoft.com/java/jdk:11u1-zulu-centos
- mcr.microsoft.com/java/jdk:11u1-zulu-debian8
- mcr.microsoft.com/java/jdk:11u1-zulu-debian9
- mcr.microsoft.com/java/jdk:11u1-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11u10-zulu-alpine
- mcr.microsoft.com/java/jdk:11u10-zulu-centos
- mcr.microsoft.com/java/jdk:11u10-zulu-debian10
- mcr.microsoft.com/java/jdk:11u10-zulu-debian9
- mcr.microsoft.com/java/jdk:11u10-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11u10-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:11u11-zulu-alpine
- mcr.microsoft.com/java/jdk:11u11-zulu-centos
- mcr.microsoft.com/java/jdk:11u11-zulu-debian10
- mcr.microsoft.com/java/jdk:11u11-zulu-debian9
- mcr.microsoft.com/java/jdk:11u11-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11u11-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:11u12-zulu-alpine
- mcr.microsoft.com/java/jdk:11u12-zulu-centos
- mcr.microsoft.com/java/jdk:11u12-zulu-debian10
- mcr.microsoft.com/java/jdk:11u12-zulu-debian9
- mcr.microsoft.com/java/jdk:11u12-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11u12-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:11u13-zulu-alpine
- mcr.microsoft.com/java/jdk:11u13-zulu-centos
- mcr.microsoft.com/java/jdk:11u13-zulu-debian10
- mcr.microsoft.com/java/jdk:11u13-zulu-debian9
- mcr.microsoft.com/java/jdk:11u13-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11u13-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:11u2-zulu-alpine
- mcr.microsoft.com/java/jdk:11u2-zulu-centos
- mcr.microsoft.com/java/jdk:11u2-zulu-debian8
- mcr.microsoft.com/java/jdk:11u2-zulu-debian9
- mcr.microsoft.com/java/jdk:11u2-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11u3-zulu-alpine
- mcr.microsoft.com/java/jdk:11u3-zulu-centos
- mcr.microsoft.com/java/jdk:11u3-zulu-debian8
- mcr.microsoft.com/java/jdk:11u3-zulu-debian9
- mcr.microsoft.com/java/jdk:11u3-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11u4-zulu-alpine
- mcr.microsoft.com/java/jdk:11u4-zulu-centos
- mcr.microsoft.com/java/jdk:11u4-zulu-debian8
- mcr.microsoft.com/java/jdk:11u4-zulu-debian9
- mcr.microsoft.com/java/jdk:11u4-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11u5-zulu-alpine
- mcr.microsoft.com/java/jdk:11u5-zulu-centos
- mcr.microsoft.com/java/jdk:11u5-zulu-debian8
- mcr.microsoft.com/java/jdk:11u5-zulu-debian9
- mcr.microsoft.com/java/jdk:11u5-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11u6-zulu-alpine
- mcr.microsoft.com/java/jdk:11u6-zulu-centos
- mcr.microsoft.com/java/jdk:11u6-zulu-debian10
- mcr.microsoft.com/java/jdk:11u6-zulu-debian8
- mcr.microsoft.com/java/jdk:11u6-zulu-debian9
- mcr.microsoft.com/java/jdk:11u6-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11u7-zulu-alpine
- mcr.microsoft.com/java/jdk:11u7-zulu-centos
- mcr.microsoft.com/java/jdk:11u7-zulu-debian10
- mcr.microsoft.com/java/jdk:11u7-zulu-debian9
- mcr.microsoft.com/java/jdk:11u7-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11u7-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:11u7-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jdk:11u8-zulu-alpine
- mcr.microsoft.com/java/jdk:11u8-zulu-centos
- mcr.microsoft.com/java/jdk:11u8-zulu-debian10
- mcr.microsoft.com/java/jdk:11u8-zulu-debian9
- mcr.microsoft.com/java/jdk:11u8-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11u8-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:11u9-zulu-alpine
- mcr.microsoft.com/java/jdk:11u9-zulu-centos
- mcr.microsoft.com/java/jdk:11u9-zulu-debian10
- mcr.microsoft.com/java/jdk:11u9-zulu-debian9
- mcr.microsoft.com/java/jdk:11u9-zulu-ubuntu
- mcr.microsoft.com/java/jdk:11u9-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:12u1-zulu-debian8
- mcr.microsoft.com/java/jdk:12u1-zulu-debian9
- mcr.microsoft.com/java/jdk:12u1-zulu-ubuntu
- mcr.microsoft.com/java/jdk:12u2-zulu-debian8
- mcr.microsoft.com/java/jdk:12u2-zulu-debian9
- mcr.microsoft.com/java/jdk:12u2-zulu-ubuntu
- mcr.microsoft.com/java/jdk:13-zulu-alpine
- mcr.microsoft.com/java/jdk:13-zulu-centos
- mcr.microsoft.com/java/jdk:13-zulu-debian10
- mcr.microsoft.com/java/jdk:13-zulu-debian8
- mcr.microsoft.com/java/jdk:13-zulu-debian9
- mcr.microsoft.com/java/jdk:13-zulu-ubuntu
- mcr.microsoft.com/java/jdk:13-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:13-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jdk:13u1-zulu-alpine
- mcr.microsoft.com/java/jdk:13u1-zulu-centos
- mcr.microsoft.com/java/jdk:13u1-zulu-debian8
- mcr.microsoft.com/java/jdk:13u1-zulu-debian9
- mcr.microsoft.com/java/jdk:13u1-zulu-ubuntu
- mcr.microsoft.com/java/jdk:13u2-zulu-alpine
- mcr.microsoft.com/java/jdk:13u2-zulu-centos
- mcr.microsoft.com/java/jdk:13u2-zulu-debian8
- mcr.microsoft.com/java/jdk:13u2-zulu-debian9
- mcr.microsoft.com/java/jdk:13u2-zulu-ubuntu
- mcr.microsoft.com/java/jdk:13u3-zulu-alpine
- mcr.microsoft.com/java/jdk:13u3-zulu-centos
- mcr.microsoft.com/java/jdk:13u3-zulu-debian10
- mcr.microsoft.com/java/jdk:13u3-zulu-debian9
- mcr.microsoft.com/java/jdk:13u3-zulu-ubuntu
- mcr.microsoft.com/java/jdk:13u3-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:13u3-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jdk:13u4-zulu-alpine
- mcr.microsoft.com/java/jdk:13u4-zulu-centos
- mcr.microsoft.com/java/jdk:13u4-zulu-debian10
- mcr.microsoft.com/java/jdk:13u4-zulu-debian9
- mcr.microsoft.com/java/jdk:13u4-zulu-ubuntu
- mcr.microsoft.com/java/jdk:13u4-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:13u5-zulu-alpine
- mcr.microsoft.com/java/jdk:13u5-zulu-centos
- mcr.microsoft.com/java/jdk:13u5-zulu-debian10
- mcr.microsoft.com/java/jdk:13u5-zulu-debian9
- mcr.microsoft.com/java/jdk:13u5-zulu-ubuntu
- mcr.microsoft.com/java/jdk:13u5-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:13u6-zulu-alpine
- mcr.microsoft.com/java/jdk:13u6-zulu-centos
- mcr.microsoft.com/java/jdk:13u6-zulu-debian10
- mcr.microsoft.com/java/jdk:13u6-zulu-debian9
- mcr.microsoft.com/java/jdk:13u6-zulu-ubuntu
- mcr.microsoft.com/java/jdk:13u6-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:13u7-zulu-alpine
- mcr.microsoft.com/java/jdk:13u7-zulu-centos
- mcr.microsoft.com/java/jdk:13u7-zulu-debian10
- mcr.microsoft.com/java/jdk:13u7-zulu-debian9
- mcr.microsoft.com/java/jdk:13u7-zulu-ubuntu
- mcr.microsoft.com/java/jdk:13u7-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:13u8-zulu-alpine
- mcr.microsoft.com/java/jdk:13u8-zulu-centos
- mcr.microsoft.com/java/jdk:13u8-zulu-debian10
- mcr.microsoft.com/java/jdk:13u8-zulu-debian9
- mcr.microsoft.com/java/jdk:13u8-zulu-ubuntu
- mcr.microsoft.com/java/jdk:13u8-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:13u9-zulu-alpine
- mcr.microsoft.com/java/jdk:13u9-zulu-centos
- mcr.microsoft.com/java/jdk:13u9-zulu-debian10
- mcr.microsoft.com/java/jdk:13u9-zulu-debian9
- mcr.microsoft.com/java/jdk:13u9-zulu-ubuntu
- mcr.microsoft.com/java/jdk:13u9-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:14-zulu-centos
- mcr.microsoft.com/java/jdk:14-zulu-debian10
- mcr.microsoft.com/java/jdk:14-zulu-debian8
- mcr.microsoft.com/java/jdk:14-zulu-debian9
- mcr.microsoft.com/java/jdk:14-zulu-ubuntu
- mcr.microsoft.com/java/jdk:14-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:14-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jdk:14u0-zulu-centos
- mcr.microsoft.com/java/jdk:14u0-zulu-debian8
- mcr.microsoft.com/java/jdk:14u0-zulu-debian9
- mcr.microsoft.com/java/jdk:14u0-zulu-ubuntu
- mcr.microsoft.com/java/jdk:14u0-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:14u1-zulu-centos
- mcr.microsoft.com/java/jdk:14u1-zulu-debian10
- mcr.microsoft.com/java/jdk:14u1-zulu-debian9
- mcr.microsoft.com/java/jdk:14u1-zulu-ubuntu
- mcr.microsoft.com/java/jdk:14u1-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:14u1-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jdk:14u2-zulu-centos
- mcr.microsoft.com/java/jdk:14u2-zulu-debian10
- mcr.microsoft.com/java/jdk:14u2-zulu-debian9
- mcr.microsoft.com/java/jdk:14u2-zulu-ubuntu
- mcr.microsoft.com/java/jdk:14u2-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:15-zulu-alpine
- mcr.microsoft.com/java/jdk:15-zulu-centos
- mcr.microsoft.com/java/jdk:15-zulu-debian10
- mcr.microsoft.com/java/jdk:15-zulu-debian9
- mcr.microsoft.com/java/jdk:15-zulu-ubuntu
- mcr.microsoft.com/java/jdk:15-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:15u0-zulu-alpine
- mcr.microsoft.com/java/jdk:15u0-zulu-centos
- mcr.microsoft.com/java/jdk:15u0-zulu-debian10
- mcr.microsoft.com/java/jdk:15u0-zulu-debian9
- mcr.microsoft.com/java/jdk:15u0-zulu-ubuntu
- mcr.microsoft.com/java/jdk:15u0-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:15u1-zulu-alpine
- mcr.microsoft.com/java/jdk:15u1-zulu-centos
- mcr.microsoft.com/java/jdk:15u1-zulu-debian10
- mcr.microsoft.com/java/jdk:15u1-zulu-debian9
- mcr.microsoft.com/java/jdk:15u1-zulu-ubuntu
- mcr.microsoft.com/java/jdk:15u1-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:15u2-zulu-alpine
- mcr.microsoft.com/java/jdk:15u2-zulu-centos
- mcr.microsoft.com/java/jdk:15u2-zulu-debian10
- mcr.microsoft.com/java/jdk:15u2-zulu-debian9
- mcr.microsoft.com/java/jdk:15u2-zulu-ubuntu
- mcr.microsoft.com/java/jdk:15u2-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:15u3-zulu-alpine
- mcr.microsoft.com/java/jdk:15u3-zulu-centos
- mcr.microsoft.com/java/jdk:15u3-zulu-debian10
- mcr.microsoft.com/java/jdk:15u3-zulu-debian9
- mcr.microsoft.com/java/jdk:15u3-zulu-ubuntu
- mcr.microsoft.com/java/jdk:15u3-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:15u4-zulu-alpine
- mcr.microsoft.com/java/jdk:15u4-zulu-centos
- mcr.microsoft.com/java/jdk:15u4-zulu-debian10
- mcr.microsoft.com/java/jdk:15u4-zulu-debian9
- mcr.microsoft.com/java/jdk:15u4-zulu-ubuntu
- mcr.microsoft.com/java/jdk:15u4-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:15u5-zulu-alpine
- mcr.microsoft.com/java/jdk:15u5-zulu-centos
- mcr.microsoft.com/java/jdk:15u5-zulu-debian10
- mcr.microsoft.com/java/jdk:15u5-zulu-debian9
- mcr.microsoft.com/java/jdk:15u5-zulu-ubuntu
- mcr.microsoft.com/java/jdk:15u5-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:16-zulu-centos
- mcr.microsoft.com/java/jdk:16-zulu-debian10
- mcr.microsoft.com/java/jdk:16-zulu-debian9
- mcr.microsoft.com/java/jdk:16-zulu-ubuntu
- mcr.microsoft.com/java/jdk:16-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:16u0-zulu-centos
- mcr.microsoft.com/java/jdk:16u0-zulu-debian10
- mcr.microsoft.com/java/jdk:16u0-zulu-debian9
- mcr.microsoft.com/java/jdk:16u0-zulu-ubuntu
- mcr.microsoft.com/java/jdk:16u0-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:16u1-zulu-centos
- mcr.microsoft.com/java/jdk:16u1-zulu-debian10
- mcr.microsoft.com/java/jdk:16u1-zulu-debian9
- mcr.microsoft.com/java/jdk:16u1-zulu-ubuntu
- mcr.microsoft.com/java/jdk:16u1-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:16u2-zulu-centos
- mcr.microsoft.com/java/jdk:16u2-zulu-debian10
- mcr.microsoft.com/java/jdk:16u2-zulu-debian9
- mcr.microsoft.com/java/jdk:16u2-zulu-ubuntu
- mcr.microsoft.com/java/jdk:16u2-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:17-zulu-alpine
- mcr.microsoft.com/java/jdk:17-zulu-centos
- mcr.microsoft.com/java/jdk:17-zulu-debian10
- mcr.microsoft.com/java/jdk:17-zulu-debian9
- mcr.microsoft.com/java/jdk:17-zulu-ubuntu
- mcr.microsoft.com/java/jdk:17-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:17u0-zulu-alpine
- mcr.microsoft.com/java/jdk:17u0-zulu-centos
- mcr.microsoft.com/java/jdk:17u0-zulu-debian10
- mcr.microsoft.com/java/jdk:17u0-zulu-debian9
- mcr.microsoft.com/java/jdk:17u0-zulu-ubuntu
- mcr.microsoft.com/java/jdk:17u0-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:17u1-zulu-alpine
- mcr.microsoft.com/java/jdk:17u1-zulu-centos
- mcr.microsoft.com/java/jdk:17u1-zulu-debian10
- mcr.microsoft.com/java/jdk:17u1-zulu-debian9
- mcr.microsoft.com/java/jdk:17u1-zulu-ubuntu
- mcr.microsoft.com/java/jdk:17u1-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:7-zulu-alpine
- mcr.microsoft.com/java/jdk:7-zulu-centos
- mcr.microsoft.com/java/jdk:7-zulu-debian10
- mcr.microsoft.com/java/jdk:7-zulu-debian8
- mcr.microsoft.com/java/jdk:7-zulu-debian9
- mcr.microsoft.com/java/jdk:7-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:7-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jdk:7u191-zulu-alpine
- mcr.microsoft.com/java/jdk:7u191-zulu-centos
- mcr.microsoft.com/java/jdk:7u191-zulu-debian8
- mcr.microsoft.com/java/jdk:7u191-zulu-debian9
- mcr.microsoft.com/java/jdk:7u191-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u201-zulu-alpine
- mcr.microsoft.com/java/jdk:7u201-zulu-centos
- mcr.microsoft.com/java/jdk:7u201-zulu-debian8
- mcr.microsoft.com/java/jdk:7u201-zulu-debian9
- mcr.microsoft.com/java/jdk:7u201-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u211-zulu-alpine
- mcr.microsoft.com/java/jdk:7u211-zulu-centos
- mcr.microsoft.com/java/jdk:7u211-zulu-debian8
- mcr.microsoft.com/java/jdk:7u211-zulu-debian9
- mcr.microsoft.com/java/jdk:7u211-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u222-zulu-alpine
- mcr.microsoft.com/java/jdk:7u222-zulu-centos
- mcr.microsoft.com/java/jdk:7u222-zulu-debian8
- mcr.microsoft.com/java/jdk:7u222-zulu-debian9
- mcr.microsoft.com/java/jdk:7u222-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u232-zulu-alpine
- mcr.microsoft.com/java/jdk:7u232-zulu-centos
- mcr.microsoft.com/java/jdk:7u232-zulu-debian8
- mcr.microsoft.com/java/jdk:7u232-zulu-debian9
- mcr.microsoft.com/java/jdk:7u232-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u242-zulu-alpine
- mcr.microsoft.com/java/jdk:7u242-zulu-centos
- mcr.microsoft.com/java/jdk:7u242-zulu-debian8
- mcr.microsoft.com/java/jdk:7u242-zulu-debian9
- mcr.microsoft.com/java/jdk:7u242-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u252-zulu-alpine
- mcr.microsoft.com/java/jdk:7u252-zulu-centos
- mcr.microsoft.com/java/jdk:7u252-zulu-debian8
- mcr.microsoft.com/java/jdk:7u252-zulu-debian9
- mcr.microsoft.com/java/jdk:7u252-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u262-zulu-alpine
- mcr.microsoft.com/java/jdk:7u262-zulu-centos
- mcr.microsoft.com/java/jdk:7u262-zulu-debian10
- mcr.microsoft.com/java/jdk:7u262-zulu-debian9
- mcr.microsoft.com/java/jdk:7u262-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u262-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:7u262-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jdk:7u272-zulu-alpine
- mcr.microsoft.com/java/jdk:7u272-zulu-centos
- mcr.microsoft.com/java/jdk:7u272-zulu-debian10
- mcr.microsoft.com/java/jdk:7u272-zulu-debian9
- mcr.microsoft.com/java/jdk:7u272-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u272-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:7u282-zulu-alpine
- mcr.microsoft.com/java/jdk:7u282-zulu-centos
- mcr.microsoft.com/java/jdk:7u282-zulu-debian10
- mcr.microsoft.com/java/jdk:7u282-zulu-debian9
- mcr.microsoft.com/java/jdk:7u282-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u282-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:7u285-zulu-alpine
- mcr.microsoft.com/java/jdk:7u285-zulu-centos
- mcr.microsoft.com/java/jdk:7u285-zulu-debian10
- mcr.microsoft.com/java/jdk:7u285-zulu-debian9
- mcr.microsoft.com/java/jdk:7u285-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u285-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:7u292-zulu-alpine
- mcr.microsoft.com/java/jdk:7u292-zulu-centos
- mcr.microsoft.com/java/jdk:7u292-zulu-debian10
- mcr.microsoft.com/java/jdk:7u292-zulu-debian9
- mcr.microsoft.com/java/jdk:7u292-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u292-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:7u302-zulu-alpine
- mcr.microsoft.com/java/jdk:7u302-zulu-centos
- mcr.microsoft.com/java/jdk:7u302-zulu-debian10
- mcr.microsoft.com/java/jdk:7u302-zulu-debian9
- mcr.microsoft.com/java/jdk:7u302-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u302-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:7u312-zulu-alpine
- mcr.microsoft.com/java/jdk:7u312-zulu-centos
- mcr.microsoft.com/java/jdk:7u312-zulu-debian10
- mcr.microsoft.com/java/jdk:7u312-zulu-debian9
- mcr.microsoft.com/java/jdk:7u312-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u312-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:7u322-zulu-alpine
- mcr.microsoft.com/java/jdk:7u322-zulu-centos
- mcr.microsoft.com/java/jdk:7u322-zulu-debian10
- mcr.microsoft.com/java/jdk:7u322-zulu-debian9
- mcr.microsoft.com/java/jdk:7u322-zulu-ubuntu
- mcr.microsoft.com/java/jdk:7u322-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:8-zulu-alpine
- mcr.microsoft.com/java/jdk:8-zulu-centos
- mcr.microsoft.com/java/jdk:8-zulu-debian10
- mcr.microsoft.com/java/jdk:8-zulu-debian8
- mcr.microsoft.com/java/jdk:8-zulu-debian9
- mcr.microsoft.com/java/jdk:8-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:8-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jdk:8u181-zulu-alpine
- mcr.microsoft.com/java/jdk:8u181-zulu-centos
- mcr.microsoft.com/java/jdk:8u181-zulu-debian8
- mcr.microsoft.com/java/jdk:8u181-zulu-debian9
- mcr.microsoft.com/java/jdk:8u181-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u192-zulu-alpine
- mcr.microsoft.com/java/jdk:8u192-zulu-centos
- mcr.microsoft.com/java/jdk:8u192-zulu-debian8
- mcr.microsoft.com/java/jdk:8u192-zulu-debian9
- mcr.microsoft.com/java/jdk:8u192-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u202-zulu-alpine
- mcr.microsoft.com/java/jdk:8u202-zulu-centos
- mcr.microsoft.com/java/jdk:8u202-zulu-debian8
- mcr.microsoft.com/java/jdk:8u202-zulu-debian9
- mcr.microsoft.com/java/jdk:8u202-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u212-zulu-alpine
- mcr.microsoft.com/java/jdk:8u212-zulu-centos
- mcr.microsoft.com/java/jdk:8u212-zulu-debian8
- mcr.microsoft.com/java/jdk:8u212-zulu-debian9
- mcr.microsoft.com/java/jdk:8u212-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u222-zulu-alpine
- mcr.microsoft.com/java/jdk:8u222-zulu-centos
- mcr.microsoft.com/java/jdk:8u222-zulu-debian8
- mcr.microsoft.com/java/jdk:8u222-zulu-debian9
- mcr.microsoft.com/java/jdk:8u222-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u232-zulu-alpine
- mcr.microsoft.com/java/jdk:8u232-zulu-centos
- mcr.microsoft.com/java/jdk:8u232-zulu-debian8
- mcr.microsoft.com/java/jdk:8u232-zulu-debian9
- mcr.microsoft.com/java/jdk:8u232-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u232-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:8u242-zulu-alpine
- mcr.microsoft.com/java/jdk:8u242-zulu-centos
- mcr.microsoft.com/java/jdk:8u242-zulu-debian10
- mcr.microsoft.com/java/jdk:8u242-zulu-debian8
- mcr.microsoft.com/java/jdk:8u242-zulu-debian9
- mcr.microsoft.com/java/jdk:8u242-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u242-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:8u252-zulu-alpine
- mcr.microsoft.com/java/jdk:8u252-zulu-centos
- mcr.microsoft.com/java/jdk:8u252-zulu-debian10
- mcr.microsoft.com/java/jdk:8u252-zulu-debian9
- mcr.microsoft.com/java/jdk:8u252-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u252-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:8u252-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jdk:8u262-zulu-alpine
- mcr.microsoft.com/java/jdk:8u262-zulu-centos
- mcr.microsoft.com/java/jdk:8u262-zulu-debian10
- mcr.microsoft.com/java/jdk:8u262-zulu-debian9
- mcr.microsoft.com/java/jdk:8u262-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u262-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:8u265-zulu-alpine
- mcr.microsoft.com/java/jdk:8u265-zulu-centos
- mcr.microsoft.com/java/jdk:8u265-zulu-debian10
- mcr.microsoft.com/java/jdk:8u265-zulu-debian9
- mcr.microsoft.com/java/jdk:8u265-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u265-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:8u272-zulu-alpine
- mcr.microsoft.com/java/jdk:8u272-zulu-centos
- mcr.microsoft.com/java/jdk:8u272-zulu-debian10
- mcr.microsoft.com/java/jdk:8u272-zulu-debian9
- mcr.microsoft.com/java/jdk:8u272-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u272-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:8u275-zulu-alpine
- mcr.microsoft.com/java/jdk:8u275-zulu-centos
- mcr.microsoft.com/java/jdk:8u275-zulu-debian10
- mcr.microsoft.com/java/jdk:8u275-zulu-debian9
- mcr.microsoft.com/java/jdk:8u275-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u275-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:8u282-zulu-alpine
- mcr.microsoft.com/java/jdk:8u282-zulu-centos
- mcr.microsoft.com/java/jdk:8u282-zulu-debian10
- mcr.microsoft.com/java/jdk:8u282-zulu-debian9
- mcr.microsoft.com/java/jdk:8u282-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u282-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:8u292-zulu-alpine
- mcr.microsoft.com/java/jdk:8u292-zulu-centos
- mcr.microsoft.com/java/jdk:8u292-zulu-debian10
- mcr.microsoft.com/java/jdk:8u292-zulu-debian9
- mcr.microsoft.com/java/jdk:8u292-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u292-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:8u302-zulu-alpine
- mcr.microsoft.com/java/jdk:8u302-zulu-centos
- mcr.microsoft.com/java/jdk:8u302-zulu-debian10
- mcr.microsoft.com/java/jdk:8u302-zulu-debian9
- mcr.microsoft.com/java/jdk:8u302-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u302-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jdk:8u312-zulu-alpine
- mcr.microsoft.com/java/jdk:8u312-zulu-centos
- mcr.microsoft.com/java/jdk:8u312-zulu-debian10
- mcr.microsoft.com/java/jdk:8u312-zulu-debian9
- mcr.microsoft.com/java/jdk:8u312-zulu-ubuntu
- mcr.microsoft.com/java/jdk:8u312-zulu-ubuntu-18.04

### jre

- mcr.microsoft.com/java/jre:11-zulu-alpine
- mcr.microsoft.com/java/jre:11-zulu-centos
- mcr.microsoft.com/java/jre:11-zulu-debian10
- mcr.microsoft.com/java/jre:11-zulu-debian8
- mcr.microsoft.com/java/jre:11-zulu-debian9
- mcr.microsoft.com/java/jre:11-zulu-ubuntu
- mcr.microsoft.com/java/jre:11-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:11-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jre:11u1-zulu-alpine
- mcr.microsoft.com/java/jre:11u1-zulu-centos
- mcr.microsoft.com/java/jre:11u1-zulu-debian8
- mcr.microsoft.com/java/jre:11u1-zulu-debian9
- mcr.microsoft.com/java/jre:11u1-zulu-ubuntu
- mcr.microsoft.com/java/jre:11u10-zulu-alpine
- mcr.microsoft.com/java/jre:11u10-zulu-centos
- mcr.microsoft.com/java/jre:11u10-zulu-debian10
- mcr.microsoft.com/java/jre:11u10-zulu-debian9
- mcr.microsoft.com/java/jre:11u10-zulu-ubuntu
- mcr.microsoft.com/java/jre:11u10-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:11u11-zulu-alpine
- mcr.microsoft.com/java/jre:11u11-zulu-centos
- mcr.microsoft.com/java/jre:11u11-zulu-debian10
- mcr.microsoft.com/java/jre:11u11-zulu-debian9
- mcr.microsoft.com/java/jre:11u11-zulu-ubuntu
- mcr.microsoft.com/java/jre:11u11-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:11u12-zulu-alpine
- mcr.microsoft.com/java/jre:11u12-zulu-centos
- mcr.microsoft.com/java/jre:11u12-zulu-debian10
- mcr.microsoft.com/java/jre:11u12-zulu-debian9
- mcr.microsoft.com/java/jre:11u12-zulu-ubuntu
- mcr.microsoft.com/java/jre:11u12-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:11u13-zulu-alpine
- mcr.microsoft.com/java/jre:11u13-zulu-centos
- mcr.microsoft.com/java/jre:11u13-zulu-debian10
- mcr.microsoft.com/java/jre:11u13-zulu-debian9
- mcr.microsoft.com/java/jre:11u13-zulu-ubuntu
- mcr.microsoft.com/java/jre:11u13-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:11u2-zulu-alpine
- mcr.microsoft.com/java/jre:11u2-zulu-centos
- mcr.microsoft.com/java/jre:11u2-zulu-debian8
- mcr.microsoft.com/java/jre:11u2-zulu-debian9
- mcr.microsoft.com/java/jre:11u2-zulu-ubuntu
- mcr.microsoft.com/java/jre:11u3-zulu-alpine
- mcr.microsoft.com/java/jre:11u3-zulu-centos
- mcr.microsoft.com/java/jre:11u3-zulu-debian8
- mcr.microsoft.com/java/jre:11u3-zulu-debian9
- mcr.microsoft.com/java/jre:11u3-zulu-ubuntu
- mcr.microsoft.com/java/jre:11u4-zulu-alpine
- mcr.microsoft.com/java/jre:11u4-zulu-centos
- mcr.microsoft.com/java/jre:11u4-zulu-debian8
- mcr.microsoft.com/java/jre:11u4-zulu-debian9
- mcr.microsoft.com/java/jre:11u4-zulu-ubuntu
- mcr.microsoft.com/java/jre:11u5-zulu-alpine
- mcr.microsoft.com/java/jre:11u5-zulu-centos
- mcr.microsoft.com/java/jre:11u5-zulu-debian8
- mcr.microsoft.com/java/jre:11u5-zulu-debian9
- mcr.microsoft.com/java/jre:11u5-zulu-ubuntu
- mcr.microsoft.com/java/jre:11u6-zulu-alpine
- mcr.microsoft.com/java/jre:11u6-zulu-centos
- mcr.microsoft.com/java/jre:11u6-zulu-debian10
- mcr.microsoft.com/java/jre:11u6-zulu-debian8
- mcr.microsoft.com/java/jre:11u6-zulu-debian9
- mcr.microsoft.com/java/jre:11u6-zulu-ubuntu
- mcr.microsoft.com/java/jre:11u7-zulu-alpine
- mcr.microsoft.com/java/jre:11u7-zulu-centos
- mcr.microsoft.com/java/jre:11u7-zulu-debian10
- mcr.microsoft.com/java/jre:11u7-zulu-debian9
- mcr.microsoft.com/java/jre:11u7-zulu-ubuntu
- mcr.microsoft.com/java/jre:11u7-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:11u7-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jre:11u8-zulu-alpine
- mcr.microsoft.com/java/jre:11u8-zulu-centos
- mcr.microsoft.com/java/jre:11u8-zulu-debian10
- mcr.microsoft.com/java/jre:11u8-zulu-debian9
- mcr.microsoft.com/java/jre:11u8-zulu-ubuntu
- mcr.microsoft.com/java/jre:11u8-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:11u9-zulu-alpine
- mcr.microsoft.com/java/jre:11u9-zulu-centos
- mcr.microsoft.com/java/jre:11u9-zulu-debian10
- mcr.microsoft.com/java/jre:11u9-zulu-debian9
- mcr.microsoft.com/java/jre:11u9-zulu-ubuntu
- mcr.microsoft.com/java/jre:11u9-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:12u1-zulu-debian8
- mcr.microsoft.com/java/jre:12u1-zulu-debian9
- mcr.microsoft.com/java/jre:12u1-zulu-ubuntu
- mcr.microsoft.com/java/jre:12u2-zulu-debian8
- mcr.microsoft.com/java/jre:12u2-zulu-debian9
- mcr.microsoft.com/java/jre:12u2-zulu-ubuntu
- mcr.microsoft.com/java/jre:13-zulu-alpine
- mcr.microsoft.com/java/jre:13-zulu-centos
- mcr.microsoft.com/java/jre:13-zulu-debian10
- mcr.microsoft.com/java/jre:13-zulu-debian8
- mcr.microsoft.com/java/jre:13-zulu-debian9
- mcr.microsoft.com/java/jre:13-zulu-ubuntu
- mcr.microsoft.com/java/jre:13-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:13-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jre:13u1-zulu-alpine
- mcr.microsoft.com/java/jre:13u1-zulu-centos
- mcr.microsoft.com/java/jre:13u1-zulu-debian8
- mcr.microsoft.com/java/jre:13u1-zulu-debian9
- mcr.microsoft.com/java/jre:13u1-zulu-ubuntu
- mcr.microsoft.com/java/jre:13u2-zulu-alpine
- mcr.microsoft.com/java/jre:13u2-zulu-centos
- mcr.microsoft.com/java/jre:13u2-zulu-debian8
- mcr.microsoft.com/java/jre:13u2-zulu-debian9
- mcr.microsoft.com/java/jre:13u2-zulu-ubuntu
- mcr.microsoft.com/java/jre:13u3-zulu-alpine
- mcr.microsoft.com/java/jre:13u3-zulu-centos
- mcr.microsoft.com/java/jre:13u3-zulu-debian10
- mcr.microsoft.com/java/jre:13u3-zulu-debian9
- mcr.microsoft.com/java/jre:13u3-zulu-ubuntu
- mcr.microsoft.com/java/jre:13u3-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:13u3-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jre:13u4-zulu-alpine
- mcr.microsoft.com/java/jre:13u4-zulu-centos
- mcr.microsoft.com/java/jre:13u4-zulu-debian10
- mcr.microsoft.com/java/jre:13u4-zulu-debian9
- mcr.microsoft.com/java/jre:13u4-zulu-ubuntu
- mcr.microsoft.com/java/jre:13u4-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:13u5-zulu-alpine
- mcr.microsoft.com/java/jre:13u5-zulu-centos
- mcr.microsoft.com/java/jre:13u5-zulu-debian10
- mcr.microsoft.com/java/jre:13u5-zulu-debian9
- mcr.microsoft.com/java/jre:13u5-zulu-ubuntu
- mcr.microsoft.com/java/jre:13u5-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:13u6-zulu-alpine
- mcr.microsoft.com/java/jre:13u6-zulu-centos
- mcr.microsoft.com/java/jre:13u6-zulu-debian10
- mcr.microsoft.com/java/jre:13u6-zulu-debian9
- mcr.microsoft.com/java/jre:13u6-zulu-ubuntu
- mcr.microsoft.com/java/jre:13u6-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:13u7-zulu-alpine
- mcr.microsoft.com/java/jre:13u7-zulu-centos
- mcr.microsoft.com/java/jre:13u7-zulu-debian10
- mcr.microsoft.com/java/jre:13u7-zulu-debian9
- mcr.microsoft.com/java/jre:13u7-zulu-ubuntu
- mcr.microsoft.com/java/jre:13u7-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:13u8-zulu-alpine
- mcr.microsoft.com/java/jre:13u8-zulu-centos
- mcr.microsoft.com/java/jre:13u8-zulu-debian10
- mcr.microsoft.com/java/jre:13u8-zulu-debian9
- mcr.microsoft.com/java/jre:13u8-zulu-ubuntu
- mcr.microsoft.com/java/jre:13u8-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:13u9-zulu-alpine
- mcr.microsoft.com/java/jre:13u9-zulu-centos
- mcr.microsoft.com/java/jre:13u9-zulu-debian10
- mcr.microsoft.com/java/jre:13u9-zulu-debian9
- mcr.microsoft.com/java/jre:13u9-zulu-ubuntu
- mcr.microsoft.com/java/jre:13u9-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:14-zulu-centos
- mcr.microsoft.com/java/jre:14-zulu-debian10
- mcr.microsoft.com/java/jre:14-zulu-debian8
- mcr.microsoft.com/java/jre:14-zulu-debian9
- mcr.microsoft.com/java/jre:14-zulu-ubuntu
- mcr.microsoft.com/java/jre:14-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:14-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jre:14u0-zulu-centos
- mcr.microsoft.com/java/jre:14u0-zulu-debian8
- mcr.microsoft.com/java/jre:14u0-zulu-debian9
- mcr.microsoft.com/java/jre:14u0-zulu-ubuntu
- mcr.microsoft.com/java/jre:14u0-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:14u1-zulu-centos
- mcr.microsoft.com/java/jre:14u1-zulu-debian10
- mcr.microsoft.com/java/jre:14u1-zulu-debian9
- mcr.microsoft.com/java/jre:14u1-zulu-ubuntu
- mcr.microsoft.com/java/jre:14u1-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:14u1-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jre:14u2-zulu-centos
- mcr.microsoft.com/java/jre:14u2-zulu-debian10
- mcr.microsoft.com/java/jre:14u2-zulu-debian9
- mcr.microsoft.com/java/jre:14u2-zulu-ubuntu
- mcr.microsoft.com/java/jre:14u2-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:15-zulu-alpine
- mcr.microsoft.com/java/jre:15-zulu-centos
- mcr.microsoft.com/java/jre:15-zulu-debian10
- mcr.microsoft.com/java/jre:15-zulu-debian9
- mcr.microsoft.com/java/jre:15-zulu-ubuntu
- mcr.microsoft.com/java/jre:15-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:15u0-zulu-alpine
- mcr.microsoft.com/java/jre:15u0-zulu-centos
- mcr.microsoft.com/java/jre:15u0-zulu-debian10
- mcr.microsoft.com/java/jre:15u0-zulu-debian9
- mcr.microsoft.com/java/jre:15u0-zulu-ubuntu
- mcr.microsoft.com/java/jre:15u0-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:15u1-zulu-alpine
- mcr.microsoft.com/java/jre:15u1-zulu-centos
- mcr.microsoft.com/java/jre:15u1-zulu-debian10
- mcr.microsoft.com/java/jre:15u1-zulu-debian9
- mcr.microsoft.com/java/jre:15u1-zulu-ubuntu
- mcr.microsoft.com/java/jre:15u1-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:15u2-zulu-alpine
- mcr.microsoft.com/java/jre:15u2-zulu-centos
- mcr.microsoft.com/java/jre:15u2-zulu-debian10
- mcr.microsoft.com/java/jre:15u2-zulu-debian9
- mcr.microsoft.com/java/jre:15u2-zulu-ubuntu
- mcr.microsoft.com/java/jre:15u2-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:15u3-zulu-alpine
- mcr.microsoft.com/java/jre:15u3-zulu-centos
- mcr.microsoft.com/java/jre:15u3-zulu-debian10
- mcr.microsoft.com/java/jre:15u3-zulu-debian9
- mcr.microsoft.com/java/jre:15u3-zulu-ubuntu
- mcr.microsoft.com/java/jre:15u3-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:15u4-zulu-alpine
- mcr.microsoft.com/java/jre:15u4-zulu-centos
- mcr.microsoft.com/java/jre:15u4-zulu-debian10
- mcr.microsoft.com/java/jre:15u4-zulu-debian9
- mcr.microsoft.com/java/jre:15u4-zulu-ubuntu
- mcr.microsoft.com/java/jre:15u4-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:15u5-zulu-alpine
- mcr.microsoft.com/java/jre:15u5-zulu-centos
- mcr.microsoft.com/java/jre:15u5-zulu-debian10
- mcr.microsoft.com/java/jre:15u5-zulu-debian9
- mcr.microsoft.com/java/jre:15u5-zulu-ubuntu
- mcr.microsoft.com/java/jre:15u5-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:16-zulu-centos
- mcr.microsoft.com/java/jre:16-zulu-debian10
- mcr.microsoft.com/java/jre:16-zulu-debian9
- mcr.microsoft.com/java/jre:16-zulu-ubuntu
- mcr.microsoft.com/java/jre:16-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:16u0-zulu-centos
- mcr.microsoft.com/java/jre:16u0-zulu-debian10
- mcr.microsoft.com/java/jre:16u0-zulu-debian9
- mcr.microsoft.com/java/jre:16u0-zulu-ubuntu
- mcr.microsoft.com/java/jre:16u0-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:16u1-zulu-centos
- mcr.microsoft.com/java/jre:16u1-zulu-debian10
- mcr.microsoft.com/java/jre:16u1-zulu-debian9
- mcr.microsoft.com/java/jre:16u1-zulu-ubuntu
- mcr.microsoft.com/java/jre:16u1-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:16u2-zulu-centos
- mcr.microsoft.com/java/jre:16u2-zulu-debian10
- mcr.microsoft.com/java/jre:16u2-zulu-debian9
- mcr.microsoft.com/java/jre:16u2-zulu-ubuntu
- mcr.microsoft.com/java/jre:16u2-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:17-zulu-alpine
- mcr.microsoft.com/java/jre:17-zulu-centos
- mcr.microsoft.com/java/jre:17-zulu-debian10
- mcr.microsoft.com/java/jre:17-zulu-debian9
- mcr.microsoft.com/java/jre:17-zulu-ubuntu
- mcr.microsoft.com/java/jre:17-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:17u0-zulu-alpine
- mcr.microsoft.com/java/jre:17u0-zulu-centos
- mcr.microsoft.com/java/jre:17u0-zulu-debian10
- mcr.microsoft.com/java/jre:17u0-zulu-debian9
- mcr.microsoft.com/java/jre:17u0-zulu-ubuntu
- mcr.microsoft.com/java/jre:17u0-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:17u1-zulu-alpine
- mcr.microsoft.com/java/jre:17u1-zulu-centos
- mcr.microsoft.com/java/jre:17u1-zulu-debian10
- mcr.microsoft.com/java/jre:17u1-zulu-debian9
- mcr.microsoft.com/java/jre:17u1-zulu-ubuntu
- mcr.microsoft.com/java/jre:17u1-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:7-zulu-alpine
- mcr.microsoft.com/java/jre:7-zulu-centos
- mcr.microsoft.com/java/jre:7-zulu-debian10
- mcr.microsoft.com/java/jre:7-zulu-debian8
- mcr.microsoft.com/java/jre:7-zulu-debian9
- mcr.microsoft.com/java/jre:7-zulu-ubuntu
- mcr.microsoft.com/java/jre:7-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:7-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jre:7u191-zulu-alpine
- mcr.microsoft.com/java/jre:7u191-zulu-centos
- mcr.microsoft.com/java/jre:7u191-zulu-debian8
- mcr.microsoft.com/java/jre:7u191-zulu-debian9
- mcr.microsoft.com/java/jre:7u191-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u201-zulu-alpine
- mcr.microsoft.com/java/jre:7u201-zulu-centos
- mcr.microsoft.com/java/jre:7u201-zulu-debian8
- mcr.microsoft.com/java/jre:7u201-zulu-debian9
- mcr.microsoft.com/java/jre:7u201-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u211-zulu-alpine
- mcr.microsoft.com/java/jre:7u211-zulu-centos
- mcr.microsoft.com/java/jre:7u211-zulu-debian8
- mcr.microsoft.com/java/jre:7u211-zulu-debian9
- mcr.microsoft.com/java/jre:7u211-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u222-zulu-alpine
- mcr.microsoft.com/java/jre:7u222-zulu-centos
- mcr.microsoft.com/java/jre:7u222-zulu-debian8
- mcr.microsoft.com/java/jre:7u222-zulu-debian9
- mcr.microsoft.com/java/jre:7u222-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u232-zulu-alpine
- mcr.microsoft.com/java/jre:7u232-zulu-centos
- mcr.microsoft.com/java/jre:7u232-zulu-debian8
- mcr.microsoft.com/java/jre:7u232-zulu-debian9
- mcr.microsoft.com/java/jre:7u232-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u242-zulu-alpine
- mcr.microsoft.com/java/jre:7u242-zulu-centos
- mcr.microsoft.com/java/jre:7u242-zulu-debian8
- mcr.microsoft.com/java/jre:7u242-zulu-debian9
- mcr.microsoft.com/java/jre:7u242-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u252-zulu-alpine
- mcr.microsoft.com/java/jre:7u252-zulu-centos
- mcr.microsoft.com/java/jre:7u252-zulu-debian8
- mcr.microsoft.com/java/jre:7u252-zulu-debian9
- mcr.microsoft.com/java/jre:7u252-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u262-zulu-alpine
- mcr.microsoft.com/java/jre:7u262-zulu-centos
- mcr.microsoft.com/java/jre:7u262-zulu-debian10
- mcr.microsoft.com/java/jre:7u262-zulu-debian9
- mcr.microsoft.com/java/jre:7u262-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u262-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:7u262-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jre:7u272-zulu-alpine
- mcr.microsoft.com/java/jre:7u272-zulu-centos
- mcr.microsoft.com/java/jre:7u272-zulu-debian10
- mcr.microsoft.com/java/jre:7u272-zulu-debian9
- mcr.microsoft.com/java/jre:7u272-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u272-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:7u282-zulu-alpine
- mcr.microsoft.com/java/jre:7u282-zulu-centos
- mcr.microsoft.com/java/jre:7u282-zulu-debian10
- mcr.microsoft.com/java/jre:7u282-zulu-debian9
- mcr.microsoft.com/java/jre:7u282-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u282-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:7u285-zulu-alpine
- mcr.microsoft.com/java/jre:7u285-zulu-centos
- mcr.microsoft.com/java/jre:7u285-zulu-debian10
- mcr.microsoft.com/java/jre:7u285-zulu-debian9
- mcr.microsoft.com/java/jre:7u285-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u285-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:7u292-zulu-alpine
- mcr.microsoft.com/java/jre:7u292-zulu-centos
- mcr.microsoft.com/java/jre:7u292-zulu-debian10
- mcr.microsoft.com/java/jre:7u292-zulu-debian9
- mcr.microsoft.com/java/jre:7u292-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u292-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:7u302-zulu-alpine
- mcr.microsoft.com/java/jre:7u302-zulu-centos
- mcr.microsoft.com/java/jre:7u302-zulu-debian10
- mcr.microsoft.com/java/jre:7u302-zulu-debian9
- mcr.microsoft.com/java/jre:7u302-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u302-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:7u312-zulu-alpine
- mcr.microsoft.com/java/jre:7u312-zulu-centos
- mcr.microsoft.com/java/jre:7u312-zulu-debian10
- mcr.microsoft.com/java/jre:7u312-zulu-debian9
- mcr.microsoft.com/java/jre:7u312-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u312-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:7u322-zulu-alpine
- mcr.microsoft.com/java/jre:7u322-zulu-centos
- mcr.microsoft.com/java/jre:7u322-zulu-debian10
- mcr.microsoft.com/java/jre:7u322-zulu-debian9
- mcr.microsoft.com/java/jre:7u322-zulu-ubuntu
- mcr.microsoft.com/java/jre:7u322-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:8-zulu-alpine
- mcr.microsoft.com/java/jre:8-zulu-centos
- mcr.microsoft.com/java/jre:8-zulu-debian10
- mcr.microsoft.com/java/jre:8-zulu-debian8
- mcr.microsoft.com/java/jre:8-zulu-debian9
- mcr.microsoft.com/java/jre:8-zulu-ubuntu
- mcr.microsoft.com/java/jre:8-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:8-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jre:8u181-zulu-alpine
- mcr.microsoft.com/java/jre:8u181-zulu-centos
- mcr.microsoft.com/java/jre:8u181-zulu-debian8
- mcr.microsoft.com/java/jre:8u181-zulu-debian9
- mcr.microsoft.com/java/jre:8u181-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u192-zulu-alpine
- mcr.microsoft.com/java/jre:8u192-zulu-centos
- mcr.microsoft.com/java/jre:8u192-zulu-debian8
- mcr.microsoft.com/java/jre:8u192-zulu-debian9
- mcr.microsoft.com/java/jre:8u192-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u202-zulu-alpine
- mcr.microsoft.com/java/jre:8u202-zulu-centos
- mcr.microsoft.com/java/jre:8u202-zulu-debian8
- mcr.microsoft.com/java/jre:8u202-zulu-debian9
- mcr.microsoft.com/java/jre:8u202-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u212-zulu-alpine
- mcr.microsoft.com/java/jre:8u212-zulu-centos
- mcr.microsoft.com/java/jre:8u212-zulu-debian8
- mcr.microsoft.com/java/jre:8u212-zulu-debian9
- mcr.microsoft.com/java/jre:8u212-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u222-zulu-alpine
- mcr.microsoft.com/java/jre:8u222-zulu-centos
- mcr.microsoft.com/java/jre:8u222-zulu-debian8
- mcr.microsoft.com/java/jre:8u222-zulu-debian9
- mcr.microsoft.com/java/jre:8u222-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u232-zulu-alpine
- mcr.microsoft.com/java/jre:8u232-zulu-centos
- mcr.microsoft.com/java/jre:8u232-zulu-debian8
- mcr.microsoft.com/java/jre:8u232-zulu-debian9
- mcr.microsoft.com/java/jre:8u232-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u232-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:8u242-zulu-alpine
- mcr.microsoft.com/java/jre:8u242-zulu-centos
- mcr.microsoft.com/java/jre:8u242-zulu-debian10
- mcr.microsoft.com/java/jre:8u242-zulu-debian8
- mcr.microsoft.com/java/jre:8u242-zulu-debian9
- mcr.microsoft.com/java/jre:8u242-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u242-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:8u252-zulu-alpine
- mcr.microsoft.com/java/jre:8u252-zulu-centos
- mcr.microsoft.com/java/jre:8u252-zulu-debian10
- mcr.microsoft.com/java/jre:8u252-zulu-debian9
- mcr.microsoft.com/java/jre:8u252-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u252-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:8u252-zulu-ubuntu-19.10
- mcr.microsoft.com/java/jre:8u262-zulu-alpine
- mcr.microsoft.com/java/jre:8u262-zulu-centos
- mcr.microsoft.com/java/jre:8u262-zulu-debian10
- mcr.microsoft.com/java/jre:8u262-zulu-debian9
- mcr.microsoft.com/java/jre:8u262-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u262-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:8u265-zulu-alpine
- mcr.microsoft.com/java/jre:8u265-zulu-centos
- mcr.microsoft.com/java/jre:8u265-zulu-debian10
- mcr.microsoft.com/java/jre:8u265-zulu-debian9
- mcr.microsoft.com/java/jre:8u265-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u265-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:8u272-zulu-alpine
- mcr.microsoft.com/java/jre:8u272-zulu-centos
- mcr.microsoft.com/java/jre:8u272-zulu-debian10
- mcr.microsoft.com/java/jre:8u272-zulu-debian9
- mcr.microsoft.com/java/jre:8u272-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u272-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:8u275-zulu-alpine
- mcr.microsoft.com/java/jre:8u275-zulu-centos
- mcr.microsoft.com/java/jre:8u275-zulu-debian10
- mcr.microsoft.com/java/jre:8u275-zulu-debian9
- mcr.microsoft.com/java/jre:8u275-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u275-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:8u282-zulu-alpine
- mcr.microsoft.com/java/jre:8u282-zulu-centos
- mcr.microsoft.com/java/jre:8u282-zulu-debian10
- mcr.microsoft.com/java/jre:8u282-zulu-debian9
- mcr.microsoft.com/java/jre:8u282-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u282-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:8u292-zulu-alpine
- mcr.microsoft.com/java/jre:8u292-zulu-centos
- mcr.microsoft.com/java/jre:8u292-zulu-debian10
- mcr.microsoft.com/java/jre:8u292-zulu-debian9
- mcr.microsoft.com/java/jre:8u292-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u292-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:8u302-zulu-alpine
- mcr.microsoft.com/java/jre:8u302-zulu-centos
- mcr.microsoft.com/java/jre:8u302-zulu-debian10
- mcr.microsoft.com/java/jre:8u302-zulu-debian9
- mcr.microsoft.com/java/jre:8u302-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u302-zulu-ubuntu-18.04
- mcr.microsoft.com/java/jre:8u312-zulu-alpine
- mcr.microsoft.com/java/jre:8u312-zulu-centos
- mcr.microsoft.com/java/jre:8u312-zulu-debian10
- mcr.microsoft.com/java/jre:8u312-zulu-debian9
- mcr.microsoft.com/java/jre:8u312-zulu-ubuntu
- mcr.microsoft.com/java/jre:8u312-zulu-ubuntu-18.04

### windows

- mcr.microsoft.com/windows:10.0.17763.2300
- mcr.microsoft.com/windows:10.0.17763.2300-amd64
- mcr.microsoft.com/windows:10.0.18363.1556
- mcr.microsoft.com/windows:10.0.18363.1556-amd64
- mcr.microsoft.com/windows:10.0.19041.1348
- mcr.microsoft.com/windows:10.0.19041.1348-amd64
- mcr.microsoft.com/windows:10.0.19042.1348
- mcr.microsoft.com/windows:10.0.19042.1348-amd64
- mcr.microsoft.com/windows:1809
- mcr.microsoft.com/windows:1809-amd64
- mcr.microsoft.com/windows:1809-KB5007206
- mcr.microsoft.com/windows:1809-KB5007206-amd64
- mcr.microsoft.com/windows:1909
- mcr.microsoft.com/windows:1909-amd64
- mcr.microsoft.com/windows:1909-KB5003169
- mcr.microsoft.com/windows:1909-KB5003169-amd64
- mcr.microsoft.com/windows:2004
- mcr.microsoft.com/windows:2004-amd64
- mcr.microsoft.com/windows:2004-KB5007186
- mcr.microsoft.com/windows:2004-KB5007186-amd64
- mcr.microsoft.com/windows:20H2
- mcr.microsoft.com/windows:20H2-amd64
- mcr.microsoft.com/windows:20H2-KB5007186
- mcr.microsoft.com/windows:20H2-KB5007186-amd64

### vscode_base

- mcr.microsoft.com/vscode/devcontainers/base:0-alpine
- mcr.microsoft.com/vscode/devcontainers/base:0-alpine-3.10
- mcr.microsoft.com/vscode/devcontainers/base:0-alpine-3.11
- mcr.microsoft.com/vscode/devcontainers/base:0-alpine-3.12
- mcr.microsoft.com/vscode/devcontainers/base:0-debian
- mcr.microsoft.com/vscode/devcontainers/base:0-buster
- mcr.microsoft.com/vscode/devcontainers/base:0-debian-10
- mcr.microsoft.com/vscode/devcontainers/base:0-stretch
- mcr.microsoft.com/vscode/devcontainers/base:0-debian-9
- mcr.microsoft.com/vscode/devcontainers/base:0-ubuntu
- mcr.microsoft.com/vscode/devcontainers/base:0-focal
- mcr.microsoft.com/vscode/devcontainers/base:0-ubuntu-20.04
- mcr.microsoft.com/vscode/devcontainers/base:0-bionic
- mcr.microsoft.com/vscode/devcontainers/base:0-ubuntu-18.04

### vscode_cpp

- mcr.microsoft.com/vscode/devcontainers/cpp:0-buster
- mcr.microsoft.com/vscode/devcontainers/cpp:0-debian-10
- mcr.microsoft.com/vscode/devcontainers/cpp:0-stretch
- mcr.microsoft.com/vscode/devcontainers/cpp:0-debian-9

### vscode_dotnetcore

- mcr.microsoft.com/vscode/devcontainers/dotnetcore:0-3.1
- mcr.microsoft.com/vscode/devcontainers/dotnetcore:0-2.1

### vscode_go

- mcr.microsoft.com/vscode/devcontainers/go:0-1
- mcr.microsoft.com/vscode/devcontainers/go:0-1.15
- mcr.microsoft.com/vscode/devcontainers/go:0-1.14

### vscode_java

- mcr.microsoft.com/vscode/devcontainers/java:0-8
- mcr.microsoft.com/vscode/devcontainers/java:0-11
- mcr.microsoft.com/vscode/devcontainers/java:0-14

### vscode_javascript_node

- mcr.microsoft.com/vscode/devcontainers/javascript-node:0-14
- mcr.microsoft.com/vscode/devcontainers/javascript-node:0-12
- mcr.microsoft.com/vscode/devcontainers/javascript-node:0-10

### vscode_php

- mcr.microsoft.com/vscode/devcontainers/php:0-7
- mcr.microsoft.com/vscode/devcontainers/php:0-7.4
- mcr.microsoft.com/vscode/devcontainers/php:0-7.3

### vscode_python

- mcr.microsoft.com/vscode/devcontainers/python:0-3
- mcr.microsoft.com/vscode/devcontainers/python:0-3.8
- mcr.microsoft.com/vscode/devcontainers/python:0-3.7
- mcr.microsoft.com/vscode/devcontainers/python:0-3.6

### vscode_ruby

- mcr.microsoft.com/vscode/devcontainers/ruby:0-2
- mcr.microsoft.com/vscode/devcontainers/ruby:0-2.7
- mcr.microsoft.com/vscode/devcontainers/ruby:0-2.6

### vscode_typescript_node

- mcr.microsoft.com/vscode/devcontainers/typescript-node:0-14
- mcr.microsoft.com/vscode/devcontainers/typescript-node:0-12
- mcr.microsoft.com/vscode/devcontainers/typescript-node:0-10

### vscode_universal

- mcr.microsoft.com/vscode/devcontainers/universal:0

### vscode_rust

- mcr.microsoft.com/vscode/devcontainers/rust:0
