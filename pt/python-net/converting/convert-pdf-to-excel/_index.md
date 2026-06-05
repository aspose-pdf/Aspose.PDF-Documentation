---
title: Converter PDF para Excel em Python
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /pt/python-net/convert-pdf-to-excel/
lastmod: "2026-04-14"
description: Aprenda como converter PDF para Excel em Python, incluindo XLS, XLSX, CSV, ODS, saída de única planilha e manipulação de colunas com Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Converta PDF para Excel, XLSX, CSV e ODS em Python
Abstract: Este artigo mostra como converter arquivos PDF para formatos de planilha com Aspose.PDF for Python via .NET. Ele abrange saída em XLS, XLSX, XLSM, CSV e ODS, além de opções para controlar colunas em branco e reduzir o número de planilhas geradas.
---

## Converter PDF para Excel em Python

**Aspose.PDF for Python via .NET** suporta a conversão de arquivos PDF para Excel e outros formatos de planilha a partir de código Python.

Use esta página quando precisar converter um PDF para XLS, XLSX, CSV ou ODS para extração de tabelas, reutilização de relatórios, ordenação, filtragem ou análise posterior. Durante a conversão de PDF para Excel, páginas individuais do PDF podem ser renderizadas como planilhas do Excel.

O primeiro exemplo converte um arquivo PDF para o formato Spreadsheet 2003 XML. Seções posteriores mostram XLSX, XLSM, CSV, ODS e saída de planilha única.

{{% alert color="success" %}}
**Tente converter PDF para Excel online**

Aspose.PDF apresenta-lhe uma aplicação online ["PDF para XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para Excel com App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

O trecho de código a seguir mostra o processo de conversão de arquivo PDF em formato XLS ou XLSX com Aspose.PDF for Python via .NET.

Etapas: Converter um arquivo PDF para o formato Excel (Planilha XML 2003)

1. Carregue o documento PDF.
1. Configurar opções de salvamento do Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Salve o arquivo convertido.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_spread_sheet2003(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Converter PDF para XLSX em Python

Etapas: Converter um arquivo PDF para o formato XLSX (Excel 2007+)

1. Carregue o documento PDF.
1. Configurar opções de salvamento do Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Salve o arquivo convertido.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Converter PDF para XLSX com Controle de Coluna

Ao converter um PDF para o formato Excel, uma coluna em branco pode ser adicionada como a primeira coluna no arquivo de saída. Use o `insert_blank_column_at_first` opção de `ExcelSaveOptions` classe para controlar esse comportamento. Seu valor padrão é `true`.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_control_column(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Converter PDF para uma única planilha do Excel

Aspose.PDF for Python via .NET mostra como converter um PDF em um arquivo Excel (.xlsx), com a opção 'minimize_the_number_of_worksheets' habilitada.

Etapas: Converter PDF para XLS ou XLSX em uma única planilha no Python

1. Carregue o documento PDF.
1. Configurar opções de salvamento do Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. A opção 'minimize_the_number_of_worksheets' reduz o número de planilhas do Excel combinando páginas PDF em menos planilhas (por exemplo, uma planilha para todo o documento, se possível).
1. Salve o arquivo convertido.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_single_excel_worksheet(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Converter PDF para Excel 2007 habilitado para macro (XLSM)

Este exemplo em Python mostra como converter um arquivo PDF em um arquivo Excel no formato XLSM (Pasta de Trabalho do Excel com Macro).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_macro(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Converter para outros formatos de planilha

### Converter PDF para CSV

A função 'convert_pdf_to_excel_2007_csv' executa a mesma operação de antes, mas desta vez o formato de destino é CSV (Valores Separados por Vírgula) em vez de XLSM.

Etapas: Converter PDF para CSV em Python

1. Criar uma instância de [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto com o documento PDF de origem.
1. Criar uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) com **ExcelSaveOptions.ExcelFormat.CSV**
1. Salve-o no formato **CSV** chamando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* método e passá-lo [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_csv(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.CSV
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para ODS

Etapas: Converter PDF para ODS em Python

1. Criar uma instância de [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto com o documento PDF de origem.
1. Criar uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) com **ExcelSaveOptions.ExcelFormat.ODS**
1. Salve no formato **ODS** chamando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método e passando-o [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

A conversão para o formato ODS é realizada da mesma forma que todos os outros formatos.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_ods(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.ODS
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Conversões relacionadas

- [Converter PDF para Word](/pdf/pt/python-net/convert-pdf-to-word/) se sua prioridade é fluxo de texto editável ao invés de estrutura de planilha.
- [Converter PDF para HTML](/pdf/pt/python-net/convert-pdf-to-html/) quando você precisa de saída compatível com navegador.
- [Converter PDF para outros formatos](/pdf/pt/python-net/convert-pdf-to-other-files/) para EPUB, Markdown, texto, XPS e fluxos de trabalho de exportação relacionados.
