---
title: Establecer propiedades del elemento de estructura Tagged PDF en Java
linktitle: Estableciendo propiedades de Structure Elements
type: docs
weight: 30
url: /es/java/setting-structure-elements-properties/
description: Aprenda cómo establecer propiedades de los elementos de estructura de PDF etiquetado en Java con Aspose.PDF, incluyendo título, idioma, texto real, texto alternativo, texto de expansión, enlaces, notas y nombres de etiquetas.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Esta página cubre patrones comunes de configuración de propiedades para los elementos de estructura de PDF etiquetado en Java.

## Establecer propiedades comunes de Structure Elements

Utilice este ejemplo cuando un elemento de estructura etiquetado debe exponer metadatos de accesibilidad como título, idioma, texto real y texto alternativo.

1. Cree un nuevo Tagged PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e inicializa los metadatos de contenido etiquetado.
1. Cree una sección y un elemento de encabezado en el árbol de estructura.
1. Establezca las propiedades del encabezado y guarde el documento.

```java
public static void setProperties(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        StructureElement rootElement = taggedContent.getRootElement();
        SectElement sectionElement = taggedContent.createSectElement();
        rootElement.appendChild(sectionElement, true);

        HeaderElement headerElement = taggedContent.createHeaderElement(1);
        sectionElement.appendChild(headerElement, true);
        headerElement.setText("The Header");

        headerElement.setTitle("Title");
        headerElement.setLanguage("en-US");
        headerElement.setAlternativeText("Alternative Text");
        headerElement.setExpansionText("Expansion Text");
        headerElement.setActualText("Actual Text");

        document.save(outputFile.toString());
    }
}
```

## Establecer elementos de texto

Utilice este ejemplo cuando necesite agregar un elemento de párrafo simple al árbol de estructura etiquetado.

1. Cree un nuevo Tagged PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`ParagraphElement`](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/) y establezca su texto.
1. Agregue el párrafo al elemento raíz y guarde el documento.

```java
public static void setTextElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        paragraphElement.setText("Paragraph.");
        taggedContent.getRootElement().appendChild(paragraphElement, true);

        document.save(outputFile.toString());
    }
}
```

## Establecer elementos de bloque de texto

Este ejemplo crea varios elementos de estructura a nivel de bloque, incluidos encabezados de varios niveles y un párrafo.

1. Cree un nuevo Tagged PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregue elementos de encabezado para los niveles requeridos y luego crea un elemento de párrafo.
1. Agregue los elementos de bloque a la estructura raíz y guarde el documento.

```java
public static void setTextBlockElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        for (int level = 1; level <= 6; level++) {
            HeaderElement header = taggedContent.createHeaderElement(level);
            header.setText("H" + level + ". Header of Level " + level);
            taggedContent.getRootElement().appendChild(header, true);
        }

        ParagraphElement p = taggedContent.createParagraphElement();
        p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                + "Aenean nec lectus ac sem faucibus imperdiet.");
        taggedContent.getRootElement().appendChild(p, true);

        document.save(outputFile.toString());
    }
}
```

## Establecer elementos en línea

Utilice este ejemplo cuando los elementos de estructura de bloque deben contener spans en línea anidados.

1. Cree un nuevo Tagged PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Construya los elementos de encabezado y agregue los span como hijos.
1. Cree un párrafo con múltiples spans y guarde el documento.

```java
public static void setInlineElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        for (int level = 1; level <= 6; level++) {
            HeaderElement header = taggedContent.createHeaderElement(level);
            taggedContent.getRootElement().appendChild(header, true);

            SpanElement span1 = taggedContent.createSpanElement();
            span1.setText("H" + level + ". ");
            header.appendChild(span1, true);

            SpanElement span2 = taggedContent.createSpanElement();
            span2.setText("Level " + level + " Header");
            header.appendChild(span2, true);
        }

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        paragraphElement.setText("P. ");
        taggedContent.getRootElement().appendChild(paragraphElement, true);

        for (int index = 1; index <= 10; index++) {
            SpanElement span = taggedContent.createSpanElement();
            span.setText("Span " + index + ". ");
            paragraphElement.appendChild(span, true);
        }

        document.save(outputFile.toString());
    }
}
```

## Establecer nombres de etiqueta personalizados

Este ejemplo asigna nombres de etiqueta personalizados a los elementos de párrafo y span en la estructura etiquetada.

1. Cree un nuevo Tagged PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y añada un elemento de sección.
1. Cree párrafos y spans, luego establece nombres de etiqueta personalizados para cada elemento.
1. Agregue los elementos a la sección y guarde el documento.

```java
public static void setTagName(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        SectElement sectionElement = taggedContent.createSectElement();
        taggedContent.getRootElement().appendChild(sectionElement, true);

        String[] paragraphTags = {"P1", "Para", "Para", "Paragraph"};
        String[] spanTags = {"SPAN", "Sp", "Sp", "TheSpan"};

        for (int index = 0; index < 4; index++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            paragraph.setText("P" + (index + 1) + ". ");
            paragraph.setTag(paragraphTags[index]);

            SpanElement span = taggedContent.createSpanElement();
            span.setText("Span " + (index + 1) + ".");
            span.setTag(spanTags[index]);

            paragraph.appendChild(span, true);
            sectionElement.appendChild(paragraph, true);
        }

        document.save(outputFile.toString());
    }
}
```

## Establecer elementos de enlace y figura

