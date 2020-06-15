using System.Collections.Generic;
using CommandLine;

namespace Newbe.McrMirror
{
    public class FlowOptions
    {
        /// <summary>
        /// skip download config from remote
        /// </summary>
        [Option('d', "skip-download-config",
            HelpText = "skip download config from remote",
            Default = false)]
        public bool? SkipDownloadConfig { get; set; }

        /// <summary>
        /// launch downloader in parallel
        /// </summary>
        [Option('p', "parallel",
            HelpText = "launch downloader in parallel",
            Default = true)]
        public bool? DownloadParallel { get; set; }

        /// <summary>
        /// url for download config.
        /// </summary>
        [Option('u', "url-of-config",
            HelpText = "url for download config",
            Default = "https://gitee.com/yks/Newbe.McrMirror/raw/master/src/GithubActionGeneration/config.json")]
        public string ConfigUrl { get; set; }

        /// <summary>
        /// file name for saving config file
        /// </summary>
        [Option('f', "filename-of-config",
            HelpText = " file name for saving config file",
            Default = "config.json")]
        public string ConfigFilename { get; set; }

        /// <summary>
        /// images need to be download
        /// </summary>
        [Option('i', "image",
            Required = true,
            HelpText = "images need to be download")]
        public IEnumerable<string> Images { get; set; }

        /// <summary>
        /// remove source tag after re-tag
        /// </summary>
        [Option('r', "remove-source-tag",
            HelpText = "remove source tag after re-tag",
            Default = true)]
        public bool? RemoveSourceTag { get; set; }
    }
}