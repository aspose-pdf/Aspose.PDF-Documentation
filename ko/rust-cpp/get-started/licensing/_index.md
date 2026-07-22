---
title: Aspose PDF 라이선스
linktitle: 라이선스 및 제한 사항
type: docs
weight: 90
url: /ko/rust-cpp/licensing/
description: Aspose. PDF for Rust는 고객에게 클래식 라이선스를 얻도록 권장합니다. 제품을 더 잘 탐색하기 위해 제한된 라이선스를 사용할 수도 있습니다.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: C++를 통한 Aspose.PDF for Rust 라이선스
Abstract: C++를 통한 Aspose.PDF for Rust 라이선스 페이지는 제품에 사용할 수 있는 라이선스 옵션을 설명합니다. 고객은 클래식 라이선스, 메터드 라이선스 또는 평가용 제한 라이선스 중에서 선택할 수 있습니다. 이 페이지는 정식 라이선스를 취득함으로써 전체 기능을 활용하고 평가 제한을 제거하는 등의 이점을 강조합니다.
SoftwareApplication: rust-cpp
---

## 라이선스

- **Rust source code**는 MIT 라이선스에 따라 라이선스됩니다.
- **shared library** (AsposePDFforRust_windows_amd64.dll, libAsposePDFforRust_linux_amd64.so, libAsposePDFforRust_darwin_amd64.dylib, libAsposePDFforRust_darwin_arm64.dylib)는 독점이며 상업용 라이선스가 필요합니다. 전체 기능을 사용하려면 라이선스를 취득해야 합니다.

## 평가 버전

평가를 위해 **Aspose.PDF for Rust via C++** 를 무료로 사용할 수 있습니다. 평가 버전은 특정 제한이 있지만 제품의 거의 모든 기능을 제공합니다. 라이선스를 구매하고 라이선스를 적용하는 몇 줄의 코드를 추가하면 동일한 평가 버전이 라이선스가 적용됩니다.

- 평가 버전 제한 없이 Aspose.PDF for Rust를 테스트하려면 30일 임시 라이선스를 요청할 수 있습니다. 자세한 내용은 다음을 참조하십시오. [임시 라이선스를 받는 방법은?](https://purchase.aspose.com/temporary-license)?

### 평가 버전의 제한 사항

고객이 구매 전에 당사 구성 요소를 충분히 테스트하길 원하므로 평가 버전에서는 일반적으로 사용하듯이 이용할 수 있습니다.

- **평가 워터마크가 있는 문서**. Aspose.PDF for Rust의 평가 버전은 전체 제품 기능을 제공하지만, 생성된 파일의 모든 페이지 상단에 \"Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd.\" 텍스트가 워터마크로 표시됩니다.
- **처리할 수 있는 페이지 수 제한**. 평가 버전에서는 문서의 처음 네 페이지만 처리할 수 있습니다.

### 프로덕션 환경에서 사용

프로덕션 환경에서는 상업 라이선스 키가 필요합니다. 상업 라이선스를 구매하려면 문의해 주세요.

### 라이선스 적용

라이선스 파일 (Aspose.PDF.RustViaCPP.lic)을 사용하여 Aspose.PDF for Rust의 전체 기능을 활성화하기 위해 라이선스를 적용합니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set license with filename
        pdf.set_license("Aspose.PDF.RustViaCPP.lic")?;

        // Now you can work with the licensed PDF document
        // ...

        Ok(())
    }
```