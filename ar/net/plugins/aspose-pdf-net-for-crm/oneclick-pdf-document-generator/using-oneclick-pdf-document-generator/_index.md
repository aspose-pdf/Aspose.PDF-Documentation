---
title: استخدام مولد مستندات PDF OneClick
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/using-oneclick-pdf-document-generator/
description: تعلم كيفية استخدام Aspose.PDF مولد مستندات PDF OneClick في Microsoft Dynamics
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using OneClick PDF Document Generator",
    "alternativeHeadline": "Streamlined PDF Generation in Microsoft Dynamics",
    "abstract": "افتح إمكانية توليد مستندات سلسة في Microsoft Dynamics مع مولد مستندات PDF OneClick من Aspose.PDF. تتيح هذه الميزة المبتكرة للمستخدمين إنشاء قوالب PDF قابلة للتخصيص مباشرة داخل CRM، وتوليد المستندات بكفاءة بنقرة واحدة، ودمج أزرار OneClick بسهولة في النماذج للوصول المبسط. عزز قدرات إدارة البيانات لديك وحسن الإنتاجية مع هذه الأداة القوية",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
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
    "url": "/net/using-oneclick-pdf-document-generator/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-oneclick-pdf-document-generator/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إنشاء قالب وإضافته في CRM

- افتح Word وأنشئ قالبًا.
- أدخل حقول MailMerge للبيانات القادمة من CRM.

![إدراج حقول MailMerge](using-oneclick-pdf-document-generator_1.png)

- تأكد من أن اسم الحقل يتطابق تمامًا مع حقل CRM.
- القوالب محددة للاستخدام مع كيان فردي.

![قالب تجريبي](using-oneclick-pdf-document-generator_2.png)

- بمجرد إنشاء القالب، افتح كيان تكوين PDF OneClick في CRM وأنشئ سجلًا جديدًا.
- أعط اسم القالب، اختر الكيان الذي تم تعريف القالب له وأرفق المستند الذي تم إنشاؤه في المرفق.

![اختر القالب](using-oneclick-pdf-document-generator_3.png)

## توليد مستند من زر الشريط

- افتح السجل حيث تريد توليد المستند. (تأكد من أن القالب قد تم إرفاقه بالفعل في التكوين لذلك الكيان)
- انقر على زر PDF OneClick من الشريط.

![انقر على PDF OneClick](using-oneclick-pdf-document-generator_4.png)

- من النافذة المنبثقة: اختر القالب، اسم الملف والإجراء وانقر على توليد.
- تحقق من الملف الذي تم تنزيله أو الملاحظات، بناءً على الاختيار.

## تكوين أزرار OneClick واستخدامها

- لاستخدام زر OneClick مباشرة من النموذج، افتح تخصيص النموذج.
- أدخل WebResource حيث تريد إضافة أزرار OneClick.
- اختر OpenButtonPage في WebResource وأعطه اسمًا.
- قم بتكوين الأزرار في حقل البيانات في العينة التالية.

![خصائص WebResource](using-oneclick-pdf-document-generator_5.png)

- استخدم سطرًا منفصلًا لكل زر واستخدم الصيغة التالية:
  - الصيغة: اسم القالب |<الإجراء: تنزيل/ملاحظة>|اسم ملف الإخراج
  - المثال: تجريبي|تنزيل|ملفي الذي تم تنزيله
- احفظ وانشر التخصيص.
- الزر متاح على النموذج.

![الزر متاح على النموذج](using-oneclick-pdf-document-generator_6.png)