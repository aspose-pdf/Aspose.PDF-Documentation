---
title: نقل الحقل
linktitle: نقل الحقل
type: docs
weight: 50
url: /ar/python-net/move-field/
description: انقل حقل نموذج موجود إلى موضع مختلف في مستند PDF.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: نقل حقل نموذج PDF إلى موضع جديد باستخدام Python
Abstract: يوضح هذا المثال كيفية نقل حقل نموذج موجود إلى موضع مختلف في مستند PDF باستخدام Aspose.PDF لـ Python. يفتح الكود ملف PDF موجود، وينقل حقل النموذج المحدد إلى إحداثيات جديدة، ويحفظ المستند المحدث.
---

غالبًا ما تتطلب نماذج PDF تعديلات التخطيط بعد الإنشاء. باستخدام Aspose.PDF لـ Python، يمكن للمطورين نقل حقول النموذج الحالية إلى موضع جديد دون إعادة إنشائها.

يوضح هذا المثال كيفية إعادة وضع حقل «البلد» من خلال تحديد إحداثيات جديدة لوضعه داخل الصفحة. ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) توفر الفئة طريقة move_field لنقل الحقول داخل صفحة PDF.

1. افتح نموذج PDF الحالي.
1. قم بإنشاء كائن ForMeditor.
1. قم بربط وثيقة PDF إلى ForMeditor.
1. انقل حقل «البلد» إلى موضع جديد باستخدام الإحداثيات.
1. احفظ المستند المعدل.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Move field to new page
    form_editor.move_field("Country", 200, 600, 280, 620)
    # Save updated document
    form_editor.save(outfile)
```
