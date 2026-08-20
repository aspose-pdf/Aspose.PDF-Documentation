---
title: Получить привилегии документа
linktitle: Получить привилегии документа
type: docs
weight: 10
url: /ru/java/get-document-privileges/
description: Узнайте, как проверять привилегии PDF‑документа в Java с помощью фасада PdfFileInfo.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получение привилегий PDF‑документа с помощью Aspose.PDF for Java
Abstract: Узнайте, как получать привилегии документа с помощью Aspose.PDF for Java. Пример на Java создает объект PdfFileInfo, читает его настройки DocumentPrivilege и выводит флаги разрешений для печати, копирования, изменения, аннотаций, заполнения форм, экранных чтений и сборки.
---
## Получите привилегии документа

Использовать `PdfFileInfo.getDocumentPrivilege()` чтобы проверить, какие операции разрешены текущим PDF.

### Шаги

1. Создайте `PdfFileInfo` объект для входного PDF.
2. Вызовите `getDocumentPrivilege()` для получения набора привилегий.
3. Прочитайте соответствующие булевы флаги из возвращённого `DocumentPrivilege` объект.
4. Закройте `PdfFileInfo` экземпляр после завершения.

### Пример на Java

```java
public static void getDocumentPrivileges(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    DocumentPrivilege privileges = pdfInfo.getDocumentPrivilege();

    System.out.println("Document Privileges:");
    System.out.println("  Can Print: " + privileges.isAllowPrint());
    System.out.println("  Can Degraded Print: " + privileges.isAllowDegradedPrinting());
    System.out.println("  Can Copy: " + privileges.isAllowCopy());
    System.out.println("  Can Modify Contents: " + privileges.isAllowModifyContents());
    System.out.println("  Can Modify Annotations: " + privileges.isAllowModifyAnnotations());
    System.out.println("  Can Fill In: " + privileges.isAllowFillIn());
    System.out.println("  Can Screen Readers: " + privileges.isAllowScreenReaders());
    System.out.println("  Can Assembly: " + privileges.isAllowAssembly());
    pdfInfo.close();
}
```


