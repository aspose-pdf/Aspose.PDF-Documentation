---
title: استبدال صيغة النص
linktitle: استبدال صيغة النص
type: docs
weight: 30
url: /ar/python-net/replace-text-regex/
description: في هذا المثال، يتم استبدال جميع الأرقام المكونة من أربعة أرقام في المستند بالعنصر النائب «[NUMBER]». هذا مفيد لإخفاء البيانات الحساسة أو تطبيع المحتوى أو إخفاء هوية المستندات.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استبدال النص باستخدام التعبيرات العادية مع PDFContentEditor في Python
Abstract: يوضح هذا المثال كيفية استبدال النص في PDF باستخدام التعبيرات العادية مع Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية البحث عن الأنماط واستبدال جميع التطابقات عبر المستند.
---

تسمح التعبيرات العادية باستبدال النص المرن استنادًا إلى الأنماط بدلاً من السلاسل الثابتة. من خلال تمكين دعم regex في «replace_text_strategy»، يمكنك مطابقة المحتوى الديناميكي مثل الأرقام أو التواريخ أو السلاسل المنسقة.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) مثال.
1. قم بربط وثيقة PDF المدخلة.
1. قم بتكوين إستراتيجية الاستبدال لاستخدام regex.
1. استبدل الأنماط المطابقة عبر المستند بأكمله.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_regex(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace text in the whole document
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text_strategy.is_regular_expression_used = True
    content_editor.replace_text(r"\d{4}", "[NUMBER]")
    # Save updated document
    content_editor.save(outfile)
```
