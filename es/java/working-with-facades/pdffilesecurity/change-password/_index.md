---
title: Cambiar contraseña del archivo PDF
linktitle: Cambiar contraseña del archivo PDF
type: docs
weight: 10
url: /es/java/change-password/
description: Aprenda cómo cambiar las contraseñas de PDF en Java con la fachada PdfFileSecurity.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Actualice las contraseñas de usuario y propietario de PDF en Java
Abstract: Aprenda cómo cambiar las contraseñas de PDF con Aspose.PDF for Java. El conjunto de ejemplos de Java cubre el cambio directo de contraseñas de usuario y propietario, el cambio de contraseñas mientras se restablecen los ajustes de seguridad, y un flujo de trabajo de cambio de contraseña estilo try que devuelve una bandera de éxito.
---
## Cambiar contraseña del archivo PDF

Usar `PdfFileSecurity` cuando necesitas rotar credenciales en un PDF ya asegurado.

### Pasos

1. Crear un `PdfFileSecurity` instancia.
2. Vincular el PDF seguro con `bindPdf`.
3. Llame al apropiado `changePassword` sobrecargar, dependiendo de si también deseas restablecer los privilegios y el tamaño de la clave.
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
