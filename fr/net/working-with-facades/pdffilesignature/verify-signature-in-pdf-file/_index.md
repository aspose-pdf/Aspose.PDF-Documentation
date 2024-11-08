---
title: Vérifier la Signature dans un Fichier PDF
type: docs
weight: 30
url: /fr/net/verify-signature-in-pdf/
description: Cette section explique comment vérifier la signature dans un fichier PDF en utilisant la classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Vérifier si le Fichier PDF est Signé en Utilisant une Signature

Pour vérifier si un fichier PDF est signé en utilisant une [signature particulière](/pdf/fr/net/working-with-signature-in-a-pdf-file/), utilisez la méthode VerifySigned de la classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Cette méthode nécessite le nom de la signature et retourne vrai si le PDF est signé avec ce nom de signature. Il est également possible de vérifier qu'un [PDF est signé](/pdf/fr/net/working-with-signature-in-a-pdf-file/), sans vérifier avec quelle signature il est signé.

### Vérification qu'un PDF est Signé avec une Signature Donnée

L'extrait de code suivant vous montre comment vérifier si un PDF est signé en utilisant une signature donnée.

```csharp
public static void IsPdfSigned()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.ContainsSignature())
                Console.WriteLine("Document Signed");
            pdfSign.Close();
        }
```

### Vérification qu'un PDF est signé

Pour déterminer si un fichier est signé, sans fournir le nom de la signature, utilisez le code suivant.

```csharp
 public static void IsPdfSignedWithGivenSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySigned("Signature1"))
            {
                Console.WriteLine("PDF Signed");
            }
            //if (pdfSign.VerifySigned("Signature2"))
            //{
            //    Console.WriteLine("PDF Signed");
            //}
        }
```

## Vérifier si la signature est valide

La méthode [VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) de la classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) vous permet de valider une signature particulière. Cette méthode nécessite le nom de la signature en entrée et renvoie vrai si la signature est valide. Le fragment de code suivant vous montre comment valider une signature.

```csharp
public static void IsPdfSignatureValid()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySignature("Signature1"))
            {
                Console.WriteLine("Signature Verified");
            }
        }
```