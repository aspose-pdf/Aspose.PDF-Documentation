---
title: حذف صفحات PDF برمجيًا باستخدام Python
linktitle: حذف صفحات PDF
type: docs
weight: 80
url: /ar/python-net/delete-pages/
description: يمكنك حذف صفحات من ملف PDF باستخدام Aspose.PDF للبايثون عبر .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية حذف صفحات PDF باستخدام بايثون
Abstract: توفر هذه المقالة دليلًا مختصرًا حول كيفية حذف صفحات من ملف PDF باستخدام مكتبة Aspose.PDF للبايثون عبر .NET. تركز على استخدام فئة `PageCollection` لإزالة صفحات محددة. تتضمن العملية استدعاء طريقة `delete()` مع فهرس الصفحة المراد حذفها ثم حفظ المستند المحدث باستخدام طريقة `save()`. بالإضافة إلى ذلك، يتم توفير قطعة شيفرة لتوضيح حذف صفحة من ملف PDF، موضحًا استخدام مكتبة Aspose.PDF في سياق عملي.
---

يمكنك حذف صفحات من ملف PDF باستخدام Aspose.PDF للبايثون عبر .NET. لحذف صفحة معينة، استخدم [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) الخاص بـ [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

## حذف صفحة من ملف PDF

يقوم Aspose.PDF للبايثون عبر .NET بحذف الصفحة 2 من ملف PDF المدخل ويُحفظ المستند المحدث في ملف جديد. هذه الخاصية مفيدة لإزالة الصفحات غير المرغوب فيها أو الحساسة دون تعديل باقي المستند.

1. حمّل PDF المدخل كـ [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. احذف الصفحة باستخدام [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. استدعِ طريقة [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) لحفظ ملف PDF المحدث.

تُظهر قطعة الشيفرة التالية كيفية حذف صفحة معينة من ملف PDF باستخدام بايثون.

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

## حذف صفحات متعددة من مستند PDF

يسمح حذف صفحات متعددة بإزالة مجموعة من الصفحات المحددة في عملية واحدة، مما يكون أكثر كفاءة من حذف الصفحات واحدةً تلو الأخرى. يتم حفظ ملف PDF الناتج في ملف جديد، مع الحفاظ على المستند الأصلي.

1. حمّل PDF المدخل كـ [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. احذف الصفحات المدرجة في مصفوفة الصفحات باستخدام [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. احفظ الـ[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) المحدث في ملف جديد.

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

