# Day 1 工作与学习记录

## 1. 基本信息

| 项目 | 内容 |
|---|---|
| 日期 | 2026-11-16 |
| 项目目录 | `D:\gnome-repro` |
| 虚拟环境 | `D:\gnome-repro\.venv1` |
| 基础解释器 | `C:\Users\duow1\Miniconda3\python.exe` |
| 包目录 | `D:\gnome-repro\.venv1\Lib\site-packages` |
| 代码仓库 | `https://github.com/Duo45/GNome_Respository-for-Practice.git` |
| 主分支 | `main` |

Python 完整版本号和 NumPy 精确版本号应以项目终端中的实际输出为准：

```bat
python --version
python -c "import sys; print(sys.version); print(sys.executable)"
python -c "import numpy; print(numpy.__version__); print(numpy.__file__)"
```

## 2. 第一天目标

1. 理解 Python 解释器、虚拟环境、pip 和依赖清单的作用。
2. 创建一次即可长期复用的项目虚拟环境。
3. 建立项目目录骨架，安装 NumPy，并固定依赖版本。
4. 初始化 Git 仓库并完成首次本地提交。
5. 在新终端中验证环境可以重新激活并导入 NumPy。
6. 明确本地提交与 GitHub 远程推送的区别。

## 3. 核心概念

### Python 解释器

解释器真正负责执行 Python 代码。`python` 在当前终端中指向哪个程序，可以用以下命令确认：

```bat
where python
python -c "import sys; print(sys.executable)"
```

进入虚拟环境后，解释器应指向：

```text
D:\gnome-repro\.venv1\Scripts\python.exe
```

### 虚拟环境

虚拟环境为单个项目提供独立的 Python 包目录，避免不同项目的依赖互相覆盖。本项目使用 `.venv1`。

激活成功后，命令提示符应显示：

```text
(.venv1) D:\gnome-repro>
```

激活只对当前终端有效。打开新终端后必须重新激活：

```bat
cd /d D:\gnome-repro
call .venv1\Scripts\activate.bat
```

`.venv1` 是本机生成的环境目录，不应提交到 Git。需要提交的是 Python 版本记录、`requirements.txt` 和安装说明。

### pip

pip 负责安装和管理 Python 包。统一使用下面这种写法：

```bat
python -m pip install 包名
```

`python -m pip` 会调用当前 `python` 对应的 pip，降低把包装入错误环境的风险。

### 为什么依赖必须写入文件

聊天记录、终端历史和本机的 `.venv1` 都不是可靠的长期配置来源。把依赖版本写入 `requirements.txt` 后，未来可以按同一份清单重建环境。

推荐记录精确版本，例如：

```text
numpy==实际版本号
```

只写 `numpy` 不能保证以后安装到相同版本。

## 4. 项目结构

```text
D:\gnome-repro
├── data\
├── src\
├── tests\
├── notebooks\
├── reports\
├── .gitignore
├── README.md
└── requirements.txt
```

| 路径 | 用途 |
|---|---|
| `data\` | 原始数据和中间数据 |
| `src\` | Python 源代码 |
| `tests\` | 自动化测试 |
| `notebooks\` | Jupyter Notebook |
| `reports\` | 实验报告和学习记录 |
| `README.md` | 环境说明、安装步骤和验收方法 |
| `requirements.txt` | Python 依赖及版本 |
| `.gitignore` | 排除虚拟环境、缓存等不应提交的文件 |

Git 不跟踪空目录，因此目录中使用了 `.gitkeep` 占位文件。

## 5. 环境创建与日常使用

### 首次创建

```bat
mkdir "D:\gnome-repro"
cd /d "D:\gnome-repro"

python -m venv .venv1
call .venv1\Scripts\activate.bat

python --version
where python
python -c "import sys, platform, site, os; print(sys.version); print(sys.executable); print(platform.platform()); print(site.getsitepackages()); print(os.getcwd())"

