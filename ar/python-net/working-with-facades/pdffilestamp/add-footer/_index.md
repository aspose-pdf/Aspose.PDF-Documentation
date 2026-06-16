---
title: إضافة تذييل إلى PDF
linktitle: إضافة تذييل إلى PDF
type: docs
weight: 10
url: /ar/python-net/add-footer/
description: تعرف على كيفية إضافة تذييلات النص والصور إلى صفحات PDF باستخدام PDFfileStamp في Python.
lastmod: "2026-06-11"
TechArticle: true
AlternativeHeadline: إضافة تذييلات النص والصورة إلى PDF في Python
Abstract: توضح هذه المقالة كيفية إضافة محتوى تذييل إلى مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET باستخدام واجهة PDFfileStamp. يوضح كيفية إضافة تذييل نص ووضع تذييل صورة وتطبيق هوامش تذييل مخصصة قبل حفظ ملف PDF المحدث.
---

يوفر Aspose.PDF لبيثون عبر .NET [طابع ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) واجهة لإضافة محتوى متكرر إلى صفحات PDF. يمكنك استخدامه لوضع نص التذييل أو الصور في أسفل كل صفحة وضبط هوامش التذييل للتحكم في الموضع.

## إضافة تذييل نصي

استخدم `add_footer()` مع `FormattedText` الكائن عندما تريد وضع نفس تذييل النص على كل صفحة من صفحات PDF. تقوم الوسيطة الثانية بتعيين الهامش السفلي المستخدم لوضع التذييل.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_footer(infile: str, outfile: str) -> None:
    """Add a text footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Footer")
        pdf_stamper.add_footer(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## إضافة تذييل صورة

استخدم `add_footer()` مع دفق الصور عندما يجب أن يعرض التذييل شعارًا أو صورة أخرى بدلاً من النص. يفتح المثال ملف الصورة كتدفق ثنائي ويضعه في أسفل كل صفحة.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_footer(infile: str, image_file: str, outfile: str) -> None:
    """Add an image footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_footer(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## إضافة تذييل بهوامش مخصصة

استخدم التحميل الزائد بثلاث قيم هامشية عندما تحتاج إلى مزيد من التحكم في موضع التذييل. في هذا المثال، تتم إضافة التذييل بهوامش سفلية ولليسار ولليمين مخصصة.

```python
import sys
from os import path
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_footer_with_margins(infile: str, outfile: str) -> None:
    """Add a text footer with bottom, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("This footer has margins on all sides.")
        pdf_stamper.add_footer(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
