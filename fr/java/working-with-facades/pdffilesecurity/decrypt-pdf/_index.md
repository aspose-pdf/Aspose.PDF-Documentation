---
title: Décrypter un fichier PDF
type: docs
weight: 20
url: fr/java/decrypt-pdf-file/
description: Ce sujet explique comment décrypter un fichier PDF en utilisant la classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Décrypter un fichier PDF en utilisant le mot de passe propriétaire

{{% alert color="primary" %}}
Essayez en ligne <br>
Vous pouvez essayer de déverrouiller le document en utilisant Aspose.PDF et obtenir les résultats en ligne à ce lien :
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

Pour décrypter un fichier PDF, vous devez créer un objet [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) puis appeler la méthode [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-). Vous devez également passer le mot de passe propriétaire à la méthode [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-). Le code suivant montre comment décrypter un fichier PDF.

```java
    public static void DecryptPDFFile() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // Créer un objet PdfFileSecurity
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            // Décrypter le document PDF
            fileSecurity.decryptFile("User_P@ssw0rd");
            fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
        }
    }
```