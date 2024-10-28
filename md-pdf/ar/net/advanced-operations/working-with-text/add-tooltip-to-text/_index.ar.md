---
title: استخدام تلميح PDF باستخدام C#
linktitle: تلميح PDF
type: docs
weight: 20
url: /net/pdf-tooltip/
description: تعلم كيفية إضافة تلميح إلى جزء النص في PDF باستخدام C# و Aspose.PDF
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "استخدام تلميح PDF باستخدام C#",
    "alternativeHeadline": "إضافة تلميح PDF إلى النص",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثائق PDF",
    "keywords": "pdf, c#, إضافة تلميح pdf",
    "wordcount": "302",
    "proficiencyLevel": "مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-tooltip/"
    },
    "dateModified": "2022-02-04",
    "description": "تعلم كيفية إضافة تلميح إلى جزء النص في PDF باستخدام C# و Aspose.PDF"
}
</script>
الشفرة التالية تعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## إضافة تلميح للنص المبحوث عنه عن طريق إضافة زر غير مرئي

غالباً ما يُطلب إضافة بعض التفاصيل لعبارة أو كلمة معينة كتلميح في مستند PDF بحيث يظهر عندما يمرر المستخدم مؤشر الفأرة فوق النص. يوفر Aspose.PDF لـ .NET هذه الميزة لإنشاء التلميحات عن طريق إضافة زر غير مرئي فوق النص المبحوث عنه. ستظهر لك الشفرة التالية الطريقة لتحقيق هذه الوظيفة:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string outputFile = dataDir + "Tooltip_out.pdf";

// إنشاء مستند نموذجي بنص
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("حرك مؤشر الفأرة هنا لعرض تلميح"));
doc.Pages[1].Paragraphs.Add(new TextFragment("حرك مؤشر الفأرة هنا لعرض تلميح طويل جداً"));
doc.Save(outputFile);

// فتح المستند بنص
Document document = new Document(outputFile);
// إنشاء كائن TextAbsorber للعثور على جميع العبارات التي تطابق التعبير النظامي
TextFragmentAbsorber absorber = new TextFragmentAbsorber("حرك مؤشر الفأرة هنا لعرض تلميح");
// قبول الممتص لصفحات المستند
document.Pages.Accept(absorber);
// الحصول على فقرات النص المستخرجة
TextFragmentCollection textFragments = absorber.TextFragments;

// التكرار عبر الفقرات
foreach (TextFragment fragment in textFragments)
{
    // إنشاء زر غير مرئي على موضع فقرة النص
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // سيتم عرض قيمة AlternateName كتلميح بواسطة تطبيق المشاهد
    field.AlternateName = "تلميح للنص.";
    // إضافة حقل الزر للمستند
    document.Form.Add(field);
}

// التالي سيكون نموذج لتلميح طويل جداً
absorber = new TextFragmentAbsorber("حرك مؤشر الفأرة هنا لعرض تلميح طويل جداً");
document.Pages.Accept(absorber);
textFragments = absorber.TextFragments;

foreach (TextFragment fragment in textFragments)
{
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // تحديد نص طويل جداً
    field.AlternateName = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                            " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                            " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                            " Duis aute irure dolor in reprehenderit in voluptate velit" +
                            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                            " occaecat cupidatat non proident, sunt in culpa qui officia" +
                            " deserunt mollit anim id est laborum.";
    document.Form.Add(field);
}

