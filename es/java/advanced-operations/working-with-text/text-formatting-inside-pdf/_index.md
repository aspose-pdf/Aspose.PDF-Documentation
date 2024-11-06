---
title: Formateo de Texto dentro de PDF 
linktitle: Formateo de Texto dentro de PDF
type: docs
weight: 30
url: es/java/text-formatting-inside-pdf/
description: Esta página explica cómo formatear texto dentro de su archivo PDF. Hay agregar sangría de línea, agregar borde de texto, agregar texto subrayado, agregar un borde alrededor del texto agregado, alineación de texto para el contenido del cuadro flotante, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cómo agregar Sangría de Línea a PDF

Aspose.PDF para Java ofrece la propiedad SubsequentLinesIndent en la clase [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions). La cual se puede usar para especificar sangría de línea en escenarios de generación de PDF con TextFragment y la colección de Paragraphs.

Por favor use el siguiente fragmento de código para usar la propiedad:

```java
public static void AddLineIndentToPDF() {
        // Crear nuevo objeto de documento
        Document document = new Document();
        Page page = document.getPages().add();

        TextFragment text = new TextFragment(
                "Un rápido zorro marrón saltó sobre el perro perezoso. Un rápido zorro marrón saltó sobre el perro perezoso. Un rápido zorro marrón saltó sobre el perro perezoso. Un rápido zorro marrón saltó sobre el perro perezoso. Un rápido zorro marrón saltó sobre el perro perezoso. Un rápido zorro marrón saltó sobre el perro perezoso. Un rápido zorro marrón saltó sobre el perro perezoso. Un rápido zorro marrón saltó sobre el perro perezoso.");

        // Inicializar TextFormattingOptions para el fragmento de texto y especificar
        // el valor de SubsequentLinesIndent
        TextFormattingOptions textOptions = new TextFormattingOptions();
        textOptions.setSubsequentLinesIndent(20);
        text.getTextState().setFormattingOptions(textOptions);

        page.getParagraphs().add(text);

        text = new TextFragment("Línea2");
        page.getParagraphs().add(text);

        text = new TextFragment("Línea3");
        page.getParagraphs().add(text);

        text = new TextFragment("Línea4");
        page.getParagraphs().add(text);

        text = new TextFragment("Línea5");
        page.getParagraphs().add(text);

        document.save(_dataDir + "SubsequentIndent_out.pdf");
    }
```


## Cómo agregar un borde de texto

El siguiente fragmento de código muestra cómo agregar un borde a un texto utilizando TextBuilder y configurando el método DrawTextRectangleBorder de TextState:

```java
public static void AddTextBorder() {
    // Crear un nuevo objeto de documento
    Document pdfDocument = new Document();
    // Obtener una página en particular
    Page pdfPage = pdfDocument.getPages().add();
    // Crear fragmento de texto
    TextFragment textFragment = new TextFragment("texto principal");
    textFragment.setPosition(new Position(100, 600));
    // Establecer propiedades del texto
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());
    // Usar setStrokingColor para dibujar un borde (trazo) alrededor del rectángulo de texto
    textFragment.getTextState().setStrokingColor (Color.getDarkRed());
    // Usar el método setDrawTextRectangleBorder para establecer el valor en true
    textFragment.getTextState().setDrawTextRectangleBorder(true);
    TextBuilder tb = new TextBuilder(pdfPage);
    tb.appendText(textFragment);
    // Guardar el documento
    pdfDocument.save(_dataDir + "PDFWithTextBorder_out.pdf");
}
```


## Cómo agregar texto subrayado

El siguiente fragmento de código te muestra cómo agregar texto subrayado al crear un nuevo archivo PDF.

```java
public static void AddUnderlineText(){
    // Crear objeto de documentación
    Document pdfDocument = new Document();
    // Agregar una página al documento PDF
    Page page = pdfDocument.getPages().add();
    // Crear TextBuilder para la primera página
    TextBuilder tb = new TextBuilder(page);
    // TextFragment con texto de ejemplo
    TextFragment fragment = new TextFragment("Texto con decoración de subrayado");
    // Establecer la fuente para TextFragment
    fragment.getTextState().setFont (FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize (10);
    // Establecer el formato del texto como subrayado
    fragment.getTextState().setUnderline(true);
    // Especificar la posición donde se necesita colocar TextFragment
    fragment.setPosition (new Position(10, 800));
    // Añadir TextFragment al archivo PDF
    tb.appendText(fragment);

    // Guardar el documento PDF resultante.
    pdfDocument.save(_dataDir + "AddUnderlineText_out.pdf");
}
```


## Cómo agregar un borde alrededor del texto añadido

Tienes control sobre la apariencia del texto que agregas. El ejemplo a continuación muestra cómo agregar un borde alrededor de un fragmento de texto que has añadido dibujando un rectángulo a su alrededor. Obtén más información sobre la clase [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor).

```java
public static void AddBorderAroundAddedText() {
    PdfContentEditor editor = new PdfContentEditor();
    editor.bindPdf(_dataDir + "input.pdf");
    LineInfo lineInfo = new LineInfo();
    lineInfo.setLineWidth(2);
    lineInfo.setVerticeCoordinate (new float[] { 0, 0, 100, 100, 50, 100 });
    lineInfo.setVisibility(true);
    editor.createPolygon(lineInfo, 1, new java.awt.Rectangle(0, 0, 0, 0), "");

    // Guardar el documento PDF resultante.
    editor.save(_dataDir + "AddingBorderAroundAddedText_out.pdf");
}
```

