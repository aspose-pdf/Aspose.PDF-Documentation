---
title: استبدال الصور في PDF
linktitle: استبدال الصور في PDF
type: docs
weight: 30
url: /ar/python-net/replace-image/
description: يربط هذا المثال ملف PDF مُدخل، ويستبدل الصورة الأولى في الصفحة 1 بصورة جديدة، ويحفظ المستند المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استبدال صورة في PDF باستخدام PDFContentEditor في بايثون
Abstract: يوضح هذا المثال كيفية استبدال صورة موجودة في مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية استهداف صورة معينة على الصفحة واستبدالها بصورة جديدة، ثم حفظ ملف PDF المحدث.
---

غالبًا ما تحتوي ملفات PDF على صور قد تحتاج إلى تحديث أو استبدال، مثل الشعارات أو الرسوم التخطيطية أو الصور. مع [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك استبدال صورة معينة في صفحة معينة من خلال توفير رقم الصفحة وفهرس الصورة ومسار ملف الصورة الجديد.

1. قم بإنشاء مثيل محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. استبدل صورة معينة على صفحة معينة.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_image(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace image on page 1
    content_editor.replace_image(1, 1, image_file)
    # Save updated document
    content_editor.save(outfile)
```
