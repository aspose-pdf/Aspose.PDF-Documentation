---
title: Comprobar los límites de forma en gráficos PDF con Java
linktitle: Comprobar los límites de forma
type: docs
weight: 70
url: /es/java/checking-shape-bounds/
description: Aprenda cómo validar los límites de forma en colecciones de gráficos PDF en Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validar los límites de forma de los gráficos en archivos PDF usando Java
Abstract: Este artículo muestra cómo validar los límites de forma en colecciones de Graph utilizando Aspose.PDF for Java. Cubre la habilitación de la comprobación estricta de límites, el intento de agregar una forma fuera de rango y el manejo de la excepción resultante mientras se sigue guardando el documento.
---
Utilice `BoundsCheckMode` cuando necesita asegurarse de que las formas encajen dentro de un contenedor de gráfico.

## Validar los límites de la forma del gráfico

1. Cree un nuevo PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Cree un [`Graph`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor y añádalo a la página.
1. Cree el [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) forma y configure su geometría.
1. Habilite la comprobación estricta de límites y intente agregar la forma a la colección de gráficos con `BoundsCheckMode`.
1. Maneje la excepción si la forma no encaja.
1. Guarde el PDF de salida [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
