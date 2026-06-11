---
title: قم بتسلسل ملفات PDF متعددة
linktitle: قم بتسلسل ملفات PDF متعددة
type: docs
weight: 20
url: /ar/python-net/concatenate-pdf-files/
description: ادمج ملفات PDF متعددة في مستند واحد باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دمج ملفات PDF متعددة في ملف PDF واحد في Python
Abstract: تعرف على كيفية دمج ملفات PDF متعددة في مستند واحد باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية استخدام الطريقة المتسلسلة لدمج العديد من ملفات PDF بسلاسة مع الحفاظ على محتواها وتنسيقها.
---

يعد دمج ملفات PDF مهمة شائعة في إدارة المستندات وإعداد التقارير وسير العمل الآلي. باستخدام Aspose.PDF لـ Python، يمكن للمطورين بسهولة دمج ملفات PDF متعددة في مستند موحد واحد. الطريقة المتسلسلة لـ [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) تضمن الفئة الاحتفاظ بجميع الصفحات من ملفات الإدخال في الإخراج النهائي، مع الحفاظ على تخطيطها الأصلي ومحتواها. هذا الأسلوب مفيد لإنشاء تقارير شاملة أو دمج النماذج أو أرشفة مستندات متعددة بكفاءة.

1. قم بإنشاء كائن محرر ملفات PDF.
1. دمج ملفات PDF متعددة.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge, output_file)
```
