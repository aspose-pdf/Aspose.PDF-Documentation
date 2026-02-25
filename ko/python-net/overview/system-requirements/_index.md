---
title: 시스템 요구 사항
linktitle: 시스템 요구 사항
type: docs
weight: 30
url: /ko/python-net/system-requirements/
description: 이 섹션에서는 개발자가 Aspose.PDF for Python을 성공적으로 사용하기 위해 필요한 지원 운영 체제를 나열합니다.
lastmod: "2025-02-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: .NET을 통한 Aspose.PDF for Python 지원 운영 체제
Abstract: Aspose.PDF for Python via .NET은 개발자가 Microsoft Office 또는 Adobe Acrobat Automation 없이 PDF 문서를 관리할 수 있도록 설계된 PDF 처리 API입니다. 이 API는 Python 3.5 이상이 설치된 Windows 및 Linux 등 다양한 운영 체제에서 32비트 및 64비트 Python 응용 프로그램 개발을 지원합니다. API는 Windows XP부터 Windows 11까지의 여러 Windows 버전과 Ubuntu, OpenSUSE, CentOS와 같은 주요 Linux 배포판과 호환됩니다. Linux 시스템의 경우 GCC-6 런타임 라이브러리, .NET Core Runtime의 종속성(런타임 자체는 필요 없음), Python 3.5-3.7 버전을 위한 pymalloc 빌드가 특정 요구 사항에 포함됩니다. 또한 공유 libpython 라이브러리가 필요하며, 올바른 라이브러리 경로 인식을 위해 구성 조정이 필요할 수 있습니다.
---

## 개요

Aspose.PDF for Python via .NET은 개발자가 Microsoft Office® 또는 Adobe Acrobat Automation 없이 PDF 문서를 작업할 수 있도록 하는 PDF 처리 API입니다. Aspose.PDF for Python은 Python 3.5 이상이 설치된 다양한 운영 체제(예: Windows 및 Linux)용 32비트 및 64비트 Python 응용 프로그램 개발에 사용할 수 있습니다.

## 지원되는 운영 체제

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
- 및 기타

## 대상 Linux에 대한 시스템 요구 사항

- GCC-6 런타임 라이브러리(이후 버전).

- .NET Core Runtime의 종속성. .NET Core Runtime 자체를 설치할 필요는 없습니다.

- Python 3.5-3.7의 경우: Python의 pymalloc 빌드가 필요합니다. --with-pymalloc Python 빌드 옵션은 기본적으로 활성화됩니다. 일반적으로 pymalloc 빌드된 Python은 파일명에 m 접미사가 붙어 있습니다.

- libpython 공유 Python 라이브러리. --enable-shared Python 빌드 옵션은 기본적으로 비활성화되어 있으며, 일부 Python 배포판에는 libpython 공유 라이브러리가 포함되지 않을 수 있습니다. 일부 Linux 플랫폼에서는 패키지 관리자를 통해 libpython 공유 라이브러리를 설치할 수 있습니다. 예: sudo apt-get install libpython3.7. 일반적인 문제는 libpython 라이브러리가 표준 시스템 공유 라이브러리 위치와 다른 곳에 설치된다는 점입니다. 이 문제는 Python을 컴파일할 때 Python 빌드 옵션을 사용해 대체 라이브러리 경로를 설정하거나, 시스템 표준 공유 라이브러리 위치에 libpython 라이브러리 파일에 대한 심볼릭 링크를 생성하여 해결할 수 있습니다. 일반적으로 libpython 공유 라이브러리 파일 이름은 Python 3.5-3.7의 경우 libpythonX.Ym.so.1.0이며, Python 3.8 이상에서는 libpythonX.Y.so.1.0입니다(예: libpython3.7m.so.1.0, libpython3.9.so.1.0).



