---
title: Contrôler les Exceptions du Fichier PDF
type: docs
weight: 30
url: /java/control-exception/
description: Ce sujet explique comment contrôler les exceptions sur le fichier PDF en utilisant la classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

La classe [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) vous permet de contrôler les exceptions. Pour ce faire, vous devez définir [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) sur false ou true. Si vous définissez l'opération sur false, le résultat de [decryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) renverra true ou false selon l'exactitude du mot de passe.

Si vous définissez [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) sur true, alors vous pouvez obtenir le résultat de l'opération en utilisant l'opérateur try-catch.

```java
    public static void ControlExceptionPDFFile() {
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
        fileSecurity.setAllowExceptions(false);
        // Déchiffrer le document PDF

        if (!fileSecurity.decryptFile("IncorrectPassword")) {
            System.out.println("Quelque chose ne va pas...");
            System.out.println("Dernière exception : " + fileSecurity.getLastException().getMessage());
        }
        fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
    }
```