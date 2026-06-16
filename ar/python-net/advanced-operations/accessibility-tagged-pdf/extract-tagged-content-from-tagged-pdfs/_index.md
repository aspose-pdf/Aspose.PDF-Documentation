---
title: استخراج المحتوى الموسوم من ملفات PDF في Python
linktitle: استخراج المحتوى الموسوم
type: docs
weight: 20
url: /ar/python-net/extract-tagged-content-from-tagged-pdfs/
description: تعرف على كيفية استخراج محتوى PDF ذي العلامات في Python باستخدام Aspose.PDF لـ Python عبر .NET، بما في ذلك الوصول إلى المحتوى الذي تم وضع علامة عليه وبنية الجذر وعناصر البنية الفرعية.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

في هذه المقالة، ستتعلم كيفية استخراج المحتوى ذي العلامات من مستندات PDF باستخدام Python.

استخدم هذه الأمثلة عندما تحتاج إلى فحص PDF ذي علامات تمييز، أو قراءة شجرة البنية المنطقية، أو التحقق من أن عناصر البنية تم إنشاؤها بشكل صحيح لعمليات سير عمل إمكانية الوصول.

## الحصول على محتوى PDF ذي علامات

من أجل الحصول على محتوى مستند PDF بنص مميز، يقدم Aspose.PDF [المحتوى الموسوم](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) ملكية لـ [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.

قم بإنشاء مستند PDF متقدم ومزود بعلامات كاملة مع جدول محتويات منظم وهرمي (TOC):

1. قم بإنشاء كائن مستند جديد.
1. قم بالوصول إلى الخاصية tagged_content.
1. قم بتعيين عنوان المستند باستخدام 'set_title () '.
1. قم بتعيين لغة المستند باستخدام 'set_language () '.
1. احفظ المستند.

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

## الحصول على بنية الجذر

تحتوي ملفات PDF ذات العلامات على شجرة بنية منطقية تحدد البنية الدلالية للمستند. يمثل StructTreeRoot جذر هذه الشجرة المنطقية، بينما يوفر rootElement واجهة للتفاعل مع عنصر بنية المستوى الأعلى للمستند.

يوضح مقتطف الشفرة التالي كيفية الحصول على البنية الجذرية لمستند PDF الموسوم:

1. قم بإنشاء مستند PDF جديد تم وضع علامة عليه.
1. الوصول إلى المحتوى الذي تم وضع علامة عليه وتعيين البيانات الوصفية.
1. جذر شجرة هيكل الوصول وعنصر الجذر.
1. احفظ ملف PDF الذي تم وضع علامة عليه.

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

## الوصول إلى عناصر الطفل

تحتوي ملفات PDF ذات العلامات على شجرة بنية منطقية تحدد التسلسل الهرمي الدلالي للمستند (العناوين والفقرات والنماذج والقوائم وما إلى ذلك). يتيح لك الوصول إلى عناصر البنية هذه وتعديلها:

- افحص البيانات الوصفية مثل العنوان واللغة والنص الفعلي والخصائص المتعلقة بإمكانية الوصول
- تحديث الخصائص لتحسين إمكانية الوصول أو الترجمة
- اضبط بنية المستند المنطقي برمجيًا لتوافق PDF/UA

 يوضح مقتطف الشفرة التالي كيفية الوصول إلى العناصر الفرعية لمستند PDF ذي العلامات:

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

## موضوعات PDF ذات صلة

- [إنشاء ملف PDF ذي علامات](/pdf/ar/python-net/create-tagged-pdf/) لإنشاء مستندات ذات علامات يمكن الوصول إليها قبل فحص هيكلها.
- [إعداد خصائص عناصر الهيكل](/pdf/ar/python-net/setting-structure-elements-properties/) لتحديث الخصائص الدلالية بعد استخراج عناصر البنية.
- [العمل مع الجدول في ملفات PDF ذات العلامات](/pdf/ar/python-net/working-with-table-in-tagged-pdfs/) لعمليات سير عمل إمكانية الوصول إلى الجداول ذات العلامات.