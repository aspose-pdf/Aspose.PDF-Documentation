---
title: Rust를 사용하여 PDF에 헤더와 푸터 추가
linktitle: PDF에 헤더와 푸터 추가
type: docs
weight: 90
url: /ko/rust-cpp/add-headers-and-footers-of-pdf-file/
description:
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rust를 사용하여 PDF에 헤더와 푸터를 추가하는 방법
Abstract: 이 문서는 asposepdf Rust 라이브러리를 사용하여 PDF 문서에 텍스트 헤더와 푸터를 추가하는 방법을 보여줍니다. 기존 PDF를 열고, 모든 페이지의 헤더 또는 푸터에 일관된 텍스트를 삽입한 다음, 수정된 문서를 새 파일로 저장하는 방법을 설명합니다. 예제들은 페이지 번호, 제목 또는 브랜드와 같은 작업을 Rust 애플리케이션에서 프로그래밍 방식으로 추가할 수 있는 간단하고 오류 방지 워크플로를 보여줍니다.
SoftwareApplication: rust-cpp
---

## 헤더와 푸터를 텍스트 조각으로 추가

### PDF 문서의 푸터에 텍스트 추가

우리 도구를 사용하면 기존 PDF를 열고, 모든 페이지에 텍스트 바닥글을 추가한 다음, asposepdf Rust 라이브러리를 사용하여 수정된 PDF를 새 파일로 저장할 수 있습니다. Rust의 Result 타입을 사용하여 오류를 우아하게 처리합니다.

1. 기존 PDF 문서를 엽니다.
1. 다음으로 바닥글에 텍스트를 추가합니다 [add_text_footer](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_footer/).
1. 수정된 PDF를 저장합니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Footer of a PDF-document
        pdf.add_text_footer("FOOTER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_footer.pdf")?;

        Ok(())
    }
```

### PDF 문서의 헤더에 텍스트 추가

이 코드 조각은 기존 PDF 파일을 열고, 모든 페이지에 텍스트 헤더를 추가한 다음, asposepdf 라이브러리를 사용하여 수정된 문서를 새 파일로 저장하는 방법을 보여줍니다. 이는 PDF에 일관된 헤더를 삽입하는 간단하고 자동화된 방법을 제공합니다.

1. 기존 PDF를 엽니다.
1. 도움을 사용하여 헤더에 텍스트를 추가합니다 [add_text_header](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_header/).
1. 수정된 PDF를 저장합니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Header of a PDF-document
        pdf.add_text_header("HEADER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_header.pdf")?;

        Ok(())
    }
```