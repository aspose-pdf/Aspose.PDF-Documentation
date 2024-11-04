---
title: Establecer Privilegios en un Archivo PDF Existente
type: docs
weight: 50
url: /java/set-privileges/
description: Este tema explica cómo establecer privilegios en un archivo PDF existente utilizando la Clase PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Establecer Privilegios en un Archivo PDF Existente (facades)

Para establecer los privilegios de un archivo PDF, cree un objeto de la clase [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) y vincule el PDF de entrada usando el método bindPdf. Luego, debe llamar al método setPrivilege para establecer los privilegios. Puede especificar los privilegios utilizando el objeto [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/DocumentPrivilege) y luego pasar este objeto al método setPrivilege y guardar el PDF de salida utilizando el método save.

El siguiente fragmento de código le muestra cómo establecer los privilegios de un archivo PDF.

```java
public static void SetPrivilege1() {
        // Crear objeto DocumentPrivileges
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // Crear objeto PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege(privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```


Vea el siguiente método especificando una contraseña:

```java
 public static void SetPrivilege2() {
        // Crear objeto DocumentPrivileges
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // Crear objeto PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege("", "P@ssw0rd", privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```