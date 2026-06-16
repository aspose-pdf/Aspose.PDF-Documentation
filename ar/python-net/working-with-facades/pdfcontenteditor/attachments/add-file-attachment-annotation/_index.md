---
title: إضافة تعليق توضيحي لمرفق الملف
linktitle: إضافة تعليق توضيحي لمرفق الملف
type: docs
weight: 30
url: /ar/python-net/add-file-attachment-annotation/
description: يقوم المثال بربط ملف PDF للإدخال وإضافة تعليق توضيحي لمرفق الملف إلى الصفحة الأولى باستخدام مسار الملف وحفظ المستند المحدث.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة التعليقات التوضيحية لمرفقات الملفات إلى PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية إنشاء تعليق توضيحي لمرفق الملف في ملف PDF باستخدام مسار ملف مع Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية تحديد موضع التعليق التوضيحي وتعيين نص الوصف واختيار نوع الرمز وحفظ المستند المعدل.
---

تسمح لك التعليقات التوضيحية لمرفقات الملفات بتضمين ملفات خارجية كرموز تفاعلية على صفحة PDF. باستخدام التحميل الزائد لمسار الملف، يمكنك إرفاق الملفات مباشرة من القرص دون فتح التدفقات يدويًا. تتيح لك هذه الطريقة أيضًا تخصيص رمز التعليق التوضيحي وتقديم وصف للمستخدمين.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) كائن.
1. قم بربط ملف PDF المدخل.
1. حدد مستطيل التعليق التوضيحي.
1. أضف التعليق التوضيحي لمرفق الملف.
1. احفظ المستند المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_file_attachment_annotation(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create file attachment annotation on page 1
    content_editor.create_file_attachment(
        apd.Rectangle(100, 520, 20, 20),
        "Attachment annotation contents",
        attachment_file,
        1,
        "PushPin",
    )
    # Save updated document
    content_editor.save(outfile)
```
