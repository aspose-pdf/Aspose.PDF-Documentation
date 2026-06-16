---
title: حذف الطابع حسب الفهرس
linktitle: حذف الطابع حسب الفهرس
type: docs
weight: 50
url: /ar/python-net/delete-stamp-by-index/
description: يقوم هذا المثال بإنشاء طابعين مطاطيين على الصفحة 2. بعد ذلك، يمكن حذف الطابع من خلال تحديد الفهرس الخاص به.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احذف ختمًا مطاطيًا حسب الفهرس في ملف PDF باستخدام PDFContentEditor في Python
Abstract: يوضح هذا المثال كيفية حذف تعليق توضيحي للختم المطاطي في ملف PDF باستخدام فهرسه مع Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية إضافة طوابع متعددة ثم حذف واحدة منها بناءً على ترتيبها على الصفحة.
---

عند وجود عدة أختام مطاطية على الصفحة، يمكنك حذف واحدة محددة باستخدام الفهرس الخاص بها. تسمح طريقة delete_stamp () بإزالة التعليقات التوضيحية وفقًا لتسلسلها، وهو أمر مفيد عندما لا تتعقب معرفات الطوابع ولكنك تعرف ترتيبها.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) مثال.
1. قم بربط وثيقة PDF المدخلة.
1. قم بربط ملف PDF المدخل بمثيل PDFContentEditor باستخدام bind_pdf (infile).
1. اتصل بـ 'delete_stamp (1، [2، 3]) 'لإزالة الطابع بالفهرس 1 من الصفحتين 2 و 3.
1. احفظ مستند PDF المعدل في ملف الإخراج باستخدام save (outfile).

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    content_editor.delete_stamp(1, [2, 3])
    # Save updated document
    content_editor.save(outfile)
```
