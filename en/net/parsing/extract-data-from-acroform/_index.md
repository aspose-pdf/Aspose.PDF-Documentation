---
title:  Extract Data from AcroForm using C#
linktitle:  Extract Data from AcroForm
type: docs
weight: 50
url: /net/extract-data-from-acroform/
description: Aspose.PDF makes it easy to extract form field data from PDF files. Learn how to extract data from AcroForms and save it into JSON, XML, or FDF format.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Data from AcroForm using C#",
    "alternativeHeadline": "Effortlessly Extract Acrobat Form Data with C#",
    "abstract": "Discover the new functionality in Aspose.PDF for .NET that simplifies the extraction of form field data from AcroForms in PDF documents. With the ability to export data into JSON, XML, FDF, and XFDF formats, users can efficiently manage form data while leveraging concise code examples for seamless integration into applications",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "826",
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
    "url": "/net/extract-data-from-acroform/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-data-from-acroform/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Extract form fields from PDF document

As well as enabling you to generate form fields and fill form fields, Aspose.PDF for .NET makes it easy to extract form field data or information about form fields from PDF files.

In the sample code below we demonstrate how to iterate through each page in a PDF to extract information about all of the AcroForm in the PDF as well as the form field values. This sample code presumes that you don’t know the name of the form fields in advance.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExtractFormFields()
{
    // Load source PDF document
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {

        // Get values from all fields
        foreach (Aspose.Pdf.Forms.Field formField in document.Form)
        {
            Console.WriteLine("Field Name : {0} ", formField.PartialName);
            Console.WriteLine("Value : {0} ", formField.Value);
        }
    }
}
```

If you do know the name of the form fields that you wish to extract values from then you can use indexer in Documents.Form collection to quickly retrieve this data. Look at the bottom of this article for a sample code on how to use that function.

## Retrieve form field value by title

The form field's Value property allows you to get the value of a particular field. To get the value, get the form field from the Document object's Form collection. This example selects a TextBoxField and retrieves its value using the Value property.

## Extract form fields from PDF document to JSON

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExtractFormFieldsToJson()
{
    // Load source PDF document
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {
        // Extract form fields and convert to JSON
        var formData = document.Form.Cast<Aspose.Pdf.Forms.Field>().Select(f => new { Name = f.PartialName, f.Value });
        string jsonString = System.Text.Json.JsonSerializer.Serialize(formData);

        // Output the JSON string
        Console.WriteLine(jsonString);
    }
}
```

## Extract Data to XML from a PDF File

Form class allows you to export data to an XML file from the PDF file using ExportXml method. In order to export data to XML, you need to create an object of Form class and then call the ExportXml method using the FileStream object. Finally, you can close FileStream object and dispose Form object. The following code snippet shows you how to export data to XML file.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExportFormDataToXml()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Open form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        form.BindPdf(dataDir + "input.pdf");

        // Create xml file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            form.ExportXml(xmlOutputStream);
        }
    }
}
```

## Export Data to FDF from a PDF File

Form class allows you to export data to an FDF file from the PDF file using ExportFdf method. In order to export data to FDF, you need to create an object of Form class and then call the ExportFdf method using the FileStream object. Finally, you can save the PDF file using Save method of the Form class. The following code snippet shows you how to export data to FDF file.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExportDataToPdf()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Open Document
        form.BindPdf(dataDir + "input.pdf");

        // Create fdf file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            form.ExportFdf(fdfOutputStream);
        }

        // Save updated document
        form.Save(dataDir + "ExportDataToPdf_out.pdf");
    }
}
```

## Export Data to XFDF from a PDF File

Form class allows you to export data to an XFDF file from the PDF file using ExportXfdf method. In order to export data to XFDF, you need to create an object of Form class and then call the ExportXfdf method using the FileStream object. Finally, you can save the PDF file using Save method of the Form class. The following code snippet shows you how to export data to XFDF file.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExportDataToXFDF()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Open Document
        form.BindPdf(dataDir + "input.pdf");

        // Create xfdf file
        using (var xfdfOutputStream = new FileStream(dataDir + "student1.xfdf", FileMode.Create))
        {
            // Export data
            form.ExportXfdf(xfdfOutputStream);
        }

        // Save updated document
        form.Save(dataDir + "ExportDataToXFDF_out.pdf");
    }
}
```
