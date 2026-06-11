---
title: إضافة مرفق
linktitle: إضافة مرفق
type: docs
weight: 10
url: /ar/python-net/add-attachment/
description: يقوم هذا المثال بربط ملف PDF المدخل وإرفاق ملف خارجي بالصفحة الأولى وحفظ ملف PDF المعدل مع المرفق المضمن.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة مرفقات الملفات إلى PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية إرفاق ملفات خارجية بمستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية ربط ملف PDF وإضافة مرفقات بالأوصاف وحفظ المستند المحدث.
---

تسمح لك مرفقات الملفات في ملفات PDF بتضمين المستندات التكميلية أو الصور أو الموارد الأخرى مباشرة داخل PDF. مع [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك إرفاق الملفات برمجيًا بصفحات محددة وتعيين اسم المرفق وتقديم وصف.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط ملف PDF المدخل.
1. افتح ملف المرفقات.
1. أضف المرفق إلى PDF.
1. احفظ المستند المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment to page 1
    with open(attachment_file, "rb") as attachment_stream:
        content_editor.add_document_attachment(
            attachment_stream,
            path.basename(attachment_file),
            "This is a sample attachment for demonstration purposes.",
        )
    # Save updated document
    content_editor.save(outfile)
```
