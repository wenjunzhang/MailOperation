$date = (Get-Date).AddMonths(-2)
#ȥ�� -whatif��ʼ����ִ�� 
Get-ChildItem -Path "c:\scripts\E*.log" | where {!$_.PSIsContainer} | foreach {if ($_.LastWriteTime -lt $date){Remove-Item $_ -whatif}}