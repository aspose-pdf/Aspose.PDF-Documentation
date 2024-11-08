---
title: Управление Исключениями в PDF Файле
type: docs
weight: 30
url: /ru/java/control-exception/
description: Эта тема объясняет, как управлять исключениями в PDF файле с помощью класса PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

Класс [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) позволяет управлять исключениями. Для этого необходимо установить [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) в false или true. Если установить операцию в false, результат [decryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) вернёт true или false в зависимости от правильности пароля.

Если установить [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) в true, тогда вы можете получить результат операции, используя оператор try-catch.

```java
    public static void ControlExceptionPDFFile() {
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
        fileSecurity.setAllowExceptions(false);
        // Расшифровка PDF документа

        if (!fileSecurity.decryptFile("IncorrectPassword")) {
            System.out.println("Что-то пошло не так...");
            System.out.println("Последнее исключение: " + fileSecurity.getLastException().getMessage());
        }
        fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
    }
```