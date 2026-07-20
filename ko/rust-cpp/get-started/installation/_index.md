---
title: Rust용 Aspose.PDF를 C++를 통해 설치하는 방법
linktitle: 설치
type: docs
weight: 20
url: /ko/rust-cpp/installation/
description: 이 섹션에서는 제품 설명과 Aspose.PDF for Rust를 직접 설치하는 방법에 대한 지침을 보여줍니다.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust 설치 가이드
Abstract: Aspose.PDF for Rust via C++ 설치 가이드는 Rust 프로젝트에서 C++ 통합을 사용하여 라이브러리를 설치하고 구성하는 단계별 지침을 제공합니다. 여기에는 수동 설정 및 NuGet과 같은 패키지 관리자를 사용하는 다양한 설치 방법이 포함됩니다. 또한 이 가이드는 시스템 요구 사항, 종속성 및 원활한 통합을 보장하기 위한 필수 구성 단계를 설명합니다. 이 문서는 개발자가 Rust via C++에서 PDF 문서를 효과적으로 생성, 읽기 및 조작하는 데 도움이 됩니다.
SoftwareApplication: rust-cpp
---

## 설치

### Aspose 웹사이트에서 설치

이 패키지에는 bzip2 압축 파일로 저장된 대용량 파일이 포함되어 있습니다.

1. **다운로드** 아카이브 **Aspose.PDF for Rust via C++** 공식 Aspose 웹사이트에서.
   가장 최신(가장 최근) 버전이 상단에 표시되며, **Download** 버튼을 클릭하면 기본적으로 다운로드됩니다.
   최신 버전을 사용하는 것이 권장됩니다. 필요할 경우에만 이전 버전을 다운로드하십시오.
   예시: `Aspose.PDF-for-Rust-via-CPP-25.6.zip`

   아카이브 파일 이름 형식은: `Aspose.PDF-for-Rust-via-CPP-YY.M.zip`, 어디:
   - `YY` = 연도의 마지막 두 자리 (예: `25` 2025년용)
   - `M` = 월 번호부터 `1` 에 `12`

2. **추출** 아카이브를 선택한 디렉터리로 `{path}` 적절한 도구를 사용하여:

   - Linux/macOS에서:

     ```bash
     unzip Aspose.PDF-for-Rust-via-CPP-YY.M.zip -d {path}
     ```

   - Windows에서는 기본 제공 Explorer 추출을 사용하거나 압축 해제 도구(7-Zip, WinRAR)를 사용하십시오.

3. **Add** 라이브러리를 Rust 프로젝트에 종속성으로 추가하십시오. 두 가지 방법으로 할 수 있습니다:

   - **명령줄 사용:**

     ```bash
     cargo add asposepdf --path {path}/asposepdf
     ```

   - **수동 편집 `Cargo.toml`:**
     프로젝트를 엽니다 `Cargo.toml` 아래에 다음을 추가 `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { path = "{path}/asposepdf" }
     ```

4. **프로젝트를 빌드** (`cargo build`). 첫 번째 빌드 시, 플랫폼에 적합한 동적 라이브러리가 자동으로 추출됩니다 `.bz2` 아카이브 안에 `lib` 폴더와 프로젝트에 연결되었습니다.

**노트**

