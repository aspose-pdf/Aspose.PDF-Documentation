---
title: 런타임 구성 Aspose.PDF for Rust via C++
linktitle: 런타임 구성
type: docs
weight: 100
url: /ko/rust-cpp/runtime-configuration/
description: "Rust 애플리케이션이 네이티브 동적 라이브러리(예: Aspose.PDF)에 의존하는 경우, Linux 및 macOS 시스템에서 제대로 작동하려면 올바른 런타임 경로 구성이 필요합니다."
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rust용 네이티브 Aspose.PDF의 RPATH 구성
Abstract: Rust에서 네이티브 동적 라이브러리를 사용할 때, 올바른 런타임 링크는 애플리케이션이 필요한 의존성을 찾을 수 있도록 보장하는 데 필수적입니다. Linux 및 macOS에서는 시스템 동적 로더가 RPATH를 명시적으로 설정하지 않으면 실행 파일 디렉터리를 자동으로 검색하지 않습니다. 이 문서에서는 Rust 애플리케이션이 런타임에 Aspose.PDF 네이티브 라이브러리를 올바르게 찾을 수 있도록 RPATH를 설정하는 방법을 설명합니다. 여기에서는 Cargo를 사용한 프로젝트 수준 설정, RUSTFLAGS를 이용한 환경 기반 설정, 시스템 전체 설치 옵션을 다루며 Windows 동작에 대한 참고 사항도 포함합니다.
SoftwareApplication: rust-cpp
---

> 이는 Rust에서 네이티브 동적 라이브러리를 사용할 때 표준 요구 사항입니다.

Linux와 macOS에서, 시스템 동적 로더는 RPATH가 설정되지 않으면 실행 파일 디렉터리를 자동으로 검색하지 않습니다. 런타임에 Aspose.PDF 네이티브 라이브러리를 애플리케이션이 찾을 수 있도록 **RPATH**(Run-time Search Path)를 설정해야 합니다.

우리 빌드 스크립트는 라이브러리를 추출하고 출력 디렉터리(예: `target/debug/`)에 심볼릭 링크를 만들려고 시도합니다. 실행 파일이 이를 찾을 수 있도록 하려면, 다음 옵션 중 하나를 선택하십시오:

## 옵션 1: 프로젝트 수준 구성 (권장)

폴더를 이름으로 생성 `.cargo` 프로젝트 루트 디렉터리(존재하지 않을 경우)에 파일을 만들고 이름을 지정하십시오 `config.toml` 그 안에:

```toml
[target.'cfg(target_os = "linux")']
rustflags = ["-C", "link-arg=-Wl,-rpath,$ORIGIN"]

[target.'cfg(target_os = "macos")']
rustflags = ["-C", "link-arg=-Wl,-rpath,@loader_path"]
```

## 옵션 2: RUSTFLAGS 환경 변수

다음 플래그를 사용하여 프로젝트를 빌드하세요:

```bash
# Linux
RUSTFLAGS="-C link-arg=-Wl,-rpath,\$ORIGIN" cargo build

# macOS
RUSTFLAGS="-C link-arg=-Wl,-rpath,@loader_path" cargo build
```

## 옵션 3: 시스템 전체 설치 (개발에는 권장되지 않음)

전역적으로 라이브러리를 설치하고 싶다면:

* **Linux:** 복사 `.so` 파일로 `/usr/local/lib` 그리고 실행 `sudo ldconfig`.
* **macOS:** 복사 `.dylib` 파일로 `/usr/local/lib`.

> **Windows**
> 보통은 라이브러리가 동일한 폴더에 있기 때문에 별도의 조치가 필요하지 않습니다. `.exe`. 또는, 포함하는 디렉터리를 추가할 수 있습니다. `.dll` 귀하의 시스템으로 `PATH` 환경 변수.
