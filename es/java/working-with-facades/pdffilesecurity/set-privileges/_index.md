---
title: Establecer privilegios en un archivo PDF existente
linktitle: Establecer privilegios en un archivo PDF existente
type: docs
weight: 40
url: /java/set-privileges/
description: Aprenda a configurar privilegios de PDF en Java con la fachada PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Administrar permisos de PDF y controles de acceso en Java
Abstract: Aprenda a controlar los permisos de PDF con Aspose.PDF para Java. El conjunto de ejemplos de Java cubre la aplicación de privilegios sin contraseñas, la aplicación de privilegios con contraseñas de usuario y propietario, y un flujo de trabajo de actualización de privilegios estilo prueba que devuelve un indicador de éxito.
---
## Establecer privilegios en un archivo PDF existente



Utilice este flujo de trabajo cuando necesite cambiar lo que los usuarios pueden hacer con un PDF existente.


### 
Pasos


1. 
Cree una instancia `PdfFileSecurity`.

2. 
Vincule el PDF de origen con `bindPdf`.
3. Cree un objeto `DocumentPrivilege` y configure las acciones permitidas.

4. 
Llame a la sobrecarga `setPrivilege` o `trySetPrivilege` apropiada.

5. 
Guarde el resultado si la actualización se realiza correctamente y luego cierre el objeto.


### 
Ejemplos de Java

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
