---
title: تنسيق مستند PDF باستخدام بايثون
linktitle: تنسيق مستند PDF
type: docs
weight: 11
url: /ar/python-net/formatting-pdf-document/
description: قم بإنشاء وتنسيق مستند PDF باستخدام Aspose.PDF لبايثون عبر .NET. استخدم الجزء التالي من الكود لحل مهامك.
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تنسيق مستند PDF باستخدام بايثون",
    "alternativeHeadline": "كيفية تنسيق مستند PDF في بايثون عبر .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات pdf",
    "keywords": "pdf, dotnet, python, تنسيق مستند pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/formatting-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "قم بإنشاء وتنسيق مستند PDF باستخدام Aspose.PDF لبايثون عبر .NET. استخدم الجزء التالي من الكود لحل مهامك."
}
</script>


## تنسيق مستند PDF

### الحصول على خصائص نافذة المستند وعرض الصفحة

يساعدك هذا الموضوع على فهم كيفية الحصول على خصائص نافذة المستند، وتطبيق العارض، وكيفية عرض الصفحات. لتعيين هذه الخصائص:

افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). يمكنك الآن تعيين خصائص كائن المستند، مثل

- CenterWindow – تمركز نافذة المستند على الشاشة. الافتراضي: خطأ.
- Direction – ترتيب القراءة. يحدد هذا كيفية ترتيب الصفحات عند عرضها جنبًا إلى جنب. الافتراضي: من اليسار إلى اليمين.
- DisplayDocTitle – عرض عنوان المستند في شريط عنوان نافذة المستند. الافتراضي: خطأ (يتم عرض العنوان).
- HideMenuBar – إخفاء أو عرض شريط القوائم الخاص بنافذة المستند. الافتراضي: خطأ (يتم عرض شريط القوائم).
- HideToolBar – إخفاء أو عرض شريط الأدوات الخاص بنافذة المستند. الافتراضي: خطأ (يتم عرض شريط الأدوات).
- HideWindowUI – إخفاء أو عرض عناصر نافذة المستند مثل أشرطة التمرير.
 الافتراضي: false (يتم عرض عناصر واجهة المستخدم).
- NonFullScreenPageMode – كيفية عرض المستند عند عدم عرضه في وضع الشاشة الكاملة.
- PageLayout – تخطيط الصفحة.
- PageMode – كيفية عرض المستند عند فتحه لأول مرة. الخيارات هي عرض الصور المصغرة، الشاشة الكاملة، عرض لوحة المرفقات.

يظهر لك مقتطف الشيفرة التالي كيفية الحصول على الخصائص باستخدام فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # الحصول على خصائص المستند المختلفة
    # موضع نافذة المستند - الافتراضي: false
    print("CenterWindow :", document.center_window)

    # ترتيب القراءة السائد؛ يحدد موضع الصفحة
    # عندما يتم العرض جنبًا إلى جنب - الافتراضي: L2R
    print("Direction :", document.direction)

    # ما إذا كان يجب أن تعرض شريط عنوان النافذة عنوان المستند
    # إذا كان false، يعرض شريط العنوان اسم ملف PDF - الافتراضي: false
    print("DisplayDocTitle :", document.display_doc_title)

    # ما إذا كان يجب تغيير حجم نافذة المستند لتتناسب مع حجم
    # الصفحة الأولى المعروضة - الافتراضي: false
    print("FitWindow :", document.fit_window)

    # ما إذا كان يجب إخفاء شريط القوائم لتطبيق العارض - الافتراضي: false
    print("HideMenuBar :", document.hide_menubar)

    # ما إذا كان يجب إخفاء شريط الأدوات لتطبيق العارض - الافتراضي: false
    print("HideToolBar :", document.hide_tool_bar)

    # ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل أشرطة التمرير
    # وترك محتويات الصفحة فقط معروضة - الافتراضي: false
    print("HideWindowUI :", document.hide_window_ui)

    # وضع صفحة المستند. كيفية عرض المستند عند الخروج من وضع الشاشة الكاملة.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # تخطيط الصفحة أي صفحة واحدة، عمود واحد
    print("PageLayout :", document.page_layout)

    # كيف ينبغي عرض المستند عند فتحه
    # أي عرض الصور المصغرة، الشاشة الكاملة، عرض لوحة المرفقات
    print("pageMode :", document.page_mode)

