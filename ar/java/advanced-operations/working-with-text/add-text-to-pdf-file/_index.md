---
title: إضافة نص إلى PDF في Java
linktitle: إضافة نص إلى PDF
type: docs
weight: 10
url: /ar/java/add-text-to-pdf-file/
description: تعلم كيفية إضافة النص، مقاطع HTML، القوائم، الروابط، والخطوط المخصصة إلى مستندات PDF في Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف النص، الروابط، HTML، والخطوط إلى ملفات PDF باستخدام Java.
Abstract: تشرح هذه المقالة كيفية إضافة النص وتنسيقه في مستندات PDF باستخدام Aspose.PDF for Java. تغطي الإدراج البسيط للنص، تخطيط الفقرات، الروابط التشعبية، النص من اليمين إلى اليسار، تنسيق الخطوط، الشفافية، الحدود، أجزاء HTML و LaTeX، النص المتدرج، والخطوط المخصصة المحملة من الملفات أو التدفقات.
---
Aspose.PDF for Java يدعم إدراج النص العادي، وتخطيط متقدم، وتنسيق، وتدرجات لونية، وHTML، وLaTeX، وخطوط مخصصة.

## أضف مقطع نصي بسيط

استخدم هذا المثال عندما يجب وضع سلسلة نصية قصيرة عند إحداثيات صفحة ثابتة.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. إنشاء `TextFragment` وحدد موقعه.
1. أضفه إلى الصفحة واحفظ المستند.

```java
public static void addTextSimpleCase(Path outputFile) {
      try (Document document = new Document()) {
          Page page = document.getPages().add();

          TextFragment textFragment = new TextFragment("Hello, Aspose!");
          textFragment.setPosition(new Position(100, 600));

          page.getParagraphs().add(textFragment);
          document.save(outputFile.toString());
      }
  }
```

## أضف فقرة داخل مستطيل

استخدم هذا المثال عندما يجب تدفق كتلة نص أكبر داخل منطقة محدودة.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. حمِّل النص المصدر وقم بتكوين `TextParagraph` المستطيل ووضع التغليف.
1. إلحاق الجزء عبر `TextBuilder` واحفظ ملف PDF.

```java
public static void addParagraph(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String text = Files.exists(loremPath)
                ? Files.readString(loremPath)
                : "Lorem ipsum sample text not found.";

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setFirstLineIndent(20);
        paragraph.setRectangle(new Rectangle(80, 800, 400, 200, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.DiscretionaryHyphenation);

        TextFragment fragment = new TextFragment(text);
        fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        fragment.getTextState().setFontSize(12);

        paragraph.appendLine(fragment);
        builder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## إضافة فقرات بإعدادات إزاحة مختلفة

استخدم هذا المثال عندما يجب أن تستخدم السطر الأول والسطر التالي قواعد شد مختلف للمسافات البادئة.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. قم بإعداد الجزء النصي المشترك وإنشاء عدة `TextParagraph` كائنات.
1. قم بتكوين المسافة البادئة لكل فقرة، أضفها، واحفظ المستند.

```java
public static void addParagraphsIndents(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String text = Files.exists(loremPath)
                ? Files.readString(loremPath)
                : "Lorem ipsum sample text not found.";

        TextFragment fragment = new TextFragment(text);
        fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        fragment.getTextState().setFontSize(12);

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph1 = new TextParagraph();
        paragraph1.setFirstLineIndent(20);
        paragraph1.setRectangle(new Rectangle(80, 800, 300, 50, true));
        paragraph1.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
        paragraph1.appendLine(fragment);
        builder.appendParagraph(paragraph1);

        TextParagraph paragraph2 = new TextParagraph();
        paragraph2.setSubsequentLinesIndent(20);
        paragraph2.setRectangle(new Rectangle(320, 800, 500, 50, true));
        paragraph2.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
        paragraph2.appendLine(fragment);
        builder.appendParagraph(paragraph2);

        document.save(outputFile.toString());
    }
}
```

## إدراج نص مع فاصل سطر يدوي

استخدم هذا المثال عندما يجب أن يحتوي مقطع نصي واحد على سطر جديد صريح.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. إنشاء `TextFragment` يتضمن فاصل سطر وتكوين نمطه.
1. أضفه من خلال `TextParagraph` واحفظ ملف PDF.

```java
public static void addNewLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());

        TextParagraph paragraph = new TextParagraph();
        paragraph.appendLine(textFragment);
        paragraph.setPosition(new Position(100, 600));

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## فحص فواصل الأسطر المكتشفة

