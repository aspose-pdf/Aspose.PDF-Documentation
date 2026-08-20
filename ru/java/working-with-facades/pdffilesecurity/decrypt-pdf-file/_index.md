---
title: Расшифровать PDF-файл
linktitle: Расшифровать PDF-файл
type: docs
weight: 20
url: /ru/java/decrypt-pdf-file/
description: Узнайте, как расшифровать PDF в Java с помощью фасада PdfFileSecurity.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Снимите ограничения безопасности PDF с помощью Java.
Abstract: Узнайте, как расшифровать PDF с помощью Aspose.PDF for Java. Набор примеров Java включает прямое расшифрование с использованием пароля владельца и рабочий процесс расшифрования в стиле try, который позволяет обрабатывать ошибки без возбуждения исключения.
---
## Расшифровать PDF-файл

Используйте этот рабочий процесс, когда у вас есть пароль владельца и необходимо снять защиту с PDF.

### Шаги

1. Создайте `PdfFileSecurity` экземпляр.
2. Связать зашифрованный PDF с `bindPdf`.
3. Вызовите `decryptFile` или `tryDecryptFile` с паролем владельца.
4. Сохраните результат, если расшифровка удалась.
5. Закройте объект безопасности.

### Примеры Java

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


