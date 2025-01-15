---
title: Add PDF Form Fields
type: docs
weight: 10
url: /net/add-form-fields/
description: This topic explains how to work with Form Fields with Aspose.PDF Facades using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Form Fields",
    "alternativeHeadline": "Effortlessly Enhance PDFs with Custom Form Fields",
    "abstract": "Enhance your PDF documents with dynamic interactivity by adding form fields using the FormEditor class in Aspose.PDF for .NET. This feature allows you to effortlessly incorporate text fields, submit buttons with URLs, and JavaScript functionality to push buttons, streamlining user input and data submission in your PDFs",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "548",
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
    "url": "/net/add-form-fields/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-form-fields/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Add Form Field in an Existing PDF file

In order to add a form field in an existing PDF file, you need to use [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) method of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. This method requires you to specify the type of the field you want to add along with the name and location of the field. You need to create an object of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class, use [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) method to add a new field in the PDF, Also, you can specify a limit on the number of characters in your field with [SetFieldLimit](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) and finally use [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method to save the updated PDF file. The following code snippet shows you how to add form field in an existing PDF file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a text field named "Country" to the first page of the PDF
        // Specify the coordinates of the field (left, bottom, right, top)
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);

        // Set a character limit for the "Country" field to 20 characters
        editor.SetFieldLimit("Country", 20);

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```

## Add Submit Button URL in an Existing PDF File 

[AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) method allows you to set the submit button's URL in a PDF file. This is the URL where the data is posted when the submit button is clicked. In our example code, we specify the URL, the name of our field, the page number to which we want to add, and the button placement coordinates.
[AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) method required the name of the submit button field and the URL. This method is provided by [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) class. The following code snippet shows you how to set submit button URL.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddSubmitBtn()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var editor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         editor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a submit button named "Submit" to the first page of the PDF
         // Specify the button text ("Submit"), the URL to which the form data will be submitted,
         // and the coordinates of the button (left, bottom, right, top)
         editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);

         // Save PDF document
         editor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## Add JavaScript for Push Button

[AddFieldScript](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfieldscript) method allows you to add JavaScript to a push button in a PDF file. This method requires the name of the push button and the JavaScript . This method is provided by [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) class. The following code snippet shows you how to set JavaScript to a push button.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFieldScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a JavaScript action to the field named "Last Name"
        // The script displays an alert box with the message "Only one last name"
        editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```

