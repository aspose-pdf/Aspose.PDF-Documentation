---
title: Convertir PDF a Excel en Python
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: /es/python-java/convert-pdf-to-excel/
lastmod: "2022-12-23"
keywords: convertir PDF a Excel usando python, convertir PDF a XLS usando python, convertir PDF a XLSX usando python, exportar tabla de PDF a Excel en python.
description: La biblioteca Aspose.PDF para Python le permite convertir PDF al formato Excel usando Python. Estos formatos incluyen XLS, XLSX, Hoja de Cálculo XML 2003, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Descripción general

Este artículo explica cómo **convertir PDF a formatos de Excel usando Python**. Cubre los siguientes temas.

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

Aspose.PDF para Python a través de Java es un componente de manipulación de PDF, hemos introducido una función que convierte archivos PDF a libros de Excel (archivos XLSX). Durante esta conversión, las páginas individuales del archivo PDF se convierten en hojas de cálculo de Excel.

{{% alert color="success" %}}
**Intenta convertir PDF a Excel en línea**

Aspose.PDF te presenta una aplicación en línea gratuita ["PDF a XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

El siguiente fragmento de código muestra el proceso para convertir un archivo PDF en formato XLS o XLSX con Aspose.PDF para Python a través de Java.

<a name="python-pdf-to-xls"><strong>Pasos: Convertir PDF a XLS en Python</strong></a>

1. Crear una instancia del objeto [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) con el documento PDF de origen.
2. Crear una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. Guardarlo en formato **XLS** especificando la **extensión .xls** llamando al método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) y pasándole [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python
from asposepdf import Api

# inicializar licencia
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# conversión desde array de bytes
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result1.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)

# conversión desde archivo
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result2.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)

# conversión desde array de bytes
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result3.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)

# conversión desde archivo
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result4.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)
```


<a name="python-pdf-to-xlsx"><strong>Pasos: Convertir PDF a XLSX en Python</strong></a>

1. Crear una instancia del objeto [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) con el documento PDF de origen.
2. Crear una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. Guardarlo en formato **XLSX** especificando la **extensión .xlsx** llamando al método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) y pasándole [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
doc.save(documentOutName, save_option)
```

## Convertir PDF a XLS con control de Columna

Al convertir un PDF a formato XLS, se añade una columna en blanco al archivo de salida como primera columna.
 El uso de la opción InsertBlankColumnAtFirst en la 'clase ExcelSaveOptions' es para controlar esta columna. Su valor predeterminado es true.

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

## Convertir PDF a una sola hoja de cálculo de Excel

Al exportar un archivo PDF con muchas páginas a XLS, cada página se exporta a una hoja diferente en el archivo Excel. Esto se debe a que la propiedad MinimizeTheNumberOfWorksheets está configurada como false por defecto. Para asegurarse de que todas las páginas se exporten a una sola hoja en el archivo Excel de salida, configure la propiedad MinimizeTheNumberOfWorksheets como true.

