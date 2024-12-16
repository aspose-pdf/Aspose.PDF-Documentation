---
title: Changer le mot de passe d'un fichier PDF
type: docs
weight: 40
url: /fr/java/change-password/
description: Ce sujet explique comment changer le mot de passe d'un fichier PDF en utilisant la classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Changer le mot de passe d'un fichier PDF

Pour changer le mot de passe d'un fichier PDF, vous devez créer un objet [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) puis appeler la méthode [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-). Vous devez passer l'ancien mot de passe propriétaire et les nouveaux mots de passe utilisateur et propriétaire à la méthode [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-).

Le code suivant vous montre comment changer les mots de passe d'un fichier PDF.

```java
    public static void ChangePassword() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // Créer un objet PdfFileSecurity
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.changePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.getPrint(),
                    KeySize.x256);
            fileSecurity.save(_dataDir + "sample_encrtypted1.pdf");
        }
    }
```