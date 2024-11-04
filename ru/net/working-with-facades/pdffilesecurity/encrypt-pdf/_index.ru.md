---
title: Encrypt PDF File
type: docs
weight: 10
url: /net/encrypt-pdf-file/
description: Эта тема объясняет, как зашифровать PDF файл с использованием класса PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

Шифрование PDF документа защищает его содержимое от несанкционированного доступа извне, особенно при обмене файлами или архивировании.

Конфиденциальные PDF документы могут быть зашифрованы и защищены паролем. Только пользователь, знающий пароль, сможет расшифровать, открыть и просмотреть эти документы.

Давайте рассмотрим, как работает шифрование PDF с библиотекой Aspose.PDF.

## Зашифровать PDF файл с использованием различных типов и алгоритмов шифрования

Чтобы зашифровать PDF файл, необходимо создать объект [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) и затем вызвать метод [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Вы можете передать пароль пользователя, пароль владельца и привилегии в метод [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Также необходимо передать значения KeySize и Algorithm этому методу.

Посмотрите возможный список таких [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm):

|**Имя участника**|**Значение**|**Описание**|
| :- | :- | :- |
|RC4x40|0|RC4 с длиной ключа 40.|
|RC4x128|1|RC4 с длиной ключа 128.|
|AESx128|2|AES с длиной ключа 128.|
|AESx256|3|AES с длиной ключа 256.|

Следующий фрагмент кода показывает, как зашифровать PDF-файл.

```csharp
public static void EncryptPDFFile()
        {
            // Создать объект PdfFileSecurity
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample.pdf");
            // Зашифровать файл с использованием 256-битного шифрования
            fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.Print, KeySize.x256, Algorithm.AES);
            fileSecurity.Save(_dataDir + "sample_encrypted.pdf");
        }
```