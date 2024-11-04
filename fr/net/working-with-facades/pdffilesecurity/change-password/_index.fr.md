---
title: Changer le mot de passe du fichier PDF
type: docs
weight: 40
url: /net/change-password/
description: Ce sujet explique comment changer le mot de passe sur un fichier PDF en utilisant la classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Changer le mot de passe d'un fichier PDF

Pour changer le mot de passe d'un fichier PDF, vous devez créer un objet [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) et ensuite appeler la méthode [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2). Vous devez passer l'ancien mot de passe propriétaire et les nouveaux mots de passe utilisateur et propriétaire à la méthode [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2).

{{% alert color="primary" %}}

- Le **mot de passe utilisateur**, s'il est défini, est ce que vous devez fournir pour ouvrir un PDF. Acrobat/Reader demandera à un utilisateur de saisir le mot de passe utilisateur. S'il n'est pas correct, le document ne s'ouvrira pas.
- Le **mot de passe propriétaire**, s'il est défini, contrôle les autorisations, telles que l'impression, la modification, l'extraction, les commentaires, etc. Acrobat/Reader interdira ces actions en fonction des paramètres d'autorisation. Acrobat demandera ce mot de passe si vous souhaitez définir/modifier les autorisations.

{{% /alert %}}

L'extrait de code suivant vous montre comment changer les mots de passe d'un fichier PDF.

```csharp
public static void ChangePassword()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // Create PdfFileSecurity object
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.Print, KeySize.x256);
                fileSecurity.Save(_dataDir + "sample_encrtypted1.pdf");
            }
        }
```