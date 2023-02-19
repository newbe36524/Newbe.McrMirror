function CreateImagesFromDockerhub {
    param (
        $url,
        $tagsFromMark,
        $tagsEndMark,
        $imageName,
        $namespace
    )
    $body = (Invoke-WebRequest -Uri $url).Content 
    $json = $body | ConvertFrom-Json
    $body | Out-File "defs/$imageName.json"
    $full_description = $json.full_description

    $fromIndex = $full_description.IndexOf($tagsFromMark)
    $toIndex = $full_description.IndexOf($tagsEndMark)

    $linuxTagsContent = $full_description.SubString($fromIndex, $toIndex - $fromIndex)
    $tags = $linuxTagsContent -split "`n" | Where-Object {
        $_ -ne $null -and $_.Contains("Dockerfile") 
    } | ForEach-Object {
        $_.SubString(0, $_.IndexOf("|")).Trim() 
    } | Where-Object {
        $_ -ne "Tags" -and $_ -ne "Tag" -and -not $_.Contains("nano") -and -not $_.Contains("preview")
    } | ForEach-Object {
        $_ -split ","
    } | ForEach-Object {
        $_.Trim()
    } | Sort-Object | Get-Unique

    $domain = "mcr.microsoft.com"

    return $tags | ForEach-Object {
        if ($namespace) {
            @{
                "source" = "$domain/$namespace/$imageName`:$_"
                "tag"    = "$imageName`:$_"
                "group"  = "$imageName"
            }
        }
        else {
            @{
                "source" = "$domain/$imageName`:$_"
                "tag"    = "$imageName`:$_"
                "group"  = "$imageName"
            }
        }
        
    }
}
function VsCodeImages {
    
    $config = @(
        @{"source" = "mcr.microsoft.com/vscode/devcontainers/base"; "group" = "vscode_base"; "tags" = @("alpine", "alpine-3.10", "alpine-3.11", "alpine-3.12", "debian", "buster", "debian-10", "stretch", "debian-9", "ubuntu", "focal", "ubuntu-20.04", "bionic", "ubuntu-18.04") },
        @{"source" = "mcr.microsoft.com/vscode/devcontainers/cpp"; "group" = "vscode_cpp"; "tags" = @("bullseye", "debian-11", "buster", "debian-10", "stretch", "debian-9", "hirsute", "ubuntu-21.04", "focal", "ubuntu-20.04", "bionic", "ubuntu-18.04") },
        @{"source" = "mcr.microsoft.com/vscode/devcontainers/dotnetcore"; "group" = "vscode_dotnetcore"; "tags" = @("3.1", "2.1") },
        @{"source" = "mcr.microsoft.com/vscode/devcontainers/go"; "group" = "vscode_go"; "tags" = @("1", "1.15", "1.14") },
        @{"source" = "mcr.microsoft.com/vscode/devcontainers/java"; "group" = "vscode_java"; "tags" = @("8", "11", "14" ) },
        @{"source" = "mcr.microsoft.com/vscode/devcontainers/javascript-node"; "group" = "vscode_javascript_node"; "tags" = @("14", "12", "10" ) },
        @{"source" = "mcr.microsoft.com/vscode/devcontainers/php"; "group" = "vscode_php"; "tags" = @("7", "7.4", "7.3" ) },
        @{"source" = "mcr.microsoft.com/vscode/devcontainers/python"; "group" = "vscode_python"; "tags" = @("3", "3.8", "3.7", "3.6" ) },
        @{"source" = "mcr.microsoft.com/vscode/devcontainers/ruby"; "group" = "vscode_ruby"; "tags" = @("2", "2.7", "2.6" ) },
        @{"source" = "mcr.microsoft.com/vscode/devcontainers/typescript-node"; "group" = "vscode_typescript_node"; "tags" = @("14", "12", "10" ) }
    )
    $vsVersions = @("0")
    $config | ForEach-Object {
        $source = $_.source
        $group = $_.group
        $name = $_.name
        $tags = $_.tags
        $tags | ForEach-Object {
            $tag = $_
            $vsVersions | ForEach-Object {
                $version = $_
                @{
                    "source" = "$source`:$version-$tag"
                    "tag"    = "$group`:$version-$tag"
                    "group"  = "$group"
                }
            }
      
        }
    }
}


function VsCodeImages2 {
    $config = @(
        @{"source" = "mcr.microsoft.com/vscode/devcontainers/universal"; "group" = "vscode_universal"; }
        @{"source" = "mcr.microsoft.com/vscode/devcontainers/rust"; "group" = "vscode_rust"; }
    )
    $vsVersions = @("1", "0")
    $config | ForEach-Object {
        $source = $_.source
        $group = $_.group
        $name = $_.name
        $vsVersions | ForEach-Object {
            $version = $_
            @{
                "source" = "$source`:$version"
                "tag"    = "$group`:$version"
                "group"  = "$group"
            }
        }
    }
}

function CreateImages {
    @(
        (CreateImagesFromDockerhub -url "https://hub.docker.com/api/content/v1/products/images/microsoft-dotnet-sdk" -tagsFromMark "## Linux amd64 Tags" -tagsEndMark "## Nano Server 2022 amd64 Tags" -imageName "sdk" -namespace "dotnet"),
        (CreateImagesFromDockerhub -url "https://hub.docker.com/api/content/v1/products/images/microsoft-dotnet-runtime-deps" -tagsFromMark "## Linux amd64 Tags" -tagsEndMark "You can retrieve a list of all available tags for dotnet/runtime-deps" -imageName "runtime-deps" -namespace "dotnet"),
        (CreateImagesFromDockerhub -url "https://hub.docker.com/api/content/v1/products/images/microsoft-dotnet-runtime" -tagsFromMark "## Linux amd64 Tags" -tagsEndMark "## Nano Server 2022 amd64 Tags" -imageName "runtime" -namespace "dotnet"),
        (CreateImagesFromDockerhub -url "https://hub.docker.com/api/content/v1/products/images/microsoft-dotnet-aspnet" -tagsFromMark "## Linux amd64 Tags" -tagsEndMark "## Nano Server 2022 amd64 Tags" -imageName "aspnet" -namespace "dotnet"),
        (CreateImagesFromDockerhub -url "https://hub.docker.com/api/content/v1/products/images/microsoft-mssql-server" -tagsFromMark "Linux Images" -tagsEndMark "You can retrieve a list of all available tags for mssql/server" -imageName "server" -namespace "mssql"),
        (CreateImagesFromDockerhub -url "https://hub.docker.com/api/content/v1/products/images/microsoft-java-jdk" -tagsFromMark "Linux Images" -tagsEndMark "You can retrieve a list of all available tags for java/jdk" -imageName "jdk" -namespace "java"),
        (CreateImagesFromDockerhub -url "https://hub.docker.com/api/content/v1/products/images/microsoft-java-jre" -tagsFromMark "Linux Images" -tagsEndMark "You can retrieve a list of all available tags for java/jre" -imageName "jre" -namespace "java"),
        (CreateImagesFromDockerhub -url "https://hub.docker.com/api/content/v1/products/images/microsoft-windows" -tagsFromMark "Windows Images" -tagsEndMark "Multi-arch Images" -imageName "windows" -namespace ""),
        (VsCodeImages)
        (VsCodeImages2)
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
