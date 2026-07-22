---
title: PDF 문서를 프로그래밍 방식으로 저장
linktitle: PDF 저장
type: docs
weight: 30
url: /ko/rust-cpp/save-pdf-document/
description: C++를 통한 Aspose.PDF for Rust로 PDF 파일을 저장하는 방법을 알아보세요.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: C++를 통한 Aspose.PDF for Rust로 PDF 문서를 저장
Abstract: C++를 통한 Aspose.PDF for Rust는 PDF 문서를 다양한 형식 및 위치에 고효율과 유연성으로 저장할 수 있는 포괄적인 기능을 제공합니다. 이 라이브러리를 사용하면 개발자가 PDF를 파일 시스템이나 메모리 스트림에 저장하거나 DOCX, XLSX, 이미지와 같은 다른 형식으로 출력할 수 있습니다. 저장 매개변수를 사용자 정의하고 파일 크기를 최적화하며 데이터 무결성을 보장하는 옵션을 제공합니다. 문서에는 자세한 설명과 코드 샘플이 포함되어 있어 개발자가 애플리케이션에 PDF 저장 기능을 효율적으로 구현할 수 있도록 돕습니다.
SoftwareApplication: rust-cpp
---

## PDF 문서를 파일 시스템에 저장

예제는 다음을 보여줍니다 [새로운](https://reference.aspose.com/pdf/rust-cpp/core/new/) 새 PDF 문서를 생성하는 방법으로, 보고서나 청구서와 같이 동적으로 문서를 생성하는 기본 기능입니다.

코드는 간단하며 텍스트, 이미지 또는 주석을 PDF에 추가하는 등 더 고급 기능을 위한 템플릿으로 사용할 수 있습니다.

이 예제는 Aspose.PDF Rust 라이브러리를 간단히 사용하는 방법을 보여주며, 문서를 생성, 수정 및 저장하는 잠재력을 강조합니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_new.pdf")?;

        Ok(())
    }
```
