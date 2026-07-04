---
title: 페이지 속성 가져오기 및 설정
linktitle: 페이지 속성 가져오기 및 설정
type: docs
url: /ko/go-cpp/get-and-set-page-properties/
description: Aspose.PDF for Go를 사용하여 PDF 문서의 페이지 속성을 가져오고 설정하는 방법을 배우세요. 이를 통해 문서 형식을 맞춤화할 수 있습니다.
lastmod: "2026-07-04"
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go를 사용한 페이지 속성 가져오기 및 설정
Abstract: Aspose.PDF for Go via C++는 PDF 문서에서 페이지 속성을 가져오고 설정하는 포괄적인 기능을 제공하여 개발자가 크기, 회전, 여백 및 메타데이터와 같은 다양한 페이지 속성에 접근하고 수정할 수 있게 합니다. 이러한 기능을 통해 특정 애플리케이션 요구 사항을 만족하도록 문서 레이아웃 및 모양을 정밀하게 제어할 수 있습니다. 이 라이브러리는 PDF 페이지의 원활한 맞춤화와 최적화를 보장합니다. 문서에서는 개발자가 애플리케이션 내에서 페이지 속성을 효율적으로 검색하고 업데이트할 수 있도록 자세한 가이드와 코드 샘플을 제공합니다.
SoftwareApplication: go-cpp
---


Aspose.PDF for Go를 사용하면 PDF 파일의 페이지 속성을 읽고 설정할 수 있습니다. 이 섹션에서는 PDF 파일의 페이지 수를 가져오는 방법, 색상과 같은 PDF 페이지 속성 정보를 얻는 방법 및 페이지 속성을 설정하는 방법을 보여줍니다.

## PDF 파일의 페이지 수 가져오기

문서를 다룰 때 종종 해당 문서가 몇 페이지인지 알고 싶습니다. Aspose.PDF를 사용하면 두 줄 이하의 코드만으로 가능합니다.

**Aspose.PDF for Go via C\u002B\u002B**는 페이지 수를 계산하도록 허용합니다 [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) 함수.

다음 코드 스니펫은 PDF 문서를 열고, 페이지 수를 가져온 다음 결과를 출력하도록 설계되었습니다.

그 [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) 이 메서드는 PDF 문서의 총 페이지 수를 가져오기 위해 호출됩니다. 이는 특정 페이지를 추출하거나 모든 페이지에 걸쳐 작업을 수행하는 등 문서의 길이를 알아야 하는 작업에 유용합니다. 이 메서드는 문서 구조를 간단히 조회하는 방법입니다.

PDF 파일의 페이지 수를 가져오려면:

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
      // PageCount() returns page count in PDF-document
      count, err := pdf.PageCount()
      if err != nil {
        log.Fatal(err)
      }
      // Print
      fmt.Println("Count:", count)
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## 페이지 크기 설정

이 예제에서 메서드 pdf.PageSetSize()는 PDF 문서의 첫 번째 페이지 크기를 변경합니다. PageSizeA1 상수는 첫 번째 페이지가 A1 용지 크기로 설정되도록 보장합니다. 이는 문서를 표준화된 형식으로 변환하거나 특정 콘텐츠가 페이지에 올바르게 맞도록 할 때 유용합니다.

1. PDF 문서를 다음을 사용하여 열기 [열기](https://reference.aspose.com/pdf/go-cpp/core/open/) 메서드.
1. 다음으로 페이지 크기 설정 [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/) 함수.
1. 문서를 저장하는 방법 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) 메서드.

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
        // PageSetSize(num int32, pageSize int32) sets size of page
        err = pdf.PageSetSize(1, asposepdf.PageSizeA1)
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_page1_SetSize_A1.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```