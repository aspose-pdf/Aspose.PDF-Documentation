---
title: تقسيم ملف PDF من البداية
linktitle: تقسيم ملف PDF من البداية
type: docs
weight: 10
url: /ar/python-net/split-pdf-from-beginning/
description: قم بتقسيم مستند PDF من البداية باستخدام Aspose.PDF لبيثون.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تقسيم ملف PDF من البداية في بايثون باستخدام Aspose.PDF
Abstract: تعرف على كيفية تقسيم مستند PDF من البداية باستخدام Aspose.PDF لـ Python. يوضح هذا المثال استخراج عدد معين من الصفحات بدءًا من الصفحة الأولى لإنشاء مستند PDF جديد.
---

يعد تقسيم ملفات PDF من البداية مفيدًا عندما تحتاج إلى الصفحات القليلة الأولى من المستند كملف منفصل. باستخدام Aspose.PDF لبيثون، طريقة split_from_first في [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) يسمح لك الفصل باستخراج عدد محدد من الصفحات بدءًا من الصفحة الأولى. هذه الميزة مثالية لإنشاء مقتطفات أو معاينات أو أقسام أصغر من ملف PDF أكبر بدون تحرير الملف الأصلي يدويًا.

1. قم بإنشاء كائن محرر ملفات PDF.
1. قم بتقسيم ملف PDF من الصفحة الأولى.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF from Beginning
def split_pdf_from_beginning(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_from_first(input_pdf_path, 3, output_pdf_path)
```
