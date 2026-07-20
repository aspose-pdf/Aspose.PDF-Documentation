---
title: 如何通过 C++ 为 Rust 安装 Aspose.PDF
linktitle: 安装
type: docs
weight: 20
url: /zh/rust-cpp/installation/
description: 本节展示了产品描述以及在您自己的环境中安装 Aspose.PDF for Rust 的说明。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust 安装指南
Abstract: Aspose.PDF for Rust via C++ 安装指南提供了逐步说明，以在带有 C++ 集成的 Rust 项目中安装和配置该库。它涵盖了各种安装方式，包括手动设置以及使用像 NuGet 这样的包管理器。该指南还概述了系统要求、依赖项和必要的配置步骤，以确保在开发环境中实现无缝集成。本文件帮助开发者有效地在 Rust via C++ 中创建、读取和操作 PDF 文档。
SoftwareApplication: rust-cpp
---

## 安装

### 从 Aspose 网站安装

此软件包包括一个大型文件，存储为 bzip2 存档。

1. **下载** 存档 **Aspose.PDF for Rust via C++**，来源于官方 Aspose 网站。
   最新（最近）的版本列在顶部，默认情况下点击 **Download** 按钮时会下载该版本。
   建议使用此最新版本。如有需要，仅下载之前的版本。
   示例： `Aspose.PDF-for-Rust-via-CPP-25.6.zip`

   存档文件名的格式是： `Aspose.PDF-for-Rust-via-CPP-YY.M.zip`，其中：
   - `YY` = 年份的最后两位（例如， `25` 用于 2025)
   - `M` = 月号 来自 `1` 到 `12`

2. **提取** 存档到您选择的目录 `{path}` 使用合适的工具：

   - 在 Linux/macOS 上：

     ```bash
     unzip Aspose.PDF-for-Rust-via-CPP-YY.M.zip -d {path}
     ```

   - 在 Windows 上，使用内置的 Explorer 解压功能或任何解压工具（7-Zip、WinRAR）。

3. **添加** 库作为依赖到你的 Rust 项目中。你可以通过两种方式实现：

   - **使用命令行:**

     ```bash
     cargo add asposepdf --path {path}/asposepdf
     ```

   - **手动编辑 `Cargo.toml`:**
     打开你的项目 `Cargo.toml` 并在以下位置添加 `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { path = "{path}/asposepdf" }
     ```

4. **构建你的项目** (`cargo build`). 在第一次构建时，适用于您平台的相应动态库将自动从 the 中提取。 `.bz2` 存档在 `lib` 文件夹并链接到您的项目。

**注释**

- 构建脚本尝试在您的输出目录中创建一个 **符号链接** 指向库（例如， `target/debug/`).
- 对于 **Linux 和 macOS**，您还必须遵循 [运行时配置](#runtime-configuration) 下面的章节确保可执行文件在运行时能够找到库。
- 全部 `.bz2` 档案具有对应的 `.sha256` 校验和文件。如果校验和缺失或无效，构建将失败。

### 从 GitHub 安装

此软件包包含预编译的本机库（`.dll`, `.so`, `.dylib`) 这些被压缩存储 `.bz2` GitHub 仓库内的归档。

1. **添加** 库作为依赖到你的 Rust 项目中。你可以通过两种方式实现：

   - **使用命令行:**

     ```bash
     cargo add asposepdf --git https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git
     ```

   - **手动编辑 `Cargo.toml`:**

     打开你的项目 `Cargo.toml` 并在以下位置添加 `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git" }
     ```

    > **注意:** 要使用特定的发布版本，您可以指定标签:
    >
    > ```toml
    > asposepdf = { git = \"https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git", tag = "v1.26.1" }
    > ```

2. **构建你的项目** (`cargo build`). 在第一次构建时，适用于您平台的相应动态库将自动从 the 中提取。 `.bz2` 存档在 `lib` 文件夹并链接到您的项目。

**注释**

