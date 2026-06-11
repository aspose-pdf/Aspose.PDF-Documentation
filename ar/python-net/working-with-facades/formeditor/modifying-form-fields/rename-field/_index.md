---
title: إعادة تسمية الحقل
linktitle: إعادة تسمية الحقل
type: docs
weight: 70
url: /ar/python-net/rename-field/
description: أعد تسمية حقل نموذج موجود في مستند PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إعادة تسمية حقل نموذج PDF باستخدام Python
Abstract: يوضح هذا المثال كيفية إعادة تسمية حقل نموذج موجود في مستند PDF باستخدام Aspose.PDF لـ Python. يفتح الكود ملف PDF للإدخال، ويغير اسم حقل النموذج المحدد باستخدام فئة ForMeditor، ويحفظ المستند المحدث.
---

غالبًا ما تعتمد نماذج PDF على أسماء الحقول للبرمجة والأتمتة ومعالجة البيانات. باستخدام Aspose.PDF لـ Python، يمكن للمطورين إعادة تسمية الحقول الموجودة دون إعادة إنشائها أو تغيير تخطيط النموذج.

ال [المحرر السابق](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) يوفر class طريقة «rename_field»، والتي تسمح للمطورين بتغيير اسم حقل موجود مع الحفاظ على موضعه وقيمته ومظهره.

1. قم بتحميل نموذج PDF الموجود.
1. قم بإنشاء مثيل ForMeditor.
1. قم بربط وثيقة PDF بالمحرر.
1. أعد تسمية الحقل الهدف.
1. احفظ ملف PDF المحدث.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def rename_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Rename field in document
    form_editor.rename_field("City", "Town")
    # Save updated document
    form_editor.save(outfile)
```

