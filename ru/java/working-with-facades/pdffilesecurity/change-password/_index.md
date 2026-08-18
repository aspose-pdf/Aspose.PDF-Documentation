---
title: Изменить пароль PDF-файла
linktitle: Изменить пароль PDF-файла
type: docs
weight: 10
url: /java/change-password/
description: Узнайте, как изменить пароли PDF в Java с помощью фасада PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Обновление паролей пользователя и владельца PDF в Java
Abstract: Узнайте, как изменить пароли PDF с помощью Aspose.PDF для Java. Набор примеров Java охватывает непосредственное изменение паролей пользователя и владельца, изменение паролей при сбросе настроек безопасности, а также рабочий процесс смены пароля в пробном стиле, который возвращает флаг успеха.
---
## Изменить пароль PDF-файла

Используйте `PdfFileSecurity`, когда вам нужно сменить учетные данные в уже защищенном PDF-файле.

### Шаги

1. Создайте экземпляр `PdfFileSecurity`.
2. Свяжите защищенный PDF-файл с помощью `bindPdf`.
3. Вызовите соответствующую перегрузку `changePassword`, в зависимости от того, хотите ли вы также сбросить привилегии и размер ключа.
4. Сохраните обновленный файл и закройте объект безопасности.

### Примеры Java

```java
public static void changeUserAndOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void changePasswordAndResetSecurity(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryChangePasswordWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryChangePassword("owner_password", "new_user_password", "new_owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Password change failed. Check owner password or document security.");
    }
    fileSecurity.close();
}
```
