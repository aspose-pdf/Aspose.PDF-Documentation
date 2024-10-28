---
title: Extrair páginas de PDF
type: docs
weight: 20
url: /java/extract-pdf-pages/
description: Esta seção explica como extrair páginas de PDF com com.aspose.pdf.facades usando a classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Extrair páginas de PDF entre dois números usando caminhos de arquivos

O método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) da classe [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) permite que você extraia um intervalo específico de páginas de um arquivo PDF. Esta sobrecarga permite que você extraia páginas enquanto manipula os arquivos PDF do disco. Esta sobrecarga requer os seguintes parâmetros: caminho do arquivo de entrada, página inicial, página final e caminho do arquivo de saída. As páginas da página inicial até a página final serão extraídas e a saída será salva no disco. O snippet de código a seguir mostra como extrair páginas de PDF entre dois números usando caminhos de arquivos.

```java
  public static void Extract_PDFPages_FilePaths() {
        // Criar objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();

        // Extrair páginas
        pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
    }
```


## Extrair Array de Páginas de PDF Usando Caminhos de Arquivo

Se você não deseja extrair um intervalo de páginas, mas sim um conjunto de páginas específicas, o método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) permite que você faça isso também. Primeiro, você precisa criar um array de inteiros com todos os números de página que precisam ser extraídos. Esta sobrecarga do método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) recebe os seguintes parâmetros: arquivo PDF de entrada, array de inteiros das páginas a serem extraídas e arquivo PDF de saída. O trecho de código a seguir mostra como extrair páginas do PDF usando caminhos de arquivo.

```java
 public static void Extract_ArrayPDFPages_FilePaths() {
        // Criar objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        int[] pagesToExtract = new int[] { 1, 2 };
        // Extrair páginas
        pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
    }
```


## Extrair Páginas de PDF entre Dois Números Usando Streams

O método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) da classe [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) permite que você extraia um intervalo de páginas usando streams. Você precisa passar os seguintes parâmetros para essa sobrecarga: stream de entrada, página inicial, página final e stream de saída. As páginas especificadas pelo intervalo entre a página inicial e a página final serão extraídas do stream de entrada e salvas no stream de saída. O seguinte trecho de código mostra como extrair páginas de PDF entre dois números usando streams.

```java
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


## Extrair Array de Páginas de PDF Usando Streams

Um array de páginas pode ser extraído do stream PDF e salvo no stream de saída usando a sobrecarga apropriada do método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-). Se você não deseja extrair um intervalo de páginas, mas sim um conjunto de páginas específicas, o método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) permite que você faça isso também. Primeiro, você precisa criar um array de inteiros com todos os números das páginas que precisam ser extraídas. Esta sobrecarga do método [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) recebe os seguintes parâmetros: stream de entrada, array de inteiros de páginas a serem extraídas e stream de saída. O snippet de código a seguir mostra como extrair páginas de PDF usando streams.

```java
public static void Extract_ArrayPDFPages_Streams()
        {
            // Criar objeto PdfFileEditor
            PdfFileEditor pdfEditor = new PdfFileEditor();
            // Criar streams
            using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
            using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
            {
                int[] pagesToExtract = new int[] { 1, 2 };
                // Extrair páginas
                pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
            }
        }
```