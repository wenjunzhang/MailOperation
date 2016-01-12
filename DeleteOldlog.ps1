$date = (Get-Date).AddMonths(-2)
#去掉 -whatif开始真正执行 
Get-ChildItem -Path "c:\scripts\E*.log" | where {!$_.PSIsContainer} | foreach {if ($_.LastWriteTime -lt $date){Remove-Item $_ -whatif}}