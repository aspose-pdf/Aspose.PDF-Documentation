---
title: Enregistrer le document PDF
linktitle: Enregistrer
type: docs
weight: 30
url: fr/java/save-pdf-document/
description: Apprenez à enregistrer un fichier PDF avec la bibliothèque Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Enregistrer le document PDF dans le système de fichiers

Vous pouvez enregistrer le document PDF créé ou manipulé dans le système de fichiers en utilisant la méthode Save de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
Lorsque vous ne fournissez pas le type de format (options), le document est enregistré au format Aspose.PDF v.1.7 (*.pdf).

```java
package com.aspose.pdf.examples;


import java.io.FileOutputStream;

import java.nio.file.Path;
import java.nio.file.Paths;
import com.aspose.pdf.*;

public final class BasicOperationsSave {

    private BasicOperationsSave() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) {
        SaveDocument();
        SaveDocumentStream();
        SaveDocumentAsPDFx();
    }

    public static void SaveDocument() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // effectuer quelques manipulations, par exemple ajouter une nouvelle page vide
        pdfDocument.getPages().add();
        pdfDocument.save(modifiedFileName);
    }
```


## Enregistrer un document PDF dans un flux

Vous pouvez également enregistrer le document PDF créé ou manipulé dans un flux en utilisant les surcharges des méthodes Save.

```java
public static void SaveDocumentStream() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // faire quelques manipulations, par exemple ajouter une nouvelle page vide
        pdfDocument.getPages().add();
        try {
            pdfDocument.save(new FileOutputStream(modifiedFileName));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

```

## Enregistrer un document PDF dans des applications Web

Pour enregistrer des documents dans des applications Web, vous pouvez utiliser les méthodes proposées ci-dessus. De plus, la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) a une méthode Save surchargée.
```java
    // @RequestMapping(value = "/files/{file_name}", method = RequestMethod.GET)
    // public void getFile(@PathVariable("file_name") String fileName, HttpServletResponse response) {
    //     try {
    //         response.setContentType("application/pdf");
    //         // obtenir votre fichier en tant qu'InputStream
    //         InputStream is = new FileInputStream(_dataDir + fileName);
    //         // le copier dans l'OutputStream de la réponse
    //         org.apache.commons.io.IOUtils.copy(is, response.getOutputStream());
    //         response.flushBuffer();
    //     } catch (IOException ex) {
    //         log.info("Error writing file to output stream. Filename was '{}'", fileName, ex);
    //         throw new RuntimeException("IOError writing file to output stream");
    //     }
    // }
```


Pour une explication plus détaillée, veuillez vous référer à la section [Showcase]().

## Enregistrer au format PDF/A ou PDF/X

PDF/A est une version du format de document portable (PDF) standardisée par l'ISO pour une utilisation dans l'archivage et la préservation à long terme des documents électroniques. PDF/A diffère du PDF en ce qu'il interdit des fonctionnalités non adaptées à l'archivage à long terme, telles que la liaison des polices (par opposition à l'intégration des polices) et le cryptage. Les exigences ISO pour les visionneuses PDF/A incluent des directives de gestion des couleurs, la prise en charge des polices intégrées, et une interface utilisateur pour lire les annotations intégrées.

PDF/X est un sous-ensemble de la norme ISO PDF. Le but de PDF/X est de faciliter l'échange de graphiques, et il a donc une série d'exigences liées à l'impression qui ne s'appliquent pas aux fichiers PDF standard.

Dans les deux cas, la méthode Save est utilisée pour stocker les documents, tandis que les documents doivent être préparés en utilisant la méthode Convert.

```java
public static void SaveDocumentAsPDFx() {
        Document pdfDocument = new Document("../../../Samples/SimpleResume.pdf");
        pdfDocument.getPages().add();
        pdfDocument.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
        pdfDocument.save("../../../Samples/SimpleResume_X3.pdf");
    }

}
```