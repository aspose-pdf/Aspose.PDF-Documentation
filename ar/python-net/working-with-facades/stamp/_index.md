---
title: فئة الطوابع
linktitle: فئة الطوابع
type: docs
weight: 150
url: /ar/python-net/stamp-class/
description: تعرف على كيفية العمل مع فئة Stamp لإضافة صور وPDF وطوابع نصية إلى مستندات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يوفر Aspose.PDF لبيثون عبر .NET [ختم](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/stamp/) فئة لوضع محتوى مرئي قابل لإعادة الاستخدام على صفحات PDF. يمكن أن يستند الختم إلى نص أو صورة أو حتى صفحة من PDF آخر، ويمكن وضعه وتدويره وتصميمه وقصره على صفحات محددة.

توضح هذه المقالة العديد من عمليات سير عمل الطوابع الشائعة:

1. قم بإنشاء موارد نصية قابلة لإعادة الاستخدام للطوابع النصية.
1. أضف طوابع صور وصفحة PDF.
1. أضف طوابع نصية ذات نمط.
1. حدد الطابع للصفحات المحددة.
1. قم بتكوين طابع صورة الخلفية.

يستخدم المثال وظيفتين مساعدتين: واحدة تنشئ نصًا منسقًا للطوابع النصية، والأخرى تنشئ `TextState` الكائن المستخدم لتصميم الطوابع النصية.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def _create_text_logo(text: str) -> pdf_facades.FormattedText:
    """Create formatted text for text stamp examples."""
    return pdf_facades.FormattedText(
        text,
        drawing.Color.blue,
        drawing.Color.light_gray,
        pdf_facades.FontStyle.HELVETICA_BOLD,
        pdf_facades.EncodingType.WINANSI,
        True,
        14,
    )


def _create_text_state() -> ap.text.TextState:
    """Create a text state used to style text stamps."""
    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.dark_blue
    text_state.font_size = 16
    text_state.font_style = ap.text.FontStyles.BOLD
    return text_state
```

## إضافة طابع صورة

استخدم `bind_image()` عندما يجب أن يعرض الطابع صورة مثل الشعار أو الشارة أو الرمز. بعد ربط الصورة، يمكنك تعيين معرف الختم والأصل قبل إضافته إلى المستند.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to the PDF."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.stamp_id = 1
        stamp.set_origin(36, 520)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## إضافة صفحة PDF كطابع

استخدم `bind_pdf()` عندما تريد استخدام صفحة من ملف PDF آخر كمحتوى ختم. يعد هذا مفيدًا للتراكبات مثل الموافقات أو القوالب أو العناصر المرئية التي تم إنشاؤها مسبقًا المخزنة في مستند منفصل.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_pdf_page_as_stamp(infile: str, stamp_pdf: str, outfile: str) -> None:
    """Add the first page of another PDF as a stamp."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_pdf(stamp_pdf, 1)
        stamp.page_number = 1
        stamp.set_origin(36, 250)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## أضف طابعًا نصيًا مع حالة النص

استخدم `bind_logo()` جنبا إلى جنب مع `bind_text_state()` عندما تريد إنشاء طابع نصي باستخدام نمط خط مخصص. يُعد هذا الأسلوب مفيدًا لعلامات الموافقة والتسميات والتعليقات التوضيحية الخاصة بسير العمل.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_text_stamp_with_text_state(infile: str, outfile: str) -> None:
    """Add a text stamp and style it with a TextState object."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_logo(_create_text_logo("Approved by signing workflow"))
        stamp.bind_text_state(_create_text_state())
        stamp.set_origin(36, 700)
        stamp.rotation = 15.0

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## إضافة طابع إلى صفحات محددة

في حالة عدم ظهور الطابع في كل صفحة، قم بتعيين أرقام الصفحات المستهدفة إلى `pages` الملكية. يضيف هذا المثال ختم صورة إلى الصفحة الأولى فقط.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_stamp_to_specific_pages(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp only to the selected pages."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.pages = [1]
        stamp.set_origin(400, 40)
        stamp.set_image_size(120, 60)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## إضافة طابع صورة خلفية

استخدم ختم الخلفية عندما يجب أن تظهر الصورة خلف محتوى الصفحة. يمكنك أيضًا التحكم في عتامة الختم والدوران والجودة والحجم والموضع لإنشاء تأثيرات بنمط العلامة المائية.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_background_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add a rotated background image stamp with opacity and quality settings."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.is_background = True
        stamp.opacity = 0.35
        stamp.quality = 90
        stamp.rotation = 45.0
        stamp.set_image_size(160, 80)
        stamp.set_origin(200, 300)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## موضوعات الواجهات ذات الصلة

- [العمل مع واجهات PDF في بايثون](/pdf/ar/python-net/working-with-facades/)
- [أضف الرؤوس والتذييلات والطوابع باستخدام PDFfileStamp](/pdf/ar/python-net/pdffilestamp-class/)
- [أضف طابع صفحة إلى ملفات PDF في Python](/pdf/ar/python-net/add-stamp/)
