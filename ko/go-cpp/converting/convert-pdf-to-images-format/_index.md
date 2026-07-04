---
title: Go에서 PDF를 이미지 형식으로 변환
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /ko/go-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-04"
description: 이 주제에서는 Aspose.PDF for Go를 사용하여 PDF를 다양한 이미지 형식(e.g. TIFF, BMP, JPEG, PNG, SVG)으로 몇 줄의 코드만으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go를 사용하여 PDF를 이미지 형식으로 변환하는 도구
Abstract: Aspose.PDF for Go via C++는 PDF 문서를 JPEG, PNG, BMP, TIFF 등 다양한 이미지 형식으로 원활하게 변환할 수 있게 합니다. 이 기능을 통해 개발자는 원본 문서의 콘텐츠, 레이아웃 및 해상도를 유지하면서 고품질 이미지를 렌더링할 수 있습니다. 라이브러리는 해상도, 이미지 품질 및 색 깊이와 같은 출력 설정에 대한 유연한 옵션을 제공합니다. 문서에는 단계별 지침과 코드 샘플이 제공되어 개발자가 PDF를 이미지로 변환하는 기능을 애플리케이션에 효율적으로 통합할 수 있도록 돕습니다.
SoftwareApplication: go-cpp
---

## PDF를 이미지로 변환하기

이 기사에서는 PDF를 이미지 형식으로 변환하는 옵션을 보여드리겠습니다.

이전에 스캔한 문서는 종종 PDF 파일 형식으로 저장됩니다. 그러나 그래픽 편집기에서 편집하거나 이미지 형식으로 추가 전송해야 합니까? 우리는 **Aspose.PDF for Go via C++**를 사용하여 PDF를 이미지로 변환하는 범용 도구를 제공합니다.
가장 일반적인 작업은 전체 PDF 문서 또는 문서의 특정 페이지를 이미지 세트로 저장해야 할 때입니다. **Aspose.PDF for Go via C++**는 PDF를 JPG 및 PNG 형식으로 변환하여 특정 PDF 파일에서 이미지를 얻는 데 필요한 단계를 간소화합니다.

**Aspose.PDF for Go via C++** 다양한 PDF를 이미지 형식으로 변환하는 것을 지원합니다. 섹션을 확인하십시오. [Aspose.PDF 지원 파일 형식](https://docs.aspose.com/pdf/go-cpp/supported-file-formats/).

## PDF를 JPEG로 변환

제공된 Go 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 첫 페이지를 JPEG 이미지로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. 페이지를 JPEG로 변환하기 [PageToJpg](https://reference.aspose.com/pdf/go-cpp/convert/pagetojpg/) 함수.
1. PDF 문서를 닫고 할당된 모든 리소스를 해제하십시오.

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

제공된 Go 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 첫 페이지를 TIFF 이미지로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. 페이지를 TIFF로 변환하기 [PageToTiff](https://reference.aspose.com/pdf/go-cpp/convert/pagetotiff/) 함수.
1. PDF 문서를 닫고 할당된 모든 리소스를 해제하십시오.

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

제공된 Go 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 첫 페이지를 PNG 이미지로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. 사용하여 페이지를 PNG로 변환 [PageToPng](https://reference.aspose.com/pdf/go-cpp/convert/pagetopng/) 함수.
1. PDF 문서를 닫고 할당된 모든 리소스를 해제하십시오.

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

무료 애플리케이션이 어떻게 작동하는지 예시로, 다음 기능을 확인해 주세요.

Aspose.PDF for Go는 온라인 무료 애플리케이션을 제공합니다 ["PDF를 PNG로"](https://products.aspose.app/pdf/conversion/pdf-to-png), 여기서 그 기능과 품질이 어떻게 작동하는지 조사해 볼 수 있습니다.

[![무료 앱을 사용하여 PDF를 PNG로 변환하는 방법](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)**는 2차원 벡터 그래픽(정적 및 동적(인터랙티브 또는 애니메이션))을 위한 XML 기반 파일 형식 사양들의 집합입니다. SVG 사양은 1999년부터 월드 와이드 웹 컨소시엄(W3C)에서 개발 중인 오픈 표준입니다.

## PDF를 SVG로 변환

제공된 Go 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 첫 페이지를 SVG 이미지로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. 페이지를 SVG로 변환하기 [PageToSvg](https://reference.aspose.com/pdf/go-cpp/convert/pagetosvg/) 함수.
1. PDF 문서를 닫고 할당된 모든 리소스를 해제하십시오.

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

제공된 Go 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 첫 페이지를 DICOM 이미지로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. 페이지를 DICOM으로 변환하기 [PageToDICOM](https://reference.aspose.com/pdf/go-cpp/convert/pagetodicom/) 함수.
1. PDF 문서를 닫고 할당된 모든 리소스를 해제하십시오.

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

제공된 Go 코드 조각은 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 첫 페이지를 BMP 이미지로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. 페이지를 BMP로 변환하려면 [PageToBmp](https://reference.aspose.com/pdf/go-cpp/convert/pagetobmp/) 함수.
1. PDF 문서를 닫고 할당된 모든 리소스를 해제하십시오.

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