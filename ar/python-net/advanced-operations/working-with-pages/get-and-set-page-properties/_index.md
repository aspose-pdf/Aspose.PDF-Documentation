---
title: الحصول على خصائص صفحة PDF وتعيينها في Python
linktitle: الحصول على خصائص الصفحة وإعدادها
type: docs
weight: 90
url: /ar/python-net/get-and-set-page-properties/
description: تعرف على كيفية فحص وتحديث خصائص صفحة PDF مثل معلومات الحجم والعد واللون في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية الحصول على خصائص الصفحة وتعيينها باستخدام Python
Abstract: تتناول هذه المقالة إمكانيات Aspose.PDF لـ Python عبر .NET، مع التركيز على قراءة خصائص الصفحة وإعدادها في ملفات PDF باستخدام Python. تتناول المقالة العديد من الوظائف بما في ذلك تحديد عدد الصفحات في PDF، والوصول إلى خصائص الصفحة وتعديلها، ومعالجة معلومات الألوان. للحصول على عدد الصفحات، يتم استخدام فئة «المستند» ومجموعة «PageCollection»، مع مقتطفات التعليمات البرمجية التي توضح كيفية استرداد عدد الصفحات، حتى بدون حفظ المستند. تشرح المقالة خصائص الصفحة المختلفة مثل MediaBox و BleedBox و TrimBox و ArtBox و CropBox، وتوفر أمثلة التعليمات البرمجية للوصول إلى هذه الخصائص. بالإضافة إلى ذلك، فإنه يغطي استرداد صفحة معينة من PDF وحفظها كمستند منفصل، بالإضافة إلى تحديد نوع لون كل صفحة. يتم تنفيذ الأمثلة في كل مكان في Python، مما يوضح التطبيقات العملية لهذه الميزات.
---

يتيح لك Aspose.PDF لـ Python عبر .NET قراءة خصائص الصفحات وتعيينها في ملف PDF في تطبيقات Python الخاصة بك. يوضح هذا القسم كيفية الحصول على عدد الصفحات في ملف PDF، والحصول على معلومات حول خصائص صفحة PDF مثل اللون وتعيين خصائص الصفحة. تستخدم الأمثلة [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) و [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) واجهات برمجة التطبيقات ومكتوبة بلغة Python.

استخدم هذا الدليل عندما تحتاج إلى فحص بيانات تعريف الصفحة أو تحديد عدد الصفحات أو تحديث خصائص مستوى الصفحة كجزء من تحليل المستند أو مهام التطبيع.

## احصل على عدد الصفحات في ملف PDF

عند التعامل مع المستندات، غالبًا ما تريد معرفة عدد الصفحات التي تحتوي عليها. مع Aspose.PDF لا يتطلب هذا أكثر من سطرين من التعليمات البرمجية.

للحصول على عدد الصفحات في ملف PDF:

1. افتح ملف PDF باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.
1. ثم استخدم [مجموعة الصفحات](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) خاصية العد للمجموعة (من كائن المستند) للحصول على إجمالي عدد الصفحات في المستند.

