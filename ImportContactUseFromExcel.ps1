#CSV文件要以逗号分隔，并以unicode编码。详见http://blog.sina.com.cn/s/blog_998fcd9a0101k5kl.html
$Contacts = Import-CSV C:\csv的具体路径.csv

#各种参数可以或详细或简单的设置
$Contacts | ForEach {New-MailContact -Name $_.DisplayName -ExternalEmailAddress $_.ExternalEmailAddress -Alias $_.Alias}