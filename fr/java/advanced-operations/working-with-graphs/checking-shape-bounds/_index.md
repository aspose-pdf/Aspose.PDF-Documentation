---
title: Vérifier les limites de forme dans les graphiques PDF avec Java
linktitle: Vérifier les limites de la forme
type: docs
weight: 70
url: /java/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Découvrez comment valider les limites de forme dans les collections de graphiques PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Valider les limites de la forme du graphique dans les fichiers PDF à l'aide de Java
Abstract: Cet article montre comment valider les limites de forme dans les collections Graph à l'aide d'Aspose.PDF pour Java. Il couvre l'activation de la vérification stricte des limites, la tentative d'ajout d'une forme hors plage et la gestion de l'exception résultante tout en enregistrant le document.
---
Utilisez `BoundsCheckMode` lorsque vous devez vous assurer que les formes tiennent dans un conteneur graphique.


## 
Valider les limites de la forme du graphique


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Créez un conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) et ajoutez-le à la page.
1. Créez la forme [Rectangle] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) et configurez sa géométrie.

1. 
Activez la vérification des limites strictes et essayez d'ajouter la forme à la collection de graphiques avec `BoundsCheckMode`.

1. 
Gérez l'exception si la forme ne correspond pas.

1. 
Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void checkShapeBounds(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 100.0);
        graph.setTop(10);
        graph.setLeft(15);
        graph.setBorder(new BorderInfo(BorderSide.Box, 1, Color.getBlack()));
        page.getParagraphs().add(graph);

        Rectangle rectangle = new Rectangle(-1, 0, 50, 50);
        rectangle.getGraphInfo().setFillColor(Color.getTomato());
        try {
            graph.getShapes().updateBoundsCheckMode(BoundsCheckMode.ThrowExceptionIfDoesNotFit);
            graph.getShapes().addItem(rectangle);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }

        document.save(outputFile.toString());
    }
}
```