يوضح مقتطف الشفرة التالي كيفية الحصول على عدد صفحات ملف PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count(input_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### احصل على عدد الصفحات دون حفظ المستند

في بعض الأحيان نقوم بإنشاء ملفات PDF بسرعة وأثناء إنشاء ملف PDF، قد نواجه المتطلبات (إنشاء جدول المحتويات وما إلى ذلك) للحصول على عدد صفحات ملف PDF دون حفظ الملف عبر النظام أو البث. لذلك من أجل تلبية هذا المطلب، هناك طريقة [فقرات العملية ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) تم تقديمه في فئة المستندات. يرجى إلقاء نظرة على مقتطف الشفرة التالي الذي يعرض خطوات الحصول على عدد الصفحات دون حفظ المستند.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count_without_saving(input_file_name):
    # Instantiate Document instance
    document = ap.Document()
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

## احصل على خصائص الصفحة

تحتوي كل صفحة في ملف PDF على عدد من الخصائص، مثل العرض والارتفاع ومربع التسييل والقص والتقطيع. Aspose.PDF يسمح لك بالوصول إلى هذه الخصائص.

### فهم خصائص الصفحة: الفرق بين Artbox و BleedBox و CropBox و MediaBox و TrimBox وخاصية Rect

- **صندوق الوسائط**: صندوق الوسائط هو أكبر مربع صفحة. وهو يتوافق مع حجم الصفحة (على سبيل المثال A4 و A5 و US Letter وما إلى ذلك) المحدد عند طباعة المستند إلى PostScript أو PDF. بمعنى آخر، يحدد مربع الوسائط الحجم المادي للوسائط التي يتم عرض مستند PDF عليها أو طباعتها.
- **مربع التسييل**: إذا كان المستند مضخمًا، فسيحتوي ملف PDF أيضًا على مربع التسييل. التسييل هو مقدار اللون (أو العمل الفني) الذي يمتد إلى ما وراء حافة الصفحة. يتم استخدامه للتأكد من أنه عند طباعة المستند وتقطيعه إلى حجمه («اقتطاعه»)، سينتقل الحبر إلى حافة الصفحة. حتى في حالة عدم دقة الصفحة - قم بقطع علامات القطع قليلاً - لن تظهر أي حواف بيضاء على الصفحة.
- **صندوق التقليم**: يشير مربع القطع إلى الحجم النهائي للمستند بعد الطباعة والتشذيب.
- **صندوق الفن**: المربع الفني هو المربع المرسوم حول المحتويات الفعلية للصفحات في مستنداتك. يتم استخدام مربع الصفحة هذا عند استيراد مستندات PDF في تطبيقات أخرى.
- **صندوق الاقتصاص**: مربع الاقتصاص هو حجم «الصفحة» الذي يتم عرض مستند PDF به في Adobe Acrobat. في العرض العادي، يتم عرض محتويات مربع الاقتصاص فقط في Adobe Acrobat.
  للحصول على أوصاف تفصيلية لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، وخاصة حدود الصفحات 10.10.1.
- **Page.Rect**: التقاطع (المستطيل المرئي بشكل شائع) بين MediaBox و DropBox (`Page.rect`). انظر إلى [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) اكتب خصائص المستطيل. توضح الصورة أدناه هذه الخصائص.

لمزيد من التفاصيل، يرجى زيارة [هذه الصفحة](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### الوصول إلى خصائص الصفحة

ال [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) يوفر الفصل جميع الخصائص المتعلقة بصفحة PDF معينة. جميع صفحات ملفات PDF موجودة في [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) الكائنات [مجموعة الصفحات](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) مجموعة.

من هناك، يمكن الوصول إلى أي فرد `Page` الكائنات باستخدام الفهرس الخاص بها، أو قم بالتمرير عبر المجموعة للحصول على جميع الصفحات. بمجرد الوصول إلى صفحة فردية، يمكننا الحصول على خصائصها. يوضح مقتطف الشفرة التالي كيفية الحصول على خصائص الصفحة ( `Page` API).

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_properties(input_file_name):
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
        "Rect": page.rect,
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(
            f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}"
        )

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## تحديد لون الصفحة

ال [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) توفر الفئة الخصائص المتعلقة بصفحة معينة في مستند PDF، بما في ذلك نوع اللون - RGB، الأسود والأبيض، الرمادي أو غير المحدد - الذي تستخدمه الصفحة.

يتم تضمين جميع صفحات ملفات PDF بواسطة [مجموعة الصفحات](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) مجموعة. ال [نوع اللون](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) تحدد الخاصية لون العناصر على الصفحة. للحصول على معلومات اللون أو تحديدها لصفحة PDF معينة، استخدم [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) الكائنات [نوع اللون](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) الملكية.

يوضح مقتطف الشفرة التالي كيفية التكرار من خلال صفحة فردية من ملف PDF للحصول على معلومات اللون.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_color_type(input_file_name):
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
            ap.ColorType.UNDEFINED: "undefined",
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```

## موضوعات الصفحة ذات الصلة

- [العمل مع صفحات PDF في بايثون](/pdf/ar/python-net/working-with-pages/)
- [تغيير حجم صفحة PDF في Python](/pdf/ar/python-net/change-page-size/)
- [قص صفحات PDF في بايثون](/pdf/ar/python-net/crop-pages/)
- [تدوير صفحات PDF في بايثون](/pdf/ar/python-net/rotate-pages/)