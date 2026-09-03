---
title: Agregar texto a PDF en Java
linktitle: Agregar texto a PDF
type: docs
weight: 10
url: /java/add-text-to-pdf-file/
description: Aprenda a agregar texto, fragmentos HTML, listas, enlaces y fuentes personalizadas a documentos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue texto, enlaces, HTML y fuentes a archivos PDF con Java
Abstract: Este artículo explica cómo agregar y aplicar estilo a texto en documentos PDF usando Aspose.PDF para Java. Cubre inserción de texto simple, diseño de párrafo, hipervínculos, texto de derecha a izquierda, estilo de fuente, transparencia, bordes, fragmentos HTML y LaTeX, texto degradado y fuentes personalizadas cargadas desde archivos o secuencias.
---
Aspose.PDF para Java admite la inserción de texto sin formato, diseño avanzado, estilo, degradados, HTML, LaTeX y fuentes personalizadas.


## 
Agregar un fragmento de texto simple



Utilice este ejemplo cuando una cadena de texto corta deba colocarse en coordenadas de página fijas.


1. Cree un nuevo documento PDF y agregue una página.

1. Cree un `TextFragment` y establezca su posición.
1. Agréguelo a la página y guarde el documento.


```java
public static void addTextSimpleCase(Path outputFile) {
      try (Document document = new Document()) {
          Page page = document.getPages().add();

          TextFragment textFragment = new TextFragment("Hello, Aspose!");
          textFragment.setPosition(new Position(100, 600));

          page.getParagraphs().add(textFragment);
          document.save(outputFile.toString());
      }
  }
```

## 
Agregar un párrafo dentro de un rectángulo



Utilice este ejemplo cuando un bloque de texto más grande deba fluir dentro de un área delimitada.


1. Cree un nuevo documento PDF y agregue una página.

1. Cargue el texto fuente y configure un rectángulo `TextParagraph` y un modo de ajuste.
1. Adjunte el fragmento a través de `TextBuilder` y guarde el PDF.


```java
public static void addParagraph(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String text = Files.exists(loremPath)
                ? Files.readString(loremPath)
                : "Lorem ipsum sample text not found.";

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setFirstLineIndent(20);
        paragraph.setRectangle(new Rectangle(80, 800, 400, 200, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.DiscretionaryHyphenation);

        TextFragment fragment = new TextFragment(text);
        fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        fragment.getTextState().setFontSize(12);

        paragraph.appendLine(fragment);
        builder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## 
Agregar párrafos con diferentes configuraciones de sangría



Utilice este ejemplo cuando la primera línea y las siguientes deban utilizar reglas de sangría diferentes.


1. Cree un nuevo documento PDF y agregue una página.

1. Prepare el fragmento de texto compartido y cree múltiples objetos `TextParagraph`.
1. Configure la sangría para cada párrafo, añádalos y guarde el documento.


```java
public static void addParagraphsIndents(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String text = Files.exists(loremPath)
                ? Files.readString(loremPath)
                : "Lorem ipsum sample text not found.";

        TextFragment fragment = new TextFragment(text);
        fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        fragment.getTextState().setFontSize(12);

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph1 = new TextParagraph();
        paragraph1.setFirstLineIndent(20);
        paragraph1.setRectangle(new Rectangle(80, 800, 300, 50, true));
        paragraph1.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
        paragraph1.appendLine(fragment);
        builder.appendParagraph(paragraph1);

        TextParagraph paragraph2 = new TextParagraph();
        paragraph2.setSubsequentLinesIndent(20);
        paragraph2.setRectangle(new Rectangle(320, 800, 500, 50, true));
        paragraph2.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
        paragraph2.appendLine(fragment);
        builder.appendParagraph(paragraph2);

        document.save(outputFile.toString());
    }
}
```

## 
Insertar texto con un salto de línea manual



Utilice este ejemplo cuando un fragmento de texto deba contener una nueva línea explícita.


1. Cree un nuevo documento PDF y agregue una página.

1. Cree un `TextFragment` que contenga un salto de línea y configure su estilo.
1. Agréguelo a través de `TextParagraph` y guarde el PDF.


```java
public static void addNewLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());

        TextParagraph paragraph = new TextParagraph();
        paragraph.appendLine(textFragment);
        paragraph.setPosition(new Position(100, 600));

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## 
Inspeccionar saltos de línea detectados



