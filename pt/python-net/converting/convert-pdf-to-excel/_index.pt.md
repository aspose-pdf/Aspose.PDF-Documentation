---
title: Converter PDF para Excel em Python
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /python-net/convert-pdf-to-excel/
lastmod: "2022-12-23"
keywords: converter PDF para Excel usando python, converter PDF para XLS usando python, converter PDF para XLSX usando python, exportar tabela de PDF para Excel em python.
description: A biblioteca Aspose.PDF para Python permite converter PDF para formato Excel usando Python. Esses formatos incluem XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Visão Geral

Este artigo explica como **converter PDF para formatos Excel usando Python**. Ele abrange os seguintes tópicos.

_Formato_: **XLS**

- [Python PDF para XLS](#python-pdf-to-xls)
- [Python Converter PDF para XLS](#python-pdf-to-xls)
- [Python Como converter arquivo PDF para XLS](#python-pdf-to-xls)

_Formato_: **XLSX**

- [Python PDF para XLSX](#python-pdf-to-xlsx)
- [Python Converter PDF para XLSX](#python-pdf-to-xlsx)
- [Python Como converter arquivo PDF para XLSX](#python-pdf-to-xlsx)

_Formato_: **Excel**

- [Python PDF para Excel](#python-pdf-to-xlsx)
- [Python PDF para Excel XLS](#python-pdf-to-xls)
- [Python PDF para Excel XLSX](#python-pdf-to-xlsx)

_Formato_: **CSV**

- [Python PDF para CSV](#python-pdf-to-csv)
- [Python Converter PDF para CSV](#python-pdf-to-csv)
- [Python Como converter arquivo PDF para CSV](#python-pdf-to-csv)

_Formato_: **ODS**

- [Python PDF para ODS](#python-pdf-to-ods)
- [Python Converter PDF para ODS](#python-pdf-to-ods)
- [Python Como converter arquivo PDF para ODS](#python-pdf-to-ods)

## Conversão de PDF para EXCEL via Python

**Aspose.PDF para Python via .NET** suporta o recurso de conversão de arquivos PDF para formatos Excel e CSV.

Aspose.PDF para Python via .NET é um componente de manipulação de PDF, introduzimos um recurso que renderiza o arquivo PDF para uma planilha Excel (arquivos XLSX). Durante essa conversão, as páginas individuais do arquivo PDF são convertidas em planilhas do Excel.

{{% alert color="success" %}}
**Tente converter PDF para Excel online**

Aspose.PDF apresenta a você o aplicativo online gratuito ["PDF para XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), onde você pode tentar investigar a funcionalidade e a qualidade do funcionamento.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

O trecho de código a seguir mostra o processo de conversão de um arquivo PDF para o formato XLS ou XLSX com Aspose.PDF para Python via .NET.

<a name="python-pdf-to-xls"><strong>Passos: Converter PDF para XLS em Python</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o documento PDF de origem.
2. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
3. Salve no formato **XLS** especificando a **extensão .xls** chamando o método [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) e passando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xls.xls"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003

    # Salve o arquivo no formato MS Excel
    document.save(output_pdf, save_option)
```


<a name="python-pdf-to-xlsx"><strong>Passos: Converter PDF para XLSX em Python</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o documento PDF de origem.
2. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
3. Salve no formato **XLSX** especificando a **extensão .xlsx** chamando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) e passando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_xlsx.xlsx"
    # Abra o documento PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()

    # Salve o arquivo no formato MS Excel
    document.save(output_pdf, save_option)
```

## Converter PDF para XLS com controle de Coluna

Ao converter um PDF para o formato XLS, uma coluna em branco é adicionada ao arquivo de saída como primeira coluna.
 O uso da opção InsertBlankColumnAtFirst na classe 'ExcelSaveOptions' é utilizado para controlar esta coluna. Seu valor padrão é verdadeiro.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_with_control_column.xls"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.insert_blank_column_at_first = True

    # Salvar o arquivo no formato MS Excel
    document.save(output_pdf, save_option)
```

## Converter PDF para uma Única Planilha do Excel

Ao exportar um arquivo PDF com muitas páginas para XLS, cada página é exportada para uma planilha diferente no arquivo do Excel. Isso ocorre porque a propriedade MinimizeTheNumberOfWorksheets é definida como falsa por padrão. Para garantir que todas as páginas sejam exportadas para uma única planilha no arquivo Excel de saída, defina a propriedade MinimizeTheNumberOfWorksheets como verdadeira.


<a name="python-pdf-to-excel-single"><strong>Passos: Converter PDF para XLS ou XLSX em uma Única Planilha no Python</strong></a>
1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o documento PDF de origem.
2. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) com **MinimizeTheNumberOfWorksheets = true**.
3. Salve no formato **XLS** ou **XLSX** com uma única planilha chamando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) e passando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_single_excel_worksheet.xls"
    # Abra o documento PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.minimize_the_number_of_worksheets = True

    # Salve o arquivo no formato MS Excel
    document.save(output_pdf, save_option)

```


## Converter para outros formatos de planilha

### Converter para CSV

A conversão para o formato CSV é realizada da mesma forma que acima. Tudo o que você precisa - definir o formato apropriado.

<a name="python-pdf-to-csv"><strong>Passos: Converter PDF para CSV em Python</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o documento PDF de origem.
2. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) com **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. Salve no formato **CSV** chamando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) e passando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_csv.csv"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.CSV

    # Salvar o arquivo
    document.save(output_pdf, save_option)
```


### Converter para ODS

<a name="python-pdf-to-ods"><strong>Passos: Converter PDF para ODS em Python</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o documento PDF de origem.
2. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) com **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Salve no formato **ODS** chamando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) e passando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

A conversão para o formato ODS é realizada da mesma forma que todos os outros formatos.

```python

    import aspose.pdf as ap
    
    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_ods.ods"
    # Abra o documento PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.ODS

    # Salve o arquivo
    document.save(output_pdf, save_option)
```


## Veja Também

Este artigo também aborda esses tópicos. Os códigos são os mesmos que acima.

_Formato_: **Excel**
- [Python PDF para Excel Código](#python-pdf-to-xlsx)
- [Python PDF para Excel API](#python-pdf-to-xlsx)
- [Python PDF para Excel Programaticamente](#python-pdf-to-xlsx)
- [Python PDF para Excel Biblioteca](#python-pdf-to-xlsx)
- [Python Salvar PDF como Excel](#python-pdf-to-xlsx)
- [Python Gerar Excel de PDF](#python-pdf-to-xlsx)
- [Python Criar Excel de PDF](#python-pdf-to-xlsx)
- [Python Conversor de PDF para Excel](#python-pdf-to-xlsx)

_Formato_: **XLS**
- [Python PDF para XLS Código](#python-pdf-to-xls)
- [Python PDF para XLS API](#python-pdf-to-xls)
- [Python PDF para XLS Programaticamente](#python-pdf-to-xls)
- [Python PDF para XLS Biblioteca](#python-pdf-to-xls)
- [Python Salvar PDF como XLS](#python-pdf-to-xls)
- [Python Gerar XLS de PDF](#python-pdf-to-xls)
- [Python Criar XLS de PDF](#python-pdf-to-xls)
- [Python Conversor de PDF para XLS](#python-pdf-to-xls)

_Formato_: **XLSX**

- [Python PDF para XLSX Código](#python-pdf-to-xlsx)
- [API Python PDF para XLSX](#python-pdf-to-xlsx)
- [Python PDF para XLSX Programaticamente](#python-pdf-to-xlsx)
- [Biblioteca Python PDF para XLSX](#python-pdf-to-xlsx)
- [Python Salvar PDF como XLSX](#python-pdf-to-xlsx)
- [Python Gerar XLSX de PDF](#python-pdf-to-xlsx)
- [Python Criar XLSX de PDF](#python-pdf-to-xlsx)
- [Conversor Python PDF para XLSX](#python-pdf-to-xlsx)

_Format_: **CSV**
- [Código Python PDF para CSV](#python-pdf-to-csv)
- [API Python PDF para CSV](#python-pdf-to-csv)
- [Python PDF para CSV Programaticamente](#python-pdf-to-csv)
- [Biblioteca Python PDF para CSV](#python-pdf-to-csv)
- [Python Salvar PDF como CSV](#python-pdf-to-csv)
- [Python Gerar CSV de PDF](#python-pdf-to-csv)
- [Python Criar CSV de PDF](#python-pdf-to-csv)
- [Conversor Python PDF para CSV](#python-pdf-to-csv)

_Format_: **ODS**
- [Código Python PDF para ODS](#python-pdf-to-ods)
- [API Python PDF para ODS](#python-pdf-to-ods)
- [Python PDF para ODS Programaticamente](#python-pdf-to-ods)
- [Biblioteca Python PDF para ODS](#python-pdf-to-ods)

- [Python Salvar PDF como ODS](#python-pdf-to-ods)
- [Python Gerar ODS de PDF](#python-pdf-to-ods)  
- [Python Criar ODS de PDF](#python-pdf-to-ods)  
- [Python Conversor de PDF para ODS](#python-pdf-to-ods)