---
title: Добавить нумерацию Bates в PDF на Java
linktitle: Добавление нумерации Bates
type: docs
weight: 10
url: /ru/java/add-bates-numbering/
description: Узнайте, как добавить и удалить нумерацию Bates в PDF‑документах с использованием Java и Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить нумерацию Bates через Java
Abstract: В этой статье объясняется, как создавать и удалять артефакты нумерации Бейтса в PDF‑документах с использованием Aspose.PDF for Java. Описывается настройка `BatesNArtifact`, применение его с помощью вспомогательных средств нумерации Бейтса или общих средств пагинации, а также удаление нумерации Бейтса из документа.
---
Артефакты нумерации Бейтса полезны в юридических, архивных и процессах контроля документов, где каждой странице нужен постоянный идентификатор на уровне страницы.

## Добавьте нумерацию Бейтса с помощью специального помощника

Используйте этот пример, когда нужно применить нумерацию Бейтса с помощью специального помощника коллекции страниц.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте любые дополнительные страницы, необходимые для примера.
1. Создайте [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) конфигурация.
1. Примените нумерацию Bates к коллекции страниц и сохраните выходной файл.

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

## Добавьте нумерацию Bates через артефакты пагинации

В этом примере применяется нумерация Бейтса путем передачи артефакта Бейтса через общий API пагинации.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте необходимые страницы.
1. Создайте [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) и добавьте его в список артефактов пагинации.
1. Примените артефакты пагинации к коллекции страниц и сохраните документ.

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

## Удалите нумерацию Bates

Используйте этот подход, когда существующие артефакты нумерации Bates следует удалить из документа.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вызовите вспомогательную функцию коллекции страниц, которая удаляет нумерацию Bates.
1. Сохраните очищенный выходной файл.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```


