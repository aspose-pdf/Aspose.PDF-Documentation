---
title: Comprobar los límites de la forma en gráficos PDF con Java
linktitle: Comprobar los límites de la forma
type: docs
weight: 70
url: /es/java/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Aprenda cómo validar los límites de forma en colecciones de gráficos PDF en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validar los límites de forma de gráfico en archivos PDF usando Java
Abstract: Este artículo muestra cómo validar los límites de forma en colecciones de Graph usando Aspose.PDF for Java. Cubre la activación de la verificación estricta de límites, el intento de agregar una forma fuera de rango y el manejo de la excepción resultante mientras se sigue guardando el documento.
---
Usar `BoundsCheckMode` cuando necesitas asegurarte de que las formas se ajusten dentro de un contenedor de gráfico.

## Validar los límites de la forma del gráfico

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Crear un [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contenedor y agrégalo a la página.
1. Crear el [Rectángulo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) forma y configura su geometría.
1. Habilitar la verificación estricta de límites y intentar agregar la forma a la colección de gráficos con `BoundsCheckMode`.
1. Manejar la excepción si la forma no encaja.
1. Guardar el PDF de salida [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
