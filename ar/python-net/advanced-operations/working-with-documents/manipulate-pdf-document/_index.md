---
title: التلاعب بوثيقة PDF في بايثون عبر .NET
linktitle: التلاعب بوثيقة PDF
type: docs
weight: 20
url: ar/python-net/manipulate-pdf-document/
description: تحتوي هذه المقالة على معلومات حول كيفية التحقق من وثيقة PDF لمعيار PDF A باستخدام بايثون، كيفية العمل مع الفهرس، كيفية تحديد تاريخ انتهاء PDF، إلخ.
keywords: "التلاعب بـ pdf بايثون"
lastmod: "2023-04-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "التلاعب بوثيقة PDF عبر بايثون",
    "alternativeHeadline": "كيفية التلاعب بملف PDF باستخدام بايثون",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء وثائق pdf",
    "keywords": "pdf, dotnet, python, التلاعب بملف pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق Aspose.PDF Doc",
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
                "contactType": "المبيعات",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "تحتوي هذه المقالة على معلومات حول كيفية التحقق من وثيقة PDF لمعيار PDF A باستخدام بايثون، كيفية العمل مع الفهرس، كيفية تحديد تاريخ انتهاء PDF، إلخ."
}
</script>


## التلاعب بمستند PDF في بايثون

## التحقق من مستند PDF وفقًا لمعيار PDF A (A 1A و A 1B)

للتحقق من توافق مستند PDF مع PDF/A-1a أو PDF/A-1b، استخدم طريقة [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) في فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). تتيح لك هذه الطريقة تحديد اسم الملف الذي سيتم حفظ النتيجة فيه ونوع التحقق المطلوب من تعداد PdfFormat: PDF_A_1A أو PDF_A_1B.

يُظهر لك مقطع الشيفرة التالي كيفية التحقق من مستند PDF لـ PDF/A-1A.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # التحقق من PDF لـ PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

يُظهر لك مقطع الشيفرة التالي كيفية التحقق من مستند PDF لـ PDF/A-1b.

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # التحقق من PDF لـ PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```


## العمل مع جدول المحتويات

### إضافة جدول المحتويات إلى ملف PDF موجود

يمثل جدول المحتويات في PDF "جدول المحتويات". وهو ميزة تتيح للمستخدمين التنقل بسرعة عبر مستند بتوفير نظرة عامة على أقسامه وعناوينه.

لإضافة جدول المحتويات إلى ملف PDF موجود، استخدم فئة العناوين في مساحة الأسماء [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/). يمكن لمساحة الأسماء [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) إنشاء ملفات PDF جديدة والتعامل مع الملفات الموجودة. لإضافة جدول المحتويات إلى ملف PDF موجود، استخدم مساحة الأسماء Aspose.Pdf. يوضح مقتطف الشيفرة التالي كيفية إنشاء جدول محتويات داخل ملف PDF موجود باستخدام بايثون عبر .NET.

```python

    import aspose.pdf as ap

    # تحميل ملف PDF موجود
    doc = ap.Document(input_pdf)

    # الوصول إلى الصفحة الأولى من ملف PDF
    tocPage = doc.pages.insert(1)

    # إنشاء كائن لتمثيل معلومات جدول المحتويات
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("جدول المحتويات")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # تعيين العنوان لجدول المحتويات
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # إنشاء كائنات نصية سيتم استخدامها كعناصر جدول المحتويات
    titles = ["الصفحة الأولى", "الصفحة الثانية", "الصفحة الثالثة", "الصفحة الرابعة"]
    for i in range(0, 2):
        # إنشاء كائن عنوان
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # تحديد الصفحة الوجهة لكائن العنوان
        heading2.destination_page = doc.pages[i + 2]

        # الصفحة الوجهة
        heading2.top = doc.pages[i + 2].rect.height

        # إحداثيات الوجهة
        segment2.text = titles[i]

        # إضافة العنوان إلى الصفحة التي تحتوي على جدول المحتويات
        tocPage.paragraphs.add(heading2)

    # حفظ المستند المحدث
    doc.save(output_pdf)
```


### تعيين نوع TabLeaderType مختلف لمستويات TOC المختلفة

