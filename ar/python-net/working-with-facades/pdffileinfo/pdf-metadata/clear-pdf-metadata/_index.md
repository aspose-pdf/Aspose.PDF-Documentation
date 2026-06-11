---
title: مسح بيانات PDF الأولية
linktitle: مسح بيانات PDF الأولية
type: docs
weight: 10
url: /ar/python-net/clear-pdf-metadata/
description: قم بإزالة جميع البيانات الوصفية من مستند PDF باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: مسح بيانات PDF الوصفية باستخدام Aspose.PDF لبيثون
Abstract: يشرح هذا الدليل كيفية إزالة جميع البيانات الوصفية من مستند PDF باستخدام Aspose.PDF لـ Python عبر .NET. سوف تتعلم مسح حقول البيانات الوصفية القياسية والمخصصة وحفظ ملف PDF المعقم. هذا مفيد للخصوصية أو الأمان أو إعداد ملفات PDF للإصدار العام.
---

غالبًا ما يحتوي PDF على بيانات وصفية مثل العنوان والمؤلف والكلمات الرئيسية وتواريخ الإنشاء والحقول المخصصة. في بعض السيناريوهات، قد ترغب في إزالة جميع البيانات الوصفية من PDF، على سبيل المثال قبل التوزيع أو الأرشفة. يوفر Aspose.PDF طريقة clear_info () لإزالة جميع البيانات الوصفية بسهولة. بعد المسح، يمكنك حفظ ملف PDF باستخدام طريقة save ().

1. قم بتحميل ملف PDF.
1. امسح جميع البيانات الوصفية.
1. احفظ ملف PDF النظيف.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def clear_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Clear PDF metadata
    pdf_info.clear_info()

    # Save updated metadata
    pdf_info.save(outfile)
```
