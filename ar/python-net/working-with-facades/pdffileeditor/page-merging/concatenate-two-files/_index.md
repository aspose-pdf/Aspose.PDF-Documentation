---
title: قم بتوصيل ملفين من ملفات PDF
linktitle: قم بتوصيل ملفين من ملفات PDF
type: docs
weight: 60
url: /ar/python-net/concatenate-two-files/
description: قم بربط ملفي PDF في مستند واحد باستخدام Aspose.PDF لبيثون.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دمج ملفين PDF في ملف PDF واحد في Python
Abstract: تعرف على كيفية ربط ملفي PDF في مستند واحد باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية دمج ملفي PDF بسلاسة مع الحفاظ على المحتوى الأصلي والتنسيق.
---

يعد الجمع بين ملفي PDF مهمة شائعة عند دمج التقارير أو العقود أو النماذج. باستخدام Aspose.PDF لـ Python، يمكنك دمج ملفي PDF برمجيًا في مستند واحد باستخدام طريقة التسلسل الخاصة بـ [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) فئة. هذا يضمن تضمين جميع الصفحات من كلا الملفين في ملف PDF الناتج مع الحفاظ على التخطيط الأصلي والمحتوى والبنية.

1. قم بإنشاء كائن محرر ملفات PDF.
1. دمج ملفين PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge[0], files_to_merge[1], output_file)
```
