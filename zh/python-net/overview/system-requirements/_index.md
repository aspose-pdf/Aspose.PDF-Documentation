---
title: 系统要求
linktitle: 系统要求
type: docs
weight: 30
url: zh/python-net/system-requirements/
description: 本节列出了开发人员需要成功使用 Aspose.PDF for Python 的支持操作系统。
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 概述

Aspose.PDF for Python via .NET 是一个 PDF 处理 API，允许开发人员在不需要 Microsoft Office® 或 Adobe Acrobat Automation 的情况下处理 PDF 文档。Aspose.PDF for Python 可用于开发适用于不同操作系统（如安装了 Python 3.5 或更高版本的 Windows 和 Linux）的 32 位和 64 位 Python 应用程序。

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

## 目标 Linux 的系统要求

- GCC-6 运行时库（或更高版本）。

- .NET Core 运行时的依赖项。不需要安装 .NET Core 运行时本身。

- 对于 Python 3.5-3.7：需要 Python 的 pymalloc 构建。--with-pymalloc Python 构建选项是默认启用的。通常，Python 的 pymalloc 构建在文件名中带有 m 后缀标记。

- libpython 共享 Python 库。
 --enable-shared Python 构建选项默认是禁用的，一些 Python 发行版不包含 libpython 共享库。对于某些 Linux 平台，可以使用包管理器安装 libpython 共享库，例如：sudo apt-get install libpython3.7。常见的问题是 libpython 库安装在与共享库的标准系统位置不同的位置。可以通过使用 Python 构建选项在编译 Python 时设置备用库路径来解决此问题，或者通过在共享库的系统标准位置为 libpython 库文件创建符号链接来解决。通常，libpython 共享库文件名为 libpythonX.Ym.so.1.0（适用于 Python 3.5-3.7），或 libpythonX.Y.so.1.0（适用于 Python 3.8 或更高版本）（例如：libpython3.7m.so.1.0，libpython3.9.so.1.0）。