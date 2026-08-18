---
title: Форматирование PDF-текста в Java
linktitle: Форматирование текста внутри PDF
type: docs
weight: 70
url: /java/text-formatting-inside-pdf/
description: Узнайте, как форматировать текст внутри PDF-документов в Java с использованием интервалов, примечаний, списков, многоколоночного макета и параметров стиля.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Форматируйте и стилизуйте текст внутри PDF-файлов с помощью Java
Abstract: В этой статье объясняется, как форматировать текст в PDF-документах с помощью Aspose.PDF для Java. Он охватывает межстрочный интервал, межсимвольный интервал, маркированные и нумерованные списки, сноски и концевые сноски, содержимое встроенного абзаца, макет с несколькими столбцами, принудительные разрывы страниц и настраиваемые позиции табуляции.
---
Aspose.PDF для Java предлагает элементы управления форматированием текста для интервалов, списков, примечаний, встроенного макета и композиции из нескольких столбцов.

## Установите простой межстрочный интервал

Используйте этот пример, когда в тексте абзаца должно использоваться фиксированное значение межстрочного интервала.

1. Создайте новый PDF-документ и добавьте страницу.
1. Загрузите или подготовьте исходный текст и создайте `TextFragment`.
1. Установите межстрочный интервал, добавьте фрагмент на страницу и сохраните документ.

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

## Сравните режимы межстрочного интервала с пользовательским шрифтом

Используйте этот пример, когда необходимо протестировать межстрочный интервал с разными режимами форматирования для одного и того же шрифта.

1. Создайте новый PDF-документ и добавьте страницу.
1. Загрузите собственный шрифт и подготовьте два фрагмента с разными режимами межстрочного интервала.
1. Добавьте оба фрагмента на страницу и сохраните PDF.

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

## Установка интервала между символами с помощью текстовых фрагментов

Используйте этот пример, когда один и тот же текст должен отображаться с разными значениями интервала между символами.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создавайте фрагменты текста с помощью вспомогательного метода для нескольких значений интервалов.
1. Добавьте фрагменты на страницу и сохраните документ.

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

## Установите интервал между символами внутри абзаца текста

Используйте этот пример, когда необходимо применить интервал между символами внутри ограниченного текстового абзаца.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте `TextParagraph` с целевым прямоугольником и параметрами переноса.
1. Добавьте стилизованный фрагмент текста и сохраните PDF-файл.

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

## Создайте маркированный список с помощью HTML

Используйте этот пример, когда форматирование неупорядоченного списка должно быть создано с помощью разметки HTML.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте строку списка HTML.
1. Добавьте его как `HtmlFragment` и сохраните документ.

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

## Создайте нумерованный список с помощью HTML

Используйте этот пример, когда форматирование упорядоченного списка должно быть создано на основе разметки HTML.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте упорядоченную строку списка HTML.
1. Добавьте его как `HtmlFragment` и сохраните документ.

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

## Создайте маркированный список с помощью LaTeX

Используйте этот пример, когда форматирование неупорядоченного списка должно быть отображено с помощью разметки TeX.

1. Создайте новый PDF-документ и добавьте страницу.
1. Подготовьте строку списка TeX в среде `itemize`.
1. Добавьте его как `TeXFragment` и сохраните PDF.

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

## Создайте нумерованный список с помощью LaTeX

Используйте этот пример, когда форматирование упорядоченного списка должно быть отображено на основе разметки TeX.

1. Создайте новый PDF-документ и добавьте страницу.
1. Подготовьте строку списка TeX в среде `enumerate`.
1. Добавьте его как `TeXFragment` и сохраните PDF.

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

## Создайте маркированный список с текстовыми абзацами

Используйте этот пример, когда маркированный список вручную необходимо создать из фрагментов обычного текста.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте `TextParagraph` и добавьте фрагменты с префиксом маркера.
1. Добавьте абзац на страницу и сохраните документ.

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

## Создайте нумерованный список с текстовыми абзацами

