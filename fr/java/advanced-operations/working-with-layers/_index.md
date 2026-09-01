---
title: Travailler avec des calques PDF à l'aide de Java
linktitle: Travailler avec des calques PDF
type: docs
weight: 50
url: /java/working-with-pdf-layers/
description: Découvrez comment ajouter, verrouiller, extraire, aplatir et fusionner des calques PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gérer les calques PDF avec Java
Abstract: Cet article explique comment utiliser les calques PDF, également appelés groupes de contenu facultatifs, à l'aide d'Aspose.PDF pour Java. Découvrez comment ajouter des calques à une page, verrouiller un calque existant, extraire le contenu des calques dans des fichiers ou des flux, aplatir le contenu en calques et fusionner des calques en un seul.
---
Aspose.PDF pour Java expose les couches PDF via l'API `Layer` sur chaque page. Vous pouvez créer des groupes de contenu facultatifs, modifier leur comportement et exporter ou aplatir leur contenu si nécessaire.


## 
Ajouter des calques à une page PDF


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Créez et configurez les objets [Layer] (https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) requis sur la page.
1. Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void addLayers(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Layer layer = new Layer("oc1", "Red Line");
        layer.getContents().add(new SetRGBColorStroke(1, 0, 0));
        layer.getContents().add(new MoveTo(500, 700));
        layer.getContents().add(new LineTo(400, 700));
        layer.getContents().add(new Stroke());
        page.getLayers().add(layer);

        document.save(outputFile.toString());
    }
}
```


L'exemple complet crée trois calques distincts avec un contenu de lignes rouges, vertes et bleues.


## 
Verrouiller un calque


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Accédez à la [Page] cible (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et obtenez sa collection [Couche] (https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. Verrouillez la cible [Couche] (https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).

1. 
Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void lockLayer(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        if (!page.getLayers().isEmpty()) {
            Layer layer = page.getLayers().getFirst();
            layer.lock();
            document.save(outputFile.toString());
        }
    }
}
```
