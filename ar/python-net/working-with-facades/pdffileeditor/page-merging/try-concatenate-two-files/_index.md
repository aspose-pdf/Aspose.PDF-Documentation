---
title: حاول ربط ملفين من ملفات PDF
linktitle: حاول ربط ملفين من ملفات PDF
type: docs
weight: 90
url: /ar/python-net/try-concatenate-two-files/
description: قم بربط ملفين من ملفات PDF باستخدام Aspose.PDF لبيثون.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دمج ملفي PDF بأمان في Python بدون استثناءات
Abstract: تعرف على كيفية ربط ملفي PDF بأمان باستخدام Aspose.PDF لـ Python. تقوم طريقة try_concatenate بدمج الملفات دون رفع الاستثناءات، مما يسمح بمعالجة الأخطاء بطريقة رشيقة في حالة فشل العملية.
---

قد يفشل دمج ملفي PDF أحيانًا بسبب تلف الملف أو التنسيقات غير المتوافقة أو مشكلات أخرى. باستخدام Aspose.PDF لبيثون، تسمح لك طريقة try_concatenate لفئة PDFfileEditor بمحاولة دمج ملفي PDF بأمان. في حالة فشل العملية، تقوم بإرجاع False بدلاً من رفع الاستثناء، مما يمنحك التحكم الكامل في معالجة الأخطاء في عمليات سير العمل التلقائية أو المعالجة المجمعة.

1. قم بإنشاء كائن محرر ملفات PDF.
1. محاولة دمج ملفين PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def try_concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(
        files_to_merge[0], files_to_merge[1], output_file
    ):
        print("Concatenation failed for the provided files.")
```
