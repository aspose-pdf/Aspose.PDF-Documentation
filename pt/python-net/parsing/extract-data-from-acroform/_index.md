---
title: Extrair Dados de AcroForm usando Python
linktitle: Extrair Dados de AcroForm
type: docs
weight: 50
url: /pt/python-net/extract-data-from-acroform/
description: Aspose.PDF facilita a extração de dados de campos de formulário de arquivos PDF. Aprenda como extrair dados de AcroForms e salvá-los em formato JSON, XML ou FDF.
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Extrair Dados de AcroForm via Python
Abstract: O artigo oferece um guia abrangente sobre como usar o Aspose.PDF para Python para gerenciar campos de formulário em documentos PDF. Detalha vários métodos para extrair, manipular e exportar dados de formulário de PDFs. O artigo começa demonstrando como extrair os valores dos campos de formulário e armazená‑los em um dicionário, fornecendo posteriormente os dados em formato JSON. Ele também ilustra a exportação de dados de formulário diretamente para arquivos JSON, aprimorando as capacidades de serialização de dados. Além disso, o artigo aborda a exportação de dados de formulário para outros formatos, como XML, FDF (Formato de Dados de Formulário) e XFDF, que são úteis para intercâmbio de dados e armazenamento estruturado. Cada seção inclui trechos de código Python para auxiliar na compreensão e implementação. No geral, o artigo serve como um recurso prático para desenvolvedores que desejam integrar o manuseio de formulários PDF em suas aplicações Python.
---

## Extrair campos de formulário de documento PDF

Além de permitir que você gere e preencha campos de formulário, o Aspose.PDF para Python facilita a extração de dados ou informações de campos de formulário de arquivos PDF.

O trecho de código cria um dicionário para armazenar os valores de todos os campos no formulário PDF. Ele itera pelos nomes dos campos do formulário, recupera seus valores e preenche o dicionário com esses dados. Por fim, imprime os valores coletados do formulário.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = self.dataDir + infile
    form = apdf.facades.Form(path_infile)

    form_values = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_values[formField] = form.get_field(formField)

    print(form_values)
```

## Recuperar valor de campo de formulário por título

## Extrair campos de formulário de documento PDF para JSON

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

O trecho de código Python fornecido extrai os valores de seus campos e serializa esses dados em formato JSON. Ele importa os módulos necessários, constrói os caminhos de arquivos de entrada e saída, recupera os nomes e valores dos campos do formulário PDF e grava a string JSON serializada em um arquivo de saída especificado.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if need
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    # Output the JSON string
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Extrair Dados para XML de um Arquivo PDF

O próximo trecho de código Python cria um objeto de formulário, vincula um documento PDF a esse objeto e exporta os dados do formulário para um arquivo XML. O código extrai automaticamente os dados de um formulário PDF e os salva em um formato XML estruturado.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export data to XML file
    with FileIO(path_outfile, "w") as f:
        form.export_xml(f)
```

## Exportar Dados para FDF de um Arquivo PDF

O trecho de código a seguir cria um objeto de formulário, vincula um documento PDF a esse formulário e, em seguida, exporta os dados do formulário para um arquivo FDF (Formato de Dados de Formulário). O arquivo FDF é um formato usado para armazenar dados de formulário de documentos PDF, permitindo fácil intercâmbio de dados.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## Exportar Dados para XFDF de um Arquivo PDF

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

