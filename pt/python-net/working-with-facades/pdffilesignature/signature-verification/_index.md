---
title: Verificação de Assinatura
type: docs
weight: 90
url: /pt/python-net/signature-verification/
description: Saiba como verificar assinaturas digitais e verificar se um PDF contém assinaturas usando PdfFileSignature em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verificar Assinaturas de PDF em Python
Abstract: Este artigo explica como verificar assinaturas digitais em documentos PDF com Aspose.PDF for Python via .NET. Ele mostra como validar uma assinatura existente e como verificar se um PDF contém alguma assinatura.
---

Aspose.PDF for Python via .NET fornece o [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fachada para validar documentos PDF assinados. Depois que um PDF foi assinado, você pode usá-lo para confirmar que uma assinatura é válida e para detectar se o documento contém entradas de assinatura.

Este exemplo demonstra duas tarefas comuns de verificação:

1. Verifique se uma assinatura PDF existente é válida.
1. Verifique se um PDF contém alguma assinatura.

## Verificar uma assinatura PDF

Usar `verify_signature()` quando você precisa validar uma assinatura específica no documento. O exemplo resolve o primeiro nome de assinatura disponível e verifica se essa assinatura é válida.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def verify_pdf_signature(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signature(sign_name)
        print(f"Signature '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

## Verificar se um PDF contém assinaturas

Usar `contains_signature()` quando você só precisa saber se o PDF inclui alguma assinatura. Isso é útil como uma verificação rápida antes de executar uma lógica de verificação ou extração mais detalhada.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_if_pdf_contains_signatures(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        contains_signatures = pdf_signature.contains_signature()
        print(f"PDF contains signatures: {contains_signatures}")
    finally:
        pdf_signature.close()
```
