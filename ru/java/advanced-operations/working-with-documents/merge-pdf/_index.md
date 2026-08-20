---
title: Объединить PDF-файлы в Java
linktitle: Объединить PDF-файлы
type: docs
weight: 50
url: /ru/java/merge-pdf-documents/
description: Узнайте, как объединить несколько PDF файлов в один документ на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объединяйте полные документы, выбранные диапазоны и чередующиеся страницы с помощью Java
Abstract: Эта статья объясняет, как объединять PDF‑документы с помощью Aspose.PDF for Java. В ней рассматриваются объединение двух файлов, объединение нескольких документов, выбор диапазонов страниц, вставка одного документа в другой в определённой позиции, чередование страниц и построение объединённого вывода с закладками разделов.
---
Aspose.PDF for Java поддерживает несколько стратегий объединения в зависимости от того, как должен быть собран вывод.

## Объединить два PDF-документа

Используйте этот подход, когда вам нужен самый простой процесс объединения и вы хотите добавить один полный документ к другому.

1. Откройте оба исходных PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) объекты.
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) коллекция из второго документа в первый документ.
1. Сохраните обновлённый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```

## Скопировать выбранный диапазон страниц между документами

Этот вспомогательный метод сохраняет логику объединения диапазонов страниц в одном месте, чтобы другие примеры могли повторно использовать ту же проверенную процедуру копирования.

1. Откройте или получите исходный и целевой PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) объекты.
1. Нормализуйте запрашиваемый диапазон страниц, чтобы он оставался в пределах доступного [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) коллекция.
1. Добавьте каждую страницу из проверенного диапазона в целевой документ.

```java
private static void appendPageRange(Document sourceDocument, Document destinationDocument, int startPage, int endPage) {
    int totalPages = sourceDocument.getPages().size();
    if (totalPages == 0) {
        return;
    }

    int start = Math.max(1, startPage);
    int end = Math.min(endPage, totalPages);
    if (start > end) {
        return;
    }

    for (int pageNumber = start; pageNumber <= end; pageNumber++) {
        destinationDocument.getPages().add(sourceDocument.getPages().get_Item(pageNumber));
    }
}
```

## Объедините несколько PDF-документов в один файл

Используйте этот шаблон, когда вам нужно объединить список входных файлов в один выходной документ последовательно.

1. Создайте пустой выходной PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Откройте каждый входной файл по одному и скопируйте его полностью [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) диапазон в выходной документ.
1. Сохраните объединённый результат после обработки всех исходных файлов.

```java
public static void mergeMultipleDocuments(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                appendPageRange(sourceDocument, outputDocument, 1, sourceDocument.getPages().size());
            }
        }
        outputDocument.save(outputFile.toString());
    }
}
```

## Объединить выбранные диапазоны страниц из двух документов

Этот пример создает пользовательский выходной файл, беря только определённые диапазоны страниц из каждого исходного документа.

1. Откройте оба исходных PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) объекты и создать новый выходной документ.
1. Добавьте только необходимое [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) диапазоны из каждого исходного документа.
1. Сохраните собранный выходной документ.

```java
public static void mergeSelectedPageRanges(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        appendPageRange(document1, outputDocument, 1, 2);
        appendPageRange(document2, outputDocument, 2, 3);
        outputDocument.save(outputFile.toString());
    }
}
```

## Вставить один PDF‑документ в другой в определённую позицию

Используйте этот подход, когда один документ должен отображаться внутри другого, а не только до или после него.

1. Откройте базовый и вставленный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) объекты и создать новый выходной документ.
1. Скопируйте первую часть базового документа, затем добавьте полностью вставляемый документ, а в конце добавьте оставшуюся часть базового. [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) диапазон.
1. Сохраните переупорядоченный результат в новый файл.

```java
public static void mergeInsertDocumentAtPosition(Path inputFile1, Path inputFile2, int insertAfterPage, Path outputFile) {
    try (Document baseDocument = new Document(inputFile1.toString());
         Document insertDocument = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int baseTotalPages = baseDocument.getPages().size();
        int insertIndex = Math.max(0, Math.min(insertAfterPage, baseTotalPages));

        appendPageRange(baseDocument, outputDocument, 1, insertIndex);
        appendPageRange(insertDocument, outputDocument, 1, insertDocument.getPages().size());
        appendPageRange(baseDocument, outputDocument, insertIndex + 1, baseTotalPages);

        outputDocument.save(outputFile.toString());
    }
}
```

## Объединить два PDF‑документа, чередуя страницы

В этом примере страницы из двух документов чередуются, что полезно, когда оба входных файла должны постранично вносить вклад в конечный результат.

1. Откройте оба исходных PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) объекты и создать новый выходной документ.
1. Переберите максимальное доступное количество страниц и добавьте каждую доступную [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) поочередно из первого и второго документов.
1. Сохраните документ с чередующимся выводом.

```java
public static void mergeAlternatingPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int document1Pages = document1.getPages().size();
        int document2Pages = document2.getPages().size();
        int maxPages = Math.max(document1Pages, document2Pages);

        for (int pageNumber = 1; pageNumber <= maxPages; pageNumber++) {
            if (pageNumber <= document1Pages) {
                outputDocument.getPages().add(document1.getPages().get_Item(pageNumber));
            }
            if (pageNumber <= document2Pages) {
                outputDocument.getPages().add(document2.getPages().get_Item(pageNumber));
            }
        }

        outputDocument.save(outputFile.toString());
    }
}
```

## Объединить документы с разделительными страницами и закладками

Используйте этот шаблон, когда объединённый файл должен оставаться легко навигируемым и чётко показывать, где начинается каждый исходный документ.

1. Создайте пустой выходной PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и откройте каждый исходный файл поочередно.
1. Добавьте разделитель [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) с заголовком, затем создать [КоллекцияЭлементовОглавления](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) закладка для этого раздела.
1. Добавьте исходные страницы, при желании добавьте закладку, указывающую на первую страницу содержимого, и сохраните окончательный объединённый документ.

```java
public static void mergeWithSectionSeparatorsAndBookmarks(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        int sectionIndex = 1;
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                int sourcePageCount = sourceDocument.getPages().size();

                Page separatorPage = outputDocument.getPages().add();
                separatorPage.getParagraphs().add(new TextFragment(
                        "Section " + sectionIndex + ": " + inputFile.getFileName()));

                OutlineItemCollection sectionBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                sectionBookmark.setTitle("Section " + sectionIndex);
                sectionBookmark.setAction(new GoToAction(separatorPage));
                outputDocument.getOutlines().add(sectionBookmark);

                int firstContentPageNumber = outputDocument.getPages().size() + 1;
                appendPageRange(sourceDocument, outputDocument, 1, sourcePageCount);

                if (sourcePageCount > 0 && firstContentPageNumber <= outputDocument.getPages().size()) {
                    OutlineItemCollection contentBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                    contentBookmark.setTitle("Section " + sectionIndex + " Content");
                    contentBookmark.setAction(new GoToAction(outputDocument.getPages().get_Item(firstContentPageNumber)));
                    sectionBookmark.add(contentBookmark);
                }
            }
            sectionIndex++;
        }

        outputDocument.save(outputFile.toString());
    }
}
```