Utilice este ejemplo cuando necesite revisar el resultado de la notificación relacionada con el diseño del texto y el ajuste de línea.


1. Cree un nuevo documento PDF y habilite el registro de notificaciones.

1. Agregue varios fragmentos de texto largos a la página.
1. Inspeccione las notificaciones y guarde el documento.


```java
public static void determineLineBreak(Path outputFile) {
    try (Document document = new Document()) {
        document.setEnableNotificationLogging(true);

        Page page = document.getPages().add();
        for (int i = 0; i < 4; i++) {
            TextFragment text = new TextFragment(
                    "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
                            + "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                            + "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
                            + "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
                            + "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
                            + "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
                            + "culpa qui officia deserunt mollit anim id est laborum.");
            text.getTextState().setFontSize(20);
            page.getParagraphs().add(text);
        }

        System.out.println(document.getPages().get_Item(1).getNotifications());
        document.save(outputFile.toString());
    }
}
```

## 
Medir el ancho del texto dinámicamente



Utilice este ejemplo cuando deba medir el ancho de caracteres y cadenas antes de tomar decisiones sobre el diseño.


1. Resuelva la fuente de destino y cree un `TextState`.

1. Mida caracteres y compare los resultados de las API de estado de texto y fuente.
1. Envíe cualquier discrepancia para su validación.


```java
public static void getTextWidthDynamically(Path outputFile) {
    Font font = FontRepository.findFont("Arial");
    TextState textState = new TextState();
    textState.setFont(font);
    textState.setFontSize(14);

    if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001) {
        System.out.println("Unexpected font string measure!");
    }

    if (Math.abs(textState.measureString("z") - 7.0) > 0.001) {
        System.out.println("Unexpected font string measure!");
    }

    for (char c = 'A'; c <= 'z'; c++) {
        double fontMeasure = font.measureString(String.valueOf(c), 14);
        double textStateMeasure = textState.measureString(String.valueOf(c));
        if (Math.abs(fontMeasure - textStateMeasure) > 0.001) {
            System.out.println("Font and state string measuring doesn't match!");
        }
    }
}
```

## 
Agregar texto con un segmento de hipervínculo



Utilice este ejemplo cuando una parte de un fragmento de texto deba comportarse como un enlace web.


1. Cree un nuevo documento PDF y agregue una página.

1. Construya un `TextFragment` con varios objetos `TextSegment`.
1. Asigne un hipervínculo y un estilo al segmento de destino y luego guarde el documento.


```java
public static void addTextWithHyperlink(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment = new TextFragment("Sample Text Fragment");
        fragment.getSegments().add(new TextSegment(" ... Text Segment 1..."));

        TextSegment segment = new TextSegment("Link to Aspose");
        fragment.getSegments().add(segment);
        segment.setHyperlink(new WebHyperlink("https://products.aspose.com/pdf"));
        segment.getTextState().setForegroundColor(Color.getBlue());
        segment.getTextState().setFontStyle(FontStyles.Italic);

        fragment.getSegments().add(new TextSegment("TextSegment without hyperlink"));

        page.getParagraphs().add(fragment);
        document.save(outputFile.toString());
    }
}
```

## 
Agregar texto de derecha a izquierda



Utilice este ejemplo cuando el documento deba mostrar contenido de secuencia de comandos de derecha a izquierda con la alineación adecuada.


1. Cree un nuevo documento PDF y agregue una página.

1. Cree un `TextFragment` con el texto RTL de destino y configure su fuente y alineación.
1. Agréguelo a la página y guarde el PDF.


