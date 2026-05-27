---
title: Revisão e Permissões
type: docs
weight: 40
url: /pt/python-net/revision-permissions/
description: Aprenda como inspecionar revisões de assinatura, revisões de documento e permissões de certificação em arquivos PDF usando PdfFileSignature em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ler Dados de Revisão de Assinatura PDF e Permissão de Acesso em Python
Abstract: Este artigo explica como inspecionar informações de revisão e permissão em arquivos PDF assinados ou certificados com Aspose.PDF for Python via .NET. Ele mostra como obter o número da revisão de uma assinatura, contar o total de revisões de documento e ler as permissões de acesso de um PDF certificado.
---

Aspose.PDF for Python via .NET fornece o [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fachada para trabalhar com documentos PDF assinados e certificados. Além de adicionar assinaturas, você também pode inspecionar os metadados da assinatura para entender quantas revisões um documento contém e quais mudanças são permitidas após a certificação.

Este exemplo demonstra três tarefas comuns de inspeção:

1. Obtenha o número da revisão de uma assinatura existente.
1. Obtenha o número total de revisões em um documento assinado.
1. Leia as permissões de acesso de um PDF certificado.

## Obtenha o número da revisão de uma assinatura

Use esta abordagem quando um PDF já contém uma ou mais assinaturas e você precisar identificar a revisão associada a uma assinatura específica. O exemplo resolve o primeiro nome de assinatura disponível e então chama `get_revision()`.

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

## Obtenha o número total de revisões do documento

Usar `get_total_revision()` quando você precisa saber quantas revisões estão armazenadas no PDF assinado. Isso é útil para verificar se o documento passou por várias atualizações após a aplicação da assinatura original.

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

## Obtenha permissões de acesso de um PDF certificado

Documentos certificados podem definir quais alterações são permitidas após a certificação. Use `get_access_permissions()` para inspecionar esse nível de permissão e determinar se o documento permite nenhuma alteração, preenchimento de formulários ou outras modificações controladas.

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

