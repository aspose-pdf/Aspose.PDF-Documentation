---
title: Travailler avec l'impression PDF 
type: docs
weight: 10
url: /java/print-pdf-file/
description: Cette section explique comment imprimer un fichier PDF avec Aspose.PDF Facades en utilisant la classe PdfViewer.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Impression d'un fichier PDF sur l'imprimante par défaut en utilisant les paramètres d'imprimante et de page

La classe [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) vous permet d'imprimer un fichier PDF sur l'imprimante par défaut. Vous devez donc créer un objet [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) et ouvrir le PDF en utilisant la méthode openPdfFile(..).

Appelez la méthode printDocument(..) pour imprimer le PDF sur l'imprimante par défaut.

Le code suivant montre comment imprimer un PDF sur l'imprimante par défaut avec les paramètres de l'imprimante et de la page.

```java
 public static void PrintingPDFFile() {
        // Créer un objet PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Ouvrir le fichier PDF d'entrée
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Définir les attributs pour l'impression
        viewer.setAutoResize(true); // Imprimer le fichier avec la taille ajustée
        viewer.setAutoRotate(true); // Imprimer le fichier avec la rotation ajustée
        viewer.setPrintPageDialog(false); // Ne pas produire la boîte de dialogue du numéro de page lors de l'impression

        // Créer des objets pour les paramètres d'imprimante et de page et PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Définir le nom de l'imprimante
        printerSettings.setPrinterName("Microsoft Print to PDF");
        

        // Définir la taille de la page (si nécessaire)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Définir les marges de la page (si nécessaire)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimer le document en utilisant les paramètres de l'imprimante et de la page
        viewer.printDocumentWithSettings(pageSettings, printerSettings);
        
        // Fermer le fichier PDF après l'impression
        viewer.close();
    }
```


Afin d'afficher une boîte de dialogue d'impression, essayez d'utiliser l'extrait de code suivant :

```java
public static void PrintingPDFDisplayPrintDialog() {
        // Créer un objet PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Ouvrir le fichier PDF d'entrée
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Définir les attributs pour l'impression
        viewer.setAutoResize(true); // Imprimer le fichier avec la taille ajustée
        viewer.setAutoRotate(true); // Imprimer le fichier avec la rotation ajustée
        viewer.setPrintPageDialog(true);

        // Créer des objets pour les paramètres de l'imprimante et de la page ainsi que PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Définir la taille des pages (si nécessaire)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Définir les marges de la page (si nécessaire)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        java.awt.print.PrinterJob pj = java.awt.print.PrinterJob.getPrinterJob();

        if (pj.printDialog()) {
            printerSettings.setPrinterName(pj.getPrintService().getName());
            printerSettings.setCopies((short) pj.getCopies());
            // Imprimer le document en utilisant les paramètres de l'imprimante et de la page
            viewer.printDocumentWithSettings(pageSettings, printerSettings);
        }
        // Fermer le fichier PDF après l'impression
        viewer.close();
    }
```


## Imprimer un PDF sur une Imprimante Virtuelle

Il existe des imprimantes qui impriment sur un fichier. Nous définissons le nom de l'imprimante virtuelle et, par analogie avec l'exemple précédent, nous effectuons les réglages.

```java
public static void PrintingPDFToSoftPrinter() {
        // Créer un objet PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Ouvrir le fichier PDF d'entrée
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Définir les attributs pour l'impression
        viewer.setAutoResize(true); // Imprimer le fichier avec taille ajustée
        viewer.setAutoRotate(true); // Imprimer le fichier avec rotation ajustée
        viewer.setPrintPageDialog(false); // Ne pas produire la boîte de dialogue du numéro de page lors de l'impression

        // Créer des objets pour les paramètres de l'imprimante et de la page et PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Définir l'imprimante Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");
        // ou Adobe
        // printerSettings.setPrinterName("Adobe PDF");

        // Définir la PageSize (si nécessaire)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Définir les Marges de la Page (si nécessaire)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimer le document en utilisant les paramètres de page et d'imprimante
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Fermer le fichier PDF après l'impression
        viewer.close();
    }
```


## Masquer la boîte de dialogue d'impression

Aspose.PDF pour Java vous permet de masquer la boîte de dialogue d'impression. Pour cela, utilisez la méthode [getPrintPageDialog](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer#getPrintPageDialog--).

L'extrait de code suivant vous montre comment masquer la boîte de dialogue d'impression.

