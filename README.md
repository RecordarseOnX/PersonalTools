# 神奇工具（Web 工具合集）

这是一个基于 FastAPI 的 Web 工具后端，当前包含：

- 🎵 B站音频提取工具

## 在线部署（推荐 Render）
1. 打开 [https://render.com](https://render.com)
2. 创建新服务，选择本项目代码仓库
3. 设置：
   - 构建命令: `pip install -r requirements.txt`
   - 启动命令: `uvicorn main:app --host 0.0.0.0 --port 10000`
4. 部署完成后，你会得到一个 API 地址

## 本地运行
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
访问：http://localhost:8000/docs 查看 API 文档
