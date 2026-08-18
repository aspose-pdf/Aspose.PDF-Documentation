---
title: Подсчет PDF-артефактов в Java
linktitle: Подсчет артефактов
type: docs
weight: 40
url: /java/counting-artifacts/
description: Узнайте, как проверять и подсчитывать артефакты нумерации страниц в PDF-документах с помощью Java с Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Подсчет артефактов в PDF с использованием Java
Abstract: В этой статье объясняется, как проверять и подсчитывать артефакты нумерации страниц в PDF-документах с помощью Aspose.PDF для Java. Он показывает, как перебирать артефакты страницы и подсчитывать подтипы водяных знаков, фона, верхнего и нижнего колонтитула.
---
## Подсчет артефактов нумерации страниц на странице

Используйте этот пример, если вам нужно быстро подсчитать основные подтипы артефактов нумерации страниц на странице.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Прочтите коллекцию [Артефакт](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) с целевой [Страницы](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Просмотрите коллекцию страниц [Артефакт](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) и подсчитайте каждый подтип нумерации страниц, о котором вам нужно сообщить.

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
