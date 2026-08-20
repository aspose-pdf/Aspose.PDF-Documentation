---
title: Formatear texto PDF en Java
linktitle: Formato de texto dentro de PDF
type: docs
weight: 70
url: /java/text-formatting-inside-pdf/
description: Aprenda a formatear texto dentro de documentos PDF en Java usando espacios, notas, listas, diseño de varias columnas y opciones de estilo.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Formatee y aplique estilo al texto dentro de archivos PDF con Java
Abstract: Este artículo explica cómo formatear texto en documentos PDF usando Aspose.PDF para Java. Cubre interlineado, espaciado entre caracteres, listas numeradas y con viñetas, notas al pie y notas al final, contenido de párrafos en línea, diseño de varias columnas, saltos de página forzados y tabulaciones personalizadas.
---
Aspose.PDF para Java ofrece controles de formato de texto para espaciado, listas, notas, diseño en línea y composición de varias columnas.


## 
Establecer interlineado simple



Utilice este ejemplo cuando el texto del párrafo deba utilizar un valor de interlineado fijo.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Cargue o prepare el texto fuente y cree un `TextFragment`.
1. Establezca el interlineado, agregue el fragmento a la página y guarde el documento.


```java
public static void specifyLineSpacingSimpleCase(Path outputFile) throws Exception {
        try (Document document = new Document()) {
            Page page = document.getPages().add();

            Path loremPath = dataDir.resolve("lorem.txt");
            String text = Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum text not found.";

            TextFragment textFragment = new TextFragment(text);
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setLineSpacing(16);
            page.getParagraphs().add(textFragment);

            document.save(outputFile.toString());
        }
    }
```

## 
Comparar modos de interlineado con una fuente personalizada



Utilice este ejemplo cuando deba probar el interlineado con diferentes modos de formato para la misma fuente.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Cargue la fuente personalizada y prepare dos fragmentos con diferentes modos de interlineado.
1. Agregue ambos fragmentos a la página y guarde el PDF.


```java
public static void specifyLineSpacingSpecificCase(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Path fontFile = dataDir.resolve("HPSimplified.ttf");
        Path loremPath = dataDir.resolve("lorem.txt");
        String text = Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum text not found.";

        try (InputStream fontStream = Files.newInputStream(fontFile)) {
            Font font = FontRepository.openFont(fontStream, FontTypes.TTF);

            TextFragment fragment1 = new TextFragment(text);
            fragment1.getTextState().setFont(font);
            fragment1.getTextState().setFormattingOptions(new TextFormattingOptions());
            fragment1.getTextState().getFormattingOptions().setLineSpacing(TextFormattingOptions.LineSpacingMode.FontSize);
            page.getParagraphs().add(fragment1);

            TextFragment fragment2 = new TextFragment(text);
            fragment2.getTextState().setFont(font);
            fragment2.getTextState().setFormattingOptions(new TextFormattingOptions());
            fragment2.getTextState().getFormattingOptions().setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);
            page.getParagraphs().add(fragment2);
        }

        document.save(outputFile.toString());
    }
}
```

## 
Establecer espacio entre caracteres con fragmentos de texto



Utilice este ejemplo cuando el mismo texto deba mostrarse con diferentes valores de espaciado entre caracteres.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Cree fragmentos de texto con el método auxiliar para varios valores de espaciado.
1. Agregue los fragmentos a la página y guarde el documento.


```java
public static void characterSpacingUsingTextFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.getParagraphs().add(makeCharacterSpacingFragment(2.0f));
        page.getParagraphs().add(makeCharacterSpacingFragment(1.0f));
        page.getParagraphs().add(makeCharacterSpacingFragment(0.75f));

        document.save(outputFile.toString());
    }
}

private static TextFragment makeCharacterSpacingFragment(float spacing) {
    TextFragment fragment = new TextFragment("Sample Text with character spacing");
    fragment.getTextState().setFont(FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize(14);
    fragment.getTextState().setCharacterSpacing(spacing);
    return fragment;
}
```

## 
Establecer el espacio entre caracteres dentro de un párrafo de texto



