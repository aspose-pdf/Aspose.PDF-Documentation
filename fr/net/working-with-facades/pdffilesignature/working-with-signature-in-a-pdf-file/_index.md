---
title: Travailler avec la signature dans un fichier PDF
type: docs
weight: 40
url: fr/net/working-with-signature-in-a-pdf-file/
description: Cette section explique comment extraire les informations de signature, extraire l'image de la signature, changer la langue, etc. en utilisant la classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Comment extraire les informations de signature

Aspose.PDF pour .NET prend en charge la fonctionnalité de signer numériquement les fichiers PDF en utilisant la classe PdfFileSignature. Actuellement, il est également possible de déterminer la validité d'un certificat, mais nous ne pouvons pas extraire le certificat entier. Les informations qui peuvent être extraites sont la clé publique, l'empreinte digitale et l'émetteur, etc.

Pour extraire les informations de signature, nous avons introduit la méthode ExtractCertificate(..) dans la classe PdfFileSignature. Veuillez consulter l'extrait de code suivant qui démontre les étapes pour extraire le certificat de l'objet PdfFileSignature :

```csharp
public static void ExtractSignatureInfo()
        {
            string input = _dataDir + "DigitallySign.pdf";
            string certificateFileName = "extracted_cert.pfx";
            using (PdfFileSignature pdfFileSignature = new PdfFileSignature())
            {
                pdfFileSignature.BindPdf(input);
                var sigNames = pdfFileSignature.GetSignNames();
                if (sigNames.Count > 0)
                {
                    string sigName = sigNames[0];
                    if (!string.IsNullOrEmpty(sigName))
                    {
                        Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
                        if (cerStream != null)
                        {
                            using (cerStream)
                            {
                                using (FileStream fs = new FileStream(_dataDir + certificateFileName, FileMode.CreateNew))
                                {
                                    cerStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## Extraction d'image à partir du champ de signature (PdfFileSignature)

Aspose.PDF pour .NET prend en charge la fonctionnalité de signature numérique des fichiers PDF en utilisant la classe PdfFileSignature et lors de la signature du document, vous pouvez également définir une image pour SignatureAppearance. Désormais, cette API offre également la possibilité d'extraire des informations de signature ainsi que l'image associée au champ de signature.

Afin d'extraire les informations de signature, nous avons introduit la méthode ExtractImage(..) à la classe PdfFileSignature. Veuillez jeter un œil au code suivant qui démontre les étapes pour extraire une image de l'objet PdfFileSignature :

```csharp
public static void ExtractSignatureImage()
        {
            using (PdfFileSignature signature = new PdfFileSignature())
            {
                signature.BindPdf(_dataDir + "DigitallySign.pdf");

                if (signature.ContainsSignature())
                {
                    foreach (string sigName in signature.GetSignNames())
                    {
                        string outFile = _dataDir + "ExtractImages_out.jpg";
                        using (Stream imageStream = signature.ExtractImage(sigName))
                        {
                            if (imageStream != null)
                            {
                                imageStream.Position = 0;
                                using (FileStream fs = new FileStream(outFile, FileMode.OpenOrCreate))
                                {
                                    imageStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## Supprimer la Localisation et la Raison

La fonctionnalité Aspose.PDF permet une configuration flexible pour l'instance de signature numérique. La classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) offre la possibilité de signer un fichier PDF. L'implémentation de la méthode Sign permet de signer le PDF et de passer l'objet de signature particulier à cette classe. La méthode Sign contient un ensemble d'attributs pour la personnalisation de la signature numérique de sortie. Dans le cas où vous avez besoin de supprimer certains attributs de texte de la signature résultante, vous pouvez les laisser vides. Le code suivant démontre comment supprimer les deux lignes Localisation et Raison du bloc de signature :

```csharp
public static void SupressLocationReason()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Create a rectangle for signature location
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Set signature appearance
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Create any of the three signature types
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
            // Save output PDF file
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## Caractéristiques de personnalisation pour la signature numérique

Aspose.PDF pour .NET permet des fonctionnalités de personnalisation pour une signature numérique. La méthode Sign de la classe [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) est implémentée avec 6 surcharges pour votre utilisation confortable. Par exemple, vous pouvez configurer la signature résultante uniquement par l'instance de la classe SignatureCustomAppearance et les valeurs de ses propriétés. L'extrait de code suivant montre comment masquer la légende "Signé numériquement par" de la signature numérique de sortie de votre PDF.

```csharp
  public static void CustomizationFeaturesForDigitalSign()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Créer un rectangle pour l'emplacement de la signature
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Créer l'un des trois types de signature
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Times New Roman",
                DigitalSignedLabel = "Signé par:"
            };
            signature.CustomAppearance = signatureCustomAppearance;

            pdfSign.Sign(1, true, rect, signature);
            // Enregistrer le fichier PDF de sortie
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## Changer la Langue Dans le Texte de Signature Numérique

En utilisant Aspose.PDF pour l'API .NET, vous pouvez signer un fichier PDF en utilisant l'un des trois types de signatures suivants :

- PKCS#1
- PKCS#7
- PKCS#7

Chacune des signatures fournies contient un ensemble de propriétés de configuration implémentées pour votre commodité (localisation, format de date et d'heure, famille de polices, etc.). La classe [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) fournit la fonctionnalité correspondante. L'extrait de code suivant démontre comment changer la langue dans le texte de signature numérique :

```csharp
     public static void ChangeLanguageInDigitalSignText()
        {
            string inFile = _dataDir + "sample01.pdf";
            string outFile = _dataDir + "DigitallySign.pdf";

            using (Aspose.Pdf.Facades.PdfFileSignature pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
            {
                pdfSign.BindPdf(inFile);
                //create a rectangle for signature location
                System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

                //create any of the three signature types
                PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021")
                {
                    Reason = "Pruebas Firma",
                    ContactInfo = "Contacto Pruebas",
                    Location = "Población (Provincia)",
                    Date = DateTime.Now
                };
                SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
                {
                    DateSignedAtLabel = "Fecha",
                    DigitalSignedLabel = "Digitalmente firmado por",
                    ReasonLabel = "Razón",
                    LocationLabel = "Localización",
                    FontFamilyName = "Arial",
                    FontSize = 10d,
                    Culture = System.Globalization.CultureInfo.InvariantCulture,
                    DateTimeFormat = "yyyy.MM.dd HH:mm:ss"
                };
                pkcs.CustomAppearance = signatureCustomAppearance;
                // sign the PDF file
                pdfSign.Sign(1, true, rect, pkcs);
                //save output PDF file
                pdfSign.Save(outFile);
            }
        }
```