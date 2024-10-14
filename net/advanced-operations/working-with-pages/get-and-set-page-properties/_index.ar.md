---
title: الحصول وتعيين خصائص الصفحة
type: docs
url: /net/get-and-set-page-properties/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "الحصول وتعيين خصائص الصفحة",
    "alternativeHeadline": "الحصول وتعيين خصائص صفحات PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "pdf, c#, الحصول على خصائص الصفحة, تعيين خصائص الصفحة",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
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
                "contactType": "مبيعات",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
Aspose.PDF لـ .NET يتيح لك قراءة وتعيين خصائص الصفحات في ملف PDF في تطبيقات .NET الخاصة بك. هذا القسم يوضح كيفية الحصول على عدد الصفحات في ملف PDF، والحصول على معلومات حول خصائص صفحة PDF مثل اللون وتعيين خصائص الصفحة. الأمثلة المعطاة بلغة C# ولكن يمكنك استخدام أي لغة .NET مثل VB.NET لتحقيق نفس الشيء.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## الحصول على عدد الصفحات في ملف PDF

عند العمل مع الوثائق، غالبًا ما ترغب في معرفة عدد الصفحات التي تحتويها. مع Aspose.PDF هذا لا يستغرق أكثر من سطرين من الكود.

للحصول على عدد الصفحات في ملف PDF:

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. ثم استخدم خاصية Count (من كائن Document) لمجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) للحصول على العدد الإجمالي للصفحات في المستند.

الشفرة التالية تظهر كيفية الحصول على عدد الصفحات لملف PDF.
### الحصول على عدد الصفحات دون حفظ المستند

في بعض الأحيان، نولد ملفات PDF بشكل مباشر وأثناء إنشاء ملف PDF، قد نواجه الحاجة (مثل إنشاء جدول المحتويات إلخ) للحصول على عدد صفحات ملف PDF دون حفظ الملف على النظام أو التيار. لذا، لتلبية هذا الطلب، تم تقديم طريقة [ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs) في فئة الوثيقة. يرجى الاطلاع على الجزء التالي من الكود الذي يوضح خطوات الحصول على عدد الصفحات دون حفظ المستند.

## الحصول على خصائص الصفحة

كل صفحة في ملف PDF لها عدد من الخصائص، مثل العرض، الارتفاع، وصندوق القص والتقليم.
كل صفحة في ملف PDF لها عدد من الخصائص، مثل العرض والارتفاع والبليد والكروب والتريمبوكس.

### **فهم خصائص الصفحة: الفرق بين أرتبوكس، بليدبوكس، كروببوكس، ميديابوكس، تريمبوكس وخاصية الريكت**

- **ميديا بوكس**: الميديا بوكس هو أكبر صندوق في الصفحة. يتوافق مع حجم الصفحة (على سبيل المثال A4، A5، الرسالة الأمريكية، إلخ) المختار عند طباعة المستند إلى بوستسكريبت أو PDF. بمعنى آخر، الميديا بوكس يحدد الحجم الفيزيائي للوسائط التي يتم عرض مستند PDF عليها أو طباعتها.
- **بليد بوكس**: إذا كان المستند يحتوي على بليد، فسيكون لدى الـPDF أيضًا بليد بوكس. البليد هو مقدار اللون (أو العمل الفني) الذي يمتد إلى ما وراء حافة الصفحة. يستخدم للتأكد من أنه عندما يتم طباعة المستند وقصه إلى الحجم ("تقليمه")، ستذهب الحبر إلى حافة الصفحة. حتى لو تم قص الصفحة بشكل خاطئ - قص قليلاً عن علامات القص - لن تظهر أي حواف بيضاء على الصفحة.
- **تريم بوكس**: يشير التريم بوكس إلى الحجم النهائي للمستند بعد الطباعة والقص.
- **صندوق القص**: يشير صندوق القص إلى الحجم النهائي للمستند بعد الطباعة والقص.
- **صندوق الفن**: صندوق الفن هو الصندوق المرسوم حول محتويات الصفحات الفعلية في مستنداتك. يُستخدم هذا الصندوق للصفحات عند استيراد مستندات PDF في تطبيقات أخرى.
- **صندوق القص**: صندوق القص هو "حجم الصفحة" الذي يتم عرض مستند PDF الخاص بك به في Adobe Acrobat. في العرض العادي، يتم عرض محتويات صندوق القص فقط في Adobe Acrobat.
  للحصول على وصف مفصل لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، وخاصة 10.10.1 حدود الصفحة.
