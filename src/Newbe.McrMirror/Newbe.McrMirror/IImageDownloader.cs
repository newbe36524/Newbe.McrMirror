using System;
using System.Threading.Tasks;

namespace Newbe.McrMirror
{
    public interface IImageDownloader
    {
        Task Download(DownloadInfo downloadInfo);
    }
}