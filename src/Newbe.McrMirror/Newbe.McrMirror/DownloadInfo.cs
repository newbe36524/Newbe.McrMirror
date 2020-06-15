namespace Newbe.McrMirror
{
    public class DownloadInfo
    {
        public string SourceUrl { get; set; } = null!;
        public string TargetTag { get; set; } = null!;
        public bool RemoveSourceTag { get; set; }
    }
}