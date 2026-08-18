---
title: Exemplo de Hello World usando Java
linktitle: Exemplo de Olá Mundo
type: docs
weight: 20
url: /java/hello-world-example/
description: Este exemplo demonstra como criar um documento PDF simples com texto estilizado Hello World usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exemplo de Olá Mundo via Java
Abstract: Este artigo fornece um exemplo de Hello World para Aspose.PDF para Java. O exemplo cria um novo documento PDF, adiciona uma página, cria um TextFragment com posição, fonte e cores personalizadas, anexa o texto à página com TextBuilder e salva o resultado como um arquivo PDF.
---
Um exemplo de “Hello World” é o caminho mais curto para entender o fluxo de trabalho básico de criação de PDF. Neste artigo, o exemplo cria um novo PDF, coloca um fragmento de texto estilizado na página e salva o arquivo de saída.

O exemplo Java segue estas etapas:

1. Crie um [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objeto.
1. Adicione um [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um [Fragmento de Texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) com o texto `Hello, world!`.
1. Defina o [Posição](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/), fonte, tamanho da fonte, cor de fundo e cor de primeiro plano no fragmento [Estado de texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Crie um [Construtor de texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) para a página.
1. Anexe o [Fragmento de Texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) para o [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Salve o PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

O seguinte código Java é baseado em `GetStartedExamples.java`.

```java
public static void simpleExample(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Hello, world!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getBlue());
        textFragment.getTextState().setForegroundColor(Color.getYellow());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```
