---
title: إجراء إضافة مستند
linktitle: إجراء إضافة مستند
type: docs
weight: 20
url: /ar/python-net/add-document-action/
description: يضيف هذا المثال تنبيه JavaScript يظهر عند فتح PDF. يتم إرفاق البرنامج النصي بحدث فتح المستند ويتم تنفيذه تلقائيًا في برامج عرض PDF المدعومة.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة مستند افتح إجراء جافا سكريبت إلى ملف PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية إضافة إجراء JavaScript على مستوى المستند يتم تشغيله عند فتح PDF. باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات، يوضح النموذج كيفية ربط مستند وتعيين إجراء حدث مفتوح وحفظ ملف PDF المحدث.
---

تسمح لك الإجراءات على مستوى المستند بتحديد السلوكيات التي يتم تنفيذها تلقائيًا عند حدوث أحداث معينة، مثل فتح PDF. مع [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك إرفاق شفرة جافا سكريبت بهذه الأحداث. يمكن استخدام هذا للإشعارات أو منطق التحقق أو عمليات سير العمل التفاعلية.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط ملف PDF المدخل.
1. إضافة إجراء على مستوى المستند.
1. احفظ المستند المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_document_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add JavaScript action for document open event
    content_editor.add_document_additional_action(
        content_editor.DOCUMENT_OPEN,
        "app.alert('Document opened with PdfContentEditor action');",
    )
    # Save updated document
    content_editor.save(outfile)
```
