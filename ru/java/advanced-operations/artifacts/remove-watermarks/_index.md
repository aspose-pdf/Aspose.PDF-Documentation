---
title: Удаление водяных знаков из PDF на Java
linktitle: Удаление водяных знаков
type: docs
weight: 90
url: /ru/java/remove-watermarks/
description: Удалить артефакты водяных знаков с первой страницы PDF в Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удаление водяных знаков из PDF на Java
Abstract: Удалить артефакты водяных знаков с первой страницы PDF в Java.
---
Удалить артефакты водяных знаков с первой страницы PDF в Java.

## Удаление артефактов водяных знаков

Пример удаляет с первой страницы только артефакты типа `Pagination` и подтипа `Watermark`. Видимые водяные знаки, сохранённые в виде обычного текста страницы, изображений или аннотаций, остаются в PDF.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите коллекцию артефактов страницы в обратном порядке.
1. Удалите артефакты нумерации, подтип которых соответствует водяному знаку.
1. Сохраните документ.

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## См. также

- [Добавление водяных знаков](/pdf/ru/java/add-watermarks/)
- [Извлечение текста и границ водяных знаков](/pdf/ru/java/extract-watermarks/)
- [Работа с PDF-артефактами](/pdf/ru/java/artifacts/)
