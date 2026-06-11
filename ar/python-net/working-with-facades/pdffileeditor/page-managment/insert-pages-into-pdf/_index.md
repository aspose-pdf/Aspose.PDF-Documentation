---
title: إدراج صفحات في PDF
linktitle: إدراج صفحات في PDF
type: docs
weight: 40
url: /ar/python-net/insert-pages-into-pdf/
description: أدخل صفحات من ملف PDF إلى آخر باستخدام Aspose.PDF لبيثون.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إدراج صفحات من ملف PDF آخر إلى ملف PDF موجود في Python
Abstract: تعرف على كيفية إدراج صفحات من ملف PDF إلى آخر باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية إضافة صفحات محددة من ملف PDF ثانوي إلى موضع معين من المستند الأصلي، وإنشاء ملف PDF مدمج مع وضع دقيق للصفحة.
---

يعد إدراج الصفحات في ملف PDF موجود مطلبًا شائعًا عند دمج المستندات أو إضافة المحتوى أو إعادة تنظيم التقارير. باستخدام Aspose.PDF لـ Python، يمكن للمطورين إدراج صفحات برمجيًا من ملف PDF إلى آخر في موقع محدد.

توضح هذه المقالة كيفية استخدام طريقة الإدراج الخاصة بـ [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) فئة. من خلال تحديد أرقام الصفحات لإدراجها والموقع المستهدف، يمكنك دمج المحتوى من ملفات PDF مختلفة مع الحفاظ على التنسيق والهيكل الأصليين.

1. قم بإنشاء كائن محرر ملفات PDF.
1. حدد موضع الإدراج والصفحات.
1. إدراج صفحات.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Insert Pages into PDF
def insert_pages_into_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page number where new pages will be inserted (1-based index)
    insert_page_number = 2

    pdf_editor.insert(infile, insert_page_number, sample_file, [1, 2], outfile)
```
