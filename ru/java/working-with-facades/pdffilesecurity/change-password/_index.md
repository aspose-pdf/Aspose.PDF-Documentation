---
title: Сменить пароль PDF‑файла
linktitle: Сменить пароль PDF‑файла
type: docs
weight: 10
url: /ru/java/change-password/
description: Узнайте, как менять пароли PDF в Java с помощью фасада PdfFileSecurity.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Обновите пароли пользователя и владельца PDF в Java
Abstract: Узнайте, как менять пароли PDF с помощью Aspose.PDF for Java. Набор примеров на Java охватывает прямое изменение паролей пользователя и владельца, изменение паролей при сбросе настроек безопасности, а также процесс изменения пароля в стиле try, который возвращает флаг успеха.
---
## Смените пароль PDF‑файла

Использовать `PdfFileSecurity` когда вам необходимо сменить учетные данные в уже защищённом PDF.

### Шаги

1. Создайте `PdfFileSecurity` экземпляр.
2. Привяжите защищённый PDF к `bindPdf`.
3. Вызовите соответствующий `changePassword` перегрузка, в зависимости от того, хотите ли вы также сбросить привилегии и размер ключа.
4. Сохраните обновлённый файл и закройте объект безопасности.

### Примеры на Java

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


