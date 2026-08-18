---
title: Definir propriedades de elementos de estrutura PDF marcados em Java
linktitle: Definir propriedades de elementos estruturais
type: docs
weight: 30
url: /java/setting-structure-elements-properties/
description: Aprenda como definir propriedades de elementos de estrutura PDF marcados em Java com Aspose.PDF, incluindo título, idioma, texto real, texto alternativo, texto de expansão, links, notas e nomes de tags.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Esta página aborda padrões comuns de configuração de propriedades para elementos de estrutura PDF marcados em Java.

## Definir propriedades comuns de elementos de estrutura

Use este exemplo quando um elemento de estrutura marcado precisar expor metadados de acessibilidade, como título, idioma, texto real e texto alternativo.

1. Crie um novo PDF marcado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e inicialize os metadados do conteúdo marcado.
1. Crie uma seção e um elemento de cabeçalho na árvore de estrutura.
1. Defina as propriedades do cabeçalho e salve o documento.

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

## Definir elementos de texto

Use este exemplo quando precisar adicionar um elemento de parágrafo simples à árvore de estrutura marcada.

1. Crie um novo PDF marcado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/) e defina seu texto.
1. Anexe o parágrafo ao elemento raiz e salve o documento.

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

## Definir elementos de bloco de texto

Este exemplo cria vários elementos de estrutura em nível de bloco, incluindo títulos de vários níveis e um parágrafo.

1. Crie um novo PDF marcado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione elementos de cabeçalho para os níveis necessários e crie um elemento de parágrafo.
1. Anexe os elementos do bloco à estrutura raiz e salve o documento.

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

## Definir elementos embutidos

Use este exemplo quando os elementos da estrutura de bloco devem conter extensões embutidas aninhadas.

1. Crie um novo PDF marcado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie elementos de cabeçalho e anexe span filhos a eles.
1. Crie um parágrafo com vários trechos e salve o documento.

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

## Definir nomes de tags personalizados

Este exemplo atribui nomes de tags personalizados a elementos de parágrafo e extensão na estrutura marcada.

1. Crie um novo PDF marcado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione um elemento de seção.
1. Crie parágrafos e trechos e defina nomes de tags personalizados para cada elemento.
1. Anexe os elementos à seção e salve o documento.

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

## Definir elementos de link e figura

Use este exemplo quando os elementos de link marcados devem incluir descrições alternativas, hiperlinks e conteúdo de figura com atributos de layout.

1. Crie um novo PDF marcado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione elementos de link dentro dos parágrafos.
1. Configure destinos de hiperlink, descrições alternativas e o elemento de figura vinculado.
1. Defina o atributo de layout necessário e salve o documento.

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

## Adicione parágrafos com conteúdo relacionado a links embutidos

Este exemplo cria elementos de parágrafo que combinam texto simples e elementos de extensão aninhados.

1. Crie um novo PDF marcado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie elementos de parágrafo e adicione filhos de extensão com texto personalizado.
1. Anexe os parágrafos ao elemento raiz e salve o documento.

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

## Definir elementos de nota

Use este exemplo quando os elementos da estrutura de notas devem ser criados com IDs automáticos ou explícitos.

1. Crie um novo PDF marcado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione um elemento de parágrafo.
1. Crie elementos de nota e defina seu texto e IDs conforme necessário.
1. Anexe as notas ao parágrafo e salve o documento.

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

## Defina o idioma e o título do conteúdo multilíngue

Este exemplo atribui metadados em nível de documento e, em seguida, cria parágrafos com valores de idioma diferentes.

1. Crie um novo PDF marcado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e defina o título e o idioma do documento.
1. Adicione um elemento de cabeçalho e crie parágrafos para cada frase localizada.
1. Salve o documento marcado multilíngue.

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

## Adicione um auxiliar de parágrafo para conteúdo marcado

Este método auxiliar cria um parágrafo, atribui seu idioma e o anexa à estrutura raiz.

1. Crie um [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/).
1. Defina o texto e o idioma do elemento.
1. Anexe o parágrafo ao elemento raiz do conteúdo marcado.

```java
private static void addParagraph(ITaggedContent taggedContent, String text, String language) {
    ParagraphElement paragraph = taggedContent.createParagraphElement();
    paragraph.setText(text);
    paragraph.setLanguage(language);
    taggedContent.getRootElement().appendChild(paragraph, true);
}
```
