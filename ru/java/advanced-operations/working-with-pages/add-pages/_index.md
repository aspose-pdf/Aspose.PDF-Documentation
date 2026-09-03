---
title: Добавить страницы PDF в Java
linktitle: Добавление страниц
type: docs
weight: 10
url: /ru/java/add-pages/
description: Узнайте, как добавлять или вставлять страницы в PDF‑документы на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить или вставить страницы PDF с Java
Abstract: Эта статья объясняет, как добавлять страницы в файлы PDF с помощью Aspose.PDF for Java. В ней рассматривается вставка пустой страницы в определённую позицию, добавление страницы в конец документа и импорт страницы из другого PDF.
---
Aspose.PDF for Java позволяет вставлять пустые страницы или импортировать страницы из другого документа.

## Вставьте пустую страницу в определённую позицию

Используйте этот пример, когда нужно добавить пустую страницу в середину существующего PDF.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вставьте новую страницу в целевую позицию в коллекции страниц.
1. Сохраните обновлённый документ.

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

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте новую страницу в конец коллекции страниц.
1. Сохраните изменённый PDF.

```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## Добавьте страницу из другого документа

Используйте этот пример, когда хотите импортировать страницу из одного PDF в другой PDF.

1. Создайте место назначения [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и откройте исходный документ.
1. Добавьте любой необходимый контент назначения и импортируйте целевую страницу из исходного PDF.
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


