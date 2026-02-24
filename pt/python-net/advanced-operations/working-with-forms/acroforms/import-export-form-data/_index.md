---
title: Importar e Exportar Dados de Formulário
type: docs
weight: 80
url: /pt/python-net/import-export-form-data/
description: Esta seção explica como importar e exportar dados de formulário.
lastmod: "2025-08-05"
TechArticle: true
AlternativeHeadline: Técnicas de importação e exportação usando Aspose.PDF para Python via .NET.
Abstract: Esta compilação apresenta um conjunto abrangente de técnicas de importação e exportação de dados de formulário usando Aspose.PDF para Python via .NET. Ela cobre fluxos de trabalho para integrar formulários PDF com formatos de dados externos, incluindo XML, FDF, XFDF e JSON. Os usuários podem automatizar o preenchimento em massa de formulários importando dados estruturados para campos interativos, ou extrair os valores dos campos para análise, backup ou integração com outros sistemas. Os exemplos demonstram como vincular formulários PDF, transferir dados entre formatos e salvar documentos atualizados, permitindo um processamento de documentos escalável e consistente em diversas aplicações.
---

## Importar Dados de Formulário de um arquivo XML

O próximo exemplo demonstra como importar dados de formulário de um arquivo XML para um formulário PDF existente usando Aspose.PDF para Python. Ao vincular um formulário PDF, carregar os dados XML e salvar o arquivo atualizado, você pode preencher rapidamente campos interativos do formulário sem editar manualmente cada página. Este método é ideal para automatizar o preenchimento em massa de formulários, processar grandes conjuntos de dados e garantir a consistência dos dados em vários documentos.

Use os seguintes passos:

1. Crie um objeto Form usando Aspose.PDF.
1. Vincule o Formulário PDF.
1. Carregue os Dados XML.
1. Importe XML para o PDF.
1. Salve o PDF Atualizado.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Define the working directory path
    workdir_path = "/path/to/working/directory"

    # Construct full file paths using the working directory
    path_infile = path.join(workdir_path, infile)
    path_datafile = path.join(workdir_path, datafile)
    path_outfile = path.join(workdir_path, outfile)

    # Create a Form object from Aspose.PDF
    form = ap.facades.Form()

    # Bind the input PDF form
    form.bind_pdf(path_infile)

    # Import XML data into the form
    with FileIO(path_datafile, "r") as f:
        form.import_xml(f)

    # Save the form with imported data to a new PDF file
    form.save(path_outfile)
```

## Exportar Dados de Campos de Formulário de um documento PDF para um arquivo XML

A biblioteca Python mostra como exportar dados de campos de formulário de um documento PDF para um arquivo XML usando Aspose.PDF para Python. Ao vincular um formulário PDF e salvar seus valores de campo em formato XML, você pode armazenar, processar ou reutilizar facilmente os dados do formulário em outras aplicações ou fluxos de trabalho. Esta abordagem é ideal para backup de dados, análise e integração com sistemas externos.

Use os seguintes passos:

1. Crie um objeto Form usando Aspose.PDF.
1. Vincule o Formulário PDF
1. Exporte os Dados do Formulário
1. Salve os Valores dos Campos em XML

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Combine the working directory path with the input PDF file name
    path_infile = path.join(self.workdir_path, infile)

    # Combine the working directory path with the output XML file name
    path_outfile = path.join(self.workdir_path, datafile)

    # Create a Form object to work with PDF form fields
    form = ap.facades.Form()

    # Bind the PDF document containing the form
    form.bind_pdf(path_infile)

    # Open the XML file in write mode to store exported form data
    with FileIO(path_outfile, "w") as f:
        # Export form field data from the PDF to the XML file
        form.export_xml(f)
```

## Importar Dados de Campos de Formulário de um FDF

O método 'import_data_from_fdf' importa dados de campos de formulário de um arquivo FDF (Formato de Dados de Formulários) para um formulário PDF existente e salva o documento atualizado. Essa abordagem é útil para pré-preencher ou atualizar formulários PDF programaticamente sem modificar a estrutura do documento.

Use os seguintes passos:

1. Crie um objeto Form usando Aspose.PDF.
1. Vincule o PDF de entrada.
1. Importe os dados do formulário com import_fdf().
1. Salve o PDF com os dados importados no caminho de arquivo de saída especificado.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form()
    form.bind_pdf(path_infile)

    with FileIO(path_datafile, "r") as f:
        form.import_fdf(f)
        form.save(path_outfile)
```

## Exportar Dados de Campos de Formulário para FDF

Este exemplo demonstra como exportar dados de formulário de um documento PDF para um arquivo FDF (Formato de Dados de Formulários) usando Aspose.PDF para Python via .NET.

1. Crie um objeto Form usando Aspose.PDF.
1. Vincule o documento PDF.
1. Exporte os dados do formulário com export_fdf().

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## Importar Dados de Campos de Formulário de um XFDF

Este exemplo exporta dados de campos de formulário de um documento PDF para um arquivo XFDF (Formato XML de Dados de Formulários) e então salva o PDF atualizado usando Aspose.PDF para Python via .NET.

1. Crie um objeto Form usando Aspose.PDF.
1. Vincule o documento PDF ao formulário.
1. Exporte os dados do formulário para um arquivo XFDF.
1. Salve o formulário processado.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_datafile, "w") as f:
        form.export_xfdf(f)
        form.save(path_outfile)
```

## Exportar Dados de Campos de Formulário para XFDF

Este código extrai dados de campos de formulário de um documento PDF e os exporta para um arquivo XFDF (Formato XML de Dados de Formulários) usando Aspose.PDF para Python.

1. Crie um objeto Form usando Aspose.PDF.
1. Vincule o documento PDF ao formulário.
1. Exporte os dados do formulário para um arquivo FDF.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

## Importar Dados de outro PDF

Este trecho de código demonstra como transferir dados de campos de formulário de um PDF de origem para um PDF de destino. Os dados do formulário são exportados para um fluxo XFDF a partir do PDF de origem e então importados para o PDF alvo usando Aspose.PDF para Python via .NET.

1. Crie um objeto Form usando Aspose.PDF.
1. Vincule o documento PDF ao formulário.
1. Exporte os dados do formulário do PDF de origem.
1. Importe os dados do formulário para o PDF de destino.
1. Salve o PDF de destino atualizado.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    # Bind PDF document
    form_source.bind_pdf(path_infile)
    form_dest.bind_pdf(path_outfile)

    # Export form data to an FDF file
    with StringIO() as f:
        form_source.export_xfdf(f)
        form_dest.import_xfdf(f)
        form_dest.save()
```

## Extrair campos de formulário para Json

Este método extrai campos de formulário de um arquivo de entrada e os exporta para um arquivo JSON.

1. Crie um objeto Form usando Aspose.PDF.
1. Abra o arquivo de saída no modo de escrita usando FileIO().
1. Exporte os campos de formulário para o arquivo JSON usando o método form.export_json().

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

## Extrair campos de formulário para documento JSON

1. Crie um objeto Form a partir do arquivo de entrada.
1. Inicialize um dicionário vazio para armazenar os dados dos campos do formulário.
1. Itere por todos os campos de formulário e extraia seus valores.
1. Serialize o dicionário de dados do formulário para uma string JSON com identação de 4 espaços.
1. Escreva a string JSON no arquivo de saída com codificação UTF-8.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

