---
title: Go를 사용하여 PDF에 텍스트 추가
linktitle: PDF에 텍스트 추가
type: docs
weight: 10
url: /ko/go-cpp/add-text-to-pdf-file/
description: Aspose.PDF를 사용하여 콘텐츠 향상 및 문서 편집을 위해 Go에서 PDF 문서에 텍스트를 추가하는 방법을 배우세요.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Aspose.PDF for Go를 사용하여 PDF에 텍스트 추가
Abstract: Add Text to PDF File 섹션은 Aspose.PDF for C++ 및 Go 문서에서 PDF 파일에 프로그래밍 방식으로 텍스트를 삽입하는 단계별 지침을 제공합니다. 여기에는 위치 지정, 글꼴 사용자 정의, 색상 조정 및 텍스트 정렬 옵션을 포함한 다양한 텍스트 추가 방법이 다루어집니다. 이 가이드는 PDF 내 특정 페이지와 위치에 텍스트를 추가하는 방법을 보여 주어 정확한 콘텐츠 배치를 보장합니다. 자세한 코드 예제와 설명을 통해 개발자는 PDF 문서 관리 향상을 위해 텍스트 삽입 기능을 애플리케이션에 쉽게 통합할 수 있습니다.
SoftwareApplication: go-cpp
---

기존 PDF 파일에 텍스트를 추가하려면:

1. PDF 파일을 엽니다.
1. PDF 문서에 텍스트를 추가하려면 [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/) 함수.
1. 수정 사항을 동일한 파일에 저장합니다.

## 텍스트 추가

다음 코드 조각은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

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
        // PageAddText(num int32, addText string) adds text on page
        err = pdf.PageAddText(1, "added text")
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
