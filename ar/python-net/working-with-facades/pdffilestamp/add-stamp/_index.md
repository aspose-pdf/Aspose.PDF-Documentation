---
title: إضافة ختم إلى PDF
linktitle: إضافة ختم إلى PDF
type: docs
weight: 40
url: /ar/python-net/add-stamp/
description: تعرف على كيفية إضافة طابع إلى صفحات PDF باستخدام PDFfileStamp في Python.
lastmod: "2026-06-11"
TechArticle: true
AlternativeHeadline: إضافة طوابع نصية إلى PDF في Python
Abstract: توضح هذه المقالة كيفية إضافة محتوى الطوابع إلى مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET باستخدام واجهة PDFfileStamp. يوضح كيفية إنشاء طابع ووضعه على الصفحة والتحكم في التدوير والتعتيم وحفظ ملف PDF المحدث.
---

يوفر Aspose.PDF لبيثون عبر .NET [طابع ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) واجهة لإضافة محتوى متكرر إلى صفحات PDF. بالإضافة إلى الرؤوس والتذييلات وأرقام الصفحات، يمكنك استخدامها لوضع طوابع نصية على كل صفحة من صفحات المستند.

## أضف الطابع إلى PDF

بعد تكوين الختم، قم بربط ملف PDF المدخل بـ `PdfFileStamp`وأضف الطابع واحفظ ملف الإخراج. يقوم هذا بتطبيق الطابع الذي تم تكوينه عبر المستند.

```python
import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def add_stamp_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to a PDF file."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
