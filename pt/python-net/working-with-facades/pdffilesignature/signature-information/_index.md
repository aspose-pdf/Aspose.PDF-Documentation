---
title: Informações da Assinatura
type: docs
weight: 60
url: /pt/python-net/signature-information/
description: Aprenda como ler nomes de assinaturas, detalhes do assinante, carimbos de data/hora e metadados de assinatura de arquivos PDF assinados usando PdfFileSignature em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ler Detalhes da Assinatura de Documentos PDF em Python
Abstract: Este artigo explica como inspecionar metadados de assinatura em documentos PDF assinados com Aspose.PDF for Python via .NET. Ele mostra como listar nomes de assinaturas, ler detalhes do assinante, obter a data e hora da assinatura e extrair o motivo e o local da assinatura.
---

Aspose.PDF for Python via .NET fornece o [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fachada para inspeção de assinaturas digitais em documentos PDF. Após um documento ter sido assinado, você pode usá-la para ler os nomes das assinaturas e recuperar metadados como o nome do assinante, informações de contato, hora da assinatura, motivo e localização.

Este exemplo demonstra quatro tarefas comuns de informações de assinatura:

1. Listar todos os nomes de assinatura em um PDF assinado.
1. Ler detalhes do assinante para uma assinatura selecionada.
1. Obtenha a data e hora da assinatura.
1. Leia o motivo e a localização da assinatura.

## Obtenha nomes de assinatura

Use este método quando um PDF pode conter uma ou mais assinaturas e você deseja inspecionar quais entradas de assinatura estão disponíveis. O exemplo abre o documento e imprime a lista retornada por `get_sign_names()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_names(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature_names = list_signature_names(pdf_signature)
        print(f"Signature Names: {signature_names}")
    finally:
        pdf_signature.close()
```

## Obter detalhes do assinante

Depois de conhecer o nome da assinatura, você pode recuperar metadados específicos do assinante. Este exemplo lê o nome do assinante e as informações de contato da primeira assinatura disponível no documento.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signer_details(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signer_name = pdf_signature.get_signer_name(sign_name)
        contact_info = pdf_signature.get_contact_info(sign_name)
        print(
            f"Signer Details for '{sign_name}': "
            f"signer_name={signer_name}, contact_info={contact_info}"
        )
    finally:
        pdf_signature.close()
```

## Obter data e hora da assinatura

Usar `get_date_time()` para determinar quando uma assinatura específica foi aplicada. Isso é útil para auditoria e para exibir o histórico de assinaturas nos fluxos de trabalho de documentos.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_date_and_time(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_date = pdf_signature.get_date_time(sign_name)
        print(f"Signature Date and Time for '{sign_name}': {signature_date}")
    finally:
        pdf_signature.close()
```

## Obter motivo e localização da assinatura

As assinaturas digitais também podem armazenar metadados descritivos, como o motivo e a localização da assinatura. Este exemplo recupera ambos os valores para a assinatura selecionada e os imprime juntos.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_reason_and_location(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_reason = pdf_signature.get_reason(sign_name)
        signature_location = pdf_signature.get_location(sign_name)
        print(
            f"Signature Reason and Location for '{sign_name}': "
            f"reason={signature_reason}, location={signature_location}"
        )
    finally:
        pdf_signature.close()
```