Utilice este ejemplo cuando los elementos de enlace etiquetados deben incluir descripciones alternativas, hipervínculos y contenido de figura con atributos de diseño.

1. Cree un nuevo Tagged PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agregue elementos de enlace dentro de los párrafos.
1. Configure los destinos de hipervínculo, descripciones alternativas y el elemento de figura vinculado.
1. Establezca el atributo de diseño requerido y guarde el documento.

```java
public static void setElements(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Link Elements Example");
        taggedContent.setLanguage("en-US");

        for (int index = 1; index <= 4; index++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            taggedContent.getRootElement().appendChild(paragraph, true);

            LinkElement link = taggedContent.createLinkElement();
            paragraph.appendChild(link, true);
            link.setHyperlink(new WebHyperlink("http://google.com"));
            link.setText(index == 4 ? "The multiline link: Google Google Google Google" : "Google");
            link.setAlternateDescriptions("Link to Google");
        }

        ParagraphElement paragraph = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraph, true);

        LinkElement link = taggedContent.createLinkElement();
        paragraph.appendChild(link, true);
        link.setHyperlink(new WebHyperlink("http://google.com"));

        FigureElement figure = taggedContent.createFigureElement();
        figure.setImage(imageFile.toString(), 1200);
        figure.setAlternativeText("Google icon");

        StructureAttributes linkLayoutAttributes = link.getAttributes().getAttributes(AttributeOwnerStandard.Layout);
        StructureAttribute placementAttribute = new StructureAttribute(AttributeKey.Placement);
        placementAttribute.setNameValue(AttributeName.Placement_Block);
        linkLayoutAttributes.setAttribute(placementAttribute);

        link.appendChild(figure, true);
        link.setAlternateDescriptions("Link to Google");

        document.save(outputFile.toString());
    }
}
```

## Agregar párrafos con contenido de enlaces en línea

Este ejemplo crea elementos de párrafo que combinan texto plano y elementos de span anidados.

1. Cree un nuevo Tagged PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree elementos de párrafo y añada hijos span con texto personalizado.
1. Agregue los párrafos al elemento raíz y guarde el documento.

```java
public static void addLinkElement(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Text Elements Example");
        taggedContent.setLanguage("en-US");

        for (int paragraphIndex = 1; paragraphIndex <= 4; paragraphIndex++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            taggedContent.getRootElement().appendChild(paragraph, true);

            SpanElement span1 = taggedContent.createSpanElement();
            span1.setText("Span_" + paragraphIndex + "1");
            SpanElement span2 = taggedContent.createSpanElement();
            span2.setText(" and Span_" + paragraphIndex + "2.");

            paragraph.setText("Paragraph with ");
            paragraph.appendChild(span1, true);
            paragraph.appendChild(span2, true);
        }

        document.save(outputFile.toString());
    }
}
```

## Establecer elementos de nota

Utilice este ejemplo cuando los elementos de estructura de nota deben crearse con IDs automáticos o explícitos.

1. Cree un nuevo Tagged PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y añada un elemento de párrafo.
1. Cree elementos de nota y establezca su texto e IDs según sea necesario.
1. Adjunte las notas al párrafo y guarde el documento.

```java
public static void setNoteElement(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Sample of Note Elements");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraph = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraph, true);

        NoteElement note1 = taggedContent.createNoteElement();
        paragraph.appendChild(note1, true);
        note1.setText("Note with auto generate ID. ");

        NoteElement note2 = taggedContent.createNoteElement();
        paragraph.appendChild(note2, true);
        note2.setText("Note with ID = 'note_002'. ");
        note2.setId("note_002");

        NoteElement note3 = taggedContent.createNoteElement();
        paragraph.appendChild(note3, true);
        note3.setText("Note with ID = 'note_003'. ");
        note3.setId("note_003");

        document.save(outputFile.toString());
    }
}
```

## Establecer idioma y título para contenido multilingüe

Este ejemplo asigna metadatos a nivel de documento y luego crea párrafos con diferentes valores de idioma.

1. Cree un nuevo Tagged PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y establezca el título del documento y el idioma.
1. Agregue un elemento de encabezado y cree párrafos para cada frase localizada.
1. Guarde el documento etiquetado multilingüe.

```java
public static void setLanguageAndTitle(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example Tagged Document");
        taggedContent.setLanguage("en-US");

        HeaderElement header = taggedContent.createHeaderElement(1);
        header.setText("Phrase on different languages");
        taggedContent.getRootElement().appendChild(header, true);

        addParagraph(taggedContent, "Hello, World!", "en-US");
        addParagraph(taggedContent, "Hallo Welt!", "de-DE");
        addParagraph(taggedContent, "Bonjour le monde!", "fr-FR");
        addParagraph(taggedContent, "Hola Mundo!", "es-ES");

        document.save(outputFile.toString());
    }
}
```

## Agregar un asistente de párrafo para contenido etiquetado

Este método auxiliar crea un párrafo, le asigna el idioma y lo agrega a la estructura raíz.

1. Cree un [`ParagraphElement`](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/).
1. Establezca el texto y el idioma para el elemento.
1. Añada el párrafo al elemento raíz del contenido etiquetado.

```java
private static void addParagraph(ITaggedContent taggedContent, String text, String language) {
    ParagraphElement paragraph = taggedContent.createParagraphElement();
    paragraph.setText(text);
    paragraph.setLanguage(language);
    taggedContent.getRootElement().appendChild(paragraph, true);
}
```
