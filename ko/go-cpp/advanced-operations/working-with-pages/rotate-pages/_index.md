---
title: Go로 PDF 페이지 회전
linktitle: PDF 페이지 회전
type: docs
weight: 50
url: /ko/go-cpp/rotate-pages/
description: 이 항목에서는 Go를 사용하여 C++를 통해 기존 PDF 파일의 페이지 방향을 프로그래밍 방식으로 회전하는 방법을 설명합니다.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go로 PDF 페이지 회전
Abstract: Aspose.PDF for Go via C++는 PDF 문서의 페이지를 회전하는 강력한 기능을 제공하여 개발자가 필요에 따라 페이지 방향을 수정할 수 있게 합니다. 이 라이브러리는 90도, 180도, 270도로 페이지를 회전하는 것을 지원하여 문서 레이아웃을 빠르고 효율적으로 조정할 수 있습니다. 이 기능은 방향이 잘못된 페이지를 수정하거나 문서의 표시 방식을 변경하는 데 유용합니다. 문서에는 단계별 지침과 코드 샘플이 포함되어 있어 개발자가 페이지 회전 기능을 애플리케이션에 원활하게 통합할 수 있도록 돕습니다.
SoftwareApplication: go-cpp
---

이 섹션에서는 Go를 사용하여 기존 PDF 파일에서 페이지 방향을 가로에서 세로로, 또는 그 반대로 변경하는 방법을 설명합니다.

페이지를 회전하면 전문적인 환경에서 PDF를 인쇄하거나 표시할 때 올바른 정렬이 보장됩니다.

1. PDF 문서를 엽니다.
1. PDF 페이지 회전. The [PageRotate](https://reference.aspose.com/pdf/go-cpp/organize/rotate/) 함수는 지정된 페이지에 특정 회전(이 경우 180도)을 적용합니다.
1. 변경 사항을 새 파일에 저장합니다. The [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) 함수는 원본을 보존하면서 업데이트된 버전을 저장하기 위해 새로운 PDF 파일을 생성합니다.

이 예제에서는 PDF 문서의 특정 페이지를 회전합니다:

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
    // PageRotate(num int32, rotation int32) rotates page
    err = pdf.PageRotate(1, asposepdf.RotationOn180)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_page1_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

문서의 모든 PDF 페이지를 회전하는 옵션도 있습니다:

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
    // Rotate(rotation int32) rotates PDF-document
    err = pdf.Rotate(asposepdf.RotationOn270)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```