import psutil
from socket import gethostname
result = {}
result["hostname"] = gethostname()
result["cpu_percent_per_core"] = psutil.cpu_percent(interval=1, percpu=True)
print(result)
