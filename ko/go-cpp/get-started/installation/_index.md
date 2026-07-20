---
title: C++를 사용하여 Aspose.PDF for Go 설치 방법
linktitle: 설치
type: docs
weight: 20
url: /ko/go-cpp/installation/
description: 이 섹션에서는 제품 설명과 직접 Aspose.PDF for Go를 설치하는 방법에 대한 지침을 보여줍니다.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go 설치 안내
Abstract: Aspose.PDF for Go via C++ 설치 가이드는 C++와 통합된 Go 프로젝트에서 라이브러리를 사용하기 위해 설치 및 구성하는 단계별 지침을 제공합니다. 여기서는 수동 설정 및 NuGet과 같은 패키지 관리자를 사용하는 등 다양한 설치 방법을 다룹니다. 또한 시스템 요구사항, 종속성 및 원활한 통합을 보장하기 위한 필수 구성 단계도 설명합니다. 이 문서는 개발자가 Go via C++에서 PDF 문서를 효율적으로 생성, 읽기 및 조작하는 데 도움이 됩니다.
SoftwareApplication: go-cpp
---

## 설치

이 패키지에는 bzip2 아카이브로 저장된 대용량 파일이 포함되어 있습니다.

1. 프로젝트에 asposepdf 패키지를 추가하세요:

```sh
go get github.com/aspose-pdf/aspose-pdf-go-cpp@latest
```

2. 큰 파일을 생성합니다:

- **macOS 및 linux**

1. 터미널 열기

2. Go 모듈 캐시에서 github.com/aspose-pdf의 폴더를 나열하십시오:

```sh
ls $(go env GOMODCACHE)/github.com/aspose-pdf/
```

3. 이전 단계에서 얻은 패키지의 특정 버전 폴더로 현재 폴더를 변경합니다:

```sh
cd $(go env GOMODCACHE)/github.com/aspose-pdf/aspose-pdf-go-cpp@vx.x.x
```

`@vx.x.x`를 실제 패키지 버전으로 교체하십시오.

4. 슈퍼유저 권한으로 go generate를 실행하세요:

```sh
sudo go generate
```

- **윈도우**

1. 명령 프롬프트 열기

2. Go 모듈 캐시에서 github.com/aspose-pdf의 폴더를 나열하십시오:

```cmd
for /f "delims=" %G in ('go env GOMODCACHE') do for /d %a in ("%G\github.com\aspose-pdf\*") do echo %~fa
```

3. 이전 단계에서 얻은 패키지의 특정 버전 폴더로 현재 폴더를 변경합니다:

```cmd
cd <specific version folder of the package>
```

4. go generate 실행:

```cmd
go generate
```

5. 패키지의 특정 버전 폴더를 %PATH% 환경 변수에 추가:

```cmd
setx PATH "%PATH%;<specific version folder of the package>\lib\"
```

교체 `<specific version folder of the package>` 실제 경로(2단계에서 얻은)와 함께.

## 테스트

루트 패키지 폴더에서 테스트 실행:

```sh
go test -v
```

## 빠른 시작

모든 코드 스니펫은 다음에 포함되어 있습니다 [스니펫](https://github.com/aspose-pdf/aspose-pdf-go-cpp).