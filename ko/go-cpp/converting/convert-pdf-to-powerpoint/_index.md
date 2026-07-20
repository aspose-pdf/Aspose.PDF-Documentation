---
title: Go에서 PDF를 PPTX로 변환
linktitle: PDF를 PowerPoint로 변환
type: docs
weight: 30
url: /ko/go-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-04"
description: Aspose.PDF는 Go를 사용하여 PDF를 PPTX 형식으로 변환할 수 있도록 합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF를 PowerPoint로 변환하는 Golang 도구
Abstract: Aspose.PDF for Go via C++는 원본 레이아웃, 포맷 및 콘텐츠 구조를 유지하면서 PDF 문서를 PowerPoint(PPTX) 형식으로 변환하기 위한 신뢰할 수 있는 솔루션을 제공합니다. 이 기능을 통해 개발자는 정적 PDF 파일을 동적이고 편집 가능한 프레젠테이션으로 원활하게 변환할 수 있습니다. 이 라이브러리는 변환 과정을 제어할 수 있는 맞춤형 옵션을 제공하여 비즈니스 및 전문적인 사용에 적합한 고품질 출력을 보장합니다. 문서에서는 단계별 지침과 코드 샘플을 제공하여 개발자가 PDF-to-PowerPoint 변환을 애플리케이션에 효율적으로 통합할 수 있도록 도와줍니다.
SoftwareApplication: go-cpp
---

## PDF를 PPTX로 변환

제공된 Go 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 PPTX로 변환하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. 다음을 사용하여 PDF 파일을 PPTX로 변환합니다 [SavePptx](https://reference.aspose.com/pdf/go-cpp/convert/savepptx/) 함수.
1. PDF 문서를 닫고 할당된 모든 리소스를 해제합니다.

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
      // SavePptX(filename string) saves previously opened PDF-document as PptX-document with filename
      err = pdf.SavePptX("sample.pptx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF를 PowerPoint로 온라인 변환해 보세요**

Aspose.PDF for Go가 온라인 무료 애플리케이션을 제공합니다 [“PDF to PPTX”](https://products.aspose.app/pdf/conversion/pdf-to-pptx), 여기서 기능과 품질을 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 PPTX로 무료 앱과 함께](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}