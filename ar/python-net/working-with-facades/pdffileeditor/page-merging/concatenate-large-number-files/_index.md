---
title: قم بتوصيل عدد كبير من ملفات PDF
linktitle: قم بتوصيل عدد كبير من ملفات PDF
type: docs
weight: 10
url: /ar/python-net/concatenate-large-number-files/
description: ادمج عددًا كبيرًا من ملفات PDF بكفاءة باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتوصيل ملفات PDF الكبيرة في Python باستخدام التخزين المؤقت للقرص
Abstract: تعرف على كيفية دمج عدد كبير من ملفات PDF بكفاءة باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية تمكين التخزين المؤقت للقرص لمعالجة ملفات PDF الكبيرة دون استنفاد ذاكرة النظام، مما يضمن التسلسل السلس للعديد من الملفات.
---

عند العمل مع مجموعات كبيرة من ملفات PDF، يمكن أن يصبح استهلاك الذاكرة عقبة أثناء التسلسل. باستخدام Aspose.PDF لـ Python، يمكنك تمكين التخزين المؤقت للقرص في [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) فئة لدمج العديد من ملفات PDF بكفاءة. تجمع الطريقة المتسلسلة ملفات الإدخال في ملف PDF واحد بينما يمنع المخزن المؤقت للقرص استخدام الذاكرة العالية. يعد هذا الأسلوب مثاليًا لمعالجة المستندات المجمعة أو إنشاء التقارير تلقائيًا أو دمج أرشيفات PDF الكبيرة.

1. قم بإنشاء كائن محرر ملفات PDF.
1. دمج ملفات PDF متعددة.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_large_number_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.use_disk_buffer = True  # Enable disk buffering for large files
    pdf_editor.concatenate(files_to_merge, output_file)
```
