---
title: Extract Tagged Content from PDFs in Python
linktitle: Extract Tagged Content
type: docs
weight: 20
url: /python-net/extract-tagged-content-from-tagged-pdfs/
description: Learn how to extract tagged PDF content in Python with Aspose.PDF for Python via .NET, including access to tagged content, root structure, and child structure elements.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

In this article, you will learn how to extract tagged content from PDF documents using Python.

Use these examples when you need to inspect a tagged PDF, read the logical structure tree, or validate that structure elements were created correctly for accessibility workflows.

## Getting Tagged PDF Content

In order to get content of PDF Document with Tagged Text, Aspose.PDF offers [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) property of [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class.

Create an advanced, fully tagged PDF document with a structured and hierarchical Table of Contents (TOC):

1. Create a new Document object.
1. Access the tagged_content property.
1. Set the document title using 'set_title()'.
1. Set the document language using 'set_language()'.
1. Save the document.

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

# region Extract Tagged Content from PDF
def get_tagged_content(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Work with Tagged PDF content
        # Set Title and Language for Document
        tagged_content.set_title("Simple Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Getting Root Structure

Tagged PDFs contain a logical structure tree that defines the semantic structure of the document. The StructTreeRoot represents the root of this logical tree, while the RootElement provides an interface to interact with the top-level structure element of the document.

Following code snippet shows how to get the root structure of Tagged PDF Document:

1. Create a new tagged PDF document.
1. Access tagged content and set metadata.
1. Access StructTreeRoot and RootElement.
1. Save the tagged PDF.

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def get_root_structure(outfile):

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

        print(f"StructTreeRootElement: {struct_tree_root_element}")
        print(f"RootElement: {root_element}")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Accessing Child Elements

Tagged PDFs contain a logical structure tree that defines the semantic hierarchy of the document (headings, paragraphs, forms, lists, etc.). Accessing and modifying these structure elements allows you to:

- Inspect metadata such as title, language, actual_text, and accessibility-related properties
- Update properties for improved accessibility or localization
- Programmatically adjust the logical document structure for PDF/UA compliance

 Following code snippet shows how to access child elements of a Tagged PDF Document:

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def access_child_elements(infile, outfile):

    # Open PDF Document
    with ap.Document(infile) as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Access to root element(s)
        element_list = tagged_content.struct_tree_root_element.child_elements

        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = cast(ap.logicalstructure.StructureElement, element)
                # Get properties
                print(
                    "StructureElement properties - "
                    f"title: {structure_element.title}, "
                    f"language: {structure_element.language}, "
                    f"actual_text: {structure_element.actual_text}, "
                    f"expansion_text: {structure_element.expansion_text}, "
                    f"alternative_text: {structure_element.alternative_text}"
                )

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
        document.save(outfile)
```

## Related Tagged PDF Topics

- [Create Tagged PDF](/pdf/python-net/create-tagged-pdf/) to build accessible tagged documents before inspecting their structure.
- [Setting Structure Elements Properties](/pdf/python-net/setting-structure-elements-properties/) to update semantic properties after extracting structure elements.
- [Working with Table in Tagged PDFs](/pdf/python-net/working-with-table-in-tagged-pdfs/) for tagged-table accessibility workflows.