---
title: Rust를 사용하여 PDF에서 텍스트 추출
linktitle: PDF에서 텍스트 추출
type: docs
weight: 30
url: /ko/rust-cpp/extract-text-from-pdf/
description: 이 문서에서는 Aspose.PDF for Rust를 사용하여 PDF 문서에서 텍스트를 추출하는 다양한 방법을 설명합니다.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust를 사용한 텍스트 추출
Abstract: C++을 통해 제공되는 Aspose.PDF for Rust는 PDF 문서에서 텍스트를 추출하는 강력하고 효율적인 방법을 제공합니다. 이 라이브러리는 여러 추출 기술을 지원하여 사용자가 전체 문서, 특정 페이지 또는 PDF 내의 사전 정의된 영역에서 텍스트를 가져올 수 있도록 합니다.
SoftwareApplication: rust-cpp
---

## PDF 문서에서 텍스트 추출

PDF 문서에서 텍스트를 추출하는 것은 매우 일반적이고 유용한 작업입니다. PDF에는 접근, 분석 또는 다양한 목적을 위해 처리해야 하는 중요한 정보가 자주 포함되어 있습니다. 텍스트를 추출하면 데이터베이스, 보고서 또는 기타 문서에서 보다 쉽게 재사용할 수 있습니다.

텍스트를 추출하면 PDF 내용이 검색 가능해져 사용자가 전체 문서를 수동으로 검토하지 않고도 특정 정보를 빠르게 찾을 수 있습니다.

PDF 문서에서 텍스트를 추출하려는 경우, 다음을 사용할 수 있습니다 [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) 함수.
Rust를 사용하여 PDF 파일에서 텍스트를 추출하기 위한 아래 코드 스니펫을 확인하십시오.

1. 주어진 파일 이름으로 PDF 문서를 엽니다.
1. [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) PDF 문서에서 텍스트 내용을 추출합니다.
1. 추출된 텍스트를 콘솔에 출력합니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Return the PDF-document contents as plain text
        let txt = pdf.extract_text()?;

        // Print extracted text
        println!("Extracted text:\n{}", txt);

        Ok(())
    }
```