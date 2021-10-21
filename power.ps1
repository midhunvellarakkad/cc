Get-EventLog -LogName Security -InstanceId 4624,4625,4634,4648,4719,4964,1102,4720,4722,4723,4732,4738,4698,4699,4700,4701,4702,5152,5153  -newest 500| Export-Csv C:\cevent\critical.csv
