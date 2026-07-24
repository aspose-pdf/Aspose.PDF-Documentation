---
title: Rust에서 PDF를 PPTX로 변환
linktitle: PDF를 PowerPoint로 변환
type: docs
weight: 30
url: /ko/rust-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-20"
description: Aspose.PDF를 사용하면 Rust로 PDF를 PPTX 형식으로 변환할 수 있습니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF를 PowerPoint로 변환하기 위한 Rust 도구
Abstract: Aspose.PDF for Rust via C++는 PDF 문서를 PowerPoint (PPTX) 형식으로 변환하면서 원본 레이아웃, 서식 및 콘텐츠 구조를 보존하는 신뢰할 수 있는 솔루션을 제공합니다. 이 기능을 통해 개발자는 정적 PDF 파일을 동적인 편집 가능한 프레젠테이션으로 원활히 변환할 수 있습니다. 이 라이브러리는 변환 과정을 제어할 수 있는 사용자 정의 옵션을 제공하여 비즈니스 및 전문적 사용에 적합한 고품질 출력을 보장합니다. 문서에는 단계별 안내와 코드 예제가 포함되어 있어 개발자가 애플리케이션에 PDF‑to‑PowerPoint 변환을 효율적으로 통합할 수 있도록 도와줍니다.
SoftwareApplication: rust-cpp
---

## PDF를 PPTX로 변환

제공된 Rust 코드 조각은 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 PPTX로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. PDF 파일을 PPTX로 변환하는 데 사용 [save_pptx](https://reference.aspose.com/pdf/rust-cpp/convert/save_pptx/) 함수.

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as PptX-document
      pdf.save_pptx("sample.pptx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**PDF를 PowerPoint 온라인으로 변환해 보세요**

Aspose.PDF for Rust가 무료 온라인 애플리케이션을 제공합니다 [“PDF to PPTX”](https://products.aspose.app/pdf/conversion/pdf-to-pptx), 여기서 기능과 품질을 직접 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 PPTX로 무료 앱 사용](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}