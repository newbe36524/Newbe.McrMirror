using System;
using System.Threading.Tasks;
using CommandLine;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;

namespace Newbe.McrMirror
{
    class Program
    {
        static async Task<int> Main(string[] args)
        {
            var parserResult = Parser.Default.ParseArguments<FlowOptions>(args);
            await parserResult
                .WithParsedAsync(o =>
                {
                    var services = new ServiceCollection();
                    services.AddLogging(logging => { logging.AddConsole(); });
                    services.AddTransient<IImageDownloader, ImageDownloader>();
                    services.AddSingleton<IDownloadFlow, DownloadFlow>();
                    var provider = services.BuildServiceProvider();
                    var flow = provider.GetRequiredService<IDownloadFlow>();
                    return flow.RunAsync(o);
                });
            return 0;
        }
    }
}