---
title: Cambiar contraseña del archivo PDF
linktitle: Cambiar contraseña del archivo PDF
type: docs
weight: 10
url: /java/change-password/
description: Aprenda a cambiar contraseñas de PDF en Java con la fachada PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Actualizar contraseñas de usuario y propietario de PDF en Java
Abstract: Aprenda a cambiar contraseñas de PDF con Aspose.PDF para Java. El conjunto de ejemplos de Java cubre el cambio de contraseñas de usuario y propietario directamente, el cambio de contraseñas mientras se restablece la configuración de seguridad y un flujo de trabajo de cambio de contraseña de estilo de prueba que devuelve un indicador de éxito.
---
## Cambiar contraseña del archivo PDF



Utilice `PdfFileSecurity` cuando necesite rotar credenciales en un PDF ya protegido.


### 
Pasos


1. Cree una instancia `PdfFileSecurity`.

2. Enlaza el PDF protegido con `bindPdf`.
3. Llame a la sobrecarga `changePassword` adecuada, dependiendo de si también desea restablecer los privilegios y el tamaño de la clave.

4. Guarde el archivo actualizado y cierre el objeto de seguridad.


### 
Ejemplos de Java

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
