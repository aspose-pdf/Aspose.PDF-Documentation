---
title: Converter PDF para Excel em Python
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /pt/python-net/convert-pdf-to-excel/
lastmod: "2026-05-21"
description: Aprenda como converter arquivos PDF para Excel em Python com Aspose.PDF for Python via .NET, incluindo XLS, XLSX, CSV, ODS e saída de planilha única.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Converter PDF para Excel em Python
Abstract: Este artigo fornece um guia abrangente sobre a conversão de arquivos PDF para vários formatos Excel usando Python, especificamente com a biblioteca Aspose.PDF for Python via .NET. Ele detalha os processos de conversão para os formatos XLS, XLSX, CSV e ODS. O documento explica as etapas necessárias para converter PDF para XLS e XLSX, destacando a criação de instâncias Document e ExcelSaveOptions, e o uso do método Document.Save() para especificar os formatos de saída. O artigo também discute recursos como o controle da inserção de colunas em branco e a minimização do número de planilhas durante a conversão. Além disso, fornece exemplos de conversão de PDFs para planilhas Excel individuais e outros formatos como CSV e ODS, enfatizando a flexibilidade e funcionalidade do Aspose.PDF. Uma ferramenta online para conversão de PDF para XLSX também é mencionada, permitindo que os usuários explorem a qualidade da conversão. O artigo conclui com uma lista de tópicos relacionados e trechos de código para auxiliar ainda mais na compreensão e implementação dessas conversões programaticamente.
---

## Converter PDF para Excel (Spreadsheet 2003 XML)

**Aspose.PDF for Python via .NET** suporta o recurso de converter arquivos PDF para os formatos Excel e CSV.

Aspose.PDF for Python via .NET é um componente de manipulação de PDF, introduzimos um recurso que renderiza arquivos PDF para pasta de trabalho do Excel (arquivos XLSX). Durante essa conversão, as páginas individuais do arquivo PDF são convertidas em planilhas do Excel.

Use esta página quando precisar extrair conteúdo de PDF orientado a tabelas ou no estilo de relatório para formatos de planilha, a fim de ordenar, filtrar ou analisar posteriormente.

{{% alert color="success" %}}
**Tente converter PDF para Excel online**

Aspose.PDF apresenta a você um aplicativo online ["PDF para XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para Excel com App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

O trecho de código a seguir mostra o processo de conversão de arquivo PDF para formato XLS ou XLSX com Aspose.PDF for Python via .NET.

Etapas: Converter um arquivo PDF para o formato Excel (Planilha XML 2003)

1. Carregar o documento PDF.
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

## Converter PDF para Excel 2007+ (XLSX)

Etapas: Converter um arquivo PDF para o formato XLSX (Excel 2007+)

1. Carregar o documento PDF.
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

## Converter PDF para XLS com controle de coluna

Ao converter um PDF para o formato XLS, uma coluna em branco é adicionada ao arquivo de saída como primeira coluna. Na classe 'ExcelSaveOptions' a opção 'insert_blank_column_at_first' é usada para controlar essa coluna. Seu valor padrão é true.

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

Aspose.PDF for Python via .NET mostra como converter um PDF para um arquivo Excel (.xlsx), com a opção ‘minimize_the_number_of_worksheets’ ativada.

Passos: Converter PDF para XLS ou XLSX em uma única planilha no Python

1. Carregar o documento PDF.
1. Configurar opções de salvamento do Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. A opção 'minimize_the_number_of_worksheets' reduz o número de planilhas do Excel combinando páginas PDF em menos planilhas (por exemplo, uma única planilha para todo o documento, se possível).
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

Este exemplo em Python mostra como converter um arquivo PDF em um arquivo Excel no formato XLSM (Pasta de Trabalho com Macro do Excel).

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

A função 'convert_pdf_to_excel_2007_csv' realiza a mesma operação de antes, mas desta vez o formato de destino é CSV (Valores Separados por Vírgula) em vez de XLSM.

Etapas: Converter PDF para CSV em Python

1. Crie uma instância de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto com o documento PDF de origem.
1. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) com **ExcelSaveOptions.ExcelFormat.CSV**
1. Salve-o no formato **CSV** chamando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* método e passando isso [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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

1. Crie uma instância de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto com o documento PDF de origem.
1. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) com **ExcelSaveOptions.ExcelFormat.ODS**
1. Salve-o no formato **ODS** chamando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método e passando-o [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

A conversão para o formato ODS é feita da mesma forma que todos os outros formatos.

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

- [Converter PDF para Word](/pdf/pt/python-net/convert-pdf-to-word/) se a sua prioridade for fluxo de texto editável em vez de estrutura de planilha.
- [Converter PDF para HTML](/pdf/pt/python-net/convert-pdf-to-html/) quando você precisar de saída compatível com o navegador.
- [Converter PDF para outros formatos](/pdf/pt/python-net/convert-pdf-to-other-files/) para EPUB, Markdown, texto, XPS e fluxos de trabalho de exportação relacionados.