## Cómo agregar un salto de línea

TextFragment no soporta el salto de línea dentro del texto.
 Sin embargo, para agregar texto con salto de línea, utilice TextFragment con TextParagraph:

- use "\r\n" o Environment.NewLine en TextFragment en lugar de un solo “\n”;
- cree un objeto TextParagraph. Esto agregará texto con división de líneas;
- agregue el TextFragment con TextParagraph.AppendLine;
- agregue el TextParagraph con TextBuilder.AppendParagraph.
Por favor, use el siguiente fragmento de código.

```java
public static void AddNewLineFeed() {        
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    // Inicializar nuevo TextFragment con texto que contiene los marcadores de nueva línea necesarios
    TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");

    // Establecer propiedades del fragmento de texto si es necesario
    textFragment.getTextState().setFontSize (12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());

    // Crear objeto TextParagraph
    TextParagraph par = new TextParagraph();

    // Agregar nuevo TextFragment al párrafo
    par.appendLine(textFragment);

    // Establecer posición del párrafo
    par.setPosition (new Position(100, 600));

    // Crear objeto TextBuilder
    TextBuilder textBuilder = new TextBuilder(page);
    // Agregar el TextParagraph usando TextBuilder
    textBuilder.appendParagraph(par);

    // Guardar el documento PDF resultante.
    pdfDocument.save(_dataDir + "AddNewLineFeed_out.pdf");
}
```

## Cómo añadir texto tachado

La clase TextState proporciona las capacidades para establecer el formato de los TextFragments que se colocan dentro de un documento PDF. Puede utilizar esta clase para establecer el formato del texto como Negrita, Cursiva, Subrayado y a partir de esta versión, la API ha proporcionado las capacidades para marcar el formato del texto como Tachado. Por favor, intente usar el siguiente fragmento de código para añadir TextFragment con formato Tachado.

Por favor, use el fragmento de código completo:

```java
public static void AddStrikeOutText(){
    // Abrir documento
    Document pdfDocument = new Document();
    // Obtener página particular
    Page pdfPage = (Page)pdfDocument.getPages().add();

    // Crear fragmento de texto
    TextFragment textFragment = new TextFragment("texto principal");
    textFragment.setPosition (new Position(100, 600));

    // Establecer propiedades del texto
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());
    // usar el método setStrikeOut para habilitar texto tachado
    textFragment.getTextState().setStrikeOut(true);
    // Marcar texto como Negrita
    textFragment.getTextState().setFontStyle(FontStyles.Bold);

    // Crear objeto TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Añadir el fragmento de texto a la página PDF
    textBuilder.appendText(textFragment);

    // Guardar el documento PDF resultante.
    pdfDocument.save(_dataDir + "AddStrikeOutText_out.pdf");        
}
```


## Aplicar Sombreado de Gradiente al Texto

El formato de texto se ha mejorado aún más en la API para escenarios de edición de texto y ahora puede agregar texto con espacio de color de patrón dentro de un documento PDF. La clase com.aspose.pdf.Color se ha mejorado aún más introduciendo el nuevo método `setPatternColorSpace`, que se puede usar para especificar colores de sombreado para el texto. Este nuevo método agrega diferentes Sombras de Gradiente al texto, por ejemplo, Sombreado Axial, Sombreado Radial (Tipo 3) como se muestra en el siguiente fragmento de código:

```java
public static void ApplyGradientShading() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("always print correctly");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));

    // Crear un nuevo color con espacio de color de patrón
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```


Para aplicar un Degradado Radial, puedes usar el método `setPatternColorSpace` igual a `GradientRadialShading(startingColor, endingColor)` en el fragmento de código anterior.

```java
public static void ApplyGradientShadingRadial() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("always print correctly");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));

    // Crear un nuevo color con espacio de color de patrón
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```

## Cómo alinear texto con contenido flotante

Aspose.PDF admite establecer la alineación del texto para contenidos dentro de un elemento de Caja Flotante.
 Las propiedades de alineación de la instancia Aspose.Pdf.FloatingBox se pueden utilizar para lograr esto como se muestra en el siguiente ejemplo de código.

```java
public static void AlignTextToFloatContent() {
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    FloatingBox floatBox = new FloatingBox(100, 100);
    floatBox.setVerticalAlignment(VerticalAlignment.Bottom); // Ajustar el texto al contenido flotante
    floatBox.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
    floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
    
    page.getParagraphs().add(floatBox);

    FloatingBox floatBox1 = new FloatingBox(100, 100);
    floatBox1.setVerticalAlignment(VerticalAlignment.Center); // Ajustar el texto al contenido centrado
    floatBox1.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox1.getParagraphs().add(new TextFragment("FloatingBox_center"));
    floatBox1.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox1);

    FloatingBox floatBox2 = new FloatingBox(100, 100);
    floatBox2.setVerticalAlignment(VerticalAlignment.Top); // Ajustar el texto al contenido superior
    floatBox2.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox2.getParagraphs().add(new TextFragment("FloatingBox_top"));
    floatBox2.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox2);

    pdfDocument.save(_dataDir + "FloatingBox_alignment_review_out.pdf");        
}
```