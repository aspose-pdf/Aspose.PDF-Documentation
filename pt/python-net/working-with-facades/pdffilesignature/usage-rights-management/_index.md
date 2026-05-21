---
title: Gerenciamento de Direitos de Uso
type: docs
weight: 100
url: /pt/python-net/usage-rights-management/
description: Saiba como detectar e remover direitos de uso de documentos PDF usando PdfFileSignature em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover Direitos de Uso de PDF em Python
Abstract: Este artigo explica como inspecionar e remover direitos de uso de documentos PDF com Aspose.PDF for Python via .NET. Ele mostra como verificar se um PDF contém direitos de uso e como salvar uma nova versão do documento após a remoção desses direitos.
---

Aspose.PDF for Python via .NET fornece o [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fachada para trabalhar com PDFs assinados e configurações relacionadas de direitos de uso. Em alguns fluxos de trabalho, pode ser necessário inspecionar se um documento contém direitos de uso e removê-los antes de salvar uma versão atualizada do arquivo.

Este exemplo demonstra uma tarefa comum de gerenciamento de direitos de uso:

1. Verifique se um PDF contém direitos de uso.
1. Remova os direitos de uso do documento.
1. Salve o arquivo PDF atualizado.

## Verifique se o PDF contém direitos de uso

Antes de remover os direitos de uso, o exemplo verifica o estado atual do documento chamando `contains_usage_rights()`. Isto permite confirmar se os direitos de uso estão presentes antes de fazer alterações.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_usage_rights(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights: {had_usage_rights}")
    finally:
        pdf_signature.close()
```

## Remover direitos de uso do PDF

Usar `remove_usage_rights()` quando o documento não deve mais manter as configurações de direitos de uso existentes. O exemplo verifica o estado inicial, remove os direitos e salva o PDF atualizado em um novo arquivo.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_usage_rights(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights before removal: {had_usage_rights}")
        pdf_signature.remove_usage_rights()
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
