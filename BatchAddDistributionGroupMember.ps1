可通过姓名加成员，但如果姓名字段有重复，会加入失败，最好以邮箱的方式加入。具体单个命令可见官方技术文档。
Import-CSV "具体路径.csv" | ForEach {Add-DistributionGroupMember -Identity "通讯组名称" -Member $_.ExternalEmailAddress}