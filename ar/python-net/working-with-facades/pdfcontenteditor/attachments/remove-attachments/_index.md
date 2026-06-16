---
title: إزالة المرفقات
linktitle: إزالة المرفقات
type: docs
weight: 50
url: /ar/python-net/remove-attachments/
description: يقوم هذا المثال بربط ملف PDF للإدخال وحذف جميع المرفقات وحفظ ملف PDF المعدل بدون أي ملفات مضمنة.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإزالة جميع المرفقات من ملف PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية إزالة جميع مرفقات الملفات من مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية ربط PDF وحذف المرفقات المضمنة وحفظ المستند المحدث.
---

قد تحتوي ملفات PDF على مرفقات مثل المستندات أو الصور أو الملفات الأخرى. هناك سيناريوهات تحتاج فيها إلى تنظيف ملف PDF من جميع المرفقات لأغراض الأمان أو الخصوصية أو التوزيع. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك إزالة جميع المرفقات المضمنة في المستند برمجيًا.

1. قم بإنشاء كائن محرر محتوى PDF. 
1. قم بربط ملف PDF المدخل.
1. احذف جميع المرفقات.
1. احفظ المستند المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_attachments(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove all attachments from document
    content_editor.delete_attachments()
    # Save updated document
    content_editor.save(outfile)
```
