---
title: Supprimer des images d'un fichier PDF à l'aide de Java
linktitle: Supprimer des images
type: docs
weight: 20
url: /java/delete-images-from-pdf-file/
description: Découvrez comment supprimer des images incorporées dans des fichiers PDF en Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Supprimer les images intégrées des fichiers PDF avec Java
Abstract: Cet article montre comment supprimer des images de documents PDF à l'aide d'Aspose.PDF pour Java. L'exemple supprime une ressource image de la première page par son index dans la collection d'images de page, puis enregistre le document modifié.
---
Utilisez la collection de ressources d’images de page lorsque vous devez supprimer des images incorporées d’une page PDF.


## 
Supprimer une image intégrée par index


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Accédez aux ressources d'images sur la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Supprimez l'image cible de la collection de ressources de page par son index.
1. Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```
