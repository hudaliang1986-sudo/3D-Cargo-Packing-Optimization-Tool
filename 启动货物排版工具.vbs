' 货物排版计算工具 - Windows启动器
Set WshShell = CreateObject("WScript.Shell")
currentPath = WshShell.CurrentDirectory

' 使用默认浏览器打开HTML文件
Set objShell = CreateObject("Shell.Application")
objShell.Open(currentPath & "\货物排版计算工具.html")

' 或者使用Edge/Chrome打开
' WshShell.Run "msedge.exe """ & currentPath & "\货物排版计算工具.html""", 1, False
' WshShell.Run "chrome.exe """ & currentPath & "\货物排版计算工具.html""", 1, False