python -m pip install --upgrade pip
python -m pip install numpy
python -m pip freeze > requirements.txt
```

### 每天使用

```bat
cd /d D:\gnome-repro
call .venv1\Scripts\activate.bat
python -m pip install -r requirements.txt
python -c "import numpy"
```

正常使用期间不需要反复删除和重建 `.venv1`。

### 新终端验收

关闭旧终端，打开一个新的 `cmd`：

```bat
cd /d D:\gnome-repro
call .venv1\Scripts\activate.bat
where python
python -c "import sys; print(sys.version); print(sys.executable)"
python -c "import numpy; print(numpy.__version__); print(numpy.__file__)"
```

验收要求：

- 当前目录为 `D:\gnome-repro`。
- 解释器位于 `.venv1\Scripts`。
- `import numpy` 成功。
- NumPy 路径位于 `.venv1\Lib\site-packages`。

## 6. Git 工作流程

Git 的基本过程是：

```text
修改文件 → git add → git commit → git push
工作区     暂存区     本地历史      远程仓库
```

### 初始化仓库

```bat
cd /d D:\gnome-repro
git init -b main
git status --short
```

`git init -b main` 创建 `.git` 目录并将主分支命名为 `main`。`git status` 只能查看已有仓库，不能创建仓库。

### 配置提交身份

如果 Git 提示 `Author identity unknown`：

```bat
git config user.name "你的姓名"
git config user.email "你的邮箱"
```

### 暂存、检查、提交

```bat
git add .
git status --short
git diff --cached --stat
git commit -m "chore: initialize reproducible Python environment"
```

| 命令 | 含义 |
|---|---|
| `git add .` | 将当前项目中的非忽略文件加入暂存区 |
| `git status --short` | 紧凑查看文件状态 |
| `git diff --cached --stat` | 查看即将提交的文件和行数变化 |
| `git commit -m "..."` | 将暂存区保存为一次本地提交 |

`git commit` 只保存已经暂存的内容，不会上传 GitHub。提示 `nothing to commit` 通常表示暂存区没有新变化。

### 查看提交

```bat
git log -1 --oneline
git show --stat --oneline HEAD
git ls-files
```

`git ls-files` 用于确认虚拟环境是否被错误跟踪；正常情况下不应出现 `.venv1`。

### 配置和推送远程仓库

```bat
git remote -v
git remote add origin https://github.com/Duo45/GNome_Respository-for-Practice.git
git push -u origin main
```

| 命令 | 含义 |
|---|---|
| `git remote -v` | 查看已配置的远程仓库地址 |
| `git remote add origin URL` | 添加名为 `origin` 的远程仓库 |
| `git push -u origin main` | 将本地 `main` 推送到 `origin` 并建立跟踪关系 |

如果 `origin` 已存在：

```bat
git remote set-url origin https://github.com/Duo45/GNome_Respository-for-Practice.git
```

首次推送完成后，后续通常可以直接使用：

```bat
git push
```

### 修正最近一次提交说明

如果提交说明写错，并且该提交尚未推送：

```bat
git commit --amend -m "chore: initialize reproducible Python environment"
```

`--amend` 修改最近一次提交，不会创建新提交。已经推送的提交不要随意修改。

## 7. 常用命令速查

| 命令 | 作用 |
|---|---|
| `where python` | 查看 Python 搜索路径 |
| `py -0p` | 列出 Python Launcher 管理的解释器 |
| `python --version` | 查看 Python 版本 |
| `python -c "..."` | 直接执行 Python 代码 |
| `python -m venv .venv1` | 创建虚拟环境 |
| `call .venv1\Scripts\activate.bat` | 在 `cmd` 中激活环境 |
| `.\.venv1\Scripts\Activate.ps1` | 在 PowerShell 中激活环境 |
| `python -m pip --version` | 查看 pip 及包目录 |
| `python -m pip install -r requirements.txt` | 按清单安装依赖 |
| `python -m pip freeze` | 输出已安装包及版本 |
| `cd /d D:\gnome-repro` | 同时切换盘符和目录 |
| `dir /a` | 查看当前目录，包括隐藏文件 |
| `type 文件名` | 查看文本文件内容 |
| `notepad 文件名` | 打开或创建文本文件 |
| `git status` | 查看工作区和暂存区状态 |
| `git add .` | 将修改加入暂存区 |
| `git commit -m "说明"` | 创建本地提交 |
| `git log --oneline` | 查看简洁提交历史 |
| `git remote -v` | 查看远程地址 |
| `git push` | 上传本地新提交 |
| `git pull` | 拉取并整合远程提交 |

## 8. 第一天遇到的问题

| 问题 | 原因 | 解决方法 |
|---|---|---|
| `py` 不是内部或外部命令 | Python Launcher 未安装或未加入 `PATH` | 使用 `where python` 找到真实解释器 |
| `cd D:\` 后仍停留在 C 盘 | `cmd` 不会仅通过 `cd` 自动切换盘符 | 使用 `cd /d D:\gnome-repro` |
| `git status` 提示不是 Git 仓库 | 尚未执行 `git init` | 执行 `git init -b main` |
| 提交说明写成了 GitHub URL | 混淆提交说明和远程仓库地址 | 尚未推送时使用 `git commit --amend` 修正 |
| 再次提交提示 `nothing to commit` | 没有新的暂存内容 | 用 `--amend` 改说明，或先修改并用 `git add` 暂存 |

## 9. 第一天完成情况

- [x] 创建项目目录和五个子目录。
- [x] 创建 `.venv1` 虚拟环境。
- [x] 安装 NumPy。
- [x] 创建 `requirements.txt`、`README.md` 和 `.gitignore`。
- [x] 完成首次本地 Git 提交。
- [x] 确认首次提交包含 8 个文件、47 行新增内容。
- [ ] 在新终端中完成最终激活和 NumPy 导入验证。
- [ ] 将本地提交推送到 GitHub。
- [ ] 确认本地 `main` 与远程 `origin/main` 指向同一提交。

## 10. 后续固定工作流

每天开始：

```bat
cd /d D:\gnome-repro
call .venv1\Scripts\activate.bat
python -m pip install -r requirements.txt
python -c "import numpy"
git status
```

安装新依赖后：

```bat
python -m pip install 新包
python -m pip freeze > requirements.txt
type requirements.txt
```

每天结束前：

```bat
git status --short
git diff
git add .
git diff --cached
git commit -m "描述当天完成的内容"
git push
git status
```

最终目标是 `git status` 显示工作区干净，并且本地分支正确跟踪 `origin/main`。
