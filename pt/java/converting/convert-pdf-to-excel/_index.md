---
title: Converter PDF para Excel em Java
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /pt/java/convert-pdf-to-excel/
lastmod: "2026-10-06"
description: Aprenda como converter arquivos PDF para Excel em Java com Aspose.PDF, incluindo saída XML Spreadsheet 2003, XLSX, XLSM, CSV e ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como converter PDF para Excel em Java
Abstract: Este artigo explica como converter arquivos PDF para formatos compatíveis com Excel usando o Aspose.PDF for Java. Ele aborda a saída em XML Spreadsheet 2003, XLSX, XLSM, CSV e ODS, juntamente com opções para inserção de colunas em branco e minimização do número de planilhas.
---
Aspose.PDF for Java pode exportar o conteúdo de PDF para vários formatos de planilha com diferentes opções de layout. Use [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para escolher o formato de livro de trabalho de destino e controlar como o conteúdo da página é mapeado para planilhas e colunas.

## Converter PDF para XML do Excel 2003

Use este exemplo quando o conteúdo PDF deve ser exportado para o formato de planilha XML do Excel 2003.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) e defina seu formato para `XMLSpreadSheet2003`.
1. Chamar `document.save(outputFile.toString(), saveOptions)` portanto, o PDF carregado é serializado no esquema XML do Excel 2003.
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

## Converter PDF para XLSX

Use este exemplo quando o conteúdo PDF deve ser convertido para o formato Excel 2007\u002B XLSX.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) e defina seu formato para `XLSX`.
1. Chamar `document.save(outputFile.toString(), saveOptions)` então o layout do PDF é exportado como uma pasta de trabalho Office Open XML.
1. Salve o arquivo de planilha de saída.

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

## Converter PDF para XLSX com controle de coluna

Use este exemplo quando o manuseio de colunas deve ser ajustado durante a conversão de PDF para Excel.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para `XLSX` saída.
1. Habilitar `setInsertBlankColumnAtFirst(true)` quando uma coluna adicional à esquerda é necessária para melhorar o layout da planilha produzida a partir do PDF.
1. Chamar `document.save(outputFile.toString(), saveOptions)` e escreva o arquivo XLSX convertido.

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

## Converter PDF para uma única planilha do Excel

Use este exemplo quando todas as páginas do PDF devem ser exportadas para uma única planilha.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) para `XLSX` exportar.
1. Habilitar `setMinimizeTheNumberOfWorksheets(true)` assim várias páginas de PDF são consolidadas em menos planilhas.
1. Chamar `document.save(outputFile.toString(), saveOptions)` e salve o arquivo de saída XLSX.

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

## Converter PDF para XLSM

Use este exemplo quando a saída de PDF deve ser salva como uma pasta de trabalho do Excel habilitada para macro.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) e defina o formato para `XLSM`.
1. Chamar `document.save(outputFile.toString(), saveOptions)` portanto, o conteúdo do PDF é exportado para um contêiner de pasta de trabalho com macros habilitadas.
1. Salvar o arquivo XLSM.

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

## Converter PDF para CSV

Use este exemplo quando o conteúdo tabular do PDF deve ser exportado como CSV.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) e defina o formato para `CSV`.
1. Chamar `document.save(outputFile.toString(), saveOptions)` então o conteúdo do PDF é achatado em uma saída de texto separada por vírgulas.
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

## Converter PDF para ODS

Use este exemplo quando o conteúdo do PDF deve ser exportado para o formato de planilha OpenDocument.

1. Abra o PDF de origem em um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Criar [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) e defina o formato para `ODS`.
1. Chamar `document.save(outputFile.toString(), saveOptions)` portanto, o PDF é exportado no formato de planilha OpenDocument.
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
