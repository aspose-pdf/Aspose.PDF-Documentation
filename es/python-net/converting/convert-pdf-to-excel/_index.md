---
title: Convertir PDF a Excel en Python
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: /es/python-net/convert-pdf-to-excel/
lastmod: "2025-09-27"
description: Convierta PDFs a hojas de cálculo de Excel sin esfuerzo con Aspose.PDF for Python via .NET. Siga esta guía para conversiones precisas de PDF a XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Convertir PDF a Excel y hojas de cálculo
Abstract: >
    Esta página explica cómo convertir PDF a XLS, XLSX, CSV y ODS con Aspose.PDF for Python via .NET. También muestra opciones para controlar columnas vacías, combinar datos en menos hojas y ajustar la salida de Excel según el contenido del PDF.
---

## Conversión de PDF a EXCEL mediante Python

**Aspose.PDF for Python via .NET** admite la función de convertir archivos PDF a formatos Excel y CSV.

Aspose.PDF for Python via .NET es un componente de manipulación de PDF, hemos introducido una función que convierte archivos PDF a libros de Excel (archivos XLSX). Durante esta conversión, las páginas individuales del archivo PDF se convierten en hojas de Excel.

{{% alert color="success" %}}
**Intenta convertir PDF a Excel en línea**

Aspose.PDF te presenta una aplicación en línea gratuita ["PDF a XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a Excel con aplicación gratuita](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

El siguiente fragmento de código muestra el proceso para convertir un archivo PDF a formato XLS o XLSX con Aspose.PDF for Python via .NET.

Pasos: Convertir un archivo PDF a formato Excel (XML Spreadsheet 2003)

1. Cargar el documento PDF.
1. Configurar opciones de guardado de Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Guarda el archivo convertido.

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

Pasos: Convertir un archivo PDF a formato XLSX (Excel 2007+)

1. Cargar el documento PDF.
1. Configurar opciones de guardado de Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Guarda el archivo convertido.

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

## Convertir PDF a XLS con columna de control

Al convertir un PDF al formato XLS, se agrega una columna en blanco al archivo de salida como primera columna. La \u0027ExcelSaveOptions class\u0027 \u0027insert_blank_column_at_first\u0027 opción se usa para controlar esta columna. Su valor predeterminado es true.

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

## Convertir PDF a una única hoja de Excel

Aspose.PDF for Python via .NET muestra cómo convertir un PDF a un archivo Excel (.xlsx), con la opción ‘minimize_the_number_of_worksheets’ habilitada.

Pasos: Convertir PDF a XLS o XLSX en una hoja única con Python

1. Cargar el documento PDF.
1. Configurar opciones de guardado de Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. La opción 'minimize_the_number_of_worksheets' reduce el número de hojas de Excel combinando páginas PDF en menos hojas de cálculo (p. ej., una hoja de cálculo para todo el documento si es posible).
1. Guarda el archivo convertido.

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

## Convertir archivo PDF a un archivo Excel en formato XLSM

Este ejemplo de Python muestra cómo convertir un archivo PDF en un archivo Excel en formato XLSM (Libro de Excel con macros habilitadas).

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

## Convertir a otros formatos de hoja de cálculo

### Convertir a CSV

La función 'convert_pdf_to_excel_2007_csv' realiza la misma operación que antes, pero esta vez el formato de destino es CSV (Valores Separados por Comas) en lugar de XLSM.

Pasos: Convertir PDF a CSV en Python

1. Crear una instancia de [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto con el documento PDF de origen.
1. Crear una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) con **ExcelSaveOptions.ExcelFormat.CSV**
1. Guárdalo en formato **CSV** llamando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* método y pasándolo [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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

### Convertir a ODS

Pasos: Convertir PDF a ODS en Python

1. Crear una instancia de [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto con el documento PDF de origen.
1. Crear una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) con **ExcelSaveOptions.ExcelFormat.ODS**
1. Guárdalo en formato **ODS** llamando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método y pasándolo [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

La conversión al formato ODS se realiza de la misma manera que los demás formatos.

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
