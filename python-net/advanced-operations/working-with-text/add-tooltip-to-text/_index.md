---
title: PDF Tooltip using Python
linktitle: PDF Tooltip
type: docs
weight: 20
url: /python-net/pdf-tooltip/
description: Learn how to add tooltip to the text fragment in PDF using Python and Aspose.PDF
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip using Python",
    "alternativeHeadline": "Add PDF Tooltip to the Text",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, add pdf tooltip",
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
    "url": "/python-net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/pdf-tooltip/"
    },
    "dateModified": "2024-02-04",
    "description": "Learn how to add tooltip to the text fragment in PDF using Python and Aspose.PDF"
}
</script>

## Add Tooltip to Searched Text by adding Invisible Button

This code demonstrates how to add tooltips to specific text fragments in a PDF document using Aspose.PDF. The tooltips are displayed when the mouse cursor hovers over the corresponding text.

The following code snippet will show you the way to achieve this functionality:

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("Move the mouse cursor here to display a tooltip")
    )
    document.pages[1].paragraphs.add(
        ap.text.TextFragment(
            "Move the mouse cursor here to display a very long tooltip"
        )
    )
    document.save(output_pdf)

    # Open document with text
    document = ap.Document(output_pdf)
    # Create TextAbsorber object to find all the phrases matching the regular expression
    absorber = ap.text.TextFragmentAbsorber(
        "Move the mouse cursor here to display a tooltip"
    )
    # Accept the absorber for the document pages
    document.pages.accept(absorber)
    # Get the extracted text fragments
    text_fragments = absorber.text_fragments

    # Loop through the fragments
    for fragment in text_fragments:
        # Create invisible button on text fragment position
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # alternate_name value will be displayed as tooltip by a viewer application
        field.alternate_name = "Tooltip for text."
        # Add button field to the document
        document.form.add(field)

    # Next will be sapmle of very long tooltip
    absorber = ap.text.TextFragmentAbsorber(
        "Move the mouse cursor here to display a very long tooltip"
    )
    document.pages.accept(absorber)
    text_fragments = absorber.text_fragments

    for fragment in text_fragments:
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # Set very long text
        field.alternate_name = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
            " sed do eiusmod tempor incididunt ut labore et dolore magna"
            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
            " ullamco laboris nisi ut aliquip ex ea commodo consequat."
            " Duis aute irure dolor in reprehenderit in voluptate velit"
            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
            " occaecat cupidatat non proident, sunt in culpa qui officia"
            " deserunt mollit anim id est laborum."
        )
        document.form.add(field)

    # Save document
    document.save(output_pdf)
```

## Create a Hidden Text Block and Show it on Mouse Over

This Python code snippet shows how to add floating text to a PDF document, which appears when the mouse cursor hovers over a specific area.

First, a new PDF document is created, and a paragraph containing the text "Move the mouse cursor here to display floating text" is added to it. The document is then saved.

Next, the saved document is reopened, and a TextAbsorber object is created to find the previously added text fragment. This text fragment is then used to define the position and characteristics of the floating text field.

A TextBoxField object is created to represent the floating text field, and its properties such as position, value, read-only status, and visibility are set accordingly. Additionally, a unique name and appearance characteristics are assigned to the field.

The floating text field is added to the document's form, and an invisible button field is created at the position of the original text fragment. HideAction events are assigned to the button field, specifying that the floating text field should appear when the mouse cursor enters its vicinity and disappear when the cursor exits.

Finally, the button field is added to the document's form, and the modified document is saved.

This code snippet provides a method to create interactive floating text elements in a PDF document using Aspose.PDF for Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("Move the mouse cursor here to display floating text")
    )
    document.save(output_pdf)

    # Open document with text
    document = ap.Document(output_pdf)
    # Create TextAbsorber object to find all the phrases matching the regular expression
    absorber = ap.text.TextFragmentAbsorber(
        "Move the mouse cursor here to display floating text"
    )
    # Accept the absorber for the document pages
    document.pages.accept(absorber)
    # Get the first extracted text fragment
    text_fragments = absorber.text_fragments
    fragment = text_fragments[1]

    # Create hidden text field for floating text in the specified rectangle of the page
    floating_field = ap.forms.TextBoxField(
        fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
    )
    # Set text to be displayed as field value
    floating_field.value = 'This is the "floating text field".'
    # We recommend to make field 'readonly' for this scenario
    floating_field.read_only = True
    # Set 'hidden' flag to make field invisible on document opening
    floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

    # Setting a unique field name isn't necessary but allowed
    floating_field.partial_name = "FloatingField_1"

    # Setting characteristics of field appearance isn't necessary but makes it better
    floating_field.default_appearance = ap.annotations.DefaultAppearance(
        "Helv", 10, ap.Color.blue.to_rgb()
    )
    floating_field.characteristics.background = ap.Color.light_blue.to_rgb()
    floating_field.characteristics.border = ap.Color.dark_blue.to_rgb()
    floating_field.border = ap.annotations.Border(floating_field)
    floating_field.border.width = 1
    floating_field.multiline = True

    # Add text field to the document
    document.form.add(floating_field)
    # Create invisible button on text fragment position
    button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
    # Create new hide action for specified field (annotation) and invisibility flag.
    # (You also may reffer floating field by the name if you specified it above.)
    # Add actions on mouse enter/exit at the invisible button field

    button_field.actions.on_enter = ap.annotations.HideAction(
        floating_field.partial_name, False
    )
    button_field.actions.on_exit = ap.annotations.HideAction(
        floating_field.partial_name
    )

    # Add button field to the document
    document.form.add(button_field)

    # Save document
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
