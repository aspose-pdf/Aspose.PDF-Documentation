---
title: PDF 문서를 프로그래밍 방식으로 저장
linktitle: PDF 저장
type: docs
weight: 30
url: /ko/go-cpp/save-pdf-document/
description: C++를 통해 Aspose.PDF for Go로 PDF 파일을 저장하는 방법을 배웁니다.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: C++를 통해 Aspose.PDF for Go로 PDF 문서 저장
Abstract: Aspose.PDF for Go via C++는 높은 효율성과 유연성을 갖춘 다양한 형식과 위치에 PDF 문서를 저장하는 포괄적인 기능을 제공합니다. 이 라이브러리를 사용하면 개발자가 PDF를 파일 시스템이나 메모리 스트림에 저장하거나 DOCX, XLSX, 이미지와 같은 대체 형식으로 출력할 수 있습니다. 저장 매개변수를 사용자 정의하고 파일 크기를 최적화하며 데이터 무결성을 보장하는 옵션을 제공합니다. 문서에는 자세한 설명과 코드 샘플이 포함되어 있어 개발자가 애플리케이션에서 PDF 저장 기능을 효율적으로 구현할 수 있도록 돕습니다.
SoftwareApplication: go-cpp
---

## PDF 문서를 파일 시스템에 저장

예제는 다음을 보여줍니다 [New](https://reference.aspose.com/pdf/go-cpp/core/new/) 새 PDF 문서를 생성하는 메서드로, 보고서나 청구서와 같이 동적으로 문서를 생성하는 기본 기능입니다.

코드는 간단하며 텍스트, 이미지 또는 주석을 PDF에 추가하는 등 더 고급 기능을 위한 템플릿 역할을 할 수 있습니다.

이 예제는 Aspose.PDF Go 라이브러리의 직관적인 사용을 보여주며, 문서를 생성, 수정 및 저장하는 잠재력을 나타냅니다.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // New creates a new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_New_SaveAs.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
