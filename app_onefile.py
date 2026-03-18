import webbrowser
import os
import sys
import subprocess
import shutil
import time
import ctypes

def show_message(msg):
    """显示消息弹窗"""
    try:
        ctypes.windll.user32.MessageBoxW(0, msg, "货物排版计算工具", 0x40)
    except:
        print(msg)

# 添加控制台输出用于调试
print("=" * 50)
print("货物排版计算工具启动中...")
print(f"sys.frozen: {getattr(sys, 'frozen', False)}")
print(f"sys._MEIPASS: {getattr(sys, '_MEIPASS', 'NOT SET')}")
print("=" * 50)

def find_browser():
    """尝试找到可用的浏览器"""
    browsers = [
        # Windows常见浏览器
        (r"C:\Program Files\Google\Chrome\Application\chrome.exe", "Chrome"),
        (r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "Chrome"),
        (r"C:\Program Files\Microsoft\Edge\Application\msedge.exe", "Edge"),
        (r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", "Edge"),
        (r"C:\Program Files\Mozilla Firefox\firefox.exe", "Firefox"),
        (r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe", "Firefox"),
        (r"C:\Program Files\Opera\launcher.exe", "Opera"),
        (r"C:\Program Files (x86)\Opera\launcher.exe", "Opera"),
        (r"C:\Users\%s\AppData\Local\Google\Chrome\Application\chrome.exe" % os.getenv('USERNAME', ''), "Chrome"),
        (r"C:\Users\%s\AppData\Local\Microsoft\Edge\Application\msedge.exe" % os.getenv('USERNAME', ''), "Edge"),
    ]
    
    for path, name in browsers:
        expanded_path = os.path.expandvars(path)
        if os.path.exists(expanded_path):
            return expanded_path, name
    
    return None, None

def open_with_browser(html_file):
    """尝试用多种方式打开浏览器"""
    
    # 方法1: 尝试找到并使用已知浏览器（最可靠）
    browser_path, browser_name = find_browser()
    if browser_path:
        try:
            print(f"尝试方法1: 使用{browser_name}")
            subprocess.Popen([browser_path, html_file], 
                           creationflags=subprocess.CREATE_NO_WINDOW)
            print("方法1成功")
            show_message(f"正在打开{browser_name}浏览器...")
            return True
        except Exception as e:
            print(f"方法1失败: {e}")
    
    # 方法2: 使用cmd start命令
    try:
        print("尝试方法2: cmd start")
        subprocess.Popen(['cmd', '/c', 'start', '', html_file], 
                        creationflags=subprocess.CREATE_NO_WINDOW)
        print("方法2成功")
        show_message("正在打开浏览器...")
        return True
    except Exception as e:
        print(f"方法2失败: {e}")
    
    # 方法3: 使用Windows默认应用打开HTML文件
    try:
        print("尝试方法3: os.startfile")
        os.startfile(html_file)
        print("方法3成功")
        show_message("正在打开文件...")
        return True
    except Exception as e:
        print(f"方法3失败: {e}")
    
    # 方法4: 使用系统默认浏览器
    try:
        print("尝试方法4: webbrowser")
        webbrowser.open('file://' + html_file)
        print("方法4成功")
        show_message("正在打开浏览器...")
        return True
    except Exception as e:
        print(f"方法4失败: {e}")
    
    return False

# 获取HTML文件路径
if getattr(sys, 'frozen', False):
    # 打包后的exe运行时
    if hasattr(sys, '_MEIPASS'):
        html_file = os.path.join(sys._MEIPASS, '货物排版计算工具.html')
        print(f"尝试从MEIPASS加载: {html_file}")
    else:
        exe_dir = os.path.dirname(sys.executable)
        html_file = os.path.join(exe_dir, '货物排版计算工具.html')
        print(f"尝试从exe目录加载: {html_file}")
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(exe_dir, '货物排版计算工具.html')
    print(f"开发模式，从脚本目录加载: {html_file}")

# 尝试其他位置
if not os.path.exists(html_file):
    html_file = os.path.join(os.getcwd(), '货物排版计算工具.html')
    print(f"尝试从当前目录加载: {html_file}")

# 检查文件是否存在
if not os.path.exists(html_file):
    print(f"错误：找不到HTML文件: {html_file}")
    # 弹出错误窗口
    import ctypes
    ctypes.windll.user32.MessageBoxW(0, "找不到HTML文件！\n请确保货物排版计算工具.html文件存在。", "错误", 0x10)
    sys.exit(1)

print(f"找到HTML文件: {html_file}")

# 尝试打开浏览器
if not open_with_browser(html_file):
    print("无法打开浏览器")
    # 如果所有方法都失败，显示错误
    import ctypes
    ctypes.windll.user32.MessageBoxW(0, "无法打开浏览器！\n请手动打开货物排版计算工具.html文件。", "警告", 0x30)
