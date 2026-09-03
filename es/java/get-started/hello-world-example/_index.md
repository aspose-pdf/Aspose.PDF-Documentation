---
title: Ejemplo de Hola Mundo usando Java
linktitle: Hola mundo ejemplo
type: docs
weight: 20
url: /java/hello-world-example/
description: Este ejemplo demuestra cómo crear un documento PDF simple con texto estilo Hola Mundo usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ejemplo de Hola Mundo a través de Java
Abstract: Este artículo proporciona un ejemplo de Hola mundo para Aspose.PDF para Java. El ejemplo crea un nuevo documento PDF, agrega una página, crea un TextFragment con posición, fuente y colores personalizados, agrega el texto a la página con TextBuilder y guarda el resultado como un archivo PDF.
---
Un ejemplo de "Hola mundo" es el camino más corto para comprender el flujo de trabajo básico de creación de PDF. En este artículo, el ejemplo crea un nuevo PDF, coloca un fragmento de texto con estilo en la página y guarda el archivo de salida.



El ejemplo de Java sigue estos pasos:


1. Cree un objeto [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.

1. Cree un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) con el texto `Hello, world!`.
1. Establezca la [Posición](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/), la fuente, el tamaño de fuente, el color de fondo y el color de primer plano a través del fragmento [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).

1. Cree un [TextBuilder](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) para la página.

1. Agregue el [Fragmento de texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) a la [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. Guarde el [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).



El siguiente código Java está basado en `GetStartedExamples.java`.

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
