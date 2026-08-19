---
title: Разделить PDF-файлы на Java
linktitle: Разделить PDF-файлы
type: docs
weight: 60
url: /ru/java/split-pdf-document/
description: Узнайте, как разделять страницы PDF на отдельные PDF‑файлы в Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Разделяйте PDF‑документы по страницам, диапазонам, группам и шаблонам имён файлов с помощью Java
Abstract: В этой статье объясняется, как разделять PDF‑документы с помощью Aspose.PDF for Java. Рассматриваются разделение на отдельные страницы, на две или три части, нечётные и чётные страницы, фрагменты фиксированного размера, пользовательские диапазоны, первая или последняя страница плюс остальное, пользовательские группы страниц и генерация стабильных имён файлов.
---
Aspose.PDF for Java поддерживает несколько вариантов разбиения, помимо вывода «одна страница в файл».

## Разбить PDF на одностраничные файлы

Используйте этот подход, когда каждая исходная страница должна стать отдельным выходным документом.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для каждого [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) вы хотите экспортировать.
1. Добавьте выбранное [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в новый документ.
1. Сохраните каждый выводной PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void splitDocuments(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve("Page_" + pageNumber + ".pdf").toString());
            }
        }
    }
}
```

## Разделить PDF на две части

Этот пример делит исходный документ на два последовательных выходных файла, основываясь на средней точке.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вычислите середину доступного [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) коллекция.
1. Скопируйте первую половину страниц в один выходной документ, а оставшиеся страницы — в другой.
1. Сохраните оба полученных документа.

```java
public static void splitDocumentsIntoTwoParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int midPoint = totalPages / 2;

        try (Document firstDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= midPoint; pageNumber++) {
                firstDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            firstDocument.save(outputDir.resolve("Part_1.pdf").toString());
        }

        try (Document secondDocument = new Document()) {
            for (int pageNumber = midPoint + 1; pageNumber <= totalPages; pageNumber++) {
                secondDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            secondDocument.save(outputDir.resolve("Part_2.pdf").toString());
        }
    }
}
```

## Разделить PDF на группы страниц фиксированного размера

Используйте этот шаблон, когда каждый файл вывода должен содержать одинаковое количество страниц, за исключением, возможно, последней части.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебрать [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) коллекция группами по `pagesPerPart`.
1. Создайте новый выходной документ для каждой группы и скопируйте рассчитанный диапазон страниц в него.
1. Сохраните каждую часть с сгенерированным именем файла.

```java
public static void splitDocumentsEveryNPages(Path inputFile, Path outputDir, int pagesPerPart) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int partIndex = 1;

        for (int startPage = 1; startPage <= totalPages; startPage += pagesPerPart) {
            int endPage = Math.min(startPage + pagesPerPart - 1, totalPages);
            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Every_" + pagesPerPart + "_Part_" + partIndex + ".pdf").toString());
            }
            partIndex++;
        }
    }
}
```

## Разделить PDF по пользовательским диапазонам страниц

Этот пример позволяет вам задавать явные начальные и конечные страницы для каждого выходного документа.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Определить требуемое [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) диапазоны в массиве или другой коллекции.
1. Проверьте каждый диапазон относительно количества страниц исходного документа и скопируйте соответствующие страницы в новый документ.
1. Сохраните каждый файл вывода, основанный на диапазоне.

```java
public static void splitDocumentsByPageRanges(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        Integer[][] ranges = {{1, 3}, {4, 6}, {7, null}};

        for (int index = 0; index < ranges.length; index++) {
            int startPage = ranges[index][0];
            Integer endPage = ranges[index][1];
            if (startPage > totalPages) {
                continue;
            }

            int effectiveEnd = endPage == null ? totalPages : Math.min(endPage, totalPages);
            if (startPage > effectiveEnd) {
                continue;
            }

            try (Document rangeDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= effectiveEnd; pageNumber++) {
                    rangeDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                rangeDocument.save(outputDir.resolve(
                        "Range_" + (index + 1) + "_" + startPage + "_to_" + effectiveEnd + ".pdf").toString());
            }
        }
    }
}
```

## Разделить первую страницу и остальные страницы

Используйте этот подход, когда обложка должна быть экспортирована отдельно от остальной части документа.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и подтвердите, что он содержит страницы.
1. Создайте один выходной документ для первого [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Создайте другой документ для оставшегося диапазона страниц, когда доступно более одной страницы.
1. Сохраните оба результата.

```java
public static void splitDocumentsFirstPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document firstPageDocument = new Document()) {
            firstPageDocument.getPages().add(document.getPages().get_Item(1));
            firstPageDocument.save(outputDir.resolve("First_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        try (Document remainingPagesDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber++) {
                remainingPagesDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            remainingPagesDocument.save(outputDir.resolve("Remaining_Pages.pdf").toString());
        }
    }
}
```

## Разделить последнюю страницу и предыдущие страницы

В этом примере последняя страница отделяется от остальной части документа, что полезно для извлечения страниц резюме или подписей.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и проверьте, что он не пустой.
1. Скопировать последнее [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в новый выходной документ.
1. Удалите эту страницу из оригинального документа, когда прежние страницы всё ещё остаются.
1. Сохраните последнюю страницу и остальные страницы как отдельные файлы.

```java
public static void splitDocumentsLastPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document lastPageDocument = new Document()) {
            lastPageDocument.getPages().add(document.getPages().get_Item(totalPages));
            lastPageDocument.save(outputDir.resolve("Last_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        document.getPages().delete(totalPages);
        document.save(outputDir.resolve("Previous_Pages.pdf").toString());
    }
}
```

## Разделить PDF на три части

Используйте этот шаблон, когда документ должен быть разделён на три последовательных раздела примерно одинакового размера.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и определите общее количество страниц.
1. Вычислите приблизительный размер каждой части вывода.
1. Создайте до трёх документов и скопируйте соответствующие [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) диапазоны.
1. Сохраните каждую сгенерированную часть.

```java
public static void splitDocumentsIntoThreeParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        int partSize = Math.max(1, (totalPages + 2) / 3);
        for (int partIndex = 0; partIndex < 3; partIndex++) {
            int startPage = partIndex * partSize + 1;
            int endPage = Math.min((partIndex + 1) * partSize, totalPages);
            if (startPage > totalPages) {
                break;
            }

            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Three_Parts_" + (partIndex + 1) + ".pdf").toString());
            }
        }
    }
}
```

## Разделить PDF на пользовательские группы страниц

Этот пример показывает, как создавать выходные файлы из наборов страниц, не идущих последовательно, вместо непрерывных диапазонов.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Определить пользовательские группы [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) числа.
1. Создайте новый выходной документ для каждой группы и добавьте в него только корректные страницы из этой группы.
1. Сохраните каждый непустой документ группы.

```java
public static void splitDocumentsCustomPageGroups(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        List<List<Integer>> groups = List.of(
                List.of(1, 2, 5),
                List.of(3, 4, 6, 7));

        int groupIndex = 1;
        for (List<Integer> group : groups) {
            try (Document groupDocument = new Document()) {
                for (Integer pageNumber : group) {
                    if (pageNumber >= 1 && pageNumber <= totalPages) {
                        groupDocument.getPages().add(document.getPages().get_Item(pageNumber));
                    }
                }
                if (groupDocument.getPages().size() > 0) {
                    groupDocument.save(outputDir.resolve("Custom_Group_" + groupIndex + ".pdf").toString());
                }
            }
            groupIndex++;
        }
    }
}
```

## Разделить PDF на отдельные страницы со стабильными именами файлов

Используйте эту версию, когда имена выходных файлов должны оставаться лексически сортируемыми, например в автоматизированных конвейерах.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте один выходной документ для каждого [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Сохраните каждый файл с номером страницы, дополненным нулями.

```java
public static void splitDocumentsWithStableFilenames(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve(String.format("Page_%03d.pdf", pageNumber)).toString());
            }
        }
    }
}
```

## Разделить PDF на нечётные и чётные страницы

Этот пример создает два выходных файла, разделяя страницы в зависимости от чётности их номера.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте один выходной документ для нечётных [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) числа и другое для четных номеров страниц.
1. Перебирайте исходные страницы с необходимым шагом для каждого выходного документа.
1. Сохраните результаты нечётных и чётных страниц отдельно.

```java
public static void splitDocumentsOddEvenPages(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();

        try (Document oddDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= totalPages; pageNumber += 2) {
                oddDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            oddDocument.save(outputDir.resolve("Odd_Pages.pdf").toString());
        }

        try (Document evenDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber += 2) {
                evenDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            evenDocument.save(outputDir.resolve("Even_Pages.pdf").toString());
        }
    }
}
```

