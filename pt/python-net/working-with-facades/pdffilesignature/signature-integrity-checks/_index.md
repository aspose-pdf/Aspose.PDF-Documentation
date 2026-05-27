---
title: Verificações de Integridade de Assinatura
type: docs
weight: 70
url: /pt/python-net/signature-integrity-checks/
description: Saiba como verificar se uma assinatura PDF cobre todo o documento e validar a integridade do documento assinado usando PdfFileSignature em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validar Cobertura e Integridade da Assinatura PDF em Python
Abstract: Este artigo explica como inspecionar a integridade de assinatura digital em documentos PDF assinados com Aspose.PDF for Python via .NET. Ele mostra como verificar se uma assinatura cobre todo o documento e como validar a integridade do conteúdo assinado.
---

Aspose.PDF for Python via .NET fornece o [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fachada para validar documentos PDF assinados. Depois que um arquivo foi assinado, você pode usá-la para verificar se a assinatura se aplica ao documento completo e se o conteúdo assinado ainda é válido.

Este exemplo demonstra duas verificações de integridade comuns:

1. Verifique se uma assinatura cobre todo o documento.
1. Valide a integridade do conteúdo PDF assinado.

## Verifique se uma assinatura cobre todo o documento

Usar `covers_whole_document()` quando você precisa confirmar que a assinatura se aplica ao PDF completo e não apenas a parte de seu conteúdo. O exemplo lê o primeiro nome de assinatura disponível e verifica sua cobertura.

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

## Validar integridade do documento

Usar `verify_signed()` para confirmar que o conteúdo do documento assinado não foi alterado após a aplicação da assinatura. Este método ajuda a verificar se o documento permanece válido para a assinatura selecionada.

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

