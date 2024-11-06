---
title: Controlar Excepción de Archivo PDF
type: docs
weight: 30
url: es/java/control-exception/
description: Este tema explica cómo controlar la excepción en un archivo PDF utilizando la clase PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

La clase [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) te permite controlar excepciones. Para hacer esto, necesitas establecer [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) a false o true. Si estableces la operación en false, el resultado de [decryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) devolverá true o false dependiendo de la corrección de la contraseña.

Si estableces [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) a true, entonces puedes obtener el resultado de la operación usando el operador try-catch.

```java
    public static void ControlarExcepcionArchivoPDF() {
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
        fileSecurity.setAllowExceptions(false);
        // Desencriptar documento PDF

        if (!fileSecurity.decryptFile("IncorrectPassword")) {
            System.out.println("Algo salió mal...");
            System.out.println("Última excepción: " + fileSecurity.getLastException().getMessage());
        }
        fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
    }
```