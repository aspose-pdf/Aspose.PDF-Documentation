---
title: Convertir le PDF en BMP
linktitle: Convertir le PDF en BMP
type: docs
weight: 40
url: /fr/androidjava/convert-pdf-to-bmp/
lastmod: "2026-07-01"
description: Cet article décrit comment convertir des pages PDF en image BMP, convertir toutes les pages en images BMP et convertir une seule page PDF en image BMP avec Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Le [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) La classe vous permet de convertir des pages PDF en <abbr title="Bitmap Image File">BMP</abbr> images. Cette classe fournit une méthode nommée [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) qui permet de convertir une page particulière du fichier PDF au format d'image Bmp.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

La classe BmpDevice vous permet de convertir des pages PDF en images BMP. Cette classe fournit une méthode nommée process(..) qui vous permet de convertir une page particulière du fichier PDF en image BMP.

## Convertir une page PDF en image BMP

Pour convertir une page PDF en image BMP :

1. Créez un objet de la classe Document, pour obtenir la page particulière que vous souhaitez convertir.
1. Appelez la méthode process(..) pour convertir la page en BMP.

L'extrait de code suivant montre comment convertir une page particulière en image BMP.

```java
//Convert PDF to BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Convertir toutes les pages PDF en images BMP

Pour convertir toutes les pages d'un fichier PDF au format BMP, vous devez itérer afin d'obtenir chaque page individuelle et la convertir au format BMP. L'extrait de code suivant vous montre comment parcourir toutes les pages d'un fichier PDF et les convertir en BMP.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

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

## Convertir une région de page particulière en image (DOM)

Nous pouvons convertir des documents PDF en différents formats d'image à l'aide des objets de périphériques d'image d'Aspose.PDF. Cependant, il arrive parfois qu'il soit nécessaire de convertir une région de page particulière en format d'image. Nous pouvons satisfaire cette exigence en deux étapes. Tout d'abord, recadrer la page PDF à la région souhaitée, puis la convertir en image à l'aide de l'objet de périphérique d'image souhaité.

Le fragment de code suivant vous montre comment convertir des pages PDF en images.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
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
        // Create BMP device with specified attributes
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```
