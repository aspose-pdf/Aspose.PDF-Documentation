---
title: التعليقات التوضيحية الإضافية باستخدام Python
linktitle: التعليقات التوضيحية الإضافية
type: docs
weight: 60
url: /ar/python-net/extra-annotations/
description: يصف هذا القسم كيفية إضافة، الحصول على، وحذف أنواع إضافية من التعليقات التوضيحية من مستند PDF الخاص بك.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "التعليقات التوضيحية الإضافية باستخدام Python",
    "alternativeHeadline": "كيفية إضافة تعليقات توضيحية إضافية في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, python, تعليق توضيحي على الرابط, تعليق توضيحي على علامة",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
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
    "url": "/python-net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extra-annotations/"
    },
    "dateModified": "2023-02-04",
    "description": "يصف هذا القسم كيفية إضافة، الحصول على، وحذف أنواع إضافية من التعليقات التوضيحية من مستند PDF الخاص بك باستخدام Python."
}
</script>


## كيفية إضافة توضيح Caret إلى ملف PDF موجود عبر بايثون

توضيح Caret هو رمز يشير إلى تحرير النص. توضيح Caret هو أيضًا توضيح ترميز، لذا فإن فئة Caret تشتق من فئة Markup وتوفر أيضًا وظائف للحصول أو تعيين خصائص توضيح Caret وإعادة تعيين تدفق مظهر توضيح Caret.
غالبًا ما تستخدم توضيحات Caret لاقتراح تغييرات أو إضافات أو تغييرات على النص.

الخطوات التي ننشئ بها توضيح Caret:

1. تحميل ملف PDF - جديد [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. إنشاء [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) جديد وتعيين معلمات Caret (مستطيل جديد، العنوان، الموضوع، الأعلام، اللون). يُستخدم هذا التوضيح للإشارة إلى إدراج النص.
1. بمجرد أن نتمكن من إلحاق التوضيحات بالصفحة.

يظهر الكود التالي كيفية إضافة توضيح Caret إلى ملف PDF:

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Aspose User"
    caretAnnotation1.subject = "Inserted text 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```


### احصل على توضيح Caret

يرجى محاولة استخدام مقتطف الشيفرة التالي للحصول على توضيح Caret في مستند PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        print(ca.rect)
```

### حذف توضيح Caret

يوضح مقتطف الشيفرة التالي كيفية حذف توضيح Caret من ملف PDF باستخدام بايثون.

```python

    import aspose.pdf as ap

    # تحميل ملف PDF
    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

## إضافة توضيح رابط

[الروابط](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) هي توضيحات تفتح عناوين URL أو تنتقل إلى مواقع معينة داخل نفس المستند أو داخل مستند خارجي عند النقر عليها.

A Link Annotations هو مساحة مستطيلة يمكن وضعها في أي مكان على الصفحة. كل رابط له إجراء PDF مرافق يتم تنفيذه عند نقر المستخدم في منطقة هذا الرابط.

يظهر مقتطف الشيفرة التالي كيفية إضافة رابط توضيحي لملف PDF باستخدام مثال رقم هاتف:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # إنشاء كائن TextFragmentAbsorber للعثور على رقم هاتف
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # قبول الماص للصفحة الأولى فقط
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # إنشاء رابط توضيحي وتعيين الإجراء للاتصال برقم هاتف
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # إضافة التوضيح إلى الصفحة
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```


### الحصول على تعليق الارتباط

يرجى محاولة استخدام مقطع الشيفرة التالي للحصول على [تعليق الارتباط](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) من مستند PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### حذف تعليق الارتباط

يُظهر مقطع الشيفرة التالي كيفية حذف تعليق الارتباط من ملف PDF. لهذا نحتاج إلى العثور على كل تعليقات الارتباط في الصفحة الأولى وإزالتها. بعد ذلك سنحفظ المستند بعد إزالة التعليق.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```


## إخفاء منطقة معينة من الصفحة باستخدام تعليق الإخفاء باستخدام Aspose.PDF لـ Python

يدعم Aspose.PDF لـ Python عبر .NET ميزة إضافة التعليقات وكذلك تعديلها في ملف PDF موجود. تخدم تعليقات الإخفاء في مستندات PDF غرض إزالة أو إخفاء المعلومات السرية من المستند بشكل دائم. تتضمن عملية تحرير المعلومات تغطية أو تظليل محتوى معين، مثل النصوص أو الصور أو الرسومات، بطريقة تقيد رؤيته وإمكانية الوصول إليه من قبل الآخرين. يضمن ذلك بقاء المعلومات الحساسة مخفية ومحميّة داخل المستند. لتلبية هذا المتطلب، يتم توفير فئة باسم [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/) التي يمكن استخدامها لإخفاء مناطق معينة من الصفحة أو يمكن استخدامها لتعديل تعليقات الإخفاء الحالية وإخفائها (أي تسطيح التعليق وإزالة النص الموجود تحته).

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    redactionAnnotation = ap.annotations.RedactionAnnotation(page, ap.Rectangle(270, 190, 371, 250, True))
    redactionAnnotation.title = "John Smith"
    redactionAnnotation.fill_color = ap.Color.light_gray
    redactionAnnotation.color = ap.Color.red
    redactionAnnotation.redact()

    page.annotations.append(redactionAnnotation)
    document.save(output_file)
```


### الحصول على تعليق التعتيم

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        print(pa.rect)
```    

### حذف تعليق التعتيم

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```  

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
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
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>