---
title: Удаление верхних и нижних колонтитулов из PDF на Java
linktitle: Удаление колонтитулов
type: docs
weight: 110
url: /ru/java/remove-headers-footers/
description: Удалить артефакты заголовка и колонтитула с первой страницы PDF в Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удаление верхних и нижних колонтитулов из PDF на Java
Abstract: Удалить артефакты заголовка и колонтитула с первой страницы PDF в Java.
---
Удалить артефакты заголовка и колонтитула с первой страницы PDF в Java.

## Удаление артефактов колонтитулов

Используйте этот подход, когда необходимо удалить существующие артефакты заголовка и колонтитула со страницы.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите коллекцию артефактов страницы в обратном порядке.
1. Удалите артефакты разметки страниц, у которых подтип соответствует верхнему или нижнему колонтитулу.
1. Сохраните документ.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## См. также

- [Добавление колонтитулов](/pdf/ru/java/artifacts-header-footer/)
- [Работа с PDF-артефактами](/pdf/ru/java/artifacts/)
