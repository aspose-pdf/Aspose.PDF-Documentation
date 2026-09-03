---
title: Ejemplo de Hello World usando Java
linktitle: Ejemplo de Hello World
type: docs
weight: 20
url: /es/java/hello-world-example/
description: Esta muestra demuestra cómo crear un documento PDF sencillo con texto Hello World con estilo usando Aspose.PDF for Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ejemplo Hello World mediante Java
Abstract: Este artículo proporciona un ejemplo Hello World para Aspose.PDF for Java. El ejemplo crea un nuevo documento PDF, agrega una página, crea un TextFragment con posición personalizada, fuente y colores, agrega el texto a la página con TextBuilder y guarda el resultado como un archivo PDF.
---
Un ejemplo \"Hello World\" es la forma más corta de comprender el flujo de trabajo básico de creación de PDF. En este artículo, el ejemplo crea un nuevo PDF, coloca un fragmento de texto con estilo en la página y guarda el archivo de salida.

El ejemplo de Java sigue estos pasos:

1. Crear un [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objeto.
1. Agregar un [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Crear un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) con el texto `Hello, world!`.
1. Establecer el [Position](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/), fuente, tamaño de fuente, color de fondo y color de primer plano a través del fragmento [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Crear un [TextBuilder](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) para la página.
1. Agregar el [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) al [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Guardar el PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
