---
title: Use FloatingBox para layout de PDF em Java
linktitle: Usando FloatingBox
type: docs
weight: 30
url: /java/floating-box/
description: Aprenda como usar FloatingBox para layout de texto, conteúdo de várias colunas e posicionamento preciso em documentos PDF com Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Crie e posicione contêineres FloatingBox estilizados em PDF com Java
Abstract: Este artigo explica como usar FloatingBox em Aspose.PDF para Java. Abrange a colocação de texto em contêineres flutuantes com bordas, a criação de layouts repetidos de várias colunas, o uso de cores de fundo, deslocamentos absolutos e opções de alinhamento horizontal ou vertical.
---
Aspose.PDF para Java usa `FloatingBox` para construir contêineres de texto reutilizáveis ​​e layouts baseados em colunas.

## Crie e adicione uma caixa flutuante

Use este exemplo quando o texto precisar ser colocado dentro de um contêiner flutuante com borda.

1. Crie um novo documento PDF e adicione uma página.
1. Crie um `FloatingBox`, defina seu tamanho e borda e adicione conteúdo de texto.
1. Adicione a caixa à página e salve o documento.

```java
public static void createAndAddFloatingBox(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           FloatingBox box = new FloatingBox(400, 30);
           box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
           box.setNeedRepeating(false);
           String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
           box.getParagraphs().add(new TextFragment(phrase));

           page.getParagraphs().add(box);
           document.save(outputFile.toString());
       }
   }
```

## Crie um layout repetido de várias colunas

Use este exemplo quando o texto longo deve fluir por várias colunas dentro de uma caixa flutuante.

1. Crie uma página e configure as margens.
1. Calcule as larguras das colunas e defina as configurações da coluna `FloatingBox`.
1. Adicione fragmentos de texto repetidos à caixa e salve o documento.

```java
public static void multiColumnLayout(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            box.getParagraphs().add(new TextFragment(phrase));
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Comece cada fragmento como o primeiro item de uma coluna

Use este exemplo quando cada fragmento inserido iniciar um novo segmento de fluxo de coluna.

1. Crie uma página e configure a multicoluna `FloatingBox`.
1. Crie fragmentos de texto e marque-os com `setFirstParagraphInColumn(true)`.
1. Adicione a caixa à página e salve o PDF.

```java
public static void multiColumnLayout2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            TextFragment text = new TextFragment(phrase);
            text.setFirstParagraphInColumn(true);
            box.getParagraphs().add(text);
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Adicione uma caixa flutuante com cor de fundo

Use este exemplo quando o contêiner flutuante tiver um preenchimento de fundo visível.

1. Crie um novo documento PDF e adicione uma página.
1. Crie um `FloatingBox`, defina sua cor de fundo e adicione texto.
1. Coloque a caixa na página e salve o documento.

```java
public static void backgroundSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setBackgroundColor(Color.getLightGreen());
        box.setNeedRepeating(false);
        box.getParagraphs().add(new TextFragment("text example"));

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Posicione uma caixa flutuante com deslocamentos absolutos

Use este exemplo quando a caixa flutuante precisar aparecer em um deslocamento exato na página.

1. Crie uma página e prepare o conteúdo do texto ao redor.
1. Crie um `FloatingBox`, defina o posicionamento absoluto e atribua deslocamentos superior e esquerdo.
1. Adicione o conteúdo à página e salve o documento.

```java
public static void offsetSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setTop(45);
        box.setLeft(15);
        box.setPositioningMode(ParagraphPositioningMode.Absolute);
        box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
        box.getParagraphs().add(new TextFragment("text example 1"));

        page.getParagraphs().add(new TextFragment("text example 2"));
        page.getParagraphs().add(box);
        page.getParagraphs().add(new TextFragment("text example 3"));

        document.save(outputFile.toString());
    }
}
```

## Alinhe o texto dentro das caixas flutuantes

Use este exemplo quando caixas flutuantes demonstrarem diferentes alinhamentos verticais com o mesmo alinhamento horizontal.

1. Crie um novo documento PDF e adicione uma página.
1. Crie vários objetos `FloatingBox` com diferentes configurações de alinhamento.
1. Adicione-os à página e salve o resultado.

```java
public static void alignTextToFloat(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox floatBox = new FloatingBox(100, 100);
        floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
        floatBox.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
        floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox);

        FloatingBox floatBox2 = new FloatingBox(100, 100);
        floatBox2.setVerticalAlignment(VerticalAlignment.Center);
        floatBox2.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox2.getParagraphs().add(new TextFragment("FloatingBox_center"));
        floatBox2.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox2);

        FloatingBox floatBox3 = new FloatingBox(100, 100);
        floatBox3.setVerticalAlignment(VerticalAlignment.Top);
        floatBox3.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox3.getParagraphs().add(new TextFragment("FloatingBox_top"));
        floatBox3.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox3);

        document.save(outputFile.toString());
    }
}
```
