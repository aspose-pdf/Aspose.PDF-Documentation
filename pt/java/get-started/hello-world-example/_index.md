---
title: Exemplo de Hello World usando Java
linktitle: Exemplo Hello World
type: docs
weight: 20
url: /pt/java/hello-world-example/
description: Esta amostra demonstra como criar um documento PDF simples com texto Hello World estilizado usando Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exemplo Hello World via Java
Abstract: Este artigo fornece um exemplo Hello World para Aspose.PDF for Java. O exemplo cria um novo documento PDF, adiciona uma página, cria um TextFragment com posição personalizada, fonte e cores, adiciona o texto à página com TextBuilder e salva o resultado como um arquivo PDF.
---
Um exemplo "Hello World" é o caminho mais curto para entender o fluxo de trabalho básico de criação de PDF. Neste artigo, o exemplo cria um novo PDF, coloca um fragmento de texto estilizado na página e salva o arquivo de saída.

O exemplo em Java segue estes passos:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) para o documento.
1. Crie um [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) com o texto `Hello, world!`.
1. Defina o [Position](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/), fonte, tamanho da fonte, cor de fundo e cor de primeiro plano através do fragmento [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Crie um [TextBuilder](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) para a página.
1. Anexe o [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) para o [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Salve o PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
