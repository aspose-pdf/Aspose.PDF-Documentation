---
title: احصل على بيانات PDF الوصفية
linktitle: احصل على بيانات PDF الوصفية
type: docs
weight: 20
url: /ar/python-net/get-pdf-metadata/
description: قم باستخراج البيانات الوصفية وعرضها من مستندات PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استرداد بيانات PDF الوصفية باستخدام Aspose.PDF لبيثون.
Abstract: يوضح هذا الدليل كيفية استخراج البيانات الوصفية وعرضها من مستندات PDF باستخدام Aspose.PDF لـ Python. سوف تتعلم الوصول إلى خصائص PDF القياسية مثل العنوان والمؤلف والكلمات الرئيسية وتواريخ الإنشاء/التعديل، بالإضافة إلى حقول البيانات الوصفية المخصصة. بالإضافة إلى ذلك، يغطي الدليل عمليات التحقق من صلاحية PDF والتشفير وحالة المحفظة.
---

غالبًا ما تحتوي مستندات PDF على بيانات تعريف قيمة تصف محتوى المستند والتأليف والأذونات. يوفر Aspose.PDF واجهة برمجة تطبيقات ملائمة لاسترداد خصائص البيانات الوصفية القياسية والمخصصة. مقتطف الشفرة هذا: كيفية استخدام [معلومات ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) فئة لفحص ملفات PDF برمجيًا، بما في ذلك أمثلة خطوة بخطوة في Python.

1. قم بتحميل ملف PDF.
1. استرجع البيانات الوصفية القياسية.
1. تحقق من حالة PDF والأمان.
1. استرجع البيانات الوصفية المخصصة.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_metadata(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    print(f"Subject: {pdf_info.subject}")
    print(f"Title: {pdf_info.title}")
    print(f"Keywords: {pdf_info.keywords}")
    print(f"Creator: {pdf_info.creator}")
    print(f"Creation Date: {pdf_info.creation_date}")
    print(f"Modification Date: {pdf_info.mod_date}")

    # Check PDF status
    print(f"Is Valid PDF: {pdf_info.is_pdf_file}")
    print(f"Is Encrypted: {pdf_info.is_encrypted}")
    print(f"Has Open Password: {pdf_info.has_open_password}")
    print(f"Has Edit Password: {pdf_info.has_edit_password}")
    print(f"Is Portfolio: {pdf_info.has_collection}")

    # Retrieve and display a specific custom attribute
    reviewer = pdf_info.get_meta_info("Reviewer")
    print(f"Reviewer: {reviewer if reviewer else 'No Reviewer metadata found.'}")
```
