---
title: Update Links in PDF using Python
linktitle: Update Links
type: docs
weight: 20
url: /python-net/update-links/
description: Update links in PDF programmatically. This guide is about how to update links in PDF in Python language.
lastmod: "2025-07-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to update Links in PDF
Abstract: The Aspose.PDF for Python via .NET guide on updating links walks developers through the process of modifying hyperlink behavior within PDF documents using Python. It explains how to change link destinations to point to specific pages, external websites, or even other PDF files. The documentation also covers how to adjust the appearance of link annotations, including text color, and provides practical code examples for each scenario. Whether you're correcting outdated URLs or enhancing navigation, this resource offers a clear and efficient approach to managing links programmatically.
---

## Update LinkAnnotation Text Color

This example shows how to detect all link annotations on the first page of a PDF using Aspose.PDF for Python, then highlight the text near each link by changing its font color to red. It uses TextFragmentAbsorber with a slightly expanded area around each link rectangle to find and modify nearby text.

This can be used for:

- Visually marking links in a document
- Enhancing accessibility by emphasizing linked content
- Preprocessing PDF files before review or export

For each of these link annotations, the script retrieves its rectangular boundary and slightly expands that region to include nearby text, allowing for broader visual identification. It then applies a TextFragmentAbsorber over this expanded area to extract any text fragments located within it. These captured fragments are modified by changing their font color to red, effectively marking the surrounding text for emphasis and review. After applying all these updates, the modified document is saved to the output path, preserving the highlighted annotations and their associated text.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Filter all link annotations on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Loop through each link annotation found
    for la in link_annotations:
        # Create a text absorber for extracting text fragments
        ta = ap.text.TextFragmentAbsorber()

        # Get the rectangle area of the annotation
        rect = la.rect

        # Expand the rectangle slightly to catch text near the link
        rect.llx -= 2  # Lower-left x
        rect.lly -= 2  # Lower-left y
        rect.urx += 2  # Upper-right x
        rect.ury += 2  # Upper-right y

        # Restrict text search to the adjusted rectangle
        ta.text_search_options = ap.text.TextSearchOptions(rect)

        # Apply the absorber to the first page
        ta.visit(document.pages[1])

        # Iterate through found text fragments and change their color to red
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    # Save the updated PDF document to the output path
    document.save(path_outfile)
```

## Update Border

The script focuses on the first page of the document and filters out all annotations, selecting only those of the LINK type—these typically represent interactive elements, such as hyperlinks or navigation triggers. For each of these link annotations, the code casts them to the LinkAnnotation type and updates their color property to red, visually highlighting them to stand out from other content. After all link annotations have been modified, the updated document is saved to the defined output location, preserving the new styling.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Get all annotations of type LINK on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Loop through each link annotation and change its color to red
    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red  # Highlight the link in red

    # Save the modified PDF to the output path
    document.save(path_outfile)
```    

## Update Web Destination

Once the paths are in place, the original document is loaded using the Aspose.PDF library, making its content accessible for modification. The script then focuses on the first page of the document, filtering out all annotations and selecting only those that are link-type, typically representing clickable areas or hyperlinks. To avoid type errors and ensure safe handling, each annotation is checked with is_assignable and then cast to the appropriate LinkAnnotation type. If the link is associated with a GoToURIAction, meaning it points to a web address, the script updates that URI to redirect users to "https://www.google.com". Finally, after all desired changes have been applied, the modified document is saved to the specified output path.

```python

    import aspose.pdf as ap
    from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the PDF document
document = ap.Document(path_infile)

# Find all LINK annotations on the first page
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]

# Loop through annotations and replace target URI
for la in link_annotations:
    # Ensure the annotation is a LinkAnnotation
    if is_assignable(la, ap.annotations.LinkAnnotation):
        annotation = cast(ap.annotations.LinkAnnotation, la)
        
        # Check if the action is of type GoToURIAction
        if is_assignable(annotation.action, ap.annotations.GoToURIAction):
            action = cast(ap.annotations.GoToURIAction, annotation.action)
            
            # Replace the existing URI with Google
            action.uri = "https://www.google.com"

# Save the modified document to output path
document.save(path_outfile)
```