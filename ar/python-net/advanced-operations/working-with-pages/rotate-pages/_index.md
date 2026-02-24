---
title: تدوير صفحات PDF باستخدام بايثون
linktitle: تدوير صفحات PDF
type: docs
weight: 110
url: /ar/python-net/rotate-pages/
description: يصف هذا الموضوع كيفية تدوير اتجاه الصفحات في ملف PDF موجود برمجيًا باستخدام بايثون.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تدوير الصفحات في PDF باستخدام بايثون
Abstract: توفر هذه المقالة دليلًا حول كيفية تحديث أو تغيير اتجاه صفحات ملف PDF موجود برمجيًا باستخدام بايثون. باستخدام Aspose.PDF لبايثون عبر .NET، يمكن للمستخدمين بسهولة التبديل بين الاتجاهات الأفقية والعمودية عن طريق تعديل خصائص MediaBox الخاصة بالصفحة. تتضمن المقالة مقتطف كود بايثون يُظهر كيفية التكرار عبر صفحات وثيقة PDF، وتعديل أبعاد ومواقع MediaBox الخاصة بها، وضبط CropBox إذا لزم الأمر. بالإضافة إلى ذلك، توضح كيفية ضبط زاوية تدوير الصفحات باستخدام طريقة 'rotate' لتحقيق الاتجاه المطلوب. تُختتم العملية بحفظ ملف PDF المحدث.
---

يصف هذا الموضوع كيفية تحديث أو تغيير اتجاه صفحات ملف PDF موجود برمجيًا باستخدام بايثون.

## تغيير اتجاه الصفحة

تُدوِّر هذه الدالة كل صفحة من PDF [`مستند`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 90 درجة باتجاه عقارب الساعة باستخدام Aspose.PDF لبايثون.
تُعَدُّ مفيدة لتصحيح مشكلات اتجاه الصفحات، مثل المستندات الممسوحة ضوئيًا التي تكون مائلة. يظل ملف PDF الأصلي بدون تغيّر، ويتم حفظ النسخة المُدوَّرة كملف جديد.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_page(infile, outfile):
    """
    Rotate all pages in a PDF document by 90 degrees clockwise.

    Demonstrates how to rotate PDF pages using the Aspose.PDF library.
    This function applies a 90-degree clockwise rotation to every page
    in the input document and saves the result to a new file.

    Args:
        infile (str): Path to the input PDF file to rotate.
        outfile (str): Path where the rotated PDF will be saved.

    Returns:
        None: The function modifies the PDF pages and saves to the output path.

    Note:
        - Applies 90-degree clockwise rotation (ap.Rotation.ON90) to all pages
        - Rotates every page in the document uniformly
        - The original document is not modified; a new file is created
        - Rotation options include: ON90 (90°), ON180 (180°), ON270 (270°)
        - Useful for correcting page orientation or adjusting layout

    Example:
        >>> rotate_page("input.pdf", "rotated_output.pdf")
        # Rotates all pages 90 degrees clockwise and saves to rotated_output.pdf
    """
    document = ap.Document(infile)
    for page in document.pages:
        # `page` is a `Page` object; `rotate` uses the `Rotation` enum
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```


