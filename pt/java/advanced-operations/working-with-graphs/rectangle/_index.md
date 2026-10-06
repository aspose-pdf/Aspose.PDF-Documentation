---
title: Adicionar formas de retângulo ao PDF em Java
linktitle: Adicionar retângulo
type: docs
weight: 50
url: /pt/java/add-rectangle/
description: Aprenda a desenhar e preencher formas de retângulo em arquivos PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhar formas de retângulo em arquivos PDF usando Java
Abstract: Este artigo mostra como adicionar formas de retângulo a documentos PDF usando Aspose.PDF for Java. Ele aborda retângulos com contorno, preenchimentos sólidos, preenchimentos em degradê, transparência alfa e controle de ordem Z para formas sobrepostas.
---
## Adicionar um contorno de retângulo

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicionar um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Criar um [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner e adicioná-lo à página.
1. Criar o [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) forma e configurar sua geometria.
1. Adicionar o [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) para o [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner.
1. Salvar o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## Preencha um retângulo com cor sólida ou degradê

Os exemplos de retângulo incluem:

- `createRectangleFilled` para um preenchimento sólido com `Color.getRed()`
- `addDrawingWithGradientFill` para um `GradientAxialShading` preencher

## Use transparência alfa

`createRectangleWithAlphaColorChannel` aplica cores translúcidas com `Color.fromArgb(...)` para que os retângulos sobrepostos permaneçam visíveis.

## Controlar a ordem z dos retângulos

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicionar um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Defina o necessário [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) tamanho.
1. Adicione o configurado [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) formas na página de destino com a ordem z necessária.
1. Salvar o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
