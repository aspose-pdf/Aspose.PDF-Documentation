---
title: إزالة الإجراء المفتوح
linktitle: إزالة الإجراء المفتوح
type: docs
weight: 30
url: /ar/python-net/remove-open-action/
description: يقوم هذا المثال بتحميل ملف PDF موجود، ويزيل الإجراء المفتوح، ويحفظ المستند الذي تم تنظيفه.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة إجراء فتح المستند من PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية إزالة إجراء فتح مستند من PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية ربط PDF ومسح الإجراء المفتوح وحفظ المستند المحدث.
---

قد تحتوي مستندات PDF على إجراءات يتم تنفيذها تلقائيًا عند فتح الملف، مثل تنبيهات JavaScript أو أوامر التنقل أو السلوكيات الأخرى. في بعض السيناريوهات، قد تحتاج إلى إزالة هذه الإجراءات لأسباب تتعلق بالأمان أو الامتثال أو تجربة المستخدم.

باستخدام PDFContentEditor، يمكنك بسهولة إزالة إجراء فتح المستند والتأكد من فتح ملف PDF دون تنفيذ أي سلوك تلقائي.

1. قم بإنشاء كائن محرر محتوى PDF.
1. قم بربط ملف PDF المدخل.
1. قم بإزالة إجراء فتح المستند.
1. احفظ المستند المحدث.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_open_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove open action from the document
    content_editor.remove_document_open_action()
    # Save updated document
    content_editor.save(outfile)
```
