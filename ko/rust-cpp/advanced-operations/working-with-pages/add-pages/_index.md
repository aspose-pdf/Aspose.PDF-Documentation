---
title: PDF 문서에 페이지 추가
linktitle: 페이지 추가
type: docs
weight: 10
url: /ko/rust-cpp/add-pages/
description: Aspose.PDF를 사용한 Rust에서 기존 PDF에 페이지를 추가하여 문서를 강화하고 확장하는 방법을 살펴보세요.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust를 사용하여 PDF 페이지 추가
Abstract: Aspose.PDF for Rust via C++는 PDF 문서에 페이지를 추가하는 강력한 기능을 제공하여 개발자가 새 페이지를 동적으로 생성하고 특정 요구 사항에 따라 맞춤 설정할 수 있게 합니다. 이 라이브러리는 빈 페이지를 삽입하거나 기존 문서에서 페이지를 복사하는 것을 지원하며 페이지 크기, 방향 및 내용을 정의하는 옵션을 제공합니다. 이러한 기능을 통해 문서를 원활하게 확장하고 맞춤화할 수 있습니다. 문서에는 자세한 지침과 코드 샘플이 포함되어 있어 개발자가 애플리케이션에서 페이지 추가 기능을 효율적으로 구현할 수 있도록 돕습니다.
SoftwareApplication: rust-cpp
---

## PDF 파일에 페이지 추가

제공된 Rust 코드 조각은 Aspose.PDF 라이브러리를 사용하여 PDF 끝에 페이지를 추가하는 작업을 수행하는 방법을 보여줍니다.

1. The [open](https://reference.aspose.com/pdf/rust-cpp/core/open/) 함수는 프로그램이 기존 PDF 파일(sample.pdf)을 로드하여 조작할 수 있게 합니다. 이는 편집, 콘텐츠 추가 또는 데이터 읽기와 같은 모든 PDF 관련 작업에 필수적입니다.
1. The [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) 메서드는 기존 PDF 문서에 새로운 빈 페이지를 삽입하는 데 사용됩니다. 이는 문서를 확장하거나 추가 콘텐츠를 준비하는 데 유용합니다.
1. The [저장](https://reference.aspose.com/pdf/rust-cpp/core/save/) 이 메서드는 PDF에 대한 수정 사항이 파일에 다시 기록되도록 보장합니다. 이 단계는 새로운 페이지 추가와 같은 변경 사항을 지속하는 데 중요합니다.

이 스니펫은 기본 PDF 조작 작업을 위해 Aspose.PDF Rust 라이브러리를 사용하는 간결하고 효율적인 예시입니다.

Aspose.PDF for Rust를 사용하면 파일 내의 어느 위치에든 PDF 문서에 페이지를 삽입할 수 있을 뿐만 아니라 PDF 파일의 끝에 페이지를 추가할 수 있습니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add new page in PDF-document
        pdf.page_add()?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```

## PDF 파일에 페이지 삽입

The [page_insert](https://reference.aspose.com/pdf/rust-cpp/core/page_insert/) 이 메서드는 지정된 위치에 새 페이지를 삽입합니다. 이 기능은 기존 문서에 추가 페이지를 삽입해야 할 때 유용합니다. 예를 들어, 보고서나 프레젠테이션에 새로운 섹션이나 내용을 추가하는 경우입니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Insert new page at the specified position in PDF-document
        pdf.page_insert(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```