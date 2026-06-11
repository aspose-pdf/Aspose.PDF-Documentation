---
title: حذف الصور من PDF
linktitle: حذف الصور من PDF
type: docs
weight: 20
url: /ar/python-net/delete-images/
description:
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حذف صور محددة من صفحة PDF باستخدام PDFContentEditor في بايثون
Abstract: يوضح هذا المثال كيفية حذف صور معينة من مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية استهداف الصور على صفحة معينة وحفظ المستند المحدث.
---

في بعض الأحيان، قد ترغب في إزالة صور معينة فقط من ملف PDF بدلاً من مسح جميع العناصر المرئية. مع [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك حذف الصور المحددة من خلال تحديد رقم الصفحة وفهرس الصور.

يقوم مقتطف الشفرة هذا بربط ملف PDF المُدخل، وحذف الصورة الثانية من الصفحة 1، وحفظ ملف PDF المعدل، مع ترك الصور الأخرى سليمة.

1. قم بإنشاء مثيل محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. احذف صورًا محددة من صفحة معينة.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_images(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete image on page 1
    content_editor.delete_image(1, [2])
    # Save updated document
    content_editor.save(outfile)
```