استخدم هذا المثال عندما تحتاج إلى مراجعة إخراج الإشعار المتعلق بتخطيط النص وتغليف السطر.

1. إنشاء مستند PDF جديد وتفعيل تسجيل الإشعارات.
1. أضف عدة مقاطع نصية طويلة إلى الصفحة.
1. افحص الإشعارات واحفظ المستند.

```java
public static void determineLineBreak(Path outputFile) {
    try (Document document = new Document()) {
        document.setEnableNotificationLogging(true);

        Page page = document.getPages().add();
        for (int i = 0; i < 4; i++) {
            TextFragment text = new TextFragment(
                    "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
                            + "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                            + "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
                            + "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
                            + "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
                            + "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
                            + "culpa qui officia deserunt mollit anim id est laborum.");
            text.getTextState().setFontSize(20);
            page.getParagraphs().add(text);
        }

        System.out.println(document.getPages().get_Item(1).getNotifications());
        document.save(outputFile.toString());
    }
}
```

## قياس عرض النص ديناميكيًا

استخدم هذا المثال عندما يجب قياس عرض الأحرف والسلاسل قبل اتخاذ قرارات التخطيط.

1. تحديد الخط المستهدف وإنشاء `TextState`.
1. قِس الأحرف وقارن النتائج من واجهات برمجة تطبيقات الخط وحالة النص.
1. أخرج أي عدم تطابق للتحقق.

```java
public static void getTextWidthDynamically(Path outputFile) {
    Font font = FontRepository.findFont("Arial");
    TextState textState = new TextState();
    textState.setFont(font);
    textState.setFontSize(14);

    if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001) {
        System.out.println("Unexpected font string measure!");
    }

    if (Math.abs(textState.measureString("z") - 7.0) > 0.001) {
        System.out.println("Unexpected font string measure!");
    }

    for (char c = 'A'; c <= 'z'; c++) {
        double fontMeasure = font.measureString(String.valueOf(c), 14);
        double textStateMeasure = textState.measureString(String.valueOf(c));
        if (Math.abs(fontMeasure - textStateMeasure) > 0.001) {
            System.out.println("Font and state string measuring doesn't match!");
        }
    }
}
```

## إضافة نص مع جزء رابط تشعبي

استخدم هذا المثال عندما يجب أن يعمل جزء من مقطع النص كرابط ويب.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. ابنِ `TextFragment` مع عدة `TextSegment` كائنات.
1. عيّن ارتباطًا تشعبيًا ونمطًا للجزء المستهدف، ثم احفظ المستند.

```java
public static void addTextWithHyperlink(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment = new TextFragment("Sample Text Fragment");
        fragment.getSegments().add(new TextSegment(" ... Text Segment 1..."));

        TextSegment segment = new TextSegment("Link to Aspose");
        fragment.getSegments().add(segment);
        segment.setHyperlink(new WebHyperlink("https://products.aspose.com/pdf"));
        segment.getTextState().setForegroundColor(Color.getBlue());
        segment.getTextState().setFontStyle(FontStyles.Italic);

        fragment.getSegments().add(new TextSegment("TextSegment without hyperlink"));

        page.getParagraphs().add(fragment);
        document.save(outputFile.toString());
    }
}
```

## إضافة نص من اليمين إلى اليسار

استخدم هذا المثال عندما يجب على المستند عرض محتوى نصي من اليمين إلى اليسار مع محاذاة صحيحة.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. إنشاء `TextFragment` مع النص RTL المستهدف وقم بتكوين الخط والمحاذاة الخاصة به.
1. أضفه إلى الصفحة واحفظ ملف PDF.

