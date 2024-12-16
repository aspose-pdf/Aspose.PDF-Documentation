---
title: Converter PDF para Excel 
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /pt/java/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: Aspose.PDF para Java permite que você converta PDF para o formato Excel usando Java. Durante isso, as páginas individuais do arquivo PDF são convertidas em planilhas do Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF para Java API permite que você renderize seus arquivos PDF para os formatos de arquivo Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) e [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). Já temos outra API, conhecida como [Aspose.Cells para Java](https://products.aspose.com/cells/java), que fornece a capacidade de criar e manipular pastas de trabalho do Excel existentes. Também fornece a capacidade de transformar pastas de trabalho do Excel para o formato PDF.

{{% alert color="primary" %}}

**Tente converter PDF para Excel online**

Aspose.PDF for Java apresenta a você o aplicativo online gratuito ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Converção PDF para Excel com Aplicativo Gratuito](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Converter PDF para Excel XLS

Para converter arquivos PDF para o formato XLS, o Aspose.PDF possui uma classe chamada [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Um objeto da classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) é passado como segundo argumento para o método Document.Save(..).

Converter um arquivo PDF para o formato XLSX faz parte da biblioteca do Aspose.PDF para a versão Java 18.6. Para converter arquivos PDF para o formato XLSX, você precisa definir o formato como XLSX usando o método setFormat() da Classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

O trecho de código a seguir mostra como converter um arquivo PDF nos formatos xls e .xlsx:

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoXLSX {

    private ConvertPDFtoXLSX() {

    }

    // O caminho para o diretório de documentos.
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        ConvertPDFtoExcelSimple();
        ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst();
        ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets();
        ConvertPDFtoExcelAdvanced_SaveXLSX();
    }

    public static void ConvertPDFtoExcelSimple() {
        // Carregar documento PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Instanciar objeto ExcelSaveOption
        ExcelSaveOptions excelsave = new ExcelSaveOptions();

        // Salvar a saída em formato XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
}
```

## Converter PDF para XLS com Controle de Coluna

Ao converter um PDF para o formato XLS, uma coluna em branco é adicionada ao arquivo de saída como a primeira coluna. A opção InsertBlankColumnAtFirst na classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) é usada para controlar essa coluna. Seu valor padrão é true.

```java
    public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Carregar documento PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // Instanciar objeto de opção de salvamento Excel
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setInsertBlankColumnAtFirst(false);
        // Salvar o resultado no formato XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## Converter PDF para uma Única Planilha do Excel

Ao exportar um arquivo PDF com muitas páginas para XLS, cada página é exportada para uma folha diferente no arquivo Excel.
 Isso ocorre porque a propriedade MinimizeTheNumberOfWorksheets está configurada como false por padrão. Para garantir que todas as páginas sejam exportadas para uma única planilha no arquivo Excel de saída, configure a propriedade MinimizeTheNumberOfWorksheets como true.

```java
    public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Carregar documento PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Instanciar objeto ExcelSave Option
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setMinimizeTheNumberOfWorksheets(true);

        // Salvar a saída no formato XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## Converter para o formato XLSX

Por padrão, o Aspose.PDF usa o XML Spreadsheet 2003 para armazenar dados. Para converter arquivos PDF para o formato XLSX, o Aspose.PDF possui uma classe chamada ExcelSaveOptions com Formato. Um objeto da classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) é passado como segundo argumento para o método Document.Save(..).

```java
    public static void ConvertPDFtoExcelAdvanced_SaveXLSX() {
        // Carregar documento PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Instanciar objeto ExcelSave Option
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);

        // Salvar a saída no formato XLS
        pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
    }
```