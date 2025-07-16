import time
from datetime import timedelta

start = time.time()

for _ in range(10**9):
    pass

end = time.time()
print(f"Waktu eksekusi: {timedelta(seconds=end - start)}")