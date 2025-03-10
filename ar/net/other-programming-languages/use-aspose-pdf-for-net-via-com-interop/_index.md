---
title: Aspose.PDF for .NET عبر COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/use-aspose-pdf-for-net-via-com-interop/
description: اكتشف كيفية استخدام Aspose.PDF for .NET عبر COM Interop للتكامل السلس مع التطبيقات غير .NET.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose.PDF for .NET via COM Interop",
    "alternativeHeadline": "Aspose.PDF for .NET Enables COM Interop Usage",
    "abstract": "يدعم Aspose.PDF for .NET الآن التكامل السلس مع لغات البرمجة المختلفة من خلال COM Interop، مما يسمح للمطورين باستخدام قدراته القوية في معالجة PDF خارج إطار عمل .NET. تعزز هذه الميزة المرونة من خلال تحويل كائنات Aspose.PDF إلى كائنات COM، مما يسهل التفاعلات مع التعليمات البرمجية غير المُدارة مع الحفاظ على أداء عالٍ من خلال تقنيات الربط المبكر والمتأخر.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1338",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/use-aspose-pdf-for-net-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/use-aspose-pdf-for-net-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

تنطبق المعلومات في هذا الموضوع على السيناريوهات التي تريد فيها استخدام [Aspose.PDF for .NET](/pdf/ar/net/) عبر COM Interop في أي من لغات البرمجة التالية:

- ASP
- دلفي
- JScript
- Perl
- PHP
- PowerBuilder
- بايثون
- VBScript
- Visual Basic
- C++

{{% /alert %}}

## العمل مع COM Interop

يعمل Aspose.PDF for .NET تحت سيطرة إطار عمل .NET ويسمى هذا الكود المُدار. الكود المكتوب في جميع اللغات المذكورة أعلاه يعمل خارج إطار عمل .NET ويسمى هذا الكود غير المُدار. يحدث التفاعل بين الكود غير المُدار وAspose.PDF عبر المرفق .NET المعروف باسم COM Interop.

كائنات Aspose.PDF هي كائنات .NET، ولكن عند استخدامها عبر COM Interop، تظهر ككائنات COM في لغة البرمجة الخاصة بك. لذلك، من الأفضل التأكد من أنك تعرف كيفية إنشاء واستخدام كائنات COM في لغة البرمجة الخاصة بك، قبل أن تبدأ في استخدام [Aspose.PDF for .NET](/pdf/ar/net/).

{{% alert color="primary" %}}

- في عالم COM نميز بين خادم COM وعميل COM. يخزن خادم COM فئات COM بينما يطلب عميل COM من خادم COM الحصول على مثيلات الفئات، أي كائنات COM.
- يمكن أن يعرف عميل COM أو ببساطة تطبيق العميل عن محتويات فئة COM أو يكون غير مدرك تمامًا لطرقها وخصائصها. لذلك يمكن لتطبيق العميل اكتشاف بنية فئة COM عند التجميع/البناء أو فقط أثناء التنفيذ. تُعرف عملية "الاكتشاف" باسم الربط، لذا لدينا **الربط المبكر** و**الربط المتأخر**.
- باختصار، فئة COM تشبه الصندوق الأسود وللعمل معها تحتاج إلى مكتبة نوع، هذه الملف الثنائي يحتوي على وصف لطرق وخصائص فئة COM، وأي لغة عالية المستوى تدعم العمل مع كائنات COM غالبًا ما تحتوي على تعبير بناء جملة لإضافة مكتبة نوع، على سبيل المثال، هذا هو [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) في C++.
- تُستخدم مكتبة النوع للربط المبكر.
- يمكن لكائن COM أن يكشف عن طرقه وخصائصه بطريقتين: من خلال **واجهة التوزيع** (dispinterface) وفي **vtable** (جدول الوظائف الافتراضية).
- ضمن **واجهة التوزيع**، يتم تحديد كل طريقة وخصيصة بواسطة عضو فريد؛ هذا العضو هو معرف توزيع الوظيفة (أو **DispID**).
- **vtable** هو مجرد مجموعة من المؤشرات إلى الوظائف التي تدعمها واجهة فئة COM.
- الكائن الذي يكشف عن طرقه من خلال كلا الواجهتين يدعم **واجهة مزدوجة**.
- هناك مزايا لكل نوع من الربط. يوفر الربط المبكر أداءً متزايدًا والتحقق من بناء الجملة في وقت التجميع. يكون الربط المتأخر أكثر فائدة عندما تكتب عملاء تنوي أن تكون ***متوافقة مع الإصدارات المستقبلية*** من فئة COM الخاصة بك. مع الربط المتأخر، لا تكون المعلومات من مكتبة النوع "مربوطة بشكل صارم" في عميلك، لذا يمكنك أن تكون أكثر ثقة في أن عميلك يمكن أن يعمل مع الإصدارات المستقبلية من فئة COM دون تغييرات في الكود.
- آلية الربط المتأخر لها ميزة كبيرة: إذا قرر منشئ DLL COM إصدار نسخة جديدة، مع تخطيط واجهة وظيفة مختلف، فإن أي كود يستدعي تلك الطرق لن يتعطل ما لم تكن الطرق غير متاحة؛ حتى إذا كان **vtable** مختلفًا، فإن الربط المتأخر يدير اكتشاف DISPIDs الجديدة واستدعاء الطرق المناسبة.
{{% /alert %}}

