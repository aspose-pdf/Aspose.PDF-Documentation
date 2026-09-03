---
title: Establecer privilegios en un archivo PDF existente
linktitle: Establecer privilegios en un archivo PDF existente
type: docs
weight: 40
url: /es/java/set-privileges/
description: Aprenda cómo establecer privilegios PDF en Java con la fachada PdfFileSecurity.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Administre permisos PDF y controles de acceso en Java
Abstract: Aprenda cómo controlar los permisos PDF con Aspose.PDF for Java. El conjunto de ejemplos Java cubre la aplicación de privilegios sin contraseñas, la aplicación de privilegios con contraseñas de usuario y propietario, y un flujo de trabajo de actualización de privilegios al estilo try que devuelve una bandera de éxito.
---
## Establecer privilegios en un archivo PDF existente

Utilice este flujo de trabajo cuando necesite cambiar lo que los usuarios pueden hacer con un PDF existente.

### Pasos

1. Crear un `PdfFileSecurity` instancia.
2. Vincular el PDF de origen con `bindPdf`.
3. Crear un `DocumentPrivilege` objeto y configurar las acciones permitidas.
4. Llame al apropiado `setPrivilege` o `trySetPrivilege` sobrecargar.
5. Guardar el resultado si la actualización tiene éxito, luego cerrar el objeto.

### Ejemplos de Java

```java
public static void setPdfPrivilegesWithoutPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.setPrivilege(privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void setPdfPrivilegesWithPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    privilege.setAllowCopy(false);
    fileSecurity.setPrivilege("user_password", "owner_password", privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void trySetPdfPrivilegesWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    if (fileSecurity.trySetPrivilege("user_password", "owner_password", privilege)) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Setting privileges failed. Check passwords or document state.");
    }
    fileSecurity.close();
}
```
