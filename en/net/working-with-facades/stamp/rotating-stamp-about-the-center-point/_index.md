---
title: Rotating stamp about the center point
type: docs
weight: 20
url: /net/rotating-stamp-about-the-center-point/
description: This section explains how to rotate stamp about the center point using Stamp Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotating stamp about the center point",
    "alternativeHeadline": "Rotate Stamps Precisely Around Their Center Point",
    "abstract": "The feature in Aspose.PDF for .NET allows users to rotate stamps within PDF files precisely around their center point. Utilizing the Stamp class, developers can easily set rotation values from 0 to 360 degrees, enhancing the flexibility and customization of watermark placement in documents. This functionality is ideal for creating visually dynamic PDFs with personalized stamp orientations",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "339",
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
    "url": "/net/rotating-stamp-about-the-center-point/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotating-stamp-about-the-center-point/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

{{% alert color="primary" %}}

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) in [Aspose.PDF for .NET](/pdf/net/) allows you to add a stamp in an existing PDF file. Sometimes, users do need to rotate the stamp. In this article, we’ll see how to rotate a stamp about its center point.

{{% /alert %}}

## Implementation details

[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class allows you to add a watermark in a PDF file. You can specify image to be added as a stamp using [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1) method. The [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) method allows you to set the origin of the added stamp; this origin is the lower-left coordinates of the stamp. You can also set the size of the image using [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize) method.

Now, we see how the stamp can be rotated about the center of the stamp. [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class provides a property named Rotation. This property sets or gets the rotation from 0 to 360 of stamp content. We can specify any rotation value from 0 to 360. By specifying the rotation value we can rotate the stamp about its center point. If a Stamp is an object of Stamp type then the rotation value can be specified as aStamp.Rotation = 90. In this case the stamp will be rotated at 90 degrees about the center of the stamp content. The following code snippet shows you how to rotate the stamp about the center point:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-RotatingStamp-RotatingStamp.cs" >}}