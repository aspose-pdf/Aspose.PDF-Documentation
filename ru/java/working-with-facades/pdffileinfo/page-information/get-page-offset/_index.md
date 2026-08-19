---
title: Получить смещение страницы
linktitle: Получить смещение страницы
type: docs
weight: 20
url: /ru/java/get-page-offset/
description: Узнайте, как проверять смещения X и Y страницы в Java с помощью фасада PdfFileInfo.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получить смещения страниц PDF с использованием Java
Abstract: Узнайте, как получить смещения страниц с помощью Aspose.PDF for Java. Пример на Java использует PdfFileInfo для чтения смещений X и Y страницы 1 и преобразует значения в пунктах в дюймы для более удобного анализа макета.
---
## Получите смещение страницы

Используйте этот рабочий процесс, когда нужно понять, как содержимое страницы расположено относительно начала координат PDF.

### Шаги

1. Создайте `PdfFileInfo` объект для входного PDF.
2. Вызов `getPageXOffset` и `getPageYOffset` для целевой страницы.
3. Преобразуйте значения в пунктах в дюймы, разделив на `72.0`.
4. Используйте или выведите преобразованные значения.
5. Закрыть `PdfFileInfo` экземпляр.

### Пример на Java

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```

