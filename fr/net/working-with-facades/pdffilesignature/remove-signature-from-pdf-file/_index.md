---
title: Supprimer la Signature d'un Fichier PDF
type: docs
weight: 20
url: fr/net/remove-signature-from-pdf/
description: Cette section explique comment supprimer la signature d'un fichier PDF en utilisant la classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Supprimer la Signature Numérique du Fichier PDF

Lorsqu'une signature a été ajoutée à un fichier PDF, il est possible de la supprimer. Vous pouvez supprimer soit une signature particulière, soit toutes les signatures d'un fichier. La méthode la plus rapide pour supprimer la signature supprime également le champ de signature, mais il est possible de simplement retirer la signature, en conservant le champ de signature afin que le fichier puisse être signé à nouveau.

La méthode RemoveSignature de la classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) vous permet de supprimer une signature d'un fichier PDF. Ce document prend le nom de la signature comme entrée. Soit spécifiez directement le nom de la signature, pour supprimer toutes les signatures, obtenez les noms des signatures en utilisant la méthode [GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername).

L'extrait de code suivant montre comment supprimer la signature numérique du fichier PDF.

```csharp
 public static void RemoveSignature()
        {
            // Créer un objet PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();
            // Ouvrir le document PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            // Obtenir la liste des noms de signature
            var sigNames = pdfSign.GetSignNames();
            // Supprimer toutes les signatures du fichier PDF
            for (int index = 0; index < sigNames.Count; index++)
            {
                Console.WriteLine($"Removed {sigNames[index]}");
                pdfSign.RemoveSignature(sigNames[index]);
            }
            // Enregistrer le fichier PDF mis à jour
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```
### Supprimer la signature mais conserver le champ de signature

Comme indiqué ci-dessus, la méthode [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) de la classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) vous permet de supprimer les champs de signature des fichiers PDF. Lors de l'utilisation de cette méthode avec des versions antérieures à la 9.3.0, à la fois la signature et le champ de signature sont supprimés. Certains développeurs souhaitent supprimer uniquement la signature et conserver le champ de signature afin qu'il puisse être utilisé pour re-signer le document. Pour conserver le champ de signature et supprimer uniquement la signature, veuillez utiliser l'extrait de code suivant.

```csharp
public static void RemoveSignatureButKeepField()
        {
            // Créer un objet PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Ouvrir le document PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            pdfSign.RemoveSignature("Signature1", false);

            // Enregistrer le fichier PDF mis à jour
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```

Le texte suivant montre comment supprimer toutes les signatures des champs.

```csharp
public static void RemoveSignatureButKeepField2()
        {
            // Créer un objet PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Ouvrir le document PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            var sigNames = pdfSign.GetSignNames();
            foreach (var sigName in sigNames)
            {
                pdfSign.RemoveSignature(sigName, false);
            }

            // Enregistrer le fichier PDF mis à jour
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }

```