---
title: Converter PDF para Excel em Python
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /pt/python-net/convert-pdf-to-excel/
lastmod: "2025-09-27"
description: Converta PDFs para planilhas Excel sem esforço com Aspose.PDF para Python via .NET. Siga este guia para conversões precisas de PDF para XLSX
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Converter PDF para Excel em Python
Abstract: Este artigo fornece um guia abrangente sobre como converter arquivos PDF para diversos formatos Excel usando Python, especificamente com a biblioteca Aspose.PDF para Python via .NET. Detalha os processos de conversão para os formatos XLS, XLSX, CSV e ODS. O documento explica as etapas necessárias para converter PDF para XLS e XLSX, destacando a criação de instâncias de Document e ExcelSaveOptions, e o uso do método Document.Save() para especificar os formatos de saída. O artigo também discute recursos como controlar a inserção de colunas em branco e minimizar o número de planilhas durante a conversão. Além disso, fornece exemplos de conversão de PDFs para planilhas Excel únicas e outros formatos como CSV e ODS, enfatizando a flexibilidade e funcionalidade do Aspose.PDF. Uma ferramenta online para conversão de PDF para XLSX também é mencionada, permitindo que os usuários explorem a qualidade da conversão. O artigo conclui com uma lista de tópicos relacionados e trechos de código para auxiliar ainda mais na compreensão e implementação dessas conversões programaticamente.
---

## Conversão de PDF para EXCEL via Python

**Aspose.PDF para Python via .NET** suporta o recurso de converter arquivos PDF para Excel e formatos CSV.

Aspose.PDF para Python via .NET é um componente de manipulação de PDF, introduzimos um recurso que renderiza arquivos PDF para um workbook Excel (arquivos XLSX). Durante essa conversão, as páginas individuais do arquivo PDF são convertidas em planilhas Excel.

{{% alert color="success" %}}
**Experimente converter PDF para Excel online**

Aspose.PDF apresenta a você um aplicativo gratuito online ["PDF para XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), onde você pode experimentar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF PDF para Excel com App Gratuito](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

O trecho de código a seguir mostra o processo de conversão de um arquivo PDF para o formato XLS ou XLSX com Aspose.PDF para Python via .NET.

Etapas: Converter um arquivo PDF para o formato Excel (Planilha XML 2003)

1. Carregue o documento PDF.
1. Configure as opções de salvamento do Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Salve o arquivo convertido.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

Etapas: Converter um arquivo PDF para o formato XLSX (Excel 2007+)

1. Carregue o documento PDF.
1. Configure as opções de salvamento do Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Salve o arquivo convertido.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Converter PDF para XLS com Controle de Coluna

Ao converter um PDF para o formato XLS, uma coluna em branco é adicionada ao arquivo de saída como primeira coluna. Na classe 'ExcelSaveOptions', a opção 'insert_blank_column_at_first' é usada para controlar essa coluna. Seu valor padrão é verdadeiro.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Converter PDF para Planilha Excel Única

Aspose.PDF para Python via .NET demonstra como converter um PDF para um arquivo Excel (.xlsx), com a opção 'minimize_the_number_of_worksheets' habilitada.

Etapas: Converter PDF para XLS ou XLSX em Planilha Única no Python

1. Carregue o documento PDF.
1. Configure as opções de salvamento do Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. A opção 'minimize_the_number_of_worksheets' reduz o número de planilhas Excel ao combinar páginas PDF em menos planilhas (por exemplo, uma única planilha para todo o documento, se possível).
1. Salve o arquivo convertido.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Converter arquivo PDF para um arquivo Excel no formato XLSM

Este exemplo em Python mostra como converter um arquivo PDF para um arquivo Excel no formato XLSM (Pasta de Trabalho Excel com Macro).

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## Converter para outros formatos de planilha

### Converter para CSV

A função 'convert_pdf_to_excel_2007_csv' realiza a mesma operação de antes, mas desta vez o formato alvo é CSV (Valores Separados por Vírgula) em vez de XLSM.

Etapas: Converter PDF para CSV em Python

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o documento PDF de origem.
1. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) com **ExcelSaveOptions.ExcelFormat.CSV**
1. Salve-o no formato **CSV** chamando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* e passando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

from os import path
import aspose.pdf as apdf

def convert_pdf_to_excel_2007_csv(infile, outfile):
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter para ODS

Etapas: Converter PDF para ODS em Python

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o documento PDF de origem.
1. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) com **ExcelSaveOptions.ExcelFormat.ODS**
1. Salve-o no formato **ODS** chamando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) e passando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

A conversão para o formato ODS é realizada da mesma forma que todos os outros formatos.

```python

    from os import path
    import aspose.pdf as apdf
    
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.ODS
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

