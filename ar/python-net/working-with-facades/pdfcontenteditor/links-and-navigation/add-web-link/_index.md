---
title: إضافة رابط ويب
linktitle: إضافة رابط ويب
type: docs
weight: 60
url: /ar/python-net/add-web-link/
description: يربط هذا المثال ملف PDF مُدخل، ويضيف تعليقًا توضيحيًا لرابط الويب باللون الأزرق على الصفحة 1 يشير إلى صفحة منتج Python PDF الخاصة بـ Aspose، ويحفظ المستند المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة رابط ويب إلى PDF باستخدام PDFContentEditor في بايثون
Abstract: يوضح هذا المثال كيفية إضافة رابط ويب إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية إنشاء منطقة قابلة للنقر على صفحة تفتح عنوان URL محددًا في متصفح الويب وحفظ المستند المحدث.
---

تسمح روابط الويب في ملفات PDF للمستخدمين بالانتقال مباشرة إلى الموارد أو مواقع الويب أو الوثائق عبر الإنترنت. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك تحديد منطقة مستطيلة على صفحة PDF تفتح، عند النقر عليها، عنوان URL في متصفح الويب الافتراضي.

1. قم بإنشاء مثيل محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. حدد مستطيلًا لرابط الويب القابل للنقر.
1. حدد عنوان URL ورقم الصفحة ولون الارتباط.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_web_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a web link annotation to page 1
    content_editor.create_web_link(
        apd.Rectangle(100, 650, 200, 20),
        "https://products.aspose.com/pdf/python-net/",
        1,
        apd.Color.blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
