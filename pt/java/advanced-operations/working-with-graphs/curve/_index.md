---
title: Adicione formas curvas ao PDF em Java
linktitle: Adicionar curva
type: docs
weight: 30
url: /java/add-curve/
description: Aprenda como desenhar e preencher formas curvas em arquivos PDF em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhe formas curvas em arquivos PDF usando Java
Abstract: Este artigo mostra como adicionar formas curvas a documentos PDF usando Aspose.PDF para Java. Ele cobre a criação de uma curva a partir de matrizes de coordenadas e a aplicação da cor do traço ou da cor de preenchimento dentro de um contêiner Gráfico.
---
As curvas em Aspose.PDF para Java são definidas por uma matriz de coordenadas flutuantes passada para `Curve`.

## Adicione um contorno de curva

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione uma [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um contêiner [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) e adicione-o à página.
1. Crie a forma [Curva](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) e configure seus pontos de controle.
1. Adicione a [Curva](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) ao contêiner [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Defina as propriedades de forma exigidas pelo exemplo, incluindo [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Salve o PDF de saída [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
