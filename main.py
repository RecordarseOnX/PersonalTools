from fastapi import FastAPI, Request
from tools.bilibili_audio import router as bilibili_router
from utils.cleaner import start_cleanup_task

app = FastAPI(title="神奇工具")

# 注册工具路由
app.include_router(bilibili_router, prefix="/bilibili-audio")

# 启动后台清理任务
@app.on_event("startup")
async def startup_event():
    start_cleanup_task()
