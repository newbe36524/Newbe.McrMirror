using System.Collections.Generic;
using Newtonsoft.Json;

namespace Newbe.McrMirror
{
    public class RepositoryConfig
    {
        [JsonProperty("dockerhub_name")] public string DockerHubUsername { get; set; } = null!;
        [JsonProperty("dockerhub_namespace")] public string DockerhubNamespace { get; set; }
        [JsonProperty("aliyun_name")] public string AliyunUsername { get; set; } = null!;
        [JsonProperty("aliyun_namespace")] public string AliyunNamespace { get; set; }
        [JsonProperty("tencentyun_name")] public string TencentyunUsername { get; set; } = null!;
        [JsonProperty("tencentyun_namespace")] public string TencentyunNamespace { get; set; }

        [JsonProperty("images")] public ImageItem[] Images { get; set; } = null!;

        public class ImageItem
        {
            public string Source { get; set; }
            public string Tag { get; set; }
        }
    }
}