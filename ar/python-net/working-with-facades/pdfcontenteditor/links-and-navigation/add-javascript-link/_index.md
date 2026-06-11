---
title: إضافة رابط جافا سكريبت
linktitle: إضافة رابط جافا سكريبت
type: docs
weight: 30
url: /ar/python-net/add-javascript-link/
description: يربط هذا المثال ملف PDF للإدخال، ويضيف رابط JavaScript يقوم بتشغيل تنبيه عند النقر، ويحفظ المستند المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة رابط جافا سكريبت إلى PDF باستخدام محرر محتوى PDFفي بايثون
Abstract: يوضح هذا المثال كيفية إضافة رابط JavaScript إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية إنشاء منطقة قابلة للنقر تقوم بتنفيذ شفرة JavaScript عند النقر عليها، وحفظ ملف PDF المحدث.
---

تسمح روابط JavaScript في ملفات PDF بوظائف تفاعلية مثل عرض التنبيهات أو إجراء العمليات الحسابية أو تعديل محتوى المستند ديناميكيًا. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك تحديد مستطيل قابل للنقر على الصفحة وربطه بشفرة JavaScript المخصصة.

1. قم بإنشاء مثيل محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. حدد مستطيلًا لرابط JavaScript القابل للنقر.
1. حدد رقم الصفحة ولون الرابط.
1. قم بتعيين كود JavaScript للتنفيذ عند النقر عليه.
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


def add_javascript_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript link action
    content_editor.create_java_script_link(
        "app.alert('PdfContentEditor JavaScript link');",
        apd.Rectangle(160, 560, 260, 20),
        1,
        apd.Color.orange,
    )
    # Save updated document
    content_editor.save(outfile)
```
