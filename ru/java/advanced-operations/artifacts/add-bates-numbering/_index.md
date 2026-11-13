---
title: Добавление нумерации Бейтса в PDF на Java
linktitle: Добавление нумерации Бейтса
type: docs
weight: 10
url: /ru/java/add-bates-numbering/
description: Добавить последовательные идентификаторы Бейтса на страницы PDF в Java с помощью специализированного помощника нумерации Бейтса или универсального API пагинации.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление нумерации Бейтса в PDF на Java
Abstract: Добавить последовательные идентификаторы Бейтса на страницы PDF в Java с помощью специализированного помощника нумерации Бейтса или универсального API пагинации.
---
Артефакты нумерации Бейтса полезны в юридических, архивных и документооборотных процессах, где каждой странице нужен постоянный идентификатор на уровне страницы.

## Добавление нумерации Бейтса специальным методом

Используйте этот пример, когда хотите применить нумерацию Бейтса через специализированный помощник коллекции страниц.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте любые дополнительные страницы, необходимые для примера.
1. Настройте объект [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/).
1. Примените нумерацию Бейтса к коллекции страниц.
1. Сохраните выходной файл.

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

## Добавление нумерации Бейтса через артефакты пагинации

В этом примере применяется нумерация Бейтса путем передачи артефакта Бейтса через универсальный API пагинации.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте необходимые страницы.
1. Создайте [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/).
1. Добавьте его в список артефактов пагинации.
1. Примените артефакты пагинации к коллекции страниц.
1. Сохраните документ.

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

## См. также

- [Удаление нумерации Бейтса](/pdf/ru/java/remove-bates-numbering/)
- [Работа с PDF-артефактами](/pdf/ru/java/artifacts/)
