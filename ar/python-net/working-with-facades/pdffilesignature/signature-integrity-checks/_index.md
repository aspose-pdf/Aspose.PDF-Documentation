---
title: عمليات التحقق من سلامة التوقيع
linktitle: عمليات التحقق من سلامة التوقيع
type: docs
weight: 70
url: /ar/python-net/signature-integrity-checks/
description: تعرف على كيفية التحقق مما إذا كان توقيع PDF يغطي المستند بأكمله والتحقق من سلامة المستند الموقّع باستخدام PDFfileSignature في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحقق من صحة تغطية توقيع PDF وتكاملها في Python
Abstract: تشرح هذه المقالة كيفية فحص سلامة التوقيع الرقمي في مستندات PDF الموقعة باستخدام Aspose.PDF لـ Python عبر .NET. يوضح كيفية التحقق مما إذا كان التوقيع يغطي المستند بأكمله وكيفية التحقق من سلامة المحتوى الموقّع.
---

يوفر Aspose.PDF لبيثون عبر .NET [توقيع ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) واجهة للتحقق من مستندات PDF الموقعة. بعد توقيع الملف، يمكنك استخدامه للتحقق مما إذا كان التوقيع ينطبق على المستند الكامل وما إذا كان المحتوى الموقّع لا يزال صالحًا.

يوضح هذا المثال فحصين شائعين للنزاهة:

1. تحقق مما إذا كان التوقيع يغطي المستند بأكمله.
1. تحقق من سلامة محتوى PDF الموقّع.

## تحقق مما إذا كان التوقيع يغطي المستند بأكمله

استخدم `covers_whole_document()` عندما تحتاج إلى تأكيد أن التوقيع ينطبق على ملف PDF الكامل وليس فقط على جزء من محتواه. يقرأ المثال اسم التوقيع الأول المتاح ويتحقق من تغطيته.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_signature_coverage(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        covers_document = pdf_signature.covers_whole_document(sign_name)
        print(f"Signature '{sign_name}' covers the whole document: {covers_document}")
    finally:
        pdf_signature.close()
```

## التحقق من سلامة المستند

استخدم `verify_signed()` للتأكد من أن محتوى المستند الموقّع لم يتم تغييره بعد تطبيق التوقيع. تساعد هذه الطريقة في التحقق مما إذا كانت الوثيقة لا تزال صالحة للتوقيع المحدد.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def validate_document_integrity(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signed(sign_name)
        print(f"Document integrity for '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

