---
title: Travailler avec la signature dans un fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/working-with-signature-in-a-pdf-file/
description: Cette section explique comment extraire des informations de signature, extraire une image de la signature, changer de langue, etc. en utilisant la classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Signature in PDF File",
    "alternativeHeadline": "Extract Signature Details and Images from PDFs",
    "abstract": "La nouvelle fonctionnalité dans Aspose.PDF for .NET améliore la sécurité des documents PDF en permettant aux utilisateurs d'extraire des informations et des images de signature avec la classe PdfFileSignature. Cette fonctionnalité inclut également la possibilité de personnaliser les signatures numériques, de supprimer des informations spécifiques comme l'emplacement et la raison, et de changer les paramètres de langue pour le texte de signature, fournissant un ensemble d'outils complet pour gérer efficacement les signatures PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "878",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/working-with-signature-in-a-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-signature-in-a-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Comment extraire des informations de signature

Aspose.PDF for .NET prend en charge la fonctionnalité de signature numérique des fichiers PDF en utilisant la classe PdfFileSignature. Actuellement, il est également possible de déterminer la validité d'un certificat, mais nous ne pouvons pas extraire l'ensemble du certificat. Les informations qui peuvent être extraites sont la clé publique, l'empreinte digitale et l'émetteur, etc.

Pour extraire des informations de signature, nous avons introduit la méthode ExtractCertificate(..) dans la classe PdfFileSignature. Veuillez consulter le code suivant qui démontre les étapes pour extraire le certificat de l'objet PdfFileSignature :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSignatureInfo()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        // Get list of signature names
        var sigNames = pdfFileSignature.GetSignatureNames();
        if (sigNames.Count > 0)
        {
            SignatureName sigName = sigNames[0];            
            // Extract signature certificate
            Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
            if (cerStream != null)
            {
                using (cerStream)
                {
                    using (FileStream fs = new FileStream(dataDir + "extracted_cert.pfx", FileMode.CreateNew))
                    {
                        cerStream.CopyTo(fs);
                    }
                }
            }
            
        }
    }
}
```

## Extraction d'image du champ de signature (PdfFileSignature)

Aspose.PDF for .NET prend en charge la fonctionnalité de signature numérique des fichiers PDF en utilisant la classe PdfFileSignature et lors de la signature du document, vous pouvez également définir une image pour SignatureAppearance. Maintenant, cette API fournit également la capacité d'extraire des informations de signature ainsi que l'image associée au champ de signature.

Afin d'extraire des informations de signature, nous avons introduit la méthode ExtractImage(..) dans la classe PdfFileSignature. Veuillez consulter le code suivant qui démontre les étapes pour extraire l'image de l'objet PdfFileSignature :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSignatureImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var signature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        signature.BindPdf(dataDir + "ExtractingImage.pdf");

        if (signature.ContainsSignature())
        {
            // Get list of signature names
            foreach (string sigName in signature.GetSignatureNames())
            {                
                // Extract signature image
                using (Stream imageStream = signature.ExtractImage(sigName))
                {
                    if (imageStream != null)
                    {
                        imageStream.Position = 0;
                        using (FileStream fs = new FileStream(dataDir + "ExtractImages_out.jpg", FileMode.OpenOrCreate))
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

## Supprimer l'emplacement et la raison

La fonctionnalité Aspose.PDF permet une configuration flexible pour l'instance de signature numérique. La classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) offre la possibilité de signer un fichier PDF. L'implémentation de la méthode Sign permet de signer le PDF et de passer l'objet de signature particulier à cette classe. La méthode Sign contient un ensemble d'attributs pour la personnalisation de la signature numérique de sortie. Dans le cas où vous devez supprimer certains attributs de texte de la signature résultante, vous pouvez les laisser vides. Le code suivant démontre comment supprimer l'emplacement et la raison de la zone de signature :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SupressLocationReason()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
        // Set signature appearance
        pdfFileSignature.SignatureAppearance = dataDir + "aspose-logo.png";

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdfFileSignature.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

## Fonctionnalités de personnalisation pour la signature numérique

Aspose.PDF for .NET permet des fonctionnalités de personnalisation pour une signature numérique. La méthode Sign de la classe [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) est implémentée avec 6 surcharges pour votre utilisation confortable. Par exemple, vous pouvez configurer la signature résultante uniquement par l'instance de la classe SignatureCustomAppearance et ses valeurs de propriétés. Le code suivant démontre comment cacher la légende "Signé numériquement par" de la signature numérique de sortie de votre PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizationFeaturesForDigitalSign()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1
        // Create signature appearance
        var signatureCustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
        {
            FontSize = 6,
            FontFamilyName = "Times New Roman",
            DigitalSignedLabel = "Signed by:"
        };
        // Set signature appearance
        signature.CustomAppearance = signatureCustomAppearance;

        pdfFileSignature.Sign(1, true, rect, signature);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

## Changer la langue dans le texte de la signature numérique

En utilisant l'API Aspose.PDF for .NET, vous pouvez signer un fichier PDF en utilisant l'un des trois types de signatures suivants :

- PKCS#1.
- PKCS#7.
- PKCS#12.

Chacune des signatures fournies contient un ensemble de propriétés de configuration mises en œuvre pour votre commodité (localisation, format de date et d'heure, famille de polices, etc.). La classe [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) fournit la fonctionnalité correspondante. Le code suivant démontre comment changer la langue dans le texte de la signature numérique :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeLanguageInDigitalSignText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();   
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");
        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

        // Create any of the three signature types
        var pkcs = new Aspose.Pdf.Forms.PKCS7(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Pruebas Firma",
            ContactInfo = "Contacto Pruebas",
            Location = "Población (Provincia)",
            Date = DateTime.Now
        };
        
        var signatureCustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
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
        // Set signature appearance
        pkcs.CustomAppearance = signatureCustomAppearance;
        // Sign the PDF file
        pdfFileSignature.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```