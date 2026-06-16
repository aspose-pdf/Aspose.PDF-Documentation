---
title: قم بتسلسل ملفات PDF مع التحسين
linktitle: قم بتسلسل ملفات PDF مع التحسين
type: docs
weight: 30
url: /ar/python-net/concatenate-pdf-files-with-optimization/
description: قم بربط ملفات PDF متعددة في ملف PDF محسن واحد باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دمج ملفات PDF مع الإخراج المحسن في Python
Abstract: تعرف على كيفية ربط ملفات PDF متعددة في ملف PDF واحد محسن باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية تمكين تحسين الحجم لتقليل حجم ملف الإخراج مع الحفاظ على المحتوى والتنسيق.
---

عند دمج ملفات PDF متعددة، يمكن أن يصبح الملف الناتج كبيرًا، خاصة إذا كان يحتوي على صور أو محتوى معقد. باستخدام Aspose.PDF لـ Python، يمكن للمطورين تمكين التحسين أثناء التسلسل لتقليل حجم الملف دون فقدان الجودة. الخاصية optimize_size في [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) تضمن الفئة أن يكون ملف PDF المدمج مضغوطًا وفعالًا، مما يجعله مناسبًا للمشاركة أو التخزين أو الأرشفة.

1. قم بإنشاء كائن محرر ملفات PDF وتمكين التحسين.
1. دمج ملفات PDF.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def concatenate_pdf_files_with_optimization(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.optimize_size = True  # Enable optimization for smaller output file size
    pdf_editor.concatenate(files_to_merge, output_file)
```
