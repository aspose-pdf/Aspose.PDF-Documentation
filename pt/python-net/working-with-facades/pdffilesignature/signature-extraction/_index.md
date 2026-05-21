---
title: Extração de Assinatura
type: docs
weight: 50
url: /pt/python-net/signature-extraction/
description: Saiba como extrair uma imagem de assinatura e o certificado de assinatura de um PDF assinado usando PdfFileSignature em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair Imagem de Assinatura e Certificado de PDF em Python
Abstract: Este artigo explica como extrair dados relacionados a assinaturas de documentos PDF assinados com Aspose.PDF for Python via .NET. Ele mostra como ler a primeira assinatura disponível, exportar sua imagem e salvar o fluxo do certificado associado em um arquivo de saída.
---

Aspose.PDF for Python via .NET fornece o [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fachada para inspecionar e extrair dados de documentos PDF assinados. Após um PDF ser assinado, você pode usá-la para exportar recursos de assinatura, como a imagem visual da assinatura e o certificado associado à assinatura.

Este exemplo demonstra duas tarefas comuns de extração:

1. Extrair a imagem visual associada a uma assinatura.
1. Extrair o certificado de assinatura de um PDF assinado.

## Extrair uma imagem de assinatura

Use este método quando o PDF contém uma assinatura visível e você deseja exportar os dados da imagem. O exemplo abre o documento assinado, obtém o primeiro nome de assinatura disponível, extrai o fluxo da imagem e grava‑o em um arquivo.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_image(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_image = pdf_signature.extract_image(sign_name)
        write_stream_data(signature_image, outfile)
    finally:
        pdf_signature.close()
```

## Extrair um certificado de assinatura

Usar `extract_certificate()` quando você precisar dos dados do certificado anexados a uma assinatura. Isso é útil para inspeção, fluxos de trabalho de validação ou para armazenar o certificado do assinante separadamente do documento PDF.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_certificate(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_certificate = pdf_signature.extract_certificate(sign_name)
        write_stream_data(signature_certificate, outfile)
    finally:
        pdf_signature.close()
```

