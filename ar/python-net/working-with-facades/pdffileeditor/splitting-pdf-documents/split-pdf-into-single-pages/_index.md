---
title: تقسيم PDF إلى صفحات مفردة
linktitle: تقسيم PDF إلى صفحات مفردة
type: docs
weight: 30
url: /ar/python-net/split-pdf-into-single-pages/
description: قم بتقسيم مستند PDF إلى ملفات PDF ذات صفحة واحدة باستخدام Aspose.PDF لبيثون.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتقسيم ملف PDF إلى صفحات فردية في Python
Abstract: تعرف على كيفية تقسيم مستند PDF إلى ملفات PDF ذات صفحة واحدة باستخدام Aspose.PDF لـ Python. تقوم هذه الطريقة باستخراج كل صفحة من ملف PDF الأصلي وحفظها كملف منفصل لإدارة المستندات ومعالجتها بشكل مرن.
---

يعد تقسيم PDF إلى صفحات مفردة مفيدًا للمعالجة على مستوى الصفحة أو الطباعة أو توزيع أقسام المستند بشكل فردي. باستخدام Aspose.PDF لبيثون، فإن طريقة «split_to_pages» الخاصة بـ [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) يقوم الفصل بإنشاء ملفات PDF منفصلة لكل صفحة في المستند المصدر. يسمح هذا الأسلوب بالاستخراج الآلي للصفحات للأرشفة أو المراجعة أو المشاركة الفردية مع الحفاظ على التخطيط الأصلي والمحتوى.

1. قم بإنشاء كائن محرر ملفات PDF.
1. قم بتقسيم PDF إلى صفحات فردية.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Split PDF into Single Pages
def split_pdf_into_single_pages(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_pages(input_pdf_path, output_pdf_path)
```
