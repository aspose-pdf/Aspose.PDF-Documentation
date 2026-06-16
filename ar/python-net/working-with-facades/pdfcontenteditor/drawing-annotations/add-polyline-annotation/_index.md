---
title: إضافة تعليق توضيحي متعدد الخطوط
linktitle: إضافة تعليق توضيحي متعدد الخطوط
type: docs
weight: 50
url: /ar/python-net/add-polyline-annotation/
description: يقوم المثال بربط ملف PDF مُدخل، وإنشاء خط متعدد الأسطر في الصفحة الأولى، وحفظ المستند المعدل مع تعليق توضيحي.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف تعليقًا توضيحيًا متعدد الأسطر إلى ملف PDF باستخدام محرر محتوى PDFفي Python
Abstract: يوضح هذا المثال كيفية إضافة تعليق توضيحي متعدد الأسطر إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية تحديد تسلسل الرؤوس ونمط الحدود ومستطيل التعليق التوضيحي والنص وحفظ المستند المحدث.
---

تسمح لك التعليقات التوضيحية متعددة الخطوط بتمييز سلسلة من مقاطع الخطوط المتصلة في PDF. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك رسم خط متعدد الخطوط عن طريق تحديد إحداثيات الرؤوس ونمط الحدود ورقم الصفحة وحدود التعليقات التوضيحية. وهذا مفيد لتمثيل المسارات أو الاتجاهات أو الاتصالات بشكل مرئي في المخططات والمستندات.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط ملف PDF المدخل.
1. قم بتكوين خصائص الخطوط المتعددة.
1. أضف التعليق التوضيحي متعدد الخطوط.
1. احفظ المستند المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_polyline_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    line_info = pdf_facades.LineInfo()
    line_info.border_style = 0  # 0 - Solid
    line_info.vertice_coordinate = [120, 420, 180, 460, 230, 430, 290, 470]
    content_editor.create_poly_line(
        line_info,
        1,
        apd.Rectangle(110, 410, 200, 90),
        "This is polyline annotation",
    )

    # Save output PDF file
    content_editor.save(outfile)
```