Utilice este ejemplo cuando se deba aplicar el espaciado entre caracteres dentro de un párrafo de texto delimitado.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Cree un `TextParagraph` con un rectángulo de destino y opciones de ajuste.
1. Agregue el fragmento de texto con estilo y guarde el PDF.


```java
public static void characterSpacingUsingTextParagraph(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(100, 700, 500, 750, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        TextFragment fragment = new TextFragment("Sample Text with character spacing");
        fragment.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment.getTextState().setFontSize(14);
        fragment.getTextState().setCharacterSpacing(2.0f);

        paragraph.appendLine(fragment);
        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## 
Crear una lista de viñetas con HTML



Utilice este ejemplo cuando se deba generar un formato de lista desordenado a partir del marcado HTML.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Construya la cadena de lista HTML.
1. Agréguelo como `HtmlFragment` y guarde el documento.


```java
public static void createBulletListHtmlVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlList = "<ul><li>First item in the list</li>"
                + "<li>Second item with more text to demonstrate wrapping behavior.</li>"
                + "<li>Third item</li><li>Fourth item</li></ul>";
        page.getParagraphs().add(new HtmlFragment(htmlList));
        document.save(outputFile.toString());
    }
}
```

## 
Crea una lista numerada con HTML



Utilice este ejemplo cuando el formato de lista ordenada deba generarse a partir del marcado HTML.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Cree la cadena de lista HTML ordenada.
1. Agréguelo como `HtmlFragment` y guarde el documento.


```java
public static void createNumberedListHtmlVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlList = "<ol><li>First item in the list</li>"
                + "<li>Second item with more text to demonstrate wrapping behavior.</li>"
                + "<li>Third item</li><li>Fourth item</li></ol>";
        page.getParagraphs().add(new HtmlFragment(htmlList));
        document.save(outputFile.toString());
    }
}
```

## 
Crea una lista de viñetas con LaTeX



Utilice este ejemplo cuando el formato de lista desordenada deba representarse a partir del marcado TeX.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Prepare la cadena de la lista TeX con el entorno `itemize`.
1. Agréguelo como `TeXFragment` y guarde el PDF.


```java
public static void createBulletListLatexVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String texList = "Lists are easy to create: \\begin{itemize}"
                + "\\item First item"
                + "\\item Second item with more text to demonstrate wrapping behavior."
                + "\\item Third item"
                + "\\item Fourth item"
                + "\\end{itemize}";
        page.getParagraphs().add(new TeXFragment(texList));
        document.save(outputFile.toString());
    }
}
```

## 
Crea una lista numerada con LaTeX



Utilice este ejemplo cuando el formato de lista ordenada deba representarse a partir del marcado TeX.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Prepare la cadena de la lista TeX con el entorno `enumerate`.
1. Agréguelo como `TeXFragment` y guarde el PDF.


```java
public static void createNumberedListLatexVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String texList = "Lists are easy to create: \\begin{enumerate}"
                + "\\item First item"
                + "\\item Second item with more text to demonstrate wrapping behavior."
                + "\\item Third item"
                + "\\item Fourth item"
                + "\\end{enumerate}";
        page.getParagraphs().add(new TeXFragment(texList));
        document.save(outputFile.toString());
    }
}
```

## 
Crea una lista de viñetas con párrafos de texto



Utilice este ejemplo cuando deba crear una lista de viñetas manual a partir de fragmentos de texto sin formato.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Cree un `TextParagraph` y agregue fragmentos con prefijo de viñetas.
1. Agregue el párrafo a la página y guarde el documento.


```java
public static void createBulletList(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String[] items = {
                "First item in the list",
                "Second item with more text to demonstrate wrapping behavior.",
                "Third item",
                "Fourth item"
        };

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(80, 200, 400, 800, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        for (String item : items) {
            TextFragment fragment = new TextFragment("- " + item);
            fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
            fragment.getTextState().setFontSize(12);
            paragraph.appendLine(fragment);
        }

        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## 
Crea una lista numerada con párrafos de texto.



Utilice este ejemplo cuando deba crear una lista numerada manualmente a partir de fragmentos de texto sin formato.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Cree un `TextParagraph` y agregue fragmentos numerados.
1. Agregue el párrafo a la página y guarde el documento.


```java
public static void createNumberedList(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String[] items = {
                "First item in the list",
                "Second item with more text to demonstrate wrapping behavior.",
                "Third item",
                "Fourth item"
        };

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(80, 200, 400, 800, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        for (int i = 0; i < items.length; i++) {
            TextFragment fragment = new TextFragment((i + 1) + ". " + items[i]);
            fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
            fragment.getTextState().setFontSize(12);
            paragraph.appendLine(fragment);
        }

        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## 
Agregar una nota al pie básica



Utilice este ejemplo cuando un fragmento de texto deba hacer referencia a una simple nota al pie.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Cree el fragmento de texto principal y asigne un `Note` como nota al pie.
1. Agregue cualquier texto de continuación en línea y guarde el documento.


```java
public static void addFootnote(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setFootNote(new Note("This is the footnote content."));
        page.getParagraphs().add(textFragment);

        TextFragment inlineText = new TextFragment(" This is another text after footnote in the same paragraph.");
        inlineText.setInLineParagraph(true);
        inlineText.getTextState().setFont(FontRepository.findFont("Arial"));
        inlineText.getTextState().setFontSize(14);
        page.getParagraphs().add(inlineText);

        document.save(outputFile.toString());
    }
}
```

## 
Agregar una nota al pie con estilo de texto personalizado



Utilice este ejemplo cuando el contenido de las notas al pie deba utilizar su propia configuración de fuente, tamaño y color.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Cree el fragmento de texto principal y configure una nota al pie con estilo.
1. Adjunte la nota y guarde el PDF.


```java
public static void addFootnoteCustomTextStyle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);

        Note note = new Note("This is the footnote content with custom text style.");
        TextState noteTextState = new TextState();
        noteTextState.setFont(FontRepository.findFont("Times New Roman"));
        noteTextState.setFontSize(10);
        noteTextState.setForegroundColor(Color.getRed());
        noteTextState.setFontStyle(FontStyles.Italic);
        note.setTextState(noteTextState);
        textFragment.setFootNote(note);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
