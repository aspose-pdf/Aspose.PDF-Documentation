---
title: Interactive Annotations using Python
linktitle: Interactive Annotations
type: docs
weight: 60
url: /python-net/interactive-annotations/
description: Learn how to add, read, and delete link annotations, and how to create navigation and print buttons in PDF documents using Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Work with interactive PDF annotations and buttons in Python.
Abstract: This article explains how to work with interactive annotations in PDF files using Aspose.PDF for Python via .NET. It covers adding link annotations, reading existing link areas, deleting link annotations, creating page navigation buttons, and adding a print button to a PDF document.
---

This article shows how to work with interactive annotations in PDF documents using Aspose.PDF for Python via .NET.

The example script demonstrates several common workflows:

- add a link annotation to existing text
- get link annotation rectangles from a page
- delete link annotations
- create navigation buttons
- create a print button

## Link Annotation

### Add Link Annotation

This example searches the first page for the text fragment `"file"` and places a clickable link annotation over the matching text area. When the user clicks the annotation, the PDF opens the specified web address.

#### Load the document and find the target text

Create a `Document` object and use `TextFragmentAbsorber` to search for the text that will become interactive.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

document.pages[1].accept(text_fragment_absorber)
phone_number_fragment = text_fragment_absorber.text_fragments[1]
```

#### Create the link annotation

Build a `LinkAnnotation` using the rectangle of the matched text fragment and assign a URI action to it.

```python
link_annotation = ap.annotations.LinkAnnotation(
    document.pages[1], phone_number_fragment.rectangle
)
link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")
```

#### Add the annotation and save the PDF

Append the annotation to the page and save the updated file.

```python
document.pages[1].annotations.append(link_annotation)
document.save(outfile)
```

#### Complete example

```python
def link_add(infile, outfile):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

    document.pages[1].accept(text_fragment_absorber)
    phone_number_fragment = text_fragment_absorber.text_fragments[1]

    link_annotation = ap.annotations.LinkAnnotation(
        document.pages[1], phone_number_fragment.rectangle
    )
    link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")

    document.pages[1].annotations.append(link_annotation)
    document.save(outfile)
```

### Get Link Annotation

To inspect existing interactive links, filter the annotations collection on the first page and keep only items whose type is `LINK`. The sample then prints the rectangle for each matching annotation.

#### Load the PDF and collect link annotations

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Read the annotation rectangles

Loop through the filtered annotations and print the coordinates of each link area.

```python
for link_annotation in link_annotations:
    print(link_annotation.rect)
```

#### Complete example

```python
def link_get(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        print(link_annotation.rect)
```

### Delete Link Annotation

This workflow removes all link annotations from the first page and saves the cleaned PDF as a new file.

#### Find the link annotations to remove

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Delete each link annotation

```python
for link_annotation in link_annotations:
    document.pages[1].annotations.delete(link_annotation)
```

#### Save the updated document

```python
document.save(outfile)
```

#### Complete example

```python
def link_delete(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        document.pages[1].annotations.delete(link_annotation)

    document.save(outfile)
```

## Widget Annotation

### Add Navigation Button

Navigation buttons are useful in multi-page PDFs when you want readers to move between pages without using the viewer interface. This sample adds `Previous Page` and `Next Page` buttons to each page.

#### Define button settings

Store the button captions, positions, and predefined actions in a simple configuration list.

```python
button_config = [
    ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
    ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
]
```

#### Load the PDF and ensure multiple pages exist

The sample opens the source document and adds one more page so the navigation actions have at least two pages to work with.

```python
document = ap.Document(infile)
document.pages.add()
```

#### Create the buttons on each page

For every page, create a `ButtonField`, set its text and colors, assign a predefined navigation action, and add it to the form.

```python
for page in document.pages:
    for name, x_pos, action in button_config:
        rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
        button = ap.forms.ButtonField(page, rect)
        button.partial_name = name
        button.value = name
        button.characteristics.border = ap.Color.red.to_rgb()
        button.characteristics.background = ap.Color.orange.to_rgb()
        button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
        document.form.add(button)
```

#### Save the result

```python
document.save(outfile)
```

#### Complete example

```python
def navigation_buttons_add(infile, outfile):
    button_config = [
        ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
        ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
    ]

    document = ap.Document(infile)
    document.pages.add()

    for page in document.pages:
        for name, x_pos, action in button_config:
            rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ap.forms.ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

### Add Print Button

This example creates a new one-page PDF and places a print button near the top of the page. Clicking the button triggers the predefined print action in a compatible PDF viewer.

#### Create a new PDF and add a page

```python
document = ap.Document()
page = document.pages.add()
```

#### Create and configure the button

Define the button rectangle, create the `ButtonField`, set its caption, and attach the print action.

```python
rect = ap.Rectangle(72, 748, 164, 768, True)

print_button = ap.forms.ButtonField(page, rect)
print_button.alternate_name = "Print current document"
print_button.color = ap.Color.black
print_button.partial_name = "printBtn1"
print_button.value = "Print Document"
print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
    ap.annotations.PredefinedAction.FILE_PRINT
)
```

#### Set border and background styles

The sample defines a solid border and applies custom colors to make the button visible in the document.

```python
border = ap.annotations.Border(print_button)
border.style = ap.annotations.BorderStyle.SOLID
border.width = 2
print_button.border = border

print_button.characteristics.border = ap.Color.blue.to_rgb()
print_button.characteristics.background = ap.Color.light_blue.to_rgb()
```

#### Add the button and save the PDF

```python
document.form.add(print_button)
document.save(outfile)
```

#### Complete example

```python
def print_button_add(infile, outfile):
    document = ap.Document()
    page = document.pages.add()

    rect = ap.Rectangle(72, 748, 164, 768, True)

    print_button = ap.forms.ButtonField(page, rect)
    print_button.alternate_name = "Print current document"
    print_button.color = ap.Color.black
    print_button.partial_name = "printBtn1"
    print_button.value = "Print Document"
    print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
        ap.annotations.PredefinedAction.FILE_PRINT
    )

    border = ap.annotations.Border(print_button)
    border.style = ap.annotations.BorderStyle.SOLID
    border.width = 2
    print_button.border = border

    print_button.characteristics.border = ap.Color.blue.to_rgb()
    print_button.characteristics.background = ap.Color.light_blue.to_rgb()

    document.form.add(print_button)
    document.save(outfile)
```

## Related Topics

- [Import and Export Annotations](/python-net/import-export-annotations/)
- [Markup Annotations](/python-net/markup-annotations/)
- [Media Annotations](/python-net/media-annotations/)
- [Security Annotations](/python-net/security-annotations/)
- [Shape Annotations](/python-net/shape-annotations/)
- [Text Based Annotations](/python-net/text-based-Annotations/)
- [Watermark Annotations](/python-net/watermark-annotations/)
