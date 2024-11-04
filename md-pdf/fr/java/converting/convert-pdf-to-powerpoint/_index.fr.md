---
title: Convertir PDF en Microsoft PowerPoint 
linktitle: Convertir PDF en PowerPoint
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
lastmod: "2021-11-19"
description: Aspose.PDF vous permet de convertir un PDF au format PowerPoint en utilisant Java. Une façon consiste à convertir un PDF en PPTX avec des diapositives sous forme d'images.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF pour Java** vous permet de suivre la progression de la conversion de PDF en PPTX. Nous avons une API nommée Aspose.Slides qui offre la fonctionnalité de créer ainsi que de manipuler des présentations PPT/PPTX. Cette API fournit également la fonctionnalité de convertir des fichiers PPT/PPTX en format PDF. Dans Aspose.PDF pour Java, nous avons introduit une fonctionnalité pour transformer des documents PDF en format PPTX. Lors de cette conversion, les pages individuelles du fichier PDF sont converties en diapositives séparées dans le fichier PPTX.

Lors de la conversion de PDF en PPTX, le texte est rendu en tant que texte que vous pouvez sélectionner/mettre à jour, au lieu d'être rendu sous forme d'image.
 Veuillez noter que pour convertir des fichiers PDF au format PPTX, Aspose.PDF fournit une classe nommée PptxSaveOptions. Un objet de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) est passé en tant que second argument à la méthode [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Consultez le snippet de code suivant pour résoudre vos tâches de conversion de PDF en format PowerPoint :

```java
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_Simple();
        convertPDFtoPPTX_SlideAsImages();
        convertPDFtoPPTX_ProgresDetails();
    }

    public static void convertPDFtoPPTX_Simple() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // Charger le document PDF
        Document document = new Document(documentFileName);

        // Instancier l'instance de PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // Enregistrer la sortie au format PPTX
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```

## Convertir PDF en PPTX avec des Diapositives comme Images

Dans le cas où vous avez besoin de convertir un PDF consultable en PPTX sous forme d'images au lieu de texte sélectionnable, Aspose.PDF fournit une telle fonctionnalité via la classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions). Pour cela, définissez la propriété SlidesAsImages de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) à 'true' comme indiqué dans l'exemple de code suivant.

Le code suivant montre le processus de conversion des fichiers PDF en format PPTX avec des diapositives sous forme d'images.

```java
public static void convertPDFtoPPTX_SlideAsImages() {
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
    String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

    // Charger le document PDF
    Document document = new Document(documentFileName);
    // Instancier l'instance de PptxSaveOptions
    PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();
    // Enregistrer la sortie au format PPTX
    pptxSaveOptions.setSlidesAsImages(true);

    document.save(pptxDocumentFileName, pptxSaveOptions);
    document.close();
}
```


## Afficher la progression sur la console avec Aspose.PDF pour Java ressemble à ceci :

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.PptxSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Convertir PDF en PPTX.
 */
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_ProgressDetails();
    }

    public static void convertPDFtoPPTX_ProgressDetails() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // Charger le document PDF
        Document document = new Document(documentFileName);

        // Instancier PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // Spécifier un gestionnaire de progression personnalisé
        pptx_save.setCustomProgressHandler(new ShowProgressOnConsole());

        // Enregistrer la sortie au format PPTX
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```


## Détail de la progression de la conversion PPTX

Aspose.PDF pour Java vous permet de suivre la progression de la conversion de PDF à PPTX. La classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) fournit la propriété [CustomProgressHandler](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlSaveOptions) qui peut être spécifiée à une méthode personnalisée pour suivre la progression de la conversion comme indiqué dans l'exemple de code suivant.

```java
package com.aspose.pdf.examples;

import java.time.LocalDateTime;

import com.aspose.pdf.ProgressEventType;
import com.aspose.pdf.UnifiedSaveOptions.ConversionProgressEventHandler;
import com.aspose.pdf.UnifiedSaveOptions.ProgressEventHandlerInfo;

class ShowProgressOnConsole extends ConversionProgressEventHandler{

    @Override
    public void invoke(ProgressEventHandlerInfo eventInfo) {        
        switch (eventInfo.EventType) {
            case ProgressEventType.TotalProgress:
                System.out.println(
                        String.format("%s  - Progression de la conversion : %d %%.", LocalDateTime.now().toString(), eventInfo.Value));
                break;
            case ProgressEventType.ResultPageCreated:
                System.out.println(String.format("%s  - Page résultat %s de %d mise en page créée.", LocalDateTime.now().toString(),
                        eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.ResultPageSaved:
                System.out.println(String.format("%s  - Page résultat %d de %d exportée.", LocalDateTime.now(), eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.SourcePageAnalysed:
                System.out.println(String.format("%s  - Page source %d de %d analysée.", LocalDateTime.now(),  eventInfo.Value, eventInfo.MaxValue));
                break;
            default:
                break;
        }
    }
```


{{% alert color="success" %}}
**Essayez de convertir un PDF en PowerPoint en ligne**

Aspose.PDF pour Java vous propose l'application en ligne gratuite ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en PPTX avec une application gratuite](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}