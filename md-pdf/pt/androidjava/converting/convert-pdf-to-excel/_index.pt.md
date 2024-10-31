---
title: Converter PDF para Excel 
linktitle: Converter PDF para Excel 
type: docs
weight: 90
url: /androidjava/convert-pdf-to-excel/
lastmod: "2021-06-05"
description: Aspose.PDF para Android via Java permite converter PDF para o formato Excel. Durante isso, as páginas individuais do arquivo PDF são convertidas em planilhas do Excel.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF para Android via Java API permite renderizar seus arquivos PDF para os formatos de arquivo Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) e [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). Já temos outra API, conhecida como [Aspose.Cells para Java](https://products.aspose.com/cells/java), que fornece a capacidade de criar e manipular pastas de trabalho do Excel existentes. Ela também fornece a capacidade de transformar pastas de trabalho do Excel para o formato PDF.

{{% alert color="primary" %}}

Tente online.
 Você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)

{{% /alert %}}

## Converter PDF para Excel XLS

Para converter arquivos PDF para o formato XLS, o Aspose.PDF possui uma classe chamada [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Um objeto da classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) é passado como segundo argumento para o construtor Document.Save(..).

Converter um arquivo PDF em formato XLSX faz parte da biblioteca do Aspose.PDF para a versão Java 18.6. Para converter arquivos PDF para o formato XLSX, você precisa definir o formato como XLSX usando o método setFormat() da Classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

O trecho de código a seguir mostra como converter um arquivo PDF para os formatos xls e .xlsx:

```java
public void convertPDFtoExcelSimple() {
        // Abra o documento PDF de origem
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instanciar objeto de opção de salvamento do Excel
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Salvar o arquivo no formato de documento MS
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Converter PDF para XLS com Controle de Coluna

Ao converter um PDF para o formato XLS, uma coluna em branco é adicionada ao arquivo de saída como primeira coluna. A opção InsertBlankColumnAtFirst da classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) é usada para controlar essa coluna. Seu valor padrão é verdadeiro.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Abrir o documento PDF de origem
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instanciar objeto da opção ExcelSave
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Salvar o arquivo no formato de documento MS
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Converter PDF para uma Única Planilha do Excel

Ao exportar um arquivo PDF com muitas páginas para XLS, cada página é exportada para uma folha diferente no arquivo Excel. Isso ocorre porque a propriedade MinimizeTheNumberOfWorksheets é definida como false por padrão. Para garantir que todas as páginas sejam exportadas para uma única folha no arquivo Excel de saída, defina a propriedade MinimizeTheNumberOfWorksheets como true.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Abra o documento PDF de origem
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instanciar objeto ExcelSaveOption
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Salvar a saída em XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Salvar o arquivo no formato MS Excel
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

Por padrão, o Aspose.PDF usa o XML Spreadsheet 2003 para armazenar dados. Para converter arquivos PDF para o formato XLSX, o Aspose.PDF tem uma classe chamada ExcelSaveOptions com Format. Um objeto da classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) é passado como segundo argumento para o método Document.Save(..).

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Carregar documento PDF
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instanciar objeto ExcelSaveOption
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Salvar a saída em CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Salvar o arquivo no formato CSV
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```