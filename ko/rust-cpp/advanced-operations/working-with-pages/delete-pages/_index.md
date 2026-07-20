---
title: Rust via C++를 사용해 PDF 페이지 삭제
linktitle: PDF 페이지 삭제
type: docs
weight: 30
url: /ko/rust-cpp/delete-pages/
description: Aspose.PDF for Rust via C++를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust를 사용하여 PDF 페이지 삭제
Abstract: Aspose.PDF for Rust via C++는 PDF 문서에서 페이지를 삭제하는 효율적인 기능을 제공하여 개발자가 원하지 않거나 불필요한 페이지를 쉽게 제거할 수 있도록 합니다. 이 라이브러리는 페이지 번호 또는 범위를 지정하여 단일 페이지 또는 여러 페이지를 삭제할 수 있게 하여 정확한 문서 수정을 보장합니다. 이 기능은 중복된 내용을 제거하고 문서 구조를 최적화함으로써 PDF 파일을 정리하는 데 도움이 됩니다. 문서에는 단계별 지침과 코드 샘플이 제공되어 개발자가 애플리케이션 내에서 페이지 삭제 기능을 효과적으로 구현할 수 있도록 지원합니다.
SoftwareApplication: rust-cpp
---

**Aspose.PDF for Rust via C++**를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다. 다음 코드 스니펫은 특정 페이지를 삭제하여 PDF 문서를 조작하는 방법을 보여줍니다. 이 방법은 페이지 제거, 수정된 문서 저장, 적절한 리소스 관리를 보장하는 등 PDF 문서 조작 작업에 효율적입니다.

1. PDF 파일 열기.
1. 특정 페이지 삭제와 [page_delete](https://reference.aspose.com/pdf/rust-cpp/core/page_delete/) 함수.
1. Document 저장을 사용하여 [저장](https://reference.aspose.com/pdf/rust-cpp/core/save/) 메서드.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Delete specified page in PDF-document
        pdf.page_delete(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
