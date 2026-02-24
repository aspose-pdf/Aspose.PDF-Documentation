---
title: استخراج المحتوى الموسوم من PDF
linktitle: استخراج المحتوى الموسوم
type: docs
weight: 20
url: /ar/python-net/extract-tagged-content-from-tagged-pdfs/
description: تشرح هذه المقالة كيفية استخراج محتوى موسوم من مستند PDF باستخدام Aspose.PDF للغة Python عبر .NET
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

في هذه المقالة ستتعلم كيفية استخراج محتوى موسوم من مستند PDF باستخدام Python.

## الحصول على محتوى PDF الموسوم

من أجل الحصول على محتوى مستند PDF بنص موسوم، تُوفر Aspose.PDF خاصية [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) في فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

يظهر المقتطف البرمجي التالي كيفية الحصول على محتوى مستند PDF بنص موسوم:

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

## الحصول على البنية الجذرية

من أجل الحصول على البنية الجذرية لمستند PDF الموسوم، تُوفر Aspose.PDF خاصية [struct_tree_root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties) لواجهة [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) وخاصية [root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties).

يظهر المقتطف البرمجي التالي كيفية الحصول على البنية الجذرية لمستند PDF الموسوم:

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

## الوصول إلى العناصر الفرعية

من أجل الوصول إلى العناصر الفرعية لمستند PDF الموسوم، تُوفر Aspose.PDF فئة [ElementList](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/elementlist/). يوضح المقتطف البرمجي التالي كيفية الوصول إلى العناصر الفرعية لمستند PDF الموسوم:

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
