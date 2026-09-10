---
title: Définir les propriétés des éléments de structure PDF balisés en Java
linktitle: Définition des propriétés des éléments de structure
type: docs
weight: 30
url: /java/setting-structure-elements-properties/
description: Découvrez comment définir les propriétés des éléments de structure PDF balisés en Java avec Aspose.PDF, notamment le titre, la langue, le texte réel, le texte alternatif, le texte d'expansion, les liens, les notes et les noms de balises.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Cette page couvre les modèles courants de définition de propriétés pour les éléments de structure PDF balisés en Java.


## 
Définir les propriétés communes des éléments de structure

Utilisez cet exemple lorsqu'un élément de structure balisé doit exposer des métadonnées d'accessibilité telles que le titre, la langue, le texte réel et le texte alternatif.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et initialisez les métadonnées du contenu balisé.

1. 
Créez une section et un élément d'en-tête dans l'arborescence de la structure.

1. 
Définissez les propriétés de l'en-tête et enregistrez le document.


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

## 
Définir des éléments de texte

Utilisez cet exemple lorsque vous devez ajouter un simple élément de paragraphe à l’arborescence de structure balisée.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [ParagraphElement] (https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/) et définissez son texte.

1. 
Ajoutez le paragraphe à l’élément racine et enregistrez le document.


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

## 
Définir les éléments du bloc de texte

Cet exemple crée plusieurs éléments de structure au niveau du bloc, notamment des titres de plusieurs niveaux et un paragraphe.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez des éléments d'en-tête pour les niveaux requis, puis créez un élément de paragraphe.

1. 
Ajoutez les éléments de bloc à la structure racine et enregistrez le document.


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

## 
Définir des éléments en ligne

Utilisez cet exemple lorsque les éléments de structure de bloc doivent contenir des étendues en ligne imbriquées.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez des éléments d’en-tête et ajoutez-y des enfants span.

1. 
Créez un paragraphe avec plusieurs travées et enregistrez le document.


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

## 
Définir des noms de balises personnalisés

Cet exemple attribue des noms de balises personnalisées aux éléments paragraphe et span dans la structure balisée.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez un élément de section.

1. 
Créez des paragraphes et des étendues, puis définissez des noms de balises personnalisés pour chaque élément.

1. 
Ajoutez les éléments à la section et enregistrez le document.


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

## 
Définir les éléments de lien et de figure

Utilisez cet exemple lorsque les éléments de lien balisés doivent inclure des descriptions alternatives, des hyperliens et du contenu de figure avec des attributs de mise en page.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez des éléments de lien à l'intérieur des paragraphes.

1. 
Configurez les cibles des liens hypertexte, les descriptions alternatives et l'élément de figure lié.

1. 
Définissez l'attribut de mise en page requis et enregistrez le document.


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

## 
Ajouter des paragraphes avec du contenu lié aux liens en ligne

Cet exemple crée des éléments de paragraphe qui combinent du texte brut et des éléments span imbriqués.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez des éléments de paragraphe et ajoutez des enfants span avec du texte personnalisé.

1. 
Ajoutez les paragraphes à l’élément racine et enregistrez le document.


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

## 
Définir des éléments de note

Utilisez cet exemple lorsque des éléments de structure de note doivent être créés avec des ID automatiques ou explicites.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez un élément de paragraphe.

1. 
Créez des éléments de note et définissez leur texte et leurs identifiants selon vos besoins.

1. 
Ajoutez les notes au paragraphe et enregistrez le document.


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

## 
Définir la langue et le titre du contenu multilingue

Cet exemple attribue des métadonnées au niveau du document, puis crée des paragraphes avec différentes valeurs de langue.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et définissez le titre et la langue du document.

1. 
Ajoutez un élément d'en-tête et créez des paragraphes pour chaque phrase localisée.

1. 
Enregistrez le document balisé multilingue.


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

## 
Ajouter un assistant de paragraphe pour le contenu balisé

Cette méthode d'assistance crée un paragraphe, attribue sa langue et l'ajoute à la structure racine.


1. 
Créez un [ParagraphElement] (https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/).

1. 
Définissez le texte et la langue de l'élément.

1. 
Ajoutez le paragraphe à l’élément racine du contenu balisé.

```java
private static void addParagraph(ITaggedContent taggedContent, String text, String language) {
    ParagraphElement paragraph = taggedContent.createParagraphElement();
    paragraph.setText(text);
    paragraph.setLanguage(language);
    taggedContent.getRootElement().appendChild(paragraph, true);
}
```
