---
title: Extract Tagged Content from PDF
linktitle: Extract Tagged Content
type: docs
weight: 20
url: /python-net/extract-tagged-content-from-tagged-pdfs/
description: This article explains how to extract tagged content PDF document using Aspose.PDF for Python via .NET
lastmod: "2025-06-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

In this article you will learn how to to extract tagged content PDF document using Python.

## Getting Tagged PDF Content

In order to get content of PDF Document with Tagged Text, Aspose.PDF offers [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) property of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class.

Following code snippet shows how to get content of a PDF document with Tagged Text:

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Work with Tagged PDF content
        # Set Title and Language for Document
        tagged_content.set_title("Simple Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Save Tagged PDF Document
        document.save(path_outfile)
```

## Getting Root Structure

In order to get the root structure of Tagged PDF Document, Aspose.PDF offers [struct_tree_root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties) property of [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) interface and [root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties).

Following code snippet shows how to get the root structure of Tagged PDF Document:

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Properties StructTreeRootElement and RootElement are used for access to
        # StructTreeRoot object of pdf document and to root structure element (Document structure element).
        struct_tree_root_element = tagged_content.struct_tree_root_element
        root_element = tagged_content.root_element
```

## Accessing Child Elements

In order to access child elements of a Tagged PDF Document, Aspose.PDF offers [ElementList](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/elementlist/) class. Following code snippet shows how to access child elements of a Tagged PDF Document:

```python

    import aspose.pdf as ap
    from aspose.pycore import *

    # Open PDF Document
    with ap.Document(path_infile) as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Access to root element(s)
        element_list = tagged_content.struct_tree_root_element.child_elements

        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = cast(ap.logical_structure.StructureElement, element)

                # Get properties
                title = structure_element.title
                language = structure_element.language
                actual_text = structure_element.actual_text
                expansion_text = structure_element.expansion_text
                alternative_text = structure_element.alternative_text

        # Access to child elements of first element in root element
        element_list = tagged_content.root_element.child_elements[1].child_elements
        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = element

                # Set properties
                structure_element.title = "title"
                structure_element.language = "fr-FR"
                structure_element.actual_text = "actual text"
                structure_element.expansion_text = "exp"
                structure_element.alternative_text = "alt"

        # Save Tagged PDF Document
        document.save(path_outfile)
```