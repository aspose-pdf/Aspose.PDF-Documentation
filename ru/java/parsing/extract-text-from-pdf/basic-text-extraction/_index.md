---
title: Базовое извлечение текста с использованием Java
linktitle: Базовое извлечение текста
type: docs
weight: 10
url: /java/basic-text-extraction/
description: Узнайте, как извлечь текст из PDF-документов на Java с помощью Aspose.PDF со всех страниц, с определенной страницы или по структуре абзацев.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Базовое извлечение текста — это отправная точка для чтения содержимого PDF на Java. Aspose.PDF предлагает два распространенных подхода:

- Используйте `TextAbsorber`, когда вам нужен простой текстовый результат из документа или страницы.
- Используйте `ParagraphAbsorber`, когда вам нужно сохранить группировку страниц, разделов, абзацев, строк и фрагментов.

Страницы PDF не хранят текст, как текстовый документ, поэтому порядок извлечения зависит от потока содержимого страницы и макета. Для извлечения данных по конкретному региону, деталей геометрии, макетов с несколькими столбцами, аннотаций, выделенного текста или обнаружения надстрочного и нижнего индекса используйте соответствующие статьи по извлечению в этом разделе.

## Извлеките текст со всех страниц

Используйте `TextAbsorber`, чтобы собрать плоский текстовый поток из всего документа и записать его в файл. Это самый простой вариант, когда вам нужен только читаемый текстовый контент и не нужны границы или координаты абзацев.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/), чтобы накапливать текст по всему документу.
1. Вызовите `document.getPages().accept(textAbsorber)`, чтобы каждая [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) посещалась поглотителем.
1. Запишите извлеченный текстовый буфер в выходной файл.

```java
public static void extractTextFromAllPages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## Извлеките текст с определенной страницы

Наносите поглотитель только на нужную вам страницу. Номера страниц в коллекции страниц `Document` начинаются с 1, поэтому `get_Item(1)` считывает первую страницу.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) для извлечения одной страницы.
1. Вызовите `accept(textAbsorber)` на целевой [странице](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), выбранной по номеру страницы.
1. Запишите извлеченный текстовый буфер в выходной файл.

```java
public static void extractTextFromPage(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().get_Item(pageNumber).accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## Извлечение текста по структуре абзацев

Используйте `ParagraphAbsorber`, когда вам нужна структурная группировка вместо одного простого текстового потока. Он возвращает разметку страницы с разделами, абзацами, строками и объектами `TextFragment`, что полезно, когда выходные данные должны сохранять логические блоки текста.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) и просмотрите весь документ, чтобы получить результаты разметки страницы.
1. Перебирайте разметку страницы, разделы, абзацы, строки и объекты [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), предоставляемые поглотителем.
1. Создавайте выходной текст с явной нумерацией страниц, разделов и абзацев, чтобы сохранить структурную группировку.
1. Запишите извлеченный текст абзаца в выходной файл.

```java
public static void extractParagraphsFromPdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document);

        StringBuilder text = new StringBuilder();
        for (PageMarkup pageMarkup : absorber.getPageMarkups()) {
            int sectionIndex = 1;
            for (MarkupSection section : pageMarkup.getSections()) {
                int paragraphIndex = 1;
                for (MarkupParagraph paragraph : section.getParagraphs()) {
                    StringBuilder paragraphText = new StringBuilder();
                    for (List<TextFragment> line : paragraph.getLines()) {
                        for (TextFragment fragment : line) {
                            paragraphText.append(fragment.getText());
                        }
                        paragraphText.append("\r\n");
                    }
                    text.append("Page ").append(pageMarkup.getNumber())
                            .append(", Section ").append(sectionIndex)
                            .append(", Paragraph ").append(paragraphIndex)
                            .append(":\n");
                    text.append(paragraphText).append("\n");
                    paragraphIndex++;
                }
                sectionIndex++;
            }
        }

        Files.writeString(outputFile, text.toString());
    }
}
```
