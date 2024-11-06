---
title: Decrypt PDF File
type: docs
weight: 20
url: ru/net/decrypt-pdf-file/
description: Эта тема объясняет, как расшифровать PDF файл с использованием класса PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

PDF документ, зашифрованный паролем или сертификатом, должен быть разблокирован перед выполнением другой операции. Если вы попытаетесь выполнить операцию на зашифрованном PDF документе, будет выброшено исключение. После разблокировки зашифрованного PDF вы можете выполнить одну или несколько операций над ним.

## Расшифровать PDF файл с использованием пароля владельца

{{% alert color="primary" %}}
Попробуйте онлайн <br>
Вы можете попробовать разблокировать документ с помощью Aspose.PDF и получить результаты онлайн по этой ссылке:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

Для того чтобы расшифровать PDF файл, вам нужно создать объект [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) и затем вызвать метод [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). Вам также необходимо передать пароль владельца методу [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). Следующий фрагмент кода показывает, как расшифровать PDF файл.

```csharp
    public static void DecryptPDFFile()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // Создать объект PdfFileSecurity
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                // Расшифровать PDF документ
                fileSecurity.DecryptFile("P@ssw0rd");
                fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
            }
        }
```