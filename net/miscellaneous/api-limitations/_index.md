---
title: API Limitations
type: docs
weight: 70
url: /net/api-limitations/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "API Limitations",
    "alternativeHeadline": "Key API Limitations",
    "abstract": "Introducing enhanced XSL-FO to PDF conversion capabilities in Aspose.PDF for .NET, offering detailed insights into known limitations, including the lack of SVG support and restrictions on PDF/X and dynamic XFA forms. Users should be aware of specific formatting challenges when converting complex HTML documents and the constraints regarding font embedding in different operating systems",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "305",
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
    "url": "/net/api-limitations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/api-limitations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}

## **Xsl Fo to Pdf**
Following are the known issues of XSL-FO support.

- SVG is not supported
## **PDF creator information**
- Please note that you cannot set values against the **Application** and **Producer** fields, because Aspose Ltd. and Aspose.PDF for .NET x.x.x will be displayed against these fields
## **Others**
Following are some other known issues.

- Pdf/X is not supported.
- Dynamic XFA form is not supported: As its pages created/rendered at the time of PDF loading, in Adobe Acrobat/Reader. So we can't extract and save any such virtual page or several pages. Instead we (and Adobe Acrobat) can extract only one true page which contains only error message.
- Special symbols $p and $P will not work if they do not end with a blank character.
- HTML to PDF conversion :- HTML is a very vast language and with every new release of Aspose.PDF for .NET, we try our level best to deliver a better & robust version of HTML to PDF conversion (*by support all kinds of HTML*) but as there are numerous HTML files with different nature/structure and complexity, so sometimes our component encounters some issues in terms of formatting when rendering HTML contents to PDF format and it usually happens when using documents with complex structure.
- Fonts embedding is not supported in MS Word for Macintosh and also please note that in MS Word for Windows, it only limited to TrueType fonts. Therefore when viewing word(DOC) files generated as a result of PDF to DOC conversion through Aspose.PDF for.NET, embedded fonts are substituted when viewing the files in MS Word on MAC OS. For further details, please take a look over [macsupportcentral](http://www.macsupportcentral.com/2012/05/embed-fonts-microsoft-office-word-files/).
