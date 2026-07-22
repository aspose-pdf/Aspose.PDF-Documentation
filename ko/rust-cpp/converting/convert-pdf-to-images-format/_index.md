---
title: Rust에서 PDF를 이미지 형식으로 변환
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /ko/rust-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-20"
description: 이 항목에서는 Aspose.PDF for Rust를 사용하여 PDF를 TIFF, BMP, JPEG, PNG, SVG와 같은 다양한 이미지 형식으로 몇 줄의 코드만으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust를 사용하여 PDF를 이미지 형식으로 변환하는 도구
Abstract: Aspose.PDF for Rust via C++는 JPEG, PNG, BMP 및 TIFF를 포함한 다양한 이미지 형식으로 PDF 문서를 원활하게 변환할 수 있습니다. 이 기능을 통해 개발자는 원본 문서의 내용, 레이아웃 및 해상도를 유지하면서 고품질 이미지를 렌더링할 수 있습니다. 라이브러리는 해상도, 이미지 품질 및 색 깊이와 같은 출력 설정에 대한 유연한 옵션을 제공합니다. 문서에서는 단계별 지침과 코드 샘플을 제공하여 개발자가 PDF를 이미지로 변환하는 기능을 애플리케이션에 효율적으로 통합할 수 있도록 돕습니다.
SoftwareApplication: rust-cpp
---

## PDF를 이미지로 변환

이 문서에서는 PDF를 이미지 형식으로 변환하는 옵션을 보여드립니다.

이전에 스캔한 문서는 종종 PDF 파일 형식으로 저장됩니다. 하지만 그래픽 편집기에서 편집하거나 이미지 형식으로 추가 전송해야 합니까? **Aspose.PDF for Rust via C++**를 사용하여 PDF를 이미지로 변환할 수 있는 범용 도구가 있습니다.
가장 일반적인 작업은 전체 PDF 문서 또는 문서의 특정 페이지를 이미지 세트로 저장해야 할 때입니다. **Aspose.PDF for Rust via C++**는 PDF를 JPG 및 PNG 형식으로 변환하여 특정 PDF 파일에서 이미지를 얻는 데 필요한 단계를 단순화합니다.

**Aspose.PDF for Rust via C++** 다양한 PDF를 이미지 형식으로 변환하는 기능을 지원합니다. 섹션을 확인하십시오. [Aspose.PDF 지원 파일 형식](https://docs.aspose.com/pdf/rust-cpp/supported-file-formats/).

### PDF를 JPEG로 변환

제공된 Rust 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 첫 페이지를 JPEG 이미지로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. 페이지를 JPEG로 변환하기 [page_to_jpg](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_jpg/) 함수.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Jpg-image
      pdf.page_to_jpg(1, 100, "sample_page1.jpg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**PDF를 JPEG로 온라인 변환해 보세요**

Aspose.PDF for Rust는 온라인 무료 애플리케이션을 제공합니다. ["PDF를 JPEG로"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), 여기서 기능과 품질이 어떻게 작동하는지 조사해 볼 수 있습니다.

[![무료 앱을 사용한 Aspose.PDF 변환 PDF를 JPEG로](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

### PDF를 TIFF로 변환

제공된 Rust 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 첫 페이지를 TIFF 이미지로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. 페이지를 TIFF로 변환하기 [page_to_tiff](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_tiff/) 함수.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Tiff-image
      pdf.page_to_tiff(1, 100, "sample_page1.tiff")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**PDF를 온라인으로 TIFF 변환해 보세요**

Aspose.PDF for Rust는 온라인 무료 애플리케이션을 제공합니다. ["PDF를 TIFF로"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), 여기서 기능과 품질이 어떻게 작동하는지 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 TIFF로 무료 앱으로](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### PDF를 PNG로 변환

제공된 Rust 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 첫 페이지를 PNG 이미지로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. 페이지를 PNG로 변환하기 사용하여 [page_to_png](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_png/) 함수.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Png-image
      pdf.page_to_png(1, 100, "sample_page1.png")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**온라인에서 PDF를 PNG로 변환해 보세요**

우리의 무료 애플리케이션이 작동하는 방식을 예시로, 다음 기능을 확인해 보세요.

Aspose.PDF for Rust는 온라인 무료 애플리케이션을 제공합니다. ["PDF를 PNG로"](https://products.aspose.app/pdf/conversion/pdf-to-png), 여기서 기능과 품질이 어떻게 작동하는지 조사해 볼 수 있습니다.

[![무료 앱을 사용하여 PDF를 PNG로 변환하는 방법](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)**는 정적 및 동적(대화형 또는 애니메이션) 2차원 벡터 그래픽을 위한 XML 기반 파일 형식 사양군입니다. SVG 사양은 1999년부터 World Wide Web Consortium (W3C)에서 개발하고 있는 오픈 표준입니다.

### PDF를 SVG로 변환

제공된 Rust 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 첫 페이지를 SVG 이미지로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. 페이지를 SVG로 변환하기 [페이지를_svg로](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_svg/) 함수.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Svg-image
      pdf.page_to_svg(1, "sample_page1.svg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**PDF를 SVG로 온라인 변환해 보세요**

Aspose.PDF for Rust는 온라인 무료 애플리케이션을 제공합니다. ["PDF를 SVG로"](https://products.aspose.app/pdf/conversion/pdf-to-svg), 여기서 기능과 품질이 어떻게 작동하는지 조사해 볼 수 있습니다.

[![무료 앱을 사용한 Aspose.PDF PDF → SVG 변환](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

### PDF를 SVG ZIP 아카이브로 변환

다음 예제는 PDF 문서를 SVG 아카이브로 변환하며, 각 페이지가 ZIP 컨테이너 안에 별도의 SVG 파일로 저장됩니다.

1. 소스 PDF 문서를 엽니다.
1. 문서를 SVG 파일을 포함하는 ZIP 아카이브로 저장합니다.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as SVG-archive
      pdf.save_svg_zip("sample_svg.zip")?;

      Ok(())
  }
```

### PDF를 DICOM으로 변환

제공된 Rust 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 첫 페이지를 DICOM 이미지로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. Page를 DICOM으로 변환하기 [page_to_dicom](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_dicom/) 함수.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as DICOM-image
      pdf.page_to_dicom(1, 100, "sample_page1.dcm")?;

      Ok(())
  }
```

### PDF를 BMP로 변환

제공된 Rust 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 첫 페이지를 BMP 이미지로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. 페이지를 BMP로 변환하기 [페이지를 BMP로](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_bmp/) 함수.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Bmp-image
      pdf.page_to_bmp(1, 100, "sample_page1.bmp")?;

      Ok(())
  }
```