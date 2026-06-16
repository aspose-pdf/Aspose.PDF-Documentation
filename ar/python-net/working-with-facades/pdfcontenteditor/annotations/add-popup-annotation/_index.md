---
title: إضافة تعليقات توضيحية منبثقة
linktitle: إضافة تعليقات توضيحية منبثقة
type: docs
weight: 40
url: /ar/python-net/add-popup-annotation/
description: يقوم هذا المثال بتحميل ملف PDF وإضافة تعليق توضيحي منبثق إلى الصفحة الأولى وحفظ المستند المعدل. تم تعيين النافذة المنبثقة لتكون مرئية افتراضيًا وتعرض نص التعليق المحدد.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف التعليقات التوضيحية المنبثقة إلى PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية إدراج تعليق توضيحي منبثق في مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يشرح كيفية تحديد المنطقة المنبثقة وتعيين نص التعليق التوضيحي والتحكم في الرؤية وحفظ المستند المحدث.
---

التعليقات التوضيحية المنبثقة مفيدة لإضافة التعليقات أو التفسيرات أو الملاحظات التفاعلية في ملفات PDF. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك إنشاء تعليقات توضيحية منبثقة برمجيًا من خلال تحديد الموقع والمحتوى والرؤية ورقم الصفحة.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط ملف PDF المدخل.
1. حدد مستطيل التعليق التوضيحي المنبثق.
1. أضف التعليق التوضيحي المنبثق.
1. احفظ المستند المحدث.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_popup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add popup annotation to page 1
    content_editor.create_popup(
        apd.Rectangle(220, 520, 180, 80),
        "This is a popup annotation",
        True,
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
