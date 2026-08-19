---
title: Добавить текст в PDF на Java
linktitle: Добавить текст в PDF
type: docs
weight: 10
url: /ru/java/add-text-to-pdf-file/
description: Узнайте, как добавлять текст, HTML‑фрагменты, списки, ссылки и пользовательские шрифты в PDF‑документы на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте текст, ссылки, HTML и шрифты в PDF‑файлы с помощью Java.
Abstract: В этой статье объясняется, как добавлять и оформлять текст в PDF‑документах с помощью Aspose.PDF for Java. Описываются простая вставка текста, макет абзацев, гиперссылки, текст справа налево, стилизация шрифтов, прозрачность, границы, фрагменты HTML и LaTeX, градиентный текст и пользовательские шрифты, загружаемые из файлов или потоков.
---
Aspose.PDF for Java поддерживает вставку обычного текста, продвинутую верстку, стилизацию, градиенты, HTML, LaTeX и пользовательские шрифты.

## Добавьте простой текстовый фрагмент

Используйте этот пример, когда короткую строку текста нужно разместить по фиксированным координатам страницы.

1. Создайте новый документ PDF и добавьте страницу.
1. Создайте `TextFragment` и установить его позицию.
1. Добавьте его на страницу и сохраните документ.

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

## Добавьте абзац внутри прямоугольника

Используйте этот пример, когда более крупный блок текста должен быть размещён внутри ограниченной области.

1. Создайте новый документ PDF и добавьте страницу.
1. Загрузите исходный текст и настройте a `TextParagraph` прямоугольник и режим обтекания.
1. Добавьте фрагмент через `TextBuilder` и сохраните PDF.

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

## Добавьте абзацы с различными настройками отступов

Используйте этот пример, когда первая строка и последующие строки должны использовать разные правила отступов.

1. Создайте новый документ PDF и добавьте страницу.
1. Подготовьте общий текстовый фрагмент и создайте несколько `TextParagraph` объекты.
1. Настройте отступы для каждого абзаца, добавьте их и сохраните документ.

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

## Вставить текст с ручным разрывом строки

Используйте этот пример, когда один фрагмент текста должен содержать явный перевод строки.

1. Создайте новый документ PDF и добавьте страницу.
1. Создайте `TextFragment` содержащий разрыв строки и настройте его стиль.
1. Добавьте его через `TextParagraph` и сохраните PDF.

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

## Проверьте обнаруженные разрывы строк

Используйте этот пример, когда вам нужно проверить вывод уведомления, связанный с разметкой текста и переносом строк.

1. Создайте новый PDF-документ и включите журналирование уведомлений.
1. Добавьте несколько длинных текстовых фрагментов на страницу.
1. Проверьте уведомления и сохраните документ.

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

## Измерять ширину текста динамически

Используйте этот пример, когда ширины символов и строк должны измеряться до принятия решений о макете.

1. Определите целевой шрифт и создайте `TextState`.
1. Измерьте символы и сравните результаты из API шрифтов и API состояния текста.
1. Выведите любые несоответствия для валидации.

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

## Добавьте текст с сегментом гиперссылки

Используйте этот пример, когда часть фрагмента текста должна вести себя как веб‑ссылка.

1. Создайте новый документ PDF и добавьте страницу.
1. Создайте `TextFragment` с несколькими `TextSegment` объекты.
1. Назначьте гиперссылку и стиль целевому сегменту, затем сохраните документ.

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

## Добавьте текст справа налево

Используйте этот пример, когда документ должен отображать контент со скриптом справа налево с правильным выравниванием.

1. Создайте новый документ PDF и добавьте страницу.
1. Создайте `TextFragment` с целевым RTL‑текстом и настройте его шрифт и выравнивание.
1. Добавьте его на страницу и сохраните PDF.

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

## Добавьте стилизованный текст и сегменты, похожие на формулы

Используйте этот пример, когда обычный текст и сегменты, похожие на нижний индекс, должны использовать разные текстовые состояния в одном выводе.

1. Создайте новый документ PDF и добавьте страницу.
1. Создайте основной стилизованный фрагмент и составьте формулу с вспомогательными сегментами.
1. Добавьте оба фрагмента на страницу и сохраните документ.

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

## Добавьте подчеркнутый текст

Используйте этот пример, когда текстовый фрагмент должен явно отображать подчеркивание.

