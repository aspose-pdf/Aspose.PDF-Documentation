---
title: Flatten Annotation from PDF to XFDF 
type: docs
weight: 40
url: /net/flatten-annotation/
description: This section explains how to export annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

The flattening process means when an annotation is removed from a document, its visual representation is kept intact. A flattened annotation is still visible but is no longer editable by your users or by your app. This can be used, for example, to permanently apply annotations to your document or to make annotations visible to viewers that otherwise can’t show annotations. If not specified, an export will keep all annotations as they are.

When this option is selected, your annotations will be included in your exported PDF as PDF-standard annotations.

Check how the [flatteningAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations) method used in the next code snippet.

```csharp
public static void Flattening()
{
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.BindPdf(dataDir + "sample_cats_dogs.pdf");
    FlattenSettings flattenSettings = new FlattenSettings
    {
        ApplyRedactions = true,
        CallEvents = false,
        HideButtons = true,
        UpdateAppearances = true
    };
    annotationEditor.FlatteningAnnotations(flattenSettings);
    annotationEditor.Save(dataDir + "FlattenAnnotation.pdf");
}
```
