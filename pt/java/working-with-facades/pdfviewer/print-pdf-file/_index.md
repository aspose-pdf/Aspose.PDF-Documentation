---
title: Trabalhando com impressão de PDF 
type: docs
weight: 10
url: /pt/java/print-pdf-file/
description: Esta seção explica como imprimir um arquivo PDF com Aspose.PDF Facades usando a classe PdfViewer.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Imprimindo Arquivo PDF na Impressora Padrão usando Configurações de Impressora e Página

A classe [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) permite imprimir um arquivo PDF na impressora padrão. Portanto, você precisa criar um objeto [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) e abrir o PDF usando o método openPdfFile(..).

Chame o método printDocument(..) para imprimir o PDF na impressora padrão.

O trecho de código a seguir mostra como imprimir PDF na impressora padrão com configurações de impressora e página.

```java
 public static void PrintingPDFFile() {
        // Criar objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir arquivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Definir atributos para impressão
        viewer.setAutoResize(true); // Imprimir o arquivo com tamanho ajustado
        viewer.setAutoRotate(true); // Imprimir o arquivo com rotação ajustada
        viewer.setPrintPageDialog(false); // Não produzir o diálogo de número de página ao imprimir

        // Criar objetos para configurações de impressora e página e PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Definir nome da impressora
        printerSettings.setPrinterName("Microsoft Print to PDF");
        

        // Definir PageSize (se necessário)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Definir PageMargins (se necessário)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimir documento usando configurações de impressora e página
        viewer.printDocumentWithSettings(pageSettings, printerSettings);
        
        // Fechar o arquivo PDF após impressão
        viewer.close();
    }
```


Para exibir uma caixa de diálogo de impressão, tente usar o seguinte trecho de código:

```java
public static void PrintingPDFDisplayPrintDialog() {
        // Criar objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir arquivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Definir atributos para impressão
        viewer.setAutoResize(true); // Imprimir o arquivo com tamanho ajustado
        viewer.setAutoRotate(true); // Imprimir o arquivo com rotação ajustada
        viewer.setPrintPageDialog(true);

        // Criar objetos para configurações de impressora e de página e PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Definir PageSize (se necessário)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Definir PageMargins (se necessário)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        java.awt.print.PrinterJob pj = java.awt.print.PrinterJob.getPrinterJob();

        if (pj.printDialog()) {
            printerSettings.setPrinterName(pj.getPrintService().getName());
            printerSettings.setCopies((short) pj.getCopies());
            // Imprimir documento usando configurações de impressora e de página
            viewer.printDocumentWithSettings(pageSettings, printerSettings);
        }
        // Fechar o arquivo PDF após a impressão
        viewer.close();
    }
```


## Imprimir PDF para Impressora Virtual

Existem impressoras que imprimem para um arquivo. Definimos o nome da impressora virtual e, por analogia com o exemplo anterior, fazemos as configurações.

```java
public static void PrintingPDFToSoftPrinter() {
        // Criar objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir arquivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Definir atributos para impressão
        viewer.setAutoResize(true); // Imprimir o arquivo com tamanho ajustado
        viewer.setAutoRotate(true); // Imprimir o arquivo com rotação ajustada
        viewer.setPrintPageDialog(false); // Não produzir a caixa de diálogo de número de página ao imprimir

        // Criar objetos para configurações de impressora e página e PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Definir impressora Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");
        // ou Adobe
        // printerSettings.setPrinterName("Adobe PDF");

        // Definir PageSize (se necessário)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Definir PageMargins (se necessário)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimir documento usando configurações de impressora e página
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Fechar o arquivo PDF após a impressão
        viewer.close();
    }
```


## Ocultando a Caixa de Diálogo de Impressão

