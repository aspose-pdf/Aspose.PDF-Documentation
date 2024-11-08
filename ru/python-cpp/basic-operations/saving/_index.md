---
title: Сохранение PDF-документа программно
linktitle: Сохранить PDF
type: docs
weight: 30
url: /ru/python-cpp/save-pdf-document/
description: Узнайте, как сохранить PDF-файл в Python с помощью библиотеки Aspose.PDF для Python через C++. Сохранение PDF-документа в файловую систему, в поток и в веб-приложениях.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Сохранение PDF-документа в файловую систему

```python

    import AsposePDFPythonWrappers as ap

    document = ap.Document("sample.pdf")
    document.pages.add()
    document.save("sample_mod.pdf")
```