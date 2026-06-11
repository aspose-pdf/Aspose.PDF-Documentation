---
title: إضافة تعليق توضيحي للدائرة
linktitle: إضافة تعليق توضيحي للدائرة
type: docs
weight: 10
url: /ar/python-net/add-circle-annotation/
description: يقوم هذا المثال بربط ملف PDF مُدخل، وإنشاء تعليق توضيحي على شكل دائرة على الصفحة الأولى، وحفظ المستند المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة تعليق توضيحي للدائرة إلى ملف PDF باستخدام محرر محتوى PDFفي بايثون
Abstract: يوضح هذا المثال كيفية إضافة تعليق توضيحي على شكل دائرة إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية تحديد حدود التعليقات التوضيحية وتعيين نص المحتوى وتكوين اللون والمظهر وحفظ المستند المحدث.
---

التعليقات التوضيحية الدائرية مفيدة لتسليط الضوء على مجالات الاهتمام في مستند PDF. مع [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك إنشاء أشكال دائرية من خلال تحديد المستطيل الذي يحدد حدود الدائرة، إلى جانب نص التعليق التوضيحي واللون وخيارات التعبئة ورقم الصفحة وعرض الحدود.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط ملف PDF المدخل.
1. حدد حدود الدائرة.
1. أضف التعليق التوضيحي للدائرة.
1. احفظ المستند المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_circle_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create CircleAnnotation object
    rect = apd.Rectangle(300, 300, 400, 400)
    contents = "This is circle annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, False, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
