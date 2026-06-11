---
title: إضافة تعليق توضيحي على شكل مربع
linktitle: إضافة تعليق توضيحي على شكل مربع
type: docs
weight: 60
url: /ar/python-net/add-square-annotation/
description: يربط هذا المثال ملف PDF مُدخل، ويضيف تعليقًا توضيحيًا مربعًا أزرق ممتلئًا على الصفحة الأولى، ويحفظ المستند المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة تعليق توضيحي مربع إلى PDF باستخدام محرر محتوى PDFفي Python
Abstract: يوضح هذا المثال كيفية إضافة تعليق توضيحي مربع إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية تحديد مستطيل التعليق التوضيحي ومحتوى النص واللون وخيارات التعبئة وحفظ المستند المحدث.
---

تُستخدم التعليقات التوضيحية المربعة بشكل شائع لتسليط الضوء على مجالات الاهتمام أو تحديد الأقسام المهمة أو تقديم إشارات مرئية في مستند PDF. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك إنشاء تعليقات توضيحية مربعة (أو دائرية) من خلال تحديد المستطيل المحيط ونص المحتوى ولون الحدود وخيار التعبئة ورقم الصفحة وعرض الحدود.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط ملف PDF المدخل.
1. حدد التعليق التوضيحي للمربع.
1. أضف التعليق التوضيحي للمربع.
1. احفظ المستند المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_square_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create SquareAnnotation object
    rect = apd.Rectangle(100, 300, 200, 400)
    contents = "This is square annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, True, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
