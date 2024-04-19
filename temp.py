import subprocess

# 应用程序的路径，你需要根据实际情况来替换下面的路径
qq_path = "C:\\Program Files\\Tencent\\QQNT\\QQ.exe"
wechat_path = "C:\\Program Files\\Tencent\\WeChat\\WeChat.exe"
tim_path = "C:\\Program Files (x86)\\Tencent\\TIM\\Bin\\QQScLauncher"

# 启动QQ
subprocess.Popen(qq_path)

# 启动微信
subprocess.Popen(wechat_path)

# 启动TIM
subprocess.Popen(tim_path)