- 您无需手动下载或提取任何文件——所有内容都已包含在 GitHub 仓库中。
- 构建脚本尝试在您的输出目录中创建一个 **符号链接** 指向库（例如， `target/debug/`).
- 对于 **Linux 和 macOS**，您还必须遵循 [运行时配置](#runtime-configuration) 下面的章节确保可执行文件在运行时能够找到库。
- 全部 `.bz2` 档案匹配 `.sha256` 校验文件。校验和在解压前进行验证。
- 如果校验和验证失败或归档缺失，构建将以详细错误信息失败。

### 从 crates.io 安装

此软件包可在 [crates.io](https://crates.io/crates/asposepdf). 
由于大小限制，已发布的 crate 不包含本机二进制库 ("`.dll`, `.so`, 或 `.dylib`).
您可以从官方分发档案（请参见 [从 Aspose 网站安装](#installation-from-aspose-website)) 或从 GitHub 仓库（参见 [从 GitHub 安装](#installation-from-github)).
构建脚本将在构建过程中定位、验证并从压缩的 .bz2 存档中提取适当的本机库。

1. **添加** 库作为依赖到你的 Rust 项目中。你可以通过两种方式实现：

   - **使用命令行:**

     ```bash
     cargo add asposepdf
     ```

   - **手动编辑 `Cargo.toml`:**

     打开你的项目 `Cargo.toml` 并在以下位置添加 `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = "1.26.1"
     ```

2. **设置路径** 到包含本机库的目录，并下载所需文件：

   - **设置环境变量 `ASPOSE_PDF_LIB_DIR`** 指向您将放置本机文件的文件夹 `.bz2` 档案，它们的 `.sha256` 校验和文件，以及提取的本机库（`.dll`, `.so`, `.dylib`，以及 Windows 同样适用 `.lib`):

     - 在 Linux/macOS 上:

       ```bash
       export ASPOSE_PDF_LIB_DIR=/path/to/lib
       ```

     - 在 Windows（命令提示符）:

       ```cmd
       set ASPOSE_PDF_LIB_DIR=C:\path\to\lib
       ```

     - 在 Windows (PowerShell)：
     
       ```powershell
       $env:ASPOSE_PDF_LIB_DIR = "C:\path\to\lib"
       ```

**关于 ASPOSE_PDF_LIB_DIR 的注释**

该 `ASPOSE_PDF_LIB_DIR` 环境变量定义了构建脚本的工作目录。它仅在**编译期间**用于定位、验证和提取本机库归档。设置此变量**不会**自动将该目录添加到系统的运行时库搜索路径（见 [运行时配置](#runtime-configuration)).

  - **下载所需的** `.bz2` archives** 和 checksum 文件 来自 GitHub 仓库的 [`lib/` 文件夹](https://github.com/aspose-pdf/aspose-pdf-rust-cpp/tree/main/lib) 并将**它们**放入已设置的文件夹中 `ASPOSE_PDF_LIB_DIR`:

  - 对于 **Linux x64**，下载：
    - `libAsposePDFforRust_linux_amd64.so.bz2`
    - `libAsposePDFforRust_linux_amd64.so.bz2.sha256`

  - 对于 **macOS x86_64**，下载:
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2`
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2.sha256`

  - 对于 **macOS arm64**，下载：
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2`
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2.sha256`

  - 对于 **Windows x64**，下载：
    - `AsposePDFforRust_windows_amd64.dll.bz2`
    - `AsposePDFforRust_windows_amd64.dll.bz2.sha256`
    - `AsposePDFforRust_windows_amd64.lib` （本机导入库，未压缩）

**注意：** 您需要手动从 GitHub 下载这些文件，并将它们放入所指向的目录中 `ASPOSE_PDF_LIB_DIR`.  
构建脚本将自动从中解压本机库 `.bz2` 首次构建时的归档。

3. **构建** 你的项目 (`cargo build`). 在第一次构建时，将自动从该提取与您的平台匹配的本机库 `.bz2` 归档并链接到您的项目。

**重要：** 对于 **Linux 和 macOS**，您还必须遵循 [运行时配置](#runtime-configuration) 下面的章节确保可执行文件在运行时能够找到库。

**注释**

- 该 `ASPOSE_PDF_LIB_DIR` 变量仅在**构建过程中**用于定位和提取存档。
- 构建脚本尝试在您的输出目录中创建指向已提取库的 **符号链接**（例如， `target/debug/`).
- 您必须提供包含的文件夹 `.bz2` 和 `.sha256` 将文件单独处理，因为这些二进制归档未通过 crates.io 分发。
- 如果所需的归档缺失或校验和不通过，构建将因详细错误而失败。
- 通过 GitHub 或 Aspose 网站用于安装的相同二进制文件可以在此处重复使用。

## 快速入门

所有代码片段都包含在 [代码片段](https://onedrive.live.com/examples).