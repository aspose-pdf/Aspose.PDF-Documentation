---
title: Удаление фона из PDF на Java
linktitle: Удаление фона
type: docs
weight: 80
url: /ru/java/remove-backgrounds/
description: Удалить артефакты фона с первой страницы PDF в Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удаление фона из PDF на Java
Abstract: Удалить артефакты фона с первой страницы PDF в Java.
---
Удалить артефакты фона с первой страницы PDF в Java.

## Удаление артефактов фона

Используйте этот подход, когда существующие артефакты фона должны быть удалены со страницы.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите коллекцию артефактов страницы в обратном порядке.
1. Удалите артефакты, тип которых — Pagination, а подтип — Background.
1. Сохраните документ.

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## См. также

- [Добавление фона](/pdf/ru/java/add-backgrounds/)
- [Работа с PDF-артефактами](/pdf/ru/java/artifacts/)
