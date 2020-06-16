using System.Collections.Generic;
using CommandLine;
using CommandLine.Text;

namespace Newbe.McrMirror
{
    public class FlowOptions
    {
        /// <summary>
        /// skip download config from remote
        /// </summary>
        [Option('d', "skip-download-config",
            HelpText = "跳过下载 Newbe.McrMirror 的配置。请至少确保曾经下载过一次配置，才能选择跳过。",
            Default = false)]
        public bool? SkipDownloadConfig { get; set; }

        /// <summary>
        /// launch downloader in parallel
        /// </summary>
        [Option('p', "parallel",
            HelpText = "并行下载多个镜像",
            Default = true)]
        public bool? DownloadParallel { get; set; }

        /// <summary>
        /// url for download config.
        /// </summary>
        [Option('u', "url-of-config",
            HelpText = "配置文件下载地址。配置文件是用于检查镜像是否支持等相关功能的文件，需要确保至少下载过一次。",
            Default = "https://gitee.com/yks/Newbe.McrMirror/raw/master/src/GithubActionGeneration/config-v2.json")]
        public string ConfigUrl { get; set; }

        /// <summary>
        /// file name for saving config file
        /// </summary>
        [Option('f', "filename-of-config",
            HelpText = "配置文件的本地保存位置。您可以设置该项来调整位置。",
            Default = "config.json")]
        public string ConfigFilename { get; set; }

        /// <summary>
        /// images need to be download
        /// </summary>
        [Option('i', "image",
            Required = true,
            HelpText =
                "需要下载的镜像地址。可以指定多个地址同时下载多个镜像。",
            Separator = ',')]
        public IEnumerable<string> Images { get; set; }

        /// <summary>
        /// remove source tag after re-tag
        /// </summary>
        [Option('r', "remove-source-tag",
            HelpText = "重新 tag 之后，是否删除国内镜像对应的 tag 。因为使用国内服务器下载，所以会生成一个额外的 tag。启用该选项可以清理它们。",
            Default = true)]
        public bool? RemoveSourceTag { get; set; }

        [Option('h', "mirror-host",
            HelpText = "镜像服务器, 可以是 : aliyun, tencentyun 或者指定域名 (例如： registry.cn-hangzhou.aliyuncs.com)",
            Default = "aliyun")]
        public string MirrorHost { get; set; }

        [Option('n', "mirror-namespace",
            HelpText = "镜像服务器使用的名称空间, 如果是内置的 aliyun, tencentyun 则会选择作者的名称空间。当然你也可以改变它。",
            Required = false)]
        public string Namespace { get; set; }

        [Usage(ApplicationAlias = "docker-mcr")]
        public static IEnumerable<Example> Examples
        {
            get
            {
                yield return new Example("下载单个镜像。", new FlowOptions
                {
                    Images = new[] {"mcr.microsoft.com/dotnet/core/sdk:3.1"}
                });
                yield return new Example("下载多个镜像。", new FlowOptions
                {
                    Images = new[]
                    {
                        "mcr.microsoft.com/dotnet/core/sdk:3.1",
                        "mcr.microsoft.com/dotnet/core/runtime:3.1"
                    }
                });
                yield return new Example("从腾讯云下载", new FlowOptions
                {
                    Images = new[] {"mcr.microsoft.com/dotnet/core/sdk:3.1"},
                    MirrorHost = "tencentyun"
                });
                yield return new Example("关闭并行下载", new FlowOptions
                {
                    DownloadParallel = false,
                    Images = new[]
                    {
                        "mcr.microsoft.com/dotnet/core/sdk:3.1",
                        "mcr.microsoft.com/dotnet/core/runtime:3.1"
                    }
                });
                yield return new Example("从自定义的服务器下载", new FlowOptions
                {
                    DownloadParallel = false,
                    Images = new[]
                    {
                        "mcr.microsoft.com/dotnet/core/sdk:3.1"
                    },
                    MirrorHost = "registry.cn-hangzhou.aliyuncs.com",
                    Namespace = "newbe36524"
                });
            }
        }
    }
}