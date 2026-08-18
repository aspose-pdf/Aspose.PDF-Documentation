---
title: Объединение PDF-файлов в Java
linktitle: Объединить PDF-файлы
type: docs
weight: 50
url: /java/merge-pdf-documents/
description: Узнайте, как объединить несколько файлов PDF в один документ на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объединение полных документов, выбранных диапазонов и чередующихся страниц с помощью Java
Abstract: В этой статье объясняется, как объединить PDF-документы с помощью Aspose.PDF для Java. Он охватывает объединение двух файлов, объединение нескольких документов, выбор диапазонов страниц, вставку одного документа в другой в определенной позиции, чередование страниц и создание объединенного вывода с закладками разделов.
---
Aspose.PDF для Java поддерживает несколько стратегий слияния в зависимости от того, как следует собирать выходные данные.

## Объединить два PDF-документа

Используйте этот подход, когда вам нужен простейший процесс слияния и вы хотите добавить один полный документ к другому.

1. Откройте оба исходных объекта PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте коллекцию [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) из второго документа в первый документ.
1. Сохраните обновленный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```

## Копирование выбранного диапазона страниц между документами

Этот вспомогательный метод сохраняет логику слияния диапазона страниц в одном месте, поэтому другие примеры могут повторно использовать одну и ту же проверенную процедуру копирования.

1. Откройте или получите исходный и целевой PDF-объекты [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Нормализуйте запрошенный диапазон страниц, чтобы он оставался в пределах доступной коллекции [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
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

## Объединение нескольких PDF-документов в один файл

Используйте этот шаблон, когда вам нужно последовательно объединить список входных файлов в один выходной документ.

1. Создайте пустой выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Откройте каждый входной файл по одному и скопируйте его полный диапазон [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в выходной документ.
1. Сохраните объединенный результат после обработки всех исходных файлов.

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

В этом примере создается пользовательский выходной файл, используя только определенные диапазоны страниц из каждого исходного документа.

1. Откройте оба исходных объекта PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и создайте новый выходной документ.
1. Добавляйте только необходимые диапазоны [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) из каждого исходного документа.
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

## Вставка одного PDF-документа в другой в определенной позиции

Используйте этот подход, когда один документ должен появляться внутри другого, а не только до или после него.

1. Откройте базу и вставленные объекты PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и создайте новый выходной документ.
1. Скопируйте первую часть базового документа, затем добавьте весь вставленный документ и, наконец, добавьте оставшийся базовый диапазон [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
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

## Объедините два PDF-документа, чередуя страницы.

В этом примере страницы из двух документов чередуются, что полезно, когда оба входных документа должны постранично вносить вклад в окончательный результат.

1. Откройте оба исходных объекта PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и создайте новый выходной документ.
1. Переберите максимальное количество доступных страниц и поочередно добавьте каждую доступную [страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) из первого и второго документов.
1. Сохраните чередующийся выходной документ.

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

## Объединение документов с разделителями страниц и закладками

Используйте этот шаблон, если в объединенном файле должно быть легко ориентироваться и четко показывать, где начинается каждый исходный документ.

1. Создайте пустой выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и поочередно откройте каждый исходный файл.
1. Добавьте разделитель [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) с заголовком, затем создайте закладку [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) для этого раздела.
1. Добавьте исходные страницы, при необходимости добавьте закладку, указывающую на первую страницу содержимого, и сохраните окончательный объединенный документ.

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
