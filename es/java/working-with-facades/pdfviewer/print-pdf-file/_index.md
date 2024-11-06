---
title: Trabajando con la impresión de PDF
type: docs
weight: 10
url: es/java/print-pdf-file/
description: Esta sección explica cómo imprimir un archivo PDF con Aspose.PDF Facades usando la clase PdfViewer.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Imprimir un archivo PDF a la impresora predeterminada usando configuraciones de impresora y página

La clase [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) permite imprimir un archivo PDF en la impresora predeterminada. Por lo tanto, necesitas crear un objeto [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) y abrir el PDF usando el método openPdfFile(..).

Llama al método printDocument(..) para imprimir el PDF en la impresora predeterminada.

El siguiente fragmento de código muestra cómo imprimir un PDF en la impresora predeterminada con configuraciones de impresora y página.

```java
 public static void PrintingPDFFile() {
        // Crear objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir archivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Establecer atributos para la impresión
        viewer.setAutoResize(true); // Imprimir el archivo con tamaño ajustado
        viewer.setAutoRotate(true); // Imprimir el archivo con rotación ajustada
        viewer.setPrintPageDialog(false); // No producir el diálogo de número de página al imprimir

        // Crear objetos para configuraciones de impresora y página y PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Establecer nombre de la impresora
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // Establecer tamaño de página (si es necesario)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Establecer márgenes de página (si es necesario)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimir documento usando configuraciones de impresora y página
        viewer.printDocumentWithSettings(pageSettings, printerSettings);
        
        // Cerrar el archivo PDF después de imprimir
        viewer.close();
    }
```


Para mostrar un cuadro de diálogo de impresión, intente usar el siguiente fragmento de código:

```java
public static void PrintingPDFDisplayPrintDialog() {
        // Crear objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir archivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Establecer atributos para la impresión
        viewer.setAutoResize(true); // Imprimir el archivo con tamaño ajustado
        viewer.setAutoRotate(true); // Imprimir el archivo con rotación ajustada
        viewer.setPrintPageDialog(true);

        // Crear objetos para la configuración de impresora y página y PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Establecer PageSize (si es necesario)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Establecer PageMargins (si es necesario)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        java.awt.print.PrinterJob pj = java.awt.print.PrinterJob.getPrinterJob();

        if (pj.printDialog()) {
            printerSettings.setPrinterName(pj.getPrintService().getName());
            printerSettings.setCopies((short) pj.getCopies());
            // Imprimir documento usando la configuración de impresora y página
            viewer.printDocumentWithSettings(pageSettings, printerSettings);
        }
        // Cerrar el archivo PDF después de imprimir
        viewer.close();
    }
```


## Imprimir PDF en Impresora Virtual

Hay impresoras que imprimen en un archivo. Establecemos el nombre de la impresora virtual y, por analogía con el ejemplo anterior, hacemos la configuración.

```java
public static void PrintingPDFToSoftPrinter() {
        // Crear objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir archivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Establecer atributos para imprimir
        viewer.setAutoResize(true); // Imprimir el archivo con tamaño ajustado
        viewer.setAutoRotate(true); // Imprimir el archivo con rotación ajustada
        viewer.setPrintPageDialog(false); // No mostrar el diálogo de número de página al imprimir

        // Crear objetos para la impresora, configuración de página y PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Establecer impresora Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");
        // o Adobe
        // printerSettings.setPrinterName("Adobe PDF");

        // Establecer tamaño de página (si es necesario)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Establecer márgenes de página (si es necesario)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimir documento utilizando la configuración de impresora y página
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Cerrar el archivo PDF después de imprimir
        viewer.close();
    }
```


## Ocultar el Diálogo de Impresión

