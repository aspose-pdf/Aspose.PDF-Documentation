---
title: Simpan dokumen PDF secara programatis
linktitle: Simpan PDF
type: docs
weight: 30
url: /id/python-cpp/save-pdf-document/
description: Pelajari cara menyimpan file PDF dalam Python Aspose.PDF untuk Python melalui pustaka C++. Simpan dokumen PDF ke sistem file, ke aliran, dan dalam aplikasi web.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Simpan dokumen PDF ke sistem file

```python

    import AsposePDFPythonWrappers as ap

    document = ap.Document("sample.pdf")
    document.pages.add()
    document.save("sample_mod.pdf")
```