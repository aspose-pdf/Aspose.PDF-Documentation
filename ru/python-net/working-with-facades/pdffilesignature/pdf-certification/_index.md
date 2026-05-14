---
title: Сертификация PDF
linktitle: Сертификация PDF
type: docs
weight: 30
url: /python-net/pdf-certification/
description: Узнайте, как сертифицировать PDF‑документы в Python с помощью PdfFileSignature и DocMDPSignature с различными разрешениями на изменение документа.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сертифицировать PDF‑документы с разрешениями DocMDP в Python
Abstract: В этой статье объясняется, как сертифицировать PDF‑документы с помощью Aspose.PDF for Python via .NET, используя фасад PdfFileSignature. Показано, как создать DocMDPSignature, применить сертификацию с разрешениями на заполнение форм и заблокировать документ на уровне сертификации «без изменений».
---

Aspose.PDF for Python via .NET позволяет вам сертифицировать PDF‑документы, применяя подпись уровня документа с [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/). Сертификация отличается от обычной подписи одобрения, потому что она определяет, какие изменения, если они допускаются, разрешены после того, как документ был сертифицирован.

В этой статье демонстрируются два типичных рабочего процесса сертификации:

1. Сертифицировать PDF и разрешить заполнение форм после сертификации.
1. Сертифицировать PDF и предотвратить любые дальнейшие изменения.

## Сертифицировать PDF для заполнения форм

Используйте этот подход, когда документ должен оставаться сертифицированным, но пользователям всё ещё необходимо заполнять интерактивные формы или продолжать подписывать файл. The `FILLING_IN_FORMS` Уровень разрешения позволяет вносить эти контролируемые изменения, при этом сохраняя сертификат действительным.

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

## Применить сертификацию на уровне документа без разрешения на изменения

Используйте этот режим, когда сертифицированный документ должен оставаться неизменным после сертификации. The `NO_CHANGES` уровень разрешения подходит для окончательных PDF, где любое последующее изменение должно аннулировать состояние сертификации.

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
