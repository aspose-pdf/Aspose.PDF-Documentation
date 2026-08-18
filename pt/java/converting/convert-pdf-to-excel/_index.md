---
title: Converta PDF para Excel em Java
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /java/convert-pdf-to-excel/
lastmod: "2026-06-16"
description: Aprenda como converter arquivos PDF para Excel em Java com Aspose.PDF, incluindo planilha XML 2003, XLSX, XLSM, CSV e saída ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como converter PDF para Excel em Java
Abstract: Este artigo explica como converter arquivos PDF em formatos compatíveis com Excel com Aspose.PDF para Java. Abrange saída de planilha XML 2003, XLSX, XLSM, CSV e ODS, junto com opções para inserção de colunas em branco e minimização do número de planilhas.
---
Aspose.PDF for Java pode exportar conteúdo PDF para vários formatos de planilha com diferentes opções de layout. Use [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para escolher o formato da pasta de trabalho de destino e controlar como o conteúdo da página é mapeado em planilhas e colunas.

## Converter PDF em XML do Excel 2003

Use este exemplo quando o conteúdo PDF precisar ser exportado para o formato de planilha XML do Excel 2003.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) e defina seu formato como `XMLSpreadSheet2003`.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o PDF carregado seja serializado no esquema XML do Excel 2003.
1. Salve o arquivo de saída convertido.

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

## Converter PDF em XLSX

Use este exemplo quando o conteúdo PDF precisar ser convertido para o formato Excel 2007+ XLSX.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) e defina seu formato como `XLSX`.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o layout do PDF seja exportado como uma pasta de trabalho do Office Open XML.
1. Salve o arquivo da planilha de saída.

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

## Converta PDF para XLSX com controle de coluna

Use este exemplo quando o manuseio de colunas precisar ser ajustado durante a conversão de PDF para Excel.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para saída `XLSX`.
1. Habilite `setInsertBlankColumnAtFirst(true)` quando uma coluna inicial extra for necessária para melhorar o layout da planilha produzida a partir do PDF.
1. Chame `document.save(outputFile.toString(), saveOptions)` e grave o arquivo XLSX convertido.

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

## Converta PDF em uma única planilha do Excel

Use este exemplo quando todas as páginas PDF devem ser exportadas para uma planilha.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para exportação `XLSX`.
1. Habilite `setMinimizeTheNumberOfWorksheets(true)` para que várias páginas PDF sejam consolidadas em menos planilhas.
1. Chame `document.save(outputFile.toString(), saveOptions)` e salve o arquivo de saída XLSX.

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

## Converter PDF em XLSM

Use este exemplo quando a saída do PDF precisar ser salva como uma pasta de trabalho do Excel habilitada para macro.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) e defina o formato como `XLSM`.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o conteúdo do PDF seja exportado para um contêiner de pasta de trabalho habilitado para macro.
1. Salve o arquivo XLSM.

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

## Converter PDF em CSV

Use este exemplo quando o conteúdo tabular do PDF precisar ser exportado como CSV.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) e defina o formato como `CSV`.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o conteúdo do PDF seja nivelado para uma saída de texto separada por vírgula.
1. Salve o arquivo CSV gerado.

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

## Converter PDF em ODS

Use este exemplo quando o conteúdo PDF precisar ser exportado para o formato de planilha OpenDocument.

1. Abra o PDF de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) e defina o formato como `ODS`.
1. Chame `document.save(outputFile.toString(), saveOptions)` para que o PDF seja exportado em formato de planilha OpenDocument.
1. Salve o arquivo ODS convertido.

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
