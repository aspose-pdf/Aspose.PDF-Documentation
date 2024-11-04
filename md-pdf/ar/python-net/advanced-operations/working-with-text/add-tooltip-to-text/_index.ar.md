---
title: PDF Tooltip using Python
linktitle: PDF Tooltip
type: docs
weight: 20
url: /python-net/pdf-tooltip/
description: تعلم كيفية إضافة تلميح الأدوات إلى جزء النص في PDF باستخدام Python وAspose.PDF
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip using Python",
    "alternativeHeadline": "Add PDF Tooltip to the Text",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, add pdf tooltip",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/python-net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/pdf-tooltip/"
    },
    "dateModified": "2024-02-04",
    "description": "تعلم كيفية إضافة تلميح الأدوات إلى جزء النص في PDF باستخدام Python وAspose.PDF"
}
</script>


## إضافة تلميح إلى النص الذي تم البحث عنه عن طريق إضافة زر غير مرئي

يعرض هذا الكود كيفية إضافة تلميحات إلى أجزاء نصية محددة في مستند PDF باستخدام Aspose.PDF. يتم عرض التلميحات عندما يحوم مؤشر الفأرة فوق النص المقابل.

سيعرض لك مقتطف الكود التالي الطريقة لتحقيق هذه الوظيفة:

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("حرك مؤشر الفأرة هنا لعرض تلميح")
    )
    document.pages[1].paragraphs.add(
        ap.text.TextFragment(
            "حرك مؤشر الفأرة هنا لعرض تلميح طويل جدًا"
        )
    )
    document.save(output_pdf)

    # فتح المستند مع النص
    document = ap.Document(output_pdf)
    # إنشاء كائن TextAbsorber للعثور على جميع العبارات المطابقة للتعبير العادي
    absorber = ap.text.TextFragmentAbsorber(
        "حرك مؤشر الفأرة هنا لعرض تلميح"
    )
    # قبول المستخرج لصفحات المستند
    document.pages.accept(absorber)
    # الحصول على الأجزاء النصية المستخرجة
    text_fragments = absorber.text_fragments

    # حلقة على الأجزاء
    for fragment in text_fragments:
        # إنشاء زر غير مرئي على موضع الجزء النصي
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # قيمة alternate_name ستظهر كتلميح بواسطة تطبيق العرض
        field.alternate_name = "تلميح للنص."
        # إضافة حقل الزر إلى المستند
        document.form.add(field)

    # سيكون التالي مثال على تلميح طويل جدًا
    absorber = ap.text.TextFragmentAbsorber(
        "حرك مؤشر الفأرة هنا لعرض تلميح طويل جدًا"
    )
    document.pages.accept(absorber)
    text_fragments = absorber.text_fragments

    for fragment in text_fragments:
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # تعيين نص طويل جدًا
        field.alternate_name = (
            "لوريم إيبسوم دولور سيت أميت، كونسيكتيتور أديبيسيسينغ إيليت،"
            " سيد دو إيوسيمود تيمبور إنسيديدونت أوت لابوري إت دولوري ماجنا"
            " أليكا. أوت إينيم أد مينيم فينيام، كويز نوسترود إكسرسيتيشن"
            " ألامكو لابوريس نيسي أوت أليكيوب إكس إي كومودو كونسيكوات."
            " دويس أوتي إيروري دولور إن ريبريهينديريت إن وولبتات فيليت"
            " إيسي سيلوم دولور إيو فيوجيات نولا بارياتور. إكسسيبتور سينت"
            " أوكاكات كيوبيداتات نون برويدنت، سونت إن كيولبا كي أوفيسيا"
            " ديسيرونت موليت أنيم آيد إست لابوروم."
        )
        document.form.add(field)

    # حفظ المستند
    document.save(output_pdf)
