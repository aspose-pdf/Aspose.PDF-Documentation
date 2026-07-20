---
title: Rust 언어를 사용한 Hello World 예제
linktitle: Hello World 예제
type: docs
weight: 40
url: /ko/rust-cpp/hello-world-example/
description: 이 샘플은 Aspose.PDF for Rust를 사용하여 텍스트 Hello World가 포함된 간단한 PDF 문서를 만드는 방법을 보여줍니다.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust를 통한 Hello World
Abstract: C++를 통한 Aspose.PDF for Rust 시작 가이드는 라이브러리 작업에 대한 소개를 제공하며, PDF 문서를 생성하고 조작하는 기본 단계를 다룹니다. 여기에는 텍스트 내용이 포함된 간단한 PDF 파일을 생성하는 방법을 보여주는 'Hello World' 예제가 포함되어 있어 개발자가 API의 핵심 기능을 빠르게 이해하는 데 도움이 됩니다.
SoftwareApplication: rust-cpp
---

"Hello World" 예제는 전통적으로 간단한 사용 사례를 통해 프로그래밍 언어나 소프트웨어의 기능을 소개하는 데 사용됩니다.

**Aspose.PDF for Rust**는 기능이 풍부한 PDF API로, 개발자가 Rust를 사용하여 PDF 문서 생성, 조작 및 변환 기능을 삽입할 수 있게 합니다. PDF, TXT, XLSX, EPUB, TEX, DOC, DOCX, PPTX, 이미지 형식 등 많은 인기 파일 형식을 지원합니다. 이 기사에서는 텍스트 "Hello World!"가 포함된 PDF 문서를 생성합니다. 환경에 Aspose.PDF for Rust를 설치한 후 코드 샘플을 실행하여 Aspose.PDF API가 어떻게 작동하는지 확인할 수 있습니다.
아래 코드 스니펫은 다음 단계를 따릅니다:

1. 새 PDF 문서 인스턴스를 생성합니다.
1. PDF 문서에 새 페이지를 추가하는 데 사용 [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) 함수.
1. 페이지 크기를 설정하려면 [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/).
1. 첫 번째 페이지에 "Hello World!" 텍스트를 추가하려면 [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/).
1. PDF 문서를 저장하려면 [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) 메서드.

다음 코드 스니펫은 Aspose.PDF for Rust API의 작동을 보여주기 위한 Hello World 프로그램입니다.

```rs

    use asposepdf::{Document, PageSize};
    use std::error::Error;

    fn main() -> Result<(), Box<dyn Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Add a new page
        pdf.page_add()?;

        // Set the size of the first page to A4
        pdf.page_set_size(1, PageSize::A4)?;

        // Add "Hello World!" text to the first page
        pdf.page_add_text(1, "Hello World!")?;

        // Save the PDF-document as "hello.pdf"
        pdf.save_as("hello.pdf")?;

        println!("Saved PDF-document: hello.pdf");

        Ok(())
}
```
