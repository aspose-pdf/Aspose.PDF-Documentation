---
title: PDF 문서 프로그래밍 방식으로 열기
linktitle: PDF 열기
type: docs
weight: 20
url: ko/python-cpp/open-pdf-document/
description: Python Aspose.PDF for Python via C++ 라이브러리를 사용하여 PDF 파일을 여는 방법을 알아보세요. 기존 PDF, 스트림의 문서, 암호화된 PDF 문서를 열 수 있습니다.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 기존 PDF 문서 열기

문서를 여는 여러 가지 방법이 있습니다. 가장 쉬운 방법은 파일 이름을 지정하는 것입니다.

```python

    import AsposePDFPythonWrappers as ap
    # 문서 열기
    document = ap.Document("sample.pdf")
    count = document.pages.count()
    print("Pages: " + str(count))
```

## 암호화된 PDF 문서 열기

```python

    import AsposePDFPythonWrappers as ap
    # 문서 열기
    document = ap.Document("sample.pdf","password")
    count = document.pages.count()
    print("Pages: " + str(count))
```