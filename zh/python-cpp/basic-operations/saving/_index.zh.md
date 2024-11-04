---
title: 程序化保存PDF文档
linktitle: 保存PDF
type: docs
weight: 30
url: /python-cpp/save-pdf-document/
description: 学习如何在Python中使用Aspose.PDF for Python via C++库保存PDF文件。将PDF文档保存到文件系统、流中以及Web应用程序中。
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 将PDF文档保存到文件系统

```python

    import AsposePDFPythonWrappers as ap

    document = ap.Document("sample.pdf")
    document.pages.add()
    document.save("sample_mod.pdf")
```