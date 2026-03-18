# GitHub 推送指南

## 步骤1: 创建GitHub仓库

1. 打开 https://github.com/new
2. 仓库名称输入: `lingma-pallet-tool` (或其他名称)
3. 选择 "Public" 或 "Private"
4. **不要**勾选 "Add a README file"
5. **不要**勾选 "Add .gitignore"
6. 点击 "Create repository"

## 步骤2: 推送代码

创建仓库后，GitHub会显示推送命令，请运行以下命令:

```bash
git remote add origin https://github.com/你的用户名/lingma-pallet-tool.git
git branch -M main
git push -u origin main
```

或者如果GitHub显示的命令不同，请使用GitHub页面上的命令。

## 完成后

代码将推送到GitHub，您可以与他人共享仓库链接。
