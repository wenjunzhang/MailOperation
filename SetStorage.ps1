具体的单个命令请见官方链接https://technet.microsoft.com/en-us/library/aa998353%28v=exchg.160%29.aspx
Import-CSV "具体路径.CSV" | ForEach {Set-Mailbox -Identity $_.Identity -IssueWarningQuota 400mb -ProhibitSendQuota 500mb -ProhibitSendReceiveQuota 600mb -UseDatabaseDefault $false}