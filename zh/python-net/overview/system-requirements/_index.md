---
title: 系统要求
linktitle: 系统要求
type: docs
weight: 30
url: /zh/python-net/system-requirements/
description: 此部分列出开发人员成功使用 Aspose.PDF for Python via .NET 所需支持的操作系统。
lastmod: "2025-02-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python via .NET 支持的操作系统
Abstract: Aspose.PDF for Python via .NET 是一个 PDF 处理 API，旨在帮助开发人员在无需 Microsoft Office 或 Adobe Acrobat 自动化的情况下管理 PDF 文档。它支持在各种操作系统上开发 32 位和 64 位的 Python 应用程序，包括已安装 Python 3.5 或更高版本的 Windows 和 Linux。该 API 兼容多个 Windows 版本，从 Windows XP 到 Windows 11，以及主要的 Linux 发行版，如 Ubuntu、OpenSUSE 和 CentOS。对于 Linux 系统，特定需求包括 GCC-6 运行时库、.NET Core Runtime 的依赖项（无需自行安装运行时本身），以及针对 Python 3.5-3.7 的 pymalloc 构建版本。此外，还需要共享的 libpython 库，可能需要进行配置调整以正确识别库路径。
---

## 概述

Aspose.PDF for Python via .NET 是一款 PDF 处理 API，允许开发人员在无需 Microsoft Office® 或 Adobe Acrobat 自动化的情况下处理 PDF 文档。Aspose.PDF for Python 可用于在不同操作系统（如 Windows 和 Linux）上开发 32 位和 64 位的 Python 应用程序，只要系统已安装 Python 3.5 或更高版本。

## 支持的操作系统

### Windows

- Windows 2003 Server
- Windows 2008 Server
- Windows 2012 Server
- Windows 2012 R2 Server
- Windows 2016 Server
- Windows 2019 Server
- Windows XP
- Windows Vista
- Windows 7
- Windows 8, 8.1
- Windows 10
- Windows 11

### Linux

- Ubuntu
- OpenSUSE
- CentOS
- 以及其他

## Linux 目标系统要求

- GCC-6 运行时库（或更高）。

- .NET Core Runtime 的依赖项。安装 .NET Core Runtime 本身并非必需。

- 对于 Python 3.5-3.7：需要 Python 的 pymalloc 构建版本。--with-pymalloc Python 构建选项默认已启用。通常，pymalloc 构建的 Python 文件名会带有 m 后缀。

- libpython 共享 Python 库。--enable-shared Python 构建选项默认是关闭的，某些 Python 发行版不包含 libpython 共享库。对于部分 Linux 平台，可使用包管理器安装 libpython 共享库，例如：sudo apt-get install libpython3.7。常见问题是 libpython 库被安装在与系统标准共享库位置不同的路径下。可以通过在编译 Python 时使用构建选项设置替代库路径，或在系统标准共享库位置创建指向 libpython 库文件的符号链接来解决。通常，libpython 共享库文件名为 libpythonX.Ym.so.1.0（针对 Python 3.5-3.7），或 libpythonX.Y.so.1.0（针对 Python 3.8 及更高版本，例如：libpython3.7m.so.1.0，libpython3.9.so.1.0）。



