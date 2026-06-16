---
title: احذف جميع الصور من PDF
linktitle: احذف جميع الصور من PDF
type: docs
weight: 10
url: /ar/python-net/delete-all-images/
description: احذف جميع الصور من مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإزالة جميع الصور من ملف PDF باستخدام محرر محتوى PDFفي Python
Abstract: يوضح هذا المثال كيفية حذف جميع الصور من مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية ربط ملف PDF وإزالة جميع الصور المضمنة وحفظ المستند المحدث.
---

غالبًا ما تحتوي مستندات PDF على صور للرسوم التوضيحية أو العلامات التجارية أو الزخرفة. قد تكون هناك حالات تحتاج فيها إلى إزالة جميع الصور من PDF، مثل تقليل حجم الملف أو حماية المرئيات الحساسة أو إعداد نسخة نصية فقط.

استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك إزالة جميع الصور من PDF برمجيًا، مع ضمان احتواء المستند على محتوى نصي فقط. يقوم هذا المثال بربط ملف PDF للإدخال وحذف جميع الصور وحفظ الملف المعدل.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط ملف PDF المدخل.
1. احذف جميع الصور.
1. احفظ المستند المحدث.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_all_image(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete all images from the document
    content_editor.delete_image()
    # Save updated document
    content_editor.save(outfile)
```
