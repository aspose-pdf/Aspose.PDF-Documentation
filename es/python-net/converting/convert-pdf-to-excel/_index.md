---
title: Convertir PDF a Excel en Python
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: /es/python-net/convert-pdf-to-excel/
lastmod: "2022-12-23"
description: La biblioteca Aspose.PDF para Python te permite convertir PDF a formato Excel usando Python. Estos formatos incluyen XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Resumen

Este artículo explica cómo **convertir PDF a formatos Excel usando Python**. Cubre los siguientes temas.

_Formato_: **XLS**

- [Python PDF a XLS](#python-pdf-to-xls)
- [Python Convertir PDF a XLS](#python-pdf-to-xls)
- [Python Cómo convertir archivo PDF a XLS](#python-pdf-to-xls)

_Formato_: **XLSX**

- [Python PDF a XLSX](#python-pdf-to-xlsx)
- [Python Convertir PDF a XLSX](#python-pdf-to-xlsx)
- [Python Cómo convertir archivo PDF a XLSX](#python-pdf-to-xlsx)


_Formato_: **Excel**

- [Python PDF a Excel](#python-pdf-to-xlsx)
- [Python PDF a Excel XLS](#python-pdf-to-xls)
- [Python PDF a Excel XLSX](#python-pdf-to-xlsx)

_Formato_: **CSV**

- [Python PDF a CSV](#python-pdf-to-csv)
- [Python Convertir PDF a CSV](#python-pdf-to-csv)
- [Python Cómo convertir archivo PDF a CSV](#python-pdf-to-csv)

_Formato_: **ODS**

- [Python PDF a ODS](#python-pdf-to-ods)
- [Python Convertir PDF a ODS](#python-pdf-to-ods)
- [Python Cómo convertir archivo PDF a ODS](#python-pdf-to-ods)

## Conversión de PDF a EXCEL mediante Python

**Aspose.PDF para Python a través de .NET** soporta la función de convertir archivos PDF a formatos Excel y CSV.

Aspose.PDF para Python a través de .NET es un componente de manipulación de PDF, hemos introducido una función que convierte el archivo PDF a un libro de Excel (archivos XLSX). Durante esta conversión, las páginas individuales del archivo PDF se convierten en hojas de cálculo de Excel.

{{% alert color="success" %}}
**Intenta convertir PDF a Excel en línea**

Aspose.PDF te presenta la aplicación gratuita en línea ["PDF a XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

El siguiente fragmento de código muestra el proceso para convertir un archivo PDF al formato XLS o XLSX con Aspose.PDF para Python a través de .NET.

<a name="python-pdf-to-xls"><strong>Pasos: Convertir PDF a XLS en Python</strong></a>

1. Cree una instancia del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el documento PDF de origen.
2. Cree una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
3. Guárdelo en formato **XLS** especificando la **extensión .xls** llamando al método [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) y pasándole [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xls.xls"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003

    # Guardar el archivo en formato MS Excel
    document.save(output_pdf, save_option)
```


<a name="python-pdf-to-xlsx"><strong>Pasos: Convertir PDF a XLSX en Python</strong></a>

1. Cree una instancia del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el documento PDF de origen.
2. Cree una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
3. Guárdelo en formato **XLSX** especificando la **extensión .xlsx** llamando al método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) y pasándole [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_xlsx.xlsx"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()

    # Guardar el archivo en formato MS Excel
    document.save(output_pdf, save_option)
```

## Convertir PDF a XLS con control de Columna

Al convertir un PDF a formato XLS, se añade una columna en blanco al archivo de salida como primera columna.
 La opción InsertBlankColumnAtFirst en la clase 'ExcelSaveOptions' se utiliza para controlar esta columna. Su valor predeterminado es verdadero.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_with_control_column.xls"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.insert_blank_column_at_first = True

    # Guardar el archivo en formato MS Excel
    document.save(output_pdf, save_option)
```

## Convertir PDF a una sola hoja de cálculo de Excel

Al exportar un archivo PDF con muchas páginas a XLS, cada página se exporta a una hoja diferente en el archivo Excel. Esto se debe a que la propiedad MinimizeTheNumberOfWorksheets está configurada como falsa por defecto. Para asegurarse de que todas las páginas se exporten a una sola hoja en el archivo Excel de salida, configure la propiedad MinimizeTheNumberOfWorksheets como verdadera.

<a name="python-pdf-to-excel-single"><strong>Pasos: Convertir PDF a una sola hoja de cálculo XLS o XLSX en Python</strong></a>
1. Crear una instancia del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el documento PDF de origen.
2. Crear una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) con **MinimizeTheNumberOfWorksheets = true**.
3. Guardarlo en formato **XLS** o **XLSX** teniendo una sola hoja de cálculo llamando al método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) y pasándole [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_single_excel_worksheet.xls"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.minimize_the_number_of_worksheets = True

    # Guardar el archivo en formato MS Excel
    document.save(output_pdf, save_option)

```


## Convertir a otros formatos de hoja de cálculo

### Convertir a CSV

La conversión al formato CSV se realiza de la misma manera que arriba. Todo lo que necesitas es establecer el formato apropiado.

<a name="python-pdf-to-csv"><strong>Pasos: Convertir PDF a CSV en Python</strong></a>

1. Crea una instancia del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el documento PDF de origen.
2. Crea una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) con **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. Guárdalo en formato **CSV** llamando al método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) y pasándole [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_csv.csv"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.CSV

    # Guardar el archivo
    document.save(output_pdf, save_option)
```


### Convertir a ODS

<a name="python-pdf-to-ods"><strong>Pasos: Convertir PDF a ODS en Python</strong></a>

1. Crear una instancia del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el documento PDF de origen.
2. Crear una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) con **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Guardarlo en formato **ODS** llamando al método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) y pasándole [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

La conversión al formato ODS se realiza de la misma manera que todos los demás formatos.

```python

    import aspose.pdf as ap
    
    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_ods.ods"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.ODS

    # Guardar el archivo
    document.save(output_pdf, save_option)
```


## Ver También

Este artículo también cubre estos temas. Los códigos son los mismos que arriba.

_Formato_: **Excel**
- [Código Python PDF a Excel](#python-pdf-to-xlsx)
- [API Python PDF a Excel](#python-pdf-to-xlsx)
- [Python PDF a Excel Programáticamente](#python-pdf-to-xlsx)
- [Biblioteca Python PDF a Excel](#python-pdf-to-xlsx)
- [Guardar PDF como Excel en Python](#python-pdf-to-xlsx)
- [Generar Excel desde PDF en Python](#python-pdf-to-xlsx)
- [Crear Excel desde PDF en Python](#python-pdf-to-xlsx)
- [Convertidor de PDF a Excel en Python](#python-pdf-to-xlsx)

_Formato_: **XLS**
- [Código Python PDF a XLS](#python-pdf-to-xls)
- [API Python PDF a XLS](#python-pdf-to-xls)
- [Python PDF a XLS Programáticamente](#python-pdf-to-xls)
- [Biblioteca Python PDF a XLS](#python-pdf-to-xls)
- [Guardar PDF como XLS en Python](#python-pdf-to-xls)
- [Generar XLS desde PDF en Python](#python-pdf-to-xls)
- [Crear XLS desde PDF en Python](#python-pdf-to-xls)
- [Convertidor de PDF a XLS en Python](#python-pdf-to-xls)

_Formato_: **XLSX**

- [Código Python PDF a XLSX](#python-pdf-to-xlsx)
- [Python PDF a XLSX API](#python-pdf-to-xlsx)
- [Python PDF a XLSX Programáticamente](#python-pdf-to-xlsx)
- [Python PDF a XLSX Biblioteca](#python-pdf-to-xlsx)
- [Python Guardar PDF como XLSX](#python-pdf-to-xlsx)
- [Python Generar XLSX desde PDF](#python-pdf-to-xlsx)
- [Python Crear XLSX desde PDF](#python-pdf-to-xlsx)
- [Python PDF a XLSX Convertidor](#python-pdf-to-xlsx)

_Formato_: **CSV**
- [Python PDF a CSV Código](#python-pdf-to-csv)
- [Python PDF a CSV API](#python-pdf-to-csv)
- [Python PDF a CSV Programáticamente](#python-pdf-to-csv)
- [Python PDF a CSV Biblioteca](#python-pdf-to-csv)
- [Python Guardar PDF como CSV](#python-pdf-to-csv)
- [Python Generar CSV desde PDF](#python-pdf-to-csv)
- [Python Crear CSV desde PDF](#python-pdf-to-csv)
- [Python PDF a CSV Convertidor](#python-pdf-to-csv)

_Formato_: **ODS**
- [Python PDF a ODS Código](#python-pdf-to-ods)
- [Python PDF a ODS API](#python-pdf-to-ods)
- [Python PDF a ODS Programáticamente](#python-pdf-to-ods)
- [Python PDF a ODS Biblioteca](#python-pdf-to-ods)

- [Python Guardar PDF como ODS](#python-pdf-to-ods)
- [Python Generar ODS desde PDF](#python-pdf-to-ods)
- [Python Crear ODS desde PDF](#python-pdf-to-ods)
- [Python Convertidor de PDF a ODS](#python-pdf-to-ods)