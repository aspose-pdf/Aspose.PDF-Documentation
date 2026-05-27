---
title: Gerenciamento de Assinaturas
type: docs
weight: 80
url: /pt/python-net/signature-management/
description: Aprenda como remover assinaturas digitais de documentos PDF e, opcionalmente, limpar campos de assinatura usando PdfFileSignature em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover Assinaturas PDF e Limpar Campos de Assinatura em Python
Abstract: Este artigo explica como gerenciar assinaturas digitais existentes em documentos PDF com Aspose.PDF for Python via .NET. Ele mostra como remover uma assinatura de um PDF e como remover uma assinatura juntamente com seu campo de assinatura associado.
---

Aspose.PDF for Python via .NET fornece o [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fachada para trabalhar com assinaturas digitais existentes em documentos PDF. Além de ler e validar assinaturas, você também pode removê-las quando um fluxo de trabalho requer que o conteúdo assinado seja atualizado ou que o campo de assinatura seja limpo.

Este exemplo demonstra duas tarefas comuns de gerenciamento de assinaturas:

1. Remova uma assinatura de um documento PDF.
1. Remova uma assinatura e limpe o campo de assinatura associado.

## Remova uma assinatura de um PDF

Usar `remove_signature()` quando você deseja excluir a assinatura selecionada do documento enquanto mantém a estrutura subjacente do campo de assinatura intacta. O exemplo abre o PDF assinado, resolve o nome da assinatura, remove‑a e salva o arquivo de saída atualizado.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_from_pdf(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Remover uma assinatura e limpar o campo

Use a sobrecarga com o adicional `True` marque quando quiser remover a assinatura e também limpar o campo de assinatura relacionado. Isso é útil quando o campo não deve permanecer no documento após a assinatura ter sido excluída.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_with_field_cleanup(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name, True)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
