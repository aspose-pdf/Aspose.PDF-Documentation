---
title: إلحاق الصفحات بـ PDF
linktitle: إلحاق الصفحات بـ PDF
type: docs
weight: 10
url: /ar/python-net/append-pages-to-pdf/
description: قم بإلحاق صفحات من مستند PDF إلى آخر باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إلحاق صفحات من ملف PDF إلى آخر في Python
Abstract: تعرف على كيفية إلحاق صفحات من مستند PDF إلى آخر باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية استخدام فئة PDFfileEditor لدمج الصفحات من ملفات PDF متعددة وإنشاء مستند إخراج واحد.
---

يعد دمج الصفحات من مستندات PDF المختلفة مطلبًا شائعًا في عمليات سير عمل معالجة المستندات. باستخدام Aspose.PDF لـ Python، يمكن للمطورين بسهولة إلحاق صفحات من ملف PDF واحد أو أكثر إلى مستند موجود.

يوضح مقتطف الشفرة هذا كيفية استخدام طريقة الإلحاق الخاصة بـ [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) فئة لإضافة صفحات محددة من ملف PDF آخر إلى نهاية PDF المصدر. من خلال تحديد نطاق الصفحات، يمكن للمطورين التحكم بالضبط في الصفحات المضمنة في المستند النهائي.

1. قم بإنشاء كائن محرر ملفات PDF.
1. قم بإلحاق صفحات من ملف PDF آخر.

يتم إلحاق الصفحات المحددة من وثيقة PDF الثانوية بنهاية PDF الأصلي، مما يؤدي إلى إنشاء ملف إخراج مدمج.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Append Pages to PDF
def append_pages_to_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Append pages from the specified PDF document to the end of the source PDF document
    pdf_editor.append(infile, [sample_file], 1, 2, outfile)
```
