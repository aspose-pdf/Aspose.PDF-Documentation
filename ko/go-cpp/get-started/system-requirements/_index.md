---
title: 시스템 요구 사항
linktitle: 시스템 요구 사항
type: docs
weight: 30
url: /ko/go-cpp/system-requirements/
description: 이 섹션에서는 개발자가 Aspose.PDF for Go를 성공적으로 사용하기 위해 필요한 지원 운영 체제를 나열합니다.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go 시스템 요구 사항 페이지
Abstract: Aspose.PDF for Go의 시스템 요구 사항 페이지는 다양한 플랫폼에 라이브러리를 설정하기 위한 필수 세부 정보를 제공합니다. 여기에는 지원되는 운영 체제, 시스템 종속성 및 하드웨어 구성과 같은 필수 환경 설정이 포함되어 있어 라이브러리의 성공적인 설치와 최적의 성능을 보장합니다. 또한 지원되는 Go 버전과 같은 소프트웨어 선행 조건 및 다양한 시스템에서 라이브러리를 효과적으로 실행하기 위해 필요한 추가 구성에 대한 정보도 포함됩니다. 이 정보는 개발자가 개발 환경을 올바르게 설정하는 데 도움을 줍니다.
SoftwareApplication: go-cpp
---

## C++를 통한 Aspose.PDF for Go 지원 플랫폼

asposepdf 패키지는 개발자가 PDF 파일을 직접 조작할 수 있도록 하는 강력한 툴킷이며 PDF와 관련된 다양한 작업을 수행하는 데 도움을 줍니다.
PDF를 다른 형식으로 변환하기 위한 고유한 기능을 포함합니다.

Linux x64, macOS x86_64, macOS arm64 및 Windows x64 플랫폼에 대한 지원을 구현했습니다. 사용 [cgo](https://go.dev/wiki/cgo).

패키지 루트 디렉터리의 ‘lib’ 폴더에 있는 동적 라이브러리의 플랫폼 별 버전이 결과 애플리케이션을 배포하기 위해 필요합니다:

- **libAsposePDFforGo_linux_amd64.so**는 Linux x64 플랫폼용입니다.
- **libAsposePDFforGo_darwin_arm64.dylib**는 macOS arm64 플랫폼용입니다.
- **libAsposePDFforGo_darwin_amd64.dylib** - macOS x86_64 플랫폼용.
- **AsposePDFforGo_windows_amd64.dll** - Windows x64 플랫폼용.

Windows x64 플랫폼은 필요합니다 [MinGW-W64](https://www.mingw-w64.org/) 설치되었습니다