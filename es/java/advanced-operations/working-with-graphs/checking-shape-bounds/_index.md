---
title: Verifique los límites de las formas en gráficos PDF con Java
linktitle: Comprobar límites de forma
type: docs
weight: 70
url: /java/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Aprenda a validar límites de formas en colecciones de gráficos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Valide los límites de la forma del gráfico en archivos PDF usando Java
Abstract: Este artículo muestra cómo validar límites de formas en colecciones de Graph usando Aspose.PDF para Java. Cubre habilitar la verificación de límites estrictos, intentar agregar una forma fuera de rango y manejar la excepción resultante mientras se guarda el documento.
---
Utilice `BoundsCheckMode` cuando necesite asegurarse de que las formas encajen dentro de un contenedor de gráficos.


## 
Validar límites de forma de gráfico


1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. 
Cree un contenedor [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) y agréguelo a la página.
1. Crea la forma [Rectángulo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) y configura su geometría.

1. 
Habilite la verificación de límites estrictos e intente agregar la forma a la colección de gráficos con `BoundsCheckMode`.

1. 
Maneje la excepción si la forma no encaja.

1. 
Guarde el [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
