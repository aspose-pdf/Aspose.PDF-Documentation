---
title: Добавить нумерацию Бейтса в PDF на Java
linktitle: Добавление нумерации Бейтса
type: docs
weight: 10
url: /java/add-bates-numbering/
description: Узнайте, как добавлять и удалять нумерацию Бейтса в документах PDF с помощью Java с Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить нумерацию Бейтса через Java
Abstract: В этой статье объясняется, как создавать и удалять артефакты нумерации Бейтса в документах PDF с помощью Aspose.PDF для Java. В нем рассматривается настройка `BatesNArtifact`, применение его с помощью помощников нумерации Бейтса или общих помощников нумерации страниц, а также удаление нумерации Бейтса из документа.
---
Артефакты нумерации Бейтса полезны в юридических, архивных рабочих процессах и процессах управления документами, где каждой странице необходим постоянный идентификатор уровня страницы.

## Добавьте нумерацию Бейтса с помощью специального помощника

Используйте этот пример, если вы хотите применить нумерацию Бейтса с помощью специального помощника по сбору страниц.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте дополнительные страницы, необходимые для примера.
1. Создайте конфигурацию [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/).
1. Примените нумерацию Бейтса к коллекции страниц и сохраните выходной файл.

```java
public static void addBatesNArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        PageCollectionExtensions.addBatesNumbering(document.getPages(), batesArtifact);
        document.save(outputFile.toString());
    }
}
```

## Добавление нумерации Бейтса с помощью артефактов нумерации страниц

В этом примере применяется нумерация Бейтса путем передачи артефакта Бейтса через универсальный API разбиения на страницы.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте необходимые страницы.
1. Создайте [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) и добавьте его в список артефактов нумерации страниц.
1. Примените артефакты нумерации страниц к коллекции страниц и сохраните документ.

```java
public static void addBatesNArtifactPagination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        List<PaginationArtifact> paginationArtifacts = new ArrayList<>();
        paginationArtifacts.add(batesArtifact);
        PageCollectionExtensions.addPagination(document.getPages(), paginationArtifacts);
        document.save(outputFile.toString());
    }
}
```

## Удалите нумерацию Бейтса

Используйте этот подход, когда существующие артефакты нумерации Бейтса необходимо удалить из документа.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вызовите помощник по коллекции страниц, который удаляет нумерацию Бейтса.
1. Сохраните очищенный выходной файл.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```
