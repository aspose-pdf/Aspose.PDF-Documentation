---
title: تنسيق نص PDF في Java
linktitle: تنسيق النص داخل PDF
type: docs
weight: 70
url: /ar/java/text-formatting-inside-pdf/
description: تعرَّف على كيفية تنسيق النص داخل مستندات PDF باستخدام Java عبر التحكم بالمسافات، الملاحظات، القوائم، التخطيط متعدد الأعمدة، وخيارات التنسيق.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قُم بتنسيق النص وتطبيق الأنماط داخل ملفات PDF باستخدام Java
Abstract: يوضح هذا المقال كيفية تنسيق النص في مستندات PDF باستخدام Aspose.PDF for Java. يغطي التباعد بين الأسطر، والتباعد بين الأحرف، والقوائم النقطية والمرقمة، والحواشي السفلية والحواشي النهائية، ومحتوى الفقرة المضمن، وتخطيط متعدد الأعمدة، وفواصل الصفحات القسرية، وإيقافات تبويب مخصصة.
---
يقدم Aspose.PDF for Java أدوات التحكم في تنسيق النص للمسافات والقوائم والملاحظات وتخطيط مدمج وتكوين متعدد الأعمدة.

## ضبط تباعد السطر البسيط

استخدم هذا المثال عندما يجب أن يستخدم نص الفقرة قيمة تباعد سطر ثابت.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. حمّل أو جهّز النص المصدر وأنشئ `TextFragment`.
1. عيّن تباعد الأسطر، أضف الجزء إلى الصفحة، واحفظ المستند.

```java
public static void specifyLineSpacingSimpleCase(Path outputFile) throws Exception {
        try (Document document = new Document()) {
            Page page = document.getPages().add();

            Path loremPath = dataDir.resolve("lorem.txt");
            String text = Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum text not found.";

            TextFragment textFragment = new TextFragment(text);
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setLineSpacing(16);
            page.getParagraphs().add(textFragment);

            document.save(outputFile.toString());
        }
    }
```

## قارن أوضاع تباعد الأسطر باستخدام خط مخصص

استخدم هذا المثال عندما يجب اختبار تباعد الأسطر بأوضاع تنسيق مختلفة لنفس الخط.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. حمّل الخط المخصص وحضّر مقطعين بوضعيات تباعد سطور مختلفة.
1. أضف كلا الجزأين إلى الصفحة واحفظ ملف PDF..

```java
public static void specifyLineSpacingSpecificCase(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Path fontFile = dataDir.resolve("HPSimplified.ttf");
        Path loremPath = dataDir.resolve("lorem.txt");
        String text = Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum text not found.";

        try (InputStream fontStream = Files.newInputStream(fontFile)) {
            Font font = FontRepository.openFont(fontStream, FontTypes.TTF);

            TextFragment fragment1 = new TextFragment(text);
            fragment1.getTextState().setFont(font);
            fragment1.getTextState().setFormattingOptions(new TextFormattingOptions());
            fragment1.getTextState().getFormattingOptions().setLineSpacing(TextFormattingOptions.LineSpacingMode.FontSize);
            page.getParagraphs().add(fragment1);

            TextFragment fragment2 = new TextFragment(text);
            fragment2.getTextState().setFont(font);
            fragment2.getTextState().setFormattingOptions(new TextFormattingOptions());
            fragment2.getTextState().getFormattingOptions().setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);
            page.getParagraphs().add(fragment2);
        }

        document.save(outputFile.toString());
    }
}
```

## ضبط تباعد الأحرف باستخدام مقاطع النص

استخدم هذا المثال عندما يجب عرض نفس النص بقيم تباعد أحرف مختلفة.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. أنشئ مقاطع نصية باستخدام طريقة المساعدة لعدة قيم تباعد.
1. أضف القطع إلى الصفحة واحفظ المستند.

```java
public static void characterSpacingUsingTextFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.getParagraphs().add(makeCharacterSpacingFragment(2.0f));
        page.getParagraphs().add(makeCharacterSpacingFragment(1.0f));
        page.getParagraphs().add(makeCharacterSpacingFragment(0.75f));

        document.save(outputFile.toString());
    }
}

private static TextFragment makeCharacterSpacingFragment(float spacing) {
    TextFragment fragment = new TextFragment("Sample Text with character spacing");
    fragment.getTextState().setFont(FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize(14);
    fragment.getTextState().setCharacterSpacing(spacing);
    return fragment;
}
```

