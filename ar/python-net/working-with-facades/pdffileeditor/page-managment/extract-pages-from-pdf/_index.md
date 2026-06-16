---
title: استخراج صفحات من PDF
linktitle: استخراج صفحات من PDF
type: docs
weight: 30
url: /ar/python-net/extract-pages-from-pdf/
description: استخرج الصفحات المحددة من مستند PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج صفحات محددة من وثيقة PDF في Python
Abstract: تعرف على كيفية استخراج الصفحات المحددة من مستند PDF باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية إنشاء PDF جديد يحتوي على الصفحات التي تحتاج إليها فقط، مما يتيح إنشاء مستند مخصص ومعالجة مستوى الصفحة.
---

يعد استخراج الصفحات من PDF مفيدًا عندما تحتاج إلى إنشاء مجموعة فرعية من المستند أو مشاركة محتوى محدد فقط أو إعادة تنظيم ملفات PDF للعروض التقديمية أو التقارير أو الطباعة. باستخدام Aspose.PDF لـ Python، يمكن للمطورين استخراج الصفحات برمجيًا من ملف PDF وحفظها كمستند جديد.

تعرف على كيفية استخدام طريقة الاستخراج الخاصة بـ [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) فئة. من خلال تحديد قائمة الصفحات لاستخراجها، يمكنك إنشاء ملف PDF جديد يحتوي فقط على الصفحات المحددة مع الحفاظ على المحتوى الأصلي والتنسيق.

1. قم بإنشاء كائن محرر ملفات PDF.
1. حدد الصفحات لاستخراجها.
1. استخرج الصفحات.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


# Extract Pages from PDF
def extract_pages_from_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page numbers to be extracted (1-based index)
    pages_to_extract = [1, 4, 3]

    # Extract the specified pages from the PDF document and save to a new PDF document
    pdf_editor.extract(infile, pages_to_extract, outfile)
```
