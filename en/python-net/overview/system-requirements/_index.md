---
title: System Requirements
linktitle: System Requirements
type: docs
weight: 30
url: /python-net/system-requirements/
description: This section lists the supported operating systems that a developer needs to successfully work with Aspose.PDF for Python.
lastmod: "2025-02-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Supported Operating Systems of Aspose.PDF for Python via .NET
Abstract: Aspose.PDF for Python via .NET is a PDF processing API designed for developers to manage PDF documents without the need for Microsoft Office or Adobe Acrobat Automation. It supports the development of 32-bit and 64-bit Python applications on various operating systems, including Windows and Linux, where Python 3.5 or later is installed. The API is compatible with several Windows versions, from Windows XP to Windows 11, and major Linux distributions like Ubuntu, OpenSUSE, and CentOS. For Linux systems, specific requirements include GCC-6 runtime libraries, dependencies of .NET Core Runtime (without needing the runtime itself), and the pymalloc build of Python for versions 3.5-3.7. Additionally, a shared libpython library is necessary, which might require configuration adjustments for correct library path recognition.
---

## Overview

Aspose.PDF for Python via .NET, PDF Processing API that allows the developers to work with PDF documents without needing Microsoft Office® or Adobe Acrobat Automation. Aspose.PDF for Python can be used to develop 32-bit and 64-bit Python applications for different operating systems (such as Windows and Linux) where Python 3.5 or later is installed.

## Supported Operating System

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
- and others

## System Requirements for Target Linux

- GCC-6 runtime libraries (or later).

- Dependencies of .NET Core Runtime. Installing .NET Core Runtime itself is NOT required.

- For Python 3.5-3.7: The pymalloc build of Python is needed. The --with-pymalloc Python build option is enabled by default. Typically, the pymalloc build of Python is marked with m suffix in the filename.

- libpython shared Python library. The --enable-shared Python build option is disabled by default, some Python distributions do not contain the libpython shared library. For some linux platforms, the libpython shared library can be installed using the package manager, for example: sudo apt-get install libpython3.7. The common issue is that libpython library is installed in a different location than the standard system location for shared libraries. The issue can be fixed by using the Python build options to set alternate library paths when compiling Python, or fixed by creating a symbolic link to the libpython library file in the system standard location for shared libraries. Typically, the libpython shared library file name is libpythonX.Ym.so.1.0 for Python 3.5-3.7, or libpythonX.Y.so.1.0 for Python 3.8 or later (for example: libpython3.7m.so.1.0, libpython3.9.so.1.0).


