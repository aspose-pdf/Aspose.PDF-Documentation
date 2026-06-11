---
title: المراجعة والأذونات
linktitle: المراجعة والأذونات
type: docs
weight: 40
url: /ar/python-net/revision-permissions/
description: تعرف على كيفية فحص مراجعات التوقيع ومراجعات المستندات وأذونات الشهادات في ملفات PDF باستخدام PDFfileSignature في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: اقرأ مراجعة توقيع PDF وبيانات إذن الوصول في Python
Abstract: توضح هذه المقالة كيفية فحص معلومات المراجعة والإذن في ملفات PDF الموقعة أو المعتمدة باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية الحصول على رقم مراجعة التوقيع، وحساب إجمالي مراجعات المستند، وقراءة أذونات الوصول من ملف PDF معتمد.
---

يوفر Aspose.PDF لبيثون عبر .NET [توقيع ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) واجهة للعمل مع مستندات PDF الموقعة والمعتمدة. بالإضافة إلى إضافة التوقيعات، يمكنك أيضًا فحص بيانات تعريف التوقيع لفهم عدد المراجعات التي يحتوي عليها المستند والتغييرات المسموح بها بعد الشهادة.

يوضح هذا المثال ثلاث مهام فحص شائعة:

1. احصل على رقم المراجعة لتوقيع موجود.
1. احصل على العدد الإجمالي للمراجعات في مستند موقّع.
1. اقرأ أذونات الوصول من ملف PDF معتمد.

## احصل على رقم المراجعة للتوقيع

استخدم هذا الأسلوب عندما يحتوي PDF بالفعل على توقيع واحد أو أكثر وتحتاج إلى تحديد المراجعة المرتبطة بتوقيع معين. يقوم المثال بحل اسم التوقيع الأول المتاح ثم المكالمات `get_revision()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_revision(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_revision = pdf_signature.get_revision(sign_name)
        print(f"Signature Revision for '{sign_name}': {signature_revision}")
    finally:
        pdf_signature.close()
```

## احصل على العدد الإجمالي لمراجعات المستندات

استخدم `get_total_revision()` عندما تحتاج إلى معرفة عدد المراجعات المخزنة في ملف PDF الموقّع. يعد هذا مفيدًا للتحقق مما إذا كان المستند قد مر بتحديثات متعددة بعد تطبيق التوقيع الأصلي.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_total_document_revisions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        total_revisions = pdf_signature.get_total_revision()
        print(f"Total Document Revisions: {total_revisions}")
    finally:
        pdf_signature.close()
```

## احصل على أذونات الوصول من ملف PDF معتمد

يمكن للمستندات المعتمدة تحديد التغييرات المسموح بها بعد الشهادة. استخدم `get_access_permissions()` لفحص مستوى الإذن هذا وتحديد ما إذا كان المستند لا يسمح بأي تغييرات أو ملء النموذج أو أي تعديلات أخرى خاضعة للرقابة.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_access_permissions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        access_permissions = pdf_signature.get_access_permissions()
        print(f"Access Permissions: {access_permissions}")
    finally:
        pdf_signature.close()
```

