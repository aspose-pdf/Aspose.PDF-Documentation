---
title: Extract Image and Signature Information
linktitle: Extract Image and Signature Information
type: docs
weight: 30
url: /net/extract-image-and-signature-information/
description: You may extract images from the signature field and extract signature information using the SignatureField class with C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Image and Signature Information",
    "alternativeHeadline": "How to extract Image and Signature from PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, extract signature",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "You may extract images from the signature field and extract signature information using the SignatureField class with C#."
}
</script>

The next code snippets also work with a new graphical [Aspose.Drawing](/pdf/net/drawing/) interface.

## Extracting Image from Signature Field

Aspose.PDF for .NET supports the feature to digitally sign the PDF files using the [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) class and while signing the document, you can also set an image for SignatureAppearance. Now, this API also provides the capability to extract signature information as well as the image associated with the signature field.

In order to extract signature information, we have introduced the [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractimage) method to the SignatureField class. Please take a look at the following code snippet which demonstrates the steps to extract an image from the SignatureField object:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

string input = dataDir+ @"ExtractingImage.pdf";
using (Document pdfDocument = new Document(input))
{
    foreach (Field field in pdfDocument.Form)
    {
        SignatureField sf = field as SignatureField;
        if (sf != null)
        {
            string outFile = dataDir+ @"output_out.jpg";
            using (Stream imageStream = sf.ExtractImage())
            {
                if (imageStream != null)
                {
                    using (System.Drawing.Image image = Bitmap.FromStream(imageStream))
                    {
                        image.Save(outFile, System.Drawing.Imaging.ImageFormat.Jpeg);
                    }
                }
            }
        }
    }
}
```

### Replace signature Image

Sometimes you may have a requirement to only replace the image of an already present signature field inside PDF file. In order to accomplish this requirement, first, we need to search form fields inside the PDF file, identify Signature fields, get the dimensions (Rectangular dimensions) of the signature field and then stamp an image over the same dimensions.

## Extract Signature Information

Aspose.PDF for .NET supports the feature to digitally sign the PDF files using the SignatureField class. Currently, we can also determine the validity of the certificate but we cannot extract the whole certificate. The information which can be extracted is a public key, thumbprint, issuer, etc.

To extract signature information, we have introduced the [ExtractCertificate](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) method to the [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) class. Please take a look at the following code snippet which demonstrates the steps to extract the certificate from SignatureField object:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

string input = dataDir + "ExtractSignatureInfo.pdf";
using (Document pdfDocument = new Document(input))
{
    foreach (Field field in pdfDocument.Form)
    {
        SignatureField sf = field as SignatureField;
        if (sf != null)
        {
            Stream cerStream = sf.ExtractCertificate();
            if (cerStream != null)
            {
                using (cerStream)
                {
                    byte[] bytes = new byte[cerStream.Length];
                    using (FileStream fs = new FileStream(dataDir + @"input.cer", FileMode.CreateNew))
                    {
                        cerStream.Read(bytes, 0, bytes.Length);
                        fs.Write(bytes, 0, bytes.Length);
                    }
                }
            }
        }
    }
}
```

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
