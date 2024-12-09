---
title: Modify Annotations in your PDF 
type: docs
weight: 50
url: /net/modify-annotations/
description: This section explains how to modify annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modify Annotations in your PDF",
    "alternativeHeadline": "Enhance Your PDF Annotations with New Modifications",
    "abstract": "The Modify Annotations feature allows users to easily edit key attributes of annotations in PDF files using Aspose.PDF Facades. This functionality includes changing the subject, author, color, and more, along with options to delete annotations by type, streamlining the PDF annotation management process. Optimize your PDF workflow by leveraging these powerful annotation modification capabilities",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "290",
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
    "url": "/net/modify-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modify-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Modify annotation

[ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) method allows you to change basic attributes of an annotation i.e. Subject, Modified date, Author, Annotation color, and Open flag. You can also set Author directly by using ModifyAnnotations method. This class also provides two overloaded methods to delete annotations. The first method called DeleteAnnotations deletes all the annotations from a PDF file.  

For example, in the following code, consider changing the author in our annotation using [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor).

```csharp
public static void ModifyAnnotationsAuthor()
{
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.BindPdf(dataDir + "sample_cats_dogs.pdf");
    annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
    annotationEditor.Save(dataDir + "ModifyAnnotationsAuthor.pdf");
}
```

The second method allows you to delete all the annotations of a specified type.

```csharp
public static void ModifyAnnotations()
{
    var document = new Document(dataDir + "sample_cats_dogs.pdf");
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.BindPdf(document);

    // Create a new object of type Annotation to modify annotation attributes
    var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance();
    Aspose.Pdf.Annotations.FreeTextAnnotation annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
        document.Pages[1],
        new Aspose.Pdf.Rectangle(1, 1, 1, 1),
        defaultAppearance)
    {
        // Set new annotation attributees
        Title = "Aspose.PDF Demo User",
        Subject = "Technical Article"
    };
    // Modify annotations in the PDF file
    annotationEditor.ModifyAnnotations(1, 1, annotation);
    annotationEditor.Save(dataDir + "ModifyAnnotations.pdf");
}
```

## See also

Try to compare and find a way to work with annotations that suits you. Lets learn [PDF Annotations](/pdf/net/annotations/) section.