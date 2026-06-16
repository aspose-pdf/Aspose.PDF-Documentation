---
title: استبدال النص على الصفحة
linktitle: استبدال النص على الصفحة
type: docs
weight: 10
url: /ar/python-net/replace-text-on-page/
description: في هذا المثال، يتم استبدال التكرار الأول لكلمة «PDF» بـ «نص تم استبدال الصفحة 1» باستخدام حجم خط محدد.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استبدال النص على صفحة معينة باستخدام PDFContentEditor في بايثون
Abstract: يوضح هذا المثال كيفية استبدال النص في مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية استبدال التكرار الأول للنص على الصفحة وحفظ المستند المحدث.
---

استبدال النص هو مطلب شائع عند تحديث مستندات PDF. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك البحث عن نص معين واستبداله بمحتوى جديد. تسمح لك خاصية «replace_text_strategy» بالتحكم في عدد التكرارات التي يتم استبدالها.

1. قم بإنشاء مثيل محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. قم بتكوين إستراتيجية استبدال النص.
1. استبدل النص الهدف.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text on page 1
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_FIRST
    )
    content_editor.replace_text("PDF", "Page 1 Replaced Text", 14)
    # Save updated document
    content_editor.save(outfile)
```
