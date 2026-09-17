---
title: Extraire des images d'un PDF à l'aide de Java
linktitle: Extraire des images d'un PDF
type: docs
weight: 20
url: /java/extract-images-from-the-pdf-file/
description: Découvrez comment extraire des images intégrées à partir de fichiers PDF avec Aspose.PDF pour Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire des images d'un PDF via Java
Abstract: Cet article explique comment extraire des images incorporées à partir d'un document PDF avec Aspose.PDF pour Java. Il montre comment ouvrir le PDF source, accéder à une image de la collection de ressources de la page et enregistrer le XImage extrait dans un fichier externe.
---
Extrayez des images de pages PDF lorsque vous devez réutiliser des graphiques intégrés, inspecter des ressources documentaires ou exporter des images pour un traitement en aval.


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ouvrez un flux de sortie pour le fichier image extrait.

1. 
Obtenez la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) du document et accédez à sa collection `Resources.Images`.

1. 
Récupérez l'objet [XImage] (https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) requis à partir de cette collection d'images par index.

1. 
Appelez `image.save(outputImage)` pour écrire les octets de l'image extraite dans le flux cible.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