1. Создайте новый документ PDF и добавьте страницу.
1. Создайте фрагмент текста, настройте его шрифт и состояние подчеркивания, а также задайте его позицию.
1. Добавьте к нему `TextBuilder` и сохранить результат.

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

## Добавьте прозрачный текст поверх цветной формы

Используйте этот пример, когда текст должен отображаться полупрозрачным над фоновой графикой.

1. Создайте новый документ PDF и добавьте страницу.
1. Нарисуйте форму фона и создайте полупрозрачный фрагмент текста.
1. Добавьте оба элемента на страницу и сохраните документ.

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

## Добавьте невидимый текст

Используйте этот пример, когда поисковый или скрытый текст должен присутствовать без видимого отображения.

1. Создайте новый документ PDF и добавьте страницу.
1. Добавьте видимый текстовый фрагмент и второй фрагмент с включённым флагом невидимости.
1. Сохраните документ.

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

## Добавьте текст с прямоугольной рамкой

Используйте этот пример, когда текст должен быть отрисован вместе с его ограничивающим прямоугольником.

1. Создайте новый документ PDF и добавьте страницу.
1. Создайте стилизованный `TextFragment` и включить отрисовку границы текстового прямоугольника.
1. Добавьте к нему `TextBuilder` и сохраните PDF.

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

## Добавьте зачёркнутый текст

Используйте этот пример, когда текст должен быть оформлен зачеркиванием.

1. Создайте новый документ PDF и добавьте страницу.
1. Создайте стилизованный фрагмент текста с включённым зачеркиванием.
1. Добавьте его на страницу и сохраните документ.

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

## Применить осевой градиент к тексту

Используйте этот пример, когда текст должен использовать линейную градиентную заливку вместо сплошного цвета.

1. Создайте новый документ PDF и добавьте страницу.
1. Создайте фрагмент текста и назначьте его цвету переднего плана аксиальный градиент.
1. Добавьте его на страницу и сохраните PDF.

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

## Применить радиальное градиентное затенение к тексту

Используйте этот пример, когда текст должен использовать радиальное градиентное заполнение.

1. Создайте новый документ PDF и добавьте страницу.
1. Создайте TextFragment и назначьте радиальный градиент его цвету переднего плана.
1. Добавьте его на страницу и сохраните документ.

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

## Добавьте встроенный текст, отформатированный в стиле HTML

Используйте этот пример, когда необходимо вставлять форматирование верхнего и нижнего индекса с помощью HTML-разметки.

1. Создайте новый документ PDF и добавьте страницу.
1. Создайте `HtmlFragment` с требуемой встроенной разметкой.
1. Добавьте его на страницу и сохраните PDF.

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

## Добавьте фрагмент текста LaTeX

Используйте этот пример, когда математический или TeX‑форматированный контент должен быть отрисован внутри PDF.

1. Создайте новый документ PDF и добавьте страницу.
1. Создайте `TeXFragment` с требуемым выражением.
1. Добавьте его на страницу и сохраните документ.

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

## Добавьте богатый HTML-фрагмент

Используйте этот пример, когда страница должна отображать структурированный HTML‑контент, такой как заголовки, абзацы и ссылки.

1. Создайте новый документ PDF и добавьте страницу.
1. Подготовьте строку HTML‑контента и создайте `HtmlFragment`.
1. Добавьте его на страницу и сохраните PDF.

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

## Добавьте HtmlFragment с переопределённым состоянием текста

Используйте этот пример, когда импортированный HTML‑контент должен наследовать контролируемую настройку шрифта и цвета.

1. Создайте новый документ PDF и добавьте страницу.
1. Подготовьте HTML‑контент и создайте `HtmlFragment`.
1. Назначить пользовательский `TextState`, добавьте фрагмент, и сохраните документ.

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

## Используйте пользовательский шрифт, загруженный из файла

Используйте этот пример, когда текст должен использовать шрифт, загруженный напрямую из пути к файлу шрифта.

1. Разрешите путь к пользовательскому файлу шрифта.
1. Создайте TextFragment и загрузите Font через `FontRepository.openFont`.
1. Примените настройки шрифта и сохраните документ.

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

## Используйте пользовательский шрифт, загруженный из потока

Используйте этот пример, когда пользовательский шрифт должен быть открыт из потока и встроен в PDF.

1. Откройте файл шрифта как поток и загрузите его с помощью `FontRepository`.
1. Создайте фрагмент текста и назначьте встроенный шрифт.
1. Добавьте фрагмент на страницу и сохраните документ.

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