```java
public static void addTextWithRtlText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment(
                "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية.");
        textFragment.getTextState().setFont(FontRepository.findFont("Tahoma"));
        textFragment.getTextState().setFontSize(14);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.setHorizontalAlignment(HorizontalAlignment.Right);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## إضافة نص منسق ومقاطع شبيهة بالمعادلات

استخدم هذا المثال عندما يجب أن يستخدم النص العادي والجزء المكتوب كمنخفض (subscript) حالات نصية مختلفة في مخرج واحد.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. ابنِ الجزء المشكَّل الرئيسي وقم بتكوين الصيغة باستخدام الأقسام المساعدة.
1. أضف كلا الجزأين إلى الصفحة واحفظ المستند.

```java
public static void addTextWithFontStyling(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment formula = new TextFragment();
        TextFragment textFragment = new TextFragment("Hello, Aspose!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textFragment.getTextState().setUnderline(true);
        textFragment.setHorizontalAlignment(HorizontalAlignment.Left);

        TextState textStateLetters = new TextState();
        textStateLetters.setFont(FontRepository.findFont("Arial"));
        textStateLetters.setFontSize(14);
        textStateLetters.setForegroundColor(Color.getBlue());
        textStateLetters.setFontStyle(FontStyles.Bold);

        TextState textStateIndex = new TextState();
        textStateIndex.setFont(FontRepository.findFont("Arial"));
        textStateIndex.setFontSize(14);
        textStateIndex.setForegroundColor(Color.getDarkRed());
        textStateIndex.setSubscript(true);

        Position position = new Position(100, 500);
        addSegment(formula, "S = a", textStateLetters, position);
        addSegment(formula, "2n", textStateIndex, position);
        addSegment(formula, " + a", textStateLetters, position);
        addSegment(formula, "2n+1", textStateIndex, position);
        addSegment(formula, " + a", textStateLetters, position);
        addSegment(formula, "2n+2", textStateIndex, position);
        formula.setHorizontalAlignment(HorizontalAlignment.Left);

        page.getParagraphs().add(textFragment);
        page.getParagraphs().add(formula);
        document.save(outputFile.toString());
    }
}

