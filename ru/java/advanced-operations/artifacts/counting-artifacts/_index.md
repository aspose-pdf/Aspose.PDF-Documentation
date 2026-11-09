---
title: Подсчёт артефактов пагинации в PDF на Java
linktitle: Подсчёт артефактов по подтипам
type: docs
weight: 40
url: /ru/java/counting-artifacts/
description: Узнайте, как проверять и подсчитывать артефакты разметки страниц в PDF‑документах с помощью Java и Aspose.PDF.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Подсчёт артефактов пагинации в PDF на Java
Abstract: В этой статье объясняется, как проверять и подсчитывать артефакты разметки страниц в PDF‑документах с использованием Aspose.PDF for Java. Показано, как проходить по артефактам страниц и подсчитывать подтипы водяных знаков, фона, верхних и нижних колонтитулов.
---
## Подсчёт артефактов пагинации на странице

Используйте этот пример, когда вам нужно быстро подсчитать основные подтипы артефактов пагинации на странице.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите коллекцию объектов [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) с нужной страницы [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Переберите коллекцию объектов [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) на странице.
1. Подсчитайте артефакты каждого подтипа пагинации, который необходимо отразить в отчете.

```java
public static void countPdfArtifacts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int watermarks = 0;
        int backgrounds = 0;
        int headers = 0;
        int footers = 0;

        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination) {
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                    watermarks++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                    backgrounds++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Header) {
                    headers++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Footer) {
                    footers++;
                }
            }
        }

        System.out.println("Watermarks: " + watermarks);
        System.out.println("Backgrounds: " + backgrounds);
        System.out.println("Headers: " + headers);
        System.out.println("Footers: " + footers);
    }
}
```

## См. также

- [Работа с PDF-артефактами](/pdf/ru/java/artifacts/)
- [Извлечение текста и границ водяных знаков](/pdf/ru/java/extract-watermarks/)
- [Удаление фона](/pdf/ru/java/remove-backgrounds/)
- [Удаление водяных знаков](/pdf/ru/java/remove-watermarks/)
- [Удаление нумерации Бейтса](/pdf/ru/java/remove-bates-numbering/)
- [Удаление колонтитулов](/pdf/ru/java/remove-headers-footers/)
