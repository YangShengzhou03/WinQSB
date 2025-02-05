# 64位 WinQSB 安装向导 开发文档

## 项目概述

### 项目名称
64位 WinQSB 安装向导

### 项目目标
本项目旨在提供一个简单易用的安装向导，用于在64位Windows操作系统上安装并运行WinQSB软件。通过集成OTVDM（Open Tapioca Virtual DOS Machine），确保WinQSB能够在现代64位系统中正常运行。

## 项目文件结构


### 文件说明

#### 根目录
- **build**: 编译输出目录。
- **dist**: 打包后的可执行文件输出目录。
- **License**: 许可证文件。
- **resource**: 资源文件目录。
- **venv**: Python虚拟环境目录。

#### 源代码文件
- **App.py**: 主应用程序入口文件。
- **App.spec**: PyInstaller 生成的配置文件。
- **CheckVCRuntimesThread.py**: 检查VC运行时线程的脚本。
- **common.py**: 公共函数和工具类。
- **init.py**: 初始化文件。
- **MainGui.py**: 主界面逻辑文件。
- **OT_MainGui.ui**: 主界面的UI文件（使用Qt Designer设计）。
- **MyMainWindow.py**: 自定义主窗口类。
- **WinQSB version info.txt**: WinQSB 版本信息文件。

#### 文档文件
- **开发文档.md**: 项目开发文档。
- **开发环境.md**: 项目开发环境配置文档。

## 实现原理

### 安装流程
1. **启动安装向导**：用户启动安装向导后，首先会看到欢迎界面。
2. **秘钥验证**：
   - 生成一个随机数。
   - 将该随机数加1。
   - 将结果转换为16进制字符串作为秘钥。
   - 用户输入秘钥进行验证。
   - 验证通过后，继续下一步。
3. **运行OTVDM**：启动OTVDM虚拟机。
4. **运行WinQSB**：在OTVDM中启动WinQSB软件。

### 秘钥验证方法
1. **生成随机数**：使用系统随机数生成器生成一个随机整数。
2. **计算秘钥**：将随机数加1，然后将结果转换为16进制字符串。
3. **用户输入**：用户输入秘钥进行验证。
4. **验证逻辑**：将用户输入的秘钥与计算出的秘钥进行比较，如果匹配则验证通过，否则提示错误。

### 技术栈
- **Python**：主要编程语言
- **PyQt6**：图形用户界面库
- **OTVDM**：虚拟DOS环境
- **WinQSB**：目标应用程序

## 更新日志

### 2024年11月7日
- **优化安装包存放路径**：将安装包存放在更整齐规范的目录结构中，方便管理和维护。
- **支付窗口和联系作者窗口**：将支付窗口和联系作者窗口设计为圆角矩形，提升用户体验。
- **优化系统通知显示格式**：改进系统通知的显示格式，使其更加清晰和美观。

## 详细设计

### 目录结构
- **build**: 编译输出目录，用于存放中间文件。
- **dist**: 打包后的可执行文件输出目录，最终发布版本将存放于此。
- **License**: 许可证文件，包含项目的许可信息。
- **resource**: 资源文件目录，存放图标、样式表等资源文件。
- **venv**: Python虚拟环境目录，用于隔离项目依赖。

### 主要模块

#### `App.py`
- **功能**：主入口文件，负责初始化应用和显示主窗口。

#### `MainGui.py`
- **功能**：主界面逻辑文件，处理用户交互和业务逻辑。

#### `common.py`
- **功能**：公共函数和工具类，提供秘钥生成和验证等功能。

#### `OT_MainGui.ui`
- **功能**：主界面的UI文件，使用Qt Designer设计。

#### `MyMainWindow.py`
- **功能**：自定义主窗口类，扩展主界面的功能。

#### `WinQSB version info.txt`
- **功能**：记录WinQSB的版本信息。

D:\code\Pythonly winQs
├── build
├── dist
├── License
├── resource
├── venv
├── App.py
├── App.spec
├── CheckVCRuntimesThread.py
├── common.py
├── init.py
├── MainGui.py
├── OT_MainGui.ui
├── MyMainWindow.py
├── WinQSB version info.txt
├── 开发文档.md
└── 开发环境.md