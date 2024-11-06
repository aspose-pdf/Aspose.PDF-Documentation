---
title: Extrair páginas de PDF
type: docs
weight: 40
url: pt/net/extract-pdf-pages/
description: Esta seção explica como extrair páginas de PDF com Aspose.PDF Facades usando a classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Extrair Páginas de PDF entre Dois Números Usando Caminhos de Arquivo

O método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você extraia um intervalo especificado de páginas de um arquivo PDF. Esta sobrecarga permite que você extraia páginas enquanto manipula os arquivos PDF do disco. Esta sobrecarga requer os seguintes parâmetros: caminho do arquivo de entrada, página inicial, página final e caminho do arquivo de saída. As páginas da página inicial até a página final serão extraídas e a saída será salva no disco. O seguinte trecho de código mostra como extrair páginas de PDF entre dois números usando caminhos de arquivo.

```csharp
public static void Extract_PDFPages_FilePaths()
{
    // Criar objeto PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Extrair páginas
    pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## Extrair Array de Páginas de PDF Usando Caminhos de Arquivos

Se você não deseja extrair um intervalo de páginas, mas sim um conjunto de páginas específicas, o método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) permite que você faça isso também. Primeiro, você precisa criar um array de inteiros com todos os números de página que precisam ser extraídos. Esta sobrecarga do método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) leva os seguintes parâmetros: arquivo PDF de entrada, array de inteiros das páginas a serem extraídas e arquivo PDF de saída. O trecho de código a seguir mostra como extrair páginas de PDF usando caminhos de arquivos.

```csharp
public static void Extract_PDFPages_Streams()
{
    // Criar objeto PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Criar streams
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        // Extrair páginas
        pdfEditor.Extract(inputStream, 1, 3, outputStream);
}
```

## Extrair Páginas de PDF entre Dois Números Usando Streams

O método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite que você extraia um intervalo de páginas usando streams. Você precisa passar os seguintes parâmetros para esta sobrecarga: stream de entrada, página inicial, página final e stream de saída. As páginas especificadas pelo intervalo entre a página inicial e a página final serão extraídas do stream de entrada e salvas no stream de saída. O trecho de código a seguir mostra como extrair páginas de PDF entre dois números usando streams.

```csharp
public static void Extract_ArrayPDFPages_FilePaths()
{
    // Criar objeto PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Extrair páginas
    pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## Extrair Array de Páginas de PDF Usando Streams

Um array de páginas pode ser extraído do fluxo de PDF e salvo no fluxo de saída usando a sobrecarga apropriada do método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index). Se você não deseja extrair um intervalo de páginas, mas sim um conjunto de páginas específicas, o método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) permite que você faça isso também. Primeiro, você precisa criar um array de inteiros com todos os números das páginas que precisam ser extraídas. Esta sobrecarga do método [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) leva os seguintes parâmetros: fluxo de entrada, array de inteiros das páginas a serem extraídas e fluxo de saída.
O trecho de código a seguir mostra como extrair páginas de PDF usando fluxos.

```csharp
public static void Extract_ArrayPDFPages_Streams()
{
    // Criar objeto PdfFileEditor
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Criar fluxos
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
    {
        int[] pagesToExtract = new int[] { 1, 2 };
        // Extrair páginas
        pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
    }
}
```