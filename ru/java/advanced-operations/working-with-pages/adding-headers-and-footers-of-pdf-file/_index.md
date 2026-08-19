---
title: Добавить заголовки и колонтитулы PDF в Java
linktitle: Добавление заголовка и колонтитула в PDF
type: docs
weight: 50
url: /ru/java/add-headers-and-footers-of-pdf-file/
description: Узнайте, как добавить колонтитулы в PDF-файлы на Java, используя текст, изображения и структурированный контент.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте колонтитулы в PDF-файлы с помощью Java.
Abstract: В этой статье показано, как добавлять верхние и нижние колонтитулы в PDF‑документы с использованием Aspose.PDF for Java. Описывается работа с текстом, нумерацией страниц, HTML, изображениями, таблицами и содержимым верхних и нижних колонтитулов на основе LaTeX.
---
Aspose.PDF for Java позволяет вам назначать `HeaderFooter` объекты на каждой странице и заполните их различными типами контента.

## Добавьте текстовые заголовки и нижние колонтитулы

Используйте этот пример, когда вам нужен простой текстовый контент вверху и внизу каждой страницы.

1. Создайте [Верхний и нижний колонтитул](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) объекты и добавить текстовые фрагменты.
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

## Добавьте заголовки и колонтитулы с нумерацией страниц

Используйте этот пример, когда в заголовке или нижнем колонтитуле должно отображаться текущий номер страницы и общее количество страниц.

1. Создайте [Верхний и нижний колонтитул](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) объекты с заполнителями нумерации страниц.
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

## Добавьте HTML-заголовки и колонтитулы

Используйте этот пример, когда содержание заголовка и нижнего колонтитула должно включать встроенное форматирование HTML.

1. Создайте [Верхний и нижний колонтитул](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) объекты и добавить [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) контент.
1. Настройте поля для размещения.
1. Назначьте заголовок и нижний колонтитул каждой странице и сохраните документ.

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

## Добавьте изображения в заголовки и нижние колонтитулы

Используйте этот пример, когда в шапке и подвале необходимо отображать изображение на каждой странице.

1. Создайте [Изображение](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) объекты и добавить их в контейнеры заголовка и нижнего колонтитула.
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

## Добавьте заголовки и нижние колонтитулы на основе таблицы

Используйте этот пример, когда содержимое заголовка и нижнего колонтитула должно использовать табличную разметку и стилизацию текста.

1. Создайте необходимые стили текста и объекты таблицы.
1. Добавьте таблицы в [Верхний и нижний колонтитул](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) контейнеры.
1. Примените заголовок и нижний колонтитул к каждой странице и сохраните документ.

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

## Добавьте заголовки и колонтитулы LaTeX

Используйте этот пример, когда заголовок и нижний колонтитул должны отображать содержимое TeX или LaTeX.

1. Откройте исходный PDF и определите общее количество страниц.
1. Создайте [Фрагмент TeX](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) контент для верхнего и нижнего колонтитула каждой страницы.
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

