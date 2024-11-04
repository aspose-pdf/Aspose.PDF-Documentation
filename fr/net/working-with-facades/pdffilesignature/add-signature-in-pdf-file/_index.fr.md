```
---
title: Ajouter une signature dans un fichier PDF
type: docs
weight: 10
url: /net/add-signature-in-pdf/
description: Cette section explique comment ajouter une signature à un fichier PDF en utilisant la classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Ajouter une signature numérique dans un fichier PDF

La classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) vous permet d'ajouter une signature dans un fichier PDF.
``` Vous devez créer un objet de la classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) en utilisant les fichiers PDF d'entrée et de sortie. Vous devez également créer un objet [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) à l'endroit où vous souhaitez ajouter la signature et pour définir l'apparence, vous pouvez spécifier une image en utilisant la propriété [SignatureAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) de l'objet [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Aspose.Pdf.Facades fournit également différents types de signatures comme PKCS#1, PKCS#7 et PKCS#7Detached. Afin de créer une signature d'un type spécifique, vous devez créer un objet de la classe particulière comme **PKCS1**, **PKCS7** ou **PKCS7Detached** en utilisant le fichier de certificat et le mot de passe.

Une fois l'objet d'un type de signature particulier créé, vous pouvez utiliser la méthode [Sign](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) de la classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) pour signer le PDF et passer l'objet de signature particulier à cette classe. Vous pouvez également spécifier d'autres attributs pour cette méthode. Enfin, vous devez enregistrer le PDF signé en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) de la classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). L'extrait de code suivant vous montre comment ajouter une signature dans un fichier PDF.

```csharp
public static void AddPdfFileSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Créer un rectangle pour l'emplacement de la signature
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Définir l'apparence de la signature
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Créer l'un des trois types de signature
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "Je suis l'auteur du document", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australie", true, rect, signature);
            // Enregistrer le fichier PDF de sortie
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```
Le code d'exemple suivant nous montre la capacité de signer un document avec deux signatures. Dans notre exemple, nous mettons la première signature sur la première page, et la seconde sur la deuxième page. Vous pouvez spécifier les pages dont vous avez besoin.

```csharp
 public static void AddTwoSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Signer avec la 1ère signature

            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Créer un rectangle pour l'emplacement de la 1ère signature
            System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Créer un objet de la 1ère signature
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "Je suis l'auteur du document", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australie", true, rect1, signature1);
            pdfSign.Save(_dataDir + "DigitallySign.pdf");


            // Signer avec la 2ème signature

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // Créer un rectangle pour l'emplacement de la 2ème signature
            System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Créer un objet de la 2ème signature
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(2, "Je suis le réviseur du document", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australie", true, rect2, signature2);

            // Enregistrer le fichier PDF de sortie
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

Pour un document avec des formulaires ou des acroformes qui doivent être signés, voir l'exemple suivant. Vous devez créer un objet de la classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) en utilisant les fichiers PDF d'entrée et de sortie. Utilisez [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) pour la liaison. Créez une signature avec la capacité d'ajouter les propriétés requises. Dans notre exemple, ce sont 'Reason' et 'CustomAppearance'.

```csharp
 public static void AddPdfFileSignatureField()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample02.pdf");

            // Create any of the three signature types
            PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "Signer en tant qu'auteur",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6,
                    FontFamilyName = "Calibri"
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature);
            // Save output PDF file
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

Si notre document a deux champs, l'algorithme pour le signer est similaire au premier exemple.

```csharp
public static void AddPdfFileSignatureField2()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample03.pdf");

            // Créer n'importe quel des trois types de signature
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021")
            {
                Reason = "Signer en tant qu'auteur",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature1);
            // Enregistrer le fichier PDF de sortie
            pdfSign.Save(_dataDir + "DigitallySign.pdf");

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // Créer n'importe quel des trois types de signature
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "Signer en tant que réviseur",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature2", signature2);
            // Enregistrer le fichier PDF de sortie
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```