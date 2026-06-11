---
title: إضافة رأس إلى PDF
linktitle: إضافة رأس إلى PDF
type: docs
weight: 20
url: /ar/python-net/add-header/
description: تعرف على كيفية إضافة رؤوس النص والصور إلى صفحات PDF باستخدام PDFfileStamp في Python.
lastmod: "2026-06-11"
TechArticle: true
AlternativeHeadline: أضف رؤوس النص والصورة إلى PDF في Python
Abstract: تشرح هذه المقالة كيفية إضافة محتوى رأس إلى مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET باستخدام واجهة PDFfileStamp. يوضح كيفية إضافة رأس نص ووضع رأس صورة وتطبيق هوامش رأس مخصصة قبل حفظ ملف PDF المحدث.
---

يوفر Aspose.PDF لبيثون عبر .NET [طابع ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) واجهة لإضافة محتوى متكرر إلى صفحات PDF. يمكنك استخدامه لوضع نص العنوان أو الصور في أعلى كل صفحة وضبط هوامش العنوان للتحكم في الموضع.

## إضافة رأس نص

استخدم `add_header()` مع `FormattedText` الكائن عندما تريد وضع نفس نص العنوان على كل صفحة من صفحات PDF. تحدد الوسيطة الثانية الهامش العلوي للرأس.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_text_header(infile: str, outfile: str) -> None:
    """Add a text header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText("Sample Header")
        pdf_stamper.add_header(text, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## إضافة رأس صورة

استخدم `add_header()` مع ملف صورة أو دفق صور عندما يجب أن يعرض العنوان شعارًا أو رسمًا آخر. هذا مفيد لتخطيطات المستندات ذات العلامات التجارية.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_image_header(infile: str, image_file: str, outfile: str) -> None:
    """Add an image header with a top margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_header(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## إضافة عنوان بهوامش مخصصة

استخدم التحميل الزائد بثلاث قيم هامشية عندما تحتاج إلى مزيد من التحكم في موضع العنوان. في هذا المثال، تتم إضافة العنوان بهوامش مخصصة علوية ولليسار ولليمين.

```python
import sys
from os import path

import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_header_with_margins(infile: str, outfile: str) -> None:
    """Add a text header with top, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        text = pdf_facades.FormattedText(
            text="Sample Header",
            text_color=ap_pydrawing.Color.blue,
            font_name="Arial",
            text_encoding=pdf_facades.EncodingType.WINANSI,
            embedded=True,
            font_size=12.0,
        )
        pdf_stamper.add_header(text, 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
