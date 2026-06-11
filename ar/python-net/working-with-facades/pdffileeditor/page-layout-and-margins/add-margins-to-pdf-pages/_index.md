---
title: إضافة هوامش إلى صفحات PDF
linktitle: إضافة هوامش إلى صفحات PDF
type: docs
weight: 10
url: /ar/python-net/add-margins-to-pdf-pages/
description: أضف هوامش مخصصة لصفحات محددة من PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة هوامش مخصصة لصفحات PDF محددة في Python
Abstract: تعرف على كيفية إضافة هوامش مخصصة إلى صفحات محددة من PDF باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية توسيع حدود الصفحات من خلال تحديد الهوامش العلوية والسفلية واليسرى واليمنى للصفحات الفردية، مما يجعل ملفات PDF أكثر قابلية للطباعة أو متسقة بصريًا.
---

يمكن أن تؤدي إضافة هوامش إلى صفحات PDF إلى تحسين قابلية القراءة أو إعداد المستندات للطباعة أو تخصيص مساحة للتعليقات التوضيحية. باستخدام Aspose.PDF لـ Python، يمكن للمطورين إضافة هوامش برمجيًا إلى صفحات معينة من PDF دون تعديل تخطيط المحتوى.

في مقتطف الشفرة هذا، [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) يتم استخدام الفئة لإضافة هوامش 0.5 بوصة إلى الصفحتين 1 و 3 من مستند الإدخال. يتم تحديد الهوامش بالنقاط (بوصة واحدة = 72 نقطة) ويتم تطبيقها بشكل فردي على اليسار واليمين وأعلى وأسفل كل صفحة.

1. افتح مستند PDF المصدر.
1. قم بإنشاء مثيل «محرر ملفات PDF».
1. حدد الهوامش والصفحات التي تريد تعديلها.
1. قم بتطبيق الهوامش باستخدام طريقة «add_margines».
1. احفظ ملف PDF المحدث في ملف الإخراج.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Margins to PDF Pages
def add_margins_to_pdf_pages(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Define the margins to be added (in points)
    left_margin = 36  # 0.5 inch
    right_margin = 36  # 0.5 inch
    top_margin = 36  # 0.5 inch
    bottom_margin = 36  # 0.5 inch

    pdf_editor.add_margins(
        infile, outfile, [1, 3], left_margin, right_margin, top_margin, bottom_margin
    )
```
