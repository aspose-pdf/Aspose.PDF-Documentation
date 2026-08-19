---
title: Базовое извлечение текста с использованием Java
linktitle: Базовое извлечение текста
type: docs
weight: 10
url: /ru/java/basic-text-extraction/
description: Узнайте, как извлекать текст из PDF‑документов в Java с помощью Aspose.PDF со всех страниц, с определённой страницы или по структуре абзацев.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Базовое извлечение текста — отправная точка для чтения содержимого PDF в Java. Aspose.PDF предоставляет два распространённых подхода:

- Используйте `TextAbsorber` когда вам нужен результат в виде обычного текста из документа или страницы.
- Используйте `ParagraphAbsorber` когда вам нужно сохранить группировку страниц, разделов, абзацев, строк и фрагментов.

Страницы PDF не хранят текст так, как документы текстовых процессоров, поэтому порядок извлечения зависит от потока содержимого страницы и её макета. Для извлечения по определённым областям, деталей геометрии, много колонных макетов, аннотаций, выделенного текста или обнаружения надстрочного и подстрочного текста используйте соответствующие статьи об извлечении в этом разделе.

## Извлеките текст со всех страниц

Использовать `TextAbsorber` собрать единый поток текста из всего документа и записать его в файл. Это самый простой вариант, когда вам нужен только читаемый текстовый контент и не нужны границы абзацев или координаты.

1. Откройте исходный PDF в [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) для накопления текста по всему документу.
1. Вызов `document.getPages().accept(textAbsorber)` так каждый [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) посещается поглотителем.
1. Запишите извлеченный буфер текста в выходной файл.

```java
public static void extractTextFromAllPages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## Извлеките текст из конкретной страницы

Примените поглотитель только к нужной странице. Номера страниц в `Document` коллекция страниц индексируется с 1, поэтому `get_Item(1)` читает первую страницу.

1. Откройте исходный PDF в [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) для извлечения одиночной страницы.
1. Вызов `accept(textAbsorber)` на цель [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) выбранный по номеру страницы.
1. Запишите извлеченный буфер текста в выходной файл.

```java
public static void extractTextFromPage(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().get_Item(pageNumber).accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## Извлекать текст по структуре абзацев

Использовать `ParagraphAbsorber` когда вам нужна структурная группировка вместо одного простого текстового потока. Он возвращает разметку страниц с разделами, абзацами, строками и `TextFragment` объекты, что полезно, когда вывод должен сохранять логические блоки текста.

1. Откройте исходный PDF в [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) и просмотрите весь документ, чтобы построить результаты разметки страниц.
1. Итерировать по разметкам страниц, разделам, абзацам, строкам и [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) объекты, предоставляемые поглотителем.
1. Создайте выходной текст с явным нумерованием страниц, разделов и абзацев, чтобы сохранялась структурная группировка.
1. Запишите извлечённый текст абзаца в выходной файл.

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

