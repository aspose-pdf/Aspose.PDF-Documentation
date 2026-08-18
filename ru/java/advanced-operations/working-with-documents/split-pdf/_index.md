---
title: Разделить PDF-файлы в Java
linktitle: Разделить PDF-файлы
type: docs
weight: 60
url: /java/split-pdf-document/
description: Узнайте, как разделить страницы PDF на отдельные файлы PDF в Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Разделение PDF-документов по страницам, диапазонам, группам и шаблонам имен файлов с помощью Java
Abstract: В этой статье объясняется, как разделить PDF-документы с помощью Aspose.PDF для Java. Он охватывает разделение на отдельные страницы, две или три части, нечетные и четные страницы, фрагменты фиксированного размера, настраиваемые диапазоны, первую или последнюю страницу плюс остальные, настраиваемые группы страниц и стабильное создание имен файлов.
---
Aspose.PDF для Java поддерживает несколько шаблонов разделения, помимо вывода одной страницы на файл.

## Разделить PDF-файл на одностраничные файлы

Используйте этот подход, когда каждая исходная страница должна стать отдельным выходным документом.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте новый PDF-[Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для каждой [Страницы](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), которую вы хотите экспортировать.
1. Добавьте выбранную [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в новый документ.
1. Сохраните каждый выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## Разделить PDF-файл на две части

В этом примере исходный документ разделяется на два последовательных выходных файла на основе средней точки.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Рассчитайте среднюю точку доступной коллекции [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Скопируйте первую половину страниц в один выходной документ, а оставшиеся страницы — в другой.
1. Сохраните оба результирующих документа.

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

## Разделить PDF-файл на группы страниц фиксированного размера

Используйте этот шаблон, когда каждый выходной файл должен содержать одинаковое количество страниц, за исключением, возможно, последней части.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Просмотрите коллекцию [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) группами по `pagesPerPart`.
1. Создайте новый выходной документ для каждой группы и скопируйте в него рассчитанный диапазон страниц.
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

## Разделить PDF-файл по пользовательским диапазонам страниц

Этот пример позволяет вам явно определить начальную и конечную страницы для каждого выходного документа.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Определите необходимые диапазоны [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в массиве или другой коллекции.
1. Проверьте каждый диапазон на соответствие количеству исходных страниц и скопируйте соответствующие страницы в новый документ.
1. Сохраните каждый выходной файл на основе диапазона.

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

## Разделить первую страницу и оставшиеся страницы

Используйте этот подход, когда титульную страницу необходимо экспортировать отдельно от остальной части документа.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и убедитесь, что он содержит страницы.
1. Создайте один выходной документ для первой [Страницы](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Создайте еще один документ для оставшегося диапазона страниц, если доступно более одной страницы.
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

В этом примере последняя страница отделяется от остальной части документа, что полезно для извлечения страниц сводки или подписей.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и убедитесь, что он не пуст.
1. Скопируйте последнюю [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в новый выходной документ.
1. Удалите эту страницу из исходного документа, если предыдущие страницы еще остались.
1. Сохраните последнюю страницу и остальные страницы в отдельные файлы.

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

## Разделить PDF-файл на три части

Используйте этот шаблон, когда документ необходимо разделить на три последовательных раздела примерно одинакового размера.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и определите общее количество страниц.
1. Рассчитайте приблизительный размер каждой выходной части.
1. Создайте до трех документов и скопируйте соответствующие диапазоны [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
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

## Разделить PDF-файл на пользовательские группы страниц

В этом примере показано, как создавать выходные файлы из непоследовательных наборов страниц вместо непрерывных диапазонов.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Определите пользовательские группы номеров [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Создайте новый выходной документ для каждой группы и добавьте только допустимые страницы из этой группы.
1. Сохраните каждый непустой групповой документ.

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

## Разделите PDF-файл на отдельные страницы со стабильными именами файлов.

Используйте эту версию, когда имена выходных данных должны оставаться лексически сортируемыми, например в автоматизированных конвейерах.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте один выходной документ для каждой [Страницы](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Сохраняйте каждый файл с номером страницы, дополненным нулями.

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

## Разделить PDF-файл на нечетные и четные страницы

В этом примере создаются два вывода путем разделения страниц в соответствии с их четностью номеров страниц.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте один выходной документ для нечетных номеров [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и другой для четных номеров страниц.
1. Выполните итерацию по исходным страницам с необходимым приращением для каждого выходного документа.
1. Сохраните результаты нечетной и четной страницы отдельно.

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
