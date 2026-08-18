---
title: Extract Fonts from PDF via Java
linktitle: Извлечь шрифты из PDF
type: docs
weight: 30
url: /java/extract-fonts-from-pdf/
description: Используйте Aspose.PDF для Java для проверки и извлечения шрифтов, используемых в PDF-документе.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь шрифты из PDF с помощью Java
Abstract: В этой статье объясняется, как проверить шрифты, используемые в PDF-документе, с помощью Aspose.PDF для Java. Он показывает, как открыть PDF-файл, вызвать `getFontUtilities().getAllFonts()` и перебрать полученные объекты шрифтов, чтобы прочитать их имена.
---
Используйте извлечение шрифтов, когда вам нужно проверить типографику документа, проверить встроенные ресурсы или проверить использование шрифтов перед рабочими процессами преобразования или архивирования.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вызовите `document.getFontUtilities().getAllFonts()`, чтобы собрать все ресурсы [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/), на которые ссылается документ.
1. Перебирайте извлеченные объекты [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) и читайте каждое имя шрифта из метаданных шрифта.
1. Распечатайте названия шрифтов, чтобы можно было проверить или экспортировать типографику документа.

```java
public static void extractFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Font[] fonts = document.getFontUtilities().getAllFonts();
        for (Font font : fonts) {
            System.out.println(font.getFontName());
        }
    }
}
```
