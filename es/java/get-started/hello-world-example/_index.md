---
title: Ejemplo de Hola mundo usando Java
linktitle: Ejemplo de Hola mundo
type: docs
weight: 20
url: /es/java/hello-world-example/
description: Este ejemplo demuestra cómo crear un documento PDF simple con texto de Hola Mundo con estilo usando Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ejemplo de Hola Mundo vía Java
Abstract: Este artículo proporciona un ejemplo de Hola Mundo para Aspose.PDF for Java. El ejemplo crea un nuevo documento PDF, añade una página, crea un TextFragment con posición personalizada, fuente y colores, agrega el texto a la página con TextBuilder y guarda el resultado como un archivo PDF.
---
Un ejemplo de "Hello World" es la vía más corta para comprender el flujo de trabajo básico de creación de PDF. En este artículo, el ejemplo crea un nuevo PDF, coloca un fragmento de texto con estilo en la página y guarda el archivo de salida.

El ejemplo Java sigue estos pasos:

1. Cree un objeto [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Cree un [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) con el texto `Hello, world!`.
1. Establezca el [`Position`](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/), fuente, tamaño de fuente, color de fondo y color de primer plano a través de la propiedad [`TextState`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/) del fragmento.
1. Cree un [`TextBuilder`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) para la página.
1. Agregue el [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) al [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Guarde el PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

El siguiente código Java se basa en `GetStartedExamples.java`.

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
