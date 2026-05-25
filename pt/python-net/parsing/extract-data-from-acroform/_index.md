---
title: Extrair Dados do AcroForm usando Python
linktitle: Extrair Dados do AcroForm
type: docs
weight: 50
url: /pt/python-net/extract-data-from-acroform/
description: Aspose.PDF torna fácil extrair dados de campos de formulário de arquivos PDF. Aprenda como extrair dados de AcroForms e salvá-los em formato JSON, XML ou FDF.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair dados de AcroForm via Python
Abstract: O artigo fornece um guia abrangente sobre como usar Aspose.PDF for Python para gerenciar campos de formulário em documentos PDF. Ele detalha vários métodos para extrair, manipular e exportar dados de formulário de PDFs. O artigo começa demonstrando como extrair os valores dos campos de formulário e armazená‑los em um dicionário, exportando posteriormente os dados no formato JSON. Ainda demonstra a exportação direta dos dados de formulário para arquivos JSON, aprimorando as capacidades de serialização de dados. Além disso, o artigo aborda a exportação de dados de formulário para outros formatos, como XML, FDF (Forms Data Format) e XFDF, que são úteis para intercâmbio de dados e armazenamento estruturado. Cada seção inclui trechos de código Python para ajudar na compreensão e implementação. No geral, o artigo serve como um recurso prático para desenvolvedores que desejam integrar o manuseio de formulários PDF em suas aplicações Python.
---

## Extrair campos de formulário do documento PDF

[Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) de `aspose.pdf.facades` namespace fornece uma maneira direta de ler os dados de campo AcroForm sem abrir o modelo completo de objeto de documento. Itere sobre `form.field_names` para obter cada nome de campo presente no formulário, então chame `form.get_field(name)` para recuperar seu valor atual.

1. Construir um `Form` objeto passando o caminho do arquivo de entrada.
1. Iterar sobre `form.field_names` para enumerar todos os nomes de campo.
1. Chamar `form.get_field(name)` para cada nome e armazene o resultado em um dicionário.

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

## Recuperar o valor do campo de formulário por título

Quando você conhece o nome exato do campo (title) definido no formulário PDF, pode recuperar seu valor diretamente com `form.get_field(name)` sem iterar sobre toda a coleção de campos. Esta é a abordagem mais rápida quando apenas campos específicos são necessários.

1. Construir um [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) objeto com o caminho do arquivo de entrada.
1. Chamar `form.get_field("FieldName")` usando o título exato do campo como aparece no PDF.
1. Use o valor de string retornado conforme necessário em sua aplicação.

```python

    import aspose.pdf as apdf

    form = apdf.facades.Form(path_infile)

    # Retrieve a single field value by its name
    value = form.get_field("FirstName")
    print(value)
```

## Extrair campos de formulário de documento PDF para JSON

Existem duas maneiras de exportar dados AcroForm para JSON. A primeira usa o recurso interno `export_json` método em [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form), que serializa todos os dados de campo diretamente para um fluxo de arquivo em uma única chamada.

1. Construir um `Form` objeto com o caminho do arquivo de entrada.
1. Abra o arquivo de saída como um fluxo binário usando `FileIO`.
1. Chamar `form.export_json(stream, True)` para escrever a saída JSON.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

A segunda abordagem cria um dicionário Python a partir de `field_names` e `get_field`, então serializa com `json.dumps`. Use isso quando precisar transformar ou filtrar os dados antes de escrevê-los.

1. Iterar sobre `form.field_names` e preencha um dicionário com valores dos campos.
1. Serializar o dicionário com `json.dumps(form_data, indent=4)`.
1. Escreva a string JSON resultante no arquivo de saída.

```python

    import aspose.pdf as apdf
    from os import path
    import json

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Extrair Dados para XML de um Arquivo PDF

A exportação de XML é útil para integrar os dados de formulário PDF com sistemas que consomem feeds ou esquemas XML estruturados. O [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) classe fornece `export_xml` para lidar com a conversão em uma única etapa.

1. Criar um `Form` instanciar e vincular o PDF com `form.bind_pdf(path)`.
1. Abra o arquivo de saída como um fluxo binário.
1. Chamar `form.export_xml(stream)` escrever todos os dados dos campos como XML.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

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

## Exportar dados para FDF a partir de um arquivo PDF

FDF (Forms Data Format) é o formato de intercâmbio padrão para dados AcroForm e é amplamente suportado por visualizadores de PDF e ferramentas de processamento. Use `export_fdf` no [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) classe para produzir um arquivo FDF independente que pode ser importado de volta ao PDF original ou a outro formulário compatível.

1. Criar um `Form` instancie e vincule o PDF de origem com `form.bind_pdf(path)`.
1. Abra o arquivo de saída como um fluxo binário.
1. Chamar `form.export_fdf(stream)` para escrever os dados FDF.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

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

## Exportar Dados para XFDF a partir de um Arquivo PDF

XFDF (XML Forms Data Format) é o sucessor baseado em XML do FDF e é mais adequado para uso em serviços web e pipelines de dados modernos. Como FDD, um arquivo XFDF pode ser importado de volta para um formulário PDF compatível. Use `export_xfdf` no [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) classe para gerar a saída.

1. Criar um `Form` instancie e vincule o PDF de origem com `form.bind_pdf(path)`.
1. Abra o arquivo de saída como um fluxo binário.
1. Chamar `form.export_xfdf(stream)` para escrever os dados XFDF.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

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