Aspose.PDF para Java permite ocultar el diálogo de impresión. Para esto, use el método [getPrintPageDialog](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer#getPrintPageDialog--).

El siguiente fragmento de código muestra cómo ocultar el diálogo de impresión.

```java
public static void PrintingPDFHidePrintDialog() {
        // Crear objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir archivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Establecer atributos para imprimir
        viewer.setAutoResize(true); // Imprimir el archivo con tamaño ajustado
        viewer.setAutoRotate(true); // Imprimir el archivo con rotación ajustada

        viewer.setPrintPageDialog(false); // No producir el diálogo de número de página al imprimir

        // Crear objetos para la configuración de impresora y página y PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Establecer impresora Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // Establecer tamaño de página (si es necesario)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Establecer márgenes de página (si es necesario)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimir documento usando la configuración de página e impresora
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Cerrar el archivo PDF después de imprimir
        viewer.close();
    }
```


## Imprimir PDF en Color a Archivo XPS como Escala de Grises

Un documento PDF en color se puede imprimir en una impresora XPS como escala de grises, usando [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer). Para lograr esto, necesitas usar la propiedad PdfViewer.PrintAsGrayscale y establecerla en *true*.

El siguiente fragmento de código demuestra la implementación de la propiedad PdfViewer.PrintAsGrayscale.

```java
 public static void PrintingPDFasGrayscale() {
        // Crear objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir archivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Establecer atributos para imprimir
        viewer.setAutoResize(true); // Imprimir el archivo con tamaño ajustado
        viewer.setAutoRotate(true); // Imprimir el archivo con rotación ajustada

        viewer.setPrintAsGrayscale(true);

        // Crear objetos para la configuración de impresora y página y PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Establecer impresora Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // Establecer PageSize (si es necesario)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Establecer PageMargins (si es necesario)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimir documento usando configuración de impresora y página
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Cerrar el archivo PDF después de imprimir
        viewer.close();
    }
```


## Conversión de PDF a PostScript

La clase [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) proporciona la capacidad de imprimir documentos PDF y, con la ayuda de esta clase, también podemos convertir archivos PDF al formato PostScript. Para convertir un archivo PDF a PostScript, primero instale cualquier impresora PS y simplemente imprima en archivo con la ayuda de PdfViewer.

El siguiente fragmento de código te muestra cómo imprimir y convertir un PDF al formato PostScript.

```java
public static void PrintingPDFToPostScript() {
        // Crear objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir archivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Establecer atributos para la impresión
        viewer.setAutoResize(true); // Imprimir el archivo con tamaño ajustado
        viewer.setAutoRotate(true); // Imprimir el archivo con rotación ajustada

        viewer.setPrintAsGrayscale(true);
        

        // Crear objetos para configuración de impresora y de página y PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Establecer impresora PostSScript
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");
        printerSettings.setPrintToFile(true);
        printerSettings.setPrintFileName(_dataDir+"result.ps");

        // Establecer tamaño de página (si es necesario)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Establecer márgenes de página (si es necesario)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimir documento usando la configuración de impresora y de página
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Cerrar el archivo PDF después de imprimir
        viewer.close();
    }
```


## Verificación del Estado de la Tarea de Impresión

Un archivo PDF puede ser impreso en una impresora física, así como en el Microsoft XPS Document Writer, sin mostrar un cuadro de diálogo de impresión, utilizando la clase [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer). Al imprimir archivos PDF grandes, el proceso puede tardar mucho tiempo, por lo que el usuario podría no estar seguro de si el proceso de impresión se completó o si encontró un problema. Para determinar el estado de una tarea de impresión, utiliza la propiedad PrintStatus. El siguiente fragmento de código muestra cómo imprimir el archivo PDF en un archivo XPS y obtener el estado de impresión.

```java
public static void CheckingPrintJobStatus() {
        // Crear objeto PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Abrir archivo PDF de entrada
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Establecer atributos para la impresión
        viewer.setAutoResize(true); // Imprimir el archivo con tamaño ajustado
        viewer.setAutoRotate(true); // Imprimir el archivo con rotación ajustada

        viewer.setPrintAsGrayscale(true);

        // Crear objetos para la impresora y la configuración de página y PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Establecer impresora Microsoft Soft Printer
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");

        // Establecer tamaño de página (si es necesario)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Establecer márgenes de página (si es necesario)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimir documento utilizando la configuración de impresora y página
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // // Verificar el estado de impresión
        if (viewer.getPrintStatus() != null) {
            Exception ex = (Exception) viewer.getPrintStatus();
            System.out.println(ex.getMessage());
        } else {
            // No se encontraron errores. La tarea de impresión se completó con éxito
            System.out.println("¡Todo salió bien!");
        }
        // Cerrar el archivo PDF después de imprimir
        viewer.close();
    }
```