---
title: Edit PDF File Tags using Python
linktitle: Edit Tags
type: docs
weight: 70
url: /python-net/edit-pdf-file-tags/
description: This article explains how to edit tags in the PDF documents using Aspose.PDF for Python via .NET library.
lastmod: "2025-06-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Tagged PDFs are designed to ensure accessibility by marking each element—such as text, images, and links—with tags that define their purpose and role in the document. When editing these PDFs, it's crucial to preserve these tags to maintain compliance with accessibility standards.

Tools like Aspose.PDF for Python via .NET offer robust functionality for handling tagged content, but care must be taken to uphold the document’s structure and accessibility. By methodically adding alt text to images or formatting paragraphs, tagged PDFs remain accessible and user-friendly.

Methods:

- tag (add tags to specific operators like images, text, and links).
- insert_child.
- remove_child.
- clear_childs.

These methods allow you to edit pdf file tags, for example:

- Search and Wrap Content with BDC Operators
- Tag Paragraph with Text
- Tag an Image with a Figure Element
- Style and Tag Two Text Spans
- Create and Tag Link Elements
- Remove the first child structure element (likely an old, unused one).
- Save the Updated PDF

```python

    import aspose.pdf as ap
    from aspose.pycore import *
    import uuid

    #  Open PDF document
    with (ap.Document(path_infile) as document):
        # Get first page
        page = document.pages[1]
        # The marked content operator on page for the text.
        text_1_bdc = None
        link_2_bdc = None
        link_1_bdc = None
        # Find the marked content operators for the elements on the page.
        for i in range(1, page.contents.length + 1):
            op = page.contents[i]
            if is_assignable(op, ap.operators.BDC):
                bdc = cast(ap.operators.BDC, op)
                # The text operator with marked content id = 0 was found.
                if bdc.properties.mcid == 0:
                    hello_bdc = bdc
            if is_assignable(op, ap.operators.Do):
                do_x_obj = cast(ap.operators.Do, op)
                # Wrap the image XObject with marked content operator.
                image_bdc = ap.operators.BDC("Figure")
                page.contents.insert(i - 2, image_bdc)
                i += 1
                page.contents.insert(i + 1, ap.operators.EMC())
                i += 1
            if is_assignable(op, ap.operators.TextShowOperator):
                tx = cast(ap.operators.TextShowOperator, op)
                # Wrap the text operator on page with marked content operator.
                if "efter Ukendt forfatter er licenseret under" in tx.text:
                    text_1_bdc = ap.operators.BDC("P")
                    page.contents.insert(i - 1, text_1_bdc)
                    i += 1
                    page.contents.insert(i + 1, ap.operators.EMC())
                    i += 1
                # Wrap the text operator on page with marked content operator.
                if "CC" in tx.text:
                    link_1_bdc = ap.operators.BDC("Link")
                    page.contents.insert(i - 1, link_1_bdc)
                    i += 1
                    page.contents.insert(i + 1, ap.operators.EMC())
                    i += 1
                # Wrap the text operator on page with marked content operator.
                if "Dette billede" in tx.text:
                    link_2_bdc = ap.operators.BDC("Link")
                    page.contents.insert(i - 1, link_2_bdc)
                    i += 1
                    page.contents.insert(i + 1, ap.operators.EMC())
                    i += 1

        tagged = document.tagged_content
        # Find exist struct element in document.
        hello_paragraph = tagged.root_element.child_elements[1]
        # Clear the subtree of an existing structure tree element.
        hello_paragraph.clear_childs()
        # Tag paragraph struct element to text on page.
        hello_mcr = hello_paragraph.tag(hello_bdc)
        # Fill the paragraph struct element spaceAfter attribute.
        hello_space_after = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.SPACE_AFTER)
        hello_space_after.set_number_value(30.625)
        # Create a figure element and place it to root element in second position.
        figure = tagged.create_figure_element()
        tagged.root_element.insert_child(figure, 2, True)
        # Set an alternative text for the figure.
        figure.alternative_text = "A fly."
        # Tag figure struct element to image element on page.
        figure_mcr = figure.tag(image_bdc)
        # Find exist struct element in document.
        p2 = cast(ap.logicalstructure.StructureElement,tagged.root_element.child_elements[3])
        # Clear the subtree of an existing structure tree element.
        p2.clear_childs()
        # Create the span struct element.
        span1 = tagged.create_span_element()
        # Get the span1 struct element attributes.
        span1_attrs = span1.attributes.create_attributes(ap.logicalstructure.AttributeOwnerStandard.LAYOUT)
        # Fill the span1 struct element textDecorationType attribute.
        span1_text_decoration_type = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.TEXT_DECORATION_TYPE)
        span1_text_decoration_type.set_name_value(ap.logicalstructure.AttributeName.TEXT_DECORATION_TYPE_UNDERLINE)
        span1_attrs.set_attribute(span1_text_decoration_type)
        # Fill the span1 struct element textDecorationThickness attribute.
        span1_text_decoration_thickness = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.TEXT_DECORATION_THICKNESS)
        span1_text_decoration_thickness.set_number_value(0)
        span1_attrs.set_attribute(span1_text_decoration_thickness)
        # Fill the span1 struct element textDecorationColor attribute.
        span1_text_decoration_color = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.TEXT_DECORATION_COLOR)
        span1_text_decoration_color.set_array_number_value([0.0196075, 0.384308, 0.756866 ])
        span1_attrs.set_attribute(span1_text_decoration_color)
        # Append the span element to the paragraph element in the struct tree.
        p2.append_child(span1, True)
        # Create the span struct element.
        span2 = tagged.create_span_element()
        # Get the span2 struct element attributes.
        span2_attrs = span2.attributes.create_attributes(ap.logicalstructure.AttributeOwnerStandard.LAYOUT)
        # Fill the span2 struct element textDecorationType attribute.
        text_decoration_type = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.TEXT_DECORATION_TYPE)
        text_decoration_type.set_name_value(ap.logicalstructure.AttributeName.TEXT_DECORATION_TYPE_UNDERLINE)
        span2_attrs.set_attribute(text_decoration_type)
        # Fill the span2 struct element textDecorationThickness attribute.
        text_decoration_thickness = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.TEXT_DECORATION_THICKNESS)
        text_decoration_thickness.set_number_value(0)
        span2_attrs.set_attribute(text_decoration_thickness)
        # Fill the span2 struct element textDecorationColor attribute.
        text_decoration_color = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.TEXT_DECORATION_COLOR)
        text_decoration_color.set_array_number_value([ 0.0196075, 0.384308, 0.756866 ])
        span2_attrs.set_attribute(text_decoration_color)
        # Append the span struct element to the struct element tree.
        p2.append_child(span2, True)
        # Create the link struct element.
        link2 = tagged.create_link_element()
        # Set an id attribute of struct element.
        link2.set_id(str(uuid.uuid4()))
        # Append the link struct element to the struct element tree.
        span2.append_child(link2, True)
        # Tag link struct element to the page annotation element.
        link2.tag(page.annotations[1])
        # Tag link struct element to text element on page.
        link2.tag(link_2_bdc)
        # Create the link struct element.
        link1 = tagged.create_link_element()
        # Set an id attribute of struct element.
        link1.set_id(str(uuid.uuid4()))
        # Append the link struct element to the struct element tree.
        span1.append_child(link1, True)
        # Tag link struct element to the page annotation element.
        link1.tag(page.annotations[2])
        # Tag link struct element to text element on page.
        link1.tag(link_1_bdc)
        # Remove the struct element at index 0 from the struct tree.
        tagged.root_element.remove_child(0)
        # Save PDF document
        document.save(path_outfile)
```
