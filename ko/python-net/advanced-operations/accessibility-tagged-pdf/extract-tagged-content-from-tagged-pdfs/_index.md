---
title: PDF에서 태그된 콘텐츠 추출
linktitle: 태그된 콘텐츠 추출
type: docs
weight: 20
url: /ko/python-net/extract-tagged-content-from-tagged-pdfs/
description: 이 기사에서는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에서 태그된 콘텐츠를 추출하는 방법을 설명합니다.
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

이 문서에서는 Python을 사용하여 PDF 문서에서 태그된 콘텐츠를 추출하는 방법을 배웁니다.

## 태그된 PDF 콘텐츠 가져오기

태그된 텍스트가 포함된 PDF 문서의 내용을 가져오기 위해 Aspose.PDF는 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 속성을 제공합니다.

다음 코드 스니펫은 태그된 텍스트가 포함된 PDF 문서의 내용을 얻는 방법을 보여줍니다.

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

## 루트 구조 가져오기

태그된 PDF 문서의 루트 구조를 가져오기 위해 Aspose.PDF는 [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) 인터페이스의 [struct_tree_root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties) 속성과 [root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties) 속성을 제공합니다.

다음 코드 스니펫은 태그된 PDF 문서의 루트 구조를 가져오는 방법을 보여줍니다.

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

## 자식 요소 접근

태그된 PDF 문서의 자식 요소에 접근하기 위해 Aspose.PDF는 [ElementList](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/elementlist/) 클래스를 제공합니다. 다음 코드 스니펫은 태그된 PDF 문서의 자식 요소에 접근하는 방법을 보여줍니다.

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
