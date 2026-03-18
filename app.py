import webbrowser
import os
import sys
import tempfile

# 获取exe所在目录
if getattr(sys, 'frozen', False):
    # 打包后的exe运行时，exe所在目录
    exe_dir = os.path.dirname(sys.executable)
else:
    # Python脚本运行时
    exe_dir = os.path.dirname(os.path.abspath(__file__))

# HTML文件路径 - 首先尝试exe旁边
html_file = os.path.join(exe_dir, '货物排版计算工具.html')

# 如果不存在，尝试从临时目录（_MEIPASS）
if not os.path.exists(html_file) and hasattr(sys, '_MEIPASS'):
    html_file = os.path.join(sys._MEIPASS, '货物排版计算工具.html')

# 确保HTML文件存在
if not os.path.exists(html_file):
    print(f"错误：找不到HTML文件")
    print(f"已搜索位置: {exe_dir}")
    if hasattr(sys, '_MEIPASS'):
        print(f"临时目录: {sys._MEIPASS}")
    sys.exit(1)

# 在默认浏览器中打开
webbrowser.open('file://' + html_file)
