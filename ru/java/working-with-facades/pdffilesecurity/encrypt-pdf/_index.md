---
title: Шифрование PDF файла
type: docs
weight: 10
url: /ru/java/encrypt-pdf-file/
description: Эта тема объясняет, как зашифровать PDF файл с использованием класса PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Шифрование PDF файла с использованием различных типов и алгоритмов шифрования

Для того чтобы зашифровать PDF файл, вам нужно создать объект [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) и затем вызвать метод [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-). Вы можете передать пользовательский пароль, пароль владельца и привилегии методу [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-). Также нужно передать значения KeySize и Algorithm этому методу.

Следующий фрагмент кода показывает, как зашифровать PDF файл.

```java
    public static void EncryptPDFFile() {
        // Создать объект PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        // Зашифровать файл с использованием 256-битного шифрования
        fileSecurity.encryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.getPrint(), KeySize.x256,
                Algorithm.AES);
        fileSecurity.save(_dataDir + "sample_encrypted.pdf");
    }
```