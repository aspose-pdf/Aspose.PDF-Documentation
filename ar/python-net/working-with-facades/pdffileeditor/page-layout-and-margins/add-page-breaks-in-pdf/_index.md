---
title: إضافة فواصل الصفحات في PDF
linktitle: إضافة فواصل الصفحات في PDF
type: docs
weight: 20
url: /ar/python-net/add-page-breaks-in-pdf/
description: إدراج فواصل الصفحات في وثيقة PDF باستخدام Aspose.PDF لبيثون.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة فواصل الصفحات إلى صفحات PDF برمجيًا في Python
Abstract: تعرف على كيفية إدراج فواصل الصفحات في مستند PDF باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية تقسيم صفحة في موضع عمودي محدد، مما يسمح للمطورين بإعادة تنظيم المحتوى وإنشاء صفحات إضافية بشكل ديناميكي.
---

تعد فواصل الصفحات مفيدة عندما تحتاج إلى تقسيم صفحات PDF الطويلة إلى صفحات متعددة أو التحكم في كيفية توزيع المحتوى عبر المستند. باستخدام Aspose.PDF لـ Python، يمكن للمطورين إدراج فواصل صفحات في مواضع محددة دون تحرير PDF يدويًا.

توضح هذه المقالة كيفية استخدام طريقة «add_page_break» الخاصة بـ [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) فئة لإدراج فاصل صفحات بإحداثيات رأسية محددة على صفحة محددة. تقوم الطريقة بإنشاء صفحة جديدة ونقل المحتوى أسفل نقطة الفاصل إلى تلك الصفحة.

1. قم بإنشاء كائن محرر ملفات PDF.
1. حدد موضع فاصل الصفحات.
1. أدخل فاصل الصفحات.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add Page Breaks in PDF
def add_page_breaks_in_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.add_page_break(
        infile,
        outfile,
        [
            pdf_facades.PdfFileEditor.PageBreak(1, 400),
        ],
    )
```
