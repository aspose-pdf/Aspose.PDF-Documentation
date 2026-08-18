---
title: Получить информацию о странице
linktitle: Получить информацию о странице
type: docs
weight: 10
url: /java/get-page-info/
description: Узнайте, как проверить ширину, высоту и поворот страницы в Java с помощью фасада PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получите информацию о странице PDF с помощью Aspose.PDF для Java
Abstract: Узнайте, как получить информацию о странице с помощью Aspose.PDF для Java. В примере Java используется PdfFileInfo для считывания ширины, высоты и поворота страницы 1, чтобы вы могли проверить ее макет перед дальнейшей обработкой.
---
## Получите информацию о странице

В этом примере считываются основные геометрические свойства страницы 1.

### Шаги

1. Создайте объект `PdfFileInfo` для исходного PDF-файла.
2. Позвоните `getPageWidth`, `getPageHeight` и `getPageRotation`, чтобы узнать страницу, которую вы хотите проверить.
3. Используйте или распечатайте возвращенные значения.
4. Закройте экземпляр `PdfFileInfo`.

### Пример Java

```java
public static void getPageInformation(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page Width: " + pdfInfo.getPageWidth(1));
    System.out.println("Page Height: " + pdfInfo.getPageHeight(1));
    System.out.println("Page Rotation: " + pdfInfo.getPageRotation(1));
    pdfInfo.close();
}
```
