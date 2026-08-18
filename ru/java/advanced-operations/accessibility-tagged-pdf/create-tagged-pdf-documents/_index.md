---
title: Создать PDF-файл с тегами в Java
linktitle: Создать PDF с тегами
type: docs
weight: 10
url: /java/create-tagged-pdf/
description: Узнайте, как создавать PDF-документы с тегами на Java с помощью Aspose.PDF, включая элементы структуры PDF/UA, доступные поля форм, страницы содержания и автоматическую маркировку.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Создание PDF-файла с тегами означает добавление элементов структуры, которые упрощают проверку документа на соответствие требованиям доступности PDF/UA и облегчают интерпретацию вспомогательным технологиям.

## Создайте простой PDF-документ с тегами

Используйте этот пример, если вам нужен минимальный PDF-файл с тегами, заголовком и абзацем в дереве логической структуры.

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и получите его [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/).
1. Задайте заголовок и язык документа, затем создайте необходимые элементы заголовка и абзаца.
1. Добавьте элементы структуры к корневому элементу и сохраните документ.

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

## Создайте расширенный PDF-документ с тегами

В этом примере создается более богатая структура путем смешивания заголовков, абзацев, интервалов, кавычек и явных настроек макета.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и инициализируйте метаданные размеченного контента.
1. Создайте структуру заголовка и абзаца, затем добавьте интервалы и элемент кавычки внутри абзаца.
1. Отрегулируйте положение абзаца, добавьте элементы в корневую структуру и сохраните документ.

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

## Добавьте стиль текста к отмеченному контенту

Используйте этот пример, когда содержимое абзаца с тегами должно содержать явную информацию о шрифте, цвете и стиле.

1. Создайте новый PDF-файл с тегами [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте элемент абзаца и настройте его текстовое состояние.
1. Задайте текст абзаца и сохраните документ.

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

## Добавьте элементы структуры фигуры

В этом примере показано, как создать фигуру с тегом с альтернативным текстом, заголовком, настраиваемым тегом, содержимым изображения и расположением.

1. Создайте новый PDF-файл с тегами [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [FigureElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/figureelement/), установите его доступные метаданные и назначьте изображение.
1. Отрегулируйте положение фигуры и сохраните документ.

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

## Проверка PDF-файла с тегами на наличие PDF/UA

Используйте этот пример, когда вам нужно проверить, удовлетворяет ли PDF с тегами правилам проверки PDF/UA.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Запустите проверку по [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).`PDF_UA_1`.
1. Запишите журнал проверки и распечатайте результат проверки.

```java
public static void validateTaggedPdf(Path inputFile, Path logFile) {
    try (Document document = new Document(inputFile.toString())) {
        boolean isValid = document.validate(logFile.toString(), PdfFormat.PDF_UA_1);
        System.out.println("Is Valid: " + isValid);
    }
}
```

## Отрегулируйте положение элемента конструкции

В этом примере к абзацу с тегами применяются явные настройки полей и выравнивания.

1. Создайте новый PDF-файл с тегами [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте элемент структуры абзаца и подготовьте [PositionSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure/positionsettings/).
1. Примените настройки положения к абзацу и сохраните документ.

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

## Преобразование существующего PDF-файла в PDF/UA с автоматической маркировкой

Используйте этот подход, когда существующий PDF-файл необходимо преобразовать в PDF/UA и автоматически пометить тегами во время преобразования.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) и включите автоматическую пометку тегами.
1. Запустите преобразование и сохраните выходной документ.

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

## Создайте PDF-файл с тегами и доступным полем формы.

В этом примере поле формы подписи помечается тегом, чтобы оно стало частью дерева логической структуры.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте страницу с полем формы.
1. Добавьте поле формы в коллекцию форм документа.
1. Создайте элемент структуры формы с тегами, свяжите его с полем и сохраните документ.

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

## Создайте PDF-файл с тегами и оглавлением.

Используйте этот пример, когда PDF-файл с тегами должен включать базовую страницу оглавления, связанную с заголовками документа.

1. Создайте новый PDF-файл с тегом [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте страницу содержания.
1. Создайте [TOCElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/tocelement/) и заголовок, который должен появиться в оглавлении.
1. Свяжите запись оглавления с заголовком и сохраните документ.

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

## Создайте расширенный PDF-файл с тегами и оглавлением.

В этом примере создается более сложное содержание с тегами и связанными заголовками страниц, вложенными элементами списка и несколькими уровнями заголовков.

1. Создайте новый PDF-файл с тегами [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и подготовьте страницу содержания с видимым заголовком.
1. Создайте структуру оглавления, свяжите заголовок и записи оглавления с заголовками и элементами списка, а также добавьте соответствующие элементы контента.
1. Сохраните окончательный документ с расширенной структурой оглавления.

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
