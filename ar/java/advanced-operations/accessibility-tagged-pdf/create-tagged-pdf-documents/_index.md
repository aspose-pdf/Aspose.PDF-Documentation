---
title: إنشاء Tagged PDF في Java
linktitle: إنشاء Tagged PDF
type: docs
weight: 10
url: /ar/java/create-tagged-pdf/
description: تعلم كيفية إنشاء مستندات PDF موسومة في Java باستخدام Aspose.PDF، بما في ذلك عناصر Structure Elements الخاصة بـ PDF/UA، حقول FormField القابلة للوصول، صفحات TOC، والوسم التلقائي.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
إنشاء ملف PDF مؤشَّر يعني إضافة عناصر هيكل تجعل المستند أسهل في التحقق منه وفق متطلبات الوصول PDF/UA وأسهل للتقنيات المساعدة في تفسيره.

## إنشاء مستند PDF معلم بسيط

استخدم هذا المثال عندما تحتاج إلى ملف Tagged PDF بسيط يحتوي على عنوان وفقرة في شجرة البنية المنطقية.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وحصل على الخاص به [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/).
1. حدد عنوان المستند واللغة، ثم أنشئ عناصر الرأس والفقرة المطلوبة.
1. أضف عناصر الهيكل إلى العنصر الجذر واحفظ المستند.

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

## إنشاء مستند PDF موسوم متقدم

يبني هذا المثال هيكلًا أكثر ثراءً من خلال دمج العناوين والفقرات والـ spans والاقتباسات وإعدادات التخطيط الصريحة.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وتتهيئة بيانات تعريف المحتوى الموسوم.
1. قم بإنشاء هيكل العنوان والفقرة، ثم أضف عناصر span وعنصر الاقتباس داخل الفقرة.
1. ضبط موضع الفقرة، إلحاق العناصر بالهيكل الجذري، وحفظ المستند.

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

## إضافة نمط النص إلى المحتوى الموسوم

استخدم هذا المثال عندما يجب أن يحمل محتوى الفقرة الموسوم معلومات صريحة عن الخط واللون والنمط.

1. إنشاء Tagged PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ عنصر فقرة وقم بتكوين حالة نص الهيكل الخاص به.
1. قم بضبط نص الفقرة واحفظ المستند.

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

## إضافة عناصر بنية الشكل

يوضح هذا المثال كيفية إنشاء شكل مُوسَّم بنص بديل، عنوان، وسم مخصص، محتوى صورة، وتحديد الموقع.

1. إنشاء Tagged PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [FigureElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/figureelement/), اضبط البيانات الوصفية القابلة للوصول لها، وقم بتعيين الصورة.
1. قم بتعديل موضع الشكل واحفظ المستند.

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

## تحقق من صحة PDF معلم لـ PDF/UA

استخدم هذا المثال عندما تحتاج إلى التحقق مما إذا كان ملف PDF الموسوم يفي بقواعد التحقق من صحة PDF/UA.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تشغيل التحقق من الصحة ضد [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).`PDF_UA_1`.
1. اكتب سجل التحقق واطبع نتيجة التحقق.

```java
public static void validateTaggedPdf(Path inputFile, Path logFile) {
    try (Document document = new Document(inputFile.toString())) {
        boolean isValid = document.validate(logFile.toString(), PdfFormat.PDF_UA_1);
        System.out.println("Is Valid: " + isValid);
    }
}
```

## ضبط موضع عنصر البنية

هذا المثال يطبق إعدادات هوامش ومحاذاة صريحة على فقرة موسومة.

1. إنشاء Tagged PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف عنصر بنية الفقرة وقم بالتحضير [PositionSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure/positionsettings/).
1. طبق إعدادات الموضع على الفقرة واحفظ المستند.

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

## تحويل ملف PDF موجود إلى PDF/UA مع وسم تلقائي

استخدم هذا النهج عندما يجب تحويل ملف PDF موجود إلى PDF/UA وتوسيمه تلقائيًا أثناء التحويل.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) وتمكين الوسم التلقائي.
1. تشغيل التحويل وحفظ المستند الناتج.

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

## إنشاء PDF معلم يحتوي على حقل نموذج قابل للوصول

يُعليم هذا المثال حقل توقيع النموذج بحيث يصبح جزءًا من شجرة الهيكل المنطقي.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وَأضف صفحةً تحتوي على حقل نموذج.
1. أضف حقل النموذج إلى مجموعة نماذج المستند.
1. إنشاء عنصر بنية نموذج معلم، وربطه بالحقل، ثم حفظ المستند.

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

## إنشاء Tagged PDF مع صفحة TOC

استخدم هذا المثال عندما يجب أن يتضمن ملف PDF موسوم صفحة فهرس أساسية مرتبطة بعناوين المستند.

1. إنشاء Tagged PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة TOC.
1. إنشاء [TOCElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/tocelement/) و عنوان يجب أن يظهر في TOC.
1. اربط عنصر TOC بالعنوان واحفظ المستند.

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

## إنشاء PDF مُوسَّم متقدم مع صفحة TOC

يبني هذا المثال جدول محتويات (TOC) موسومًا أكثر تعقيدًا مع عناوين صفحات مرتبطة، وعناصر قائمة متداخلة، ومستويات عناوين متعددة.

1. إنشاء Tagged PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وإعداد صفحة TOC بعنوان مرئي.
1. إنشاء بنية TOC، وربط عنوان TOC والمدخلات بالعناوين وعناصر القائمة، وإضافة عناصر المحتوى ذات الصلة.
1. احفظ المستند النهائي مع بنية TOC المتقدمة.

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
