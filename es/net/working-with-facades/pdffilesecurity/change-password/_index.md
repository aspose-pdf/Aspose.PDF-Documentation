---
title: Cambiar Contraseña de Archivo PDF
type: docs
weight: 40
url: es/net/change-password/
description: Este tema explica cómo cambiar la contraseña en un archivo PDF utilizando la clase PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Cambiar Contraseña de un Archivo PDF

Para cambiar la contraseña de un archivo PDF, necesitas crear un objeto [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) y luego llamar al método [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2). Necesitas pasar la contraseña de propietario existente y las nuevas contraseñas de usuario y propietario al método [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2).

{{% alert color="primary" %}}

- La **contraseña de usuario**, si está establecida, es lo que necesitas proporcionar para abrir un PDF. Acrobat/Reader solicitará al usuario que ingrese la contraseña de usuario. Si no es correcta, el documento no se abrirá.
- La **contraseña de propietario**, si está establecida, controla los permisos, como impresión, edición, extracción, comentario, etc. Acrobat/Reader deshabilitará estas cosas según la configuración de permisos. Acrobat requerirá esta contraseña si desea establecer/cambiar permisos.

{{% /alert %}}

El siguiente fragmento de código le muestra cómo cambiar las contraseñas de un archivo PDF.

```csharp
public static void ChangePassword()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // Crear objeto PdfFileSecurity
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.Print, KeySize.x256);
                fileSecurity.Save(_dataDir + "sample_encrtypted1.pdf");
            }
        }
```