---
title: إضافة تعليق صوتي
linktitle: إضافة تعليق صوتي
type: docs
weight: 20
url: /ar/python-net/add-sound-annotation/
description: يقوم هذا المثال بربط ملف PDF للإدخال وإضافة تعليق توضيحي صوتي على الصفحة 1 وحفظ ملف PDF المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف تعليقًا صوتيًا إلى ملف PDF باستخدام PDFContentEditor في Python
Abstract: يوضح هذا المثال كيفية تضمين الصوت في مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية إضافة تعليق توضيحي صوتي قابل للنقر يقوم بتشغيل ملف صوتي مباشرة داخل PDF.
---

تتيح لك التعليقات الصوتية في ملفات PDF إضافة محتوى صوتي مثل الملاحظات الصوتية أو الموسيقى أو المؤثرات الصوتية إلى مستنداتك. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك تحديد مستطيل صغير قابل للنقر على صفحة تقوم بتشغيل ملف صوتي محدد عند تنشيطه.

1. قم بإنشاء مثيل محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. حدد مستطيلًا للتعليق الصوتي.
1. حدد الملف الصوتي واسم التعليق التوضيحي ورقم الصفحة ومعدل أخذ العينات.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_sound_annotation(infile, sound_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add sound annotation to page 1
    content_editor.create_sound(
        apd.Rectangle(80, 450, 30, 30), sound_file, "Speaker", 1, "8000"
    )
    # Save updated document
    content_editor.save(outfile)
```