## تعيين تباعد الأحرف داخل فقرة نصية

استخدم هذا المثال عندما يجب تطبيق تباعد الأحرف داخل فقرة نصية محصورة.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. أنشئ `TextParagraph` مع مستطيل هدف وخيارات الالتفاف.
1. ألحق مقطع النص المنسق واحفظ ملف PDF..

```java
public static void characterSpacingUsingTextParagraph(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(100, 700, 500, 750, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        TextFragment fragment = new TextFragment("Sample Text with character spacing");
        fragment.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment.getTextState().setFontSize(14);
        fragment.getTextState().setCharacterSpacing(2.0f);

        paragraph.appendLine(fragment);
        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## إنشاء قائمة نقطية باستخدام HTML

استخدم هذا المثال عندما ينبغي إنشاء تنسيق القوائم غير المرتبة من علامات HTML.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. أنشئ سلسلة قائمة HTML..
1. أضفه كـ `HtmlFragment` واحفظ المستند.

```java
public static void createBulletListHtmlVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlList = "<ul><li>First item in the list</li>"
                + "<li>Second item with more text to demonstrate wrapping behavior.</li>"
                + "<li>Third item</li><li>Fourth item</li></ul>";
        page.getParagraphs().add(new HtmlFragment(htmlList));
        document.save(outputFile.toString());
    }
}
```

## إنشاء قائمة مرقمة باستخدام HTML

استخدم هذا المثال عندما يجب إنشاء تنسيق قائمة مرتبة من الترميز HTML.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. أنشئ سلسلة قائمة HTML المرتبة.
1. أضفه كـ `HtmlFragment` واحفظ المستند.

```java
public static void createNumberedListHtmlVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlList = "<ol><li>First item in the list</li>"
                + "<li>Second item with more text to demonstrate wrapping behavior.</li>"
                + "<li>Third item</li><li>Fourth item</li></ol>";
        page.getParagraphs().add(new HtmlFragment(htmlList));
        document.save(outputFile.toString());
    }
}
```

## إنشاء قائمة نقطية باستخدام LaTeX

استخدم هذا المثال عندما يجب عرض تنسيق القائمة غير المرتبة من ترميز TeX.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. اضبط سلسلة قائمة TeX باستخدام `itemize` بيئة.
1. أضفه كـ `TeXFragment` واحفظ ملف PDF..

```java
public static void createBulletListLatexVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String texList = "Lists are easy to create: \\begin{itemize}"
                + "\\item First item"
                + "\\item Second item with more text to demonstrate wrapping behavior."
                + "\\item Third item"
                + "\\item Fourth item"
                + "\\end{itemize}";
        page.getParagraphs().add(new TeXFragment(texList));
        document.save(outputFile.toString());
    }
}
```

## إنشاء قائمة مرقمة باستخدام LaTeX

استخدم هذا المثال عندما يجب عرض تنسيق القائمة المرتبة من ترميز TeX.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. اضبط سلسلة قائمة TeX باستخدام `enumerate` بيئة.
1. أضفه كـ `TeXFragment` واحفظ ملف PDF..

```java
public static void createNumberedListLatexVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String texList = "Lists are easy to create: \\begin{enumerate}"
                + "\\item First item"
                + "\\item Second item with more text to demonstrate wrapping behavior."
                + "\\item Third item"
                + "\\item Fourth item"
                + "\\end{enumerate}";
        page.getParagraphs().add(new TeXFragment(texList));
        document.save(outputFile.toString());
    }
}
```

## إنشاء قائمة نقطية مع فقرات نصية

استخدم هذا المثال عندما يجب بناء قائمة نقطية يدوية من مقاطع نصية عادية.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. ابنِ `TextParagraph` وإلحاق مقاطع مسبوقة بنقطة.
1. أضف الفقرة إلى الصفحة واحفظ المستند.

```java
public static void createBulletList(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String[] items = {
                "First item in the list",
                "Second item with more text to demonstrate wrapping behavior.",
                "Third item",
                "Fourth item"
        };

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(80, 200, 400, 800, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        for (String item : items) {
            TextFragment fragment = new TextFragment("- " + item);
            fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
            fragment.getTextState().setFontSize(12);
            paragraph.appendLine(fragment);
        }

        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## إنشاء قائمة مرقمة مع فقرات نصية

استخدم هذا المثال عندما يجب إنشاء قائمة مرقمة يدوية من مقاطع نصية عادية.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. ابنِ `TextParagraph` وألْحِق مقاطع مرقمة.
1. أضف الفقرة إلى الصفحة واحفظ المستند.

```java
public static void createNumberedList(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String[] items = {
                "First item in the list",
                "Second item with more text to demonstrate wrapping behavior.",
                "Third item",
                "Fourth item"
        };

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(80, 200, 400, 800, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        for (int i = 0; i < items.length; i++) {
            TextFragment fragment = new TextFragment((i + 1) + ". " + items[i]);
            fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
            fragment.getTextState().setFontSize(12);
            paragraph.appendLine(fragment);
        }

        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## إضافة حاشية أساسية

استخدم هذا المثال عندما يجب أن يشير مقطع النص إلى حاشية بسيطة.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. أنشئ مقطع النص الرئيسي وعيّن `Note` كحاشية سفلية.
1. أضف أي نص متابعة مضمّن واحفظ المستند.

```java
public static void addFootnote(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setFootNote(new Note("This is the footnote content."));
        page.getParagraphs().add(textFragment);

        TextFragment inlineText = new TextFragment(" This is another text after footnote in the same paragraph.");
        inlineText.setInLineParagraph(true);
        inlineText.getTextState().setFont(FontRepository.findFont("Arial"));
        inlineText.getTextState().setFontSize(14);
        page.getParagraphs().add(inlineText);

        document.save(outputFile.toString());
    }
}
```

## إضافة حاشية سفلية بنمط نص مخصص

استخدم هذا المثال عندما يجب أن يستخدم محتوى الحاشية خطه وحجمه وإعدادات لونه الخاصة.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. أنشئ جزء النص الرئيسي واضبط ملاحظة حاشية سفلية مُنسَّقة.
1. أرفق الملاحظة واحفظ ملف PDF..

```java
public static void addFootnoteCustomTextStyle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);

        Note note = new Note("This is the footnote content with custom text style.");
        TextState noteTextState = new TextState();
        noteTextState.setFont(FontRepository.findFont("Times New Roman"));
        noteTextState.setFontSize(10);
        noteTextState.setForegroundColor(Color.getRed());
        noteTextState.setFontStyle(FontStyles.Italic);
        note.setTextState(noteTextState);
        textFragment.setFootNote(note);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## إضافة حاشية سفلية بنص علامة مخصص

