---
title: Extraire des Images depuis un PDF 
linktitle: Extraire des Images
type: docs
weight: 20
url: fr/androidjava/extract-images-from-the-pdf-file/
description: Comment extraire une partie de l'image d'un PDF en utilisant Aspose.PDF pour Android via Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Chaque page dans un document PDF contient des ressources (images, formulaires et polices). Nous pouvons accéder à ces ressources en appelant la méthode [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). La classe [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contient [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) et nous pouvons obtenir la liste des images en appelant la méthode [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Ainsi, pour extraire une image d'une page, nous devons obtenir une référence à la page, ensuite aux ressources de la page et enfin à la collection d'images.

Une image particulière peut être extraite par exemple par index.

The index de l'image renvoie un objet [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage). Cet objet fournit une méthode [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) qui peut être utilisée pour enregistrer l'image extraite. Le code suivant montre comment extraire des images d'un fichier PDF.

```java
public void extractImage () {
    // Ouvrir le document
    try {
        document=new Document(inputStream);
    } catch (Exception e) {
        resultMessage.setText(e.getMessage());
        return;
    }

    com.aspose.pdf.Page page=document.getPages().get_Item(1);
    com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
    // Extraire une image particulière
    com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
    File file=new File(fileStorage, "extracted-image.jpeg");
    try {
        java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
        // Enregistrer l'image de sortie
        xImage.save(outputImage, ImageType.getJpeg());
        outputImage.close();
    } catch (java.io.IOException e) {
        resultMessage.setText(e.getMessage());
        return;
    }
    resultMessage.
}
```