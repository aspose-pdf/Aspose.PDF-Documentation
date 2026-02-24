---
title: Excluir Formulários de PDF em Python
linktitle: Excluir Formulários
type: docs
weight: 70
url: /pt/python-net/remove-form/
description: Remover Texto com base no subtipo/formulário usando a biblioteca Aspose.PDF for Python via .NET. Remover todos os formulários do PDF.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover Formulários de PDF com Aspose.PDF for Python via .NET
Abstract: Este documento apresenta duas abordagens baseadas em Python para remover elementos de formulário de arquivos PDF usando Aspose.PDF for Python via .NET. O primeiro método demonstra como limpar todos os objetos de formulário de uma página específica acessando seu dicionário de recursos e invocando o método clear() na coleção de formulários. O segundo método oferece uma solução mais direcionada ao iterar através das anotações de formulário, identificar formulários do tipo máquina de escrever e excluí-los seletivamente com base em seus atributos. Ambas as técnicas concluem com a gravação do PDF atualizado em um caminho de saída especificado, oferecendo opções flexíveis para limpeza de formulários e refinamento de documentos em fluxos de trabalho automatizados.
---

## Remover todos os Formulários do PDF

Este código remove todos os elementos de formulário da primeira página de um documento PDF e, em seguida, salva o documento modificado no caminho de saída especificado.

1. Carregar o documento PDF.
1. Acessar os recursos da página.
1. Limpar objetos de formulário.
1. Salvar o documento atualizado.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(data_dir, infile)
    path_outfile = os.path.join(data_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(path_outfile)
```

## Remover Formulário Específico

O próximo exemplo itera pelos objetos de formulário em uma página PDF dada, identifica anotações de formulário do tipo máquina de escrever, exclui‑as e, em seguida, salva o PDF atualizado usando Aspose.PDF for Python via .NET.

1. Carregar o documento PDF.
1. Acessar os formulários da página.
1. Iterar sobre os formulários.
1. Verificar formulários do tipo máquina de escrever.
1. Excluir o formulário correspondente.
1. Salvar o documento atualizado.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if (form.it == "Typewriter" and form.subtype == "Form"):
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(path_outfile)
```
