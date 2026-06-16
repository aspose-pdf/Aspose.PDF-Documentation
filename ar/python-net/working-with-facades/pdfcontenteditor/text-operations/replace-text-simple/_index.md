---
title: استبدال النص البسيط
linktitle: استبدال النص البسيط
type: docs
weight: 40
url: /ar/python-net/replace-text-simple/
description: في هذا المثال، يتم استبدال جميع تكرارات «33" بـ «XXXIII» في المستند بأكمله. يوضح هذا الاستبدال المباشر للسلسلة بدون تنسيق مخصص أو تعبير عادي.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استبدال النص عبر PDF باستخدام محرر محتوى PDFفي بايثون
Abstract: يوضح هذا المثال كيفية استبدال النص في مستند PDF بأكمله باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يستبدل جميع تكرارات سلسلة محددة بنص جديد.
---

يعد استبدال النص البسيط مفيدًا عند تحديث القيم المتكررة في المستند. مع [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك تحديد نطاق بديل ونص بديل عالميًا عبر جميع الصفحات.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) مثال.
1. قم بربط وثيقة PDF المدخلة.
1. قم بتكوين نطاق بديل لجميع التكرارات.
1. استبدل النص الهدف.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_simple(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("33", "XXXIII ")
    # Save updated document
    content_editor.save(outfile)
```
