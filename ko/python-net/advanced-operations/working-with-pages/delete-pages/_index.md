---
title: Python으로 PDF 페이지 프로그래밍 방식 삭제
linktitle: PDF 페이지 삭제
type: docs
weight: 80
url: /ko/python-net/delete-pages/
description: Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 페이지를 삭제하는 방법
Abstract: 이 문서는 Aspose.PDF 라이브러리를 사용하여 .NET을 통한 Python으로 PDF 파일에서 페이지를 삭제하는 방법에 대한 간결한 안내를 제공합니다. 특정 페이지를 제거하기 위해 `PageCollection` 클래스를 활용하는 데 중점을 둡니다. 이 과정은 삭제할 페이지의 인덱스를 지정하여 `delete()` 메서드를 호출하고, 이후 `save()` 메서드로 업데이트된 문서를 저장하는 것을 포함합니다. 또한, PDF 파일에서 페이지를 삭제하는 코드를 보여주는 코드 스니펫이 제공되어 Aspose.PDF 라이브러리의 실용적인 사용 예시를 설명합니다.
---

Aspose.PDF for Python via .NET을 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다. 특정 페이지를 삭제하려면 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)의 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)를 사용하십시오.

## PDF 파일에서 페이지 삭제

Aspose.PDF for Python via .NET은 입력 PDF에서 페이지 2를 삭제하고 업데이트된 문서를 새 파일에 저장합니다. 이 기능은 문서의 다른 부분을 변경하지 않고 원하지 않거나 민감한 페이지를 제거하는 데 유용합니다.

1. 입력 PDF를 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)로 로드합니다.
1. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)을 사용하여 페이지를 삭제합니다.
1. 업데이트된 PDF 파일을 저장하려면 [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출합니다.

다음 코드 스니펫은 Python을 사용하여 PDF 파일에서 특정 페이지를 삭제하는 방법을 보여줍니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_page(input_file_name, output_file_name):
    """
    Delete a single page from a PDF document.

    Demonstrates how to remove a specific page from a PDF document using
    the Aspose.PDF library. This function deletes page 2 from the input
    document and saves the result to a new file.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete a page.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> delete_page("input.pdf", "output.pdf")
        # Removes page 2 from input.pdf and saves result as output.pdf
    """
    # Open the PDF as a Document
    document = ap.Document(input_file_name)
    # Delete page using PageCollection API
    document.pages.delete(2)
    # Save updated Document
    document.save(output_file_name)
```

## PDF 문서에서 여러 페이지 삭제

여러 페이지를 삭제하면 지정된 페이지 집합을 한 번에 제거할 수 있어 페이지를 하나씩 삭제하는 것보다 효율적입니다. 결과 PDF는 새 파일에 저장되어 원본 문서를 보존합니다.

1. 입력 PDF를 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)로 로드합니다.
1. 페이지 배열에 나열된 페이지들을 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)을 사용하여 삭제합니다.
1. 업데이트된 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)을 새 파일에 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_bunch_pages(input_file_name, output_file_name):
    """
    Delete multiple pages from a PDF document in a single operation.

    Demonstrates bulk page deletion by removing multiple specified pages
    from a PDF document. This is more efficient than deleting pages
    one by one when removing multiple pages.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete pages.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes pages 2, 3, 4, 6, 7, and 9 in this example
        - Page numbers are 1-based (page 2 is the second page)
        - Pages are deleted in the order specified in the list
        - The original document is not modified; a new file is created
        - Ensure the document has enough pages to avoid errors
        - Page numbers should be adjusted if the source document has fewer pages

    Example:
        >>> delete_bunch_pages("input.pdf", "output.pdf")
        # Removes pages 2, 3, 4, 6, 7, and 9 from input.pdf
    """
    # Open the PDF as a Document
    document = ap.Document(input_file_name)
    # Example: Deleting pages 2, 3, 4, 6, 7, and 9; modify this list as needed for your use case.
    pages = [2,3,4,6,7,9]
    # Delete pages via PageCollection API
    document.pages.delete(pages)
    # Save updated Document
    document.save(output_file_name)
```

