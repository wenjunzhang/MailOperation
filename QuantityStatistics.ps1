# ͳ��ʱ����ڵķ���������ע��Ҫ��ÿһ̨MBX�����и�����,���������ƿ��Բ�ָ��
>Get-MessageTrackingLog -ResultSize unlimited -Start "07/01/2012" -End "07/13/2012" -EventId "send" -Server "srvbj06" |Measure-Object
#ͳ�Ʒ���ʧ�ܵ����������������ƿ��Բ�ָ��
>Get-MessageTrackingLog -ResultSize unlimited -Start "07/01/2012" -End "07/13/2012" -EventId "Fail" -Server "srvbj06" |Measure-Object
#�鿴ĳ������ķ������
>Get-MessageTrackingLog -ResultSize unlimited -Start "07/01/2012" -End "07/13/2012" -EventId "send" -Sender "luochen@bpdi.com.cn" |Measure-Object
#�鿴ĳ���˺ŷ���ʧ�ܵ����
>Get-MessageTrackingLog -ResultSize unlimited -Start "07/01/2012" -End "07/13/2012" -EventId "send" -Sender "luochen@bpdi.com.cn" |Measure-Object
#ĳ��ʱ����ڵķ�������ͳ��
>Get-MessageTrackingLog -ResultSize unlimited -Start "07/01/2012" -End "07/13/2012" -EventId "send" |Group-Object -Property:sender |select name,count
#��ʱ����ڷ������ݽ�������
>Get-MessageTrackingLog -ResultSize unlimited -Start "07/01/2012" -End "07/13/2012" -EventId "send" |Group-Object -Property:sender |Select name,count|sort count -Descending