```java
public static void PrintingPDFHidePrintDialog() {
        // Créer un objet PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Ouvrir le fichier PDF d'entrée
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Définir les attributs pour l'impression
        viewer.setAutoResize(true); // Imprimer le fichier avec une taille ajustée
        viewer.setAutoRotate(true); // Imprimer le fichier avec une rotation ajustée

        viewer.setPrintPageDialog(false); // Ne pas produire la boîte de dialogue de numéro de page lors de l'impression

        // Créer des objets pour les paramètres d'imprimante et de page et PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Définir l'imprimante Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // Définir la taille de la page (si nécessaire)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Définir les marges de la page (si nécessaire)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimer le document en utilisant les paramètres d'imprimante et de page
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Fermer le fichier PDF après l'impression
        viewer.close();
    }
```


## Impression d'un PDF couleur en fichier XPS en niveaux de gris

Un document PDF en couleur peut être imprimé sur une imprimante XPS en niveaux de gris, en utilisant [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer). Pour y parvenir, vous devez utiliser la propriété PdfViewer.PrintAsGrayscale et la définir sur *true*.

Le code suivant démontre l'implémentation de la propriété PdfViewer.PrintAsGrayscale.

```java
 public static void PrintingPDFasGrayscale() {
        // Créer un objet PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Ouvrir le fichier PDF d'entrée
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Définir les attributs pour l'impression
        viewer.setAutoResize(true); // Imprimer le fichier avec une taille ajustée
        viewer.setAutoRotate(true); // Imprimer le fichier avec une rotation ajustée

        viewer.setPrintAsGrayscale(true);

        // Créer des objets pour les paramètres de l'imprimante et de la page ainsi que PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Définir l'imprimante Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // Définir la taille de la page (si nécessaire)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Définir les marges de la page (si nécessaire)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimer le document en utilisant les paramètres de l'imprimante et de la page
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Fermer le fichier PDF après l'impression
        viewer.close();
    }
```


## Conversion de PDF à PostScript

La classe [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) offre la possibilité d'imprimer des documents PDF et, avec l'aide de cette classe, nous pouvons également convertir des fichiers PDF en format PostScript. Pour convertir un fichier PDF en PostScript, installez d'abord une imprimante PS et imprimez simplement sur un fichier avec l'aide de PdfViewer.

Le code suivant vous montre comment imprimer et convertir un PDF au format PostScript.

```java
public static void PrintingPDFToPostScript() {
        // Créer un objet PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Ouvrir le fichier PDF d'entrée
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Définir les attributs pour l'impression
        viewer.setAutoResize(true); // Imprimer le fichier avec une taille ajustée
        viewer.setAutoRotate(true); // Imprimer le fichier avec une rotation ajustée

        viewer.setPrintAsGrayscale(true);
        

        // Créer des objets pour les paramètres de l'imprimante et de page et PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Définir l'imprimante PostScript
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");
        printerSettings.setPrintToFile(true);
        printerSettings.setPrintFileName(_dataDir+"result.ps");

        // Définir la taille de la page (si nécessaire)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Définir les marges de la page (si nécessaire)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimer le document en utilisant les paramètres de l'imprimante et de page
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Fermer le fichier PDF après l'impression
        viewer.close();
    }
```


## Vérification du statut du travail d'impression

Un fichier PDF peut être imprimé sur une imprimante physique ainsi que sur le Microsoft XPS Document Writer, sans afficher de boîte de dialogue d'impression, en utilisant la classe [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer). Lors de l'impression de fichiers PDF volumineux, le processus peut prendre beaucoup de temps, de sorte que l'utilisateur ne peut pas être sûr si le processus d'impression est terminé ou s'il a rencontré un problème. Pour déterminer le statut d'un travail d'impression, utilisez la propriété PrintStatus. Le fragment de code suivant montre comment imprimer le fichier PDF vers un fichier XPS et obtenir le statut de l'impression.

```java
public static void CheckingPrintJobStatus() {
        // Créer un objet PdfViewer
        PdfViewer viewer = new PdfViewer();

        // Ouvrir le fichier PDF d'entrée
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Définir les attributs pour l'impression
        viewer.setAutoResize(true); // Imprimer le fichier avec une taille ajustée
        viewer.setAutoRotate(true); // Imprimer le fichier avec une rotation ajustée

        viewer.setPrintAsGrayscale(true);

        // Créer des objets pour les paramètres de l'imprimante et de la page et PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Définir l'imprimante Microsoft Soft Printer
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");

        // Définir la taille de la page (si nécessaire)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Définir les marges de la page (si nécessaire)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Imprimer le document en utilisant les paramètres de l'imprimante et de la page
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Vérifier le statut de l'impression
        if (viewer.getPrintStatus() != null) {
            Exception ex = (Exception) viewer.getPrintStatus();
            System.out.println(ex.getMessage());
        } else {
            // Aucune erreur n'a été trouvée. Le travail d'impression s'est terminé avec succès
            System.out.println("Tout s'est bien passé !");
        }
        // Fermer le fichier PDF après l'impression
        viewer.close();
    }
```