---
title: Extraire des images d'un PDF (facades)
type: docs
weight: 30
url: /java/extract-images/
description: Cette section explique comment extraire des images avec Aspose.PDF Facades en utilisant la classe PdfExtractor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La classe [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) vous permet d'extraire des images d'un fichier PDF.
 First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) class and bind input PDF file using bindPdf method. After that, call [extractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of hasNextImage and getNextImage methods. You need to loop through all the extracted images using a while loop. In order to save the images to disk, you can call the overload of the getNextImage method which takes file path as argument. The following code snippet shows you how to extract images from the whole PDF to files.

Tout d'abord, vous devez créer un objet de la classe [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) et lier le fichier PDF d'entrée en utilisant la méthode bindPdf. Après cela, appelez la méthode [extractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--) pour extraire toutes les images en mémoire. Une fois les images extraites, vous pouvez obtenir ces images à l'aide des méthodes hasNextImage et getNextImage. Vous devez parcourir toutes les images extraites en utilisant une boucle while. Afin de sauvegarder les images sur le disque, vous pouvez appeler la surcharge de la méthode getNextImage qui prend le chemin du fichier comme argument. Le fragment de code suivant vous montre comment extraire des images de l'ensemble du PDF vers des fichiers.

```java   
public static void ExtractImages()
 {
    // Créer un extracteur et le lier au document
    Document document = new Document(_dataDir + "sample.pdf");
    PdfExtractor extractor = new PdfExtractor(document);
    extractor.setStartPage(1);
    extractor.setEndPage(3);            

    // Exécuter l'extracteur
    extractor.extractImage();
    int imageNumber = 1;
    // Itérer à travers la collection d'images extraites
    while (extractor.hasNextImage())
    {
        // Récupérer l'image de la collection et la sauvegarder dans un fichier
        extractor.getNextImage(_dataDir + String.format("image%03d.png", imageNumber++),ImageType.getPng());
    }
}
```