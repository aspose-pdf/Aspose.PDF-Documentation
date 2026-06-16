---
title: إضافة رابط محلي
linktitle: إضافة رابط محلي
type: docs
weight: 40
url: /ar/python-net/add-local-link/
description: يربط هذا المثال ملف PDF للإدخال، ويضيف رابطًا محليًا باللون الأحمر على الصفحة 1 يشير إلى الصفحة 1، ويحفظ المستند المعدل.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة رابط محلي إلى PDF باستخدام PDFContentEditor في بايثون
Abstract: يوضح هذا المثال كيفية إضافة رابط محلي إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية إنشاء منطقة قابلة للنقر تنتقل إلى صفحة أخرى داخل نفس ملف PDF وحفظ المستند المحدث.
---

تسمح الارتباطات المحلية في ملفات PDF بالتنقل السريع بين الصفحات داخل نفس المستند. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك تحديد مستطيل قابل للنقر يربط صفحة بأخرى، مما يحسن قابلية استخدام المستند والتنقل فيه.

1. قم بإنشاء مثيل محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. حدد مستطيلًا للارتباط المحلي القابل للنقر.
1. حدد صفحة المصدر وصفحة الوجهة.
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


def add_local_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a local link on page 1 to destination page 1
    content_editor.create_local_link(
        apd.Rectangle(120, 620, 220, 20),
        1,
        1,
        apd.Color.red,
    )
    # Save updated document
    content_editor.save(outfile)
```
