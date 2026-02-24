---
title: Извлечение помеченного содержимого из PDF
linktitle: Извлечь помеченное содержимое
type: docs
weight: 20
url: /ru/python-net/extract-tagged-content-from-tagged-pdfs/
description: В этой статье объясняется, как извлечь помеченное содержимое PDF‑документа, используя Aspose.PDF для Python через .NET
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

В этой статье вы узнаете, как извлечь помеченное содержимое PDF‑документа, используя Python.

## Получение помеченного PDF‑содержимого

Чтобы получить содержимое PDF‑документа с помеченным текстом, Aspose.PDF предоставляет свойство [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Следующий фрагмент кода показывает, как получить содержимое PDF‑документа с помеченным текстом:

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

## Получение корневой структуры

Чтобы получить корневую структуру помеченного PDF‑документа, Aspose.PDF предоставляет свойство [struct_tree_root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties) интерфейса [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) и [root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties).

Следующий фрагмент кода показывает, как получить корневую структуру помеченного PDF‑документа:

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

## Доступ к дочерним элементам

Чтобы получить доступ к дочерним элементам помеченного PDF‑документа, Aspose.PDF предоставляет класс [ElementList](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/elementlist/). Следующий фрагмент кода показывает, как получить доступ к дочерним элементам помеченного PDF‑документа:

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
