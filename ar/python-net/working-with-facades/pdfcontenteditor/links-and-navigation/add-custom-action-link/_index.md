---
title: إضافة رابط إجراء مخصص
linktitle: إضافة رابط إجراء مخصص
type: docs
weight: 20
url: /ar/python-net/add-custom-action-link/
description: يقوم هذا المثال بربط ملف PDF للإدخال وإضافة رابط إجراء مخصص في الصفحة الأولى وحفظ المستند المعدل. يتم استخدام قائمة الإجراءات الفارغة من أجل البساطة، ولكن يمكن أن تتضمن التطبيقات الحقيقية إجراءات فعلية.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة رابط إجراء مخصص إلى PDF باستخدام PDFContentEditor في Python
Abstract: يوضح هذا المثال كيفية إضافة رابط إجراء مخصص إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية إنشاء منطقة قابلة للنقر على الصفحة وتعيين إجراء مخصص وحفظ المستند المحدث.
---

تسمح لك روابط الإجراءات المخصصة بتحديد مناطق تفاعلية في PDF يمكنها تشغيل إجراءات محددة عند النقر عليها، مثل تنفيذ البرامج النصية أو التنقل بين الصفحات أو تشغيل الأوامر الخاصة بالتطبيق. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك إنشاء رابط إجراء مخصص من خلال تحديد الصفحة والمستطيل واللون والإجراءات.

1. قم بإنشاء مثيل محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. حدد مستطيلًا للارتباط القابل للنقر.
1. حدد رقم الصفحة ولون الرابط.
1. قم بتعيين إجراءات مخصصة (فارغة في هذا المثال).
1. احفظ مستند PDF المحدث.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_custom_action_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add custom action link. Empty action list keeps the sample runnable
    # without requiring additional enum lookups.
    content_editor.create_custom_action_link(
        apd.Rectangle(200, 500, 260, 20),
        1,
        apd.Color.dark_red,
        [],
    )
    # Save updated document
    content_editor.save(outfile)
```
