---
title: Получить информацию о странице
linktitle: Получить информацию о странице
type: docs
weight: 10
url: /ru/java/get-page-info/
description: Узнайте, как проверять ширину, высоту и поворот страницы в Java с помощью фасада PdfFileInfo.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получить информацию о странице PDF с помощью Aspose.PDF for Java
Abstract: Узнайте, как извлечь информацию о странице с помощью Aspose.PDF for Java. Пример на Java использует PdfFileInfo для чтения ширины, высоты и поворота первой страницы, чтобы вы могли проверить её макет перед дальнейшей обработкой.
---
## Получите информацию о странице

В этом примере читаются основные геометрические свойства первой страницы.

### Шаги

1. Создайте `PdfFileInfo` объект для исходного PDF.
2. Вызовите `getPageWidth`, `getPageHeight`, и `getPageRotation` для страницы, которую вы хотите проверить.
3. Используйте или выведите полученные значения.
4. Закройте `PdfFileInfo` экземпляр.

### Пример на Java

```java
public static void getPageInformation(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page Width: " + pdfInfo.getPageWidth(1));
    System.out.println("Page Height: " + pdfInfo.getPageHeight(1));
    System.out.println("Page Rotation: " + pdfInfo.getPageRotation(1));
    pdfInfo.close();
}
```


