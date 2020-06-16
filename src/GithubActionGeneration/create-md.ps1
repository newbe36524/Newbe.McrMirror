$confg = Get-Content .\config-v2.json | ConvertFrom-Json

$re = ""
$re += "tag | status"
$re += "`n --- | ---"
$confg.images | ForEach-Object {
    $tag = $_.tag
    $name = $tag.Replace( ":", "_")
    $re += "`n $tag |[![push image $name](https://github.com/newbe36524/Newbe.McrMirror/workflows/push%20image%20$name/badge.svg?branch=publish)](https://github.com/newbe36524/Newbe.McrMirror/actions?query=workflow%3A%22push+image+$name%22)"
} 

$re | Out-File md.md -Encoding utf8NoBOM

