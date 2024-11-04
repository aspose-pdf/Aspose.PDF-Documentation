---
title: Convertir PDF en JPG
linktitle: Convertir PDF en JPG
type: docs
weight: 10
url: /androidjava/convert-pdf-to-jpg/
description: Cette page décrit comment convertir des pages PDF en image JPEG, convertir toutes les pages et des pages uniques en images JPEG avec Aspose.PDF pour Android via Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Convertir des pages PDF en images JPG

La classe JpegDevice vous permet de convertir des pages PDF en images JPEG. Cette classe fournit une méthode nommée process(..) qui vous permet de convertir une page particulière du fichier PDF en image JPEG.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et visualiser les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}

## Convertir une seule page PDF en image JPG

Aspose.PDF pour Android via Java vous permet de convertir une seule page au format JPEG.

Pour convertir juste une page en une image JPEG :

1. Créez un objet de la classe Document pour obtenir la page que vous souhaitez convertir.
1. Appelez la méthode process(..) pour convertir la page en image JPEG.

Le code suivant montre les étapes pour convertir la première page d'un PDF au format Jpeg.

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // Créez un objet flux pour enregistrer l'image de sortie
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Créez un objet Résolution
            Resolution resolution = new Resolution(300);

            // Créez un objet JpegDevice avec une résolution particulière
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convertir une page particulière et enregistrer l'image dans le flux
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // Fermer le flux
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Convertir toutes les pages PDF en images JPG

Aspose.PDF pour Android via Java vous permet de convertir toutes les pages d'un fichier PDF en images :

1. Parcourir toutes les pages du fichier.
1. Convertir chaque page individuellement :
    - Créer un objet de la classe Document pour charger le document PDF.
    - Obtenir la page que vous souhaitez convertir.
    - Appeler la méthode Process pour convertir la page en Jpeg.

Le code suivant vous montre comment convertir toutes les pages PDF en images Jpeg.

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Parcourir toutes les pages du fichier PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Créer un objet stream pour enregistrer l'image de sortie
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Créer un objet Resolution
            Resolution resolution = new Resolution(300);
            // Créer un objet JpegDevice avec une résolution particulière
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convertir une page particulière et sauvegarder l'image dans le stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Fermer le stream
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


## Convertir une page PDF particulière en image JPG

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Obtenir le rectangle de la région de page particulière
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // définir la valeur de CropBox selon le rectangle de la région de page souhaitée
        document.getPages().get_Item(1).setCropBox(pageRect);
        // enregistrer le document recadré dans le flux
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // ouvrir le document PDF recadré depuis le flux et convertir en image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Créer un objet Resolution
        Resolution resolution = new Resolution(300);
        // Créer un appareil Jpeg avec des attributs spécifiés
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // Convertir une page particulière et enregistrer l'image dans le flux
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```