```

### إعداد خصائص نافذة وعرض الصفحة للمستند

يشرح هذا الموضوع كيفية إعداد خصائص نافذة المستند، وتطبيق العارض، وعرض الصفحة. لتعيين هذه الخصائص المختلفة:

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. قم بتعيين خصائص كائن المستند.
3. احفظ ملف PDF المحدث باستخدام طريقة الحفظ.

الخصائص المتاحة هي:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

يتم استخدام كل منها ووصفها في الشيفرة أدناه. يظهر لك مقتطف الشيفرة التالي كيفية تعيين الخصائص باستخدام فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # افتح المستند
    document = ap.Document(input_pdf)

    # تعيين خصائص المستند المختلفة
    # تحديد موضع نافذة المستند - الافتراضي: false
    document.center_window = True

    # ترتيب القراءة السائد؛ يحدد موضع الصفحة
    # عند العرض جنبًا إلى جنب - الافتراضي: L2R
    document.direction = ap.Direction.R2L

    # تحديد ما إذا كان شريط عنوان النافذة يجب أن يعرض عنوان المستند
    # إذا كانت false، يعرض شريط العنوان اسم ملف PDF - الافتراضي: false
    document.display_doc_title = True

    # تحديد ما إذا كان يجب تغيير حجم نافذة المستند لتناسب حجم
    # الصفحة المعروضة أولاً - الافتراضي: false
    document.fit_window = True

    # تحديد ما إذا كان يجب إخفاء شريط القائمة في تطبيق العارض - الافتراضي: false
    document.hide_menubar = True

    # تحديد ما إذا كان يجب إخفاء شريط الأدوات في تطبيق العارض - الافتراضي: false
    document.hide_tool_bar = True

    # تحديد ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل أشرطة التمرير
    # وترك محتويات الصفحة فقط معروضة - الافتراضي: false
    document.hide_window_ui = True

    # وضع صفحة المستند. تحديد كيفية عرض المستند عند الخروج من وضع الشاشة الكاملة.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # تحديد تخطيط الصفحة أي صفحة واحدة، عمود واحد
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # تحديد كيفية عرض المستند عند فتحه
    # أي عرض الصور المصغرة، الشاشة الكاملة، عرض لوحة المرفقات
    document.page_mode = ap.PageMode.USE_THUMBS

    # حفظ ملف PDF المحدث
    document.save(output_pdf)
```


### تضمين خطوط نوع 1 القياسية

بعض مستندات PDF تحتوي على خطوط من مجموعة خطوط Adobe خاصة. وتسمى الخطوط من هذه المجموعة "خطوط نوع 1 القياسية". تتضمن هذه المجموعة 14 خطًا ويتطلب تضمين هذا النوع من الخطوط استخدام علامات خاصة مثل [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). فيما يلي مقتطف الشيفرة الذي يمكن استخدامه للحصول على مستند مع جميع الخطوط المضمنة بما في ذلك خطوط نوع 1 القياسية:

```python

    import aspose.pdf as ap

    # تحميل مستند PDF موجود
    document = ap.Document(input_pdf)
    # تعيين خاصية EmbedStandardFonts للمستند
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # التحقق مما إذا كان الخط مضمنًا بالفعل
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### تضمين الخطوط أثناء إنشاء PDF

إذا كنت بحاجة لاستخدام أي خط غير الخطوط الأساسية الأربعة عشر المدعومة من قبل Adobe Reader، فيجب عليك تضمين وصف الخط أثناء إنشاء ملف PDF. إذا لم تكن معلومات الخط مضمنة، فسيقوم Adobe Reader بأخذها من نظام التشغيل إذا كانت مثبتة على النظام، أو سيقوم بتكوين خط بديل وفقًا لوصف الخط في PDF.

> يرجى ملاحظة أنه يجب تثبيت الخط المضمن على الجهاز المضيف، أي في حالة الكود التالي، يتم تثبيت خط 'Univers Condensed' على النظام.

نستخدم الخاصية 'is_embedded' لتضمين معلومات الخط في ملف PDF. تعيين قيمة هذه الخاصية إلى 'True' سيقوم بتضمين ملف الخط الكامل في PDF، مع العلم أن ذلك سيزيد من حجم ملف PDF. فيما يلي مقتطف الكود الذي يمكن استخدامه لتضمين معلومات الخط في PDF.

```python

    import aspose.pdf as ap

    # إنشاء كائن Pdf عن طريق استدعاء منشئه الفارغ
    doc = ap.Document()

    # إنشاء قسم في كائن Pdf
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" هذا نص تجريبي باستخدام خط مخصص.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # حفظ مستند PDF
    doc.save(output_pdf)
