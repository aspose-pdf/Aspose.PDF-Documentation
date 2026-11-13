---
title: Извлечение текста и границ водяных знаков в PDF на Java
linktitle: Извлечение текста и границ водяных знаков
type: docs
weight: 50
url: /ru/java/extract-watermarks/
description: Прочитать текст и ограничивающий прямоугольник артефактов водяного знака на первой странице PDF в Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение текста и границ водяных знаков в PDF на Java
Abstract: Прочитать текст и ограничивающий прямоугольник артефактов водяного знака на первой странице PDF в Java.
---
Прочитать текст и ограничивающий прямоугольник артефактов водяного знака на первой странице PDF в Java.

## Извлечение текста и границ водяных знаков

Используйте этот пример, когда нужно проверить существующие артефакты водяного знака и прочитать их текст или позицию.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите коллекцию артефактов целевой страницы.
1. Отфильтруйте артефакты пагинации по подтипу водяного знака.
1. Выведите их текст и прямоугольники.

```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## См. также

- [Добавление водяных знаков](/pdf/ru/java/add-watermarks/)
- [Удаление водяных знаков](/pdf/ru/java/remove-watermarks/)
- [Работа с PDF-артефактами](/pdf/ru/java/artifacts/)
