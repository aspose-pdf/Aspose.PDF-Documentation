---
title: Add Header and Footer to PDF using Python
linktitle: Add Header and Footer to PDF
type: docs
weight: 50
url: /python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Python via .NET allows you to add headers and footers to your PDF file using TextStamp class.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Header and Footer to PDF using Python",
    "alternativeHeadline": "How to add Header and Footer to PDF File",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, add header, add footer in pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for Python via .NET allows you to add headers and footers to your PDF file using TextStamp class."
}
</script>

**Aspose.PDF for Python via .NET** allows you to add header and footer in your existing PDF file. You may add images or text to a PDF document. Also, try to add different headers in one PDF File with Python.

## Adding Text in Header of PDF File

You can use [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) class to add text in the header of a PDF file. TextStamp class provides properties necessary to create a text based stamp like font size, font style, and font color etc. In order to add text in the header, you need to create a Document object and a TextStamp object using required properties. After that, you can call 'add_stamp' method of the Page to add the text in the header of the PDF.

You need to set the [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) property in such a way that it adjusts the text in the header area of your PDF. You also need to set 'horizontal_alignment' to Center and 'vertical_alignment' to Top.

The following code snippet shows you how to add text in the header of a PDF file with Python:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create header
    textStamp = ap.TextStamp("Header Text")
    # Set properties of the stamp
    textStamp.top_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.TOP
    # Add header on all pages
    for page in document.pages:
        page.add_stamp(textStamp)

    # Save updated document
    document.save(output_pdf)
```

## Adding Text in Footer of PDF File

You can use [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) class to add text in the footer of a PDF file. TextStamp class provides properties necessary to create a text based stamp like font size, font style, and font color etc. In order to add text in the footer, you need to create a Document object and a TextStamp object using required properties. After that, you can call 'add_stamp' method of the Page to add the text in the footer of the PDF.

The following code snippet shows you how to add text in the footer of a PDF file with Python:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Create footer
    textStamp = ap.TextStamp("Footer Text")
    # Set properties of the stamp
    textStamp.bottom_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # Add footer on all pages
    for page in document.pages:
        page.add_stamp(textStamp)

    # Save updated PDF file
    document.save(output_pdf)
```

## Adding Image in Header of PDF File

You can use [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) class to add image in the header of a PDF file. Image Stamp class provides properties necessary to create image based stamp like font size, font style, and font color etc. In order to add image in the header, you need to create a Document object and a Image Stamp object using required properties. After that, you can call 'add_stamp' method of the Page to add the image in the header of the PDF.

The following code snippet shows you how to add image in the header of a PDF file with Python:

```python 

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create header
    image_stamp = ap.ImageStamp(input_image)
    # Set properties of the stamp
    image_stamp.top_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.TOP
    # Add header on all pages
    for page in document.pages:
        page.add_stamp(image_stamp)

    # Save updated document
    document.save(output_pdf)
```

## Adding Image in Footer of PDF File

You can use [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) class to add image in the footer of a PDF file. [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) class provides properties necessary to create image based stamp like font size, font style, and font color etc. In order to add image in the footer, you need to create a Document object and an Image Stamp object using required properties. After that, you can call 'add_stamp' method of the Page to add the image in the footer of the PDF.

The following code snippet shows you how to add image in the footer of a PDF file with Python:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Create footer
    image_stamp = ap.ImageStamp(input_image)
    # Set properties of the stamp
    image_stamp.bottom_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # Add footer on all pages
    for page in document.pages:
        page.add_stamp(image_stamp)

    # Save updated PDF file
    document.save(output_pdf)
```

## Adding different Headers in one PDF File

We know that we can add TextStamp in Header/Footer section of the document by using [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) or [bottom_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) properties, but sometimes we may have the requirement to add multiple header/footers in a single PDF document. **Aspose.PDF for Python via .NET** explains how to do this.

In order to accomplish this requirement, we will create individual TextStamp objects (number of objects depends upon the number of Header/Footers required)and will add them to PDF document. We may also specify different formatting information for individual stamp object. In following example, we have created Document object and three TextStamp objects and then we have used 'add_stamp' method of the Page to add the text in the header section of the PDF. The following code snippet shows you how to add image in the footer of a PDF file with Aspose.PDF for Python:

```python

    import aspose.pdf as ap

    # Create three stamps
    stamp1 = ap.TextStamp("Header 1")
    stamp2 = ap.TextStamp("Header 2")
    stamp3 = ap.TextStamp("Header 3")

    # Set stamp alignment (place stamp on page top, centered horiznotally)
    stamp1.vertical_alignment = ap.VerticalAlignment.TOP
    stamp1.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Specify the font style as Bold
    stamp1.text_state.font_style = ap.text.FontStyles.BOLD
    # Set the text fore ground color information as red
    stamp1.text_state.foreground_color = ap.Color.red
    # Specify the font size as 14
    stamp1.text_state.font_size = 14

    # Now we need to set the vertical alignment of 2nd stamp object as Top
    stamp2.vertical_alignment = ap.VerticalAlignment.TOP
    # Set Horizontal alignment information for stamp as Center aligned
    stamp2.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Set the zooming factor for stamp object
    stamp2.zoom = 10

    # Set the formatting of 3rd stamp object
    # Specify the Vertical alignment information for stamp object as TOP
    stamp3.vertical_alignment = ap.VerticalAlignment.TOP
    # Set the Horizontal alignment inforamtion for stamp object as Center aligned
    stamp3.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Set the rotation angle for stamp object
    stamp3.rotate_angle = 35
    # Set pink as background color for stamp
    stamp3.text_state.background_color = ap.Color.pink
    # Change the font face information for stamp to Verdana
    stamp3.text_state.font = ap.text.FontRepository.find_font("Verdana")
    # First stamp is added on first page;
    document.pages[1].add_stamp(stamp1)
    # Second stamp is added on second page;
    document.pages[2].add_stamp(stamp2)
    # Third stamp is added on third page.
    document.pages[3].add_stamp(stamp3)

    # Save the updated document
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
