---
title: Extraire des informations sur les images et les signatures
linktitle: Extraire des informations sur les images et les signatures
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/extract-image-and-signature-information/
description: Vous pouvez extraire des images du champ de signature et extraire des informations de signature en utilisant la classe SignatureField avec C#.
lastmod: "2024-11-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Image and Signature Information",
    "alternativeHeadline": "Extract PDF signature images and certificate details",
    "abstract": "La nouvelle fonctionnalité Aspose.PDF for .NET extrait des images et des informations détaillées des champs de signature PDF. En utilisant C#, les développeurs peuvent récupérer des images de signature et des données de certificat, y compris la clé publique, l'empreinte digitale et les détails de l'émetteur, améliorant ainsi les capacités de manipulation des PDF. Cela améliore la vérification et la gestion des signatures numériques au sein des applications.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Extract Image, SignatureField class, ExtractImage method, ExtractCertificate method, C#, Aspose.PDF for .NET, PDF Signature, digital signature, signature information",
    "wordcount": "922",
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
    "url": "/net/extract-image-and-signature-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-image-and-signature-information/"
    },
    "dateModified": "2025-04-11",
    "description": "Vous pouvez extraire des images du champ de signature et extraire des informations de signature en utilisant la classe SignatureField avec C#."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Extraction d'image du champ de signature

Aspose.PDF for .NET prend en charge la fonctionnalité de signature numérique des fichiers PDF en utilisant la classe [SignatureField](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/signaturefield) et lors de la signature du document, vous pouvez également définir une image pour `SignatureAppearance`. Maintenant, cette API fournit également la capacité d'extraire des informations de signature ainsi que l'image associée au champ de signature.

Pour extraire des informations de signature, nous avons introduit la méthode [ExtractImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/signaturefield/methods/extractimage) à la classe SignatureField. Veuillez consulter le code suivant qui démontre les étapes pour extraire une image de l'objet `SignatureField` :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesFromSignatureField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractingImage.pdf"))
    {
        // Searching for signature fields
        foreach (var field in document.Form)
        {
            var sf = field as Aspose.Pdf.Forms.SignatureField;
            if (sf == null)
            {
                continue;
            }

            using (Stream imageStream = sf.ExtractImage())
            {
                if (imageStream != null)
                {
                    continue;
                }

                using (System.Drawing.Image image = System.Drawing.Bitmap.FromStream(imageStream))
                {
                    // Save the image
                    image.Save(dataDir + "output_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
                }
            }
        }
    }
}
```

## Extraire des informations de signature

Aspose.PDF for .NET prend en charge la fonctionnalité de signature numérique des fichiers PDF en utilisant la classe SignatureField. Actuellement, nous pouvons également déterminer la validité du certificat mais nous ne pouvons pas extraire l'ensemble du certificat. Les informations qui peuvent être extraites sont une clé publique, une empreinte digitale, un émetteur, etc.

Pour extraire des informations de signature, nous avons introduit la méthode [ExtractCertificate](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) à la classe [SignatureField](https://reference.aspose.com/pdf/fr/net/aspose.pdf.forms/signaturefield). Veuillez consulter le code suivant qui démontre les étapes pour extraire le certificat de l'objet SignatureField :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractCertificate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractSignatureInfo.pdf"))
    {
        // Searching for signature fields
        foreach (var field in document.Form)
        {
            var sf = field as Aspose.Pdf.Forms.SignatureField;
            if (sf == null)
            {
                continue;
            }
            // Extract certificate
            Stream cerStream = sf.ExtractCertificate();
            if (cerStream == null)
            {
                continue;
            }
            // Save certificate
            using (cerStream)
            {
                byte[] bytes = new byte[cerStream.Length];
                using (FileStream fs = new FileStream(dataDir + "input.cer", FileMode.CreateNew))
                {
                    cerStream.Read(bytes, 0, bytes.Length);
                    fs.Write(bytes, 0, bytes.Length);
                }
            }
        }
    }
}
```

Vous pouvez obtenir des informations sur les algorithmes de signature de document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void GetSignaturesInfo()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "signed_rsa.pdf"))
    {
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var sigNames = signature.GetSignatureNames();
            var signaturesInfoList =  signature.GetSignaturesInfo();
            foreach (var sigInfo in signaturesInfoList)
            {
                Console.WriteLine(sigInfo.DigestHashAlgorithm);
                Console.WriteLine(sigInfo.AlgorithmType);
                Console.WriteLine(sigInfo.CryptographicStandard);
                Console.WriteLine(sigInfo.SignatureName);
            }
        }
    }
}
```

Sortie d'exemple pour l'exemple ci-dessus :
```
Sha256
Rsa
Pkcs7
Signature1
```

## Vérification des signatures pour compromission

Vous pouvez utiliser la classe **SignaturesCompromiseDetector** pour vérifier les signatures numériques pour compromission.
Appelez la méthode **Check()** pour vérifier les signatures du document. 
Si aucune compromission de signature n'est détectée, la méthode renverra true.
Si la méthode renvoie false, vous pouvez vérifier si des signatures compromises utilisent la propriété **HasCompromisedSignatures** et récupérer la liste des signatures compromises via la propriété **CompromisedSignatures**.

Pour vérifier si les signatures existantes couvrent l'ensemble du document, utilisez la propriété **SignaturesCoverage**.
Cette propriété peut avoir les valeurs suivantes :
- **Indéfini** – si l'une des signatures est explicitement compromise ou si la vérification de couverture a échoué.
- **EntièrementSigné** – si les signatures couvrent l'ensemble du document.
- **PartiellementSigné** – si les signatures ne couvrent pas l'ensemble du document et qu'il y a du contenu non signé.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Check(string pdfFile)
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(pdfFile))
    {   
        // Create the compromise detector instance
        var detector = new Aspose.Pdf.SignaturesCompromiseDetector(document);
        CompromiseCheckResult result;
    
        // Check for compromise
        if (detector.Check(out result))
        {
            Console.WriteLine("No signature compromise detected");
            return;
        }
         
        // Get information about compromised signatures
        if (result.HasCompromisedSignatures)
        {
            Console.WriteLine($"Count of compromised signatures: {result.CompromisedSignatures.Count}");
            foreach (var signatureName in result.CompromisedSignatures)
            {
                Console.WriteLine($"Signature name: {signatureName.FullName}");
            }
        }
         
        // Get info about signatures coverage
        Console.WriteLine(result.SignaturesCoverage);   
    }
}
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Check(string pdfFile)
{
    // Open PDF document
    using var document = new Aspose.Pdf.Document(pdfFile);
    // Create the compromise detector instance
    var detector = new Aspose.Pdf.SignaturesCompromiseDetector(document);

    // Check for compromise
    if (detector.Check(out var result))
    {
        Console.WriteLine("No signature compromise detected");
        return;
    }
         
    // Get information about compromised signatures
    if (result.HasCompromisedSignatures)
    {
        Console.WriteLine($"Count of compromised signatures: {result.CompromisedSignatures.Count}");
        foreach (var signatureName in result.CompromisedSignatures)
        {
            Console.WriteLine($"Signature name: {signatureName.FullName}");
        }
    }
         
    // Get info about signatures coverage
    Console.WriteLine(result.SignaturesCoverage);
}
```
{{< /tab >}}
{{< /tabs >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>