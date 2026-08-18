---
title: Adicione formas retangulares ao PDF em Java
linktitle: Adicionar retângulo
type: docs
weight: 50
url: /java/add-rectangle/
description: Aprenda como desenhar e preencher formas retangulares em arquivos PDF em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhe formas retangulares em arquivos PDF usando Java
Abstract: Este artigo mostra como adicionar formas retangulares a documentos PDF usando Aspose.PDF para Java. Abrange retângulos delineados, preenchimentos sólidos, preenchimentos gradientes, transparência alfa e controle de ordem z para formas sobrepostas.
---
## Adicione um contorno retangular

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione uma [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um contêiner [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) e adicione-o à página.
1. Crie a forma [Retângulo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) e configure sua geometria.
1. Adicione o [Retângulo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) ao contêiner [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Salve o PDF de saída [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 300.0);
        page.getParagraphs().add(graph);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Rectangle rectangle = new Rectangle(20, 20, 350, 250);
        graph.getShapes().addItem(rectangle);

        document.save(outputFile.toString());
    }
}
```

## Preencha um retângulo com cor sólida ou gradiente

Os exemplos de retângulo incluem:

- `createRectangleFilled` para um preenchimento sólido com `Color.getRed()`
- `addDrawingWithGradientFill` para um preenchimento `GradientAxialShading`

## Use transparência alfa

`createRectangleWithAlphaColorChannel` aplica cores translúcidas com `Color.fromArgb(...)` para que os retângulos sobrepostos permaneçam visíveis.

## Controlar a ordem z dos retângulos

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione uma [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Defina o tamanho necessário da [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Adicione as formas [Retângulo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) configuradas à página de destino com a ordem z necessária.
1. Salve o PDF de saída [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void controlZOrderOfRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(375, 300);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setTop(0);

        addRectangleToPage(page, 50, 40, 60, 40, Color.getRed(), 2);
        addRectangleToPage(page, 20, 20, 30, 30, Color.getBlue(), 1);
        addRectangleToPage(page, 40, 40, 60, 30, Color.getGreen(), 0);

        document.save(outputFile.toString());
    }
}
```
