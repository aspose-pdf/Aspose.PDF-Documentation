---
title: إضافة تعليق توضيحي للمنحنى
linktitle: إضافة تعليق توضيحي للمنحنى
type: docs
weight: 20
url: /ar/python-net/add-curve-annotation/
description: يقوم هذا المثال بربط ملف PDF للإدخال، ويرسم منحنى متقطع على الصفحة الأولى، ويحفظ المستند المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة تعليق توضيحي للمنحنى إلى PDF باستخدام محرر محتوى PDFفي بايثون
Abstract: يوضح هذا المثال كيفية إضافة تعليق توضيحي منحني إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية تحديد رؤوس المنحنيات ونمط الحدود وحدود التعليقات التوضيحية ومحتوى النص وحفظ المستند المحدث.
---

تُستخدم التعليقات التوضيحية للمنحنى لتسليط الضوء على المسارات أو الأشكال غير المنتظمة في PDF، مما يوفر التركيز البصري أو تحديد المناطق المهمة. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك رسم منحنيات من خلال تحديد سلسلة من الرؤوس ونمط الحدود والرؤية ومستطيل التعليق التوضيحي والنص الوصفي.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط ملف PDF المُدخَّل.
1. قم بتكوين خصائص المنحنى.
1. ارسم التعليق التوضيحي للمنحنى.
1. احفظ المستند المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_curve_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 1  # 1 - Dashed
    line_info.vertice_coordinate = [120, 520, 160, 560, 220, 540, 280, 580]
    line_info.visibility = True
    content_editor.draw_curve(
        line_info,
        1,
        apd.Rectangle(110, 510, 220, 100),
        "This is curve annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
