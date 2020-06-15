using System.Collections.Generic;
using Newtonsoft.Json;

namespace Newbe.McrMirror
{
    public class RepositoryConfig
    {
        [JsonProperty("dockerhub_name")] public string DockerHubName { get; set; } = null!;
        [JsonProperty("aliyun_name")] public string AliyunName { get; set; } = null!;
        [JsonProperty("images")] public ImageItem[] Images { get; set; } = null!;

        public class ImageItem : List<string>
        {
            public string McrTag => this[0];
            public string AliyunTag => this[1];
        }
    }
}