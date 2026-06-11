---
title: تعيين بيانات PDF الأولية
linktitle: تعيين بيانات PDF الأولية
type: docs
weight: 50
url: /ar/python-net/set-pdf-metadata/
description: قم بتعديل وحفظ البيانات الوصفية في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحديث بيانات PDF الوصفية باستخدام Aspose.PDF لبيثون
Abstract: يشرح هذا الدليل كيفية تعديل البيانات الوصفية وحفظها في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية تحديث خصائص PDF القياسية مثل العنوان والموضوع والكلمات الرئيسية والمنشئ، بالإضافة إلى حقول البيانات الوصفية المخصصة. في النهاية، ستتمكن من تحديث بيانات PDF الوصفية برمجيًا وحفظ التغييرات.
---

يمكن أن تحتوي مستندات PDF على بيانات التعريف القياسية (العنوان، الموضوع، الكلمات الرئيسية، المنشئ، المؤلف) والبيانات الوصفية المخصصة المخزنة كخصائص XMP. يوفر Aspose.PDF واجهة برمجة تطبيقات بسيطة لتعديل هذه الخصائص في Python. يغطي هذا الدليل كيفية تحديث هذه الحقول وحفظ ملف PDF المعدل باستخدام [معلومات ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) فئة.

1. قم بتحميل ملف PDF.
1. قم بتحديث البيانات الوصفية القياسية.
1. إضافة بيانات تعريف مخصصة أو تحديثها.
1. احفظ البيانات الوصفية المحدثة.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    pdf_info.set_meta_info("CustomKey", "CustomValue")

    # pdf_info.save_new_info(outfile)
    # Is obsolete, use save() method instead

    # Save updated metadata
    pdf_info.save(outfile)
```