إليك المواضيع التي ستحتاج في النهاية إلى إتقانها:
{{% alert color="primary" %}}

- استخدام كائنات COM في لغة البرمجة الخاصة بك. راجع وثائق لغة البرمجة الخاصة بك والمواضيع الخاصة باللغة في هذه الوثائق.

- العمل مع كائنات COM التي تكشف عنها COM Interop .NET. راجع [التفاعل مع الكود غير المُدار](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) و[كشف مكونات إطار عمل .NET إلى COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) في MSDN.

- نموذج كائن مستند Aspose.PDF. راجع [دليل مبرمج Aspose.PDF](http://www.aspose.com/docs/display/pdfnet/Programmers+Guide) و[مرجع API](http://www.aspose.com/docs/display/pdfnet/Aspose.PDF+for+.NET+API+Reference).

{{% /alert %}}

## تسجيل Aspose.PDF for .NET مع COM Interop

تحتاج إلى تثبيت Aspose.PDF for .NET والتأكد من أنه مسجل مع COM Interop (مما يضمن أنه يمكن استدعاؤه من الكود غير المُدار).

{{% alert color="primary" %}}

لتسجيل Aspose.PDF for .NET لـ COM Interop يدويًا:

1. من قائمة **ابدأ**، اختر **جميع البرامج**، ثم **مايكروسوفت فيجوال ستوديو**، **أدوات فيجوال ستوديو**، وأخيرًا **موجه أوامر فيجوال ستوديو**.
1. أدخل الأمر لتسجيل التجميع:
   1. .NET Framework 4.8.1
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /codebase
   1. .NET 6.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /codebase
   1. .NET 7.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /codebase
   1. .NET 8.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /codebase
   1. .NET Standard 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

انتبه إلى أن /codebase ضروري فقط إذا لم يكن Aspose.PDF.dll في GAC، استخدام هذا الخيار يجعل regasm يضع مسار التجميع في السجل.

{{% alert color="primary" %}}

regasm.exe هو أداة مضمنة في .NET Framework SDK. تقع جميع أدوات .NET Framework SDK في الدليل *\Microsoft .NET\Framevork\<FrameworkVersion>*، على سبيل المثال *C:\Windows\Microsoft .NET\Framework\v4.0.30319*. إذا كنت تستخدم Visual Studio .NET:
من قائمة **ابدأ**، اختر **البرامج**، ثم **Visual Studio 2022**، وأخيرًا **موجه أوامر المطور لـ VS 2022**.
يعمل على تشغيل موجه أوامر مع جميع متغيرات البيئة اللازمة مضبوطة.

{{% /alert %}}

### ProgIDs

ProgID تعني "معرف برمجي". إنه اسم فئة COM التي تستخدم لإنشاء كائن. تتكون ProgIDs من اسم المكتبة "Aspose.PDF" واسم الفئة.

### مكتبة النوع

{{% alert color="primary" %}}

إذا كانت لغة البرمجة الخاصة بك (على سبيل المثال Visual Basic أو Delphi) تسمح لك بالإشارة إلى مكتبة نوع COM، فقم بإضافة مرجع إلى Aspose.PDF.tlb لرؤية جميع فئات Aspose.PDF for .NET والطرق والخصائص والتعدادات في متصفح الكائنات الخاص بك.

لإنشاء ملف TLB:

- .NET Framework 4.8.1
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.tlb" /codebase
- .NET 6.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.tlb" /codebase
- .NET 7.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.tlb" /codebase
- .NET 8.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.tlb" /codebase
- .NET Standard 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## إنشاء كائنات COM

إن إنشاء كائن COM مشابه لإنشاء كائن .NET عادي:

```vb
'Instantiate Pdf instance by calling its empty constructor
Dim document
Set document = CreateObject("Aspose.Pdf.Document")

```

بمجرد إنشائه، يمكنك الوصول إلى طرق وخصائص الكائن، كما لو كان كائن COM:

```vb
'Add page to the document
document.Pages.Add()
```

بعض الطرق لها تحميلات زائدة وسيتم الكشف عنها بواسطة COM Interop مع إضافة لاحقة عددية لها، باستثناء الطريقة الأولى التي تبقى دون تغيير. على سبيل المثال، تصبح تحميلات طريقة Document.Save Document.Save وDocument.Save_2، وهكذا.

لمزيد من المعلومات، راجع المقالات الخاصة باللغة في هذه الوثائق.

## إنشاء تجميع غلاف

إذا كنت بحاجة إلى استخدام العديد من فئات Aspose.PDF for .NET والطرق والخصائص، فكر في إنشاء تجميع غلاف (باستخدام C# أو أي لغة برمجة .NET أخرى). تساعد تجميعات الغلاف في تجنب استخدام Aspose.PDF for .NET مباشرة من الكود غير المُدار.

نهج جيد هو تطوير تجميع .NET يشير إلى Aspose.PDF for .NET ويقوم بكل العمل معه، ويكشف فقط مجموعة محدودة من الفئات والطرق للكود غير المُدار. يجب أن يعمل تطبيقك بعد ذلك فقط مع مكتبة الغلاف الخاصة بك.

تقليل عدد الفئات والطرق التي تحتاج إلى استدعائها عبر COM Interop يبسط المشروع. غالبًا ما يتطلب استخدام فئات .NET عبر COM Interop مهارات متقدمة.