---
title: إضافة تعليقات توضيحية نصية
linktitle: إضافة تعليقات توضيحية نصية
type: docs
weight: 50
url: /ar/python-net/add-text-annotation/
description: أضف تعليقات توضيحية نصية إلى مستند PDF باستخدام فئة PDFContentEditor في Aspose.PDF لبيثون عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة تعليقات توضيحية نصية في Python
Abstract: تعرف على كيفية إضافة التعليقات التوضيحية النصية إلى مستند PDF باستخدام فئة PDFContentEditor في Aspose.PDF لـ Python عبر .NET. يوضح هذا المثال كيفية وضع تعليق توضيحي نصي في موضع معين، وتحديد عنوانه ومحتوياته، وحفظ ملف PDF المحدث.
---

توضح هذه المقالة كيفية إضافة تعليق توضيحي نصي إلى مستند PDF باستخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) الفصل الدراسي في Aspose.PDF.

تتيح لك التعليقات التوضيحية النصية إرفاق تعليقات أو ملاحظات أو معلومات إضافية بأجزاء معينة من صفحة PDF. يمكن أن تظهر هذه التعليقات التوضيحية كرموز ويتم توسيعها من قبل المستخدمين عند عرض المستند.

في هذا المثال:

- يتم تحميل وثيقة PDF في محرر محتوى PDF.
- تتم إضافة تعليق توضيحي نصي في موضع محدد على الصفحة.
- يتضمن التعليق التوضيحي العنوان والمحتوى ونوع الرمز وإعدادات الرؤية.
- يتم حفظ المستند المعدل إلى ملف جديد.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. حدد موضع التعليق التوضيحي.
1. إضافة تعليق توضيحي نصي.
1. احفظ ملف PDF المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add text annotation to page 1
    content_editor.create_text(
        apd.Rectangle(100, 400, 50, 50),
        "Text Annotation",
        "This is a text annotation",
        True,
        "Insert",
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