```java
public static void addTextWithRtlText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment(
                "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية.");
        textFragment.getTextState().setFont(FontRepository.findFont("Tahoma"));
        textFragment.getTextState().setFontSize(14);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.setHorizontalAlignment(HorizontalAlignment.Right);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Agregue texto con estilo y segmentos tipo fórmula



Utilice este ejemplo cuando el texto normal y los segmentos tipo subíndice deban utilizar diferentes estados de texto en una salida.


1. Cree un nuevo documento PDF y agregue una página.

1. Construya el fragmento de estilo principal y componga la fórmula con segmentos auxiliares.
1. Agregue ambos fragmentos a la página y guarde el documento.


```java
public static void addTextWithFontStyling(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment formula = new TextFragment();
        TextFragment textFragment = new TextFragment("Hello, Aspose!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textFragment.getTextState().setUnderline(true);
        textFragment.setHorizontalAlignment(HorizontalAlignment.Left);

        TextState textStateLetters = new TextState();
        textStateLetters.setFont(FontRepository.findFont("Arial"));
        textStateLetters.setFontSize(14);
        textStateLetters.setForegroundColor(Color.getBlue());
        textStateLetters.setFontStyle(FontStyles.Bold);

        TextState textStateIndex = new TextState();
        textStateIndex.setFont(FontRepository.findFont("Arial"));
        textStateIndex.setFontSize(14);
        textStateIndex.setForegroundColor(Color.getDarkRed());
        textStateIndex.setSubscript(true);

        Position position = new Position(100, 500);
        addSegment(formula, "S = a", textStateLetters, position);
        addSegment(formula, "2n", textStateIndex, position);
        addSegment(formula, " + a", textStateLetters, position);
        addSegment(formula, "2n+1", textStateIndex, position);
        addSegment(formula, " + a", textStateLetters, position);
        addSegment(formula, "2n+2", textStateIndex, position);
        formula.setHorizontalAlignment(HorizontalAlignment.Left);

        page.getParagraphs().add(textFragment);
        page.getParagraphs().add(formula);
        document.save(outputFile.toString());
    }
}