- 빌드 스크립트는 출력 디렉터리(예:,)에 라이브러리의 **symbolic link**를 만들려고 시도합니다 `target/debug/`).
- **Linux 및 macOS**에 대해, 귀하는 또한 다음을 따라야 합니다. [런타임 구성](#runtime-configuration) 실행 파일이 런타임에 라이브러리를 찾을 수 있도록 아래 섹션을 확인하십시오.
- 모두 `.bz2` 아카이브는 해당됩니다 `.sha256` 체크섬 파일. 체크섬이 누락되었거나 잘못된 경우, 빌드가 실패합니다.

### GitHub에서 설치

이 패키지에는 사전 컴파일된 네이티브 라이브러리가 포함되어 있습니다 ("`.dll`, `.so`, `.dylib`) 압축된 형태로 저장됩니다 `.bz2` GitHub 리포지토리 내부의 아카이브.

1. **Add** 라이브러리를 Rust 프로젝트에 종속성으로 추가하십시오. 두 가지 방법으로 할 수 있습니다:

   - **명령줄 사용:**

     ```bash
     cargo add asposepdf --git https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git
     ```

   - **수동 편집 `Cargo.toml`:**

     프로젝트를 엽니다 `Cargo.toml` 아래에 다음을 추가 `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git" }
     ```

    > **Note:** 특정 릴리스 버전을 사용하려면 태그를 지정할 수 있습니다:
    >
    > ```toml
    > asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git", 태그 = "v1.26.1" }
    > ```

2. **프로젝트를 빌드** (`cargo build`). 첫 번째 빌드 시, 플랫폼에 적합한 동적 라이브러리가 자동으로 추출됩니다 `.bz2` 아카이브 안에 `lib` 폴더와 프로젝트에 연결되었습니다.

**노트**

- 수동으로 파일을 다운로드하거나 추출할 필요가 없습니다 - 모든 것이 GitHub 저장소에 포함되어 있습니다.
- 빌드 스크립트는 출력 디렉터리(예:,)에 라이브러리의 **symbolic link**를 만들려고 시도합니다 `target/debug/`).
- **Linux 및 macOS**에 대해, 귀하는 또한 다음을 따라야 합니다. [런타임 구성](#runtime-configuration) 실행 파일이 런타임에 라이브러리를 찾을 수 있도록 아래 섹션을 확인하십시오.
- 모두 `.bz2` 아카이브가 일치합니다 `.sha256` checksum 파일. 체크섬은 압축을 풀기 전에 확인됩니다.
- 체크섬 검증에 실패하거나 아카이브가 없으면, 빌드가 상세 오류와 함께 실패합니다.

### crates.io에서 설치

이 패키지는 다음에서 사용할 수 있습니다 [crates.io](https://crates.io/crates/asposepdf). 
크기 제한으로 인해, 배포된 크레이트에는 네이티브 바이너리 라이브러리가 포함되지 않습니다 (`.dll`, `.so`, 또는 `.dylib`).
필요한 기본 라이브러리는 공식 배포 아카이브 (see [Aspose 웹사이트에서 설치](#installation-from-aspose-website)) 또는 GitHub 저장소에서 (참조 [GitHub에서 설치](#installation-from-github)).
빌드 스크립트는 빌드 과정에서 압축된 .bz2 아카이브에서 적절한 네이티브 라이브러리를 찾고, 확인하며, 추출합니다.

1. **Add** 라이브러리를 Rust 프로젝트에 종속성으로 추가하십시오. 두 가지 방법으로 할 수 있습니다:

   - **명령줄 사용:**

     ```bash
     cargo add asposepdf
     ```

   - **수동 편집 `Cargo.toml`:**

     프로젝트를 엽니다 `Cargo.toml` 아래에 다음을 추가 `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = "1.26.1"
     ```

2. **경로 설정**: 네이티브 라이브러리를 포함하는 디렉터리로 설정하고 필요한 파일을 다운로드하십시오.

   - **환경 변수 설정 `ASPOSE_PDF_LIB_DIR`** 네이티브를 배치할 폴더를 가리키도록 `.bz2` 아카이브, 그들의 `.sha256` 체크섬 파일, 및 추출된 네이티브 라이브러리 (`.dll`, `.so`, `.dylib`, 그리고 Windows용도 `.lib`):

     - Linux/macOS에서:

       ```bash
       export ASPOSE_PDF_LIB_DIR=/path/to/lib
       ```

     - Windows에서 (명령 프롬프트):

       ```cmd
       set ASPOSE_PDF_LIB_DIR=C:\path\to\lib
       ```

     - Windows에서 (PowerShell):
     
       ```powershell
       $env:ASPOSE_PDF_LIB_DIR = "C:\path\to\lib"
       ```

**ASPOSE_PDF_LIB_DIR에 대한 참고**

그 `ASPOSE_PDF_LIB_DIR` 환경 변수는 빌드 스크립트의 작업 디렉터리를 정의합니다. 이 변수는 **컴파일 중에만** 사용되어 네이티브 라이브러리 아카이브를 찾고, 검증하고, 추출합니다. 이 변수를 설정해도 **자동으로** 디렉터리가 시스템의 런타임 라이브러리 검색 경로에 추가되지는 않습니다 (see [런타임 구성](#runtime-configuration)).

  - **필요한 항목 다운로드** `.bz2` archives** 및 체크섬 파일을 GitHub 리포지토리의 [`lib/` 폴더](https://github.com/aspose-pdf/aspose-pdf-rust-cpp/tree/main/lib) 그리고 **그것들을** 설정된 폴더에 넣으세요 `ASPOSE_PDF_LIB_DIR`:

  - **Linux x64**용, 다운로드:
    - `libAsposePDFforRust_linux_amd64.so.bz2`
    - `libAsposePDFforRust_linux_amd64.so.bz2.sha256`

  - 다음 **macOS x86_64** 용으로 다운로드:
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2`
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2.sha256`

  - **macOS arm64**용 다운로드:
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2`
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2.sha256`

  - **Windows x64**용, 다운로드:
    - `AsposePDFforRust_windows_amd64.dll.bz2`
    - `AsposePDFforRust_windows_amd64.dll.bz2.sha256`
    - `AsposePDFforRust_windows_amd64.lib` (네이티브 가져오기 라이브러리, 압축되지 않음)

**주의:** GitHub에서 이 파일들을 수동으로 다운로드하고 지정된 디렉터리에 배치해야 합니다. `ASPOSE_PDF_LIB_DIR`.  
빌드 스크립트는 네이티브 라이브러리를 자동으로 풀어냅니다. `.bz2` 첫 번째 빌드 시 아카이브.

3. **빌드** 귀하의 프로젝트 (`cargo build`). 첫 번째 빌드 시, 플랫폼에 맞는 네이티브 라이브러리가 자동으로 해당 위치에서 추출됩니다. `.bz2` 아카이브되고 프로젝트에 연결됩니다.

**중요:** **Linux 및 macOS**에 대해, 귀하는 또한 다음을 따라야 합니다. [런타임 구성](#runtime-configuration) 실행 파일이 런타임에 라이브러리를 찾을 수 있도록 아래 섹션을 확인하십시오.

**노트**

- 그 `ASPOSE_PDF_LIB_DIR` 변수는 **빌드 과정 중에만** 아카이브를 찾고 추출하는 데 사용됩니다.
- 빌드 스크립트는 추출된 라이브러리에 대한 **심볼릭 링크**를 출력 디렉터리(예:,)} `target/debug/`).
- 포함하는 폴더를 제공해야 합니다 `.bz2` 그리고 `.sha256` 파일을 별도로, 이러한 바이너리 아카이브는 crates.io를 통해 배포되지 않기 때문입니다.
- 필수 아카이브가 없거나 체크섬이 실패하면, 빌드가 상세 오류와 함께 실패합니다.
- GitHub 또는 Aspose 웹사이트를 통해 설치에 사용된 동일한 바이너리 파일을 여기에서 재사용할 수 있습니다.

## 빠른 시작

모든 코드 스니펫은 다음에 포함됩니다 [스니펫](https://onedrive.live.com/examples).