استخدم هذا المثال عندما يجب استبدال علامة الهوامش الظاهرة بنص مخصص.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. عيّن الحاشية إلى الجزء النصي الرئيسي وتجاوز نص العلامة الخاص بها.
1. أضف المحتوى المتبقي واحفظ المستند.

```java
public static void addFootnoteCustomText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setFootNote(new Note("This is the footnote content."));
        textFragment.getFootNote().setText("***");
        page.getParagraphs().add(textFragment);

        TextFragment anotherText = new TextFragment(" This is another text without footnote.");
        anotherText.getTextState().setFont(FontRepository.findFont("Arial"));
        anotherText.getTextState().setFontSize(14);
        page.getParagraphs().add(anotherText);

        document.save(outputFile.toString());
    }
}
```

## تخصيص خط فاصل الحاشية

استخدم هذا المثال عندما يجب تنسيق الخط الفاصل بين الحواشي ومحتوى الصفحة بشكل صريح.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. اضبط نمط خط ملاحظة الصفحة عبر `GraphInfo`.
1. أضف مقاطع نصية مع الحواشي واحفظ المستند.

```java
public static void addFootnoteWithCustomLineStyle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        GraphInfo graphInfo = new GraphInfo();
        graphInfo.setLineWidth(2);
        graphInfo.setColor(Color.getRed());
        graphInfo.setDashArray(new int[] {3});
        graphInfo.setDashPhase(1);
        page.setNoteLineStyle(graphInfo);

        TextFragment text1 = new TextFragment("This is a sample text with a footnote.");
        text1.setFootNote(new Note("foot note for text 1"));
        page.getParagraphs().add(text1);

        TextFragment text2 = new TextFragment("This is yet another sample text with a footnote.");
        text2.setFootNote(new Note("foot note for text 2"));
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```

