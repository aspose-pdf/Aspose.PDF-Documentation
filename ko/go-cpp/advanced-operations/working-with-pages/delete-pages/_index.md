---
title: Go로 PDF 페이지 삭제
linktitle: PDF 페이지 삭제
type: docs
weight: 30
url: /ko/go-cpp/delete-pages/
description: C++를 통해 Aspose.PDF for Go를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go로 PDF 페이지 삭제
Abstract: Aspose.PDF for Go via C++는 PDF 문서에서 페이지를 삭제하는 효율적인 기능을 제공하여 개발자가 원치 않거나 불필요한 페이지를 손쉽게 제거할 수 있도록 합니다. 이 라이브러리는 페이지 번호나 범위를 지정하여 단일 페이지 또는 여러 페이지를 삭제할 수 있게 하며, 정확한 문서 수정을 보장합니다. 이 기능은 중복된 콘텐츠를 제거하고 문서 구조를 최적화함으로써 PDF 파일을 간소화하는 데 도움이 됩니다. 문서에는 단계별 안내와 코드 샘플이 제공되어 개발자가 애플리케이션 내에서 페이지 삭제 기능을 효과적으로 구현할 수 있도록 지원합니다.
SoftwareApplication: go-cpp
---

**Aspose.PDF for Go via C++**를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다. 다음 코드 스니펫은 특정 페이지를 삭제하여 PDF 문서를 조작하는 방법을 보여줍니다. 이 방법은 페이지를 제거하고, 수정된 문서를 저장하며, 적절한 리소스 관리를 보장하는 PDF 문서 조작 작업에 효율적입니다.

1. PDF 파일 열기.
1. 특정 페이지를 삭제하는 [PageDelete](https://reference.aspose.com/pdf/go-cpp/core/pagedelete/) 함수.
1. 문서를 저장하는 [Save](https://reference.aspose.com/pdf/go-cpp/core/save/) 메서드.

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
      // PageDelete(num int32) deletes specified page in PDF-document
      err = pdf.PageDelete(1)
      if err != nil {
        log.Fatal(err)
      }
      // Save() saves previously opened PDF-document
      err = pdf.Save()
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
