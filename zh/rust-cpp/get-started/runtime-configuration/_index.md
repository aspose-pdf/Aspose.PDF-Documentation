---
title: 运行时配置 Aspose.PDF for Rust via C++
linktitle: 运行时配置
type: docs
weight: 100
url: /zh/rust-cpp/runtime-configuration/
description: 依赖本机动态库（例如 Aspose.PDF）的 Rust 应用程序需要正确的运行时路径配置，才能在 Linux 和 macOS 系统上正常工作
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 为本机 Aspose.PDF for Rust 配置 RPATH
Abstract: 在 Rust 中使用本机动态库时，正确的运行时链接至关重要，以确保您的应用程序能够找到所需的依赖项。在 Linux 和 macOS 上，系统动态加载器不会自动搜索可执行文件所在的目录，除非显式配置了 RPATH。本文说明了如何配置 RPATH，使您的 Rust 应用程序在运行时能够正确定位 Aspose.PDF 本机库。文章涵盖了使用 Cargo 的项目级配置、使用 RUSTFLAGS 的基于环境的配置以及系统范围的安装选项，并附带了 Windows 行为的说明。
SoftwareApplication: rust-cpp
---

> 在 Rust 中使用本机动态库时，这是一个标准要求。

在 Linux 和 macOS 上，系统动态加载器不会自动搜索可执行文件目录，除非已配置 RPATH。为了确保您的应用程序在运行时能够找到 Aspose.PDF 本机库，您需要配置 **RPATH**（运行时搜索路径）。

我们的构建脚本会提取该库，并尝试在您的输出目录中为其创建符号链接（例如， `target/debug/`). 为了使可执行文件能够找到它，请选择以下选项之一：

## 选项 1：项目级别配置（推荐）

在您的项目根目录创建名为 `.cargo` 的目录（如果不存在），并在其中创建 `config.toml`：

```toml
[target.'cfg(target_os = "linux")']
rustflags = ["-C", "link-arg=-Wl,-rpath,$ORIGIN"]

[target.'cfg(target_os = "macos")']
rustflags = ["-C", "link-arg=-Wl,-rpath,@loader_path"]
```

## 选项 2：RUSTFLAGS 环境变量

使用以下标志构建你的项目：

```bash
# Linux
RUSTFLAGS="-C link-arg=-Wl,-rpath,\$ORIGIN" cargo build

# macOS
RUSTFLAGS="-C link-arg=-Wl,-rpath,@loader_path" cargo build
```

## 选项 3：系统范围安装（不推荐用于开发）

如果您更倾向于全局安装该库：

* **Linux:** 复制 `.so` 文件到 `/usr/local/lib` 并运行 `sudo ldconfig`.
* **macOS:** 复制 `.dylib` 文件到 `/usr/local/lib`.

> **Windows**
> 通常不需要任何操作，因为库位于相同的文件夹中 `.exe`. 或者，您可以添加包含该目录的 `.dll` 到您的系统 `PATH` 环境变量。