private static void addSegment(TextFragment formula, String text, TextState state, Position position) {
    TextSegment segment = new TextSegment(text);
    segment.setTextState(state);
    segment.setPosition(position);
    formula.getSegments().add(segment);
}
```

## أضف نصًا تحته خط

استخدم هذا المثال عندما يجب أن يستخدم جزء النص أسلوب التسطير الظاهر.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. إنشاء قطعة النص، ضبط الخط وحالة التسطير، وتحديد موضعها.
1. أضفه إلى `TextBuilder` واحفظ النتيجة.

```java
public static void addUnderlineText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        TextBuilder textBuilder = new TextBuilder(page);

        TextFragment fragment = new TextFragment("Hello, ASPOSE.PDF!");
        fragment.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment.getTextState().setFontSize(10);
        fragment.getTextState().setUnderline(true);
        fragment.setPosition(new Position(10, 800));
        textBuilder.appendText(fragment);

        document.save(outputFile.toString());
    }
}
```

## أضف نصًا شفافًا فوق شكل ملون

استخدم هذا المثال عندما يجب أن يظهر النص بشفافية فوق رسم خلفية.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. ارسم شكل الخلفية وأنشئ قطعة نصية شبه شفافة.
1. أضف العنصرين إلى الصفحة واحفظ المستند.

```java
public static void addTextTransparent(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        com.aspose.pdf.drawing.Graph canvas = new com.aspose.pdf.drawing.Graph(100.0, 400.0);
        com.aspose.pdf.drawing.Rectangle rectangle = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
        rectangle.getGraphInfo().setFillColor(Color.fromArgb(128, 0xC5, 0xB5, 0xFF));
        canvas.getShapes().addItem(rectangle);
        canvas.setChangePosition(false);
        page.getParagraphs().add(canvas);

        TextFragment text = new TextFragment(
                "This is the transparent text. This is the transparent text. This is the transparent text.");
        text.getTextState().setForegroundColor(Color.fromArgb(30, 0, 255, 0));
        page.getParagraphs().add(text);

        document.save(outputFile.toString());
    }
}
```

## إضافة نص غير مرئي

استخدم هذا المثال عندما يجب أن يكون النص القابل للبحث أو المخفي موجودًا دون عرض مرئي.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. أضف قطعة نصية مرئية وقطعة ثانية مع تمكين العلامة غير المرئية.
1. احفظ المستند.

```java
public static void addTextInvisible(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment text1 = new TextFragment(
            "This is the visible text. This is the visible text. This is the visible text.");
        page.getParagraphs().add(text1);

        TextFragment text2 = new TextFragment(
            "This is the invisible text. This is the invisible text. This is the invisible text.");
        text2.getTextState().setInvisible(true);
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```

## إضافة نص مع حد مستطيل

استخدم هذا المثال عندما يجب رسم النص مع المستطيل المحيط به.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. إنشاء مُنسق `TextFragment` وتمكين رسم حدود مستطيل النص.
1. أضفه إلى `TextBuilder` واحفظ ملف PDF.

```java
public static void addTextBorder(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is sample text with border.");
        textFragment.setPosition(new Position(10, 700));
        textFragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());
        textFragment.getTextState().setStrokingColor(Color.getDarkRed());
        textFragment.getTextState().setDrawTextRectangleBorder(true);

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```

## إضافة نص مشطوب

استخدم هذا المثال عندما يجب أن يُظهر النص تنسيق الخط المشطوب.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. إنشاء جزء نص منسق مع تمكين الخط المشطوب.
1. أضفه إلى الصفحة واحفظ المستند.

```java
public static void addStrikeoutText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is sample strikeout text.");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());
        textFragment.getTextState().setStrikeOut(true);
        textFragment.getTextState().setFontStyle(FontStyles.Bold);
        textFragment.setPosition(new Position(100, 600));

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```

## تطبيق تظليل تدرج محوري على النص

استخدم هذا المثال عندما يجب أن يستخدم النص تعبئة متدرجة خطية بدلاً من لون صلب.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. أنشئ جزء النص وعيّن تدرجًا محوريًا على لون المقدمة.
1. أضفه إلى الصفحة واحفظ ملف PDF.

```java
public static void applyGradientAxialShadingToText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("PDF TITLE");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(36);
        textFragment.getTextState().setFont(FontRepository.findFont("Arial Bold"));
        textFragment.getTextState().setForegroundColor(new Color());
        textFragment.getTextState().getForegroundColor()
                .setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));
        textFragment.getTextState().setUnderline(true);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## تطبيق تظليل تدريجي دائري على النص

استخدم هذا المثال عندما يجب أن يستخدم النص تعبئة تدرج شعاعي.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. أنشئ جزء النص وعيّن تدرجًا دائريًا للون المقدمة الخاص به.
1. أضفه إلى الصفحة واحفظ المستند.

```java
public static void applyGradientRadialShadingToText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("PDF TITLE");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(36);
        textFragment.getTextState().setFont(FontRepository.findFont("Arial Bold"));
        textFragment.getTextState().setForegroundColor(new Color());
        textFragment.getTextState().getForegroundColor()
                .setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));
        textFragment.getTextState().setUnderline(true);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## إضافة نص منسق بنمط HTML مضمّن

استخدم هذا المثال عندما يجب إدراج تنسيق النص الفوقي والنص السفلي من خلال ترميز HTML.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. إنشاء `HtmlFragment` مع العلامات المضمنة المطلوبة.
1. أضفه إلى الصفحة واحفظ ملف PDF.

```java
public static void addTextHtmlFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        HtmlFragment textFragment = new HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>");
        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## إضافة مقطع نص LaTeX

استخدم هذا المثال عندما يجب عرض المحتوى الرياضي أو المنسق بصيغة TeX داخل ملف PDF.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. إنشاء `TeXFragment` مع التعبير المطلوب.
1. أضفه إلى الصفحة واحفظ المستند.

