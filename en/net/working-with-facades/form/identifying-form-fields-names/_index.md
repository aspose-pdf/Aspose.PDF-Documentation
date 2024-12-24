---
title: Identifying form fields names
type: docs
weight: 10
url: /net/identifying-form-fields-names/
description: Aspose.Pdf.Facades allows you identifying form fields names using Form Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Identifying form fields names",
    "alternativeHeadline": "Identify and Label PDF Form Fields Easily",
    "abstract": "The functionality in Aspose.PDF for .NET simplifies the process of identifying form field names in PDF documents. By utilizing the Form class and its attributes, users can easily retrieve and display field names alongside their corresponding fields, streamlining PDF form filling and editing. This feature enhances user experience by ensuring accurate field manipulation, especially when working with forms created in external tools like Adobe Designer",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "511",
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
    "url": "/net/identifying-form-fields-names/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/identifying-form-fields-names/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

[Aspose.PDF for .NET](/pdf/net/) provides the capability to create, edit and fill already created Pdf forms. [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) namespace contains [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) class, which contains the function named [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) and it takes two arguments i.e. Field name and field value. So in-order to fill the form fields, you must be aware of the exact form field name.

## Implementation details

We often come across a scenario where we need to fill the form which is created in some tool i.e. Adobe Designer, and we are not sure about the form fields names. So in order to fill the form fields, first we need to read the names of all the Pdf form fields. [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) class provides the property named [FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) which returns the entire field's names and returns null if PDF does not contain any field. However, when using this property, we get the names of the entire field's in PDF form and we might not be certain that which name corresponds to which field over the form.

As a solution to this problem, we will use the appearance attributes of each field. Form class has a function named [GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade) which returns attributes, including location, color, border style, font, list item and so on. To save these values we need to use [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade) class, which is used to record visual attributes of the fields. Once we have these attributes we can add a text field beneath every field which would be displaying the field name.

{{% alert color="primary" %}}
At this point, a question arises "how we would determine the location where to add the text field?"
{{% /alert %}}

{{% alert color="primary" %}}
The solution to this problem is Box property in [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade) class, which holds the field's location. We need to save these values to an array of rectangle type and use these values to identify the position where to add the new text fields.

{{% /alert %}}

In [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) namespace we have a class named [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) which provides the capability to manipulate PDF forms. Open a pdf form; add a text field beneath every existing form field and save the Pdf form with new name.

```csharp
private static void IdentifyFormFieldsNames()
{
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // First a input pdf file should be assigned
    var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf");
    // Get all field names
    var allfields = form.FieldNames;
    // Create an array which will hold the location coordinates of Form fields
    var box = new System.Drawing.Rectangle[allfields.Length];
    for (int i = 0; i < allfields.Length; i++)
    {
        // Get the appearance attributes of each field, consequtively
        var facade = form.GetFieldFacade(allfields[i]);
        // Box in FormFieldFacade class holds field's location.
        box[i] = facade.Box;
    }
    form.Save(dataDir + "IdentifyFormFields_1_out.pdf");

    using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
    {
        // Now we need to add a textfield just upon the original one
        var editor = new Aspose.Pdf.Facades.FormEditor(doc);
        for (int i = 0; i < allfields.Length; i++)
        {
            // Add text field beneath every existing form field
            editor.AddField(Aspose.Pdf.Facades.FieldType.Text, 
            "TextField" + i, allfields[i], 1, 
            box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
        }
        // Close the document
        editor.Save(dataDir + "IdentifyFormFields_out.pdf");`
    }
}
```
