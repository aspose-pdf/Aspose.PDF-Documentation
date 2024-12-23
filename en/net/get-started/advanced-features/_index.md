---
title: Advanced Features
type: docs
weight: 140
url: /net/advanced-features/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Advanced Features",
    "alternativeHeadline": "Streamlined PDF Handling and Mathematical Expression Support in C#",
    "abstract": "Discover the latest enhancement in Aspose.PDF for .NET that allows seamless sending of PDF documents to web browsers for direct download without the need for physical storage. This feature not only simplifies file delivery but also includes advanced capabilities to extract embedded files and incorporate complex mathematical expressions using LaTeX, making it an essential tool for developers working with PDF formats",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "386",
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
    "url": "/net/advanced-features/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/advanced-features/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Sending Pdf to Browser for Download

Sometimes when you are developing an ASP.NET application, you need to send PDF file(s) to web browser(s) for download without saving them physically. In order to achieve that you can save PDF document into MemoryStream object after generating it and pass bytes from that MemoryStream to Response object. Doing this will make the browser to download the generated PDF document.

Following code snippet demonstrate the above functionality:

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-Examples.Web-SendPdfToBrowserForDownload.aspx-1.cs" >}}

## Extracting embedded files from a PDF file

Aspose.PDF stands out when it comes to advanced features for working with PDF format files. It extracts embedded files way better than other tools offering this feature.

With Aspose.PDF for .NET, you can efficiently extract any embedded file which may be an embedded font, an image, a video or an audio. Following goal-specific approach demonstrates how quickly and efficiently the embedded files can be extracted. Aspose.PDF facilitates you to extract all the font files whether it is a true type (TTF) or an open type font (OTF). Likewise, using this feature, image of any format JPG, PNG, SVG etc can be extracted in its 'as is' condition.

Following code snippet extracts all the embedded files from a PDF file:

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-DocumentConversion-PDFToXML-PDFToXML.cs" >}}

## Use of Latex Script to Add Mathematical Expressions

With Aspose.PDF, you can add mathematical expressions/formulas inside PDF document using latex script. Following examples show how this feature can be used in two different ways, in order to add a mathematical formula inside a table cell:

### Without preamble and document environment

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript-WithoutPreambleanddocument.cs" >}}

### With preamble and document environment

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript2-WithPreambleanddocument.cs" >}}

### Support for Latex Tags

The align environment is defined in amsmath package, and proof environment is defined in amsthm package. Thus, you have to specify these packages using \usepackage command in the document preamble. And this means that you have to enclose the LaTeX text into document environment either as shown in the following code sample.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Text-UseLatexScript3-UseLatexScript3.cs" >}}