```


## إنشاء كتلة نصية مخفية وعرضها عند التمرير بالماوس

يعرض مقتطف الشيفرة بلغة بايثون كيفية إضافة نص عائم إلى مستند PDF، والذي يظهر عند تمرير مؤشر الماوس فوق منطقة محددة.

أولاً، يتم إنشاء مستند PDF جديد، ويتم إضافة فقرة تحتوي على النص "حرك مؤشر الماوس هنا لعرض النص العائم". ثم يتم حفظ المستند.

بعد ذلك، يُعاد فتح المستند المحفوظ، ويتم إنشاء كائن TextAbsorber للبحث عن جزء النص الذي أضيف مسبقًا. يُستخدم هذا الجزء من النص لتحديد موضع وخصائص حقل النص العائم.

يتم إنشاء كائن TextBoxField لتمثيل حقل النص العائم، وتُضبط خصائصه مثل الموضع، والقيمة، وحالة القراءة فقط، والوضوح وفقًا لذلك. بالإضافة إلى ذلك، يتم تعيين اسم فريد وخصائص المظهر للحقل.

يُضاف حقل النص العائم إلى نموذج المستند، ويتم إنشاء حقل زر غير مرئي في موضع جزء النص الأصلي.
 الأحداث HideAction مخصصة لحقل الزر، مما يحدد أن حقل النص العائم يجب أن يظهر عندما يدخل مؤشر الفأرة في محيطه ويختفي عند خروج المؤشر.

أخيرًا، يتم إضافة حقل الزر إلى نموذج المستند، ويتم حفظ المستند المعدل.

يوفر هذا المقتطف من الكود طريقة لإنشاء عناصر نص عائمة تفاعلية في مستند PDF باستخدام Aspose.PDF لـ Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("انقل مؤشر الفأرة هنا لعرض النص العائم")
    )
    document.save(output_pdf)

    # افتح المستند مع النص
    document = ap.Document(output_pdf)
    # إنشاء كائن TextAbsorber للعثور على جميع العبارات التي تطابق التعبير العادي
    absorber = ap.text.TextFragmentAbsorber(
        "انقل مؤشر الفأرة هنا لعرض النص العائم"
    )
    # قبول الماص للصفحات المستند
    document.pages.accept(absorber)
    # احصل على أول جزء نصي مُستخرج
    text_fragments = absorber.text_fragments
    fragment = text_fragments[1]

    # إنشاء حقل نص مخفي للنص العائم في المستطيل المحدد للصفحة
    floating_field = ap.forms.TextBoxField(
        fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
    )
    # تعيين النص ليُعرض كقيمة الحقل
    floating_field.value = 'هذا هو "حقل النص العائم".'
    # نوصي بجعل الحقل 'للقراءة فقط' لهذا السيناريو
    floating_field.read_only = True
    # تعيين علامة 'مخفي' لجعل الحقل غير مرئي عند فتح المستند
    floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

    # تعيين اسم حقل فريد ليس ضروريًا ولكن مسموح به
    floating_field.partial_name = "FloatingField_1"

    # تعيين خصائص مظهر الحقل ليس ضروريًا ولكن يجعله أفضل
    floating_field.default_appearance = ap.annotations.DefaultAppearance(
        "Helv", 10, ap.Color.blue.to_rgb()
    )
    floating_field.characteristics.background = ap.Color.light_blue.to_rgb()
    floating_field.characteristics.border = ap.Color.dark_blue.to_rgb()
    floating_field.border = ap.annotations.Border(floating_field)
    floating_field.border.width = 1
    floating_field.multiline = True

    # إضافة حقل نص إلى المستند
    document.form.add(floating_field)
    # إنشاء زر غير مرئي في موقع جزء النص
    button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
    # إنشاء إجراء إخفاء جديد للحقل المحدد (التعليق) وعلامة عدم الظهور.
    # (يمكنك أيضًا الإشارة إلى الحقل العائم بالاسم إذا حددته أعلاه.)
    # إضافة إجراءات عند دخول/خروج الفأرة في حقل الزر غير المرئي

    button_field.actions.on_enter = ap.annotations.HideAction(
        floating_field.partial_name, False
    )
    button_field.actions.on_exit = ap.annotations.HideAction(
        floating_field.partial_name
    )

    # إضافة حقل الزر إلى المستند
    document.form.add(button_field)

    # حفظ المستند
    document.save(output_pdf)
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
    "applicationCategory": "مكتبة معالجة PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>