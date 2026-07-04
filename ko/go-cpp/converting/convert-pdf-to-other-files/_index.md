---
title: Go에서 PDF를 EPUB, TeX, Text, XPS로 변환
linktitle: PDF를 다른 형식으로 변환
type: docs
weight: 90
url: /ko/go-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-04"
description: 이 주제에서는 Go를 사용하여 PDF 파일을 EPUB, LaTeX, 텍스트, XPS 등과 같은 다른 파일 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: PDF를 EPUB, TeX, 텍스트 및 XPS로 변환하기 위한 Golang 도구
Abstract: Aspose.PDF for Go via C++는 PDF 문서를 DOCX, PPTX, HTML, EPUB, SVG 등 다양한 파일 형식으로 변환하는 강력한 기능을 제공합니다. 이 기능을 통해 개발자는 PDF 콘텐츠를 손쉽게 추출하고 재활용할 수 있으며, 다양한 출력 형식에서도 서식, 구조 및 품질을 유지합니다. 라이브러리는 특정 요구 사항에 맞게 변환 프로세스를 사용자 지정할 수 있는 유연한 옵션을 제공합니다. 문서에는 개발자가 애플리케이션 내에서 PDF를 파일로 변환하는 작업을 효율적으로 구현하도록 돕는 포괄적인 가이드라인과 코드 샘플이 포함되어 있습니다.
SoftwareApplication: go-cpp
---

## PDF를 EPUB으로 변환

**<abbr title="Electronic Publication">EPUB</abbr>**는 International Digital Publishing Forum (IDPF)에서 제공하는 무료 및 오픈 전자책 표준입니다. 파일 확장자는 .epub입니다.
EPUB는 재배치 가능한 콘텐츠를 위해 설계되었으며, 이는 EPUB 리더가 특정 디스플레이 장치에 맞게 텍스트를 최적화할 수 있음을 의미합니다. EPUB는 고정 레이아웃 콘텐츠도 지원합니다. 이 형식은 출판사와 변환 업체가 내부적으로 사용할 수 있는 단일 형식이자 배포 및 판매를 위한 형식으로 의도되었습니다. 이는 Open eBook 표준을 대체합니다.

제공된 Go 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 EPUB으로 변환하는 방법을 보여줍니다.

1. PDF 문서를 엽니다.
1. PDF 파일을 EPUB으로 변환하는 [Epub 저장]() 함수.
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
      // SaveEpub(filename string) saves previously opened PDF-document as Epub-document with filename
      err = pdf.SaveEpub("sample.epub")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**온라인에서 PDF를 EPUB으로 변환해 보세요**

Aspose.PDF for Go가 온라인 무료 애플리케이션을 제공합니다 ["PDF를 EPUB으로"](https://products.aspose.app/pdf/conversion/pdf-to-epub), 여기서 기능과 동작 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 무료 앱으로 PDF를 EPUB으로 변환](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## PDF를 TeX로 변환

**Aspose.PDF for Go** PDF를 TeX로 변환하는 것을 지원합니다.
LaTeX 파일 형식은 특수 마크업을 포함한 텍스트 파일 형식이며, 고품질 조판을 위한 TeX 기반 문서 작성 시스템에서 사용됩니다.

제공된 Go 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 TeX로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. PDF 파일을 TeX로 변환하기 위해 [SaveTeX](https://reference.aspose.com/pdf/go-cpp/convert/savetex/) 함수.
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
      // SaveTeX(filename string) saves previously opened PDF-document as TeX-document with filename
      err = pdf.SaveTeX("sample.tex")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF를 LaTeX/TeX로 온라인 변환해 보세요**

Aspose.PDF for Go가 온라인 무료 애플리케이션을 제공합니다 ["PDF를 LaTeX로"](https://products.aspose.app/pdf/conversion/pdf-to-tex), 여기서 기능과 동작 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF를 이용한 PDF를 LaTeX/TeX로 변환, 무료 앱](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## PDF를 TXT로 변환

제공된 Go 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 TXT로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. PDF 파일을 TXT로 변환하기 위해 [텍스트 저장](https://reference.aspose.com/pdf/go-cpp/convert/savetxt/) 함수.
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
      // SaveTxt(filename string) saves previously opened PDF-document as Txt-document with filename
      err = pdf.SaveTxt("sample.txt")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF를 텍스트로 온라인 변환해 보세요**

Aspose.PDF for Go가 온라인 무료 애플리케이션을 제공합니다 ["PDF를 텍스트로"](https://products.aspose.app/pdf/conversion/pdf-to-txt), 여기서 기능과 동작 품질을 조사해 볼 수 있습니다.

[![무료 앱으로 Aspose.PDF PDF를 텍스트로 변환](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDF를 XPS로 변환

XPS 파일 형식은 주로 Microsoft Corporation의 XML Paper Specification과 연관되어 있습니다. XML Paper Specification (XPS)은 이전에 Metro라는 코드명으로 불렸으며 Next Generation Print Path (NGPP) 마케팅 개념을 포함하는 Microsoft의 이니셔티브로, 문서 생성 및 조회를 Windows 운영 체제에 통합하기 위한 것입니다.

**Aspose.PDF for Go**는 PDF 파일을 변환할 수 있는 가능성을 제공합니다 <abbr title="XML Paper Specification">XPS</abbr> 포맷. 제시된 코드 스니펫을 사용하여 Go로 PDF 파일을 XPS 포맷으로 변환해 보겠습니다.

제공된 Go 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 XPS로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. PDF 파일을 XPS로 변환하려면 [SaveXps](https://reference.aspose.com/pdf/go-cpp/convert/savexps/) 함수.
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
      // SaveXps(filename string) saves previously opened PDF-document as Xps-document with filename
      err = pdf.SaveXps("sample.xps")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**온라인에서 PDF를 XPS로 변환해 보세요**

Aspose.PDF for Go가 온라인 무료 애플리케이션을 제공합니다 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), 여기서 기능과 동작 품질을 조사해 볼 수 있습니다.

[![무료 앱으로 Aspose.PDF PDF를 XPS로 변환](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## PDF를 그레이스케일 PDF로 변환

제공된 Go 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서의 첫 페이지를 그레이스케일 PDF로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. PDF 페이지를 그레이스케일 PDF로 변환하기 [페이지 그레이스케일](https://reference.aspose.com/pdf/go-cpp/organize/pagegrayscale/) 함수.
1. PDF 문서를 닫고 할당된 모든 리소스를 해제하십시오.

이 예제는 PDF의 특정 페이지를 회색조로 변환합니다:

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
      // PageGrayscale(num int32) converts page to black and white
      err = pdf.PageGrayscale(1)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_page1_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

이 예제는 전체 PDF 문서를 그레이스케일로 변환합니다:

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
      // Grayscale() converts PDF-document to black and white
      err = pdf.Grayscale()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```