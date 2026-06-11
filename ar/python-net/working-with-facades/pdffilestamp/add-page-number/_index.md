---
title: إضافة رقم الصفحة إلى PDF
linktitle: إضافة رقم الصفحة إلى PDF
type: docs
weight: 30
url: /ar/python-net/page-number/
description: تعرف على كيفية إضافة أرقام الصفحات إلى مستندات PDF باستخدام PDFfileStamp في Python.
lastmod: "2026-06-11"
TechArticle: true
AlternativeHeadline: إضافة أرقام الصفحات إلى PDF في Python
Abstract: توضح هذه المقالة كيفية إضافة أرقام الصفحات إلى مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET باستخدام واجهة PDFfileStamp. ويعرض كيفية إضافة أرقام الصفحات بالموضع الافتراضي، ووضعها في الإحداثيات المخصصة، والتحكم في المحاذاة والهوامش.
---

يوفر Aspose.PDF لبيثون عبر .NET [طابع ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp/) واجهة لإضافة محتوى متكرر إلى صفحات PDF. يمكنك استخدامه لإدراج أرقام الصفحات ذات الموضع الافتراضي، أو وضعها في إحداثيات محددة، أو التحكم في محاذاتها وهوامشها.

## إضافة أرقام الصفحات بالموضع الافتراضي

استخدم `add_page_number()` بدون وسيطات الموضع الإضافية عندما تريد إضافة أرقام الصفحات في الموقع الافتراضي. هذه هي أبسط طريقة لترقيم كل صفحة في المستند.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_default(infile: str, outfile: str) -> None:
    """Add centered page numbers to the bottom of each page."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #")
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## إضافة أرقام الصفحات في الإحداثيات المخصصة

استخدم التحميل الزائد المستند إلى الإحداثيات عندما تحتاج إلى ظهور أرقام الصفحات في موضع X و Y محدد في كل صفحة. يكون هذا الأسلوب مفيدًا عندما يتطلب تخطيط المستند موضعًا مخصصًا.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_at_coordinates(infile: str, outfile: str) -> None:
    """Add page numbers at explicit X/Y coordinates."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #", 300, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## إضافة أرقام الصفحات مع المحاذاة والهوامش

استخدم التحميل الزائد مع وسيطات الموضع والهامش عندما تحتاج إلى مزيد من التحكم في مكان ظهور أرقام الصفحات. في هذا المثال، تتم محاذاة الأرقام إلى المنطقة العلوية اليمنى من الصفحة بهوامش صريحة.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_position_and_margins(infile: str, outfile: str) -> None:
    """Add page numbers using a predefined position and page margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number(
            "Page #",
            pdf_facades.PdfFileStamp.POS_BOTTOM_RIGHT,
            10,
            10,
            10,
            10,
        )
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## إضافة أرقام الصفحات بالنمط الروماني

تُظهر وظيفة «add_page_numbers_with_roman_style» كيفية تحسين مستند PDF عن طريق إضافة أرقام الصفحات باستخدام الأرقام الرومانية الكبيرة. إنه يستفيد من فئة PDFfileStamp من Aspose.PDF لتطبيق الترقيم المتسق عبر جميع الصفحات.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from config import initialize_data_dir, set_license


def add_page_numbers_with_roman_style(infile: str, outfile: str) -> None:
    """Add page numbers with a custom start value and Roman numbering."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE
        pdf_stamper.starting_number = 42
        pdf_stamper.add_page_number("Page #", pdf_facades.PdfFileStamp.POS_UPPER_RIGHT)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```
