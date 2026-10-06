---
title: Criar Tagged PDF em Java
linktitle: Criar Tagged PDF
type: docs
weight: 10
url: /pt/java/create-tagged-pdf/
description: Aprenda a criar documentos PDF marcados em Java com Aspose.PDF, incluindo elementos de estrutura PDF/UA, campos de formulário acessíveis, páginas de TOC e marcação automática.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /pt/java/create-tagged-pdf-documents/
---
Criar um PDF marcado significa adicionar elementos de estrutura que tornam o documento mais fácil de validar em conformidade com os requisitos de acessibilidade PDF/UA e mais fácil de ser interpretado por tecnologias assistivas.

## Criar um documento Tagged PDF simples

Use este exemplo quando precisar de um PDF marcado mínimo com um título e um parágrafo na árvore de estrutura lógica.

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e obter o seu [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/).
1. Defina o título e o idioma do documento, então crie os elementos de cabeçalho e parágrafo necessários.
1. Anexe os elementos de estrutura ao elemento raiz e salve o documento.

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

## Criar um documento Tagged PDF avançado

Este exemplo cria uma estrutura mais rica ao combinar cabeçalhos, parágrafos, spans, citações e configurações explícitas de layout.

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e inicializar metadados de conteúdo marcado.
1. Construa a estrutura de título e parágrafo, depois adicione spans e um elemento de citação dentro do parágrafo.
1. Ajuste a posição do parágrafo, anexe os elementos à estrutura raiz e salve o documento.

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

## Adicionar estilo de texto ao conteúdo marcado

Use este exemplo quando o conteúdo de parágrafo marcado deve conter informações explícitas de fonte, cor e estilo.

1. Criar um novo PDF marcado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um elemento de parágrafo e configure seu estado de texto de estrutura.
1. Defina o texto do parágrafo e salve o documento.

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

## Adicionar elementos de estrutura de figura

Este exemplo mostra como criar uma figura marcada com texto alternativo, título, tag personalizada, conteúdo de imagem e posicionamento.

1. Criar um novo PDF marcado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Criar um [FigureElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/figureelement/), defina seus metadados acessíveis e atribua a imagem.
1. Ajuste a posição da figura e salve o documento.

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

## Validar um PDF marcado para PDF/UA

Use este exemplo quando precisar verificar se um PDF marcado satisfaz as regras de validação PDF/UA.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Executar validação contra [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).`PDF_UA_1`.
1. Escreva o registro de validação e imprima o resultado da validação.

```java
public static void validateTaggedPdf(Path inputFile, Path logFile) {
    try (Document document = new Document(inputFile.toString())) {
        boolean isValid = document.validate(logFile.toString(), PdfFormat.PDF_UA_1);
        System.out.println("Is Valid: " + isValid);
    }
}
```

## Ajustar a posição do elemento de estrutura

Este exemplo aplica configurações explícitas de margem e alinhamento a um parágrafo marcado.

1. Criar um novo PDF marcado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicionar um elemento de estrutura de parágrafo e preparar [PositionSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure/positionsettings/).
1. Aplique as configurações de posição ao parágrafo e salve o documento.

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

## Converter um PDF existente para PDF/UA com marcação automática

Use esta abordagem quando um PDF existente deve ser convertido para PDF/UA e marcado automaticamente durante a conversão.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Criar [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) e habilite a marcação automática.
1. Execute a conversão e salve o documento de saída.

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

## Crie um PDF marcado com um campo de formulário acessível

Este exemplo marca um campo de formulário de assinatura para que ele faça parte da árvore de estrutura lógica.

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página com um campo de formulário.
1. Adicione o FormField à coleção de formulários do documento.
1. Criar um elemento de estrutura de formulário marcado, associá-lo ao campo e salvar o documento.

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

## Criar um PDF marcado com uma página de índice

Use este exemplo quando um PDF marcado deve incluir uma página de índice básica vinculada aos títulos do documento.

1. Criar um novo PDF marcado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página de TOC.
1. Criar o [TOCElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/tocelement/) e um cabeçalho que deve aparecer no TOC.
1. Vincule a entrada do TOC ao título e salve o documento.

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

## Criar um PDF marcado avançado com uma página de TOC

Este exemplo constrói um TOC marcado mais complexo com títulos de página vinculados, itens de lista aninhados e múltiplos níveis de título.

1. Criar um novo PDF marcado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e prepare uma página de TOC com um título visível.
1. Crie a estrutura TOC, vincule o título e as entradas do TOC aos cabeçalhos e itens de lista e adicione os elementos de conteúdo relacionados.
1. Salve o documento final com a estrutura avançada de TOC.

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
