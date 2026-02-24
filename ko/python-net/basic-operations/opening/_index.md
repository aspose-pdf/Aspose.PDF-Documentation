---
title: 프로그램을 통해 PDF 문서 열기
linktitle: PDF 열기
type: docs
weight: 20
url: /ko/python-net/open-pdf-document/
description: Python에서 .NET 라이브러리를 통해 Aspose.PDF for Python을 사용하여 PDF 파일을 여는 방법을 배웁니다. 기존 PDF, 스트림에서 문서, 그리고 암호화된 PDF 문서를 열 수 있습니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 Aspose.PDF 라이브러리를 사용하여 PDF 문서 열기
Abstract: 이 문서는 Python에서 Aspose.PDF 라이브러리를 사용하여 기존 PDF 문서를 여는 방법에 대한 안내를 제공합니다. 파일 이름을 지정하여 PDF를 여는 방법, 스트림에서 PDF를 여는 방법, 암호를 제공하여 암호화된 PDF를 여는 세 가지 방법을 설명합니다. 각 방법은 Aspose.PDF 라이브러리를 활용하여 PDF에 접근하고 포함된 페이지 수를 출력하는 코드 스니펫을 포함합니다. 이러한 예제는 다양한 PDF 파일 접근 시나리오를 처리할 수 있는 Aspose.PDF의 유연성과 기능을 보여줍니다.
---

## 기존 PDF 문서 열기

문서를 여는 방법은 여러 가지가 있습니다. 가장 쉬운 방법은 파일 이름을 지정하는 것입니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    print("Pages: " + str(len(document.pages)))
```

## 스트림에서 기존 PDF 문서 열기

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Open document
    document = ap.Document(stream)
    print("Pages: " + str(len(document.pages)))
```

## 암호화된 PDF 문서 열기

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf, password)
    print("Pages: " + str(len(document.pages)))
```

