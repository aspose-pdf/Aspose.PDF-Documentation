---
title: Flatten Annotation from PDF File to XFDF (facades)
type: docs
weight: 40
url: /java/flatten-annotation/
description: This section explains how to export annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

The flattening process means when an annotation is removed from a document, its visual representation is kept intact. A flattened annotation is still visible but is no longer editable by your users or by your app. This can be used, for example, to permanently apply annotations to your document or to make annotations visible to viewers that otherwise can’t show annotations. If not specified, an export will keep all annotations as they are.

When this option is selected, your annotations will be included in your exported PDF as PDF-standard annotations.

Check how the [flatteningAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#flatteningAnnotations--) method used in the next code snippet.

```java
public static void Flattening() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        FlattenSettings flattenSettings = new FlattenSettings();
        flattenSettings.setApplyRedactions(true);
        flattenSettings.setCallEvents(false);
        flattenSettings.setHideButtons(true);
        flattenSettings.setUpdateAppearances(true);
        annotationEditor.flatteningAnnotations(flattenSettings);
        annotationEditor.save(_dataDir + "FlattenAnnotation.pdf");
    }
```
