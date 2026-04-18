---
title: Convertir PDF a Excel en Python
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: /es/python-net/convert-pdf-to-excel/
lastmod: "2026-04-14"
description: Aprenda cómo convertir archivos PDF a Excel en Python con Aspose.PDF for Python via .NET, incluyendo XLS, XLSX, CSV, ODS y salida de una sola hoja.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Cómo convertir PDF a Excel en Python
Abstract: Este artículo ofrece una guía completa sobre la conversión de archivos PDF a varios formatos de Excel usando Python, específicamente con la biblioteca Aspose.PDF for Python via .NET. Detalla los procesos de conversión a los formatos XLS, XLSX, CSV y ODS. El documento explica los pasos necesarios para convertir PDF a XLS y XLSX, resaltando la creación de instancias de Document y ExcelSaveOptions, y el uso del método Document.Save() para especificar los formatos de salida. El artículo también discute características como controlar la inserción de columnas en blanco y minimizar el número de hojas de cálculo durante la conversión. Además, brinda ejemplos de conversión de PDFs a hojas de cálculo Excel individuales y a otros formatos como CSV y ODS, enfatizando la flexibilidad y funcionalidad de Aspose.PDF. También se menciona una herramienta en línea para la conversión de PDF a XLSX, que permite a los usuarios explorar la calidad de la conversión. El artículo concluye con una lista de temas relacionados y fragmentos de código para ayudar aún más a comprender e implementar estas conversiones programáticamente.
---

## Conversión de PDF a EXCEL mediante Python

**Aspose.PDF for Python via .NET** admite la funcionalidad de convertir archivos PDF a los formatos Excel y CSV.

Aspose.PDF for Python via .NET es un componente de manipulación de PDF, hemos introducido una característica que renderiza archivos PDF a un libro de Excel (archivos XLSX). Durante esta conversión, las páginas individuales del archivo PDF se convierten en hojas de cálculo de Excel.

Utilice esta página cuando necesite extraer contenido de PDF orientado a tablas o con estilo de informe a formatos de hoja de cálculo para ordenar, filtrar o realizar análisis posteriores.

{{% alert color="success" %}}
**Intenta convertir PDF a Excel en línea**

Aspose.PDF le presenta su aplicación en línea gratuita ["PDF a XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a Excel con la aplicación gratuita](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

El siguiente fragmento de código muestra el proceso de conversión de un archivo PDF al formato XLS o XLSX con Aspose.PDF for Python via .NET.

Pasos: Convertir un archivo PDF a formato Excel (XML Spreadsheet 2003)

1. Cargue el documento PDF.
1. Configurar opciones de guardado de Excel usando [OpcionesDeGuardadoExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Guarde el archivo convertido.

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

## Conversiones relacionadas

- [Convertir PDF a Word](/pdf/es/python-net/convert-pdf-to-word/) si tu prioridad es el flujo de texto editable en lugar de la estructura de la hoja de cálculo.
- [Convertir PDF a HTML](/pdf/es/python-net/convert-pdf-to-html/) cuando necesites una salida compatible con el navegador.
- [Convertir PDF a otros formatos](/pdf/es/python-net/convert-pdf-to-other-files/) para EPUB, Markdown, texto, XPS y flujos de trabajo de exportación relacionados.

Pasos: Convertir un archivo PDF a formato XLSX (Excel 2007+)

1. Cargue el documento PDF.
1. Configurar opciones de guardado de Excel usando [OpcionesDeGuardadoExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Guarde el archivo convertido.

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

Al convertir un PDF a formato XLS, se agrega una columna en blanco al archivo de salida como primera columna. En la clase 'ExcelSaveOptions' la opción 'insert_blank_column_at_first' se usa para controlar esta columna. Su valor predeterminado es true.

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

## Convertir PDF a una sola hoja de Excel

Aspose.PDF for Python via .NET muestra cómo convertir un PDF a un archivo Excel (.xlsx), con la opción 'minimize_the_number_of_worksheets' habilitada.

Pasos: Convertir PDF a XLS o XLSX en una sola hoja de cálculo en Python

1. Cargue el documento PDF.
1. Configurar opciones de guardado de Excel usando [OpcionesDeGuardadoExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. La opción 'minimize_the_number_of_worksheets' reduce la cantidad de hojas de Excel combinando páginas PDF en menos hojas de cálculo (p.ej., una hoja de cálculo para todo el documento si es posible).
1. Guarde el archivo convertido.

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

## Convertir archivo PDF en un archivo Excel en formato XLSM

Este ejemplo en Python muestra cómo convertir un archivo PDF en un archivo Excel en formato XLSM (Libro de Excel con macros habilitadas).

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
1. Crear una instancia de [OpcionesDeGuardadoExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) con **ExcelSaveOptions.ExcelFormat.CSV**
1. Guárdalo en formato **CSV** llamando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* método y pasándolo [OpcionesDeGuardadoExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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
1. Crear una instancia de [OpcionesDeGuardadoExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) con **ExcelSaveOptions.ExcelFormat.ODS**
1. Guárdelo en formato **ODS** llamando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método y pasándolo [OpcionesDeGuardadoExcel](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

La conversión al formato ODS se realiza de la misma manera que todos los demás formatos.

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
