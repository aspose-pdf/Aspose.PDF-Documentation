---
title: Verificar limites de formas em gráficos PDF com Java
linktitle: Verificar limites de formas
type: docs
weight: 70
url: /pt/java/checking-shape-bounds/
description: Aprenda como validar limites de formas em coleções de gráficos PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validar limites de formas de gráfico em arquivos PDF usando Java
Abstract: Este artigo mostra como validar limites de formas em coleções de Graph usando Aspose.PDF for Java. Ele aborda habilitar a verificação estrita de limites, tentar adicionar uma forma fora do intervalo e tratar a exceção resultante, mantendo a gravação do documento.
---
Use `BoundsCheckMode` quando precisar garantir que as formas cabem dentro de um contêiner de gráfico.

## Validar limites da forma do gráfico

1. Crie um novo documento PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner e adicione-o à página.
1. Crie o [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) forma e configure sua geometria.
1. Habilite a verificação estrita de limites e tente adicionar a forma à coleção de gráficos com `BoundsCheckMode`.
1. Trate a exceção se a forma não couber.
1. Salve o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
