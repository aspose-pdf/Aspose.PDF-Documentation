---
title: Preencher AcroForm - Preencher Formulário PDF usando Python
linktitle: Preencher AcroForm
type: docs
weight: 20
url: /pt/python-net/fill-form/
description: Preencher campos AcroForm em um PDF Document usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como preencher FormField em PDF usando Python
Abstract: Este artigo explica como preencher campos AcroForm em um PDF Document usando Aspose.PDF for Python via .NET. O exemplo usa a fachada Form, mapeia nomes de campos para novos valores em um dicionário, atualiza os campos correspondentes e salva o PDF de saída. Essa abordagem é útil para fluxos de trabalho automatizados de conclusão de Document e processamento em massa de formulários.
---

## Preencher FormField em um PDF Document

O exemplo a seguir preenche vários campos em um PDF Form existente usando o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada.

Use as etapas a seguir:

1. Crie um dicionário com nomes de campos e valores.
1. Associe o PDF de entrada a um objeto Form.
1. Iterar pelos campos de formulário disponíveis.
1. Preencher os campos que existem no dicionário.
1. Salvar o PDF atualizado.

```python
import aspose.pdf as ap

def fill_form(input_file_name, output_file_name):
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New",
    }

    form = ap.facades.Form(input_file_name)

    for field_name in form.field_names:
        if field_name in new_field_values:
            form.fill_field(field_name, new_field_values[field_name])

    form.save(output_file_name)
```

## Tópicos Relacionados

- [Criar AcroForm](/pdf/pt/python-net/create-form/)
- [Extrair AcroForm](/pdf/pt/python-net/extract-form/)
- [Importar e Exportar Dados do Formulário](/pdf/pt/python-net/import-export-form-data/)