Agregar una nota al pie con texto de marcador personalizado



Utilice este ejemplo cuando el marcador de nota al pie visible deba reemplazarse con texto personalizado.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Asigne la nota al pie al fragmento de texto principal y anule su texto marcador.
1. Agregue el contenido restante y guarde el documento.


```java
public static void addFootnoteCustomText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setFootNote(new Note("This is the footnote content."));
        textFragment.getFootNote().setText("***");
        page.getParagraphs().add(textFragment);

        TextFragment anotherText = new TextFragment(" This is another text without footnote.");
        anotherText.getTextState().setFont(FontRepository.findFont("Arial"));
        anotherText.getTextState().setFontSize(14);
        page.getParagraphs().add(anotherText);

        document.save(outputFile.toString());
    }
}
```

## 
Personaliza la línea separadora de notas al pie



Utilice este ejemplo cuando la línea que separa las notas al pie del contenido de la página deba tener un estilo explícito.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Configure el estilo de línea de nota de la página a través de `GraphInfo`.
1. Agregue fragmentos de texto con notas a pie de página y guarde el documento.


```java
public static void addFootnoteWithCustomLineStyle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        GraphInfo graphInfo = new GraphInfo();
        graphInfo.setLineWidth(2);
        graphInfo.setColor(Color.getRed());
        graphInfo.setDashArray(new int[] {3});
        graphInfo.setDashPhase(1);
        page.setNoteLineStyle(graphInfo);

        TextFragment text1 = new TextFragment("This is a sample text with a footnote.");
        text1.setFootNote(new Note("foot note for text 1"));
        page.getParagraphs().add(text1);

        TextFragment text2 = new TextFragment("This is yet another sample text with a footnote.");
        text2.setFootNote(new Note("foot note for text 2"));
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```

## 
Agregue una nota al pie con imagen y contenido de la tabla.



