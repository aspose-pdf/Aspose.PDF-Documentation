---
title: قص صفحات PDF باستخدام Python
linktitle: قص صفحات PDF
type: docs
weight: 70
url: /ar/python-net/crop-pages/
description: يمكنك تغيير خصائص الصفحة، مثل العرض، الارتفاع، صندوق النزف (Bleed)، صندوق القص (Crop) وصندوق التشذيب (Trimbox) باستخدام Aspose.PDF للـ Python عبر .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية الوصول إلى خصائص الصفحة وتعديلها في PDF باستخدام Python
Abstract: المقالة تقدم نظرة عامة حول كيفية الوصول إلى خصائص الصفحة وتعديلها في مستند PDF باستخدام Aspose.PDF للـ Python. يصف المقال عدة خصائص للصفحة، بما في ذلك صندوق الوسائط (media box)، صندوق النزف (bleed box)، صندوق التشذيب (trim box)، صندوق الفن (art box)، وصندوق القص (crop box)، موضحًا دورEach في تحديد أبعاد وحدود صفحة PDF لأغراض الطباعة والعرض. يمثل صندوق الوسائط أكبر حجم للصفحة، في حين يضمن صندوق النزف تغطية الحبر خارج حافة الصفحة للتشذيب. يحدد صندوق التشذيب الحجم النهائي للمستند بعد التشذيب، ويحتوي صندوق الفن على محتوى الصفحة الفعلي. يعرّف صندوق القص المنطقة المرئية في Adobe Acrobat. يتضمن المقال قطعة شفرة Python توضح كيفية تعيين صندوق قص جديد، إلى جانب الصناديق الأخرى، لصفحة محددة في مستند PDF. توضح الأمثلة المرئية مظهر الصفحة قبل وبعد تطبيق القص، مبرزًا التطبيق العملي لتعديل هذه الخصائص.
---

## الحصول على خصائص الصفحة

كل صفحة في ملف PDF تحتوي على عدد من الخصائص، مثل العرض، الارتفاع، صندوق النزف، صندوق القص وصندوق التشذيب. يتيح لك Aspose.PDF للـ Python الوصول إلى هذه الخصائص.

- **media_box**: صندوق الوسائط هو أكبر صندوق للصفحة. وهو يتطابق مع حجم الصفحة (على سبيل المثال A4، A5، US Letter، إلخ) الذي تم اختياره عندما تم طباعة المستند إلى PostScript أو PDF. بمعنى آخر، يحدد صندوق الوسائط الحجم الفعلي للوسيط الذي يعرض أو يطبع عليه مستند PDF.
- **bleed_box**: إذا كان للمستند نزف، سيحتوي PDF أيضًا على صندوق نزف. النزف هو مقدار اللون (أو العمل الفني) الذي يمتد خارج حافة الصفحة. يُستخدم لضمان أنه عندما يتم طباعة المستند وقصه إلى الحجم المناسب ("مُشذّب"), سيصل الحبر إلى حافة الصفحة بالكامل. حتى إذا تم قص الصفحة بشكل غير دقيق - قص قليلًا خارج علامات التشذيب - لن تظهر حواف بيضاء على الصفحة.
- **trim_box**: صندوق التشذيب يحدد الحجم النهائي للمستند بعد الطباعة والتشذيب.
- **art_box**: صندوق الفن هو الصندوق المرسوم حول المحتوى الفعلي للصفحات في مستنداتك. يُستخدم هذا الصندوق عند استيراد مستندات PDF في تطبيقات أخرى.
- **crop_box**: صندوق القص هو حجم "الصفحة" الذي يتم عرض مستند PDF الخاص بك عليه في Adobe Acrobat. في العرض العادي، يتم عرض محتويات صندوق القص فقط في Adobe Acrobat. للحصول على أوصاف مفصلة لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، وبشكل خاص 10.10.1 حدود الصفحة.

قم بقص أول [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) في PDF إلى منطقة مستطيلة محددة باستخدام Aspose.PDF للـ Python. تقوم الدالة بضبط عدة صناديق للصفحة—`crop_box`، `trim_box`، `art_box`، و`bleed_box`—لضمان نتائج بصرية متسقة. قد يكون القَص مفيدًا لإزالة الهوامش غير المرغوبة أو للتركيز على منطقة معينة من الصفحة.

1. حمل PDF كـ [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (استخدم `ap.Document()`).
1. حدد مستطيل القَص باستخدام [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) مع الإحداثيات المطلوبة (بالنقاط).
1. اضبط `crop_box`، `trim_box`، `art_box`، و`bleed_box` للـ [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى المستطيل المحدد.
1. احفظ الـ [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) المعدل إلى ملف إخرج جديد.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to a specified rectangular area.
    This function loads a PDF document, defines a new rectangular boundary,
    and applies this boundary to multiple box types (crop, trim, art, and bleed)
    of the first page. The modified document is then saved to a new file.
    Args:
        input_file_name (str): Path to the input PDF file to be cropped.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Note:
        The cropping rectangle is set to coordinates (200, 220, 2170, 1520)
        which defines the visible area of the page. All box types are set
        to the same dimensions to ensure consistent cropping behavior.
    """
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

في هذا المثال استخدمنا ملف عينة [هنا](crop_page.pdf). في البداية تبدو صفحتنا كما هو موضح في الشكل 1.
![الشكل 1. الصفحة المقصوصة](crop_page.png)

بعد التغيير، ستظهر الصفحة كما في الشكل 2.
![الشكل 2. الصفحة المقصوصة](crop_page2.png)

## قص صفحة PDF بناءً على محتوى الصورة الأولى

قم بقص أول [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ديناميكياً بناءً على حدود أول صورة موجودة على الصفحة. باستخدام [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/)، يحدد النص البرمجي أول صورة ويضبط `crop_box` للصفحة لتطابق أبعاد الصورة. هذه الطريقة مفيدة عندما تريد التركيز على محتوى بصري محدد بدلاً من الإحداثيات المحددة مسبقاً.

1. حمل PDF كـ [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. حدد الصور على الصفحة الأولى باستخدام [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. تحقق مما إذا كانت الصور موجودة:
- إذا وجدت، اضبط `crop_box` للـ [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) لتطابق [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) الخاص بالصورة الأولى.
- إذا لم توجد، احتفظ بالصفحة دون تغيير وأعلم المستخدم.
1. احفظ الـ [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) المعدل إلى ملف الإخراج المحدد.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page_by_content(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to the bounds of the first image found on that page.
    This function opens a PDF document, locates the first image on the first page,
    and sets the page's crop box to match the image's rectangle dimensions. If no
    images are found, the page remains unchanged.
    Args:
        input_file_name (str): Path to the input PDF file to be processed.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Raises:
        Exception: May raise exceptions related to file I/O operations or PDF processing
                  if the input file is invalid, corrupted, or inaccessible.
    Note:
        - Only processes the first page of the document
        - Uses the first image found on the page for cropping dimensions
        - If no images are found, prints a message and saves the document unchanged
        - Requires the aspose.pdf library (imported as 'ap')
    """
    document = ap.Document(input_file_name)
    # Find first image on first page using ImagePlacementAbsorber
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        first_image = absorber.image_placements[1]
        document.pages[1].crop_box = first_image.rectangle
    else:
        print("No images found on the first page")
    document.save(output_file_name)
```
