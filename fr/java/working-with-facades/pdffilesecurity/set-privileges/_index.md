---
title: Définir des Privilèges sur un Fichier PDF Existant
type: docs
weight: 50
url: /fr/java/set-privileges/
description: Ce sujet explique comment définir des privilèges sur un fichier PDF existant en utilisant la classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Définir des Privilèges sur un Fichier PDF Existant (facades)

Pour définir les privilèges d'un fichier PDF, créez un objet de classe [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) et liez le PDF d'entrée à l'aide de la méthode bindPdf. Ensuite, vous devez appeler la méthode setPrivilege pour définir les privilèges. Vous pouvez spécifier les privilèges en utilisant l'objet [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/DocumentPrivilege) puis passer cet objet à la méthode setPrivilege et enregistrer le PDF de sortie en utilisant la méthode save.

Le code suivant vous montre comment définir les privilèges d'un fichier PDF.

```java
public static void SetPrivilege1() {
        // Créer un objet DocumentPrivileges
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // Créer un objet PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege(privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```


Voir la méthode suivante avec spécification d'un mot de passe :

```java
 public static void SetPrivilege2() {
        // Créer un objet DocumentPrivileges
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // Créer un objet PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege("", "P@ssw0rd", privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```