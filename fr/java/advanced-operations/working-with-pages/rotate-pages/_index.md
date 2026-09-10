---
title: Faire pivoter les pages PDF en Java
linktitle: Rotation des pages PDF
type: docs
weight: 110
url: /java/rotate-pages/
description: Découvrez comment faire pivoter des pages PDF et modifier l'orientation des pages en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Faire pivoter les pages PDF avec Java
Abstract: Cet article explique comment faire pivoter des pages PDF à l'aide d'Aspose.PDF pour Java. L'exemple parcourt toutes les pages d'un document, applique une rotation de 90 degrés et enregistre le PDF mis à jour.
---
Utilisez l'API de rotation de page lorsque vous devez modifier l'orientation sur une ou plusieurs pages.


## 
Faire pivoter toutes les pages de 90 degrés



Utilisez cet exemple lorsque chaque page du document doit être tournée dans le sens des aiguilles d’une montre.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez tous les objets [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et définissez la valeur de rotation.
1. Enregistrez le PDF mis à jour.

```java
public static void rotatePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.setRotate(Rotation.on90);
        }
        document.save(outputFile.toString());
    }
}
```
