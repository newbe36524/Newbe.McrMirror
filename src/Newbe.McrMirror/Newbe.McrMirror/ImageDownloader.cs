using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;

namespace Newbe.McrMirror
{
    public class ImageDownloader : IImageDownloader
    {
        private readonly ILogger<ImageDownloader> _logger;

        public ImageDownloader(
            ILogger<ImageDownloader> logger)
        {
            _logger = logger;
        }

        public Task Download(DownloadInfo downloadInfo)
        {
            return Task.Run(() =>
            {
                RunDocker("pull", downloadInfo.SourceUrl);
                RunDocker("tag", downloadInfo.SourceUrl, downloadInfo.TargetTag);
                if (downloadInfo.RemoveSourceTag)
                {
                    RunDocker("rmi", downloadInfo.SourceUrl, "--force");
                }
            });
        }

        private void RunDocker(params string[] ps)
            => RunProcess("docker", ps);

        private void RunProcess(string cmd, params string[] ps)
        {
            var cmdline = string.Join(" ", GetCmdLineParts());
            _logger.LogInformation("start to run : {cmdline}", cmdline);
            var startInfo = new ProcessStartInfo
            {
                FileName = cmd,
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = true
            };
            if (ps?.Any() == true)
            {
                foreach (var s in ps)
                {
                    startInfo.ArgumentList.Add(s);
                }
            }

            var p = new Process
            {
                StartInfo = startInfo
            };
            p.OutputDataReceived += (sender, args) => { _logger.LogTrace(args.Data); };
            p.ErrorDataReceived += (sender, args) => { _logger.LogTrace(args.Data); };
            p.Start();
            p.BeginErrorReadLine();
            p.BeginOutputReadLine();
            p.WaitForExit();
            _logger.LogInformation("run to end : {cmdline}", cmdline);

            IEnumerable<string> GetCmdLineParts()
            {
                yield return cmd;
                if (ps?.Any() == true)
                {
                    foreach (var s in ps)
                    {
                        yield return s;
                    }
                }
            }
        }
    }
}