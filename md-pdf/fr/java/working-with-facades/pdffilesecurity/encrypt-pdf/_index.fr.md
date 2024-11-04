---
title: Crypter un fichier PDF
type: docs
weight: 10
url: /java/encrypt-pdf-file/
description: Ce sujet explique comment crypter un fichier PDF en utilisant la classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Crypter un fichier PDF en utilisant différents types et algorithmes de cryptage

Pour crypter un fichier PDF, vous devez créer un objet [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) puis appeler la méthode [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-). Vous pouvez passer un mot de passe utilisateur, un mot de passe propriétaire et des privilèges à la méthode [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-). Vous devez également passer les valeurs KeySize et Algorithm à cette méthode.

Le code ci-dessous montre comment crypter un fichier PDF.

```java
    public static void EncryptPDFFile() {
        // Créer un objet PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        // Crypter le fichier en utilisant un cryptage 256 bits
        fileSecurity.encryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.getPrint(), KeySize.x256,
                Algorithm.AES);
        fileSecurity.save(_dataDir + "sample_encrypted.pdf");
    }
```