```


### تعيين اسم الخط الافتراضي أثناء حفظ PDF

عندما يحتوي مستند PDF على خطوط غير متوفرة في المستند نفسه وعلى الجهاز، تقوم API باستبدال هذه الخطوط بالخط الافتراضي. إذا كان الخط متاحًا (مثبتًا على الجهاز أو مضمنًا في المستند)، يجب أن يحتوي ملف PDF الناتج على نفس الخط (يجب ألا يتم استبداله بالخط الافتراضي). يجب أن تحتوي قيمة الخط الافتراضي على اسم الخط (وليس مسار ملفات الخط). لقد قمنا بتطبيق ميزة لتعيين اسم الخط الافتراضي أثناء حفظ المستند كملف PDF. يمكن استخدام الكود التالي لتعيين الخط الافتراضي:

```python

    import aspose.pdf as ap

    # تحميل مستند PDF موجود بخط مفقود
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # تحديد اسم الخط الافتراضي
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### الحصول على جميع الخطوط من مستند PDF

في حالة رغبتك في الحصول على جميع الخطوط من مستند PDF، يمكنك استخدام طريقة [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) المقدمة في فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
 يرجى التحقق من مقتطف الشيفرة التالي للحصول على جميع الخطوط من وثيقة PDF الموجودة:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### تحسين تضمين الخطوط باستخدام FontSubsetStrategy

يوضح مقتطف الشيفرة التالي كيفية تعيين [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) باستخدام خاصية [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties):

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # سيتم تضمين جميع الخطوط كجزء من الوثيقة في حالة SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # سيتم تضمين جزء من الخطوط المدمجة بالكامل في الوثيقة، ولكن الخطوط التي لم يتم تضمينها لن تتأثر.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### الحصول على وتعيين عامل التكبير لملف PDF

أحيانًا، تريد تحديد ما هو عامل التكبير الحالي لمستند PDF. باستخدام Aspose.Pdf، يمكنك معرفة القيمة الحالية وكذلك تعيين واحدة.

تسمح لك خاصية الوجهة [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) بالحصول على قيمة التكبير المرتبطة بملف PDF. وبالمثل، يمكن استخدامها لتعيين عامل التكبير لملف.

#### تعيين عامل التكبير

يظهر مقطع الكود التالي كيفية تعيين عامل التكبير لملف PDF.

```python

    import aspose.pdf as ap

    # إنشاء كائن مستند جديد
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # حفظ المستند
    doc.save(output_pdf)
```

#### الحصول على عامل التكبير

يظهر مقطع الكود التالي كيفية الحصول على عامل التكبير لملف PDF.

```python

    import aspose.pdf as ap

    # إنشاء كائن مستند جديد
    doc = ap.Document(input_pdf)

    # إنشاء كائن GoToAction
    action = doc.open_action

    # الحصول على عامل التكبير لملف PDF
    print(action.destination.zoom)
```


### إعداد خصائص الطباعة المسبقة

تسمح Aspose.PDF بتعيين أعضاء [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) لوثيقة PDF. يسمح لك بتغيير خاصية DuplexMode لوثيقة PDF التي يتم تعيينها إلى simplex بشكل افتراضي. يمكن تحقيق ذلك باستخدام منهجيتين مختلفتين كما هو موضح أدناه.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### إعداد خصائص الطباعة المسبقة باستخدام محرر محتوى PDF

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("الملف يحتوي على قلب مزدوج للحافة القصيرة")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```