## إضافة حاشية سفلية تحتوي على صورة ومحتوى جدول

استخدم هذا المثال عندما يجب أن يحتوي الهامش نفسه على محتوى غني مثل الصور والنص والجداول.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. ابنِ كائن `Note` يحتوي على صورة، نص مدمج، وجدول.
1. أرفقه إلى الجزء النصي الرئيسي واحفظ المستند.

```java
public static void addFootnoteWithImageAndTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment text = new TextFragment("This is a sample text with a footnote.");
        page.getParagraphs().add(text);

        Note note = new Note();

        Image imageNote = new Image();
        imageNote.setFile(dataDir.resolve("logo.jpg").toString());
        imageNote.setFixHeight(20);
        imageNote.setFixWidth(20);
        note.getParagraphs().add(imageNote);

        TextFragment textNote = new TextFragment("This is the footnote content.");
        textNote.getTextState().setFontSize(20);
        textNote.setInLineParagraph(true);
        note.getParagraphs().add(textNote);

        Table table = new Table();
        table.getRows().add().getCells().add("Cell 1,1");
        table.getRows().add().getCells().add("Cell 1,2");
        note.getParagraphs().add(table);

        text.setFootNote(note);
        document.save(outputFile.toString());
    }
}
```

## إضافة حاشية سفلية

استخدم هذا المثال عندما يجب أن يشير جزء النص إلى محتوى الحاشية النهائية بدلاً من حاشية الصفحة.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. عيّن حاشية سفلية لقطعة النص الرئيسية وأضف نصًا داعمًا للجسم.
1. احفظ المستند مع محتوى الحاشية السفلية المُنشأة.

```java
public static void addEndnote(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with an endnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setEndNote(new Note("This is the EndNote content."));
        page.getParagraphs().add(textFragment);

        String textContent = loremText();
        for (int i = 0; i < 5; i++) {
            TextFragment text = new TextFragment(textContent);
            text.getTextState().setFont(FontRepository.findFont("Arial"));
            text.getTextState().setFontSize(14);
            page.getParagraphs().add(text);
        }

        document.save(outputFile.toString());
    }
}

private static String loremText() throws Exception {
    Path loremPath = dataDir.resolve("lorem.txt");
    return Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum sample text not found.";
}
```

## إضافة حاشية سفلية بنص علامة مخصص

استخدم هذا المثال عندما يتعين على علامة الهوامش النهائية استخدام تسمية مرئية مخصصة.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. عيّن حاشية سفلية لجزء النص الرئيسي وتجاوز نص العلامة.
1. أضف النص المتبقي للمستند واحفظ ملف PDF..

```java
public static void addEndnoteCustomText(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with an endnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setEndNote(new Note("This is the EndNote content."));
        textFragment.getEndNote().setText("***");
        page.getParagraphs().add(textFragment);

        String textContent = loremText();
        for (int i = 0; i < 5; i++) {
            TextFragment text = new TextFragment(textContent);
            text.getTextState().setFont(FontRepository.findFont("Arial"));
            text.getTextState().setFontSize(14);
            page.getParagraphs().add(text);
        }

        document.save(outputFile.toString());
    }
}
```

## إجبار محتوى الجدول على صفحة جديدة

استخدم هذا المثال عندما يجب أن يبدأ المحتوى المنسق صراحةً في صفحة جديدة.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. أنشئ جدولًا واملأ صفوفه.
1. اجعل الجدول يبدأ في صفحة جديدة واحفظ المستند.

