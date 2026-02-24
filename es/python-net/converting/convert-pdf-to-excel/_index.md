---
title: Convertir PDF a Excel en Python
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: /es/python-net/convert-pdf-to-excel/
lastmod: "2025-09-27"
description: Convierta PDFs a hojas de cálculo de Excel sin esfuerzo con Aspose.PDF para Python a través de .NET. Siga esta guía para conversiones precisas de PDF a XLSX.
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a Excel en Python
Abstract: Este artículo ofrece una guía completa sobre la conversión de archivos PDF a varios formatos de Excel usando Python, específicamente con la biblioteca Aspose.PDF para Python a través de .NET. Detalla los procesos de conversión a los formatos XLS, XLSX, CSV y ODS. El documento explica los pasos necesarios para convertir PDF a XLS y XLSX, resaltando la creación de instancias de Document y ExcelSaveOptions, y el uso del método Document.Save() para especificar los formatos de salida. El artículo también analiza características como el control de la inserción de columnas en blanco y la minimización del número de hojas de cálculo durante la conversión. Además, proporciona ejemplos de conversión de PDFs a una sola hoja de cálculo de Excel y a otros formatos como CSV y ODS, enfatizando la flexibilidad y funcionalidad de Aspose.PDF. También se menciona una herramienta en línea para la conversión de PDF a XLSX, que permite a los usuarios explorar la calidad de la conversión. El artículo concluye con una lista de temas relacionados y fragmentos de código para ayudar aún más a comprender e implementar estas conversiones programáticamente.
---

## Conversión de PDF a EXCEL mediante Python

**Aspose.PDF for Python via .NET** soporta la función de convertir archivos PDF a formatos Excel y CSV.

Aspose.PDF for Python via .NET es un componente de manipulación de PDF, hemos introducido una función que renderiza archivos PDF a libros de Excel (archivos XLSX). Durante esta conversión, las páginas individuales del archivo PDF se convierten en hojas de Excel.

{{% alert color="success" %}}
**Pruebe convertir PDF a Excel en línea**

Aspose.PDF le presenta una aplicación gratuita en línea ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puede probar e investigar la funcionalidad y la calidad de su funcionamiento.

[![Conversión de Aspose.PDF PDF a Excel con Aplicación Gratis](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

El siguiente fragmento de código muestra el proceso para convertir un archivo PDF a formato XLS o XLSX con Aspose.PDF for Python via .NET.

Pasos: Convertir un archivo PDF a formato Excel (XML Spreadsheet 2003)

1. Cargue el documento PDF.
1. Configure las opciones de guardado de Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
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

Pasos: Convertir un archivo PDF a formato XLSX (Excel 2007+)

1. Cargue el documento PDF.
1. Configure las opciones de guardado de Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
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

## Convertir PDF a XLS con control de columna

Al convertir un PDF a formato XLS, se agrega una columna en blanco al archivo de salida como primera columna. En la clase 'ExcelSaveOptions', la opción 'insert_blank_column_at_first' se utiliza para controlar esta columna. Su valor predeterminado es true.

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

Pasos: Convertir PDF a una sola hoja XLS o XLSX en Python

1. Cargue el documento PDF.
1. Configure las opciones de guardado de Excel usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. La opción 'minimize_the_number_of_worksheets' reduce el número de hojas de Excel combinando las páginas del PDF en menos hojas de cálculo (por ejemplo, una hoja para todo el documento si es posible).
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

## Convertir archivo PDF a un archivo Excel en formato XLSM

Este ejemplo en Python muestra cómo convertir un archivo PDF a un archivo Excel en formato XLSM (Libro de Excel con macros habilitadas).

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

La función 'convert_pdf_to_excel_2007_csv' realiza la misma operación que antes, pero esta vez el formato de destino es CSV (Valores separados por comas) en lugar de XLSM.

Pasos: Convertir PDF a CSV en Python

1. Cree una instancia del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el documento PDF de origen.
1. Cree una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) con **ExcelSaveOptions.ExcelFormat.CSV**
1. Guárdelo en formato **CSV** llamando al método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* y pasando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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

1. Crea una instancia del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el documento PDF de origen.
1. Crea una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) con **ExcelSaveOptions.ExcelFormat.ODS**
1. Guárdalo en formato **ODS** llamando al método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) y pasando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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

