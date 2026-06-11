---
title: شهادة PDF
linktitle: شهادة PDF
type: docs
weight: 30
url: /ar/python-net/pdf-certification/
description: تعرف على كيفية التصديق على مستندات PDF في Python باستخدام PDFfileSignature و DocMDPsignature مع أذونات تعديل المستندات المختلفة.
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بالتصديق على مستندات PDF باستخدام أذونات DocMDP في بايثون
Abstract: تشرح هذه المقالة كيفية التصديق على مستندات PDF باستخدام Aspose.PDF لبيثون عبر.NET باستخدام واجهة PDFfileSignature. يوضح كيفية إنشاء DocMDPSignature وتطبيق الشهادة بأذونات تعبئة النماذج وقفل مستند بمستوى شهادة بدون تغيير.
---

يتيح لك Aspose.PDF لـ Python عبر .NET التصديق على مستندات PDF من خلال تطبيق توقيع على مستوى المستند باستخدام [توقيع ملف PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/). تختلف الشهادة عن توقيع الموافقة القياسي لأنها تحدد التغييرات، إن وجدت، المسموح بها بعد اعتماد المستند.

توضح هذه المقالة عمليتي سير عمل شائعتين للشهادات:

1. قم بالتصديق على ملف PDF واسمح بملء النموذج بعد الشهادة.
1. قم بالتصديق على ملف PDF ومنع أي تغييرات أخرى.

## قم بالتصديق على ملف PDF لملء النموذج

استخدم هذا الأسلوب عندما يجب أن يظل المستند معتمدًا ولكن لا يزال المستخدمون بحاجة إلى إكمال النماذج التفاعلية أو متابعة توقيع الملف. ال `FILLING_IN_FORMS` يسمح مستوى الإذن بهذه التغييرات التي يتم التحكم فيها مع الحفاظ على صلاحية الشهادة.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def certify_pdf_with_mdp_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.FILLING_IN_FORMS,
            reason="Certified for form filling and signing",
        )
        pdf_signature.certify(
            1,
            "Certified for form filling and signing",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## قم بتطبيق شهادة على مستوى المستند دون السماح بإجراء أي تغييرات

استخدم هذا الوضع عندما يجب أن تظل الوثيقة المعتمدة بدون تغيير بعد الشهادة. ال `NO_CHANGES` مستوى الإذن مناسب لملفات PDF النهائية حيث يجب أن يؤدي أي تعديل لاحق إلى إبطال حالة الشهادة.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_document_level_certification(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.NO_CHANGES,
            reason="Certified with no further changes allowed",
        )
        pdf_signature.certify(
            1,
            "Certified with no further changes allowed",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
