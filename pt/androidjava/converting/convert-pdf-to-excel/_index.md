---
title: Converter PDF para Excel
linktitle: Converter PDF para Excel
type: docs
weight: 90
url: /pt/androidjava/convert-pdf-to-excel/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java permite que você converta PDF para o formato Excel. Durante isso, as páginas individuais do arquivo PDF são convertidas em planilhas Excel.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Android via Java API permite que você renderize seus arquivos PDF para Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) e [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) formatos de arquivo. Já temos outra API, conhecida como [Aspose.Cells for Java](https://products.aspose.com/cells/java), que fornece a capacidade de criar e manipular pastas de trabalho do Excel existentes. Também fornece a capacidade de transformar pastas de trabalho do Excel em formato PDF.

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) 

{{% /alert %}}

## Converter PDF para Excel XLS

Para converter arquivos PDF para o formato XLS, o Aspose.PDF tem uma classe chamada [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Um objeto do [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) classe é passada como segundo argumento para o Document.Save(..) construtor. 

Converter um arquivo PDF para o formato XLSX faz parte da biblioteca do Aspose.PDF for Java versão 18.6. Para converter arquivos PDF para o formato XLSX, você precisa definir o formato como XLSX usando o método setFormat() de [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) Classe.

O snippet de código a seguir mostra como converter um arquivo PDF em formato xls e .xlsx:

```java
public void convertPDFtoExcelSimple() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Converter PDF para XLS com Coluna de Controle

Ao converter um PDF para o formato XLS, uma coluna em branco é adicionada ao arquivo de saída como primeira coluna. O in [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) A opção class InsertBlankColumnAtFirst é usada para controlar esta coluna. Seu valor padrão é true.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Converter PDF para uma única planilha do Excel 

Ao exportar um arquivo PDF com muitas páginas para XLS, cada página é exportada para uma planilha diferente no arquivo Excel. Isso ocorre porque a propriedade MinimizeTheNumberOfWorksheets está definida como false por padrão. Para garantir que todas as páginas sejam exportadas para uma única planilha no arquivo Excel de saída, defina a propriedade MinimizeTheNumberOfWorksheets como true.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Save the output in XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS Excel format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## Converter para o formato XLSX 

Por padrão, Aspose.PDF usa XML Spreadsheet 2003 para armazenar dados. Para converter arquivos PDF para o formato XLSX, Aspose.PDF tem uma classe chamada ExcelSaveOptions com Format. Um objeto da [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) A classe é passada como segundo argumento para o método Document.Save(..).

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Save the output in CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Save the file into CSV format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
