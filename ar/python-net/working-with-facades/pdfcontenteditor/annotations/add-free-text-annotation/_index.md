---
title: إضافة تعليقات توضيحية نصية مجانية
linktitle: إضافة تعليقات توضيحية نصية مجانية
type: docs
weight: 20
url: /ar/python-net/add-free-text-annotation/
description: يقوم هذا المثال بتحميل ملف PDF موجود، ويضيف تعليقًا نصيًا مجانيًا إلى الصفحة الأولى في موضع محدد، ويحفظ المستند المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف تعليقًا نصيًا مجانيًا إلى ملف PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية إدراج تعليق توضيحي نصي مجاني في مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية ربط ملف PDF وتحديد موضع التعليقات التوضيحية وإضافة نص مخصص وحفظ المستند المحدث.
---

تتيح لك التعليقات التوضيحية النصية المجانية وضع نص مرئي مباشرة على صفحة PDF دون الحاجة إلى تعليقات منبثقة. باستخدام PDFContentEditor، يمكنك تحديد مستطيل التعليق التوضيحي والنص المعروض والصفحة المستهدفة.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) كائن.
1. قم بربط ملف PDF المدخل.
1. حدد موضع التعليق التوضيحي.
1. أضف التعليق التوضيحي للنص المجاني.
1. احفظ المستند المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_free_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add free text annotation to page 1
    content_editor.create_free_text(
        apd.Rectangle(200, 480, 150, 25), "This is a free text annotation", 1
    )
    # Save updated document
    content_editor.save(outfile)
```
