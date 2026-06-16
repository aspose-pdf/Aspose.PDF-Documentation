---
title: 系统需求
linktitle: 系统需求
type: docs
weight: 30
url: /zh/python-net/system-requirements/
description: 本节列出了开发人员成功使用 Aspose.PDF for Python 所需的受支持操作系统。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python via .NET 的受支持操作系统
Abstract: Aspose.PDF for Python via .NET 是一个 PDF 处理 API，旨在帮助开发人员在无需 Microsoft Office 或 Adobe Acrobat Automation 的情况下管理 PDF 文档。它支持在包括 Windows 和 Linux 在内的各种操作系统上开发 32 位和 64 位的 Python 应用程序，前提是已安装 Python 3.5 或更高版本。该 API 与多个 Windows 版本兼容，范围从 Windows XP 到 Windows 11，并且兼容主要的 Linux 发行版，如 Ubuntu、OpenSUSE 和 CentOS。对于 Linux 系统，具体要求包括 GCC-6 运行时库、.NET Core Runtime 的依赖项（无需 runtime 本身）以及 Python 3.5-3.7 的 pymalloc 构建。此外，还需要共享的 libpython 库，可能需要进行配置调整以正确识别库路径。
---

## 概述

Aspose.PDF for Python via .NET，PDF 处理 API，允许开发者在无需 Microsoft Office® 或 Adobe Acrobat 自动化的情况下处理 PDF 文档。Aspose.PDF for Python 可用于在不同操作系统（如 Windows 和 Linux）上开发 32 位和 64 位的 Python 应用程序，只要安装了 Python 3.5 或更高版本。

## 支持的操作系统

### Windows

- Windows 2003 Server
- Windows 2008 Server
- Windows 2012 Server
- Windows 2012 R2 服务器
- Windows 2016 服务器
- Windows 2019 服务器
- Windows XP
- Windows Vista
- Windows 7
- Windows 8，8.1
- Windows 10
- Windows 11

### Linux

- Ubuntu
- OpenSUSE
- CentOS
- 以及其他

## 目标 Linux 的系统要求

- GCC-6 运行时库（或更高版本）。

- .NET Core Runtime 的依赖项。不需要安装 .NET Core Runtime 本身。

- 对于 Python 3.5-3.7：需要使用 pymalloc 构建的 Python。默认启用 --with-pymalloc Python 构建选项。通常，使用 pymalloc 构建的 Python 在文件名中会带有 m 后缀。

- libpython 共享 Python 库。默认情况下，--enable-shared Python 构建选项是关闭的，一些 Python 发行版不包含 libpython 共享库。对于某些 Linux 平台，可以使用软件包管理器安装 libpython 共享库，例如：`sudo apt-get install libpython3.7`。常见的问题是 libpython 库被安装在与系统共享库标准位置不同的目录下。可以通过在编译 Python 时使用 Python 构建选项设置替代库路径来解决此问题，或者通过在系统共享库标准位置创建指向 libpython 库文件的符号链接来解决。通常，libpython 共享库文件名为 Python 3.5-3.7 的 `libpythonX.Ym.so.1.0`，或 Python 3.8 及以后版本的 `libpythonX.Y.so.1.0`（例如：`libpython3.7m.so.1.0`、`libpython3.9.so.1.0`）。


