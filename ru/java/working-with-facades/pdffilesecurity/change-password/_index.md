---
title: Изменение пароля PDF файла
type: docs
weight: 40
url: /ru/java/change-password/
description: Эта тема объясняет, как изменить пароль в PDF файле с использованием класса PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Изменение пароля PDF файла

Для того чтобы изменить пароль PDF файла, вам необходимо создать объект [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) и затем вызвать метод [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-). Вам нужно передать существующий пароль владельца и новые пользовательский и владелецкий пароли в метод [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-).

Следующий фрагмент кода показывает, как изменить пароли PDF файла.

```java
    public static void ChangePassword() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // Создание объекта PdfFileSecurity
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.changePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.getPrint(),
                    KeySize.x256);
            fileSecurity.save(_dataDir + "sample_encrtypted1.pdf");
        }
    }
```