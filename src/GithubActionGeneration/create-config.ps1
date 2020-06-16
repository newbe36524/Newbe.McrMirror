function CreateImagesFromDockerhub {
    param (
        $url,
        $tagsFromMark,
        $tagsEndMark,
        $imageName
    )
    $body = (Invoke-WebRequest -Uri $url).Content 
    $json = $body | ConvertFrom-Json
    $body | Out-File microsoft-dotnet-core-sdk.json
    $full_description = $json.full_description

    $fromIndex = $full_description.IndexOf($tagsFromMark)
    $toIndex = $full_description.IndexOf($tagsEndMark)

    $linuxTagsContent = $full_description.SubString($fromIndex, $toIndex - $fromIndex)
    $tags = $linuxTagsContent -split "`n" | Where-Object {
        $_ -ne $null -and $_.Contains("Dockerfile") 
    } | ForEach-Object {
        $_.SubString(0, $_.IndexOf("|")).Trim() 
    } | Where-Object {
        $_ -ne "Tags"
    } | ForEach-Object {
        $_ -split ","
    } | ForEach-Object {
        $_.Trim()
    } | Sort-Object | Get-Unique

    $domain = "mcr.microsoft.com"
    $namespace = "dotnet/core"

    return $tags | ForEach-Object {
        @{
            "source" = "$domain/$namespace/$imageName`:$_"
            "tag"    = "$imageName`:$_"
        }
    }
}
function CreateImages {
    @(
        (CreateImagesFromDockerhub -url "https://hub.docker.com/api/content/v1/products/images/microsoft-dotnet-core-sdk" -tagsFromMark "## Linux amd64 Tags" -tagsEndMark "## Windows Server, version 2004 amd64 Tags" -imageName "sdk"),
        (CreateImagesFromDockerhub -url "https://hub.docker.com/api/content/v1/products/images/microsoft-dotnet-core-runtime-deps" -tagsFromMark "## Linux amd64 Tags" -tagsEndMark "You can retrieve a list of all available tags for dotnet/core/runtime-deps" -imageName "runtime-deps"),
        (CreateImagesFromDockerhub -url "https://hub.docker.com/api/content/v1/products/images/microsoft-dotnet-core-runtime" -tagsFromMark "## Linux amd64 Tags" -tagsEndMark "## Windows Server, version 2004 amd64 Tags" -imageName "runtime"),
        (CreateImagesFromDockerhub -url "https://hub.docker.com/api/content/v1/products/images/microsoft-dotnet-core-aspnet" -tagsFromMark "## Linux amd64 Tags" -tagsEndMark "## Windows Server, version 2004 amd64 Tags" -imageName "aspnet")
    )
    | ForEach-Object {
        $_
    }
}

$config = @{
    "dockerhub_name"       = "newbe36524";
    "aliyun_name"          = "pianzide1117";
    "tencentyun_name"      = "472158246";
    "dockerhub_namespace"  = "newbe36524";
    "aliyun_namespace"     = "newbe36524";
    "tencentyun_namespace" = "mcr_newbe36524";
    "images"               = CreateImages ;
}

$config | ConvertTo-Json | Out-File .\config-v2.json -Encoding utf8NoBOM