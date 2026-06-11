---
title: قص صفحات PDF في بايثون
linktitle: قص صفحات PDF
type: docs
weight: 70
url: /ar/python-net/crop-pages/
description: تعرف على كيفية قص صفحات PDF وضبط مربعات الاقتصاص والتقليم والتسييل والوسائط في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية الوصول إلى خصائص الصفحة وتعديلها في PDF باستخدام Python
Abstract: تقدم المقالة نظرة عامة حول كيفية الوصول إلى خصائص الصفحة وتعديلها في مستند PDF باستخدام Aspose.PDF لـ Python. وهي تصف العديد من خصائص الصفحة، بما في ذلك مربع الوسائط، ومربع التسييل، ومربع القطع، ومربع الرسم، ومربع الاقتصاص، وتشرح أدوارها في تحديد أبعاد وحدود صفحة PDF لأغراض الطباعة والعرض. يمثل مربع الوسائط أكبر حجم للصفحة، بينما يضمن مربع التسييل تغطية الحبر خارج حافة الصفحة للتشذيب. يشير مربع القطع إلى حجم المستند النهائي بعد التشذيب، ويشتمل المربع الفني على محتوى الصفحة الفعلي. يحدد مربع الاقتصاص المنطقة المرئية في Adobe Acrobat. تتضمن المقالة مقتطفًا من شفرة Python يوضح كيفية تعيين مربع اقتصاص جديد، إلى جانب مربعات أخرى، لصفحة معينة في مستند PDF. توضح الأمثلة المرئية مظهر الصفحة قبل وبعد تطبيق الاقتصاص، وتعرض التطبيق العملي لتعديل هذه الخصائص.
---

## احصل على خصائص الصفحة

تحتوي كل صفحة في ملف PDF على عدد من الخصائص، مثل العرض والارتفاع ومربع التسييل والقص والتقطيع. Aspose.PDF لبيثون يسمح لك بالوصول إلى هذه الخصائص.

استخدم هذه الصفحة عندما تحتاج إلى تقليل مساحة الصفحة المرئية، أو إعداد الملفات لسير عمل الطباعة، أو فحص هندسة مربع الصفحة في مستندات PDF.

- **media_box**: صندوق الوسائط هو أكبر مربع صفحة. وهو يتوافق مع حجم الصفحة (على سبيل المثال A4 و A5 و US Letter وما إلى ذلك) المحدد عند طباعة المستند إلى PostScript أو PDF. بمعنى آخر، يحدد مربع الوسائط الحجم المادي للوسائط التي يتم عرض مستند PDF عليها أو طباعتها.
- **bleed_box**: في حالة حدوث نزيف في المستند، سيحتوي ملف PDF أيضًا على مربع التسييل. التسييل هو مقدار اللون (أو العمل الفني) الذي يمتد إلى ما وراء حافة الصفحة. يتم استخدامه للتأكد من أنه عند طباعة المستند وتقطيعه إلى حجمه («اقتطاعه»)، سينتقل الحبر إلى حافة الصفحة. حتى في حالة عدم دقة الصفحة - قم بقطع علامات القطع قليلاً - لن تظهر أي حواف بيضاء على الصفحة.
- **trim_box**: يشير مربع القطع إلى الحجم النهائي للمستند بعد الطباعة والتشذيب.
- **art_box**: المربع الفني هو المربع المرسوم حول المحتويات الفعلية للصفحات في مستنداتك. يتم استخدام مربع الصفحة هذا عند استيراد مستندات PDF في تطبيقات أخرى.
- **crop_box**: مربع الاقتصاص هو حجم «الصفحة» الذي يتم عرض مستند PDF به في Adobe Acrobat. في العرض العادي، يتم عرض محتويات مربع الاقتصاص فقط في Adobe Acrobat. للحصول على أوصاف تفصيلية لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، وخاصة حدود الصفحات 10.10.1.

قص الأول [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) من ملف PDF إلى منطقة مستطيلة محددة باستخدام Aspose.PDF لبيثون. تقوم الوظيفة بضبط مربعات صفحات متعددة—`crop_box`, `trim_box`, `art_box`، و `bleed_box`- لضمان نتائج مرئية متسقة. يمكن أن يكون الاقتصاص مفيدًا لإزالة الهوامش غير المرغوب فيها أو التركيز على منطقة معينة من الصفحة.

1. قم بتحميل ملف PDF كملف [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (استخدم `ap.Document()`).
1. حدد مستطيل الاقتصاص باستخدام [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) مع الإحداثيات المطلوبة (بالنقاط).
1. قم بتعيين [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)ق `crop_box`, `trim_box`, `art_box`، و `bleed_box` إلى المستطيل المحدد.
1. احفظ التعديل [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) إلى ملف إخراج جديد.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

في هذا المثال، استخدمنا ملف عينة [هنا](crop_page.pdf). في البداية تبدو صفحتنا كما هو موضح في الشكل 1.
![الشكل 1. صفحة مقصوصة](crop_page.png)

بعد التغيير، ستبدو الصفحة بالشكل 2.
![الشكل 2. صفحة مقصوصة](crop_page2.png)

## قص صفحة PDF بناءً على محتوى الصورة الأولى

قص الأول [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ديناميكيًا استنادًا إلى حدود الصورة الأولى الموجودة على الصفحة. باستخدام [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/)، يحدد البرنامج النصي الصورة الأولى ويضبط الصفحة `crop_box` لتتناسب مع أبعاد الصورة. هذا الأسلوب مفيد عندما تريد التركيز على محتوى مرئي محدد بدلاً من الإحداثيات المحددة مسبقًا.

1. قم بتحميل ملف PDF كملف [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. حدد موقع الصور على الصفحة الأولى باستخدام [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. تحقق من وجود الصور:
    - في حالة العثور عليها، قم بتعيين [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) `crop_box` لتتناسب مع الصورة الأولى [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
    - إذا لم يكن الأمر كذلك، احتفظ بالصفحة دون تغيير وأبلغ المستخدم.
1. احفظ التعديل [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) إلى ملف الإخراج المحدد.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page_by_content(input_file_name, output_file_name):
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

## موضوعات الصفحة ذات الصلة

- [العمل مع صفحات PDF في بايثون](/pdf/ar/python-net/working-with-pages/)
- [تغيير حجم صفحة PDF في Python](/pdf/ar/python-net/change-page-size/)
- [الحصول على خصائص صفحة PDF وتعيينها في Python](/pdf/ar/python-net/get-and-set-page-properties/)
- [تدوير صفحات PDF في بايثون](/pdf/ar/python-net/rotate-pages/)