---
title: Convertir le PDF en PNG
linktitle: Convertir le PDF en PNG
type: docs
weight: 20
url: /fr/androidjava/convert-pdf-to-png/
lastmod: "2026-07-01"
description: Cette page décrit comment convertir des pages PDF en image PNG, convertir toutes les pages ou des pages individuelles en images PNG avec Aspose.PDF for Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Utilisez la bibliothèque **Aspose.PDF for Android via Java** pour convertir les pages PDF en <abbr title="Portable Network Graphics">PNG</abbr> Images de manière accessible et pratique.

La classe PngDevice vous permet de convertir des pages PDF en images PNG. Cette classe fournit une méthode nommée Process qui vous permet de convertir une page particulière du fichier PDF au format image PNG.

## Convertir les pages PDF en images PNG

Pour convertir toutes les pages d'un fichier PDF en fichiers PNG, parcourez les pages individuelles et convertissez chacune au format PNG. Le fragment de code suivant montre comment parcourir toutes les pages d'un fichier PDF et convertir chacune en image PNG.

{{% alert color="primary" %}} 

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## Convertir une page PDF unique en image PNG

Passez l'index de la page en tant qu'argument à la méthode Process(..).
Le fragment de code suivant montre les étapes pour convertir la première page du PDF au format PNG.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create PngDevice object with particular resolution
            PngDevice PngDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Convertir toutes les pages PDF en image PNG

Aspose.PDF for Android via Java vous montre comment convertir toutes les pages d'un fichier PDF en images :

1. Parcourir toutes les pages du fichier.
1. Convertir chaque page individuellement:
    1. Créer un objet de la classe Document pour charger le document PDF.
    1. Obtenir la page que vous souhaitez convertir.
    1. Appelez la méthode Process pour convertir la page en Png.

Le fragment de code suivant vous montre comment convertir toutes les pages PDF en images PNG.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create JpegDevice object with particular resolution
            PngDevice JpegDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Close the stream
            try {
                imageStream.close();
            } catch (Exception e) {
                resultMessage.setText(e.getMessage());
                return;
            }
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Convertir une page PDF particulière en image PNG

Aspose.PDF for Android via Java vous montre comment convertir une page particulière au format PNG :

```java
public void convertPDFtoPNG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get rectangle of particular page region
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // set CropBox value as per rectangle of desired page region
        document.getPages().get_Item(1).setCropBox(pageRect);
        // save cropped document into stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // open cropped PDF document from stream and convert to image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create Jpeg device with specified attributes
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
