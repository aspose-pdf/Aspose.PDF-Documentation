---
title: تغيير حجم محتويات صفحة PDF
linktitle: تغيير حجم محتويات صفحة PDF
type: docs
weight: 30
url: /ar/python-net/resize-pdf-page-contents/
description: قم بتغيير حجم محتويات صفحات PDF محددة باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تغيير حجم محتويات صفحة PDF برمجيًا في Python
Abstract: تعرف على كيفية تغيير حجم محتويات صفحات PDF محددة باستخدام Aspose.PDF لـ Python. يوضح هذا المثال كيفية ضبط عرض محتوى الصفحة وارتفاعه مع الحفاظ على بنية المستند، مما يسهل تحسين التخطيطات للطباعة أو العرض.
---

غالبًا ما يكون ضبط حجم محتوى صفحة PDF ضروريًا عند إعداد المستندات للطباعة أو تركيب المحتوى في تخطيط معين أو توحيد تنسيقات الصفحات عبر المستند. باستخدام Aspose.PDF لـ Python، يمكن للمطورين تغيير حجم محتويات الصفحات المحددة برمجيًا دون تحرير المستند يدويًا.

توضح هذه المقالة كيفية استخدام طريقة «resize_contents» الخاصة بـ [محرر ملفات PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) فئة لتعديل أبعاد محتوى الصفحة لصفحات معينة في ملف PDF. من خلال تحديد العرض والارتفاع المستهدفين، يتم تغيير حجم المحتوى على الصفحات المحددة وفقًا لذلك.

1. قم بإنشاء كائن محرر ملفات PDF.
1. تغيير حجم محتويات الصفحة.

المعلمات:

- [1، 3] - قائمة أرقام الصفحات التي سيتم تغيير حجم محتوياتها.
- 400 - العرض الجديد لمحتوى الصفحة (بالنقاط).
- 750 - الارتفاع الجديد لمحتوى الصفحة (بالنقاط).

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Resize PDF Page Contents
def resize_pdf_page_contents(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    if not pdf_editor.resize_contents(
        FileIO(infile), FileIO(outfile, "w"), [1, 3], 400, 750
    ):
        raise Exception("Failed to resize PDF page contents.")
```
