---
title: إزالة الحقل
linktitle: إزالة الحقل
type: docs
weight: 60
url: /ar/python-net/remove-field/
description: يوضح هذا المثال كيفية حذف حقل «البلد» من نموذج PDF باستخدام طريقة «remove_field» لفئة «forMeditor».
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإزالة حقل نموذج من مستند PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية إزالة حقل نموذج موجود من مستند PDF باستخدام Aspose.PDF لـ Python. يقوم الكود بتحميل ملف PDF وحذف الحقل المحدد باستخدام فئة ForMeditor وحفظ المستند المحدث.
---

قد تحتوي نماذج PDF على حقول لم تعد مطلوبة بسبب تغييرات التصميم أو تحديثات سير العمل. باستخدام Aspose.PDF لـ Python، يمكن للمطورين بسهولة إزالة حقول نموذج معينة برمجيًا.

ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) توفر الفئة في Aspose.PDF طريقة «remove_field»، والتي تسمح للمطورين بحذف حقل النموذج باسمه.

1. قم بتحميل وثيقة PDF.
1. قم بإنشاء كائن ForMeditor.
1. قم بربط ملف PDF إلى ForMeditor.
1. قم بإزالة حقل النموذج المحدد.
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Remove field from document
    form_editor.remove_field("Country")
    # Save updated document
    form_editor.save(outfile)
```
