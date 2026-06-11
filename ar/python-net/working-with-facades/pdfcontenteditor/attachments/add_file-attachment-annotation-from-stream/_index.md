---
title: إضافة تعليق توضيحي لمرفق الملف من Stream
linktitle: إضافة تعليق توضيحي لمرفق الملف من Stream
type: docs
weight: 40
url: /ar/python-net/add-file-attachment-annotation-from-stream/
description: يقوم المثال بتحميل ملف PDF، وقراءة ملف خارجي في دفق الذاكرة، وإضافة تعليق توضيحي لمرفق الملف إلى الصفحة الأولى، وحفظ المستند المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة التعليقات التوضيحية لمرفقات الملفات إلى PDF من بث في Python
Abstract: يوضح هذا المثال كيفية إنشاء تعليق توضيحي لمرفق الملف في ملف PDF باستخدام دفق الملفات باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية تحديد موضع التعليق التوضيحي وتعيين الوصف وتضمين قيمة العتامة وحفظ المستند المعدل.
---

تسمح التعليقات التوضيحية لمرفقات الملفات بتضمين الملفات كرموز تفاعلية داخل صفحة PDF. باستخدام الأسلوب القائم على التدفق، يمكنك إرفاق الملفات ديناميكيًا دون الاعتماد على مسار ملف فعلي. تدعم هذه الطريقة أيضًا تخصيص مظهر التعليق التوضيحي، بما في ذلك العتامة.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط ملف PDF المدخل.
1. اقرأ ملف المرفقات كتدفق.
1. أضف التعليق التوضيحي لمرفق الملف.
1. احفظ المستند المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_file_attachment_annotation_from_stream(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    with open(attachment_file, "rb") as source_stream:
        attachment_stream = BytesIO(source_stream.read())

    # Create file attachment annotation using stream+opacity overload
    content_editor.create_file_attachment(
        apd.Rectangle(130, 520, 20, 20),
        "Attachment annotation from stream",
        attachment_stream,
        path.basename(attachment_file),
        1,
        "Tag",
        0.75,
    )
    # Save updated document
    content_editor.save(outfile)
```
