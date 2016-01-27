# 统计时间段内的发件量，请注意要在每一台MBX上运行该命令,服务器名称可以不指定
>Get-MessageTrackingLog -ResultSize unlimited -Start "07/01/2012" -End "07/13/2012" -EventId "send" -Server "srvbj06" |Measure-Object
#统计发件失败的数量，服务器名称可以不指定
>Get-MessageTrackingLog -ResultSize unlimited -Start "07/01/2012" -End "07/13/2012" -EventId "Fail" -Server "srvbj06" |Measure-Object
#查看某个邮箱的发件情况
>Get-MessageTrackingLog -ResultSize unlimited -Start "07/01/2012" -End "07/13/2012" -EventId "send" -Sender "luochen@bpdi.com.cn" |Measure-Object
#查看某个账号发送失败的情况
>Get-MessageTrackingLog -ResultSize unlimited -Start "07/01/2012" -End "07/13/2012" -EventId "send" -Sender "luochen@bpdi.com.cn" |Measure-Object
#某个时间段内的发件数量统计
>Get-MessageTrackingLog -ResultSize unlimited -Start "07/01/2012" -End "07/13/2012" -EventId "send" |Group-Object -Property:sender |select name,count
#对时间段内发件数据进行排序
>Get-MessageTrackingLog -ResultSize unlimited -Start "07/01/2012" -End "07/13/2012" -EventId "send" |Group-Object -Property:sender |Select name,count|sort count -Descending