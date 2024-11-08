---
title: Extraire des images du PDF 
linktitle: Extraire des images
type: docs
weight: 20
url: /fr/java/extract-images-from-the-pdf-file/
description: Comment extraire une partie de l'image du PDF en utilisant Aspose.PDF pour Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Chaque page dans le document PDF contient des ressources (images, formulaires et polices). Nous pouvons accéder à ces ressources en appelant la méthode [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). La classe [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contient [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) et nous pouvons obtenir la liste des images en appelant la méthode [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Ainsi, pour extraire une image d'une page, nous devons obtenir la référence de la page, ensuite des ressources de la page et enfin de la collection d'images. Nous pouvons extraire une image particulière, par exemple par index.

L'index de l'image renvoie un objet [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage).
Cet objet fournit une méthode [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) qui peut être utilisée pour enregistrer l'image extraite. Le code suivant montre comment extraire des images d'un fichier PDF.

```java
public static void Extract_Images(){
        // Le chemin vers le répertoire des documents.
        String _dataDir = "/home/admin1/pdf-examples/Samples/";
        String filePath = _dataDir + "ExtractImages.pdf";

        // Charger le document PDF
        com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

        com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection = page.getResources().getImages();
        // Extraire une image particulière
        com.aspose.pdf.XImage xImage = xImageCollection.get_Item(1);

        try {
            java.io.FileOutputStream outputImage = new java.io.FileOutputStream(_dataDir + "output.jpg");
            // Enregistrer l'image de sortie
            xImage.save(outputImage);
            outputImage.close();
        } catch (java.io.FileNotFoundException e) {
            // TODO: gérer l'exception
            e.printStackTrace();
        } catch (java.io.IOException e) {
            // TODO: gérer l'exception
            e.printStackTrace();
        }
    }
```