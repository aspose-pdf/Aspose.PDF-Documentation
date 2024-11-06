---
title: العمل مع جافاسكريبت
type: docs
url: ar/net/working-with-javascript/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع جافاسكريبت",
    "alternativeHeadline": "كيفية العمل مع جافاسكريبت في PDF",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, جافاسكريبت في pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق Aspose.PDF Doc",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "أسبوس",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
## إضافة جافا سكريبت (DOM)

### ما هو جافا سكريبت Acrobat؟

جافا سكريبت Acrobat هو لغة تعتمد على النواة الأساسية للإصدار 1.5 من جافا سكريبت ISO-16262، التي كانت تعرف سابقًا باسم ECMAScript، وهي لغة برمجة شيئية التوجه طورتها شركة Netscape Communications. تم إنشاء جافا سكريبت لتقليل معالجة صفحات الويب من الخادم إلى العميل في التطبيقات المستندة إلى الويب. ينفذ جافا سكريبت Acrobat امتدادات، على شكل كائنات جديدة وطرقها وخصائصها المصاحبة، للغة جافا سكريبت. تمكن هذه الكائنات الخاصة بـAcrobat المطور من إدارة أمان المستند، التواصل مع قاعدة بيانات، التعامل مع المرفقات الملفية، التلاعب بملف PDF بحيث يتصرف مثل نموذج تفاعلي، يمكن تمكينه عبر الويب، وما إلى ذلك. نظرًا لأن الكائنات الخاصة بـAcrobat تُضاف فوق جافا سكريبت الأساسية، لا يزال بإمكانك الوصول إلى فئاتها القياسية، بما في ذلك Math, String, Date, Array، و RegExp.

### جافا سكريبت Acrobat مقابل جافا سكريبت HTML (الويب)

تتمتع مستندات PDF بتنوع كبير حيث يمكن عرضها داخل برنامج Acrobat وكذلك متصفح الويب.
تتمتع مستندات PDF بتنوع كبير حيث يمكن عرضها سواء ضمن برنامج Acrobat أو في متصفح ويب.

- لا يمكن لـ JavaScript في Acrobat الوصول إلى الكائنات داخل صفحة HTML. وبالمثل، لا يمكن لـ JavaScript في HTML الوصول إلى الكائنات داخل ملف PDF.
- يمكن لـ JavaScript في HTML التلاعب بكائنات مثل النافذة. لا يمكن لـ JavaScript في Acrobat الوصول إلى هذا الكائن بالتحديد ولكن يمكنه التلاعب بكائنات محددة لـ PDF.

يمكنك إضافة JavaScript في مستوى الوثيقة والصفحة باستخدام [Aspose.PDF for .NET](/pdf/net/). لإضافة JavaScript:

### إضافة JavaScript إلى إجراء الوثيقة أو الصفحة

1. قم بإعلان وتوضيح كائن JavascriptAction مع جملة JavaScript المطلوبة كحجة للمنشئ.
1. قم بتعيين كائن JavascriptAction إلى الإجراء المطلوب لوثيقة PDF أو الصفحة.

المثال أدناه يطبق الـ OpenAction على وثيقة محددة.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddJavaScriptToPage-AddJavaScriptToPage.cs" >}}

### **إضافة/إزالة JavaScript في مستوى الوثيقة**
### **إضافة/إزالة JavaScript على مستوى المستند**

تمت إضافة خاصية جديدة باسم JavaScript في فئة المستند والتي تمتلك نوع تجميع JavaScript وتوفر الوصول إلى سيناريوهات JavaScript من خلال مفتاحها. تُستخدم هذه الخاصية لإضافة JavaScript على مستوى المستند. تحتوي تجميعة JavaScript على الخصائص والطرق التالية:

- string this(string key) – تحصل على JavaScript أو تعينها بواسطة اسمها
- IList Keys – توفر قائمة بالمفاتيح الموجودة في تجميعة JavaScript
- bool Remove(string key) – تزيل JavaScript بواسطة مفتاحها.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddRemoveJavascriptToDoc-AddRemoveJavascriptToDoc.cs" >}}

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


