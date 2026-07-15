---
title: Go를 사용하여 PDF에서 텍스트 추출
linktitle: PDF에서 텍스트 추출
type: docs
weight: 30
url: /ko/go-cpp/extract-text-from-pdf/
description: 이 문서는 Aspose.PDF for Go를 사용하여 PDF 문서에서 텍스트를 추출하는 다양한 방법을 설명합니다.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go를 사용한 텍스트 추출
Abstract: Aspose.PDF for Go via C++는 PDF 문서에서 텍스트를 추출하는 강력하고 효율적인 방법을 제공합니다. 이 라이브러리는 다양한 추출 기술을 지원하여 사용자가 전체 문서, 특정 페이지 또는 PDF 내의 사전 정의된 영역에서 텍스트를 가져올 수 있도록 합니다.
SoftwareApplication: go-cpp
---

## PDF 문서에서 텍스트 추출

PDF 문서에서 텍스트를 추출하는 것은 매우 일반적이고 유용한 작업입니다. PDF에는 종종 접근, 분석 또는 다양한 목적을 위해 처리해야 하는 중요한 정보가 포함되어 있습니다. 텍스트 추출은 데이터베이스, 보고서 또는 다른 문서에서 보다 쉽게 재사용할 수 있게 합니다.

텍스트를 추출하면 PDF 콘텐츠를 검색 가능하게 만들어 사용자가 전체 문서를 수동으로 검토하지 않고도 특정 정보를 빠르게 찾을 수 있습니다.

PDF 문서에서 텍스트를 추출하려는 경우, 다음을 사용할 수 있습니다 [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) 함수.
Go를 사용하여 PDF 파일에서 텍스트를 추출하기 위한 다음 코드 조각을 확인하십시오.

1. 주어진 파일 이름으로 PDF 문서를 엽니다.
1. [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) PDF 문서에서 텍스트 내용을 추출합니다.
1. 추출된 텍스트를 콘솔에 출력합니다.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"
    import "fmt"

    func main() {
        // Open(filename string) opens a PDF-document with filename
        pdf, err := asposepdf.Open("sample.pdf")
        if err != nil {
            log.Fatal(err)

        }
        // ExtractText() returns PDF-document contents as plain text
        txt, err := pdf.ExtractText()
        if err != nil {
            log.Fatal(err)
        }
        // Print
        fmt.Println("Extracted text:\n", txt)
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```