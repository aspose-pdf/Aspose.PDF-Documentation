---
title: تقسيم ملف PDF إلى النهاية
linktitle: تقسيم ملف PDF إلى النهاية
type: docs
weight: 40
url: /ar/python-net/split-pdf-to-end/
description: قم بتقسيم مستند PDF من صفحة معينة إلى الصفحة الأخيرة باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتقسيم ملف PDF من صفحة محددة إلى النهاية في Python
Abstract: تعرف على كيفية تقسيم مستند PDF من صفحة معينة إلى الصفحة الأخيرة باستخدام Aspose.PDF لـ Python. يوضح هذا المثال استخراج جميع الصفحات بدءًا من صفحة محددة لإنشاء ملف PDF جديد.
---

يعد تقسيم PDF من صفحة معينة إلى النهاية مفيدًا عندما تحتاج إلى الجزء الأخير من المستند كملف منفصل. باستخدام Aspose.PDF لبيثون، فإن طريقة split_to_end الخاصة بـ [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) يسمح لك الفصل باستخراج الصفحات بدءًا من أي رقم صفحة إلى آخر صفحة من المستند. يعد هذا مثاليًا لإنشاء مقتطفات أو استخراج فصول أو معالجة أجزاء من ملف PDF كبير دون تحريره يدويًا.

1. قم بإنشاء كائن محرر ملفات PDF.
1. قم بتقسيم PDF من صفحة محددة إلى النهاية.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF to End
def split_pdf_to_end(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_end(input_pdf_path, 2, output_pdf_path)
```
