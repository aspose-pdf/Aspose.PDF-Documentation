---
title: Convertir PDF a Excel en Java
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: /es/java/convert-pdf-to-excel/
lastmod: "2026-09-29"
description: Aprenda cómo convertir archivos PDF a Excel en Java con Aspose.PDF, incluyendo XML Spreadsheet 2003, XLSX, XLSM, CSV y salida ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convertir PDF a Excel en Java
Abstract: Este artículo explica cómo convertir archivos PDF a formatos compatibles con Excel con Aspose.PDF for Java. Cubre la salida XML Spreadsheet 2003, XLSX, XLSM, CSV y ODS, junto con opciones para la inserción de columnas en blanco y la minimización del número de hojas de cálculo.
---
Aspose.PDF for Java puede exportar el contenido de PDF a varios formatos de hoja de cálculo con diferentes opciones de diseño. Use [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para elegir el formato del libro de trabajo de destino y controlar cómo se asigna el contenido de la página a las hojas de cálculo y columnas.

## Convertir PDF a Excel 2003 XML

Utilice este ejemplo cuando el contenido PDF deba exportarse al formato de hoja de cálculo XML de Excel 2003.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) y establezca su formato a `XMLSpreadSheet2003`.
1. Llame `document.save(outputFile.toString(), saveOptions)` por lo que el PDF cargado se serializa en el esquema XML de Excel 2003.
1. Guarde el archivo de salida convertido.

```java
public static void convertPdfToExcelSpreadSheet2003(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a XLSX

Utilice este ejemplo cuando el contenido PDF deba convertirse al formato Excel 2007+ XLSX.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) y establezca su formato a `XLSX`.
1. Llame `document.save(outputFile.toString(), saveOptions)` por lo que el diseño del PDF se exporta como un libro de trabajo de Office Open XML.
1. Guarde el archivo de hoja de cálculo de salida.

```java
public static void convertPdfToExcel2007(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a XLSX con control de columnas

Use este ejemplo cuando el manejo de columnas deba ajustarse durante la conversión de PDF a Excel.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para `XLSX` salida.
1. Habilite `setInsertBlankColumnAtFirst(true)` cuando se necesita una columna adicional al inicio para mejorar el diseño de la hoja de cálculo generado a partir del PDF.
1. Llame `document.save(outputFile.toString(), saveOptions)` y escriba el archivo XLSX convertido.

```java
public static void convertPdfToExcel2007ControlColumn(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setInsertBlankColumnAtFirst(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a una sola hoja de Excel

Utilice este ejemplo cuando todas las páginas de PDF deban exportarse a una sola hoja de cálculo.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para `XLSX` exportar.
1. Habilite `setMinimizeTheNumberOfWorksheets(true)` por lo que varias páginas de PDF se consolidan en menos hojas de cálculo.
1. Llame `document.save(outputFile.toString(), saveOptions)` y guarde el archivo de salida XLSX.

```java
public static void convertPdfToExcel2007SingleExcelWorksheet(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setMinimizeTheNumberOfWorksheets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a XLSM

Utilice este ejemplo cuando la salida PDF debe guardarse como un libro de Excel habilitado para macros.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) y establezca el formato a `XLSM`.
1. Llame `document.save(outputFile.toString(), saveOptions)` por lo que el contenido del PDF se exporta a un contenedor de libro de trabajo habilitado para macros.
1. Guarde el archivo XLSM.

```java
public static void convertPdfToExcel2007Macro(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSM);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a CSV

Utilice este ejemplo cuando el contenido tabular del PDF deba exportarse como CSV.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) y establezca el formato a `CSV`.
1. Llame `document.save(outputFile.toString(), saveOptions)` por lo que el contenido del PDF se aplana a una salida de texto separado por comas.
1. Guarde el archivo CSV generado.

```java
public static void convertPdfToExcel2007Csv(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a ODS

Utilice este ejemplo cuando el contenido del PDF deba exportarse al formato de hoja de cálculo OpenDocument.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) y establezca el formato a `ODS`.
1. Llame `document.save(outputFile.toString(), saveOptions)` por lo que el PDF se exporta en formato de hoja de cálculo OpenDocument.
1. Guarde el archivo ODS convertido.

```java
public static void convertPdfToOds(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
