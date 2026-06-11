---
title: احصل على امتيازات المستند
linktitle: احصل على امتيازات المستند
type: docs
weight: 10
url: /ar/python-net/get-document-privileges/
description: تعرف على كيفية التحقق برمجيًا من امتيازات مستند PDF باستخدام Aspose.PDF لـ Python. يوضح هذا البرنامج التعليمي كيفية استخدام فئة PDFfileInfo لقراءة إعدادات أمان المستند، مثل الطباعة أو النسخ أو تعديل الأذونات.
lastmod: "2026-06-11"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استرجع امتيازات مستند PDF باستخدام Aspose.PDF لبيثون
Abstract: يمكن أن تحتوي مستندات PDF على قيود أمان تحد من الإجراءات مثل طباعة النماذج أو نسخها أو تعديلها أو تعبئتها. من خلال الوصول إلى هذه الامتيازات برمجيًا، يمكن للمطورين تحديد العمليات المسموح بها على PDF. يوضح هذا الدليل كيفية استخدام فئة PDFfileInfo لاسترداد امتيازات مستند PDF وعرضها في Python.
---

تتحكم امتيازات PDF في ما يمكن للمستخدمين فعله وما لا يمكنهم فعله بالمستند. تتضمن الأذونات الشائعة:

- طباعة المستند
- نسخ المحتوى
- تعديل التعليقات التوضيحية أو المحتويات
- تعبئة حقول النموذج
- استخدام قارئات الشاشة
- تجميع المستندات أو دمجها

باستخدام Aspose.PDF لـ Python، يمكنك فحص هذه الإعدادات برمجيًا باستخدام [معلومات ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) فئة. يكون هذا مفيدًا بشكل خاص عند العمل مع ملفات PDF متعددة في عمليات سير العمل التلقائية أو التحقق من التوافق أو التحكم في معالجة المستندات في التطبيقات.

1. قم بتحميل ملف PDF.
1. استرجع امتيازات المستند الخاصة به.
1. قم بعرض الإجراءات المسموح بها للمستند.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_document_privileges(input_file_name):
    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)

    privileges = pdf_metadata.get_document_privilege()

    print("Document Privileges:")
    print(f"  Can Print: {privileges.allow_print}")
    print(f"  Can Degraded Print: {privileges.allow_degraded_printing}")
    print(f"  Can Copy: {privileges.allow_copy}")
    print(f"  Can Modify Contents: {privileges.allow_modify_contents}")
    print(f"  Can Modify Annotations: {privileges.allow_modify_annotations}")
    print(f"  Can Fill In: {privileges.allow_fill_in}")
    print(f"  Can Screen Readers: {privileges.allow_screen_readers}")
    print(f"  Can Assembly: {privileges.allow_assembly}")
```
