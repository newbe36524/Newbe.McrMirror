$config = Get-Content config.json | ConvertFrom-Json
$tpl = Get-Content .\template.yml

$outDir = "../../.github/workflows"

$config.images | ForEach-Object {
    $sourceName = $_[0]
    $targetName = $_[1]
    $filename = $targetName.Replace("/", "_").Replace(":", "_")
    $content = $tpl.Replace("[FILE_NAME]", $filename).Replace("[SOURCE_IMAGE_NAME]", $sourceName).Replace("[TARGET_IMAGE_NAME]", $targetName).Replace("[DOCKERHUB_USERNAME]", $config.dockerhub_name).Replace("[ALIYUN_USERNAME]", $config.aliyun_name)
    $content | Out-File "$outDir/$($filename).yml" -Encoding utf8NoBOM
}