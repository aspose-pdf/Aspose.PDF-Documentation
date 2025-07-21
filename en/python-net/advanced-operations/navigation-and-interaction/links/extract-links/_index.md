---
title: Extract Links from the PDF File using Python
linktitle: Extract Links
type: docs
weight: 30
url: /python-net/extract-links/
description: Discover how to extract hyperlinks from PDF documents in Python using Aspose.PDF for content management and link analysis.
lastmod: "2025-07-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to extract Links from PDF
Abstract: The Aspose.PDF for Python via .NET guide on extracting links explains how to programmatically retrieve hyperlink annotations from PDF documents using Python. The documentation includes practical code examples and highlights how this functionality can be used for tasks such as link auditing, navigation analysis, or building interactive document features. Whether you're working with single-page PDFs or processing large batches, this guide offers a clear and efficient approach to hyperlink extraction.    
---

## Extract Links from the PDF File

This example demonstrates how to iterate through all link annotations on the first page of a PDF using Aspose.PDF for Python. It filters annotations to identify those of type LinkAnnotation, safely casts them, and then prints their page index and rectangular position on the page.

This can be used for debugging, analytics, or automated updates to existing link annotations in a PDF.

1. Load the PDF document. Use ap.Document(path_infile) to open the file.
1. Access annotations from the first page. Use document.pages[1].annotations to retrieve all annotations.
1. Filter for LinkAnnotation types only. Check each annotation's annotation_type.
1. Cast and process LinkAnnotations. Use is_assignable() and cast() to ensure safe access to LinkAnnotation properties.
1. Print annotation details. Output the page index and rectangle (location) of each link.

```python

    import aspose.pdf as ap
    from os import path

    # Construct full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # (Optional) You can construct the output file path if needed later
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only LinkAnnotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Iterate over each link annotation
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (type-safe check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Safely cast the annotation to LinkAnnotation type
            annotation = cast(ap.annotations.LinkAnnotation, la)
            
            # Print annotation location and page index
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
            print(annotation.page_index)
```

## Extract HyperLinks from the PDF File

This code demonstrates how to extract all LinkAnnotation objects from the first page of a PDF document using Aspose.PDF for Python, and then identify those that contain a GoToURIAction. For each such link, it prints out the page index and the target URI.

This is useful for tasks like:

- Auditing external links in a PDF
- Extracting documentation or support URLs
- Detecting broken or outdated hyperlinks

1. Load the PDF document. Open the file using ap.Document.
1. Get all link annotations from the first page. Filter annotations to include only those with type AnnotationType.LINK.
1. Type check and cast to LinkAnnotation. Ensure each annotation is indeed a LinkAnnotation before accessing its properties.
1. Check the link’s action type. Filter for links that use a GoToURIAction (i.e., links to a web URL).
1. Extract and print the URI and page index. Use .uri to get the external link and .page_index for context.

```python

    import aspose.pdf as ap
    from os import path

    # Construct the full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # Optional: construct output file path if needed
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only link annotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Iterate through filtered link annotations
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (safe type check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Cast the annotation to LinkAnnotation to access link-specific properties
            annotation = cast(ap.annotations.LinkAnnotation, la)

            # Check if the link's action is of type GoToURIAction (external web link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                # Cast the action to GoToURIAction to access the URI property
                action = cast(ap.annotations.GoToURIAction, annotation.action)

                # Print the page number and the link's URI
                print(f"Page {annotation.page_index}, URI: {action.uri}")
```