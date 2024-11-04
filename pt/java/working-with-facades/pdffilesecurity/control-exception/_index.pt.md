---
title: Controlar Exceção em Arquivo PDF
type: docs
weight: 30
url: /java/control-exception/
description: Este tópico explica como controlar exceções em Arquivo PDF usando a Classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

A classe [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) permite controlar exceções. Para fazer isso, você precisa definir [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) como falso ou verdadeiro. Se você definir a operação como falsa, o resultado de [decryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) retornará verdadeiro ou falso dependendo da correção da senha.

Se você definir [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) como verdadeiro, então você pode obter o resultado da operação usando o operador try-catch.

```java
    public static void ControlExceptionPDFFile() {
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
        fileSecurity.setAllowExceptions(false);
        // Descriptografar documento PDF

        if (!fileSecurity.decryptFile("IncorrectPassword")) {
            System.out.println("Algo errado...");
            System.out.println("Última exceção: " + fileSecurity.getLastException().getMessage());
        }
        fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
    }
```