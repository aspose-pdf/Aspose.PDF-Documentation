---
title: إضافة تعليق توضيحي على عربة التسوق
linktitle: إضافة تعليق توضيحي على عربة التسوق
type: docs
weight: 10
url: /ar/python-net/add-caret-annotation/
description: يقوم هذا المثال بتحميل ملف PDF موجود وإضافة تعليق توضيحي إلى الصفحة الأولى وحفظ المستند المعدل. يتضمن التعليق التوضيحي رمز علامة حمراء ونص تعليق وصفي.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة تعليق كاريت إلى ملف PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية إضافة تعليق توضيحي إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح النموذج كيفية ربط ملف PDF، وتحديد موضع التعليقات التوضيحية باستخدام المستطيلات، وتكوين خصائص علامة التبويب، وحفظ المستند المحدث.
---

تُستخدم التعليقات التوضيحية لـ Caret بشكل شائع للإشارة إلى إدراج النص أو التعليقات التحريرية في المستند. باستخدام PDFContentEditor، يمكنك إضافة التعليقات التوضيحية برمجيًا عن طريق تحديد رقم الصفحة وحدود التعليقات التوضيحية ومنطقة الشرح والرمز ونص الملاحظة واللون.

1. قم بإنشاء [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) كائن.
1. قم بربط ملف PDF المدخل.
1. تعريف معاملات التعليق التوضيحي لـ Caret:
  - رقم الصفحة حيث سيتم إضافة التعليق التوضيحي
  - مستطيل Caret (موضع التعليق التوضيحي)
  - مستطيل الشرح (منطقة النص)
  - الرمز (على سبيل المثال «P»)
  - نص التعليق التوضيحي
  - لون التعليق التوضيحي
1. أضف التعليق التوضيحي لـ Caret.
1. احفظ المستند المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_caret_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add caret annotation to page 1
    content_editor.create_caret(
        1,
        apd.Rectangle(350, 400, 10, 10),
        apd.Rectangle(300, 380, 115, 15),
        "P",
        "This is a caret annotation",
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
