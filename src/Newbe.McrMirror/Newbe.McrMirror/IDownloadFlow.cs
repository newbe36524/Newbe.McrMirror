using System.Threading.Tasks;

namespace Newbe.McrMirror
{
    public interface IDownloadFlow
    {
        Task RunAsync(FlowOptions flowOptions);
    }
}