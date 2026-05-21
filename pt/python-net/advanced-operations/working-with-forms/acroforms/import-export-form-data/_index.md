---
title: Importar e Exportar Dados de Formulário
linktitle: Importar e Exportar Dados de Formulário
type: docs
weight: 80
url: /pt/python-net/import-export-form-data/
description: Importar e exportar dados de campo AcroForm em XML, FFD, XFDF e JSON usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Técnicas de importação e exportação usando Aspose.PDF for Python via .NET.
Abstract: Esta compilação apresenta um conjunto abrangente de técnicas de importação e exportação de dados de formulário usando Aspose.PDF for Python via .NET. Ela cobre fluxos de trabalho para integrar formulários PDF com formatos de dados externos, incluindo XML, FDF, XFDF e JSON. Os usuários podem automatizar o preenchimento em massa de formulários ao importar dados estruturados em campos interativos, ou extrair valores de campo para análise, backup ou integração com outros sistemas. Os exemplos demonstram como vincular formulários PDF, transferir dados entre formatos e salvar documentos atualizados, permitindo um processamento de documentos escalável e consistente em diversas aplicações.
---

Esta página mostra fluxos de trabalho comuns para importar e exportar dados AcroForm com Aspose.PDF for Python via .NET. Todas as operações utilizam o [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada.

## Importar dados de campo de formulário do XML

Use esta abordagem para preencher um formulário PDF com dados XML externos.

1. Criar um `Form` objeto.
1. Vincule o PDF de entrada.
1. Abra o arquivo de dados XML.
1. Importar dados XML para o formulário.
1. Salvar o PDF atualizado.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xml(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xml(f)

    form.save(output_file_name)
```

## Exportar dados de campo de formulário para XML

Este método exporta os valores dos campos de formulário de um documento PDF para XML.

1. Criar um `Form` objeto.
1. Vincule o PDF de entrada.
1. Abra o arquivo de saída XML.
1. Exportar dados do formulário para XML.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xml(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)
    with FileIO(output_file_name, "w") as f:
        form.export_xml(f)
```

## Importar dados de campo de formulário do FDF

O `import_data_from_fdf` método importa dados de campo de formulário de um arquivo FDF (Forms Data Format) para um formulário PDF.

1. Criar um `Form` objeto.
1. Vincule o PDF de entrada.
1. Importe os dados do formulário com `import_fdf()`.
1. Salvar o PDF atualizado.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_fdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_fdf(f)
        form.save(output_file_name)
```

## Exportar dados de FormField para FDF

Este exemplo exporta os dados do formulário de um documento PDF para um arquivo FDF.

1. Criar um `Form` objeto.
1. Vincular o documento PDF.
1. Exportar dados de formulário com `export_fdf()`.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_fdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_fdf(f)
```

## Importar dados de campo de formulário do XFDF

Use este método para importar dados de campos de formulário de um arquivo XFDF (XML Forms Data Format) para um formulário PDF.

1. Criar um `Form` objeto.
1. Vincule o PDF de entrada.
1. Importar dados de formulário de um arquivo XFDF.
1. Salvar o PDF atualizado.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xfdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xfdf(f)
        form.save(output_file_name)
```

## Exportar dados de campos de formulário para XFDF

Este código exporta os dados dos campos de formulário de um documento PDF para um arquivo XFDF.

1. Criar um `Form` objeto.
1. Vincule o PDF de entrada.
1. Exportar dados de formulário para XFDF.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xfdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_xfdf(f)
```

## Importar dados de outro PDF

Este exemplo transfere os dados de campos de formulário de um PDF de origem para um PDF de destino exportando XFDF para um fluxo em memória e importando-o para o formulário de destino.

1. Criar origem e destino `Form` objetos.
1. Vincule os PDFs de origem e destino.
1. Exportar dados do formulário do PDF de origem.
1. Importar dados de formulário para o PDF de destino.
1. Salve o PDF de destino atualizado.

```python
from io import StringIO
import aspose.pdf as ap

def import_data_from_another_pdf(source_pdf_name, destination_pdf_name, output_file_name):
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    form_source.bind_pdf(source_pdf_name)
    form_dest.bind_pdf(destination_pdf_name)

    with StringIO() as xfdf_stream:
        form_source.export_xfdf(xfdf_stream)
        xfdf_stream.seek(0)
        form_dest.import_xfdf(xfdf_stream)

    form_dest.save(output_file_name)
```

## Extrair campos de formulário para JSON

Este método exporta campos de formulário para um arquivo JSON por meio de `export_json()`.

1. Criar um `Form` objeto.
1. Abra o arquivo de saída JSON.
1. Exportar campos de formulário usando `export_json()`.

```python
from io import FileIO
import aspose.pdf as ap

def extract_form_fields_to_json(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    with FileIO(output_file_name, "w") as json_file:
        form.export_json(json_file, True)
```

## Extrair campos de formulário para documento JSON

Este exemplo cria um documento JSON personalizado a partir dos nomes e valores dos campos de formulário.

1. Crie um objeto Form a partir do arquivo de entrada.
1. Inicialize um dicionário vazio para armazenar os dados dos campos de formulário.
1. Itere por todos os campos de formulário e extraia seus valores.
1. Serializar o dicionário de dados do formulário em uma string JSON com indentação de 4 espaços.
1. Escreva a string JSON no arquivo de saída com codificação UTF-8.

```python
import json
import aspose.pdf as ap

def extract_form_fields_to_json_doc(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    form_data = {}
    for field_name in form.field_names:
        form_data[field_name] = form.get_field(field_name)

    json_string = json.dumps(form_data, indent=4)

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Tópicos Relacionados (abordagem Facades)

- [Importar Dados XML](/pdf/pt/python-net/import-xml-data/)
- [Importar Dados FDF](/pdf/pt/python-net/import-fdf-data/)
- [Importar dados XFDF](/pdf/pt/python-net/import-xfdf-data/)
- [Importar Dados JSON](/pdf/pt/python-net/import-json-data/)
- [Exportar para XML](/pdf/pt/python-net/export-to-xml/)
- [Exportar para FDF](/pdf/pt/python-net/export-to-fdf/)
- [Exportar para XFDF](/pdf/pt/python-net/export-to-xfdf/)
- [Exportar para JSON](/pdf/pt/python-net/export-to-json/)