private static void addSegment(TextFragment formula, String text, TextState state, Position position) {
    TextSegment segment = new TextSegment(text);
    segment.setTextState(state);
    segment.setPosition(position);
    formula.getSegments().add(segment);
}
```

## 
Añadir texto subrayado



Utilice este ejemplo cuando un fragmento de texto deba usar visiblemente un estilo de subrayado.


1. Cree un nuevo documento PDF y agregue una página.

1. Cree el fragmento de texto, configure su fuente y estado de subrayado, y establezca su posición.
1. Agréguelo con `TextBuilder` y guarde el resultado.


```java
public static void addUnderlineText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        TextBuilder textBuilder = new TextBuilder(page);

        TextFragment fragment = new TextFragment("Hello, ASPOSE.PDF!");
        fragment.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment.getTextState().setFontSize(10);
        fragment.getTextState().setUnderline(true);
        fragment.setPosition(new Position(10, 800));
        textBuilder.appendText(fragment);

        document.save(outputFile.toString());
    }
}
```

## 
Agrega texto transparente sobre una forma coloreada



Utilice este ejemplo cuando el texto deba aparecer con transparencia encima de un gráfico de fondo.


1. Cree un nuevo documento PDF y agregue una página.

1. Dibuja la forma del fondo y crea un fragmento de texto semitransparente.
1. Agregue ambos elementos a la página y guarde el documento.


```java
public static void addTextTransparent(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        com.aspose.pdf.drawing.Graph canvas = new com.aspose.pdf.drawing.Graph(100.0, 400.0);
        com.aspose.pdf.drawing.Rectangle rectangle = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
        rectangle.getGraphInfo().setFillColor(Color.fromArgb(128, 0xC5, 0xB5, 0xFF));
        canvas.getShapes().addItem(rectangle);
        canvas.setChangePosition(false);
        page.getParagraphs().add(canvas);

        TextFragment text = new TextFragment(
                "This is the transparent text. This is the transparent text. This is the transparent text.");
        text.getTextState().setForegroundColor(Color.fromArgb(30, 0, 255, 0));
        page.getParagraphs().add(text);

        document.save(outputFile.toString());
    }
}
```

## 
Agregar texto invisible



Utilice este ejemplo cuando deba estar presente texto con capacidad de búsqueda u oculto sin representación visible.


1. Cree un nuevo documento PDF y agregue una página.

1. Agregue un fragmento de texto visible y un segundo fragmento con la bandera invisible habilitada.
1. Guarde el documento.


```java
public static void addTextInvisible(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment text1 = new TextFragment(
            "This is the visible text. This is the visible text. This is the visible text.");
        page.getParagraphs().add(text1);

        TextFragment text2 = new TextFragment(
            "This is the invisible text. This is the invisible text. This is the invisible text.");
        text2.getTextState().setInvisible(true);
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```

## 
Agregar texto con un borde rectangular



Utilice este ejemplo cuando el texto deba dibujarse junto con su rectángulo delimitador.


1. Cree un nuevo documento PDF y agregue una página.

1. Cree un `TextFragment` con estilo y habilite el dibujo del borde del rectángulo de texto.
1. Añádelo con `TextBuilder` y guarda el PDF.


```java
public static void addTextBorder(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is sample text with border.");
        textFragment.setPosition(new Position(10, 700));
        textFragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());
        textFragment.getTextState().setStrokingColor(Color.getDarkRed());
        textFragment.getTextState().setDrawTextRectangleBorder(true);

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```

## 
Agregar texto tachado



Utilice este ejemplo cuando el texto deba utilizar formato tachado.


1. Cree un nuevo documento PDF y agregue una página.

1. Cree un fragmento de texto con estilo y tachado habilitado.
1. Agréguelo a la página y guarde el documento.


```java
public static void addStrikeoutText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is sample strikeout text.");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());
        textFragment.getTextState().setStrikeOut(true);
        textFragment.getTextState().setFontStyle(FontStyles.Bold);
        textFragment.setPosition(new Position(100, 600));

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```

## 
Aplicar sombreado de degradado axial al texto



Utilice este ejemplo cuando el texto deba utilizar un relleno degradado lineal en lugar de un color sólido.


1. Cree un nuevo documento PDF y agregue una página.

1. Crea el fragmento de texto y asigna un degradado axial a su color de primer plano.
1. Agréguelo a la página y guarde el PDF.


```java
public static void applyGradientAxialShadingToText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("PDF TITLE");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(36);
        textFragment.getTextState().setFont(FontRepository.findFont("Arial Bold"));
        textFragment.getTextState().setForegroundColor(new Color());
        textFragment.getTextState().getForegroundColor()
                .setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));
        textFragment.getTextState().setUnderline(true);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Aplicar sombreado degradado radial al texto



Utilice este ejemplo cuando el texto deba utilizar un relleno degradado radial.


1. Cree un nuevo documento PDF y agregue una página.

1. Crea el fragmento de texto y asigna un degradado radial a su color de primer plano.
1. Agréguelo a la página y guarde el documento.


```java
public static void applyGradientRadialShadingToText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("PDF TITLE");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(36);
        textFragment.getTextState().setFont(FontRepository.findFont("Arial Bold"));
        textFragment.getTextState().setForegroundColor(new Color());
        textFragment.getTextState().getForegroundColor()
                .setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));
        textFragment.getTextState().setUnderline(true);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Agregar texto con formato de estilo HTML en línea



Utilice este ejemplo cuando el formato de superíndice y subíndice deba insertarse mediante marcado HTML.


1. Cree un nuevo documento PDF y agregue una página.

1. Cree un `HtmlFragment` con el marcado en línea requerido.
1. Agréguelo a la página y guarde el PDF.


```java
public static void addTextHtmlFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        HtmlFragment textFragment = new HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>");
        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Agregar un fragmento de texto LaTeX



Utilice este ejemplo cuando deba representar contenido matemático o con formato TeX dentro del PDF.


