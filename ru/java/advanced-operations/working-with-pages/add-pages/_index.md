---
title: Добавить PDF-страницы в Java
linktitle: Добавление страниц
type: docs
weight: 10
url: /java/add-pages/
description: Узнайте, как добавлять или вставлять страницы в документы PDF на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте или вставьте страницы PDF с помощью Java
Abstract: В этой статье объясняется, как добавлять страницы в файлы PDF с помощью Aspose.PDF для Java. Он охватывает вставку пустой страницы в определенную позицию, добавление страницы в конец документа и импорт страницы из другого PDF-файла.
---
Aspose.PDF для Java позволяет вставлять пустые страницы или импортировать страницы из другого документа.

## Вставить пустую страницу в определенную позицию

Используйте этот пример, если вам нужно добавить пустую страницу в середину существующего PDF-файла.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вставьте новую страницу в целевую позицию в коллекции страниц.
1. Сохраните обновленный документ.

```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## Добавьте пустую страницу в конец

Используйте этот пример, когда вам нужно расширить документ новой пустой последней страницей.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте новую страницу в конец коллекции страниц.
1. Сохраните измененный PDF-файл.

```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## Добавьте страницу из другого документа

Используйте этот пример, если вы хотите импортировать страницу из одного PDF-файла в другой PDF-файл.

1. Создайте целевой [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и откройте исходный документ.
1. Добавьте любой необходимый целевой контент и импортируйте целевую страницу из исходного PDF-файла.
1. Сохраните полученный документ.

```java
public static void addPageFromAnotherDocument(Path inputFile, Path outputFile) {
    try (Document document = new Document();
         Document anotherDocument = new Document(inputFile.toString())) {
        document.getPages().add().getParagraphs().add(new TextFragment("This is first page!"));
        document.getPages().add(anotherDocument.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```
