---
title: استبدال النص على الصفحة بالحالة
linktitle: استبدال النص على الصفحة بالحالة
type: docs
weight: 20
url: /ar/python-net/replace-text-on-page-with-state/
description: في هذا المثال، يتم استبدال جميع تكرارات كلمة «software» في الصفحة 1 بـ «SOFTWARE PAGE 1"، باستخدام نص أحمر بحجم خط 12.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استبدال النص بتنسيق مخصص على صفحة معينة باستخدام PDFContentEditor في Python
Abstract: يوضح هذا المثال كيفية استبدال النص على صفحة معينة في PDF أثناء تطبيق التنسيق المخصص باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية التحكم في حجم الخط واللون أثناء استبدال النص.
---

في بعض الأحيان، يتطلب استبدال النص في PDF أيضًا تغييرات التنسيق مثل اللون أو حجم الخط. باستخدام TextState، يمكنك تحديد خصائص التصميم وتطبيقها أثناء الاستبدال. يتيح لك ذلك تمييز النص المعدل أو فرض تنسيق متسق عبر المستندات.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) مثال.
1. قم بربط وثيقة PDF المدخلة.
1. حدد TextState بتنسيق مخصص.
1. قم بتكوين استراتيجية الاستبدال.
1. استبدل النص في صفحة معينة.
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_text_on_page_with_state(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.red
    text_state.font_size = 12

    # Replace text on a specific page with explicit text formatting
    content_editor.replace_text_strategy.replace_scope = (
        pdf_facades.ReplaceTextStrategy.Scope.REPLACE_ALL
    )
    content_editor.replace_text("software", 1, "SOFTWARE PAGE 1", text_state)
    # Save updated document
    content_editor.save(outfile)
```
