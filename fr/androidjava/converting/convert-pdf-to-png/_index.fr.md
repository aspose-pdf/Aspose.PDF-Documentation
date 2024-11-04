---
title: Convertir PDF en PNG
linktitle: Convertir PDF en PNG
type: docs
weight: 20
url: /androidjava/convert-pdf-to-png/
lastmod: "2021-06-05"
description: Cette page décrit comment convertir des pages PDF en images PNG, convertir toutes les pages et des pages uniques en images PNG avec Aspose.PDF pour Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Utilisez la bibliothèque **Aspose.PDF pour Android via Java** pour convertir des pages PDF en images <abbr title="Portable Network Graphics">PNG</abbr> de manière accessible et pratique.

La classe PngDevice vous permet de convertir des pages PDF en images PNG. Cette classe fournit une méthode nommée Process qui vous permet de convertir une page particulière du fichier PDF au format image PNG.

## Convertir les pages PDF en images PNG

Pour convertir toutes les pages d'un fichier PDF en fichiers PNG, parcourez les pages individuelles et convertissez chacune au format PNG. Le fragment de code suivant montre comment parcourir toutes les pages d'un fichier PDF et convertir chacune en image PNG.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## Convertir une seule page PDF en image PNG

Passez l'indice de la page comme argument à la méthode Process(..).
L'extrait de code suivant montre les étapes pour convertir la première page du PDF au format PNG.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Créer un objet stream pour enregistrer l'image de sortie
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Créer un objet Résolution
            Resolution resolution = new Resolution(300);

            // Créer un objet PngDevice avec une résolution particulière
            PngDevice PngDevice = new PngDevice(resolution);

            // Convertir une page particulière et enregistrer l'image dans le stream
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Fermer le stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Convertir toutes les pages PDF en image PNG

Aspose.PDF pour Android via Java vous montre comment convertir toutes les pages d'un fichier PDF en images :

1. Parcourez toutes les pages du fichier.
1. Convertissez chaque page individuellement :
    1. Créez un objet de la classe Document pour charger le document PDF.
    1. Obtenez la page que vous souhaitez convertir.
    1. Appelez la méthode Process pour convertir la page en PNG.

Le code suivant vous montre comment convertir toutes les pages PDF en images PNG.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Parcourez toutes les pages du fichier PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Créez un objet de stream pour enregistrer l'image de sortie
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Créez un objet Resolution
            Resolution resolution = new Resolution(300);
            // Créez un objet JpegDevice avec une résolution particulière
            PngDevice JpegDevice = new PngDevice(resolution);

            // Convertissez une page particulière et enregistrez l'image dans le flux
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Fermez le flux
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

Aspose.PDF pour Android via Java vous montre comment convertir une page particulière au format PNG :

```java
public void convertPDFtoPNG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Obtenir le rectangle de la région de la page particulière
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // définir la valeur de CropBox selon le rectangle de la région de page souhaitée
        document.getPages().get_Item(1).setCropBox(pageRect);
        // enregistrer le document rogné dans le flux
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // ouvrir le document PDF rogné depuis le flux et convertir en image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Créer un objet Resolution
        Resolution resolution = new Resolution(300);
        // Créer un périphérique Jpeg avec des attributs spécifiés
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Convertir une page particulière et enregistrer l'image dans le flux
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```