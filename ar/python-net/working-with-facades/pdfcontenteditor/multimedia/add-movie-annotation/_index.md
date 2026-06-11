---
title: إضافة تعليق توضيحي للفيلم
linktitle: إضافة تعليق توضيحي للفيلم
type: docs
weight: 10
url: /ar/python-net/add-movie-annotation/
description: يربط هذا المثال ملف PDF مُدخل، ويضيف تعليقًا توضيحيًا للفيلم على الصفحة 1، ويحفظ ملف PDF المحدث.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف تعليقًا توضيحيًا للفيلم إلى ملف PDF باستخدام محرر محتوى PDFفي Python
Abstract: يوضح هذا المثال كيفية تضمين فيلم (فيديو) في مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية إضافة تعليق توضيحي قابل للنقر يقوم بتشغيل مقطع فيديو مباشرة داخل PDF.
---

تتيح لك التعليقات التوضيحية للأفلام في ملفات PDF تضمين محتوى الوسائط المتعددة، مثل مقاطع الفيديو، في مستنداتك. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك تحديد مستطيل على الصفحة التي سيظهر فيها الفيديو. عند النقر، يمكن تشغيل الفيديو مباشرة من ملف PDF، مما يجعل مستنداتك أكثر تفاعلية وجاذبية.

1. قم بإنشاء مثيل محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. حدد مستطيلًا للتعليق التوضيحي للفيلم.
1. حدد ملف الفيديو لتضمينه.
1. قم بتعيين رقم الصفحة للتعليق التوضيحي.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_movie_annotation(infile, movie_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add movie annotation to page 1
    content_editor.create_movie(apd.Rectangle(80, 500, 220, 120), movie_file, 1)
    # Save updated document
    content_editor.save(outfile)
```
