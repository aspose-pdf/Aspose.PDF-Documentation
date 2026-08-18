---
title: Получить PDF-версию
linktitle: Получить PDF-версию
type: docs
weight: 20
url: /java/get-pdf-version/
description: Узнайте, как получить версию PDF-документа на Java с помощью фасада PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получить версию PDF с помощью Aspose.PDF для Java
Abstract: Узнайте, как получить версию PDF с помощью Aspose.PDF для Java. В примере Java создается объект PdfFileInfo, считывает строку версии с помощью `getPdfVersion()`, печатает результат и закрывает объект информации о файле.
---
## Получите PDF-версию

Используйте этот рабочий процесс, когда вам нужно проверить совместимость файлов или направить документ через логику обработки, зависящую от версии.

### Шаги

1. Создайте объект `PdfFileInfo` для файла PDF.
2. Позвоните `getPdfVersion()`, чтобы получить версию, о которой сообщается.
3. Используйте или распечатайте значение версии.
4. Закройте экземпляр `PdfFileInfo`.

### Пример Java

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
