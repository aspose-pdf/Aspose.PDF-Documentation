---
title: Расшифровка PDF-файла
linktitle: Расшифровка PDF-файла
type: docs
weight: 20
url: /ru/java/decrypt-pdf-file/
description: Узнайте, как расшифровать PDF в Java с помощью фасада PdfFileSecurity.
lastmod: "2026-09-17"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Снимите ограничения безопасности PDF с помощью Java.
Abstract: Узнайте, как расшифровать PDF с помощью Aspose.PDF for Java. Набор примеров Java включает прямое расшифрование с использованием пароля владельца и рабочий процесс расшифрования в стиле try, который позволяет обрабатывать ошибки без возбуждения исключения.
---
## Расшифровка PDF-файла

Используйте этот рабочий процесс, когда у вас есть пароль владельца и необходимо снять защиту с PDF.

### Шаги

1. Создайте экземпляр `PdfFileSecurity`.
2. Привяжите зашифрованный PDF с помощью `bindPdf`.
3. Вызовите `decryptFile` или `tryDecryptFile` с паролем владельца.
4. Сохраните результат, если расшифровка удалась.
5. Закройте объект безопасности.

### Примеры на Java

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryDecryptPdfWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryDecryptFile("owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Decryption failed. Check password or document security.");
    }
    fileSecurity.close();
}
```


