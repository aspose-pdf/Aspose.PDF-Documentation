---
title: Modifing AcroForm
linktitle: Modifing AcroForm
type: docs
weight: 40
url: /net/modifing-form/
description: Modifing form in your PDF file with Aspose.PDF for .NET library. You can Add or remove fields in existing form, getand set fieldlimit and etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modifing AcroForm",
    "alternativeHeadline": "Modify and Manage AcroForm Fields in PDF",
    "abstract": "The new Modifying AcroForm feature in the Aspose.PDF for .NET library allows users to seamlessly add or remove fields from existing PDF forms. This functionality also includes setting field limits and customizing font appearances for a refined user experience, enhancing PDF form management and interaction",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Modifing AcroForm, Aspose.PDF for .NET, PDF form fields, SetFieldLimit, custom font, Add/remove fields, Document Form collection, DefaultAppearance, manage form fields, PDF manipulation",
    "wordcount": "601",
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
    "url": "/net/modifing-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modifing-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Modifing form in your PDF file with Aspose.PDF for .NET library. You can Add or remove fields in existing form, getand set fieldlimit and etc."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Get or Set Field Limit

The FormEditor class SetFieldLimit(field, limit) method allows you to set a field limit, the maximum number of characters that can be entered into a field.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void SetFieldLimit()
{
    // Explicit dataDir initialization
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create FormEditor instance
    using (var form = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Set field limit for "textbox1"
        form.SetFieldLimit("textbox1", 15);

        // Save the updated PDF
        form.Save(dataDir + "SetFieldLimit_out.pdf");
    }
}
```

Similarly, Aspose.PDF has a method that gets the field limit using the DOM approach. The following code snippet shows the steps.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetFieldLimitUsingDOM()
{
    // Explicit dataDir initialization
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open document
    using(var document = new Aspose.Pdf.Document(dataDir + "FieldLimit.pdf"))
	{
		// Get the field and its maximum limit
		if (document.Form["textbox1"] is Aspose.Pdf.Forms.TextBoxField textBoxField)
		{
			Console.WriteLine("Limit: " + textBoxField.MaxLen);
		}
	}
}
```

You can also get the same value using the *Aspose.Pdf.Facades* namespace using the following code snippet.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetFieldLimitUsingFacades()
{
    // Explicit dataDir initialization
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create Form instance
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "FieldLimit.pdf");

        // Get the field limit for "textbox1"
        Console.WriteLine("Limit: " + form.GetFieldLimit("textbox1"));
    }
}
```

## Set Custom Font for the Form Field

Form fields in Adobe PDF files can be configured to use specific default fonts. In the early versions of Aspose.PDF, only the 14 default fonts were supported. Later releases allowed developers to apply any font. To set and update the default font used for form fields, use the DefaultAppearance(Font font, double size, Color color) class. This class can be found under the Aspose.Pdf.InteractiveFeatures namespace. To use this object, use the Field class DefaultAppearance property.

The following code snippet shows how to set the default font for PDF form fields.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void SetFormFieldFont()
{
    // Explicit dataDir initialization
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open document
    using(var document = new Aspose.Pdf.Document(dataDir + "FormFieldFont14.pdf"))
	{
		// Get particular form field from document
		if (document.Form["textbox1"] is Aspose.Pdf.Forms.Field field)
		{
			// Create font object
			var font = Aspose.Pdf.Text.FontRepository.FindFont("ComicSansMS");

			// Set the font information for form field
			field.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance(font, 10, System.Drawing.Color.Black);
		}

		// Save updated document
		document.Save(dataDir + "FormFieldFont14_out.pdf");
	}
}
```

## Add/remove fields in existing form

All the form fields are contained in the Document object's Form collection. This collection provides different methods that manage form fields, including the Delete method. If you want to delete a particular field, pass the field name as a parameter to the Delete method and then save the updated PDF document. The following code snippet shows how to delete a particular field from a PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void DeleteFormField()
{
    // Explicit dataDir initialization
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open document
    using(var document = new Aspose.Pdf.Document(dataDir + "DeleteFormField.pdf"))
	{
		// Delete a particular field by name
		document.Form.Delete("textbox1");

		// Save modified document
		document.Save(dataDir + "DeleteFormField_out.pdf");
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
