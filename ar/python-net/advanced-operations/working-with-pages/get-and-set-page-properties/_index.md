---
title: الحصول على خصائص الصفحات وتعيينها باستخدام بايثون
linktitle: الحصول على خصائص الصفحات وتعيينها
type: docs
weight: 90
url: /ar/python-net/get-and-set-page-properties/
description: يعرض هذا القسم طريقة الحصول على عدد الصفحات في ملف PDF، والحصول على معلومات حول خصائص صفحة PDF مثل اللون وتعيين خصائص الصفحة.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية الحصول على خصائص الصفحة وتعيينها باستخدام بايثون
Abstract: تناقش هذه المقالة قدرات Aspose.PDF for Python عبر .NET، مع التركيز على قراءة وتعيين خصائص الصفحات في ملفات PDF باستخدام بايثون. تغطي المقالة وظائف متعددة بما في ذلك تحديد عدد الصفحات في ملف PDF، والوصول إلى خصائص الصفحة وتعديلها، ومعالجة معلومات اللون. للحصول على عدد الصفحات، يتم استخدام الفئة `Document` ومجموعة `PageCollection`، مع مقتطفات شفرة توضح كيفية استرجاع عدد الصفحات، حتى دون حفظ المستند. تشرح المقالة خصائص الصفحات المختلفة مثل MediaBox و BleedBox و TrimBox و ArtBox و CropBox، وتوفر أمثلة شفرة للوصول إلى هذه الخصائص. بالإضافة إلى ذلك، تغطي استرجاع صفحة معينة من PDF وحفظها كمستند منفصل، بالإضافة إلى تحديد نوع اللون لكل صفحة. جميع الأمثلة مطبقة في بايثون، توضح التطبيقات العملية لهذه الميزات.
---