- **Page.Rect**: تقاطع (المستطيل المرئي المشترك) لـ MediaBox و DropBox. الصورة أدناه توضح هذه الخصائص.

لمزيد من التفاصيل، يرجى زيارة [هذه الصفحة](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **الوصول إلى خصائص الصفحة**

توفر فئة [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) جميع الخصائص المتعلقة بصفحة PDF معينة.
توفر فئة [الصفحة](https://reference.aspose.com/pdf/net/aspose.pdf/page) جميع الخصائص المتعلقة بصفحة PDF معينة.

من هناك، يمكن الوصول إلى كائنات الصفحة الفردية باستخدام الفهرس الخاص بها، أو تكرار تجميع الصفحات باستخدام حلقة foreach، للحصول على جميع الصفحات. بمجرد الوصول إلى صفحة فردية، يمكننا الحصول على خصائصها. يوضح الشفرة التالية كيفية الحصول على خصائص الصفحة.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetProperties-GetProperties.cs" >}}

## الحصول على صفحة معينة من ملف PDF

يتيح لك Aspose.PDF [تقسيم ملف PDF إلى صفحات فردية](/pdf/net/split-pdf-document/) وحفظها كملفات PDF. الحصول على صفحة محددة في ملف PDF وحفظها كملف PDF جديد هو عملية مشابهة جدًا: افتح المستند المصدر، وصول إلى الصفحة، إنشاء مستند جديد وإضافة الصفحة إليه.

يحتفظ كائن [المستند](https://reference.aspose.com/pdf/net/aspose.pdf/document) بالصفحات في ملف PDF من خلال [مجموعة الصفحات](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
الكائن [الوثيقة](https://reference.aspose.com/pdf/net/aspose.pdf/document) يحتوي على [مجموعة الصفحات](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) التي تضم الصفحات في ملف PDF.

1. حدد مؤشر الصفحة باستخدام خاصية الصفحات.
1. أنشئ كائن [وثيقة](https://reference.aspose.com/pdf/net/aspose.pdf/document) جديد.
1. أضف كائن [الصفحة](https://reference.aspose.com/pdf/net/aspose.pdf/page) إلى كائن [الوثيقة](https://reference.aspose.com/pdf/net/aspose.pdf/document) الجديد.
1. احفظ الناتج باستخدام طريقة [الحفظ](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

يوضح جزء الكود التالي كيفية الحصول على صفحة معينة من ملف PDF وحفظها كملف جديد.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetParticularPage-GetParticularPage.cs" >}}

## تحديد لون الصفحة

توفر فئة [الصفحة](https://reference.aspose.com/pdf/net/aspose.pdf/page) الخصائص المتعلقة بصفحة معينة في مستند PDF، بما في ذلك نوع اللون - RGB، أبيض وأسود، درجات الرمادي أو غير محدد - الذي تستخدمه الصفحة.
الفصل [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) يوفر خصائص تتعلق بصفحة معينة في مستند PDF، بما في ذلك نوع اللون - RGB، أبيض وأسود، مقياس الرمادي أو غير محدد - الذي تستخدمه الصفحة.

جميع صفحات ملفات PDF محتواة بواسطة مجموعة [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection). خاصية ColorType تحدد لون العناصر على الصفحة. للحصول على معلومات اللون لصفحة PDF معينة، استخدم خاصية [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) لكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

يوضح الجزء التالي من الكود كيفية التكرار عبر كل صفحة من ملف PDF للحصول على معلومات اللون.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-DeterminePageColor-DeterminePageColor.cs" >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
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

