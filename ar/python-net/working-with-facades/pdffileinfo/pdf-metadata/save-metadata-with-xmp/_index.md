---
title: حفظ البيانات الوصفية باستخدام XMP
linktitle: حفظ البيانات الوصفية باستخدام XMP
type: docs
weight: 30
url: /ar/python-net/save-metadata-with-xmp/
description: احفظ بيانات PDF الوصفية باستخدام XMP مع Aspose.PDF لبيثون عبر.NET
lastmod: "2026-06-11"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حفظ بيانات PDF الأولية باستخدام XMP باستخدام Aspose.PDF لبيثون
Abstract: يوضح هذا الدليل كيفية حفظ بيانات PDF الوصفية باستخدام XMP (منصة البيانات الوصفية القابلة للتوسيع) مع Aspose.PDF لـ Python عبر .NET. تضمن XMP تضمين البيانات الوصفية القياسية والمخصصة في تنسيق XML قياسي داخل PDF، مما يحسن التوافق عبر التطبيقات وعمليات سير العمل.
---

يمكن تخزين بيانات PDF الأولية بطرق متعددة، و XMP هي الطريقة الحديثة والموحدة لتضمين البيانات الوصفية داخل ملف PDF. باستخدام Aspose.PDF، يمكنك تحديث الحقول القياسية مثل العنوان والموضوع والكلمات الرئيسية والمنشئ، ثم حفظها بتنسيق XMP لضمان التوافق على نطاق أوسع والتحقق من المستقبل. يوصى بهذه الطريقة بدلاً من طرق تخزين البيانات الوصفية القديمة.

1. قم بتحميل ملف PDF.
1. قم بتعيين حقول بيانات التعريف القياسية.
1. احفظ البيانات الوصفية بصيغة XMP.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def save_info_with_xmp(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    # Save updated metadata
    pdf_info.save_new_info_with_xmp(outfile)
```
