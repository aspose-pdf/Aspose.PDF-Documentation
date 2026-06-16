---
title: استبدال النص بالحالة
linktitle: استبدال النص بالحالة
type: docs
weight: 50
url: /ar/python-net/replace-text-with-state/
description: في هذا المثال، يتم استبدال جميع تكرارات «البرنامج» بـ «SOFTWARE» وتنسيقها باللون الأزرق بحجم خط 14.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استبدال النص بالتنسيق المخصص في PDF باستخدام PDFContentEditor في Python
Abstract: يوضح هذا المثال كيفية استبدال النص في مستند PDF أثناء تطبيق التنسيق المخصص باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية التحكم في لون النص وحجم الخط أثناء الاستبدال.
---

عند تحديث النص في PDF، قد ترغب في إبراز المحتوى البديل. باستخدام كائن TextState، يمكنك تحديد التصميم مثل اللون وحجم الخط، ثم تطبيقه على كل النص الذي تم استبداله.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)  مثال.
1. قم بربط وثيقة PDF المدخلة.
1. حدد TextState بتنسيق مخصص.
1. قم بتكوين نطاق الاستبدال.
1. استبدل النص عبر المستند بأكمله.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 14

    # Replace text with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", "SOFTWARE", text_state)
    # Save updated document
    content_editor.save(outfile)
```
