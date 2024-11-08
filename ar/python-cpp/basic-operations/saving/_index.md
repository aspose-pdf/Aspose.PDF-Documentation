---
title: حفظ مستند PDF برمجيًا
linktitle: حفظ PDF
type: docs
weight: 30
url: /ar/python-cpp/save-pdf-document/
description: تعلم كيفية حفظ ملف PDF في مكتبة Aspose.PDF لـ Python عبر C++. حفظ مستند PDF في نظام الملفات، إلى تيار، وفي تطبيقات الويب.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## حفظ مستند PDF في نظام الملفات

```python

    import AsposePDFPythonWrappers as ap

    document = ap.Document("sample.pdf")
    document.pages.add()
    document.save("sample_mod.pdf")
```