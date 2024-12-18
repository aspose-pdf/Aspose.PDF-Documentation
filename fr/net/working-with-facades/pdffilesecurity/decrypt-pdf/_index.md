---
title: Décrypter un fichier PDF
type: docs
weight: 20
url: /fr/net/decrypt-pdf-file/
description: Ce sujet explique comment décrypter un fichier PDF en utilisant la classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

Un document PDF chiffré avec un mot de passe ou un certificat doit être déverrouillé avant qu'une autre opération puisse être effectuée dessus. Si vous essayez d'opérer sur un document PDF chiffré, vous lancerez une exception. Après avoir déverrouillé un PDF chiffré, vous pouvez effectuer une ou plusieurs opérations dessus.

## Décrypter un fichier PDF en utilisant le mot de passe propriétaire

{{% alert color="primary" %}}
Essayez en ligne <br>
Vous pouvez essayer de déverrouiller le document en utilisant Aspose.PDF et obtenir les résultats en ligne à ce lien :
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

Pour décrypter un fichier PDF, vous devez créer un objet [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) puis appeler la méthode [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). Vous devez également passer le mot de passe propriétaire à la méthode [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). L'extrait de code suivant vous montre comment déchiffrer un fichier PDF.

```csharp
    public static void DecryptPDFFile()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // Créer un objet PdfFileSecurity
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                // Déchiffrer le document PDF
                fileSecurity.DecryptFile("P@ssw0rd");
                fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
            }
        }
```