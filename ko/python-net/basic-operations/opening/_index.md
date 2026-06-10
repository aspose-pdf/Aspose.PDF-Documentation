---
title: 프로그래밍 방식으로 PDF 문서 열기
linktitle: PDF 열기
type: docs
weight: 20
url: /ko/python-net/open-pdf-document/
description: .NET 라이브러리를 통해 파이썬용 Aspose.PDF 파이썬 PDF 파일을 여는 방법을 알아보세요.기존 PDF, 스트림의 문서, 암호화된 PDF 문서를 열 수 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 Aspose.PDF 라이브러리를 사용하여 PDF 문서 열기
Abstract: 이 문서에서는 Python에서 Aspose.PDF 라이브러리를 사용하여 기존 PDF 문서를 여는 방법에 대한 가이드를 제공합니다.이를 위한 세 가지 방법, 즉 파일 이름을 지정하여 PDF를 열고, 스트림에서 PDF를 열고, 암호를 입력하여 암호화된 PDF를 여는 방법을 간략하게 설명합니다.각 방법에는 Aspose.PDF 라이브러리를 활용하여 PDF에 액세스하고 PDF에 포함된 페이지 수를 인쇄하는 방법을 보여주는 코드 스니펫이 포함되어 있습니다.이 예제는 다양한 PDF 파일 액세스 시나리오를 처리하기 위한 Aspose.PDF 의 유연성과 기능을 보여줍니다.
---

## 기존 PDF 문서 열기

문서를 여는 방법에는 여러 가지가 있습니다.가장 쉬운 방법은 파일 이름을 지정하는 것입니다.

```python
import aspose.pdf as ap

def open_document_from_file(infile):

    # Open document
    document = ap.Document(infile)
    print("Pages: " + str(len(document.pages)))
```

## 스트림에서 기존 PDF 문서 열기

```python
import aspose.pdf as ap
import io

def open_document_from_stream(infile):
    with io.FileIO(infile, "r") as stream:
        # Open document
        document = ap.Document(stream)
        print("Pages: " + str(len(document.pages)))
```

## 암호화된 PDF 문서 열기

```python
import aspose.pdf as ap

def open_document_encrypted(infile):
    password = "P@ssw0rd"
    # Open document
    document = ap.Document(infile, password)
    print("Pages: " + str(len(document.pages)))
```
