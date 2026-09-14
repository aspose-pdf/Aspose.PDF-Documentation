---
title: Извлечение шрифтов из PDF с помощью Java
linktitle: Извлечение шрифтов из PDF
type: docs
weight: 30
url: /ru/java/extract-fonts-from-pdf/
description: Используйте Aspose.PDF for Java для проверки и извлечения шрифтов, используемых в документе PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь шрифты из PDF с использованием Java
Abstract: В этой статье объясняется, как проверять шрифты, используемые в документе PDF, с помощью Aspose.PDF for Java. Показано, как открыть PDF, вызвать `getFontUtilities().getAllFonts()`, и пройтись по полученным объектам шрифтов, чтобы прочитать их названия.
---
Используйте извлечение шрифтов, когда необходимо провести аудит типографии документа, проверить встроенные ресурсы или подтвердить использование шрифтов перед процессами конвертации или архивирования.

1. Откройте исходный PDF в [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Вызовите `document.getFontUtilities().getAllFonts()` собрать каждый [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) ресурс, на который ссылается документ.
1. Итерируйте извлечённые [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) объекты и считать каждое имя шрифта из метаданных шрифта.
1. Вывести имена шрифтов, чтобы типографику документа можно было проверить или экспортировать.

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


