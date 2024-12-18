---
title: Converter PDF para Microsoft Excel 
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /pt/php-java/convert-pdf-to-excel/
lastmod: "2024-05-20"
description: Aspose.PDF para PHP permite converter PDF para o formato Excel usando PHP. Durante isso, as páginas individuais do arquivo PDF são convertidas em planilhas do Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF para PHP API permite renderizar seus arquivos PDF para os formatos de arquivo Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) e [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). Já temos outra API, conhecida como [Aspose.Cells para PHP via Java](https://products.aspose.com/cells/php-java), que fornece a capacidade de criar e manipular pastas de trabalho do Excel existentes. Ela também fornece a capacidade de transformar pastas de trabalho do Excel para o formato PDF.

{{% alert color="primary" %}}

**Tente converter PDF para Excel online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["PDF para XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF de PDF para Excel com Aplicativo Gratuito](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Converter PDF para Excel XLS

Para converter arquivos PDF para o formato XLS, o Aspose.PDF possui uma classe chamada [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Um objeto da classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) é passado como um segundo argumento para o método Document.Save(..).

Converter um arquivo PDF para o formato XLSX faz parte da biblioteca do Aspose.PDF para a versão PHP 18.6. Para converter arquivos PDF para o formato XLSX, você precisa definir o formato como XLSX usando o método setFormat() da Classe [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

Os seguintes trechos de código mostram como converter um arquivo PDF em formato XLS e XLSX:

```php
// Carregar o documento PDF de entrada usando a classe Document.
$document = new Document($inputFile);

// Criar uma instância da classe ExcelSaveOptions para especificar as opções de salvamento.
$saveOption = new ExcelSaveOptions();

// Definir o formato de saída para XLS.
// $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$XMLSpreadSheet2003);

// Definir o formato de saída para XLSX.
    $excelSaveOptions_ExcelFormat = new ExcelSaveOptions_ExcelFormat();
    $saveOption->setFormat($excelSaveOptions_ExcelFormat->XLSX);

// Salvar o documento PDF como um arquivo Excel usando as opções de salvamento especificadas.
$document->save($outputFile, $saveOption);
```