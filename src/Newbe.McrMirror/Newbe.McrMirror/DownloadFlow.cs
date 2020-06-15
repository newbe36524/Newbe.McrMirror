using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;

namespace Newbe.McrMirror
{
    public class DownloadFlow : IDownloadFlow
    {
        private readonly ILogger<DownloadFlow> _logger;
        private readonly IImageDownloader _imageDownloader;

        public DownloadFlow(
            ILogger<DownloadFlow> logger,
            IImageDownloader imageDownloader)
        {
            _logger = logger;
            _imageDownloader = imageDownloader;
        }

        public async Task RunAsync(FlowOptions flowOptions)
        {
            // download config
            if (!flowOptions.SkipDownloadConfig.HasValue || flowOptions.SkipDownloadConfig == false)
            {
                var client = new HttpClient();
                try
                {
                    var httpResponseMessage = await client.GetAsync(flowOptions.ConfigUrl);
                    if (!httpResponseMessage.IsSuccessStatusCode)
                    {
                        _logger.LogError("failed to download config");
                    }

                    var content = await httpResponseMessage.Content.ReadAsStringAsync();
                    await File.WriteAllTextAsync(flowOptions.ConfigFilename, content);
                }
                catch (Exception e)
                {
                    _logger.LogError(e, "failed to download config");
                }
            }

            // load config
            if (!File.Exists(flowOptions.ConfigFilename))
            {
                _logger.LogError("failed to find config file in path {filename}", flowOptions.ConfigFilename);
                return;
            }

            var json = await File.ReadAllTextAsync(flowOptions.ConfigFilename);
            var config = JsonConvert.DeserializeObject<RepositoryConfig>(json);

            var waitingDownloadItems = new List<RepositoryConfig.ImageItem>();
            // check config for supporting images or show errors
            foreach (var image in flowOptions.Images)
            {
                var item = config.Images.FirstOrDefault(x => x.McrTag == image);
                if (item == null)
                {
                    _logger.LogError(
                        "the images '{image}' is not supported, please contact author if you need support at https://github.com/newbe36524/Newbe.McrMirror/issues",
                        image);
                }
                else
                {
                    waitingDownloadItems.Add(item);
                }
            }

            // start to download 
            var removeSourceTag = !flowOptions.RemoveSourceTag.HasValue || flowOptions.RemoveSourceTag == true;
            if (!flowOptions.DownloadParallel.HasValue && flowOptions.DownloadParallel == true)
            {
                await Task.WhenAll(waitingDownloadItems
                    .Select(item => _imageDownloader.Download(new DownloadInfo
                    {
                        SourceUrl = $"registry.cn-hangzhou.aliyuncs.com/{item.AliyunTag}",
                        TargetTag = item.McrTag,
                        RemoveSourceTag = removeSourceTag
                    })));
            }
            else
            {
                foreach (var item in waitingDownloadItems)
                {
                    await _imageDownloader.Download(new DownloadInfo
                    {
                        SourceUrl = $"registry.cn-hangzhou.aliyuncs.com/{item.AliyunTag}",
                        TargetTag = item.McrTag,
                        RemoveSourceTag = removeSourceTag
                    });
                }
            }
        }
    }
}