---
title: Trabalhando com formulários XFA
linktitle: Formulários XFA
type: docs
weight: 20
url: /pt/python-net/xfa-forms/
description: Aspose.PDF for Python via .NET API permite que você trabalhe com campos XFA e XFA Acroform em um documento PDF.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Converter XFA-para-Acroform

{{% alert color="primary" %}}

Experimente online
Você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online neste link: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

O próximo trecho de código demonstra como converter um formulário XFA (XML Forms Architecture) dinâmico para um AcroForm padrão.

**Etapas principais incluem:**

1. Carregando o documento PDF de entrada.
1. Alterando o tipo de formulário para STANDARD.
1. Salvando o PDF convertido em um novo arquivo.

Esta conversão permite melhor compatibilidade e tratamento consistente de formulários em diferentes leitores e aplicativos PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_dynamic_xfa_to_acroform(infile: str, outfile: str):
    """Convert dynamic XFA form to standard AcroForm."""
    with ap.Document(infile) as document:
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```

## Uso de IgnoreNeedsRendering

Este exemplo demonstra como converter um formulário XFA dinâmico para um AcroForm padrão usando Aspose.PDF for Python. O código verifica se o PDF de entrada contém um formulário XFA e substitui a renderização se necessário. Em seguida, define o tipo de formulário como STANDARD e salva o PDF atualizado.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_xfa_form_with_ignore_needs_rendering(infile: str, outfile: str):
    """Convert XFA form ignoring needs rendering flag."""
    with ap.Document(infile) as document:
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```
