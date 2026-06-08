---
title: Convertir PDF a Excel en Python
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: /es/python-net/convert-pdf-to-excel/
lastmod: "2026-06-05"
description: Aprenda cómo convertir PDF a Excel en Python, incluyendo XLS, XLSX, CSV, ODS, salida de una sola hoja de cálculo y manejo de columnas con Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convierta PDF a Excel, XLSX, CSV y ODS en Python
Abstract: Este artículo muestra cómo convertir archivos PDF a formatos de hoja de cálculo con Aspose.PDF for Python via .NET. Cubre la salida XLS, XLSX, XLSM, CSV y ODS, además de opciones para controlar columnas en blanco y reducir el número de hojas de cálculo generadas.
---

## Convertir PDF a Excel en Python

**Aspose.PDF for Python via .NET** soporta la conversión de archivos PDF a Excel y otros formatos de hoja de cálculo desde código Python.

Utilice esta página cuando necesite convertir un PDF a XLS, XLSX, CSV u ODS para extracción de tablas, reutilización de informes, ordenación, filtrado o análisis posterior. Durante la conversión de PDF a Excel, las páginas individuales del PDF pueden renderizarse como hojas de cálculo de Excel.

El primer ejemplo convierte un archivo PDF al formato XML de Spreadsheet 2003. Las secciones posteriores muestran XLSX, XLSM, CSV, ODS y salida de una sola hoja de cálculo.

{{% alert color="success" %}}
**Intenta convertir PDF a Excel en línea**

Aspose.PDF le presenta una aplicación en línea ["PDF a XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de PDF a Excel con la App de Aspose.PDF](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

El siguiente fragmento de código muestra el proceso para convertir un archivo PDF a formato XLS o XLSX con Aspose.PDF for Python via .NET.

Pasos: Convertir un archivo PDF al formato Excel (XML Spreadsheet 2003)

1. Cargar el documento PDF.
1. Configurar opciones de guardado de Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Guarda el archivo convertido.

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

## Convertir PDF a XLSX en Python

Pasos: Convertir un archivo PDF al formato XLSX (Excel 2007+)

1. Cargar el documento PDF.
1. Configurar opciones de guardado de Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Guarda el archivo convertido.

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

## Convertir PDF a XLSX con control de columnas

Al convertir un PDF a un formato Excel, se puede añadir una columna en blanco como la primera columna en el archivo de salida. Use el `insert_blank_column_at_first` opción del `ExcelSaveOptions` clase para controlar este comportamiento. Su valor predeterminado es `true`.

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

## Convertir PDF a una sola hoja de Excel

Aspose.PDF for Python via .NET muestra cómo convertir un PDF a un archivo Excel (.xlsx), con la opción 'minimize_the_number_of_worksheets' habilitada.

Pasos: Convertir PDF a XLS o XLSX en una sola hoja de cálculo en Python

1. Cargar el documento PDF.
1. Configurar opciones de guardado de Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. La opción 'minimize_the_number_of_worksheets' reduce el número de hojas de Excel al combinar páginas PDF en menos hojas de cálculo (p.ej., una hoja de cálculo para todo el documento si es posible).
1. Guarda el archivo convertido.

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

## Convertir PDF a Excel 2007 con macros (XLSM)

Este ejemplo de Python muestra cómo convertir un archivo PDF en un archivo de Excel en formato XLSM (Libro de Excel con macros habilitadas).

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

## Convertir a otros formatos de hoja de cálculo

### Convertir PDF a CSV

La función 'convert_pdf_to_excel_2007_csv' realiza la misma operación que antes, pero esta vez el formato de destino es CSV (Valores Separados por Comas) en lugar de XLSM.

Pasos: Convertir PDF a CSV en Python

1. Crear una instancia de [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto con el documento PDF de origen.
1. Crear una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) con **ExcelSaveOptions.ExcelFormat.CSV**
1. Guárdalo en formato **CSV** llamando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* método y pasándolo [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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

### Convertir PDF a ODS

Pasos: Convertir PDF a ODS en Python

1. Crear una instancia de [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto con el documento PDF de origen.
1. Crear una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) con **ExcelSaveOptions.ExcelFormat.ODS**
1. Guárdalo en formato **ODS** llamando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método y pasándolo [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

La conversión al formato ODS se realiza de la misma manera que todos los demás formatos.

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

## Conversiones relacionadas

- [Convertir PDF a Word](/pdf/es/python-net/convert-pdf-to-word/) si tu prioridad es el flujo de texto editable en lugar de la estructura de la hoja de cálculo.
- [Convertir PDF a HTML](/pdf/es/python-net/convert-pdf-to-html/) cuando necesites una salida amigable para el navegador.
- [Convertir PDF a otros formatos](/pdf/es/python-net/convert-pdf-to-other-files/) para EPUB, Markdown, texto, XPS y flujos de trabajo de exportación relacionados.
