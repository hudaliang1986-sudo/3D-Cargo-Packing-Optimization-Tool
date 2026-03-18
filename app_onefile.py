import webbrowser
import os
import sys
import subprocess
import shutil

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
    
    # 方法1: 使用系统默认浏览器
    try:
        webbrowser.open('file://' + html_file)
        return True
    except:
        pass
    
    # 方法2: 尝试找到并使用已知浏览器
    browser_path, browser_name = find_browser()
    if browser_path:
        try:
            subprocess.Popen([browser_path, html_file])
            return True
        except:
            pass
    
    # 方法3: 使用Windows默认应用打开HTML文件
    try:
        os.startfile(html_file)
        return True
    except:
        pass
    
    # 方法4: 尝试使用cmd start命令
    try:
        subprocess.run(['cmd', '/c', 'start', '', html_file], check=False)
        return True
    except:
        pass
    
    return False

# 获取HTML文件路径
if getattr(sys, 'frozen', False):
    # 打包后的exe运行时
    if hasattr(sys, '_MEIPASS'):
        html_file = os.path.join(sys._MEIPASS, '货物排版计算工具.html')
    else:
        exe_dir = os.path.dirname(sys.executable)
        html_file = os.path.join(exe_dir, '货物排版计算工具.html')
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(exe_dir, '货物排版计算工具.html')

# 尝试其他位置
if not os.path.exists(html_file):
    html_file = os.path.join(os.getcwd(), '货物排版计算工具.html')

# 检查文件是否存在
if not os.path.exists(html_file):
    # 弹出错误窗口
    import ctypes
    ctypes.windll.user32.MessageBoxW(0, "找不到HTML文件！\n请确保货物排版计算工具.html文件存在。", "错误", 0x10)
    sys.exit(1)

# 尝试打开浏览器
if not open_with_browser(html_file):
    # 如果所有方法都失败，显示错误
    import ctypes
    ctypes.windll.user32.MessageBoxW(0, "无法打开浏览器！\n请手动打开货物排版计算工具.html文件。", "警告", 0x30)
