---
title: Go 에서 PDF를 JPEG, PNG, TIFF로 변환
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /ko/go-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-04"
description: Aspose.PDF for Go via C++를 사용하여 PDF를 JPEG, PNG, BMP, TIFF, SVG, DICOM으로 변환하는 방법을 배웁니다. 고해상도 이미지 변환을 위한 단계별 Go 코드 예제와 튜토리얼입니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Go 를 사용한 PDF를 이미지로 변환하기 - 완벽한 가이드
Abstract: Aspose.PDF for Go via C++는 PDF 문서를 JPEG, PNG, BMP, TIFF, SVG, DICOM 등 다양한 이미지 형식으로 손쉽게 변환할 수 있는 강력한 라이브러리입니다. 이 포괄적인 가이드는 개발자가 PDF 페이지를 고품질 이미지로 렌더링하는 방법을 배웁니다. 해상도, 품질, 색 깊이 등의 출력 설정을 완벽하게 제어할 수 있으며, 모든 변환 형식에 대한 실행 가능한 Go 코드 샘플과 단계별 지침이 포함되어 있습니다.
SoftwareApplication: go-cpp
---

## Go에서 PDF를 이미지 형식으로 변환

**Aspose.PDF for Go via C++**를 사용하면 PDF 문서를 JPEG, PNG, BMP, TIFF, SVG, DICOM 등 다양한 이미지 형식으로 손쉽게 변환할 수 있습니다. 이 가이드에서는 실제 Go 코드를 사용하여 PDF의 모든 페이지 또는 특정 페이지를 고품질 이미지로 변환하는 방법을 배웁니다.

PDF를 이미지로 변환하는 것은 다음과 같은 경우에 유용합니다:

- 스캔된 PDF 문서를 편집 가능한 이미지 형식으로 변환
- 웹이나 모바일 애플리케이션에서 표시하기 위해 PDF를 이미지로 변환
- 문서의 축소판 또는 미리보기 생성
- 의료 또는 과학 문서를 DICOM 형식으로 변환

**Aspose.PDF for Go via C++**는 해상도, 품질, 색 깊이 등을 완전히 제어하면서 PDF를 이미지로 변환할 수 있습니다. 지원되는 모든 형식에 대해 [Aspose.PDF 지원 파일 형식](https://docs.aspose.com/pdf/go-cpp/supported-file-formats/) 페이지를 확인하십시오.

## PDF를 JPEG로 변환

다음 Go 코드 예제는 PDF 페이지를 JPEG 이미지로 변환합니다:

1. PDF 문서를 엽니다.
1. [PageToJpg](https://reference.aspose.com/pdf/go-cpp/convert/pagetojpg/) 함수로 페이지를 JPEG로 변환합니다.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToJpg(num int32, resolution_dpi int32, filename string) saves the specified page as Jpg-image file
      err = pdf.PageToJpg(1, 100, "sample_page1.jpg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF를 온라인에서 JPEG로 변환해 보세요**

Aspose.PDF for Go는 온라인 무료 애플리케이션을 제공합니다 ["PDF를 JPEG로"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), 여기서 그 기능과 품질이 어떻게 작동하는지 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 JPEG로 무료 앱 사용](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## PDF를 TIFF로 변환

다음 Go 코드 예제는 PDF 페이지를 TIFF 이미지로 변환합니다:

1. PDF 문서를 엽니다.
1. [PageToTiff](https://reference.aspose.com/pdf/go-cpp/convert/pagetotiff/) 함수로 페이지를 TIFF로 변환합니다.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToTiff(num int32, resolution_dpi int32, filename string) saves the specified page as Tiff-image file
      err = pdf.PageToTiff(1, 100, "sample_page1.tiff")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF를 TIFF로 온라인 변환해 보세요**

Aspose.PDF for Go는 온라인 무료 애플리케이션을 제공합니다 ["PDF를 TIFF로"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), 여기서 그 기능과 품질이 어떻게 작동하는지 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 TIFF로 무료 앱으로](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## PDF를 PNG로 변환

다음 Go 코드 예제는 PDF 페이지를 PNG 이미지로 변환합니다:

1. PDF 문서를 엽니다.
1. [PageToPng](https://reference.aspose.com/pdf/go-cpp/convert/pagetopng/) 함수로 페이지를 PNG으로 변환합니다.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToPng(num int32, resolution_dpi int32, filename string) saves the specified page as Png-image file
      err = pdf.PageToPng(1, 100, "sample_page1.png")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF를 PNG로 온라인 변환해 보세요**

Aspose.PDF for Go는 온라인 무료 애플리케이션을 제공합니다 ["PDF를 PNG로"](https://products.aspose.app/pdf/conversion/pdf-to-png), 여기서 그 기능과 품질이 어떻게 작동하는지 조사해 볼 수 있습니다.

[![무료 앱을 사용하여 PDF를 PNG로 변환하는 방법](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)**는 2차원 벡터 그래픽(정적 및 동적(인터랙티브 또는 애니메이션))을 위한 XML 기반 파일 형식 사양들의 집합입니다. SVG 사양은 1999년부터 월드 와이드 웹 컨소시엄(W3C)에서 개발 중인 오픈 표준입니다.

## PDF를 SVG로 변환

다음 Go 코드 예제는 PDF 페이지를 SVG 이미지로 변환합니다:

1. PDF 문서를 엽니다.
1. [PageToSvg](https://reference.aspose.com/pdf/go-cpp/convert/pagetosvg/) 함수로 페이지를 SVG로 변환합니다.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToSvg(num int32, filename string) saves the specified page as Svg-image file
      err = pdf.PageToSvg(1, "sample_page1.svg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF를 SVG로 온라인 변환해 보세요**

Aspose.PDF for Go는 온라인 무료 애플리케이션을 제공합니다 [PDF를 SVG로](https://products.aspose.app/pdf/conversion/pdf-to-svg), 여기서 그 기능과 품질이 어떻게 작동하는지 조사해 볼 수 있습니다.

[![Aspose.PDF 무료 앱으로 PDF를 SVG로 변환](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

## PDF를 DICOM으로 변환

다음 Go 코드 예제는 PDF 페이지를 DICOM 이미지로 변환합니다:

1. PDF 문서를 엽니다.
1. [PageToDICOM](https://reference.aspose.com/pdf/go-cpp/convert/pagetodicom/) 함수로 페이지를 DICOM으로 변환합니다.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToDICOM(num int32, resolution_dpi int32, filename string) saves the specified page as DICOM-image file
      err = pdf.PageToDICOM(1, 100, "sample_page1.dcm")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## PDF를 BMP로 변환

다음 Go 코드 예제는 PDF 페이지를 BMP 이미지로 변환합니다:

1. PDF 문서를 엽니다.
1. [PageToBmp](https://reference.aspose.com/pdf/go-cpp/convert/pagetobmp/) 함수로 페이지를 BMP로 변환합니다.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToBmp(num int32, resolution_dpi int32, filename string) saves the specified page as Bmp-image file
      err = pdf.PageToBmp(1, 100, "sample_page1.bmp")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```