---
title: Verifique os limites da forma em gráficos PDF com Java
linktitle: Verifique os limites da forma
type: docs
weight: 70
url: /java/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Aprenda como validar limites de forma em coleções de gráficos PDF em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Valide os limites da forma do gráfico em arquivos PDF usando Java
Abstract: Este artigo mostra como validar limites de forma em coleções Graph usando Aspose.PDF para Java. Abrange a ativação da verificação de limites estritos, a tentativa de adicionar uma forma fora do intervalo e o tratamento da exceção resultante enquanto salva o documento.
---
Use `BoundsCheckMode` quando precisar garantir que as formas caibam dentro de um contêiner de gráfico.

## Validar limites da forma do gráfico

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione uma [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um contêiner [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) e adicione-o à página.
1. Crie a forma [Retângulo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) e configure sua geometria.
1. Habilite a verificação de limites estritos e tente adicionar a forma à coleção de gráficos com `BoundsCheckMode`.
1. Trate a exceção se a forma não couber.
1. Salve o PDF de saída [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
