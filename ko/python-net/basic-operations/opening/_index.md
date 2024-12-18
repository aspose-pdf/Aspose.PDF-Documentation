---
title: PDF 문서 프로그래밍 방식으로 열기
linktitle: PDF 열기
type: docs
weight: 20
url: /ko/python-net/open-pdf-document/
description: Python Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 파일을 여는 방법을 알아보세요. 기존 PDF, 스트림의 문서 및 암호화된 PDF 문서를 열 수 있습니다.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 기존 PDF 문서 열기

문서를 여는 몇 가지 방법이 있습니다. 가장 쉬운 방법은 파일 이름을 지정하는 것입니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)
    print("페이지 수: " + str(len(document.pages)))
```

## 스트림에서 기존 PDF 문서 열기

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # 문서 열기
    document = ap.Document(stream)
    print("페이지 수: " + str(len(document.pages)))
```

## 암호화된 PDF 문서 열기

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf, password)
    print("페이지 수: " + str(len(document.pages)))
```