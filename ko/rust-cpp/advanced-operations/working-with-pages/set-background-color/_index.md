---
title: Rust를 통해 C++에서 PDF의 배경색을 설정합니다
linktitle: 배경색을 설정합니다
type: docs
weight: 80
url: /ko/rust-cpp/set-background-color/
description: Rust를 사용하여 C++로 PDF 파일의 배경색을 설정합니다.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust를 사용하여 PDF의 배경색을 설정합니다
Abstract: Aspose.PDF for Rust via C++는 PDF 페이지의 배경색을 설정하는 기능을 제공하여 개발자가 문서의 모습을 사용자 지정할 수 있게 합니다. 이 기능을 통해 전체 페이지 배경에 단색을 적용할 수 있어 문서의 시각적 표현을 향상시킵니다. 개발자는 RGB 또는 CMYK와 같은 표준 색상 모델을 사용하여 색상 값을 쉽게 지정할 수 있습니다. 문서에는 자세한 설명과 코드 예제가 제공되어 개발자가 C++ 애플리케이션 내에서 배경색 사용자 지정을 효과적으로 구현하도록 돕습니다.
SoftwareApplication: rust-cpp
---

1. 제공된 코드 스니펫은 Rust에서 Aspose.PDF 라이브러리를 사용하여 PDF 파일의 배경색을 설정하는 방법을 보여줍니다.
1. 그 [열기](https://reference.aspose.com/pdf/rust-cpp/core/open/) method는 지정된 PDF 파일을 메모리로 로드하여 외관이나 내용을 수정하는 것과 같은 추가 조작을 가능하게 합니다.
1. 그 [set_background](https://reference.aspose.com/pdf/rust-cpp/organize/set_background/) 메서드는 PDF 문서에 새로운 배경 색을 적용합니다. RGB 값을 사용하면 사용자가 문서의 시각적 스타일을 맞춤 설정할 수 있습니다.
1. 그 [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) 메서드는 업데이트된 PDF를 새로운 이름으로 저장합니다.

이 코드는 브랜드 보고서 생성, 워터마크 추가, 또는 여러 문서에 걸친 시각적 일관성 향상과 같은 PDF 맞춤 작업을 자동화해야 하는 애플리케이션에 이상적입니다.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Set PDF-document background color using RGB values
      pdf.set_background(200, 100, 101)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_set_background.pdf")?;

      Ok(())
  }
```