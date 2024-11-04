---
title: الحصول على خصائص الصفحة وتعيينها باستخدام Python
linktitle: الحصول على خصائص الصفحة وتعيينها
type: docs
weight: 90
url: /python-net/get-and-set-page-properties/
description: يوضح هذا القسم كيفية الحصول على عدد الصفحات في ملف PDF، والحصول على معلومات حول خصائص صفحة PDF مثل اللون وتعيين خصائص الصفحة.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "الحصول على خصائص الصفحة وتعيينها باستخدام Python",
    "alternativeHeadline": "الحصول على خصائص صفحات PDF وتعيينها",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "pdf, python, الحصول على خصائص الصفحة, تعيين خصائص الصفحة",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "فريق مستندات Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-and-set-page-properties/"
    },
    "dateModified": "2023-04-04",
    "description": ""
}
</script>


Aspose.PDF لـ Python عبر .NET يتيح لك قراءة وتعيين خصائص الصفحات في ملف PDF في تطبيقات Python الخاصة بك. يوضح هذا القسم كيفية الحصول على عدد الصفحات في ملف PDF، والحصول على معلومات حول خصائص صفحة PDF مثل اللون وتعيين خصائص الصفحة. الأمثلة المعطاة هي بلغة Python.

## الحصول على عدد الصفحات في ملف PDF

عند العمل مع المستندات، غالبًا ما ترغب في معرفة عدد الصفحات التي تحتوي عليها. مع Aspose.PDF لا يستغرق الأمر أكثر من سطرين من التعليمات البرمجية.

للحصول على عدد الصفحات في ملف PDF:

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. ثم استخدم خاصية Count لمجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (من كائن Document) للحصول على العدد الإجمالي للصفحات في المستند.

يظهر مقتطف الكود التالي كيفية الحصول على عدد الصفحات في ملف PDF.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # الحصول على عدد الصفحات
    print("عدد الصفحات:", str(len(document.pages)))
```


### احصل على عدد الصفحات دون حفظ المستند

في بعض الأحيان نقوم بإنشاء ملفات PDF بشكل فوري وأثناء إنشاء ملف PDF قد نصادف الحاجة (إنشاء جدول المحتويات، إلخ) للحصول على عدد صفحات ملف PDF دون حفظ الملف على النظام أو البث. لذلك من أجل تلبية هذا المتطلب، تم تقديم طريقة [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) في فئة Document. يرجى إلقاء نظرة على مقتطف الشيفرة التالي الذي يوضح الخطوات للحصول على عدد الصفحات دون حفظ المستند.

```python

    import aspose.pdf as ap

    # إنشاء مثيل للمستند
    document = ap.Document()
    # إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    page = document.pages.add()
    # إنشاء مثيل للحلقة
    for i in range(0, 300):
        # إضافة TextFragment إلى مجموعة الفقرات في كائن الصفحة
        page.paragraphs.add(ap.text.TextFragment("اختبار عدد الصفحات"))
    # معالجة الفقرات في ملف PDF للحصول على عدد صفحات دقيق
    document.process_paragraphs()
    # طباعة عدد الصفحات في المستند
    print("عدد الصفحات في المستند =", str(len(document.pages)))