O Aspose.PDF para Java permite que você oculte a caixa de diálogo de impressão. Para isso, use o método [getPrintPageDialog](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer#getPrintPageDialog--).

O trecho de código a seguir mostra como ocultar a caixa de diálogo de impressão.

```java
public static void PrintingPDFHidePrintDialog() {
        // Criar objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir arquivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Definir atributos para impressão
        viewer.setAutoResize(true); // Imprimir o arquivo com tamanho ajustado
        viewer.setAutoRotate(true); // Imprimir o arquivo com rotação ajustada

        viewer.setPrintPageDialog(false); // Não produzir a caixa de diálogo de número de página ao imprimir

        // Criar objetos para configurações de impressora e página e PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Definir impressora Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // Definir PageSize (se necessário)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Definir PageMargins (se necessário)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimir documento usando configurações de impressora e página
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Fechar o arquivo PDF após a impressão
        viewer.close();
    }
```


## Imprimindo PDF Colorido em Arquivo XPS como Escala de Cinza

Um documento PDF colorido pode ser impresso em uma impressora XPS como escala de cinza, usando [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer). Para conseguir isso, você precisa usar a propriedade PdfViewer.PrintAsGrayscale e defini-la como *true*.

O trecho de código a seguir demonstra a implementação da propriedade PdfViewer.PrintAsGrayscale.

```java
 public static void PrintingPDFasGrayscale() {
        // Criar objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir arquivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Definir atributos para impressão
        viewer.setAutoResize(true); // Imprimir o arquivo com tamanho ajustado
        viewer.setAutoRotate(true); // Imprimir o arquivo com rotação ajustada

        viewer.setPrintAsGrayscale(true);

        // Criar objetos para configurações de impressora e página e PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Definir impressora Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // Definir PageSize (se necessário)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Definir PageMargins (se necessário)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimir documento usando configurações de impressora e página
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Fechar o arquivo PDF após a impressão
        viewer.close();
    }
```


## Conversão de PDF para PostScript

A classe [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) fornece a capacidade de imprimir documentos PDF e, com a ajuda desta classe, também podemos converter arquivos PDF para o formato PostScript. Para converter um arquivo PDF em PostScript, primeiro instale qualquer impressora PS e apenas imprima para arquivo com a ajuda do PdfViewer.

O trecho de código a seguir mostra como imprimir e converter um PDF para o formato PostScript.

```java
public static void PrintingPDFToPostScript() {
        // Criar objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir arquivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Definir atributos para impressão
        viewer.setAutoResize(true); // Imprimir o arquivo com tamanho ajustado
        viewer.setAutoRotate(true); // Imprimir o arquivo com rotação ajustada

        viewer.setPrintAsGrayscale(true);
        

        // Criar objetos para configurações da impressora e da página e PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Definir Impressora PostScript
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");
        printerSettings.setPrintToFile(true);
        printerSettings.setPrintFileName(_dataDir+"result.ps");

        // Definir PageSize (se necessário)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Definir PageMargins (se necessário)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimir documento usando configurações de impressora e página
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Fechar o arquivo PDF após a impressão
        viewer.close();
    }
```


## Verificando o Status da Tarefa de Impressão

Um arquivo PDF pode ser impresso em uma impressora física, assim como no Microsoft XPS Document Writer, sem exibir uma caixa de diálogo de impressão, usando a classe [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer). Ao imprimir arquivos PDF grandes, o processo pode demorar muito tempo, então o usuário pode não ter certeza se o processo de impressão foi concluído ou encontrou um problema. Para determinar o status de uma tarefa de impressão, use a propriedade PrintStatus. O trecho de código a seguir mostra como imprimir o arquivo PDF em um arquivo XPS e obter o status da impressão.

```java
public static void CheckingPrintJobStatus() {
        // Criar objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir arquivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Definir atributos para impressão
        viewer.setAutoResize(true); // Imprimir o arquivo com tamanho ajustado
        viewer.setAutoRotate(true); // Imprimir o arquivo com rotação ajustada

        viewer.setPrintAsGrayscale(true);

        // Criar objetos para configurações de impressora e página e PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Definir impressora Microsoft Soft Printer
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");

        // Definir PageSize (se necessário)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Definir PageMargins (se necessário)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimir documento usando configurações de impressora e página
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // // Verificar o status da impressão
        if (viewer.getPrintStatus() != null) {
            Exception ex = (Exception) viewer.getPrintStatus();
            System.out.println(ex.getMessage());
        } else {
            // Nenhum erro foi encontrado. Tarefa de impressão concluída com sucesso
            System.out.println("Tudo ocorreu bem!");
        }
        // Fechar o arquivo PDF após a impressão
        viewer.close();
    }
```