---
title: إضافة تعليقات توضيحية للترميز
linktitle: إضافة تعليقات توضيحية للترميز
type: docs
weight: 30
url: /ar/python-net/add-markup-annotation/
description: يربط هذا المثال ملف PDF مُدخل، ويضيف أربعة تعليقات توضيحية مختلفة للترميز إلى الصفحة الأولى، ويحفظ المستند المحدث. يوضح كل تعليق توضيحي نمطًا ولونًا مختلفين للترميز.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف التعليقات التوضيحية الخاصة بالإبراز والتسطير والشطب والتأشير المتعرج في ملف PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية إضافة تعليقات توضيحية متعددة للترميز - التمييز والتسطير والشطب والتعرج - إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح النموذج كيفية تحديد مناطق التعليقات التوضيحية وتحديد أنواع العلامات وتطبيق الألوان وحفظ المستند المعدل.
---

يتم استخدام التعليقات التوضيحية للتوصيف للتأكيد على النص أو مراجعته داخل PDF. باستخدام PDFContentEditor، يمكنك تطبيق أنماط ترميز مختلفة برمجيًا عن طريق تحديد منطقة المستطيل ونص التعليق ونوع الترميز ورقم الصفحة واللون.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) كائن.
1. قم بربط ملف PDF المدخل.
1. حدد مستطيلات التعليقات التوضيحية.
1. إضافة تعليقات توضيحية للترميز.
1. احفظ المستند المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_markup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add markup annotation to page 1
    content_editor.create_markup(
        apd.Rectangle(120, 440, 200, 20),
        "This is a highlight annotation",
        0,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 542, 200, 20),
        "This is a underline annotation",
        1,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(120, 568, 200, 20),
        "This is a strikeout annotation",
        2,
        1,
        apd.Color.orange_red,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 598, 200, 20),
        "This is a squiggly annotation",
        3,
        1,
        apd.Color.dark_blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
