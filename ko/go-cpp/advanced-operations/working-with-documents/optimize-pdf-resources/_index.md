---
title: Go를 사용하여 PDF 리소스 최적화
linktitle: PDF 리소스 최적화
type: docs
weight: 15
url: /ko/go-cpp/optimize-pdf-resources/
description: Go 도구를 사용하여 PDF 파일의 리소스를 최적화합니다.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go를 사용하여 PDF 리소스 최적화
Abstract: Aspose.PDF for Go via C++는 PDF 리소스를 최적화하는 고급 기능을 제공하여 문서 효율성을 향상하고 파일 크기를 감소시킵니다. 이 라이브러리를 통해 개발자는 중복 데이터를 제거하고 리소스를 압축함으로써 폰트, 이미지 및 메타데이터를 문서 품질을 손상시키지 않으면서 최적화할 수 있습니다. 이러한 최적화 기술은 문서 성능을 개선하여 PDF를 공유 및 저장에 보다 적합하게 만듭니다. 문서에는 자세한 가이드와 코드 샘플이 제공되어 개발자가 애플리케이션에서 리소스 최적화를 효과적으로 구현할 수 있도록 돕습니다.
SoftwareApplication: go-cpp
---

## PDF 리소스 최적화

문서 내 리소스 최적화:

  1. 문서 페이지에서 사용되지 않은 리소스는 삭제됩니다.
  1. 동일한 리소스는 단일 객체로 결합됩니다.
  1. 사용되지 않은 객체가 삭제됩니다.

최적화에는 이미지 압축, 사용되지 않은 객체 제거, 파일 크기 감소와 성능 향상을 위한 글꼴 최적화가 포함될 수 있습니다. 이 작업 중 발생하는 모든 오류는 기록되며 프로그램을 종료합니다.  
 
1. 그 [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) method는 지정된 PDF 파일(sample.pdf)을 메모리로 로드합니다.
1. PDF 내부의 리소스를 효율성을 위해 최적화합니다 using [OptimizeResource](https://reference.aspose.com/pdf/go-cpp/organize/optimizeresource/) method.
1. 그 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) method는 최적화된 PDF를 새 파일에 저장합니다.

다음 코드 스니펫은 PDF 문서를 최적화하는 방법을 보여줍니다.

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
      // OptimizeResource() optimizes resources of PDF-document
      err = pdf.OptimizeResource()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_OptimizeResource.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```