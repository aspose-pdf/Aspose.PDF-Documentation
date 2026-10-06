---
title: Adicionar Formas de Curva ao PDF em Java
linktitle: Adicionar Curva
type: docs
weight: 30
url: /pt/java/add-curve/
description: Aprenda como desenhar e preencher formas de curva em arquivos PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhar formas de curva em arquivos PDF usando Java
Abstract: Este artigo mostra como adicionar formas de curva a documentos PDF usando Aspose.PDF for Java. Ele aborda a criação de uma curva a partir de arrays de coordenadas e a aplicação de cor de traço ou cor de preenchimento dentro de um contêiner Graph.
---
Curvas em Aspose.PDF for Java são definidas por um array de coordenadas float passado para `Curve`.

## Adicionar um contorno de curva

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicionar um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Criar um [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) container e adicioná-lo à página.
1. Criar o [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) forma e configure seus pontos de controle.
1. Adicionar o [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) para o [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner.
1. Defina as propriedades de forma exigidas pelo exemplo, incluindo [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Salve o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCurve(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Curve curve1 = new Curve(new float[]{10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(curve1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
