---
title: Convertir PDF a Excel en C++
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: /cpp/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: Aspose.PDF para C++ te permite convertir PDF a formato Excel usando C++. Durante este proceso, las páginas individuales del archivo PDF se convierten en hojas de cálculo de Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Visión general

Este artículo explica cómo **convertir PDF a formatos Excel usando C++**. Cubre los siguientes temas.

_Formato_: **XLS**
- [C++ PDF a XLS](#cpp-pdf-to-xls)
- [C++ Convertir PDF a XLS](#cpp-pdf-to-xls)
- [C++ Cómo convertir archivo PDF a XLS](#cpp-pdf-to-xls)

_Formato_: **XLSX**
- [C++ PDF a XLSX](#cpp-pdf-to-xlsx)
- [C++ Convertir PDF a XLSX](#cpp-pdf-to-xlsx)
- [C++ Cómo convertir archivo PDF a XLSX](#cpp-pdf-to-xlsx)

_Formato_: **Formato Microsoft Excel XLS**
- [C++ PDF a Excel](#cpp-pdf-to-excel-xls)
- [C++ Convertir PDF a Excel](#cpp-pdf-to-excel-xls)
- [C++ Cómo convertir archivo PDF a Excel](#cpp-pdf-to-excel-xls)

_Formato_: **Formato Microsoft Excel XLSX**
- [C++ PDF a Excel](#cpp-pdf-to-excel-xlsx)
- [C++ Convertir PDF a Excel](#cpp-pdf-to-excel-xlsx)
- [C++ Cómo convertir archivo PDF a Excel](#cpp-pdf-to-excel-xlsx)

Otros temas cubiertos por este artículo
- [Ver También](#see-also)

## Conversiones de C++ PDF a Excel

**Aspose.PDF para C++** soporta la función de convertir archivos PDF a formatos de Excel.

Aspose.PDF para C++ es un componente de manipulación de PDF, hemos introducido una función que renderiza el archivo PDF a un libro de Excel (archivos XLS). Durante esta conversión, las páginas individuales del archivo PDF se convierten en hojas de cálculo de Excel.

Para convertir archivos PDF al formato <abbr title="Microsoft Excel Spreadsheet">XLS</abbr>, Aspose.PDF tiene una clase llamada ExcelSaveOptions. Un objeto de la clase ExcelSaveOptions se pasa como segundo argumento al constructor Document.Save(..).

El siguiente fragmento de código muestra el proceso para convertir un archivo PDF en formato XLS con Aspose.PDF para C++.

<a name="cpp-pdf-to-xls" id="cpp-pdf-to-xls"><strong>Pasos: Convertir PDF a XLS en C++</strong></a> | <a name="cpp-pdf-to-excel-xls" id="cpp-pdf-to-excel-xls"><strong>Pasos: Convertir PDF a formato Excel XLS en C++</strong></a>

1. Cree una instancia del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) con el documento PDF de origen.
2. Guárdelo en formato _XLS_ llamando al método **Document->Save()**.

```cpp
void ConvertPDFtoExcel()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Guardar la salida en formato XLS
    document->Save(_dataDir + outfilename, SaveFormat::Excel);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir PDF a XLS con Control de Columna

Al convertir un PDF a formato XLS, se agrega una columna en blanco al archivo de salida como primera columna. La opción InsertBlankColumnAtFirst de la clase in ExcelSaveOptions se utiliza para controlar esta columna. Su valor predeterminado es true.

```cpp
void ConvertPDFtoExcel_Advanced_InsertBlankColumnAtFirst()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para el nombre del archivo
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto ExcelSave Option
    auto excelSave = MakeObject<ExcelSaveOptions>();

    // La opción InsertBlankColumnAtFirst de la clase in ExcelSaveOptions se utiliza para controlar esta columna. Su valor predeterminado es true.
    excelSave->set_InsertBlankColumnAtFirst(false);

    // Guardar la salida en formato XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir PDF a una sola hoja de cálculo de Excel

Al exportar un archivo PDF con muchas páginas a XLS, cada página se exporta a una hoja diferente en el archivo de Excel. Esto se debe a que la propiedad MinimizeTheNumberOfWorksheets está configurada como false por defecto. Para asegurar que todas las páginas se exporten a una sola hoja en el archivo Excel de salida, configure la propiedad MinimizeTheNumberOfWorksheets como true.

```cpp
void ConvertPDFtoExcel_Advanced_MinimizeTheNumberOfWorksheets()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de opción de guardado en Excel
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_MinimizeTheNumberOfWorksheets(true);

    // Guardar la salida en formato XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir a formato XLSX

Por defecto, Aspose.PDF utiliza XML Spreadsheet 2003 para almacenar datos. Para convertir archivos PDF al formato XLSX, Aspose.PDF tiene una clase llamada [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) con 'Format'. Un objeto de la clase [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) se pasa como segundo argumento al método [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa).

El siguiente fragmento de código muestra el proceso para convertir un archivo PDF en formato XLSX.

<a name="cpp-pdf-to-xlsx" id="cpp-pdf-to-xlsx"><strong>Pasos: Convertir PDF a XLSX en C++</strong></a> | <a name="cpp-pdf-to-excel-xlsx" id="cpp-pdf-to-excel-xlsx"><strong>Pasos: Convertir PDF a formato Excel XLSX en C++</strong></a>

1. Cree una instancia del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) con el documento PDF de origen.
2. Crea una instancia de [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options).
3. Establece el formato como _ExcelSaveOptions::ExcelFormat::XLSX_.
4. Guárdalo en formato _XLSX_ llamando al método **Document->Save()** y pasándole la instancia de _ExcelSaveOptions_.

```cpp
void ConvertPDFtoExcel_Advanced_SaveXLSX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para el nombre del archivo
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de opción de guardado de Excel
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);

    // Guardar la salida en formato XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}

**Intenta convertir PDF a Excel en línea**
Aspose.PDF para C++ te presenta una aplicación gratuita en línea ["PDF a XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a Excel con Aplicación Gratuita](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Ver También

Este artículo también cubre estos temas. Los códigos son los mismos que arriba.

_Formato_: **Formato Microsoft Excel XLS**
- [C++ PDF a Excel XLS Código](#cpp-pdf-to-excel-xls)
- [C++ PDF a Excel XLS Programáticamente](#cpp-pdf-to-excel-xls)
- [C++ PDF a Excel XLS Biblioteca](#cpp-pdf-to-excel-xls)
- [C++ Guardar PDF como Excel XLS](#cpp-pdf-to-excel-xls)
- [C++ Generar Excel XLS desde PDF](#cpp-pdf-to-excel-xls)
- [C++ Crear Excel XLS desde PDF](#cpp-pdf-to-excel-xls)
- [C++ Convertidor de PDF a Excel XLS](#cpp-pdf-to-excel-xls)

_Formato_: **Formato Microsoft Excel XLSX**
- [C++ PDF a Excel XLSX Código](#cpp-pdf-to-excel-xlsx)

- [C++ PDF a Excel XLSX Programáticamente](#cpp-pdf-to-excel-xlsx)
- [C++ Biblioteca de PDF a Excel XLSX](#cpp-pdf-to-excel-xlsx) 
- [C++ Guardar PDF como Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ Generar Excel XLSX desde PDF](#cpp-pdf-to-excel-xlsx)
- [C++ Crear Excel XLSX desde PDF](#cpp-pdf-to-excel-xlsx)
- [C++ Convertidor de PDF a Excel XLSX](#cpp-pdf-to-excel-xlsx)

_Formato_: **XLS**
- [C++ Código de PDF a XLS](#cpp-pdf-to-xls)
- [C++ PDF a XLS Programáticamente](#cpp-pdf-to-xls)
- [C++ Biblioteca de PDF a XLS](#cpp-pdf-to-xls)
- [C++ Guardar PDF como XLS](#cpp-pdf-to-xls)
- [C++ Generar XLS desde PDF](#cpp-pdf-to-xls)
- [C++ Crear XLS desde PDF](#cpp-pdf-to-xls)
- [C++ Convertidor de PDF a XLS](#cpp-pdf-to-xls)

_Formato_: **XLSX**
- [C++ Código de PDF a XLSX](#cpp-pdf-to-xlsx)
- [C++ PDF a XLSX Programáticamente](#cpp-pdf-to-xlsx)
- [C++ Biblioteca de PDF a XLSX](#cpp-pdf-to-xlsx)
- [C++ Guardar PDF como XLSX](#cpp-pdf-to-xlsx)
- [C++ Generar XLSX desde PDF](#cpp-pdf-to-xlsx)
- [C++ Crear XLSX desde PDF](#cpp-pdf-to-xlsx)
- [C++ Convertidor de PDF a XLSX](#cpp-pdf-to-xlsx)