<a name="python-pdf-to-excel-single"><strong>Pasos: Convertir PDF a una sola hoja de cálculo XLS o XLSX en Python</strong></a>
1. Cree una instancia del objeto [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) con el documento PDF de origen.
2. Cree una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) con **MinimizeTheNumberOfWorksheets = True**.
3. Guárdelo en formato **XLS** o **XLSX** teniendo una sola hoja de cálculo llamando al método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) y pasándole [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._minimizeTheNumberOfWorksheets = True
# Guardar el archivo en formato MS Excel
doc.save(documentOutName, save_option)

```

## Convertir a otros formatos de hoja de cálculo

### Convertir a CSV

La conversión al formato CSV se realiza de la misma manera que arriba. Todo lo que necesitas es establecer el formato adecuado.

<a name="python-pdf-to-csv"><strong>Pasos: Convertir PDF a CSV en Python</strong></a>

1. Crea una instancia del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el documento PDF de origen.
2. Crea una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) con **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. Guárdalo en formato **CSV** llamando al método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) y pasándolo [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).


```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.csv"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.CSV
doc.save(documentOutName, save_option)
```


### Convertir a ODS

<a name="python-pdf-to-ods"><strong>Pasos: Convertir PDF a ODS en Python</strong></a>

1. Cree una instancia del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el documento PDF de origen.
2. Cree una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) con **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Guárdelo en formato **ODS** llamando al método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) y pasándole [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

La conversión al formato ODS se realiza de la misma manera que todos los demás formatos.

```python

from asposepdf import Api

documentName = "../../testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "../../testout/result1.ods"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.ODS
doc.save(documentOutName, save_option)
```


## Ver también

Este artículo también cubre estos temas. Los códigos son los mismos que arriba.

_Formato_: **Excel**
- [Código de Python de PDF a Excel](#python-pdf-to-xlsx)
- [API de Python de PDF a Excel](#python-pdf-to-xlsx)
- [Python de PDF a Excel Programáticamente](#python-pdf-to-xlsx)
- [Biblioteca de Python de PDF a Excel](#python-pdf-to-xlsx)
- [Guardar PDF como Excel en Python](#python-pdf-to-xlsx)
- [Generar Excel desde PDF en Python](#python-pdf-to-xlsx)
- [Crear Excel desde PDF en Python](#python-pdf-to-xlsx)
- [Convertidor de Python de PDF a Excel](#python-pdf-to-xlsx)

_Formato_: **XLS**
- [Código de Python de PDF a XLS](#python-pdf-to-xls)
- [API de Python de PDF a XLS](#python-pdf-to-xls)
- [Python de PDF a XLS Programáticamente](#python-pdf-to-xls)
- [Biblioteca de Python de PDF a XLS](#python-pdf-to-xls)
- [Guardar PDF como XLS en Python](#python-pdf-to-xls)
- [Generar XLS desde PDF en Python](#python-pdf-to-xls)
- [Crear XLS desde PDF en Python](#python-pdf-to-xls)
- [Convertidor de Python de PDF a XLS](#python-pdf-to-xls)

_Formato_: **XLSX**

- [Código de Python de PDF a XLSX](#python-pdf-to-xlsx)
- [API de Python PDF a XLSX](#python-pdf-to-xlsx)
- [Programáticamente de Python PDF a XLSX](#python-pdf-to-xlsx)
- [Biblioteca de Python PDF a XLSX](#python-pdf-to-xlsx)
- [Guardar PDF de Python como XLSX](#python-pdf-to-xlsx)
- [Generar XLSX de PDF en Python](#python-pdf-to-xlsx)
- [Crear XLSX de PDF en Python](#python-pdf-to-xlsx)
- [Convertidor de Python PDF a XLSX](#python-pdf-to-xlsx)

_Formato_: **CSV**
- [Código de Python PDF a CSV](#python-pdf-to-csv)
- [API de Python PDF a CSV](#python-pdf-to-csv)
- [Programáticamente de Python PDF a CSV](#python-pdf-to-csv)
- [Biblioteca de Python PDF a CSV](#python-pdf-to-csv)
- [Guardar PDF de Python como CSV](#python-pdf-to-csv)
- [Generar CSV de PDF en Python](#python-pdf-to-csv)
- [Crear CSV de PDF en Python](#python-pdf-to-csv)
- [Convertidor de Python PDF a CSV](#python-pdf-to-csv)

_Formato_: **ODS**
- [Código de Python PDF a ODS](#python-pdf-to-ods)
- [API de Python PDF a ODS](#python-pdf-to-ods)
- [Programáticamente de Python PDF a ODS](#python-pdf-to-ods)
- [Biblioteca de Python PDF a ODS](#python-pdf-to-ods)

- [Guardar PDF de Python como ODS](#python-pdf-to-ods)
- [Python Generar ODS desde PDF](#python-pdf-to-ods)
- [Python Crear ODS desde PDF](#python-pdf-to-ods)
- [Convertidor de PDF a ODS en Python](#python-pdf-to-ods)