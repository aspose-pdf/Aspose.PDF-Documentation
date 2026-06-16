---
title: إضافة عنصر قائمة
linktitle: إضافة عنصر قائمة
type: docs
weight: 10
url: /ar/python-net/add-list-item/
description: يوضح هذا المثال كيفية إضافة عناصر إلى حقل نموذج مربع القائمة في مستند PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة عناصر إلى حقول مربع قائمة PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية فتح مستند PDF وإلحاق العناصر بحقل مربع القائمة المسمى «البلد» وحفظ المستند المحدث.
---

تسمح حقول مربع القائمة في ملفات PDF للمستخدمين بتحديد خيار واحد أو عدة خيارات من مجموعة محددة مسبقًا. باستخدام Aspose.PDF لـ Python، يمكن للمطورين إضافة عناصر جديدة برمجيًا إلى هذه الحقول. ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) توفر الفئة طريقة «add_list_item» لإلحاق العناصر بحقل مربع القائمة الحالي.

1. افتح نموذج PDF موجود.
1. قم بإنشاء كائن ForMeditor.
1. قم بربط ملف PDF إلى ForMeditor.
1. أضف عناصر إلى حقل مربع القائمة «البلد».
1. احفظ المستند المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_list_item(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Add list item to list box field
    form_editor.add_list_item("Country", ["New Zealand", "New Zealand"])
    # Save updated document
    form_editor.save(outfile)
```
