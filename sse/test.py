from urllib.parse import urlencode,urlparse,unquote

url = "http:10.110.112.2:9999/api/report/?remark=&statue=&person=&type=&task_type=&cron_task_status=&create_time%5B0%5D=2022-07-06&create_time%5B1%5D=2022-07-08&page=1"

print(unquote(url).encode(encoding='utf-8'))