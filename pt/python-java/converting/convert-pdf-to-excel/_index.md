---
title: Converter PDF para Excel em Python
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /pt/python-java/convert-pdf-to-excel/
lastmod: "2022-12-23"
description: A biblioteca Aspose.PDF para Python permite converter PDF para o formato Excel usando Python. Esses formatos incluem XLS, XLSX, Planilha XML 2003, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Visão Geral

Este artigo explica como **converter PDF em formatos Excel usando Python**. Ele cobre os seguintes tópicos.

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

Aspose.PDF para Python via Java é um componente de manipulação de PDF, introduzimos um recurso que renderiza o arquivo PDF para uma planilha Excel (arquivos XLSX). Durante essa conversão, as páginas individuais do arquivo PDF são convertidas em planilhas Excel.

{{% alert color="success" %}}
**Tente converter PDF para Excel online**

Aspose.PDF apresenta a você o aplicativo online gratuito ["PDF para XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Converção PDF para Excel com Aplicativo Gratuito](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

O trecho de código a seguir mostra o processo para converter um arquivo PDF em formato XLS ou XLSX com Aspose.PDF para Python via Java.

<a name="python-pdf-to-xls"><strong>Passos: Converter PDF para XLS em Python</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) com o documento PDF de origem.
2. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. Salve no formato **XLS** especificando a **extensão .xls** chamando o método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) e passando para ele [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python



from asposepdf import Api


# init license
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# conversão a partir de array de bytes
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result1.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)

# conversão a partir de arquivo
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result2.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)


# conversão a partir de array de bytes
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result3.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)

# conversão a partir de arquivo
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result4.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)
```


<a name="python-pdf-to-xlsx"><strong>Passos: Converter PDF para XLSX em Python</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) com o documento PDF de origem.
2. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. Salve no formato **XLSX** especificando a **extensão .xlsx** chamando o método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) e passando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
doc.save(documentOutName, save_option)
```

## Converter PDF para XLS com controle de Coluna

Ao converter um PDF para o formato XLS, uma coluna em branco é adicionada ao arquivo de saída como a primeira coluna.
 O uso da opção InsertBlankColumnAtFirst na 'classe ExcelSaveOptions' é para controlar esta coluna. Seu valor padrão é verdadeiro.

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._insertBlankColumnAtFirst = True
doc.save(documentOutName, save_option)

```

## Converter PDF para uma Única Planilha do Excel

Ao exportar um arquivo PDF com muitas páginas para XLS, cada página é exportada para uma folha diferente no arquivo Excel. Isso ocorre porque a propriedade MinimizeTheNumberOfWorksheets está definida como falso por padrão. Para garantir que todas as páginas sejam exportadas para uma única folha no arquivo Excel de saída, defina a propriedade MinimizeTheNumberOfWorksheets como verdadeira.

<a name="python-pdf-to-excel-single"><strong>Passos: Converter PDF para XLS ou XLSX em Única Planilha no Python</strong></a>
1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) com o documento PDF de origem.
2. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) com **MinimizeTheNumberOfWorksheets = True**.
3. Salve no formato **XLS** ou **XLSX** com uma única planilha chamando o método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) e passando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._minimizeTheNumberOfWorksheets = True
# Salve o arquivo no formato MS Excel
doc.save(documentOutName, save_option)

```

## Converter para outros formatos de planilha


### Converter para CSV

Conversão para o formato CSV é realizada da mesma forma que acima. Tudo o que você precisa - definir o formato apropriado.

<a name="python-pdf-to-csv"><strong>Passos: Converter PDF para CSV em Python</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o documento PDF de origem.
2. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) com **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. Salve no formato **CSV** chamando o método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods)* e passando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.csv"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.CSV
doc.save(documentOutName, save_option)
```


### Converter para ODS

<a name="python-pdf-to-ods"><strong>Passos: Converter PDF para ODS em Python</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o documento PDF de origem.
2. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) com **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Salve no formato **ODS** chamando o método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) e passando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

A conversão para o formato ODS é realizada da mesma forma que todos os outros formatos.

```python

from asposepdf import Api

documentName = "../../testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "../../testout/result1.ods"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.ODS
doc.save(documentOutName, save_option)
```


## Veja Também

Este artigo também cobre esses tópicos. Os códigos são os mesmos que acima.

_Formato_: **Excel**
- [Código Python PDF para Excel](#python-pdf-to-xlsx)
- [API Python PDF para Excel](#python-pdf-to-xlsx)
- [Programação Python PDF para Excel](#python-pdf-to-xlsx)
- [Biblioteca Python PDF para Excel](#python-pdf-to-xlsx)
- [Salvar PDF como Excel em Python](#python-pdf-to-xlsx)
- [Gerar Excel a partir de PDF em Python](#python-pdf-to-xlsx)
- [Criar Excel a partir de PDF em Python](#python-pdf-to-xlsx)
- [Conversor de PDF para Excel em Python](#python-pdf-to-xlsx)

_Formato_: **XLS**
- [Código Python PDF para XLS](#python-pdf-to-xls)
- [API Python PDF para XLS](#python-pdf-to-xls)
- [Programação Python PDF para XLS](#python-pdf-to-xls)
- [Biblioteca Python PDF para XLS](#python-pdf-to-xls)
- [Salvar PDF como XLS em Python](#python-pdf-to-xls)
- [Gerar XLS a partir de PDF em Python](#python-pdf-to-xls)
- [Criar XLS a partir de PDF em Python](#python-pdf-to-xls)
- [Conversor de PDF para XLS em Python](#python-pdf-to-xls)

_Formato_: **XLSX**

- [Código Python PDF para XLSX](#python-pdf-to-xlsx)
- [API Python PDF para XLSX](#python-pdf-to-xlsx)
- [Programar Python PDF para XLSX](#python-pdf-to-xlsx)
- [Biblioteca Python PDF para XLSX](#python-pdf-to-xlsx)
- [Salvar PDF como XLSX em Python](#python-pdf-to-xlsx)
- [Gerar XLSX a partir de PDF em Python](#python-pdf-to-xlsx)
- [Criar XLSX a partir de PDF em Python](#python-pdf-to-xlsx)
- [Conversor de PDF para XLSX em Python](#python-pdf-to-xlsx)

_Formato_: **CSV**
- [Código Python PDF para CSV](#python-pdf-to-csv)
- [API Python PDF para CSV](#python-pdf-to-csv)
- [Programar Python PDF para CSV](#python-pdf-to-csv)
- [Biblioteca Python PDF para CSV](#python-pdf-to-csv)
- [Salvar PDF como CSV em Python](#python-pdf-to-csv)
- [Gerar CSV a partir de PDF em Python](#python-pdf-to-csv)
- [Criar CSV a partir de PDF em Python](#python-pdf-to-csv)
- [Conversor de PDF para CSV em Python](#python-pdf-to-csv)

_Formato_: **ODS**
- [Código Python PDF para ODS](#python-pdf-to-ods)
- [API Python PDF para ODS](#python-pdf-to-ods)
- [Programar Python PDF para ODS](#python-pdf-to-ods)
- [Biblioteca Python PDF para ODS](#python-pdf-to-ods)

- [Salvar PDF como ODS em Python](#python-pdf-to-ods)
- [Python Gerar ODS de PDF](#python-pdf-to-ods)
- [Python Criar ODS de PDF](#python-pdf-to-ods)
- [Conversor de PDF para ODS em Python](#python-pdf-to-ods)