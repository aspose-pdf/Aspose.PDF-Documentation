---
title: PDF 문서에 페이지 추가
linktitle: 페이지 추가
type: docs
weight: 10
url: /ko/go-cpp/add-pages/
description: Go에서 Aspose.PDF를 사용하여 기존 PDF에 페이지를 추가하는 방법을 살펴보고 문서를 향상 및 확장하십시오.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go를 사용하여 PDF 페이지 추가
Abstract: C++를 통한 Aspose.PDF for Go는 PDF 문서에 페이지를 추가하는 강력한 기능을 제공하여 개발자가 새 페이지를 동적으로 생성하고 특정 요구 사항에 따라 맞춤 설정할 수 있게 합니다. 이 라이브러리는 빈 페이지 삽입이나 기존 문서에서 페이지 복사를 지원하며 페이지 크기, 방향 및 내용 정의 옵션을 제공합니다. 이러한 기능은 문서의 원활한 확장 및 맞춤화를 가능하게 합니다. 문서에는 자세한 안내와 코드 샘플이 포함되어 있어 개발자가 애플리케이션에서 페이지 추가 기능을 효율적으로 구현할 수 있도록 돕습니다.
SoftwareApplication: go-cpp
---

## PDF 파일에 페이지 추가

제공된 Go 코드 스니펫은 Aspose.PDF 라이브러리를 사용하여 PDF 끝에 페이지를 추가하는 작업을 수행하는 방법을 보여줍니다. 

1. 그 [열기](https://reference.aspose.com/pdf/go-cpp/core/open/) 함수는 프로그램이 기존 PDF 파일(sample.pdf)을 로드하여 조작할 수 있게 합니다. 이는 편집, 콘텐츠 추가, 데이터 읽기와 같은 모든 PDF 관련 작업에 필수적입니다.
1. 그 [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) 메서드는 기존 PDF 문서에 새로운 빈 페이지를 삽입하는 데 사용됩니다. 이는 문서를 확장하거나 추가 콘텐츠를 준비하는 데 유용합니다.
1. 그 [저장](https://reference.aspose.com/pdf/go-cpp/core/save/) method는 PDF에 대한 수정 사항이 파일에 다시 기록되도록 보장합니다. 이 단계는 새 페이지 추가와 같은 변경 사항을 지속시키는 데 필수적입니다.
1. 그 [닫기](https://reference.aspose.com/pdf/go-cpp/core/close/) method는 defer를 사용하여 호출되며, PDF 작업 중에 할당된 모든 리소스를 해제합니다. 이는 메모리 누수를 방지하고 효율적인 리소스 사용을 보장하는 데 중요합니다.

이 코드는 기본 PDF 조작 작업을 위해 Aspose.PDF Go 라이브러리를 사용하는 간결하고 효율적인 예시입니다.

Aspose.PDF for Go는 파일의 어느 위치에든 PDF 문서에 페이지를 삽입하고 PDF 파일 끝에 페이지를 추가할 수 있게 해줍니다.

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
        // PageAdd() adds new page in PDF-document
        err = pdf.PageAdd()
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

## PDF 파일에 페이지 삽입

그 [PageInsert](https://reference.aspose.com/pdf/go-cpp/core/pageinsert/) 이 메서드는 지정된 위치에 새 페이지를 삽입합니다. 이 기능은 기존 문서에 추가 페이지를 삽입해야 할 때 유용합니다. 예를 들어, 보고서나 프레젠테이션에 새로운 섹션이나 내용을 추가하는 경우에 사용할 수 있습니다.

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
        // PageInsert(num int32) inserts new page at the specified position in PDF-document
        err = pdf.PageInsert(1)
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