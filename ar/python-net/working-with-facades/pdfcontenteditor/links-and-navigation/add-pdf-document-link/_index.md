---
title: إضافة رابط مستند PDF
linktitle: إضافة رابط مستند PDF
type: docs
weight: 50
url: /ar/python-net/add-pdf-document-link/
description: يربط هذا المثال ملف PDF مُدخل، ويضيف رابطًا باللون الأخضر إلى صفحة في PDF آخر، ويحفظ المستند المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة رابط مستند PDF باستخدام محرر محتوى PDF في بايثون
Abstract: يوضح هذا المثال كيفية إضافة رابط إلى مستند PDF آخر باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية إنشاء منطقة قابلة للنقر تفتح ملف PDF مختلفًا وحفظ المستند المحدث.
---

تسمح روابط مستندات PDF للمستخدمين بالانتقال من ملف PDF إلى آخر بسلاسة. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك تحديد مستطيل قابل للنقر يرتبط بصفحة في ملف PDF مختلف، مما يجعل مستنداتك تفاعلية ومتصلة.

1. قم بإنشاء مثيل محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. حدد مستطيلًا للارتباط القابل للنقر.
1. حدد ملف PDF المرتبط وصفحة المصدر وصفحة الوجهة.
1. قم بتعيين لون الارتباط.
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


def add_pdf_document_link(infile, linked_pdf, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add link to another PDF document
    content_editor.create_pdf_document_link(
        apd.Rectangle(140, 590, 240, 20),
        linked_pdf,
        1,
        1,
        apd.Color.green,
    )
    # Save updated document
    content_editor.save(outfile)
```
