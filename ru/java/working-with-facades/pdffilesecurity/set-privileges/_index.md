---
title: Установите права доступа к существующему PDF-файлу
linktitle: Установите права доступа к существующему PDF-файлу
type: docs
weight: 40
url: /java/set-privileges/
description: Узнайте, как установить права PDF в Java с помощью фасада PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Управление разрешениями PDF и контролем доступа в Java
Abstract: Узнайте, как контролировать разрешения PDF с помощью Aspose.PDF для Java. Набор примеров Java охватывает применение привилегий без паролей, применение привилегий с паролями пользователя и владельца, а также рабочий процесс обновления привилегий в стиле try, который возвращает флаг успеха.
---
## Установите права доступа к существующему PDF-файлу

Используйте этот рабочий процесс, когда вам нужно изменить действия пользователей с существующим PDF-файлом.

### Шаги

1. Создайте экземпляр `PdfFileSecurity`.
2. Свяжите исходный PDF-файл с помощью `bindPdf`.
3. Создайте объект `DocumentPrivilege` и настройте разрешенные действия.
4. Вызовите соответствующую перегрузку `setPrivilege` или `trySetPrivilege`.
5. Сохраните результат, если обновление пройдет успешно, затем закройте объект.

### Примеры Java

```java
public static void setPdfPrivilegesWithoutPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.setPrivilege(privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void setPdfPrivilegesWithPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    privilege.setAllowCopy(false);
    fileSecurity.setPrivilege("user_password", "owner_password", privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void trySetPdfPrivilegesWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    if (fileSecurity.trySetPrivilege("user_password", "owner_password", privilege)) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Setting privileges failed. Check passwords or document state.");
    }
    fileSecurity.close();
}
```
