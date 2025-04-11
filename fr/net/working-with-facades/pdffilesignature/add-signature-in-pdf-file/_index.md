---
title: Ajouter une signature dans un fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/add-signature-in-pdf/
description: Cette section explique comment ajouter une signature à un fichier PDF en utilisant la classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Signature in PDF File",
    "alternativeHeadline": "Add Custom Digital Signatures to PDF Files",
    "abstract": "Améliorez vos documents PDF avec la nouvelle capacité d'ajouter des signatures numériques en utilisant la classe PdfFileSignature. Cette fonctionnalité permet aux utilisateurs d'appliquer différents types de signatures, y compris PKCS#1, PKCS#7 et PKCS#7Detached, tout en personnalisant l'apparence de la signature avec des images et des attributs spécifiques. Rationalisez votre processus de vérification de documents en incorporant plusieurs signatures sur différentes pages avec facilité.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "838",
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
    "url": "/net/add-signature-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-signature-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Ajouter une signature numérique dans un fichier PDF

La classe [PdfFileSignature](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesignature) vous permet d'ajouter une signature dans un fichier PDF. Vous devez créer un objet de la classe [PdfFileSignature](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesignature) en utilisant les fichiers PDF d'entrée et de sortie. Vous devez également créer un objet [Rectangle](https://reference.aspose.com/pdf/fr/net/aspose.pdf/rectangle) à l'endroit où vous souhaitez ajouter la signature et pour définir l'apparence, vous pouvez spécifier une image en utilisant la propriété [SignatureAppearance](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) de l'objet [PdfFileSignature](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesignature). Aspose.Pdf.Facades fournit également différents types de signatures comme PKCS#1, PKCS#7 et PKCS#7Detached. Pour créer une signature d'un type spécifique, vous devez créer un objet de la classe particulière comme **PKCS1**, **PKCS7** ou **PKCS7Detached** en utilisant le fichier de certificat et le mot de passe.

Une fois l'objet d'un type de signature particulier créé, vous pouvez utiliser la méthode [Sign](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) de la classe [PdfFileSignature](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesignature) pour signer le PDF et passer l'objet de signature particulier à cette classe. Vous pouvez également spécifier d'autres attributs pour cette méthode. Enfin, vous devez enregistrer le PDF signé en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/methods/save/index) de la classe [PdfFileSignature](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesignature). L'extrait de code suivant vous montre comment ajouter une signature dans un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
    
        // Set signature appearance
        pdFileSignature.SignatureAppearance = dataDir + "aspose-logo.png";

        // Create any of the three signature types
        var signature = new PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(1, "I'm document author", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect, signature);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

L'exemple de code suivant nous montre la capacité de signer un document avec deux signatures. Dans notre exemple, nous mettons la première signature sur la première page, et la seconde sur la deuxième page. Vous pouvez spécifier les pages dont vous avez besoin.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTwoSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for 1st signature location
        System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create 1st signature object
        var signature1 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(1, "I'm document author", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1, signature1);
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");

        // Sign with 2nd signature
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "DigitallySign_out.pdf");

        // Create a rectangle for 2nd signature location
        System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create 2nd signature object
        var signature2 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(2, "I'm document reviewer", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect2, signature2);

        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign2_out.pdf");
    }
}
```

Pour un document avec des formulaires ou des acroforms qui doit être signé, voir l'exemple suivant. Vous devez créer un objet de la classe [PdfFileSignature](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilesignature) en utilisant les fichiers PDF d'entrée et de sortie. Utilisez [BindPdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) pour lier. Créez une signature avec la possibilité d'ajouter les propriétés requises. Dans notre exemple, elles sont 'Reason' et 'CustomAppearance'.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignatureField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Author",
            CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Calibri"
            }
        }; // PKCS#1
        
        pdFileSignature.Sign("Signature1", signature);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

Si notre document a deux champs, l'algorithme pour le signer est similaire au premier exemple.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignatureField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create any of the three signature types
        var signature1 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Author",
            CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
            {
                FontSize = 6
            }
        }; // PKCS#1
        pdFileSignature.Sign("Signature1", signature1);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "DigitallySign_out.pdf");

        // Create any of the three signature types
        var signature2 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Reviwer",
            CustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6
            }
        }; // PKCS#1
        
        pdFileSignature.Sign("Signature2", signature2);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign2_out.pdf");
    }
}
```