---
title: إضافة تعليق توضيحي للسطر
linktitle: إضافة تعليق توضيحي للسطر
type: docs
weight: 30
url: /ar/python-net/add-line-annotation/
description: يربط هذا المثال ملف PDF مُدخل، ويرسم تعليقًا توضيحيًا بخط أحمر مع نهايات الأسطر المربعة، ويحفظ ملف PDF المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة تعليق توضيحي خطي إلى PDF باستخدام محرر محتوى PDFفي Python
Abstract: يوضح هذا المثال كيفية إضافة تعليق توضيحي خطي إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يشرح كيفية تحديد نقاط البداية والنهاية للخط وحدود المستطيل وخصائص المظهر وحفظ المستند المحدث.
---

التعليقات التوضيحية للسطر مفيدة للتأكيد على النص أو تمييز العلاقات أو لفت الانتباه إلى مناطق محددة في PDF. مع [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك إنشاء تعليقات توضيحية للسطر برمجيًا عن طريق تحديد نقاط البداية والنهاية والمستطيل المحيط واللون ونمط الحدود ونهايات الأسطر.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط ملف PDF المدخل.
1. تعريف خصائص التعليق التوضيحي للسطر.
1. أضف التعليق التوضيحي للخط.
1. احفظ المستند المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_line_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create LineAnnotation object
    rect = apd.Rectangle(100, 100, 200, 200)
    contents = "This is line annotation"
    content_editor.create_line(
        rect,
        contents,
        100,
        100,
        200,
        200,
        1,
        1,
        apd.Color.red,
        "Solid",
        [3, 2],
        ["Square"],
    )

    # Save output PDF file
    content_editor.save(outfile)
```