تتيح لك Aspose.PDF for Python عبر .NET قراءة وتعيين خصائص الصفحات في ملف PDF داخل تطبيقات بايثون الخاصة بك. يعرض هذا القسم طريقة الحصول على عدد الصفحات في ملف PDF، والحصول على معلومات حول خصائص صفحة PDF مثل اللون وتعيين خصائص الصفحة. تستخدم الأمثلة واجهات برمجة التطبيقات [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) و[`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) ومكتوبة بلغة بايثون.

## الحصول على عدد الصفحات في ملف PDF

عند العمل مع المستندات، غالبًا ما تريد معرفة عدد الصفحات التي تحتويها. باستخدام Aspose.PDF لا يتطلب ذلك أكثر من سطرين من الشفرة.

للحصول على عدد الصفحات في ملف PDF:

1. افتح ملف PDF باستخدام الفئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. ثم استخدم خاصية Count لمجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (من كائن Document) للحصول على إجمالي عدد الصفحات في المستند.

تظهر مقتطف الشفرة التالي كيفية الحصول على عدد صفحات ملف PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count(input_file_name):
    """
    Get the total number of pages in a PDF document.
    Args:
        input_file_name (str): Path to the input PDF file.
    Returns:
        None: Prints the page count to console.
    Example:
        get_page_count("example.pdf")
        # Output: Page Count: 10
    """
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### الحصول على عدد الصفحات دون حفظ المستند

في بعض الأحيان نولد ملفات PDF في الوقت الحقيقي وخلال إنشاء ملف PDF قد نواجه الحاجة (إنشاء جدول محتويات وما إلى ذلك) للحصول على عدد صفحات ملف PDF دون حفظ الملف على النظام أو التدفق. لذا لتلبية هذه المتطلبات، تم إدخال طريقة [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) في فئة Document. يرجى إلقاء نظرة على مقتطف الشفرة التالي الذي يوضح الخطوات للحصول على عدد الصفحات دون حفظ المستند.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count_without_saving(input_file_name):
    """
    Get the page count of a PDF document after adding content without saving the file.

    This function opens an existing PDF document, adds a new page with 300 text fragments,
    processes the paragraphs to ensure accurate page counting, and prints the total number
    of pages in the document. The document is not saved to disk.

    Args:
        input_file_name (str): Path to the input PDF file to be processed.

    Returns:
        None: This function prints the page count but does not return a value.

    Example:
        >>> get_page_count_without_saving("sample.pdf")
        Number of pages in document = 2
    """
    # Instantiate Document instance
    document = ap.Document(input_file_name)
    # Add page to pages collection of PDF file
    page = document.pages.add()
    # Create loop instance
    for _ in range(0, 300):
        # Add TextFragment to paragraphs collection of page object
        page.paragraphs.add(ap.text.TextFragment("Pages count test"))
    # Process the paragraphs in PDF file to get accurate page count
    document.process_paragraphs()
    # Print number of pages in document
    print("Number of pages in document =", str(len(document.pages)))
```

## الحصول على خصائص الصفحة

كل صفحة في ملف PDF لها عدد من الخصائص، مثل العرض والارتفاع، وصناديق bleed و crop و trim. يتيح لك Aspose.PDF الوصول إلى هذه الخصائص.

### فهم خصائص الصفحة: الفرق بين Artbox و BleedBox و CropBox و MediaBox و TrimBox وخاصية Rect

- **Media box**: صندوق الوسائط هو أكبر صندوق صفحة. وهو يتطابق مع حجم الصفحة (مثلاً A4، A5، US Letter، إلخ) الذي تم اختياره عندما تم طباعة المستند إلى PostScript أو PDF. بعبارة أخرى، يحدد صندوق الوسائط الحجم الفيزيائي للوسيط الذي يُعرض أو يُطبع عليه مستند PDF.
- **Bleed box**: إذا كان للمستند bleed، فإن PDF سيحتوي أيضًا على صندوق bleed. الـ bleed هو مقدار اللون (أو الأعمال الفنية) الذي يمتد خارج حافة الصفحة. يُستخدم لضمان أن الحبر سيصل إلى حافة الصفحة عند الطباعة والقص (“trimmed”). حتى إذا تم قص الصفحة بشكل غير دقيق - أي قطعها قليلاً عن علامات القص - لن تظهر حواف بيضاء على الصفحة.
- **Trim box**: يشير صندوق الـ trim إلى الحجم النهائي للمستند بعد الطباعة والقص.
- **Art box**: صندوق الـ art هو الصندوق المرسوم حول المحتوى الفعلي للصفحات في مستنداتك. يُستخدم هذا الصندوق عند استيراد ملفات PDF في تطبيقات أخرى.
- **Crop box**: صندوق الـ crop هو حجم “الصفحة” الذي يُعرض مستند PDF به في Adobe Acrobat. في العرض العادي، تُعرض فقط محتويات صندوق الـ crop في Adobe Acrobat.
للحصول على أوصاف مفصلة لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، وبشكل خاص 10.10.1 Page Boundaries.
-- **Page.Rect**: التقاطع (المستطيل المرئي عادة) بين MediaBox و DropBox (`Page.rect`). راجع نوع [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) للحصول على خصائص المستطيل. توضح الصورة أدناه هذه الخصائص.

لمزيد من التفاصيل، يرجى زيارة [this page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### الوصول إلى خصائص الصفحة

توفر الفئة [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) جميع الخصائص المتعلقة بصفحة PDF معينة. جميع صفحات ملفات PDF مُضمّنة في مجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

من هناك، يمكن الوصول إما إلى كائنات `Page` الفردية باستخدام فهرستها، أو التكرار عبر المجموعة للحصول على جميع الصفحات. بمجرد الوصول إلى صفحة معينة، يمكننا الحصول على خصائصها. توضح مقتطف الشفرة التالي كيفية الحصول على خصائص الصفحة (واجهة `Page`).

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_properties(input_file_name):
    """
    Retrieves and displays various page properties for the first page of a PDF document.

    Args:
        input_file_name (str): Path to the PDF file to analyze.
    """
    # Open document
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Get page properties
    boxes = {
        "ArtBox": page.art_box,
        "BleedBox": page.bleed_box,
        "CropBox": page.crop_box,
        "MediaBox": page.media_box,
        "TrimBox": page.trim_box,
        "Rect": page.rect
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}")

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## تحديد لون الصفحة

توفر الفئة [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) الخصائص المتعلقة بصفحة معينة في مستند PDF، بما في ذلك نوع اللون الذي تستخدمه الصفحة - RGB، أبيض وأسود، تدرجات الرمادي أو غير معرف.

جميع صفحات ملفات PDF مضمنة في مجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/). تحدد خاصية [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) لون العناصر على الصفحة. للحصول على أو تحديد معلومات اللون لصفحة PDF معينة، استخدم خاصية [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) لكائن [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

توضح مقتطف الشفرة التالي كيفية التكرار عبر صفحات PDF الفردية للحصول على معلومات اللون.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_color_type(input_file_name):
    """
    Analyzes and prints the color type information for each page in a PDF document.

    This function opens a PDF file and iterates through all pages to determine
    the color type of each page (black and white, grayscale, RGB, or undefined).
    The results are printed to the console with human-readable descriptions.

    Args:
        input_file_name (str): Path to the PDF file to analyze.

    Returns:
        None: This function prints results directly to console and doesn't return a value.

    Example:
        >>> get_page_color_type("sample.pdf")
        Page # 1 is RGB.
        Page # 2 is Gray Scale.
        Page # 3 is Black and white.

    Note:
        Requires the aspose.pdf library (imported as ap) to be installed and available.
        The PDF file must be accessible at the specified path.
    """
    # Open source PDF file
    document = ap.Document(input_file_name)
    # Iterate through all the page of PDF file
    for page_number in range(1, len(document.pages) + 1):
        # Get the color type information for particular PDF page
        page_color_type = document.pages[page_number].color_type
        color_type_map = {
            ap.ColorType.BLACK_AND_WHITE: "Black and white",
            ap.ColorType.GRAYSCALE: "Gray Scale",
            ap.ColorType.RGB: "RGB",
            ap.ColorType.UNDEFINED: "undefined"
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```


