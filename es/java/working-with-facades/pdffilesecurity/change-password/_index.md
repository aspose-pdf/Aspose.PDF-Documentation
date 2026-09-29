---
title: Cambiar la contraseña del archivo PDF
linktitle: Cambiar la contraseña del archivo PDF
type: docs
weight: 10
url: /es/java/change-password/
description: Aprenda cómo cambiar contraseñas PDF en Java con la fachada PdfFileSecurity.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Actualizar contraseñas de usuario y propietario del PDF en Java
Abstract: Aprenda cómo cambiar contraseñas PDF con Aspose.PDF for Java. El conjunto de ejemplos Java cubre cambiar contraseñas de usuario y propietario directamente, cambiar contraseñas mientras se restablecen la configuración de seguridad y un flujo de trabajo de cambio de contraseña al estilo try que devuelve una bandera de éxito.
---
## Cambiar la contraseña del archivo PDF

Utilice `PdfFileSecurity` cuando necesita rotar credenciales en un PDF ya asegurado.

### Pasos

1. Cree una instancia de `PdfFileSecurity`.
2. Vincule el PDF seguro con `bindPdf`.
3. Llame al apropiado `changePassword` sobrecargar, dependiendo de si también desea restablecer los privilegios y el tamaño de la clave.
4. Guarde el archivo actualizado y cierre el objeto de seguridad.

### Ejemplos de Java

```java
public static void changeUserAndOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void changePasswordAndResetSecurity(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryChangePasswordWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryChangePassword("owner_password", "new_user_password", "new_owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Password change failed. Check owner password or document security.");
    }
    fileSecurity.close();
}
```
