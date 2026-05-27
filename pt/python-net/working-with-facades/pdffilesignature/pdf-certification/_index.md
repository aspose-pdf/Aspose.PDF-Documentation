---
title: Certificação de PDF
type: docs
weight: 30
url: /pt/python-net/pdf-certification/
description: Aprenda como certificar documentos PDF em Python usando PdfFileSignature e DocMDPSignature com diferentes permissões de modificação de documento.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Certificar documentos PDF com permissões DocMDP em Python
Abstract: Este artigo explica como certificar documentos PDF com Aspose.PDF for Python via .NET usando a fachada PdfFileSignature. Ele mostra como criar um DocMDPSignature, aplicar a certificação com permissões de preenchimento de formulário e bloquear um documento com um nível de certificação sem alterações.
---

Aspose.PDF for Python via .NET permite que você certifique documentos PDF aplicando uma assinatura ao nível do documento com [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/). A certificação é diferente de uma assinatura de aprovação padrão porque define quais alterações, se houver, são permitidas após o documento ter sido certificado.

Este artigo demonstra dois fluxos de trabalho de certificação comuns:

1. Certificar um PDF e permitir o preenchimento de formulários após a certificação.
1. Certificar um PDF e impedir quaisquer alterações adicionais.

## Certificar um PDF para preenchimento de formulários

Use esta abordagem quando o documento deve permanecer certificado, mas os usuários ainda precisam completar formulários interativos ou continuar assinando o arquivo. O `FILLING_IN_FORMS` o nível de permissão permite essas alterações controladas mantendo a certificação válida.

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

## Aplicar certificação ao nível do documento sem alterações permitidas

Use este modo quando o documento certificado deve permanecer inalterado após a certificação. O `NO_CHANGES` o nível de permissão é adequado para PDFs finalizados, onde qualquer modificação posterior deve invalidar o estado de certificação.

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