// حفظ المستند
document.Save(outputFile);
```
{{% alert color="primary" %}}

فيما يتعلق بطول التلميح، يحتوي نص التلميح في المستند PDF كنوع سلسلة PDF، خارج تيار المحتوى. لا توجد قيود فعالة على مثل هذه السلاسل في ملفات PDF (انظر ملحق مرجع PDF C.). ومع ذلك، فإن قارئ مطابق (مثل Adobe Acrobat) يعمل على معالج معين وفي بيئة تشغيل معينة لديه مثل هذا الحد. يرجى الرجوع إلى وثائق تطبيق قارئ PDF الخاص بك.

{{% /alert %}}

## إنشاء كتلة نص مخفية وعرضها عند تمرير الماوس

في Aspose.PDF، يتم تنفيذ ميزة لإخفاء الإجراءات بحيث يمكن إظهار/إخفاء حقل مربع النص (أو أي نوع آخر من التعليقات التوضيحية) عند دخول/خروج الماوس فوق زر غير مرئي. لهذا الغرض، يتم استخدام فئة Aspose.Pdf.Annotations.HideAction لتعيين إجراء الإخفاء/العرض لكتلة النص. يرجى استخدام الشظية البرمجية التالية لإظهار/إخفاء كتلة نص عند دخول/خروج الماوس.

يرجى أيضًا أخذ في الاعتبار أن إجراءات PDF في المستندات تعمل بشكل جيد في القراء المطابقين (مثل
يرجى أيضًا مراعاة أن إجراءات PDF في المستندات تعمل بشكل جيد في قارئات المتوافقة (على سبيل المثال

- تعمل جميع تنفيذات إجراء الإخفاء في مستندات PDF بشكل جيد في Internet Explorer الإصدار 11.0.
- تعمل جميع تنفيذات إجراء الإخفاء أيضًا في Opera الإصدار 12.14، ولكننا نلاحظ بعض التأخير في الاستجابة عند الفتح الأول للمستند.
- يعمل التنفيذ الوحيد باستخدام مُنشئ HideAction الذي يقبل اسم الحقل إذا كان Google Chrome الإصدار 61.0 يتصفح المستند؛ يرجى استخدام المُنشئين المناسبين إذا كان التصفح في Google Chrome مهمًا:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string outputFile = dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

// إنشاء مستند عينة بنص
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("حرك مؤشر الماوس هنا لعرض النص المتحرك"));
doc.Save(outputFile);

// فتح مستند بنص
Document document = new Document(outputFile);
// إنشاء كائن TextAbsorber للعثور على جميع العبارات التي تطابق التعبير العادي
TextFragmentAbsorber absorber = new TextFragmentAbsorber("حرك مؤشر الماوس هنا لعرض النص المتحرك");
// قبول الامتصاص لصفحات المستند
document.Pages.Accept(absorber);
// الحصول على أول نص مستخلص
TextFragmentCollection textFragments = absorber.TextFragments;
TextFragment fragment = textFragments[1];

// إنشاء حقل نصي مخفي للنص المتحرك في المستطيل المحدد من الصفحة
TextBoxField floatingField = new TextBoxField(fragment.Page, new Rectangle(100, 700, 220, 740));
// تعيين النص ليظهر كقيمة الحقل
floatingField.Value = "هذا هو \"حقل النص المتحرك\".";
// نوصي بجعل الحقل 'للقراءة فقط' لهذا السيناريو
floatingField.ReadOnly = true;
// تعيين علم 'مخفي' لجعل الحقل غير مرئي عند فتح المستند
floatingField.Flags |= AnnotationFlags.Hidden;

// تعيين اسم حقل فريد ليس ضروريًا ولكن مسموح به
floatingField.PartialName = "FloatingField_1";

// تعيين خصائص مظهر الحقل ليس ضروريًا ولكن يجعله أفضل
floatingField.DefaultAppearance = new DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
floatingField.Border = new Border(floatingField);
floatingField.Border.Width = 1;
floatingField.Multiline = true;

// إضافة حقل النص إلى المستند
document.Form.Add(floatingField);

// إنشاء زر غير مرئي على موضع قطعة النص
ButtonField buttonField = new ButtonField(fragment.Page, fragment.Rectangle);
// إنشاء إجراء إخفاء جديد للحقل المحدد (التعليق التوضيحي) وعلم الإخفاء.
// (يمكنك أيضاً الإشارة إلى الحقل المتحرك باسم إذا قمت بتحديده أعلاه.)
// إضافة إجراءات عند دخول/خروج الماوس في حقل الزر غير المرئي
buttonField.Actions.OnEnter = new HideAction(floatingField, false);
buttonField.Actions.OnExit = new HideAction(floatingField);

// إضافة حقل الزر إلى المستند
document.Form.Add(buttonField);

// حفظ المستند
document.Save(outputFile);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "مكتبة Aspose.PDF لـ .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "GB",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "AU",
                "availableLanguage": "الإنجليزية"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة التلاعب بملفات PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

