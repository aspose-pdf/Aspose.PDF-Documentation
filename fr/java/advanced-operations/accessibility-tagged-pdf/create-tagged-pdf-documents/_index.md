---
title: Créer un PDF balisé en Java
linktitle: Créer un PDF balisé
type: docs
weight: 10
url: /java/create-tagged-pdf/
description: Découvrez comment créer des documents PDF balisés en Java avec Aspose.PDF, y compris des éléments de structure PDF/UA, des champs de formulaire accessibles, des pages de table des matières et le balisage automatique.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Créer un PDF balisé signifie ajouter des éléments de structure qui rendent le document plus facile à valider par rapport aux exigences d'accessibilité PDF/UA et plus facile à interpréter pour les technologies d'assistance.


## 
Créer un simple document PDF balisé

Utilisez cet exemple lorsque vous avez besoin d'un PDF balisé minimal avec un titre et un paragraphe dans l'arborescence de la structure logique.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et obtenez son [ITaggedContent] (https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/).

1. 
Définissez le titre et la langue du document, puis créez les éléments d'en-tête et de paragraphe requis.

1. 
Ajoutez les éléments de structure à l’élément racine et enregistrez le document.


```java
public static void createTaggedPdfDocumentSimple(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        StructureElement rootElement = taggedContent.getRootElement();

        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        HeaderElement mainHeader = taggedContent.createHeaderElement();
        mainHeader.setText("Main Header");

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        paragraphElement.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                + "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. "
                + "Cras pellentesque libero semper, gravida magna sed, luctus leo.");

        rootElement.appendChild(mainHeader, true);
        rootElement.appendChild(paragraphElement, true);
        document.save(outputFile.toString());
    }
}
```

## 
Créer un document PDF balisé avancé

Cet exemple crée une structure plus riche en mélangeant des titres, des paragraphes, des étendues, des guillemets et des paramètres de mise en page explicites.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et initialisez les métadonnées du contenu balisé.

1. 
Créez la structure du titre et du paragraphe, puis ajoutez des étendues et un élément de citation à l'intérieur du paragraphe.

1. 
Ajustez la position du paragraphe, ajoutez les éléments à la structure racine et enregistrez le document.


