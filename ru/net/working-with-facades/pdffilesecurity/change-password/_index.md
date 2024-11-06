---
title: Изменение пароля PDF файла
type: docs
weight: 40
url: ru/net/change-password/
description: Эта тема объясняет, как изменить пароль в PDF файле с использованием класса PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Изменение пароля PDF файла

Для того чтобы изменить пароль PDF файла, необходимо создать объект [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) и затем вызвать метод [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2). Вам нужно передать существующий пароль владельца и новые пароли пользователя и владельца в метод [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2).

{{% alert color="primary" %}}

- **Пароль пользователя**, если установлен, необходимо ввести для открытия PDF. Acrobat/Reader предложит пользователю ввести пароль пользователя. Если он неверный, документ не откроется.
- **Пароль владельца**, если установлен, контролирует разрешения, такие как печать, редактирование, извлечение, комментирование и т.д. Acrobat/Reader будет запрещать эти действия на основе настроек разрешений. Acrobat потребует этот пароль, если вы хотите установить/изменить разрешения.

{{% /alert %}}

Следующий фрагмент кода показывает, как изменить пароли PDF-файла.

```csharp
public static void ChangePassword()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // Создать объект PdfFileSecurity
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.Print, KeySize.x256);
                fileSecurity.Save(_dataDir + "sample_encrtypted1.pdf");
            }
        }
```