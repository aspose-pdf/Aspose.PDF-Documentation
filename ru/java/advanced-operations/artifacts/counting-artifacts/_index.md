---
title: Подсчет артефактов PDF в Java
linktitle: Подсчет артефактов
type: docs
weight: 40
url: /ru/java/counting-artifacts/
description: Узнайте, как просматривать и подсчитывать артефакты разметки страниц в PDF-документах с помощью Java и Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Подсчет артефактов в PDF с использованием Java
Abstract: В этой статье объясняется, как просматривать и подсчитывать артефакты разметки страниц в PDF-документах с помощью Aspose.PDF for Java. Показано, как перебрать артефакты страниц и подсчитать подтипы: водяной знак, фон, заголовок и нижний колонтитул.
---
## Подсчет артефактов разметки страниц на странице

Используйте этот пример, когда вам нужен быстрый подсчёт основных подтипов артефактов пагинации на странице.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Прочитайте [Артефакт](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) коллекцию из целевого [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Перебрать страницу [Артефакт](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) коллекцию и подсчитать каждый подтип нумерации, который вам нужно отобразить.

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

