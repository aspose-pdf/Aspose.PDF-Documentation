---
title: Create Links in PDF file with Python
linktitle: Create Links
type: docs
weight: 10
url: /python-net/create-links/
description: This section explains how to create links in your PDF document with Python.
lastmod: "2025-07-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to create Links in PDF
Abstract: The Aspose.PDF for Python via .NET guide on creating links provides developers with practical instructions for adding interactive hyperlinks to PDF documents using Python. It covers how to create various types of links, including those that launch external applications, navigate to specific pages within the same document, or open other PDF files. The documentation explains how to use LinkAnnotation objects, define clickable areas with Rectangle, and assign actions like LaunchAction or GoToRemoteAction. With clear code examples and step-by-step guidance, this resource helps developers enhance PDF navigation and interactivity in their Python applications.
---

## Links in PDF Documents

According to the PDF 1.7 specification (ISO 32000-1:2008), a **Link annotation** can trigger several types of actions that define what happens when the annotation is activated. Here are the primary actions supported:

1. **GoTo** – Navigates to a destination within the same document.
1. **GoToR** – Jumps to a destination in another PDF file (remote go-to).
1. **URI** – Opens a uniform resource identifier, typically a web link.
1. **Launch** – Launches an application or opens a file (platform-dependent and often restricted for security).
1. **Named** – Executes a predefined action, such as going to the next page or printing the document.
1. **JavaScript** – Executes embedded JavaScript code (used with caution due to security concerns).
1. **SubmitForm** – Submits form data to a specified URL.
1. **ResetForm** – Resets form fields to their default values.
1. **ImportData** – Imports data into the document from an external file.

By adding a link to an application into a document, it is possible to link to applications from a document. This is useful when you want readers to take a certain action at a specific point in a tutorial, for example, or to create a feature-rich document.

To create an application link with 'LaunchAction':

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the input PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific dimensions and position
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Configure the link's border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width of 5 units
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link appearance
    link.color = ap.Color.green  # Green color for the link

    # Set the action to launch another PDF file
    # Note: Commented out system command demonstrates potential alternative launch actions
    # link.action = ap.annotations.LaunchAction(document, "start %windir%\explorer.exe")
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

## Create PDF Document Link in a PDF File

### Using GoToRemoteAction

This code snippet demonstrates how to add a link annotation to a specific page of a PDF document using a Python PDF library.

1. Open the PDF document
1. Select the second page of the document (index 1)
1. Create a link annotation:
1. Positioned at coordinates (10, 580, 120, 600)
1. Colored green
1. Links to 'sample.pdf' on its first page
1. Add the link annotation to the page
1. Save the modified document to the output file path

To create a PDF document link using 'GoToRemoteAction':

```python

import aspose.pdf as ap
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the input PDF document
document = ap.Document(path_infile)

# Access the first page of the document (Aspose uses 1-based indexing)
page = document.pages[1]

# Create a link annotation in the specified rectangle area on the page
link = ap.annotations.LinkAnnotation(
    page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
)

# Set the color of the link annotation to green
link.color = ap.Color.green

# Define a remote action to open "sample.pdf" and navigate to its first page
link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)

# Add the link annotation to the current page
page.annotations.append(link)

# Save the updated PDF to the specified output path
document.save(path_outfile)
```

### Using GoToAction

This code demonstrates how to add a link annotation to a specific page of a PDF document using Aspose.PDF for Python. The link appears as a green, dashed-bordered rectangle and allows the user to navigate to another page within the same PDF. To create a PDF document link using 'GoToAction':

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific coordinates
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Customize link annotation border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link color to green
    link.color = ap.Color.green

    # Set link destination
    if document.pages.count >= 4:
        # Link to 4th page if document has 4 or more pages
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        # Fallback: link to the last page if less than 4 pages
        link.action = ap.annotations.GoToAction(document.pages[document.pages.count])

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

### Appling GoToURIAction

Next example demonstrates how to add a link annotation to a PDF document using Aspose.PDF for Python. The link appears as a green clickable area on the first page, and when clicked, it opens the Aspose.PDF for Python documentation in a web browser via a GoToURIAction.

This functionality is useful for embedding helpful external references, documentation, or support links directly within your PDFs.

1. Load the PDF Document. Open the existing PDF file using ap.Document.
1. Access the First Page. Use document.pages[1] to access the first page (Aspose uses 1-based indexing).
1. Create a Link Annotation. Create a LinkAnnotation object and specify the clickable rectangular area using ap.Rectangle.
1. Set Annotation Appearance. Set the annotation’s color to green using link.color = ap.Color.green.
1. Assign a URI Action. Use GoToURIAction to link the annotation to an external URL.
1. Add the Annotation to the Page. Append the configured link annotation to the first page’s annotations collection.
1. Save the Modified Document. Save the updated PDF document to the specified output path.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Access the first page (Aspose uses 1-based indexing)
    page = document.pages[1]

    # Create a link annotation at the specified rectangle position
    link = ap.annotations.LinkAnnotation(
        page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
    )

    # Set the color of the link annotation to green
    link.color = ap.Color.green

    # Define a URI action that navigates to the Aspose.PDF Python documentation
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified PDF to the output path
    document.save(path_outfile)
```