Utilice este ejemplo cuando la nota al pie en sí deba contener contenido enriquecido, como imágenes, texto y tablas.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Cree un objeto `Note` con una imagen, texto en línea y una tabla.
1. Adjúntelo al fragmento de texto principal y guarde el documento.


```java
public static void addFootnoteWithImageAndTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment text = new TextFragment("This is a sample text with a footnote.");
        page.getParagraphs().add(text);

        Note note = new Note();

        Image imageNote = new Image();
        imageNote.setFile(dataDir.resolve("logo.jpg").toString());
        imageNote.setFixHeight(20);
        imageNote.setFixWidth(20);
        note.getParagraphs().add(imageNote);

        TextFragment textNote = new TextFragment("This is the footnote content.");
        textNote.getTextState().setFontSize(20);
        textNote.setInLineParagraph(true);
        note.getParagraphs().add(textNote);

        Table table = new Table();
        table.getRows().add().getCells().add("Cell 1,1");
        table.getRows().add().getCells().add("Cell 1,2");
        note.getParagraphs().add(table);

        text.setFootNote(note);
        document.save(outputFile.toString());
    }
}
```

## 
Agregar una nota al final



Utilice este ejemplo cuando un fragmento de texto deba hacer referencia al contenido de la nota final en lugar de a una nota al pie de página.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Asigne una nota final al fragmento de texto principal y agregue texto de cuerpo de apoyo.
1. Guarde el documento con el contenido de la nota final generada.


```java
public static void addEndnote(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with an endnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setEndNote(new Note("This is the EndNote content."));
        page.getParagraphs().add(textFragment);

        String textContent = loremText();
        for (int i = 0; i < 5; i++) {
            TextFragment text = new TextFragment(textContent);
            text.getTextState().setFont(FontRepository.findFont("Arial"));
            text.getTextState().setFontSize(14);
            page.getParagraphs().add(text);
        }

        document.save(outputFile.toString());
    }
}

private static String loremText() throws Exception {
    Path loremPath = dataDir.resolve("lorem.txt");
    return Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum sample text not found.";
}
```

## 
Agregar una nota al final con texto de marcador personalizado



Utilice este ejemplo cuando el marcador de nota final deba utilizar una etiqueta visible personalizada.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Asigne una nota final al fragmento de texto principal y anule su texto marcador.
1. Agregue el texto restante del documento y guarde el PDF.


```java
public static void addEndnoteCustomText(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with an endnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setEndNote(new Note("This is the EndNote content."));
        textFragment.getEndNote().setText("***");
        page.getParagraphs().add(textFragment);

        String textContent = loremText();
        for (int i = 0; i < 5; i++) {
            TextFragment text = new TextFragment(textContent);
            text.getTextState().setFont(FontRepository.findFont("Arial"));
            text.getTextState().setFontSize(14);
            page.getParagraphs().add(text);
        }

        document.save(outputFile.toString());
    }
}
```

## 
Forzar el contenido de la tabla en una nueva página



Utilice este ejemplo cuando el contenido formateado deba comenzar explícitamente en una página nueva.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Construya una tabla y complete sus filas.
1. Configure la tabla para que comience en una nueva página y guarde el documento.


