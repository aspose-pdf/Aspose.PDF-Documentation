---
title: Установить привилегии для существующего PDF-файла
linktitle: Установить привилегии для существующего PDF-файла
type: docs
weight: 40
url: /ru/java/set-privileges/
description: Узнайте, как установить привилегии PDF в Java с помощью фасада PdfFileSecurity.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Управляйте разрешениями PDF и контролем доступа в Java
Abstract: Узнайте, как контролировать разрешения PDF с помощью Aspose.PDF for Java. Набор примеров на Java охватывает применение привилегий без паролей, применение привилегий с паролями пользователя и владельца, а также рабочий процесс обновления привилегий в стиле try, который возвращает флаг успеха.
---
## Установите привилегии для существующего PDF-файла

Используйте этот рабочий процесс, когда необходимо изменить, что пользователи могут делать с существующим PDF.

### Шаги

1. Создайте `PdfFileSecurity` экземпляр.
2. Свяжите исходный PDF с `bindPdf`.
3. Создайте `DocumentPrivilege` объект и настройте разрешённые действия.
4. Вызовите соответствующий `setPrivilege` или `trySetPrivilege` перегрузка.
5. Сохраните результат, если обновление удалось, затем закройте объект.

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


