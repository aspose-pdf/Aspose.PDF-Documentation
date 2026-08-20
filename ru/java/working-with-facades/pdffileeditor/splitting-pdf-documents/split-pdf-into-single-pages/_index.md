---
title: Разделить PDF на отдельные страницы
linktitle: Разделить PDF на отдельные страницы
type: docs
weight: 30
url: /ru/java/split-pdf-into-single-pages/
description: Разделите PDF на одностраничные файлы вывода в Java с помощью фасада PdfFileEditor.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Экспортируйте каждую страницу PDF в отдельный файл с помощью Java
Abstract: Узнайте, как разделить PDF на файлы по одной странице с помощью Aspose.PDF for Java. В примере на Java используется PdfFileEditor для записи каждой страницы в отдельный файл PDF на основе шаблона имени файла.
---
## Разделить PDF на отдельные страницы

Используйте этот рабочий процесс, когда каждая исходная страница должна стать отдельным файлом PDF.

### Шаги

1. Создайте `PdfFileEditor` экземпляр.
2. Подготовьте шаблон выходного файла, включающий заполнитель страницы, например `%NUM%`.
3. Вызовите `splitToPages` с исходным файлом и шаблоном вывода.
4. Сохраните сгенерированные одностраничные файлы.

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```