```java
public static void addTextLatexFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TeXFragment textFragment = new TeXFragment(
                "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42");
        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## أضف مقطع HTML غني

استخدم هذا المثال عندما يجب أن تعرض الصفحة محتوى HTML منظم مثل العناوين والفقرات والروابط.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. قم بإعداد سلسلة محتوى HTML وإنشاء `HtmlFragment`.
1. أضفه إلى الصفحة واحفظ ملف PDF.

```java
public static void addHtmlFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlContent = """
                <h1 style='color:blue;'>Hello, Aspose!</h1>
                <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
                <p style='color:green;'>This paragraph is green.</p>
                <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
                """;
        HtmlFragment htmlFragment = new HtmlFragment(htmlContent);
        page.getParagraphs().add(htmlFragment);
        document.save(outputFile.toString());
    }
}
```

## أضف مقطع HTML مع حالة نص متجاوزة

استخدم هذا المثال عندما يجب أن يرث محتوى HTML المستورد إعداد خط ولون مُتحكم به.

1. إنشاء مستند PDF جديد وإضافة صفحة.
1. قم بإعداد محتوى HTML وإنشاء `HtmlFragment`.
1. تعيين مخصص `TextState`, أضف الجزء، واحفظ المستند.

```java
public static void addHtmlFragmentOverrideTextState(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlContent = """
                <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
                <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
                <p style='color:green;'>This paragraph is green.</p>
                <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
                """;
        HtmlFragment htmlFragment = new HtmlFragment(htmlContent);
        TextState textState = new TextState();
        textState.setFont(FontRepository.findFont("Arial"));
        textState.setFontSize(14);
        textState.setForegroundColor(Color.getRed());
        htmlFragment.setTextState(textState);

        page.getParagraphs().add(htmlFragment);
        document.save(outputFile.toString());
    }
}
```

## استخدم خطًا مخصصًا تم تحميله من ملف

استخدم هذا المثال عندما يجب أن يستخدم النص خطًا يتم تحميله مباشرةً من مسار ملف الخط.

1. حل مسار ملف الخط المخصَّص.
1. إنشاء جزء نصي وتحميل الخط عبر `FontRepository.openFont`.
1. طبق إعدادات Font واحفظ المستند.

```java
public static void useCustomFontFromFile(Path outputFile) {
    Path fontPath = fontDir.resolve("BriosoPro Italic.otf");
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment = new TextFragment("Hello, Aspose!");
        fragment.setPosition(new Position(100, 600));
        fragment.getTextState().setFont(FontRepository.openFont(fontPath.toString()));
        fragment.getTextState().setFontSize(24);
        fragment.getTextState().setForegroundColor(Color.getBlue());
        fragment.getTextState().setFontStyle(FontStyles.Italic);

        page.getParagraphs().add(fragment);
        document.save(outputFile.toString());
    }
}
```

## استخدم خطًا مخصصًا تم تحميله من تدفق

استخدم هذا المثال عندما يجب فتح خط مخصص من تدفق وإدراجه في ملف PDF.

1. افتح ملف الخط كتيار وقم بتحميله باستخدام `FontRepository`.
1. إنشاء مقطع النص وتعيين الخط المضمن.
1. أضف الشريحة إلى الصفحة واحفظ المستند.

```java
public static void useCustomFontFromStream(Path outputFile) throws Exception {
    Path fontPath = fontDir.resolve("BriosoPro Italic.otf");
    try (InputStream fontStream = Files.newInputStream(fontPath)) {
        Font font = FontRepository.openFont(fontStream, FontTypes.OTF);
        font.setEmbedded(true);

        try (Document document = new Document()) {
            Page page = document.getPages().add();

            TextFragment fragment = new TextFragment("Hello, Aspose!");
            fragment.setPosition(new Position(100, 600));
            fragment.getTextState().setFont(font);
            fragment.getTextState().setFontSize(14);
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setFontStyle(FontStyles.Italic);

            page.getParagraphs().add(fragment);
            document.save(outputFile.toString());
        }
    }
}
```
