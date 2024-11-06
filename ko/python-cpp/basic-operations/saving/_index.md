---
title: PDF 문서를 프로그래밍 방식으로 저장
linktitle: PDF 저장
type: docs
weight: 30
url: ko/python-cpp/save-pdf-document/
description: Python Aspose.PDF for Python via C++ 라이브러리를 사용하여 PDF 파일을 저장하는 방법을 배웁니다. 파일 시스템, 스트림 및 웹 애플리케이션에 PDF 문서를 저장합니다.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 파일 시스템에 PDF 문서 저장

```python

    import AsposePDFPythonWrappers as ap

    document = ap.Document("sample.pdf")  # PDF 문서를 엽니다
    document.pages.add()  # 페이지를 추가합니다
    document.save("sample_mod.pdf")  # 변경된 문서를 저장합니다
```