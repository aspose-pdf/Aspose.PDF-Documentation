---
title: Aspose PDF 라이선스
linktitle: 라이선스 및 제한 사항
type: docs
weight: 90
url: /ko/go-cpp/licensing/
description: Aspose. PDF for Go는 고객에게 클래식 라이선스를 얻도록 권장합니다. 또한 제한된 라이선스를 사용하여 제품을 더 잘 탐색할 수 있습니다.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go via C++의 라이선스
Abstract: Aspose.PDF for Go via C++의 라이선스 페이지에서는 제품에 대한 사용 가능한 라이선스 옵션을 설명합니다. 고객은 클래식 라이선스, Metered License 또는 평가용 제한된 라이선스 중에서 선택할 수 있습니다. 또한 이 페이지는 전체 기능을 활성화하고 평가 제한을 제거하는 등 적절한 라이선스를 확보했을 때의 이점을 강조합니다.
SoftwareApplication: go-cpp
---


## 평가 버전의 제한

고객이 구매 전에 당사 구성 요소를 충분히 테스트해 보기를 원하므로 평가 버전에서는 일반적인 사용 방식대로 사용할 수 있습니다.

- **평가 워터마크가 있는 문서.** Aspose.PDF for Go의 평가 버전은 전체 제품 기능을 제공하지만, 생성된 파일의 모든 페이지 상단에 "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." 텍스트가 워터마크로 표시됩니다.

- **처리할 수 있는 페이지 수를 제한합니다.**
평가 버전에서는 문서의 처음 네 페이지만 처리할 수 있습니다.

>평가 버전 제한 없이 Aspose.PDF for Go를 테스트하려면 30일 임시 라이선스를 요청할 수 있습니다. 자세한 내용은 [임시 라이선스를 받는 방법은?](https://purchase.aspose.com/temporary-license)

## 클래식 라이선스

라이선스 파일(Aspose.PDF.GoViaCPP.lic)을 사용하여 Aspose.PDF 라이브러리의 전체 기능을 활성화하기 위해 라이선스를 적용합니다.

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
        // SetLicense(filename string) licenses with filename
        err = pdf.SetLicense("Aspose.PDF.GoViaCPP.lic")
        if err != nil {
            log.Fatal(err)
        }
        // Working with PDF-document
        // ...
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
