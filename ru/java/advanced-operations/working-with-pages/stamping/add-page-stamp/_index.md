---
title: Добавить штампы страниц в PDF на Java
linktitle: Добавление штампов страниц
type: docs
weight: 30
url: /ru/java/page-stamps-in-the-pdf-file/
description: Узнайте, как добавлять штампы страниц PDF в виде наложений или фонов на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте штампы, основанные на страницах, в PDF-файлы с помощью Java
Abstract: В этой статье объясняется, как добавить штамп страницы в документ PDF с использованием Aspose.PDF for Java. В примере загружается другая страница PDF в качестве штампа, настраивается как фон и применяется к целевой странице.
---
Aspose.PDF for Java может применять страницу из другого PDF в качестве штампа или добавлять наложения нумерации страниц.

## Добавьте штамп страницы из другого PDF

Используйте этот пример, когда страница из отдельного PDF должна использоваться в качестве фонового штампа.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfpagestamp/) из внешней страницы PDF.
1. Настройте штамп и добавьте его на целевую страницу, затем сохраните результат.

```java
public static void addPageStamp(Path inputFile, Path pageStampFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfPageStamp pageStamp = new PdfPageStamp(pageStampFile.toString(), 1);
        pageStamp.setBackground(true);
        document.getPages().get_Item(1).addStamp(pageStamp);
        document.save(outputFile.toString());
    }
}
```

## Добавьте стандартный штамп номера страницы

Используйте этот пример, когда целевая страница должна отображать текущий номер с пользовательским форматированием текста.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте и настройте [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).
1. Добавьте штамп на страницу и сохраните документ.

```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```

## Добавьте штамп номера страницы римскими цифрами

Используйте этот пример, когда нумерация страниц должна начинаться с пользовательского значения и использовать заглавные римские цифры.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) и настройте нумерацию римскими цифрами.
1. Добавьте штамп на все страницы и сохраните PDF.

```java
public static void addPageNumStampRoman(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(42);
        pageNumberStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        for (Page page : document.getPages()) {
            page.addStamp(pageNumberStamp);
        }
        document.save(outputFile.toString());
    }
}
```

