---
title: Расшифровать PDF файл
type: docs
weight: 20
url: ru/java/decrypt-pdf-file/
description: Эта тема объясняет, как расшифровать PDF файл с использованием класса PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Расшифровать PDF файл с использованием пароля владельца

{{% alert color="primary" %}}
Попробуйте онлайн <br>
Вы можете попробовать разблокировать документ с использованием Aspose.PDF и получить результаты онлайн по этой ссылке:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

Для того чтобы расшифровать PDF файл, вам нужно создать объект [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) и затем вызвать метод [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-). Вам также нужно передать пароль владельца в метод [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-). Следующий фрагмент кода показывает, как расшифровать PDF файл.

```java
    public static void DecryptPDFFile() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // Создать объект PdfFileSecurity
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            // Расшифровать PDF документ
            fileSecurity.decryptFile("User_P@ssw0rd");
            fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
        }
    }
```