---
title: Cambiar Contraseña de Archivo PDF
type: docs
weight: 40
url: /es/java/change-password/
description: Este tema explica cómo cambiar la contraseña en un archivo PDF usando la clase PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Cambiar Contraseña de un Archivo PDF

Para cambiar la contraseña de un archivo PDF, necesitas crear un objeto [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) y luego llamar al método [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-). Debes pasar la contraseña de propietario existente y las nuevas contraseñas de usuario y propietario al método [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-).

El siguiente fragmento de código te muestra cómo cambiar las contraseñas de un archivo PDF.

```java
    public static void ChangePassword() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // Crear objeto PdfFileSecurity
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.changePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.getPrint(),
                    KeySize.x256);
            fileSecurity.save(_dataDir + "sample_encrtypted1.pdf");
        }
    }
```