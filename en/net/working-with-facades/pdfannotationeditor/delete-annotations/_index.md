---
title: Delete Annotations (facades)
type: docs
weight: 10
url: /net/delete-annotations/
description: This section explains how to delete annotations with Aspose.PDF Facades using PdfAnnotationEditor Class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete Annotations (facades)",
    "alternativeHeadline": "Effortlessly Remove Specific PDF Annotations with Ease",
    "abstract": "The Aspose.PDF for .NET Facades feature allows users to efficiently delete annotations from existing PDF files using the PdfAnnotationEditor class. With the ability to remove all annotations or target specific annotation types, users can streamline document editing and enhance their PDF management capabilities. This functionality simplifies the process of maintaining clean and focused PDF documents by providing straightforward methods for annotation deletion",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "427",
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
    "url": "/net/delete-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/delete-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Delete All Annotations from an Existing PDF File

[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) allows you delete all the annotations from the existing PDF file. First off, create a [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) method to delete all the annotations from the file, and then use [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method to save the updated PDF file. The following code snippet shows you how to delete all the annotations from the PDF file.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET

private static void DeleteAllAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create an instance of PdfAnnotationEditor
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Open a PDF document
        annotationEditor.BindPdf(dataDir + "DeleteAllAnnotationsFromPage.pdf");

        // Delete all annoations
        annotationEditor.DeleteAnnotations();

        // Save the updated PDF file
        annotationEditor.Save(dataDir + "DeleteAllAnnotationsFromPage_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET

private static void DeleteAllAnnotations()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create an instance of PdfAnnotationEditor
    using var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor();

    // Open a PDF document
    annotationEditor.BindPdf(dataDir + "DeleteAllAnnotationsFromPage.pdf");

    // Delete all annoations
    annotationEditor.DeleteAnnotations();

    // Save the updated PDF file
    annotationEditor.Save(dataDir + "DeleteAllAnnotationsFromPage_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}



## Delete All Annotations by Specified Type

You can use [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class to delete all the annotations, by a specified annotation type, from the existing PDF file. In order to do that you need to create a [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) method, with the string parameter, to delete all the annotations from the file; the string parameter represents the annotation type to be deleted. Finally, use [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method to save the updated PDF file. The following code snippet shows you how to delete all annotations by specified annotation type.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET

private static void DeleteAllAnnotationByType()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open a PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotations.pdf"))
    {
        // Collect all annotation types from all pages
        var annotationTypes = new List<string>();
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            // If page has no annotations, skip it
            if (page.Annotations == null)
            {
                continue;
            }

            // Retrieve each annotation type from the page
            IEnumerable<string> pageAnnotationTypes = page.Annotations.Select(ann => ann.AnnotationType.ToString());
            annotationTypes.AddRange(pageAnnotationTypes);
        }

        // Make the list of annotation types distinct
        annotationTypes = annotationTypes.Distinct().ToList();

        // Display each annotation type to the user
        int index;
        for (index = 0; index < annotationTypes.Count; index++)
        {
            Console.WriteLine($"{index + 1}. {annotationTypes[index]}");
        }

        // Prompt user to choose the annotation type to delete
        Console.Write("Please enter number: ");
        index = int.Parse(Console.ReadLine()) - 1;

        // Create an instance of PdfAnnotationEditor
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Open a PDF document
            annotationEditor.BindPdf(document);

            // Delete the annotation selected by the user
            annotationEditor.DeleteAnnotations(annotationTypes[index]);

            // Save the updated PDF file
            annotationEditor.Save(dataDir + "DeleteAllAnnotationByType_out.pdf");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET

private static void DeleteAllAnnotationByType()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open a PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotations.pdf");

    // Collect all annotation types from all pages
    var annotationTypes = new List<string>();
    foreach (Aspose.Pdf.Page page in document.Pages)
    {
        // If page has no annotations, skip it
        if (page.Annotations == null)
        {
            continue;
        }

        // Retrieve each annotation type from the page
        IEnumerable<string> pageAnnotationTypes = page.Annotations.Select(ann => ann.AnnotationType.ToString());
        annotationTypes.AddRange(pageAnnotationTypes);
    }

    // Make the list of annotation types distinct
    annotationTypes = annotationTypes.Distinct().ToList();

    // Display each annotation type to the user
    int index;
    for (index = 0; index < annotationTypes.Count; index++)
    {
        Console.WriteLine($"{index + 1}. {annotationTypes[index]}");
    }

    // Prompt user to choose the annotation type to delete
    Console.Write("Please enter number: ");
    index = int.Parse(Console.ReadLine()) - 1;

    // Create an instance of PdfAnnotationEditor
    using var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor();

    // Open a PDF document
    annotationEditor.BindPdf(document);

    // Delete the annotation selected by the user
    annotationEditor.DeleteAnnotations(annotationTypes[index]);

    // Save the updated PDF file
    annotationEditor.Save(dataDir + "DeleteAllAnnotationByType_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Delete an Annotation by Specified Name

You can use the [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class to delete a specific annotation, by its **unique name**, from an existing PDF file. In order to do that, you need to create a [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind input input PDF file using the [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call the [DeleteAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotation) method, passing the name of the annotation to delete.  Finally, use the [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method to store the updated PDF file. The following code snippet shows you how to delete an annotation by its name.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET

private static void DeleteAnnotationByName()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open a PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotations.pdf"))
    {
        // Display the list of annotations in the first page (adjust as needed for multiple pages)
        int index;
        for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
        {
            Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
        }

        // Prompt the user to enter the index of the annotation to delete
        Console.Write("Please enter number: ");
        index = int.Parse(Console.ReadLine());

        // Create an instance of PdfAnnotationEditor
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Open a PDF document
            annotationEditor.BindPdf(document);

            // Delete the annotation selected by the user
            annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

            // Save the updated PDF file
            annotationEditor.Save(dataDir + "DeleteAnnotationByName_out.pdf");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET

private static void DeleteAnnotationByName()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open a PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotations.pdf");

    // Display the list of annotations in the first page (adjust as needed for multiple pages)
    int index;
    for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
    {
        Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
    }

    // Prompt the user to enter the index of the annotation to delete
    Console.Write("Please enter number: ");
    index = int.Parse(Console.ReadLine());

    // Create an instance of PdfAnnotationEditor
    using var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor();

    // Open a PDF document
    annotationEditor.BindPdf(document);

    // Delete the annotation selected by the user
    annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

    // Save the updated PDF file
    annotationEditor.Save(dataDir + "DeleteAnnotationByName_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}
