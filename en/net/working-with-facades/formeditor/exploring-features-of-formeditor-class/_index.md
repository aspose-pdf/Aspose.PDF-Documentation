---
title: Exploring features of FormEditor class
type: docs
weight: 20
url: /net/exploring-features-of-formeditor-class/
description: You can learn details of exploring features of FormEditor class with Aspose. PDF for .NET library
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Exploring features of FormEditor class",
    "alternativeHeadline": "Enhancing PDF Forms with FormEditor Class",
    "abstract": "Discover the enhanced capabilities of the FormEditor class within the Aspose.PDF for .NET library, designed for effortless manipulation of interactive PDF forms. This feature empowers developers to seamlessly add, edit, and configure form fields, with user-friendly methods to streamline the modification process. Optimize your PDF form handling by leveraging the comprehensive functionalities of FormEditor to elevate your document workflows",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "358",
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
    "url": "/net/exploring-features-of-formeditor-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/exploring-features-of-formeditor-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

{{% alert color="primary" %}}

PDF documents sometimes contain interactive form, which are known as AcroForm. It is just like a form used in the web pages. These forms contain different types of controls i.e. Text boxes, Check boxes, and Buttons etc. A developer working with PDF files might sometimes have to edit these forms. In this article, we’ll look into the details how [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) enables us to do that.

{{% /alert %}}

## Implementation details

Developers can use [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) not only to add new forms and form fields in a PDF document, but also allow you to edit existing fields. The scope of this article is limited to the features of [Aspose.PDF for .NET](/pdf/net/) which deal with the form editing.

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) is the class which contains most of the methods and properties which allow the developers to edit form fields. You can not only add new fields, but also remove existing fields, move one field to another position, change field name, or attributes etc. The list of the features provided by this class is quite comprehensive, and it is very easy to work with the form fields using this class.

These methods can be divided into two main categories, one of which is used to manipulate the fields, and the other is used to set the new attributes of these fields. The methods which we can group under first category include AddField, AddListItem, RemoveListItem, CopyInnerField, CopyOuterField, DelListItem, MoveField, RemoveField, and RenameField etc. In the second category of the methods SetFieldAlignment, SetFieldAppearance, SetFieldAttribute, SetFieldLimit, SetFieldScript can be included. The following code snippet shows you some of the methods of FormEditor class in working:


```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExploringFormEditorFeatures()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "inFile.pdf"))
    {
        // Create instance of FormEditor
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            // Add field in the PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "field1", 1, 300, 500, 350, 525);

            // Add List field in PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "field2", 1, 300, 200, 350, 225);

            // Add list items
            editor.AddListItem("field2", "item 1");
            editor.AddListItem("field2", "item 2");

            // Add submit button
            editor.AddSubmitBtn("submitbutton", 1, "Submit Form", "http:// Testwebsite.com/testpage", 200, 200, 250, 225);

            // Delete list item
                editor.DelListItem("field2", "item 1");

            // Move field to new position
            editor.MoveField("field1", 10, 10, 50, 50);

            // Remove existing field from the PDF
            editor.RemoveField("field1");

            // Rename an existing field
            editor.RenameField("field1", "newfieldname");

            // Reset all visual attributes to empty value
            editor.ResetFacade();

            // Set the alignment style of a text field
            editor.SetFieldAlignment("field1", Aspose.Pdf.Facades.FormFieldFacade.AlignLeft);

            // Set appearance of the field
            editor.SetFieldAppearance("field1", Aspose.Pdf.Annotations.AnnotationFlags.NoRotate);

            // Set field attributes i.e. ReadOnly, Required
            editor.SetFieldAttribute("field1", Aspose.Pdf.Facades.PropertyFlag.ReadOnly);

            // Set field limit
            editor.SetFieldLimit("field1", 25);

            // Save modifications in the output file
            editor.Save(dataDir + "FormEditorFeatures2_out.pdf");                    
        }
    }
}
```