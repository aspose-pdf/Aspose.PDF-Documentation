---
title: احصل على نسخة PDF
linktitle: احصل على نسخة PDF
type: docs
weight: 20
url: /ar/python-net/get-pdf-version/
description: تعرف على كيفية تحديد إصدار مستند PDF برمجيًا باستخدام Aspose.PDF لـ Python. يوضح هذا البرنامج التعليمي كيفية استخدام فئة PDFfileInfo للتحقق من إصدار PDF للملف.
lastmod: "2026-06-11"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استرجع نسخة PDF باستخدام Aspose.PDF لبيثون
Abstract: تحتوي مستندات PDF على أرقام إصدارات تشير إلى الميزات والمواصفات التي تدعمها (على سبيل المثال، 1.4، 1.7، 2.0). تعد معرفة إصدار PDF أمرًا مهمًا للتوافق ودعم الميزات وسير عمل معالجة المستندات. في هذا الدليل، ستتعلم كيفية استرداد إصدار PDF برمجيًا باستخدام فئة PDFfileInfo في Aspose.PDF لـ Python.
---

تحدد إصدارات PDF الميزات والإمكانيات المدعومة في المستند، بما في ذلك حقول النموذج والتشفير والتعليقات التوضيحية والضغط. بالنسبة للمطورين الذين يعملون مع ملفات PDF متعددة، فإن التحقق من الإصدار يضمن التوافق مع الأدوات أو المكتبات أو عمليات سير العمل التي تعالج هذه الملفات.

باستخدام Aspose.PDF لـ Python، يمكنك بسهولة فحص إصدار PDF باستخدام [معلومات ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) فئة.

1. قم بتحميل مستند PDF.
1. استرجع نسخة PDF الخاصة بها.
1. اعرض الإصدار في وحدة التحكم.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_version(input_file_name):

    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)
    version = pdf_metadata.get_pdf_version()
    print(f"\nPDF Version: {version}")
```
