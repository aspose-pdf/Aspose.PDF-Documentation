---
title: 시스템 요구 사항
linktitle: 시스템 요구 사항
type: docs
weight: 30
url: /ko/python-net/system-requirements/
description: 이 섹션에는 개발자가 Python용 Aspose.PDF 작업을 성공적으로 수행하는 데 필요한 지원 운영 체제가 나열되어 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: .NET을 통한 파이썬용 Aspose.PDF 지원 운영 체제
Abstract: Python용 Aspose.PDF via .NET은 개발자가 마이크로소프트 오피스나 어도비 아크로뱃 오토메이션 없이도 PDF 문서를 관리할 수 있도록 설계된 PDF 처리 API입니다.파이썬 3.5 이상이 설치된 윈도우와 리눅스를 비롯한 다양한 운영 체제에서 32비트 및 64비트 파이썬 응용 프로그램을 개발할 수 있도록 지원합니다.API는 윈도우 XP부터 윈도우 11에 이르는 여러 윈도우 버전과 우분투, OpenSUSE, CentOS와 같은 주요 리눅스 배포판과 호환됩니다.리눅스 시스템의 경우 특정 요구 사항으로는 GCC-6 런타임 라이브러리, .NET 코어 런타임의 종속성 (런타임 자체가 필요 없음), 버전 3.5-3.7용 파이썬의 pymalloc 빌드가 있습니다.또한 공유 libpython 라이브러리가 필요하며, 이를 위해서는 올바른 라이브러리 경로 인식을 위한 구성 조정이 필요할 수 있습니다.
---

## 개요

.NET을 통한 Python용 Aspose.PDF, 개발자가 마이크로소프트 오피스® 또는 어도비 아크로뱃 오토메이션 없이도 PDF 문서로 작업할 수 있도록 하는 PDF 처리 API입니다.파이썬용 Aspose.PDF 는 파이썬 3.5 이상이 설치된 다양한 운영 체제 (예: 윈도우 및 리눅스) 용 32비트 및 64비트 파이썬 응용 프로그램을 개발하는 데 사용할 수 있습니다.

## 지원되는 운영 체제

### 윈도우

- 윈도우 2003 서버
- 윈도우 2008 서버
- 윈도우 2012 서버
- 윈도우 2012 R2 서버
- 윈도우 2016 서버
- 윈도우 2019 서버
- 윈도우 XP
- 윈도우 비스타
- 윈도우 7
- 윈도우 8, 8.1
- 윈도우 10
- 윈도우 11

### 리눅스

- 우분투
- OpenSUSE
- CentOS
- 및 기타

## 대상 Linux의 시스템 요구 사항

- GCC-6 런타임 라이브러리 (또는 그 이상)

- .NET 코어 런타임의 종속성.NET 코어 런타임 자체를 설치할 필요는 없습니다.

- 파이썬 3.5-3.7의 경우: 파이썬의 pymalloc 빌드가 필요합니다.--with-pymalloc 파이썬 빌드 옵션은 기본적으로 활성화되어 있습니다.일반적으로 파이썬의 pymalloc 빌드는 파일 이름에 m 접미사로 표시됩니다.

- libpython은 파이썬 라이브러리를 공유했습니다.--enable-shared 파이썬 빌드 옵션은 기본적으로 비활성화되어 있습니다. 일부 파이썬 배포판에는 libpython 공유 라이브러리가 포함되어 있지 않습니다.일부 리눅스 플랫폼의 경우 패키지 관리자를 사용하여 libpython 공유 라이브러리를 설치할 수 있습니다 (예: sudo apt-get install libpython3.7).일반적인 문제는 libpython 라이브러리가 공유 라이브러리의 표준 시스템 위치와 다른 위치에 설치된다는 것입니다.이 문제는 Python을 컴파일할 때 Python 빌드 옵션을 사용하여 대체 라이브러리 경로를 설정하여 해결하거나 공유 라이브러리의 시스템 표준 위치에 libpython 라이브러리 파일에 대한 심볼릭 링크를 생성하여 해결할 수 있습니다.일반적으로 libpython 공유 라이브러리 파일 이름은 파이썬 3.5-3.7의 경우 libPythonX.ym.so.1.0이고, 파이썬 3.8 이상의 경우 LibPythonX.y.SO.1.0입니다 (예: libpython3.7m.so.1.0, libpython3.9.so.1.0).


