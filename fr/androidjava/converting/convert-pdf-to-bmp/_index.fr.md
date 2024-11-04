---
title: Convertir PDF en BMP 
linktitle: Convertir PDF en BMP
type: docs
weight: 40
url: /androidjava/convert-pdf-to-bmp/
lastmod: "2021-06-05"
description: Cet article décrit comment convertir des pages PDF en image BMP, convertir toutes les pages en images BMP et convertir une seule page PDF en image BMP avec Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

La classe [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) vous permet de convertir des pages PDF en images <abbr title="Bitmap Image File">BMP</abbr>. Cette classe fournit une méthode nommée [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) qui vous permet de convertir une page particulière du fichier PDF au format image BMP.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

La classe BmpDevice vous permet de convertir des pages PDF en images BMP.
 Cette classe fournit une méthode nommée process(..) qui vous permet de convertir une page particulière du fichier PDF en image BMP.

## Convertir une Page PDF en Image BMP

Pour convertir une page PDF en une image BMP :

1. Créez un objet de la classe Document, pour obtenir la page particulière que vous souhaitez convertir.
2. Appelez la méthode process(..) pour convertir la page en BMP.

L'extrait de code suivant vous montre comment convertir une page particulière en image BMP.

```java
//Convertir PDF en BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Créer un objet flux pour enregistrer l'image de sortie
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Créer un objet Résolution
            Resolution resolution = new Resolution(300);

            // Créer un objet BmpDevice avec une résolution particulière
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convertir une page particulière et enregistrer l'image dans le flux
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Fermer le flux
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Convertir Toutes les Pages PDF en Images BMP

Pour convertir toutes les pages d'un fichier PDF au format BMP, vous devez itérer pour obtenir chaque page individuelle et la convertir au format BMP. Le code suivant montre comment parcourir toutes les pages d'un fichier PDF et les convertir en BMP.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Boucle à travers toutes les pages du fichier PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Crée un objet stream pour enregistrer l'image de sortie
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Crée un objet Resolution
            Resolution resolution = new Resolution(300);
            // Crée un objet BmpDevice avec une résolution particulière
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convertit une page particulière et enregistre l'image dans le flux
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Ferme le flux
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


## Convertir une région particulière de page en Image (DOM)

Nous pouvons convertir des documents PDF en différents formats d'images en utilisant les objets de dispositifs d'image d'Aspose.PDF. Cependant, il y a parfois un besoin de convertir une région spécifique de la page en format image. Nous pouvons répondre à ce besoin en deux étapes. Tout d'abord, recadrez la page PDF à la région souhaitée et convertissez-la ensuite en image en utilisant l'objet de dispositif d'image souhaité.

Le code suivant vous montre comment convertir des pages PDF en images.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Obtenir le rectangle de la région particulière de la page
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // définir la valeur de CropBox selon le rectangle de la région de page souhaitée
        document.getPages().get_Item(1).setCropBox(pageRect);
        // enregistrer le document recadré dans le flux
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // ouvrir le document PDF recadré à partir du flux et le convertir en image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Créer un objet de résolution
        Resolution resolution = new Resolution(300);
        // Créer un dispositif BMP avec des attributs spécifiés
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Convertir une page particulière et enregistrer l'image dans le flux
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```