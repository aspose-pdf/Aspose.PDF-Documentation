---
title: Получить смещение страницы
linktitle: Получить смещение страницы
type: docs
weight: 20
url: /java/get-page-offset/
description: Узнайте, как проверять смещения страниц X и Y в Java с помощью фасада PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получить смещения страниц PDF с помощью Java
Abstract: Узнайте, как получить смещения страниц с помощью Aspose.PDF для Java. В примере Java PdfFileInfo используется для считывания смещений X и Y страницы 1 и преобразует значения точек в дюймы для упрощения анализа макета.
---
## Получите смещение страницы

Используйте этот рабочий процесс, когда вам нужно понять, как содержимое страницы позиционируется относительно источника PDF.

### Шаги

1. Создайте объект `PdfFileInfo` для входного PDF-файла.
2. Вызовите `getPageXOffset` и `getPageYOffset` для целевой страницы.
3. Преобразуйте значения точек в дюймы, разделив их на `72.0`.
4. Используйте или распечатайте преобразованные значения.
5. Закройте экземпляр `PdfFileInfo`.

### Пример Java

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
