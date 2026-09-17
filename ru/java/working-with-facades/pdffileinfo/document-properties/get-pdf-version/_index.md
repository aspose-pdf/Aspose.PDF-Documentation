---
title: Получение версии PDF
linktitle: Получение версии PDF
type: docs
weight: 20
url: /ru/java/get-pdf-version/
description: Узнайте, как получить версию PDF‑документа в Java с помощью фасада PdfFileInfo.
lastmod: "2026-09-17"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получить версию PDF с помощью Aspose.PDF for Java
Abstract: Узнайте, как получить версию PDF с помощью Aspose.PDF for Java. Пример на Java создает объект PdfFileInfo, считывает строку версии с помощью `getPdfVersion()`, выводит результат и закрывает объект информации о файле.
---
## Получение версии PDF

Используйте этот рабочий процесс, когда необходимо проверить совместимость файла или направить документ через процессинг, зависящий от конкретной версии.

### Шаги

1. Создайте объект `PdfFileInfo` для PDF‑файла.
2. Вызовите `getPdfVersion()` для получения сообщённой версии.
3. Используйте или выведите значение версии.
4. Закройте экземпляр `PdfFileInfo`.

### Пример на Java

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```


