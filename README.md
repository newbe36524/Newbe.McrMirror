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

<https://github.com/newbe36524/Newbe.McrMirror/blob/master/tags.md>
