---
title: Java에서 태그가 있는 PDF 만들기
linktitle: 태그가 있는 PDF 만들기
type: docs
weight: 10
url: /java/create-tagged-pdf/
description: PDF/UA 구조 요소, 액세스 가능한 양식 필드, TOC 페이지 및 자동 태그 지정을 포함하여 Aspose.PDF를 사용하여 Java에서 태그가 지정된 PDF 문서를 만드는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

태그가 있는 PDF를 생성한다는 것은 문서를 PDF/UA 접근성 요구 사항에 따라 더 쉽게 검증하고 보조 기술을 더 쉽게 해석할 수 있도록 하는 구조 요소를 추가하는 것을 의미합니다.


## 
간단한 태그가 있는 PDF 문서 만들기

논리적 구조 트리에 제목과 단락이 있는 최소한의 태그가 있는 PDF가 필요한 경우 이 예를 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 해당 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/)를 가져옵니다.

1. 
문서 제목과 언어를 설정한 다음 필요한 헤더와 단락 요소를 만듭니다.

1. 
구조 요소를 루트 요소에 추가하고 문서를 저장합니다.


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
고급 태그가 있는 PDF 문서 만들기

이 예에서는 제목, 단락, 범위, 인용문 및 명시적 레이아웃 설정을 혼합하여 더욱 풍부한 구조를 구축합니다.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 생성하고 태그된 콘텐츠 메타데이터를 초기화합니다.

1. 
제목과 단락 구조를 구축한 다음 단락 내부에 범위와 인용 요소를 추가합니다.

1. 
단락 위치를 조정하고 요소를 루트 구조에 추가한 다음 문서를 저장합니다.


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
태그된 콘텐츠에 텍스트 스타일 추가

태그가 지정된 단락 콘텐츠에 명시적인 글꼴, 색상 및 스타일 정보가 포함되어야 하는 경우 이 예를 사용하세요.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
단락 요소를 만들고 구조 텍스트 상태를 구성합니다.

1. 
단락 텍스트를 설정하고 문서를 저장합니다.


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
그림 구조 요소 추가

이 예에서는 대체 텍스트, 제목, 사용자 정의 태그, 이미지 콘텐츠 및 위치 지정을 사용하여 태그가 지정된 그림을 만드는 방법을 보여줍니다.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
[FigureElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/figureelement/)를 만들고, 액세스 가능한 메타데이터를 설정하고, 이미지를 할당합니다.

1. 
도형 위치를 조정하고 문서를 저장합니다.


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
PDF/UA용 태그가 있는 PDF 확인

태그가 있는 PDF가 PDF/UA 유효성 검사 규칙을 충족하는지 확인해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).`PDF_UA_1`에 대해 유효성 검사를 실행합니다.

1. 
검증 로그를 작성하고 검증 결과를 인쇄합니다.


```java
public static void validateTaggedPdf(Path inputFile, Path logFile) {
    try (Document document = new Document(inputFile.toString())) {
        boolean isValid = document.validate(logFile.toString(), PdfFormat.PDF_UA_1);
        System.out.println("Is Valid: " + isValid);
    }
}
```

## 
구조 요소 위치 조정

이 예에서는 태그가 지정된 단락에 명시적 여백 및 정렬 설정을 적용합니다.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
단락 구조 요소를 추가하고 [위치 설정](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure/positionsettings/)을 준비합니다.

1. 
단락에 위치 설정을 적용하고 문서를 저장합니다.


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
자동 태그를 사용하여 기존 PDF를 PDF/UA로 변환

기존 PDF를 PDF/UA로 변환하고 변환 중에 자동으로 태그를 지정해야 하는 경우 이 접근 방식을 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/)를 만들고 자동 태그 지정을 활성화하세요.

1. 
변환을 실행하고 출력 문서를 저장합니다.


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
접근 가능한 양식 필드를 사용하여 태그가 있는 PDF 만들기

이 예에서는 서명 양식 필드에 태그를 지정하여 논리적 구조 트리의 일부가 됩니다.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 양식 필드가 있는 페이지를 추가하세요.

1. 
문서 양식 컬렉션에 양식 필드를 추가합니다.

1. 
태그가 있는 양식 구조 요소를 생성하고 이를 필드와 연결한 후 문서를 저장합니다.


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
목차 페이지가 포함된 태그가 있는 PDF 만들기

태그가 있는 PDF에 문서 제목에 연결된 기본 목차 페이지가 포함되어야 하는 경우 이 예를 사용하십시오.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 목차 페이지를 추가합니다.

1. 
[TOCElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/tocelement/)와 TOC에 표시될 헤더를 만듭니다.

1. 
목차 항목을 제목에 연결하고 문서를 저장합니다.


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
목차 페이지가 포함된 고급 태그가 있는 PDF 만들기

이 예는 연결된 페이지 제목, 중첩된 목록 항목 및 여러 제목 수준을 사용하여 보다 복잡한 태그가 지정된 목차를 구축합니다.


1. 
새로운 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 제목이 보이는 목차 페이지를 준비합니다.

1. 
목차 구조를 생성하고 목차 제목과 항목을 머리글 및 목록 항목에 연결하고 관련 콘텐츠 요소를 추가합니다.

1. 
고급 목차 구조로 최종 문서를 저장합니다.

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
