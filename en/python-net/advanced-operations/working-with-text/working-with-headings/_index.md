---
title: Working with Headings in PDF
type: docs
weight: 40
url: /python-net/working-with-headings/
description: Create numbering in heading your PDF document with Python. Aspose.PDF for Python via .NET offers different kinds of numbering styles.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to work with Headings in PDF using Python
Abstract: The article discusses the importance of headings in documents and introduces the concept of numbering styles to organize multiple headings effectively. It highlights the Aspose.PDF for Python via .NET as a tool that provides several pre-defined numbering styles, stored in the NumberingStyle enumeration. This enumeration includes styles such as Arabic numerals, Roman numerals (both uppercase and lowercase), and English letters (both uppercase and lowercase). The article outlines how these styles enhance the clarity and structure of a document by making headings more prominent and meaningful. It provides a Python code example demonstrating the application of different numbering styles to document headings using the Aspose.PDF library. The code initializes a document, adds pages, and demonstrates creating headings with specific numbering styles, such as Roman lowercase and English lowercase, to illustrate the practical use of these styles.
---

## Apply Numbering Style in Heading

Headings are the important parts of any document. Writers always try to make headings more prominent and meaningful to its readers. If there are more than one headings in a document, a writer has several options to organize these headings. One of the most common approach to organize headings is to write headings in Numbering Style.

[Aspose.PDF for Python via .NET](/pdf/python-net/) offers many pre-defined numbering styles. These pre-defined numbering styles are stored in an enumeration, [NumberingStyle](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/). The pre-defined values of NumberingStyle enumeration and their descriptions are given below:

|**Heading Types**|**Description**|
| :- | :- |
|NumeralsArabic|Arab type,for example, 1,1.1,...|
|NumeralsRomanUppercase|Roman upper type, for example, I,I.II, ...|
|NumeralsRomanLowercase|Roman lower type, for example, i,i.ii, ...|
|LettersUppercase|English upper type, for example, A,A.B, ...|
|LettersLowercase|English lower type, for example, a,a.b, ...|

The [style](https://reference.aspose.com/pdf/python-net/aspose.pdf/heading/#properties) property of [Heading](https://reference.aspose.com/pdf/python-net/aspose.pdf/heading/) class is used to set the numbering styles of the headings.

|**Figure: Pre-defined numbering styles**|
| :- |

The source code, to obtain the output shown in the above figure, is given below in the example.

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.page_info.width = 612.0
    document.page_info.height = 792.0
    document.page_info.margin = ap.MarginInfo()
    document.page_info.margin.left = 72
    document.page_info.margin.right = 72
    document.page_info.margin.top = 72
    document.page_info.margin.bottom = 72

    page = document.pages.add()
    page.page_info.width = 612.0
    page.page_info.height = 792.0
    page.page_info.margin = ap.MarginInfo()
    page.page_info.margin.left = 72
    page.page_info.margin.right = 72
    page.page_info.margin.top = 72
    page.page_info.margin.bottom = 72

    float_box = ap.FloatingBox()
    float_box.margin = page.page_info.margin

    page.paragraphs.add(float_box)

    heading = ap.Heading(1)
    heading.is_in_list = True
    heading.start_number = 1
    heading.text = "List 1"
    heading.style = ap.NumberingStyle.NUMERALS_ROMAN_LOWERCASE
    heading.is_auto_sequence = True

    float_box.paragraphs.add(heading)

    heading2 = ap.Heading(1)
    heading2.is_in_list = True
    heading2.start_number = 13
    heading2.text = "List 2"
    heading2.style = ap.NumberingStyle.NUMERALS_ROMAN_LOWERCASE
    heading2.is_auto_sequence = True

    float_box.paragraphs.add(heading2)

    heading3 = ap.Heading(2)
    heading3.is_in_list = True
    heading3.start_number = 1
    heading3.text = "the value, as of the effective date of the plan, of property to be distributed under the plan onaccount of each allowed"
    heading3.style = ap.NumberingStyle.LETTERS_LOWERCASE
    heading3.is_auto_sequence = True

    float_box.paragraphs.add(heading3)
    document.save(output_pdf)
```

