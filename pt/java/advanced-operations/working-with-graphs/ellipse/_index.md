---
title: Adicionar formas de elipse ao PDF em Java
linktitle: Adicionar elipse
type: docs
weight: 60
url: /pt/java/add-ellipse/
description: Aprenda como desenhar, preencher e rotular formas de elipse em arquivos PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhar formas de elipse em arquivos PDF usando Java
Abstract: Este artigo mostra como adicionar formas de elipse a documentos PDF usando Aspose.PDF for Java. Ele cobre elipses contornadas, elipses preenchidas e a inserção de fragmentos de texto dentro de formas de elipse.
---
## Adicionar contornos de elipse

1. Crie um novo documento PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner e adicione-o à página.
1. Crie o [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) forma e configure sua geometria.
1. Adicione o [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) para o [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner.
1. Defina as propriedades da forma exigidas pelo exemplo, incluindo [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) e [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Salve o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Ellipse"));
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

O exemplo completo adiciona duas elipses de contorno diferentes ao mesmo gráfico.

## Adicionar elipses preenchidas

`createEllipseFilled` preenche duas reticências com `Color.getGreenYellow()` e `Color.getDarkRed()`.

## Adicionar texto dentro das elipses

1. Crie um novo documento PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) e defina as opções de formatação de texto necessárias.
1. Crie um [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner e adicione-o à página.
1. Crie o [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) forma e configure sua geometria.
1. Adicione o [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) para o [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner.
1. Salve o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addTextInsideEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
