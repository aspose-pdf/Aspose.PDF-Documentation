---
title: System Requirements
linktitle: System Requirements
type: docs
weight: 30
url: ko/python-net/system-requirements/
description: 이 섹션은 개발자가 Aspose.PDF for Python을 성공적으로 사용하기 위해 필요한 지원 운영 체제를 나열합니다.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Overview

Aspose.PDF for Python via .NET은 개발자가 Microsoft Office® 또는 Adobe Acrobat Automation 없이 PDF 문서를 작업할 수 있도록 하는 PDF 처리 API입니다. Aspose.PDF for Python은 Python 3.5 이상이 설치된 다양한 운영 체제(Windows 및 Linux 등)에서 32비트 및 64비트 Python 응용 프로그램을 개발하는 데 사용할 수 있습니다.

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
- 기타


## System Requirements for Target Linux

- GCC-6 런타임 라이브러리(또는 이후 버전).

- .NET Core 런타임의 종속성. .NET Core 런타임 자체의 설치는 필요하지 않습니다.

- Python 3.5-3.7: Python의 pymalloc 빌드가 필요합니다. --with-pymalloc Python 빌드 옵션은 기본적으로 활성화되어 있습니다. 일반적으로, Python의 pymalloc 빌드는 파일 이름에 m 접미사가 붙어 표시됩니다.

- libpython 공유 Python 라이브러리.
 --enable-shared Python 빌드 옵션은 기본적으로 비활성화되어 있으며, 일부 Python 배포판에는 libpython 공유 라이브러리가 포함되어 있지 않습니다. 일부 리눅스 플랫폼에서는 패키지 관리자를 사용하여 libpython 공유 라이브러리를 설치할 수 있습니다. 예: sudo apt-get install libpython3.7. 일반적인 문제는 libpython 라이브러리가 공유 라이브러리에 대한 표준 시스템 위치와 다른 위치에 설치된다는 것입니다. 이 문제는 Python을 컴파일할 때 대체 라이브러리 경로를 설정하기 위해 Python 빌드 옵션을 사용하거나, 공유 라이브러리에 대한 시스템 표준 위치에 libpython 라이브러리 파일의 심볼릭 링크를 생성하여 해결할 수 있습니다. 일반적으로 libpython 공유 라이브러리 파일 이름은 Python 3.5-3.7의 경우 libpythonX.Ym.so.1.0이며, Python 3.8 이상의 경우 libpythonX.Y.so.1.0입니다 (예: libpython3.7m.so.1.0, libpython3.9.so.1.0).