Используйте этот пример, когда нумерованный вручную список необходимо построить из фрагментов простого текста.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте `TextParagraph` и добавьте пронумерованные фрагменты.
1. Добавьте абзац на страницу и сохраните документ.

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

## Добавьте базовую сноску

Используйте этот пример, когда фрагмент текста должен ссылаться на простую сноску.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте основной фрагмент текста и назначьте `Note` в качестве сноски.
1. Добавьте любой встроенный текст продолжения и сохраните документ.

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

## Добавьте сноску с собственным стилем текста

Используйте этот пример, когда в содержимом сноски должны использоваться собственные настройки шрифта, размера и цвета.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте основной фрагмент текста и настройте стилизованную сноску.
1. Прикрепите заметку и сохраните PDF-файл.

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

## Добавление сноски с текстом пользовательского маркера

Используйте этот пример, когда видимый маркер сноски необходимо заменить пользовательским текстом.

1. Создайте новый PDF-документ и добавьте страницу.
1. Назначьте сноску основному фрагменту текста и переопределите текст ее маркера.
1. Добавьте оставшееся содержимое и сохраните документ.

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

## Настройте линию-разделитель сносок

Используйте этот пример, когда линия, отделяющая сноски от содержимого страницы, должна быть явно стилизована.

1. Создайте новый PDF-документ и добавьте страницу.
1. Настройте стиль линии примечания страницы с помощью `GraphInfo`.
1. Добавьте фрагменты текста со сносками и сохраните документ.

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

## Добавьте сноску с изображением и содержимым таблицы.

Используйте этот пример, когда сама сноска должна содержать богатое содержимое, такое как изображения, текст и таблицы.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте объект `Note` с изображением, встроенным текстом и таблицей.
1. Прикрепите его к основному фрагменту текста и сохраните документ.

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

## Добавьте сноску

Используйте этот пример, когда фрагмент текста должен ссылаться на содержимое концевой сноски, а не на сноску страницы.

1. Создайте новый PDF-документ и добавьте страницу.
1. Присвойте сноску основному фрагменту текста и добавьте вспомогательный основной текст.
1. Сохраните документ с созданным содержимым сноски.

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

## Добавьте концевую сноску с текстом пользовательского маркера.

Используйте этот пример, когда маркер концевой сноски должен использовать пользовательскую видимую метку.

1. Создайте новый PDF-документ и добавьте страницу.
1. Назначьте сноску основному фрагменту текста и переопределите текст его маркера.
1. Добавьте оставшийся текст документа и сохраните PDF.

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

## Перенести содержимое таблицы на новую страницу

Используйте этот пример, когда форматированный контент должен явно начинаться на новой странице.

1. Создайте новый PDF-документ и добавьте страницу.
1. Постройте таблицу и заполните ее строки.
1. Настройте начало таблицы на новой странице и сохраните документ.

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

## Смешивайте встроенный контент внутри одного абзаца

Используйте этот пример, когда текст и изображения должны продолжаться внутри одного абзаца.

1. Создайте новый PDF-документ и добавьте страницу.
1. Добавьте первый фрагмент текста, затем встроенное изображение, затем еще один фрагмент встроенного текста.
1. Добавьте любой следующий отдельный абзац и сохраните документ.

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

## Создайте текстовый макет с несколькими столбцами

Используйте этот пример, когда текст в стиле статьи должен проходить через несколько столбцов.

1. Создайте новый PDF-документ и настройте поля страницы.
1. Добавьте содержимое заголовка и создайте многостолбец `FloatingBox`.
1. Заполните его текстом и сохраните окончательный PDF-файл.

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

## Создание выровненного текста с настраиваемыми позициями табуляции

Используйте этот пример, когда текст должен быть выровнен как простая таблица с использованием позиций табуляции.

1. Создайте новый PDF-документ и добавьте страницу.
1. Настройте позиции табуляции с настройками выравнивания и выноски.
1. Создайте фрагменты текста, использующие эти позиции табуляции, и сохраните документ.

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
