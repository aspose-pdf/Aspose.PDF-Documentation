---
title: Convertir PDF a Excel en Java
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: /java/convert-pdf-to-excel/
lastmod: "2026-06-16"
description: Aprenda a convertir archivos PDF a Excel en Java con Aspose.PDF, incluida la salida XML Spreadsheet 2003, XLSX, XLSM, CSV y ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a Excel en Java
Abstract: Este artículo explica cómo convertir archivos PDF a formatos compatibles con Excel con Aspose.PDF para Java. Cubre la salida de hojas de cálculo XML 2003, XLSX, XLSM, CSV y ODS, junto con opciones para la inserción de columnas en blanco y la minimización del número de hojas de trabajo.
---
Aspose.PDF para Java puede exportar contenido PDF a múltiples formatos de hojas de cálculo con diferentes opciones de diseño. Utilice [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para elegir el formato del libro de trabajo de destino y controlar cómo se asigna el contenido de la página a hojas de trabajo y columnas.


## 
Convertir PDF a Excel 2003 XML



Utilice este ejemplo cuando el contenido PDF deba exportarse al formato de hoja de cálculo XML de Excel 2003.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) y establezca su formato en `XMLSpreadSheet2003`.
1. Llame a `document.save(outputFile.toString(), saveOptions)` para que el PDF cargado se serialice en el esquema XML de Excel 2003.

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

## 
Convertir PDF a XLSX



Utilice este ejemplo cuando el contenido PDF deba convertirse al formato XLSX de Excel 2007+.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) y establezca su formato en `XLSX`.

1. Llame a `document.save(outputFile.toString(), saveOptions)` para que el diseño PDF se exporte como un libro de trabajo de Office Open XML.

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

## 
Convierta PDF a XLSX con control de columnas



Utilice este ejemplo cuando deba ajustarse el manejo de columnas durante la conversión de PDF a Excel.

1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para la salida `XLSX`.

1. Habilite `setInsertBlankColumnAtFirst(true)` cuando se necesite una columna inicial adicional para mejorar el diseño de la hoja de trabajo producida a partir del PDF.

1. Llame a `document.save(outputFile.toString(), saveOptions)` y escriba el archivo XLSX convertido.


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

## 
Convierta PDF a una sola hoja de cálculo de Excel

Utilice este ejemplo cuando todas las páginas PDF deban exportarse a una hoja de trabajo.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para exportar `XLSX`.

1. Habilite `setMinimizeTheNumberOfWorksheets(true)` para que varias páginas PDF se consoliden en menos hojas de trabajo.

1. Llame a `document.save(outputFile.toString(), saveOptions)` y guarde el archivo de salida XLSX.

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



Utilice este ejemplo cuando la salida PDF deba guardarse como un libro de Excel con macros habilitadas.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) y establezca el formato en `XLSM`.

1. Llame a `document.save(outputFile.toString(), saveOptions)` para que el contenido del PDF se exporte a un contenedor de libros habilitado para macros.
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

## 
Convertir PDF a CSV



Utilice este ejemplo cuando el contenido tabular PDF deba exportarse como CSV.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) y establezca el formato en `CSV`.
1. Llame a `document.save(outputFile.toString(), saveOptions)` para que el contenido del PDF se acople en una salida de texto separado por comas.

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

## 
Convertir PDF a ODS



Utilice este ejemplo cuando el contenido PDF deba exportarse al formato de hoja de cálculo OpenDocument.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) y establezca el formato en `ODS`.

1. Llame a `document.save(outputFile.toString(), saveOptions)` para que el PDF se exporte en formato de hoja de cálculo OpenDocument.

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
