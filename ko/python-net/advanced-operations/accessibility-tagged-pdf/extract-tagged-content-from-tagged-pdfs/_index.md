---
title: Python에서 PDF의 태그된 콘텐츠 추출
linktitle: 태그된 콘텐츠 추출
type: docs
weight: 20
url: /ko/python-net/extract-tagged-content-from-tagged-pdfs/
description: Aspose.PDF for Python via .NET를 사용하여 Python에서 태그된 PDF 콘텐츠를 추출하는 방법을 배우고, 태그된 콘텐츠, 루트 구조 및 하위 구조 요소에 대한 접근 방법을 포함합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

이 문서에서는 Python을 사용하여 PDF 문서에서 태그된 콘텐츠를 추출하는 방법을 배웁니다.

tagged PDF를 검사하거나 논리 구조 트리를 읽거나, 접근성 워크플로를 위해 구조 요소가 올바르게 생성되었는지 검증해야 할 때 이러한 예제를 사용하십시오.

## Tagged PDF 콘텐츠 가져오기

Tagged Text가 포함된 PDF 문서의 콘텐츠를 가져오기 위해, Aspose.PDF는 제공합니다 [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 속성 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스.

고급이며 완전하게 태그된 PDF 문서를 구조화되고 계층적인 목차 (TOC)와 함께 생성하십시오:

1. 새 Document 객체를 생성합니다.
1. tagged_content 속성에 접근합니다.
1. 'set_title()'을 사용하여 문서 제목을 설정합니다.
1. 'set_language()'을 사용하여 문서 언어를 설정합니다.
1. 문서를 저장합니다.

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

## 루트 구조 가져오기

Tagged PDF에는 문서의 의미 구조를 정의하는 논리적 구조 트리가 포함됩니다. StructTreeRoot는 이 논리적 트리의 루트를 나타내며, RootElement는 문서의 최상위 구조 요소와 상호 작용할 수 있는 인터페이스를 제공합니다.

다음 코드 스니펫은 Tagged PDF 문서의 루트 구조를 가져오는 방법을 보여줍니다:

1. 새 태그가 지정된 PDF 문서를 만듭니다.
1. 태그가 지정된 컨텐츠에 접근하고 메타데이터를 설정합니다.
1. StructTreeRoot와 RootElement에 접근합니다.
1. 태그가 지정된 PDF를 저장합니다.

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

## 자식 요소에 접근하기

Tagged PDF는 문서의 의미 계층 구조(제목, 단락, 양식, 목록 등)를 정의하는 논리 구조 트리를 포함합니다. 이러한 구조 요소에 접근하고 수정하면 다음을 수행할 수 있습니다:

- title, language, actual_text 및 접근성 관련 속성과 같은 메타데이터를 검사합니다
- 접근성 또는 현지화를 향상시키기 위해 속성을 업데이트합니다
- PDF/UA 준수를 위해 논리 문서 구조를 프로그래밍 방식으로 조정합니다

 다음 코드 스니펫은 Tagged PDF 문서의 하위 요소에 액세스하는 방법을 보여줍니다:

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

## 관련 Tagged PDF 주제

- [Tagged PDF 생성](/pdf/ko/python-net/create-tagged-pdf/) 구조를 검사하기 전에 접근성이 보장된 태그 문서를 만들기 위해.
- [구조 요소 속성 설정](/pdf/ko/python-net/setting-structure-elements-properties/) 구조 요소를 추출한 후 의미 속성을 업데이트합니다.
- [태그된 PDF에서 테이블 작업](/pdf/ko/python-net/working-with-table-in-tagged-pdfs/) 태그된 테이블 접근성 워크플로를 위해.