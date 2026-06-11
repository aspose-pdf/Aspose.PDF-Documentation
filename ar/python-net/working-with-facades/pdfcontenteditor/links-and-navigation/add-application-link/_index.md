---
title: إضافة رابط تطبيق
linktitle: إضافة رابط تطبيق
type: docs
weight: 10
url: /ar/python-net/add-application-link/
description: يقوم هذا المثال بربط ملف PDF للإدخال وإضافة رابط تشغيل التطبيق على الصفحة الأولى وحفظ المستند المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة رابط تشغيل التطبيق إلى PDF باستخدام PDFContentEditor في Python
Abstract: يوضح هذا المثال كيفية إضافة رابط تشغيل التطبيق إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية إنشاء منطقة قابلة للنقر تفتح تطبيقًا محددًا عند النقر عليها، وحفظ ملف PDF المحدث.
---

يمكن أن يتضمن PDF عناصر تفاعلية مثل الروابط التي تطلق تطبيقات خارجية. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك تحديد منطقة مستطيلة على صفحة تفتح، عند النقر عليها، ملفًا محددًا قابلاً للتنفيذ.

1. قم بإنشاء مثيل محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. حدد منطقة مستطيل للارتباط القابل للنقر.
1. حدد مسار التطبيق لبدء التشغيل.
1. قم بتعيين لون الارتباط.
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


def add_application_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add application launch link
    content_editor.create_application_link(
        apd.Rectangle(180, 530, 260, 20),
        "notepad.exe",
        1,
        apd.Color.purple,
    )
    # Save updated document
    content_editor.save(outfile)
```
