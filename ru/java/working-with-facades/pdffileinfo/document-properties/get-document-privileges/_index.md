---
title: Получите права доступа к документу
linktitle: Получите права доступа к документу
type: docs
weight: 10
url: /java/get-document-privileges/
description: Узнайте, как проверить права доступа к PDF-документу в Java с помощью фасада PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получите права доступа к PDF-документу с помощью Aspose.PDF для Java
Abstract: Узнайте, как получить права доступа к документу с помощью Aspose.PDF для Java. В примере Java создается объект PdfFileInfo, считываются его настройки DocumentPrivilege и печатаются флаги разрешений для печати, копирования, изменения, аннотаций, заполнения форм, программ чтения с экрана и сборки.
---
## Получите права доступа к документам

Используйте `PdfFileInfo.getDocumentPrivilege()`, чтобы проверить, какие операции разрешены текущим PDF-файлом.

### Шаги

1. Создайте объект `PdfFileInfo` для входного PDF-файла.
2. Позвоните `getDocumentPrivilege()`, чтобы получить набор привилегий.
3. Считайте соответствующие логические флаги из возвращенного объекта `DocumentPrivilege`.
4. По завершении закройте экземпляр `PdfFileInfo`.

### Пример Java

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
