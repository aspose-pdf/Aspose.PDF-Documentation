---
title: إضافة مرفق من المسار
linktitle: إضافة مرفق من المسار
type: docs
weight: 20
url: /ar/python-net/add-attachment-from-path/
description: يقوم هذا المثال بربط ملف PDF المدخل وإرفاق ملف خارجي باستخدام مسار الملف الخاص به وحفظ ملف PDF المعدل مع المرفق المضمن.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإرفاق الملفات إلى ملف PDF باستخدام التحميل الزائد لمسار الملفات في Python
Abstract: يوضح هذا المثال كيفية إرفاق ملفات خارجية بمستند PDF باستخدام التحميل الزائد لمسار الملف لـ 'add_document_attachment () 'في Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. إنه يبسط إضافة المرفقات دون فتح دفق الملفات يدويًا.
---

يمكن أن يتضمن PDF ملفات مضمنة مثل المستندات أو جداول البيانات أو الصور للرجوع إليها أو التوزيع. يسمح لك التحميل الزائد لمسار الملف لـ 'add_document_attachment () 'بإضافة المرفقات مباشرة من مسار الملف، مما يلغي الحاجة إلى فتح الملف يدويًا.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) كائن.
1. قم بربط ملف PDF المدخل.
1. قم بإضافة المرفق باستخدام مسار الملف.
1. احفظ المستند المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachment_from_path(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment using file-path overload
    content_editor.add_document_attachment(
        attachment_file,
        "Attachment added using file path overload.",
    )
    # Save updated document
    content_editor.save(outfile)
```
