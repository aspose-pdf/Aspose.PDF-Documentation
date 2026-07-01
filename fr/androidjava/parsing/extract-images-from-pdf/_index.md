---
title: Extraire les images du PDF
linktitle: Extraire les images
type: docs
weight: 20
url: /fr/androidjava/extract-images-from-the-pdf-file/
description: Comment extraire une partie de l'image d'un PDF en utilisant Aspose.PDF for Android via Java
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Chaque page d'un document PDF contient des ressources (images, formulaires et polices). Nous pouvons accéder à ces ressources en appelant [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) méthode. Classe [Ressources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contient [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) et nous pouvons obtenir la liste des images en appelant [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) méthode.

Ainsi, pour extraire une image d'une page, nous devons obtenir la référence à la page, ensuite les ressources de la page et enfin la collection d'images.
Image particulière que nous pouvons extraire, par exemple, par indice.

L'indice de l'image renvoie un [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) objet.
Cet objet fournit un [Enregistrer](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) méthode pouvant être utilisée pour enregistrer l'image extraite. Le fragment de code suivant montre comment extraire des images d'un fichier PDF.

 ```java
 public void extractImage () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.Page page=document.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
        // Extract a particular image
        com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
        File file=new File(fileStorage, "extracted-image.jpeg");
        try {
            java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
            // Save output image
            xImage.save(outputImage, ImageType.getJpeg());
            outputImage.close();
        } catch (java.io.IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.
          }
```

