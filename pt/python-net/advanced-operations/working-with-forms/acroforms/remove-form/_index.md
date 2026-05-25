---
title: Excluir Formulários de PDF em Python
linktitle: Excluir Formulários
type: docs
weight: 70
url: /pt/python-net/remove-form/
description: Remover objetos de formulário de páginas PDF usando Aspose.PDF for Python via .NET, incluindo limpeza completa e exclusão direcionada.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover Formulários de PDF com Aspose.PDF for Python via .NET
Abstract: Este artigo apresenta duas abordagens para remover elementos de formulário de documentos PDF usando Aspose.PDF for Python via .NET. O primeiro método limpa todos os objetos de formulário de uma página selecionada, enquanto o segundo método remove apenas recursos de formulário Typewriter correspondentes. Esses exemplos ajudam na limpeza de formulários, preparação de modelos e fluxos de trabalho de normalização de documentos.
---

## Remover Todos os Formulários de uma Página

Este código remove todos os objetos de formulário da página especificada por `page_num` e salva o documento atualizado.

1. Carregue o documento PDF.
1. Acesse os recursos da página.
1. Limpe os objetos de formulário.
1. Salve o documento atualizado.

```python
import aspose.pdf as ap

def remove_all_forms(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(output_file_name)
```

## Remover um Tipo de Formulário Específico

O próximo exemplo itera pelos objetos de formulário em uma página PDF especificada, identifica anotações de formulário tipo máquina de escrever, exclui‑as e, em seguida, salva o PDF atualizado usando Aspose.PDF for Python via .NET.

1. Carregue o documento PDF.
1. Acessar formulários da página.
1. Iterar sobre formulários.
1. Verificar formulários tipo máquina de escrever.
1. Excluir o formulário correspondente.
1. Salve o documento atualizado.

```python
import aspose.pdf as ap

def remove_specified_form(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(output_file_name)
```

## Tópicos Relacionados

- [Criar AcroForm](/pdf/pt/python-net/create-form/)
- [Preencher AcroForm](/pdf/pt/python-net/fill-form/)
- [Modificando AcroForm](/pdf/pt/python-net/modifying-form/)
- [Publicando Formulários](/pdf/pt/python-net/posting-form/)