تسمح Aspose.PDF لـ Python أيضًا بتعيين نوع TabLeaderType مختلف لمستويات TOC المختلفة. تحتاج إلى تعيين خاصية [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) لـ [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # تعيين LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("جدول المحتويات")
    title.text_state.font_size = 30
    toc_info.title = title

    # إضافة قسم القائمة إلى مجموعة الأقسام في مستند Pdf
    tocPage.toc_info = toc_info
    # تحديد تنسيق قائمة المستويات الأربعة من خلال تعيين الهوامش اليسرى
    # و
    # إعدادات تنسيق النص لكل مستوى

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    # إنشاء قسم في مستند Pdf
    page = doc.pages.add()

    # إضافة أربعة عناوين في القسم
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "عنوان تجريبي" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # إضافة العنوان إلى جدول المحتويات.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # حفظ ملف Pdf
    doc.save(output_pdf)
```


### إخفاء أرقام الصفحات في جدول المحتويات

في حالة عدم رغبتك في عرض أرقام الصفحات مع العناوين في جدول المحتويات، يمكنك استخدام خاصية [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) من الفئة [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) كقيمة false. يرجى مراجعة مقتطف الشيفرة التالي لإخفاء أرقام الصفحات في جدول المحتويات:

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("جدول المحتويات")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # أضف قسم القائمة إلى مجموعة الأقسام في مستند Pdf
    toc_page.toc_info = toc_info
    # تحديد تنسيق قائمة المستويات الأربعة عن طريق تعيين الهوامش اليسرى
    # وإعدادات تنسيق النص لكل مستوى

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # أضف أربعة عناوين في القسم
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "هذا عنوان للمستوى " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```


### تخصيص أرقام الصفحات عند إضافة جدول المحتويات

من الشائع تخصيص ترقيم الصفحات في جدول المحتويات عند إضافة جدول المحتويات في مستند PDF. على سبيل المثال، قد نحتاج إلى إضافة بعض البادئات قبل رقم الصفحة مثل P1، P2، P3 وهكذا. في مثل هذه الحالة، يوفر Aspose.PDF لـ Python خاصية [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) في فئة [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) والتي يمكن استخدامها لتخصيص أرقام الصفحات كما هو موضح في المثال البرمجي التالي.

```python

    import aspose.pdf as ap

    # تحميل ملفات PDF موجودة
    doc = ap.Document(input_pdf)
    # الوصول إلى الصفحة الأولى من ملف PDF
    toc_page = doc.pages.insert(1)
    # إنشاء كائن لتمثيل معلومات جدول المحتويات
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("جدول المحتويات")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # تعيين العنوان لجدول المحتويات
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # إنشاء كائن عنوان
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # تحديد الصفحة المقصودة لكائن العنوان
        heading2.destination_page = doc.pages[i + 1]
        # الصفحة المقصودة
        heading2.top = doc.pages[i + 1].rect.height
        # الإحداثيات المقصودة
        segment2.text = "صفحة " + str(i)
        # إضافة العنوان إلى الصفحة التي تحتوي على جدول المحتويات
        toc_page.paragraphs.add(heading2)

    # حفظ المستند المحدث
    doc.save(output_pdf)

```


## كيفية تعيين تاريخ انتهاء صلاحية ملف PDF

نقوم بتطبيق امتيازات الوصول على ملفات PDF بحيث يمكن لمجموعة معينة من المستخدمين الوصول إلى ميزات/كائنات معينة من مستندات PDF. من أجل تقييد الوصول إلى ملف PDF، نقوم عادةً بتطبيق التشفير وقد يكون لدينا متطلب لتعيين انتهاء صلاحية ملف PDF، بحيث يحصل المستخدم الذي يصل إلى المستند أو يعرضه على تنبيه صالح بخصوص انتهاء صلاحية ملف PDF.

```python

    import aspose.pdf as ap

    # إنشاء كائن Document
    doc = ap.Document()
    # إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    doc.pages.add()
    # إضافة جزء نصي إلى مجموعة الفقرات في كائن الصفحة
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    # إنشاء كائن JavaScript لتعيين تاريخ انتهاء صلاحية ملف PDF
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('The file is expired. You need a new one.');"
    )
    # تعيين JavaScript كإجراء فتح ملف PDF
    doc.open_action = javaScript

    # حفظ مستند PDF
    doc.save(output_pdf)
```


## تسوية استمارة PDF قابلة للتعبئة في بايثون

غالبًا ما تتضمن مستندات PDF نماذج بها عناصر تفاعلية قابلة للتعبئة مثل أزرار الراديو ومربعات الاختيار ومربعات النص والقوائم، إلخ. لجعلها غير قابلة للتحرير لأغراض تطبيقية مختلفة، نحتاج إلى تسوية ملف PDF.
يوفر Aspose.PDF الوظيفة لتسوية PDF الخاص بك في بايثون ببضع سطور من الكود فقط:

```python

    import aspose.pdf as ap

    # تحميل نموذج PDF المصدر
    doc = ap.Document(input_pdf)

    # تسوية استمارة PDF القابلة للتعبئة
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # حفظ المستند المحدث
    doc.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://releases.aspose.com/pdf/python-net",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>