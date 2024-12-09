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

```csharp
public static void DeleteAllAnnotations()
{
    // Open document
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.BindPdf(dataDir + "sample_cats_dogs.pdf");
    // Delete all annoations
    annotationEditor.DeleteAnnotations();
    // Save updated PDF
    annotationEditor.Save(dataDir + "DeleteAllAnnotation.pdf");
}   
```

## Delete All Annotations by Specified Type

You can use [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class to delete all the annotations, by a specified annotation type, from the existing PDF file. In order to do that you need to create a [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) method, with the string parameter, to delete all the annotations from the file; the string parameter represents the annotation type to be deleted. Finally, use [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method to save the updated PDF file. The following code snippet shows you how to delete all annotations by specified annotation type.

```csharp
public static void DeleteAnnotation()
{
    // Open document
    var document = new Document(dataDir + "sample_cats_dogs.pdf");
    int index;
    for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
    {
        System.Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
    }
    System.Console.Write("Please enter number:");
    index = int.Parse(System.Console.ReadLine());

    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.BindPdf(document);
    annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

    // Save updated PDF
    annotationEditor.Save(dataDir + "DeleteAnnotation.pdf");
}
```