```java
public static void createTaggedPdfDocumentAdv(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        StructureElement rootElement = taggedContent.getRootElement();

        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        HeaderElement header1 = taggedContent.createHeaderElement(1);
        header1.setText("Header Level 1");

        ParagraphElement paragraphWithQuotes = taggedContent.createParagraphElement();
        paragraphWithQuotes.getStructureTextState().setFont(FontRepository.findFont("Arial"));

        PositionSettings positionSettings = new PositionSettings();
        positionSettings.setMargin(new MarginInfo(10, 5, 10, 5));
        paragraphWithQuotes.adjustPosition(positionSettings);

        SpanElement spanElement1 = taggedContent.createSpanElement();
        spanElement1.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                + "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. ");

        QuoteElement quoteElement = taggedContent.createQuoteElement();
        quoteElement.setText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus.");
        quoteElement.getStructureTextState().setFontStyle(Nullable.of(FontStyles.Bold | FontStyles.Italic));

        SpanElement spanElement2 = taggedContent.createSpanElement();
        spanElement2.setText(" Sed non consectetur elit.");

        paragraphWithQuotes.appendChild(spanElement1, true);
        paragraphWithQuotes.appendChild(quoteElement, true);
        paragraphWithQuotes.appendChild(spanElement2, true);

        rootElement.appendChild(header1, true);
        rootElement.appendChild(paragraphWithQuotes, true);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter un style de texte au contenu balisé

Utilisez cet exemple lorsque le contenu d’un paragraphe balisé doit contenir des informations explicites sur la police, la couleur et le style.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un élément de paragraphe et configurez son état de texte de structure.

1. 
Définissez le texte du paragraphe et enregistrez le document.


```java
public static void addStyle(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();

        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraphElement, true);

        paragraphElement.getStructureTextState().setFontSize(Nullable.of(18.0f));
        paragraphElement.getStructureTextState().setForegroundColor(Color.getRed());
        paragraphElement.getStructureTextState().setFontStyle(Nullable.of(FontStyles.Italic));
        paragraphElement.setText("Red italic text.");

        document.save(outputFile.toString());
    }
}
```

## 
Ajouter des éléments de structure de figure

Cet exemple montre comment créer une figure balisée avec un texte alternatif, un titre, une balise personnalisée, un contenu d'image et un positionnement.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [FigureElement] (https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/figureelement/), définissez ses métadonnées accessibles et attribuez l'image.

1. 
Ajustez la position de la figure et enregistrez le document.


```java
public static void illustrateStructureElements(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();

        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        FigureElement figure1 = taggedContent.createFigureElement();
        taggedContent.getRootElement().appendChild(figure1, true);
        figure1.setAlternativeText("Figure One");
        figure1.setTitle("Image 1");
        figure1.setTag("Fig1");
        figure1.setImage(imageFile.toString(), 300);

        PositionSettings positionSettings = new PositionSettings();
        MarginInfo marginInfo = new MarginInfo();
        marginInfo.setLeft(50);
        marginInfo.setTop(20);
        positionSettings.setMargin(marginInfo);
        figure1.adjustPosition(positionSettings);

        document.save(outputFile.toString());
    }
}
```

## 
Valider un PDF balisé pour PDF/UA

Utilisez cet exemple lorsque vous devez vérifier si un PDF balisé satisfait aux règles de validation PDF/UA.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Exécutez la validation sur [PdfFormat] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).`PDF_UA_1`.

1. 
Rédigez le journal de validation et imprimez le résultat de la validation.


```java
public static void validateTaggedPdf(Path inputFile, Path logFile) {
    try (Document document = new Document(inputFile.toString())) {
        boolean isValid = document.validate(logFile.toString(), PdfFormat.PDF_UA_1);
        System.out.println("Is Valid: " + isValid);
    }
}
```

## 
Ajuster la position des éléments de structure

Cet exemple applique des paramètres de marge et d’alignement explicites à un paragraphe balisé.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez un élément de structure de paragraphe et préparez [PositionSettings] (https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure/positionsettings/).

1. 
Appliquez les paramètres de position au paragraphe et enregistrez le document.


```java
public static void adjustPosition(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();

        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraph = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraph, true);
        paragraph.setText("Text.");

        PositionSettings positionSettings = new PositionSettings();
        MarginInfo marginInfo = new MarginInfo();
        marginInfo.setLeft(300);
        marginInfo.setTop(20);
        marginInfo.setRight(0);
        marginInfo.setBottom(0);
        positionSettings.setMargin(marginInfo);
        positionSettings.setHorizontalAlignment(HorizontalAlignment.None);
        positionSettings.setVerticalAlignment(VerticalAlignment.None);
        positionSettings.setFirstParagraphInColumn(false);
        positionSettings.setKeptWithNext(false);
        positionSettings.setInNewPage(false);
        positionSettings.setInLineParagraph(false);
        paragraph.adjustPosition(positionSettings);

        document.save(outputFile.toString());
    }
}
```

## 
Convertissez un PDF existant en PDF/UA avec le balisage automatique

Utilisez cette approche lorsqu'un PDF existant doit être converti en PDF/UA et balisé automatiquement lors de la conversion.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [PdfFormatConversionOptions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) et activez le balisage automatique.

1. 
Exécutez la conversion et enregistrez le document de sortie.


```java
public static void convertToPdfUaWithAutomaticTagging(Path inputFile, Path outputFile, Path logFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfFormatConversionOptions options = new PdfFormatConversionOptions(
                logFile.toString(), PdfFormat.PDF_UA_1, ConvertErrorAction.Delete);

        AutoTaggingSettings autoTaggingSettings = new AutoTaggingSettings();
        autoTaggingSettings.setEnableAutoTagging(true);
        autoTaggingSettings.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Auto);
        options.setAutoTaggingSettings(autoTaggingSettings);

        document.convert(options);
        document.save(outputFile.toString());
    }
}
```

## 
Créez un PDF balisé avec un champ de formulaire accessible

Cet exemple balise un champ de formulaire de signature afin qu'il fasse partie de l'arborescence de la structure logique.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page avec un champ de formulaire.

1. 
Ajoutez le champ de formulaire à la collection de formulaires de document.

1. 
Créez un élément de structure de formulaire balisé, associez-le au champ et enregistrez le document.


```java
public static void createPdfWithTaggedFormField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        ITaggedContent taggedContent = document.getTaggedContent();
        StructureElement rootElement = taggedContent.getRootElement();

        SignatureField signatureField = new SignatureField(page, new Rectangle(50, 50, 100, 100, true));
        signatureField.setPartialName("Signature1");
        signatureField.setAlternateName("signature 1");

        Form formFields = document.getForm();
        formFields.add(signatureField);

        FormElement form = taggedContent.createFormElement();
        form.setAlternativeText("form 1");
        form.tag(signatureField);
        rootElement.appendChild(form, true);

        document.save(outputFile.toString());
    }
}
```

## 
Créer un PDF balisé avec une page de table des matières

Utilisez cet exemple lorsqu'un PDF balisé doit inclure une page de table des matières de base liée aux en-têtes du document.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une page de table des matières.

1. 
Créez le [TOCElement] (https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/tocelement/) et un en-tête qui doit apparaître dans la table des matières.

1. 
Liez l’entrée de la table des matières au titre et enregistrez le document.


```java
public static void createPdfWithTocPage(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent content = document.getTaggedContent();
        StructureElement rootElement = content.getRootElement();
        content.setLanguage("en-US");

        Page tocPage = document.getPages().add();
        tocPage.setTocInfo(new TocInfo());

        TOCElement tocElement = content.createTOCElement();
        rootElement.appendChild(tocElement, true);

        document.getPages().add();

        HeaderElement header = content.createHeaderElement(1);
        header.setText("1. Header");
        rootElement.appendChild(header, true);

        TOCIElement toci = content.createTOCIElement();
        tocElement.appendChild(toci, true);
        header.addEntryToTocPage(tocPage, toci);
        toci.addRef(header);

        document.save(outputFile.toString());
    }
}
```

## 
Créez un PDF balisé avancé avec une page de table des matières

Cet exemple crée une table des matières balisée plus complexe avec des titres de page liés, des éléments de liste imbriqués et plusieurs niveaux de titre.


1. 
Créez un nouveau [Document] PDF balisé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et préparez une page de table des matières avec un titre visible.

1. 
Créez la structure de la table des matières, liez le titre et les entrées de la table des matières aux titres et aux éléments de liste, et ajoutez les éléments de contenu associés.

1. 
Enregistrez le document final avec la structure TOC avancée.

```java
public static void createPdfWithTocPageAdvanced(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent content = document.getTaggedContent();
        StructureElement rootElement = content.getRootElement();
        content.setLanguage("en-US");

        Page tocPage = document.getPages().add();
        tocPage.setTocInfo(new TocInfo());
        tocPage.getTocInfo().setTitle(new TextFragment("Table of Contents"));

        TOCElement tocElement = content.createTOCElement();
        HeaderElement headerForTocPageTitle = content.createHeaderElement(1);
        tocElement.linkTocPageTitleToHeaderElement(tocPage, headerForTocPageTitle);

        rootElement.appendChild(headerForTocPageTitle, true);
        rootElement.appendChild(tocElement, true);

        document.getPages().add();

        HeaderElement header = content.createHeaderElement(1);
        header.setText("1. Header");
        rootElement.appendChild(header, true);

        TOCIElement toci = content.createTOCIElement();
        tocElement.appendChild(toci, true);
        header.addEntryToTocPage(tocPage, toci);
        toci.addRef(header);

        ListElement listElement = content.createListElement();
        for (int i = 1; i < 4; i++) {
            ListLIElement li = content.createListLIElement();
            listElement.appendChild(li, true);

            HeaderElement subHeader = content.createHeaderElement(2);
            subHeader.getStructureTextState().setFontSize(Nullable.of(14.0f));
            subHeader.setLanguage("en-US");
            subHeader.setText("1." + i + " subheader ");
            subHeader.addEntryToTocPage(tocPage, li);
            li.addRef(subHeader);

            ParagraphElement p = content.createParagraphElement();
            p.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit.");
            p.setLanguage("en-US");

            rootElement.appendChild(subHeader, true);
            rootElement.appendChild(p, true);
        }
        toci.appendChild(listElement, true);

        HeaderElement header2 = content.createHeaderElement(1);
        header2.setText("2. Header");
        rootElement.appendChild(header2, true);

        TOCIElement toci2 = content.createTOCIElement();
        tocElement.appendChild(toci2, true);
        header2.addEntryToTocPage(tocPage, toci2);
        toci2.addRef(header2);

        document.save(outputFile.toString());
    }
}
```