```java
public static void forceNewPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Table table = new Table();
        table.setColumnWidths("150 150 150");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All));

        for (int i = 0; i < 5; i++) {
            Row row = table.getRows().add();
            row.getCells().add("Row " + (i + 1) + " - Col 1");
            row.getCells().add("Row " + (i + 1) + " - Col 2");
            row.getCells().add("Row " + (i + 1) + " - Col 3");
        }

        table.setInNewPage(true);
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## دمج المحتوى المضمن داخل تدفق فقرة واحدة

استخدم هذا المثال عندما يجب أن تستمر النصوص والصور داخل تدفق الفقرة نفسه.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. أضف قطعة النص الأولى، ثم صورة مضمنة، ثم قطعة نص مضمنة أخرى.
1. أضف أي فقرة مستقلة تالية واحفظ المستند.

```java
public static void usingInlineParagraphProperty(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment1 = new TextFragment("This is the first part of the paragraph. ");
        fragment1.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment1.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment1);

        Image image = new Image();
        image.setInLineParagraph(true);
        image.setFile(dataDir.resolve("logo.jpg").toString());
        image.setFixHeight(30);
        image.setFixWidth(30);
        page.getParagraphs().add(image);

        TextFragment fragment2 = new TextFragment("This is the second part of the same paragraph.");
        fragment2.setInLineParagraph(true);
        fragment2.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment2.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment2);

        TextFragment fragment3 = new TextFragment("This is a new paragraph.");
        fragment3.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment3.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment3);

        document.save(outputFile.toString());
    }
}
```

## إنشاء تخطيط نص متعدد الأعمدة

استخدم هذا المثال عندما يجب أن يتدفق نص بنمط المقال عبر عدة أعمدة.

1. أنشئ مستند PDF جديد واضبط هوامش الصفحة.
1. أضف محتوى العنوان وأنشئ متعدد الأعمدة `FloatingBox`.
1. املأه بالنص واحفظ ملف PDF النهائي.

```java
public static void createMultiColumnPdf(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        document.getPageInfo().getMargin().setLeft(40);
        document.getPageInfo().getMargin().setRight(40);
        Page page = document.getPages().add();

        com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500.0, 2.0);
        page.getParagraphs().add(graph1);
        graph1.getShapes().addItem(new com.aspose.pdf.drawing.Line(new float[] {1.0f, 2.0f, 500.0f, 2.0f}));

        String html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>";
        page.getParagraphs().add(new HtmlFragment(html));

        FloatingBox box = new FloatingBox();
        box.getColumnInfo().setColumnCount(2);
        box.getColumnInfo().setColumnSpacing("5");
        box.getColumnInfo().setColumnWidths("105 105");

        TextFragment text1 = new TextFragment("By A Googler (The Official Google Blog)");
        text1.getTextState().setFontSize(8);
        text1.getTextState().setLineSpacing(2);
        box.getParagraphs().add(text1);

        text1.getTextState().setFontSize(10);
        text1.getTextState().setFontStyle(FontStyles.Italic);

        com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50.0, 10.0);
        graph2.getShapes().addItem(new com.aspose.pdf.drawing.Line(new float[] {1.0f, 10.0f, 100.0f, 10.0f}));
        box.getParagraphs().add(graph2);

        String loremText = loremText();
        box.getParagraphs().add(new TextFragment(loremText.repeat(5)));
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```

## إنشاء نص محاذى مع توقفات تبويب مخصصة

استخدم هذا المثال عندما يجب أن يتماشى النص مثل جدول بسيط باستخدام مواضع إيقاف التبويب.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. اضبط محددات التبويب مع إعدادات المحاذاة والقائد.
1. أنشئ مقاطع النص التي تستخدم تلك نقاط التبويب واحفظ المستند.

```java
public static void customTabStops(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TabStops tabStops = new TabStops();
        TabStop tabStop1 = tabStops.add(100);
        tabStop1.setAlignmentType(TabAlignmentType.Right);
        tabStop1.setLeaderType(TabLeaderType.Solid);

        TabStop tabStop2 = tabStops.add(200);
        tabStop2.setAlignmentType(TabAlignmentType.Center);
        tabStop2.setLeaderType(TabLeaderType.Dash);

        TabStop tabStop3 = tabStops.add(300);
        tabStop3.setAlignmentType(TabAlignmentType.Left);
        tabStop3.setLeaderType(TabLeaderType.Dot);

        TextFragment header = new TextFragment("This is an example of forming table with TAB stops", tabStops);
        TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tabStops);
        TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tabStops);

        TextFragment text2 = new TextFragment("#$TABdata21 ", tabStops);
        text2.getSegments().add(new TextSegment("#$TAB"));
        text2.getSegments().add(new TextSegment("data22 "));
        text2.getSegments().add(new TextSegment("#$TAB"));
        text2.getSegments().add(new TextSegment("data23"));

        page.getParagraphs().add(header);
        page.getParagraphs().add(text0);
        page.getParagraphs().add(text1);
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```
