---
title: Extraire les polices d'un PDF via Java
linktitle: Extraire les polices d'un PDF
type: docs
weight: 30
url: /java/extract-fonts-from-pdf/
description: Utilisez Aspose.PDF pour Java pour inspecter et extraire les polices utilisées dans un document PDF.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire des polices d'un PDF à l'aide de Java
Abstract: Cet article explique comment inspecter les polices utilisées dans un document PDF avec Aspose.PDF pour Java. Il montre comment ouvrir un PDF, appeler `getFontUtilities().getAllFonts()` et parcourir les objets de police résultants pour lire leurs noms.
---
Utilisez l'extraction de polices lorsque vous devez auditer la typographie d'un document, inspecter les ressources intégrées ou vérifier l'utilisation des polices avant les flux de conversion ou d'archivage.


1. 
Ouvrez le PDF source dans une instance [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Appelez `document.getFontUtilities().getAllFonts()` pour collecter chaque ressource [Font] (https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) référencée par le document.

1. 
Parcourez les objets [Font] (https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) extraits et lisez chaque nom de police à partir des métadonnées de police.

1. 
Imprimez les noms de police afin que la typographie du document puisse être auditée ou exportée.

```java
public static void extractFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Font[] fonts = document.getFontUtilities().getAllFonts();
        for (Font font : fonts) {
            System.out.println(font.getFontName());
        }
    }
}
```
