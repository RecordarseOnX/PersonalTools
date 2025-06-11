import os
import time
import threading

TMP_DIR = "tmp"
EXPIRE_SECONDS = 1800  # 30 分钟

def clean_tmp():
    now = time.time()
    for f in os.listdir(TMP_DIR):
        f_path = os.path.join(TMP_DIR, f)
        if os.path.isfile(f_path) and now - os.path.getmtime(f_path) > EXPIRE_SECONDS:
            os.remove(f_path)

def start_cleanup_task():
    def loop():
        while True:
            clean_tmp()
            time.sleep(600)  # 每 10 分钟清理一次
    t = threading.Thread(target=loop, daemon=True)
    t.start()
