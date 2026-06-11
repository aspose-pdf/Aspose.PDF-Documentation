---
title: إضافة تعليق توضيحي على شكل مضلع
linktitle: إضافة تعليق توضيحي على شكل مضلع
type: docs
weight: 40
url: /ar/python-net/add-polygon-annotation/
description: يربط هذا المثال ملف PDF مُدخل، ويرسم مضلعًا صلبًا على الصفحة الأولى، ويحفظ المستند المعدل مع تعليق توضيحي.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة تعليق توضيحي على شكل مضلع إلى ملف PDF باستخدام محرر محتوى PDFفي بايثون
Abstract: يوضح هذا المثال كيفية إضافة تعليق توضيحي مضلع إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية تحديد رؤوس المضلع ونمط الحدود وحدود التعليقات التوضيحية والنص الوصفي وحفظ المستند المحدث.
---

تُستخدم التعليقات التوضيحية المضلعة لتسليط الضوء على المناطق أو الأشكال غير المنتظمة في PDF، وتوفير التركيز البصري أو وضع علامات على مناطق محددة. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك إنشاء المضلعات من خلال تحديد إحداثيات الرؤوس ونمط الحدود ورقم الصفحة ومستطيل التعليق التوضيحي.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط ملف PDF المدخل.
1. قم بتكوين خصائص المضلع.
1. أضف التعليق التوضيحي لـ Polygon.
1. احفظ المستند المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polygon_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [100, 200, 150, 260, 220, 220, 200, 160]
    content_editor.create_polygon(
        line_info,
        1,
        apd.Rectangle(90, 150, 150, 120),
        "This is polygon annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
