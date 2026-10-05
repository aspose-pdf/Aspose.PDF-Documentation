---
title: Добавление верхних и нижних колонтитулов PDF в Java
linktitle: Добавление верхнего и нижнего колонтитулов в PDF
type: docs
weight: 50
url: /ru/java/add-headers-and-footers-of-pdf-file/
description: Узнайте, как добавить колонтитулы в PDF-файлы на Java, используя текст, изображения и структурированный контент.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте колонтитулы в PDF-файлы с помощью Java.
Abstract: В этой статье показано, как добавлять верхние и нижние колонтитулы в PDF‑документы с использованием Aspose.PDF for Java. Описывается работа с текстом, нумерацией страниц, HTML, изображениями, таблицами и содержимым верхних и нижних колонтитулов на основе LaTeX.
---
Aspose.PDF for Java позволяет вам назначать объекты `HeaderFooter` каждой странице и заполнять их различными типами контента.

## Добавление текстовых верхних и нижних колонтитулов

Используйте этот пример, когда вам нужен простой текстовый контент вверху и внизу каждой страницы.

1. Создайте объекты [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) и добавьте текстовые фрагменты.
1. Настройте отступы для верхнего и нижнего колонтитула.
1. Примените их к каждой странице исходного PDF и сохраните результат.

```java
public static void addHeaderAndFooterAsText(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Demo header"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Demo footer"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Добавление верхних и нижних колонтитулов с нумерацией страниц

Используйте этот пример, когда в верхнем или нижнем колонтитуле должны отображаться текущий номер страницы и общее количество страниц.

1. Создайте объекты [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) с заполнителями нумерации страниц.
1. Настройте поля для обоих объектов.
1. Примените их к каждой странице и сохраните обновлённый PDF.

```java
public static void usingHeaderAndFooterForPageNumbering(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Page $p from $P"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Page $p / $P"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Добавление верхних и нижних HTML-колонтитулов

Используйте этот пример, когда содержание верхнего и нижнего колонтитулов должно включать встроенное форматирование HTML.

1. Создайте объекты содержимое [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) и добавьте [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/).
1. Настройте поля для размещения.
1. Назначьте верхний и нижний колонтитулы каждой странице и сохраните документ.

```java
public static void addHeaderAndFooterAsHtml(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new HtmlFragment("This is an HTML <strong>Header</strong>"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new HtmlFragment("Powered by <i>Aspose.PDF</i>"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Добавление изображений в верхние и нижние колонтитулы

Используйте этот пример, когда в верхнем и нижнем колонтитулах необходимо отображать изображение на каждой странице.

1. Создайте объекты [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) и добавьте их в контейнеры верхнего и нижнего колонтитулов.
1. Настройте поля и назначьте контейнеры каждой странице.
1. Сохраните обновленный PDF.

```java
public static void addHeaderAndFooterAsImage(Path inputFile, Path imageFile, Path outputFile) {
    Image headerImage = new Image();
    headerImage.setFile(imageFile.toString());
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(headerImage);

    Image footerImage = new Image();
    footerImage.setFile(imageFile.toString());
    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(footerImage);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            MarginInfo margin = new MarginInfo();
            margin.setLeft(50);
            header.setMargin(margin);
            footer.setMargin(margin);
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Добавление верхних и нижних колонтитулов на основе таблицы

Используйте этот пример, когда содержимое верхнего и нижнего колонтитулов должно использовать табличную разметку и стилизацию текста.

1. Создайте необходимые стили текста и объекты таблицы.
1. Добавьте таблицы в контейнеры [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/).
1. Примените верхний и нижний колонтитулы к каждой странице и сохраните документ.

```java
public static void addHeaderAndFooterAsTable(Path inputFile, Path outputFile) {
    TextState textStateHeader = new TextState();
    textStateHeader.setFont(FontRepository.findFont("Arial"));
    textStateHeader.setFontSize(12);
    textStateHeader.setHorizontalAlignment(HorizontalAlignment.Center);

    TextState textStateFooter = new TextState();
    textStateFooter.setFont(FontRepository.findFont("Arial"));
    textStateFooter.setFontSize(12);
    textStateFooter.setHorizontalAlignment(HorizontalAlignment.Left);

    HeaderFooter header = new HeaderFooter();
    HeaderFooter footer = new HeaderFooter();

    Table tableHeader = new Table();
    tableHeader.setColumnWidths(String.valueOf(594 - header.getMargin().getLeft() - header.getMargin().getRight()));
    tableHeader.getRows().add().getCells().add("This is a Table Header", textStateHeader);

    Table table = new Table();
    table.setColumnWidths(String.valueOf(594 - footer.getMargin().getLeft() - footer.getMargin().getRight()));
    table.getRows().add().getCells().add("Powered by Aspose.PDF", textStateFooter);

    header.getParagraphs().add(tableHeader);
    footer.getParagraphs().add(table);
    footer.getMargin().setLeft(150);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## Добавление верхних и нижних колонтитулов LaTeX

Используйте этот пример, когда верхний и нижний колонтитулы должны отображать содержимое TeX или LaTeX.

1. Откройте исходный PDF и определите общее количество страниц.
1. Создайте содержимое [TeXFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) для верхнего и нижнего колонтитула каждой страницы.
1. Назначьте содержимое и сохраните документ.

```java
public static void addHeaderAndFooterAsLatex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int pageCount = document.getPages().size();
        for (int i = 1; i <= pageCount; i++) {
            HeaderFooter header = new HeaderFooter();
            header.getParagraphs().add(new TeXFragment("This is a LaTeX Header. \\today\\", true));

            HeaderFooter footer = new HeaderFooter();
            footer.getParagraphs().add(new TeXFragment("\\copyright\\ 2025 My Company -- Page \\thepage\\ is " + pageCount, true));

            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```


