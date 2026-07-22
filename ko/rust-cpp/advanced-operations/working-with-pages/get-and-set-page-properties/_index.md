---
title: 페이지 속성 가져오기 및 설정
linktitle: 페이지 속성 가져오기 및 설정
type: docs
url: /ko/rust-cpp/get-and-set-page-properties/
description: Aspose.PDF for Rust를 사용하여 PDF 문서의 페이지 속성을 가져오고 설정하는 방법을 배워 맞춤형 문서 형식을 구현할 수 있습니다.
lastmod: "2026-07-20"
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust로 페이지 속성 가져오기 및 설정
Abstract: Aspose.PDF for Rust via C++는 PDF 문서의 페이지 속성을 가져오고 설정하기 위한 포괄적인 기능을 제공하여 개발자가 크기, 회전, 여백 및 메타데이터와 같은 다양한 페이지 속성을 액세스하고 수정할 수 있게 합니다. 이러한 기능을 통해 특정 애플리케이션 요구사항을 충족하도록 문서 레이아웃과 외관을 정확하게 제어할 수 있습니다. 이 라이브러리는 PDF 페이지의 원활한 맞춤화 및 최적화를 보장합니다. 문서에는 개발자가 애플리케이션 내에서 페이지 속성을 효율적으로 검색하고 업데이트할 수 있도록 자세한 안내와 코드 예제가 제공됩니다.
SoftwareApplication: rust-cpp
---


Aspose.PDF for Rust를 사용하면 PDF 파일의 페이지 속성을 읽고 설정할 수 있습니다. 이 섹션에서는 PDF 파일의 페이지 수를 가져오는 방법, 색상과 같은 PDF 페이지 속성 정보를 얻고 페이지 속성을 설정하는 방법을 보여줍니다.

## PDF 파일의 페이지 수 가져오기

문서 작업을 할 때, 문서에 몇 페이지가 포함되어 있는지 알고 싶을 때가 많습니다. Aspose.PDF를 사용하면 이 작업은 두 줄 이상의 코드가 필요하지 않습니다.

**Aspose.PDF for Rust via C++**는 페이지를 계산하는 데 사용할 수 있습니다 [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) 함수.

다음 코드 스니펫은 PDF 문서를 열고, 페이지 수를 가져온 다음 결과를 출력하도록 설계되었습니다.

그 [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) 메서드는 PDF 문서의 전체 페이지 수를 가져오기 위해 호출됩니다. 이는 특정 페이지를 추출하거나 모든 페이지에 걸쳐 작업을 수행하는 등 문서 길이를 알아야 하는 작업에 유용합니다. 이 메서드는 문서 구조를 조회하는 간단한 방법입니다.

PDF 파일의 페이지 수를 가져오려면:

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Return page count in PDF-document
      let count = pdf.page_count()?;

      // Print the page count
      println!("Count: {}", count);

      Ok(())
  }
```

## 페이지 크기 설정

이 예제에서는 메서드 pdf.PageSetSize()가 PDF 문서의 첫 페이지 크기를 변경합니다. PageSizeA1 상수는 첫 페이지가 A1 용지 크기로 설정되도록 보장합니다. 이는 문서를 표준화된 형식으로 변환하거나 특정 콘텐츠가 페이지에 올바르게 맞도록 할 때 유용합니다.

1. PDF 문서를 다음으로 열기 [열기](https://reference.aspose.com/pdf/rust-cpp/core/open/) 메서드.
1. 다음으로 페이지 크기 설정 [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/) 함수.
1. Document를 사용하여 저장 중 [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) 메서드.

```rs

    use asposepdf::{Document, PageSize};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set the size of a page in the PDF-document
        pdf.page_set_size(1, PageSize::A1)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_page1_set_size_A1.pdf")?;

        Ok(())
    }
```