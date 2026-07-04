---
title: Go 언어를 사용한 Hello World 예제
linktitle: Hello World 예제
type: docs
weight: 40
url: /ko/go-cpp/hello-world-example/
description: 이 샘플은 Aspose.PDF for Go를 사용하여 Hello World 텍스트가 포함된 간단한 PDF 문서를 만드는 방법을 보여줍니다.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go를 통한 Hello World
Abstract: C++를 통한 Aspose.PDF for Go 시작 가이드는 라이브러리 사용에 대한 소개를 제공하며, PDF 문서를 생성하고 조작하는 기본 단계를 다룹니다. 여기에는 텍스트 내용이 포함된 간단한 PDF 파일을 생성하는 방법을 보여주는 'Hello World' 예제가 포함되어 있어 개발자가 API의 핵심 기능을 빠르게 이해할 수 있도록 도와줍니다.
SoftwareApplication: go-cpp
---

"Hello World" 예제는 일반적으로 프로그래밍 언어나 소프트웨어의 기능을 간단한 사용 사례로 소개하는 데 사용됩니다.

**Aspose.PDF for Go**는 개발자가 Go와 함께 PDF 문서 생성, 조작 및 변환 기능을 포함할 수 있는 기능이 풍부한 PDF API입니다. PDF, TXT, XPS, EPUB, TEX, DOC, DOCX, PPTX, 이미지 포맷 등 많은 인기 파일 포맷을 지원합니다. 이 문서에서는 텍스트 "Hello World!"를 포함하는 PDF 문서를 만드는 예를 보여줍니다. 환경에 Aspose.PDF for Go를 설치한 후, 코드 샘플을 실행하여 Aspose.PDF API가 어떻게 작동하는지 확인할 수 있습니다.
아래 코드 스니펫은 다음 단계들을 따릅니다:

1. 새 PDF 문서 인스턴스를 생성합니다.
1. PDF 문서에 새 페이지를 추가합니다, 사용하여 [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) 함수.
1. 페이지 크기를 사용하여 설정 [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/).
1. 첫 페이지에 "Hello World!" 텍스트를 추가합니다 [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/).
1. 복구된 PDF 문서를 사용하여 저장 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) 메서드.
1. PDF 문서를 닫고 할당된 리소스를 해제합니다.

다음 코드는 Aspose.PDF for Go API의 동작을 보여주는 Hello World 프로그램입니다.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // Create new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
                log.Fatal(err)
        }
        // Add new page
        err = pdf.PageAdd()
        if err != nil {
                log.Fatal(err)
        }
        // Set page size A4
        err = pdf.PageSetSize(1, asposepdf.PageSizeA4)
        if err != nil {
                log.Fatal(err)
        }
        // Add text on first page
        err = pdf.PageAddText(1, "Hello World!")
        if err != nil {
                log.Fatal(err)
        }
        // Save PDF-document with "hello.pdf" name
        err = pdf.SaveAs("hello.pdf")
        if err != nil {
                log.Fatal(err)
        }
        // Release allocated resources
        defer pdf.Close()
    }
```