```java
public static void forceNewPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Table table = new Table();
        table.setColumnWidths("150 150 150");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All));

        for (int i = 0; i < 5; i++) {
            Row row = table.getRows().add();
            row.getCells().add("Row " + (i + 1) + " - Col 1");
            row.getCells().add("Row " + (i + 1) + " - Col 2");
            row.getCells().add("Row " + (i + 1) + " - Col 3");
        }

        table.setInNewPage(true);
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 
Mezcle contenido en línea dentro del flujo de un párrafo



Utilice este ejemplo cuando el texto y las imágenes deban continuar dentro del mismo flujo de párrafo.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Agregue el primer fragmento de texto, luego una imagen en línea y luego otro fragmento de texto en línea.
1. Agregue cualquier párrafo independiente siguiente y guarde el documento.


```java
public static void usingInlineParagraphProperty(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment1 = new TextFragment("This is the first part of the paragraph. ");
        fragment1.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment1.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment1);

        Image image = new Image();
        image.setInLineParagraph(true);
        image.setFile(dataDir.resolve("logo.jpg").toString());
        image.setFixHeight(30);
        image.setFixWidth(30);
        page.getParagraphs().add(image);

        TextFragment fragment2 = new TextFragment("This is the second part of the same paragraph.");
        fragment2.setInLineParagraph(true);
        fragment2.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment2.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment2);

        TextFragment fragment3 = new TextFragment("This is a new paragraph.");
        fragment3.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment3.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment3);

        document.save(outputFile.toString());
    }
}
```

## 
Crear un diseño de texto de varias columnas



Utilice este ejemplo cuando el texto con estilo de artículo deba fluir a través de varias columnas.


1. 
Cree un nuevo documento PDF y configure los márgenes de la página.

1. 
Agregue el contenido del encabezado y cree un `FloatingBox` de varias columnas.
1. Rellénelo con texto y guarde el PDF final.


```java
public static void createMultiColumnPdf(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        document.getPageInfo().getMargin().setLeft(40);
        document.getPageInfo().getMargin().setRight(40);
        Page page = document.getPages().add();

        com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500.0, 2.0);
        page.getParagraphs().add(graph1);
        graph1.getShapes().addItem(new com.aspose.pdf.drawing.Line(new float[] {1.0f, 2.0f, 500.0f, 2.0f}));

        String html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>";
        page.getParagraphs().add(new HtmlFragment(html));

        FloatingBox box = new FloatingBox();
        box.getColumnInfo().setColumnCount(2);
        box.getColumnInfo().setColumnSpacing("5");
        box.getColumnInfo().setColumnWidths("105 105");

        TextFragment text1 = new TextFragment("By A Googler (The Official Google Blog)");
        text1.getTextState().setFontSize(8);
        text1.getTextState().setLineSpacing(2);
        box.getParagraphs().add(text1);

        text1.getTextState().setFontSize(10);
        text1.getTextState().setFontStyle(FontStyles.Italic);

        com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50.0, 10.0);
        graph2.getShapes().addItem(new com.aspose.pdf.drawing.Line(new float[] {1.0f, 10.0f, 100.0f, 10.0f}));
        box.getParagraphs().add(graph2);

        String loremText = loremText();
        box.getParagraphs().add(new TextFragment(loremText.repeat(5)));
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```

## 
Cree texto alineado con tabulaciones personalizadas



Utilice este ejemplo cuando el texto deba alinearse como una tabla simple utilizando posiciones de tabulación.


1. 
Cree un nuevo documento PDF y agregue una página.

1. 
Configure las tabulaciones con ajustes de alineación y guía.
1. Cree los fragmentos de texto que utilizan esas tabulaciones y guarde el documento.

```java
public static void customTabStops(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TabStops tabStops = new TabStops();
        TabStop tabStop1 = tabStops.add(100);
        tabStop1.setAlignmentType(TabAlignmentType.Right);
        tabStop1.setLeaderType(TabLeaderType.Solid);

        TabStop tabStop2 = tabStops.add(200);
        tabStop2.setAlignmentType(TabAlignmentType.Center);
        tabStop2.setLeaderType(TabLeaderType.Dash);

        TabStop tabStop3 = tabStops.add(300);
        tabStop3.setAlignmentType(TabAlignmentType.Left);
        tabStop3.setLeaderType(TabLeaderType.Dot);

        TextFragment header = new TextFragment("This is an example of forming table with TAB stops", tabStops);
        TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tabStops);
        TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tabStops);

        TextFragment text2 = new TextFragment("#$TABdata21 ", tabStops);
        text2.getSegments().add(new TextSegment("#$TAB"));
        text2.getSegments().add(new TextSegment("data22 "));
        text2.getSegments().add(new TextSegment("#$TAB"));
        text2.getSegments().add(new TextSegment("data23"));

        page.getParagraphs().add(header);
        page.getParagraphs().add(text0);
        page.getParagraphs().add(text1);
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```