```


## الحصول على خصائص الصفحة

كل صفحة في ملف PDF تحتوي على عدد من الخصائص، مثل العرض والارتفاع وصندوق النزيف وصندوق القطع وصندوق التشذيب. تتيح لك Aspose.PDF الوصول إلى هذه الخصائص.

### **فهم خصائص الصفحة: الفرق بين Artbox وBleedBox وCropBox وMediaBox وTrimBox وRect property**

- **صندوق الوسائط**: صندوق الوسائط هو أكبر صندوق للصفحة. يتوافق مع حجم الصفحة (على سبيل المثال A4، A5، رسالة الولايات المتحدة، إلخ) الذي تم اختياره عند طباعة المستند إلى PostScript أو PDF. بمعنى آخر، يحدد صندوق الوسائط الحجم الفعلي للوسائط التي يتم عرض أو طباعة مستند PDF عليها.
- **صندوق النزيف**: إذا كان للمستند نزيف، فسيحتوي PDF أيضًا على صندوق النزيف.
 Bleed هو مقدار اللون (أو العمل الفني) الذي يمتد إلى ما بعد حافة الصفحة. يُستخدم لضمان أنه عند طباعة الوثيقة وقصها إلى الحجم المطلوب ("مُقَصَّصة")، فإن الحبر سيصل إلى حافة الصفحة. حتى إذا كانت الصفحة مقصوصة بشكل غير دقيق - مقصوصة بشكل طفيف خارج علامات القص - فلن تظهر حواف بيضاء على الصفحة.

- **Trim box**: يشير مربع القص إلى الحجم النهائي لوثيقة بعد الطباعة والقص.
- **Art box**: مربع الفن هو المربع المرسوم حول المحتويات الفعلية للصفحات في وثائقك. يُستخدم هذا المربع عند استيراد وثائق PDF في تطبيقات أخرى.
- **Crop box**: مربع الاقتصاص هو حجم "الصفحة" الذي يتم عرض وثيقتك PDF به في Adobe Acrobat. في العرض العادي، يتم عرض محتويات مربع الاقتصاص فقط في Adobe Acrobat.
  للحصول على وصفات مفصلة لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، خاصة 10.10.1 حدود الصفحة.
- **Page.Rect**: التقاطع (المستطيل المرئي عادة) بين MediaBox و DropBox. الصورة أدناه توضح هذه الخصائص.

لمزيد من التفاصيل، يرجى زيارة [هذه الصفحة](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **الوصول إلى خصائص الصفحة**

توفر فئة [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) جميع الخصائص المتعلقة بصفحة PDF معينة. تحتوي جميع صفحات ملفات PDF في مجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) الخاصة بكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

من هناك، يمكن الوصول إلى كائنات الصفحة الفردية باستخدام الفهرس الخاص بها، أو التكرار عبر المجموعة باستخدام حلقة foreach للحصول على جميع الصفحات. بمجرد الوصول إلى صفحة فردية، يمكننا الحصول على خصائصها. يوضح مقطع الشيفرة التالي كيفية الحصول على خصائص الصفحة.

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)
    # احصل على صفحة معينة
    page = document.pages[1]
    # احصل على خصائص الصفحة
    print(
        "ArtBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.art_box.height,
            page.art_box.width,
            page.art_box.llx,
            page.art_box.lly,
            page.art_box.urx,
            page.art_box.ury,
        )
    )
    print(
        "BleedBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.bleed_box.height,
            page.bleed_box.width,
            page.bleed_box.llx,
            page.bleed_box.lly,
            page.bleed_box.urx,
            page.bleed_box.ury,
        )
    )
    print(
        "CropBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.crop_box.height,
            page.crop_box.width,
            page.crop_box.llx,
            page.crop_box.lly,
            page.crop_box.urx,
            page.crop_box.ury,
        )
    )
    print(
        "MediaBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.media_box.height,
            page.media_box.width,
            page.media_box.llx,
            page.media_box.lly,
            page.media_box.urx,
            page.media_box.ury,
        )
    )
    print(
        "TrimBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.trim_box.height,
            page.trim_box.width,
            page.trim_box.llx,
            page.trim_box.lly,
            page.trim_box.urx,
            page.trim_box.ury,
        )
    )
    print(
        "Rect : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.rect.height,
            page.rect.width,
            page.rect.llx,
            page.rect.lly,
            page.rect.urx,
            page.rect.ury,
        )
    )
    print("رقم الصفحة :", page.number)
    print("التدوير :", page.rotate)
```

## الحصول على صفحة معينة من ملف PDF

تتيح لك Aspose.PDF for Python [تقسيم ملف PDF إلى صفحات فردية](/pdf/python-net/split-pdf-document/) وحفظها كملفات PDF. الحصول على صفحة محددة في ملف PDF وحفظها كملف PDF جديد هو عملية مشابهة جدًا: قم بفتح المستند المصدر، الوصول إلى الصفحة، إنشاء مستند جديد وإضافة الصفحة إليه.

يحمل كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) الخاص بـ [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection) الصفحات في ملف PDF. للحصول على صفحة معينة من هذه المجموعة:

1. حدد فهرس الصفحة باستخدام خاصية Pages.
2. قم بإنشاء كائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) جديد.
3. أضف كائن [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) إلى كائن المستند الجديد.
4. قم بحفظ النتيجة باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

يوضح مقطع الشيفرة التالي كيفية الحصول على صفحة معينة من ملف PDF وحفظها كملف جديد.

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)

    # احصل على صفحة معينة
    page = document.pages[2]

    # احفظ الصفحة كملف PDF
    new_document = ap.Document()
    new_document.pages.add(page)
    new_document.save(output_pdf)
```

## تحديد لون الصفحة

توفر فئة [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) الخصائص المتعلقة بصفحة معينة في مستند PDF، بما في ذلك نوع اللون - RGB، الأسود والأبيض، الرمادي أو غير محدد - الذي تستخدمه الصفحة.

تُحتوى جميع صفحات ملفات PDF بواسطة مجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
 The [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) الخاصية تحدد لون العناصر على الصفحة. للحصول على أو تحديد معلومات اللون لصفحة PDF معينة، استخدم خاصية [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) الخاصة بكائن [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).

يُظهر مقطع الشيفرة التالي كيفية التكرار عبر صفحات ملف PDF للحصول على معلومات اللون.

```python

    import aspose.pdf as ap

    # افتح ملف PDF المصدر
    document = ap.Document(input_pdf)
    # كرر عبر جميع صفحات ملف PDF
    for page_n in range(0, len(document.pages)):
        page_number = page_n + 1
        # احصل على معلومات نوع اللون لصفحة PDF معينة
        page_color_type = document.pages[page_number].color_type
        if page_color_type == ap.ColorType.BLACK_AND_WHITE:
            print("الصفحة رقم " + str(page_number) + " بالأبيض والأسود.")

        if page_color_type == ap.ColorType.GRAYSCALE:
            print("الصفحة رقم " + str(page_number) + " بدرجات الرمادي.")

        if page_color_type == ap.ColorType.RGB:
            print("الصفحة رقم " + str(page_number) + " بنظام RGB.")

        if page_color_type == ap.ColorType.UNDEFINED:
            print("الصفحة رقم " + str(page_number) + " لونها غير معرف.")
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF لـ Python عبر مكتبة .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "مبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "بريطانيا",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة معالجة PDF لـ Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "ويندوز، ماك أو إس، لينكس",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>