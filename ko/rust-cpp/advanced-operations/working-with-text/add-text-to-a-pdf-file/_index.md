---
title: Rust를 사용하여 PDF에 텍스트 추가
linktitle: PDF에 텍스트 추가
type: docs
weight: 10
url: /ko/rust-cpp/add-text-to-pdf-file/
description: Rust에서 Aspose.PDF를 사용하여 콘텐츠 향상 및 문서 편집을 위해 PDF 문서에 텍스트를 추가하는 방법을 배우세요.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Rust용 Aspose.PDF를 사용하여 PDF에 텍스트 추가
Abstract: Aspose.PDF for C\u002B\u002B 및 Rust 문서의 Add Text to PDF File 섹션에서는 프로그래밍 방식으로 PDF 문서에 텍스트를 삽입하는 단계별 지침을 제공합니다. 여기에서는 위치 지정, 글꼴 사용자 정의, 색상 조정 및 텍스트 정렬 옵션을 포함한 다양한 텍스트 추가 방법을 다룹니다. 이 가이드는 PDF 내 특정 페이지와 위치에 텍스트를 추가하는 방법을 보여주어 정확한 콘텐츠 배치를 보장합니다. 자세한 코드 예제와 설명을 통해 개발자는 향상된 PDF 문서 관리를 위해 애플리케이션에 텍스트 삽입 기능을 손쉽게 통합할 수 있습니다.
SoftwareApplication: rust-cpp
---

기존 PDF 파일에 텍스트를 추가하려면:

1. PDF 파일을 엽니다.
1. PDF 문서에 텍스트를 추가합니다 [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/) 함수.
1. 수정을 동일한 파일에 저장합니다.

## 텍스트 추가

다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add text on page
        pdf.page_add_text(1, "added text")?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