1. Cree un nuevo documento PDF y agregue una página.

1. Cree un `TeXFragment` con la expresión requerida.
1. Agréguelo a la página y guarde el documento.


```java
public static void addTextLatexFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TeXFragment textFragment = new TeXFragment(
                "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42");
        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Agregue un fragmento HTML enriquecido



Utilice este ejemplo cuando la página deba mostrar contenido HTML estructurado, como encabezados, párrafos y enlaces.


1. Cree un nuevo documento PDF y agregue una página.

1. Prepare la cadena de contenido HTML y cree un `HtmlFragment`.
1. Agréguelo a la página y guarde el PDF.


```java
public static void addHtmlFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlContent = """
                <h1 style='color:blue;'>Hello, Aspose!</h1>
                <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
                <p style='color:green;'>This paragraph is green.</p>
                <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
                """;
        HtmlFragment htmlFragment = new HtmlFragment(htmlContent);
        page.getParagraphs().add(htmlFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Agregar un fragmento HTML con estado de texto anulado



Utilice este ejemplo cuando el contenido HTML importado deba heredar una configuración de color y fuente controlada.


1. Cree un nuevo documento PDF y agregue una página.

1. Prepare el contenido HTML y cree el `HtmlFragment`.
1. Asigne un `TextState` personalizado, agregue el fragmento y guarde el documento.


```java
public static void addHtmlFragmentOverrideTextState(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlContent = """
                <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
                <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
                <p style='color:green;'>This paragraph is green.</p>
                <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
                """;
        HtmlFragment htmlFragment = new HtmlFragment(htmlContent);
        TextState textState = new TextState();
        textState.setFont(FontRepository.findFont("Arial"));
        textState.setFontSize(14);
        textState.setForegroundColor(Color.getRed());
        htmlFragment.setTextState(textState);

        page.getParagraphs().add(htmlFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Utilice una fuente personalizada cargada desde un archivo



Utilice este ejemplo cuando el texto deba utilizar una fuente cargada directamente desde una ruta de archivo de fuente.


1. Resuelva la ruta del archivo de fuente personalizada.

1. Cree un fragmento de texto y cargue la fuente a través de `FontRepository.openFont`.
1. Aplique la configuración de fuente y guarde el documento.


```java
public static void useCustomFontFromFile(Path outputFile) {
    Path fontPath = fontDir.resolve("BriosoPro Italic.otf");
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment = new TextFragment("Hello, Aspose!");
        fragment.setPosition(new Position(100, 600));
        fragment.getTextState().setFont(FontRepository.openFont(fontPath.toString()));
        fragment.getTextState().setFontSize(24);
        fragment.getTextState().setForegroundColor(Color.getBlue());
        fragment.getTextState().setFontStyle(FontStyles.Italic);

        page.getParagraphs().add(fragment);
        document.save(outputFile.toString());
    }
}
```

## 
Utilice una fuente personalizada cargada desde una secuencia



Utilice este ejemplo cuando deba abrir una fuente personalizada desde una secuencia e incrustarla en el PDF.


1. Abra el archivo de fuente como una secuencia y cárguelo con `FontRepository`.

1. Cree el fragmento de texto y asigne la fuente incrustada.
1. Agregue el fragmento a la página y guarde el documento.

```java
public static void useCustomFontFromStream(Path outputFile) throws Exception {
    Path fontPath = fontDir.resolve("BriosoPro Italic.otf");
    try (InputStream fontStream = Files.newInputStream(fontPath)) {
        Font font = FontRepository.openFont(fontStream, FontTypes.OTF);
        font.setEmbedded(true);

        try (Document document = new Document()) {
            Page page = document.getPages().add();

            TextFragment fragment = new TextFragment("Hello, Aspose!");
            fragment.setPosition(new Position(100, 600));
            fragment.getTextState().setFont(font);
            fragment.getTextState().setFontSize(14);
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setFontStyle(FontStyles.Italic);

            page.getParagraphs().add(fragment);
            document.save(outputFile.toString());
        }
    }
}
```
