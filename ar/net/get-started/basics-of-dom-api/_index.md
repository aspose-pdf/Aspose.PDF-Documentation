---
title: أساسيات واجهة برمجة تطبيقات Aspose.PDF DOM
linktitle: أساسيات واجهة برمجة تطبيقات DOM
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /ar/net/basics-of-dom-api/
description: Aspose.PDF for .NET يستخدم أيضًا فكرة DOM لتمثيل هيكل مستند PDF من حيث الكائنات.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Basics of Aspose.PDF DOM API",
    "alternativeHeadline": "Enhanced PDF Manipulation with Aspose.PDF DOM API in C#",
    "abstract": "تقدم واجهة برمجة تطبيقات DOM الجديدة Aspose.PDF for .NET نهجًا قويًا قائمًا على الكائنات للتلاعب بمستندات PDF من خلال تمثيل هيكلها كشجرة هرمية. تتيح هذه الميزة للمطورين الوصول بسهولة إلى عناصر PDF وتحديثها وتصديرها مع تعزيز المرونة والتحكم في معالجة المستندات من خلال واجهة برمجة تطبيقات بديهية.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "891",
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
    "url": "/net/basics-of-dom-api/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/basics-of-dom-api/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## مقدمة في واجهة برمجة تطبيقات DOM

نموذج كائن المستند (DOM) هو شكل من أشكال تمثيل المستندات المنظمة كنموذج قائم على الكائنات. DOM هو المعيار الرسمي لمجموعة الويب العالمية (W3C) لتمثيل المستندات المنظمة بطريقة محايدة عن النظام الأساسي واللغة.

بعبارات بسيطة، DOM هو شجرة من الكائنات تمثل هيكل مستند ما. Aspose.PDF for .NET يستخدم أيضًا فكرة DOM لتمثيل هيكل مستند PDF من حيث الكائنات. ومع ذلك، يتم التلاعب بجوانب DOM (مثل عناصره) ضمن بناء جملة لغة البرمجة المستخدمة. يتم تحديد الواجهة العامة لـ DOM في واجهة برمجة التطبيقات (API) الخاصة به.

### مقدمة في مستند PDF

تنسيق المستندات المحمولة (PDF) هو معيار مفتوح لتبادل المستندات. مستند PDF هو مزيج من النص والبيانات الثنائية. إذا قمت بفتحه في محرر نصوص، سترى الكائنات الخام التي تحدد الهيكل ومحتويات المستند.

الهيكل المنطقي لملف PDF هرمي ويحدد التسلسل الذي ترسم به تطبيقات العرض صفحات المستند ومحتوياتها. يتكون PDF من أربعة مكونات: الكائنات، هيكل الملف، هيكل المستند وتدفقات المحتوى.

### هيكل مستند PDF

نظرًا لأن هيكل ملف PDF هرمي، فإن Aspose.PDF for .NET يصل أيضًا إلى العناصر بنفس الطريقة. تُظهر الهيكلية التالية كيف يتم هيكلة مستند PDF منطقيًا وكيف يقوم واجهة برمجة تطبيقات DOM لـ Aspose.PDF for .NET بإنشائه.

![هيكل مستند PDF](../images/structure.png)

### الوصول إلى عناصر مستند PDF

كائن المستند هو في المستوى الجذري لنموذج الكائنات. تتيح لك واجهة برمجة تطبيقات DOM لـ Aspose.PDF for .NET إنشاء كائن مستند ثم الوصول إلى جميع الكائنات الأخرى في الهيكل. يمكنك إما الوصول إلى أي من المجموعات مثل الصفحات أو عنصر فردي مثل الصفحة، إلخ. توفر واجهة برمجة التطبيقات نقاط دخول وخروج واحدة للتلاعب بمستند PDF كما هو موضح أدناه:

- فتح مستند PDF.
- الوصول إلى هيكل مستند PDF بأسلوب DOM.
- تحديث البيانات في مستند PDF.
- التحقق من صحة مستند PDF.
- تصدير مستند PDF إلى تنسيقات مختلفة.
- أخيرًا، حفظ مستند PDF المحدث.

## كيفية استخدام واجهة برمجة التطبيقات الجديدة Aspose.PDF for .NET

ستشرح هذه الموضوع واجهة برمجة التطبيقات الجديدة Aspose.PDF for .NET وتوجهك للبدء بسرعة وسهولة. يرجى ملاحظة أن التفاصيل المتعلقة باستخدام الميزات المحددة ليست جزءًا من هذه المقالة.

يتكون Aspose.PDF for .NET من جزئين:

- واجهة برمجة تطبيقات DOM لـ Aspose.PDF for .NET.
- Aspose.Pdf.Facades (Aspose.PDF.Kit القديمة لـ .NET).

ستجد تفاصيل كل من هذه المجالات أدناه.

### واجهة برمجة تطبيقات DOM لـ Aspose.PDF for .NET

تتوافق واجهة برمجة تطبيقات DOM لـ Aspose.PDF for .NET مع هيكل مستند PDF، مما يساعدك على العمل مع مستندات PDF ليس فقط على مستوى الملف والمستند، ولكن أيضًا على مستوى الكائن. لقد قدمنا مزيدًا من المرونة للمطورين للوصول إلى جميع العناصر والكائنات في مستند PDF. باستخدام فئات واجهة برمجة تطبيقات Aspose.PDF DOM، يمكنك الحصول على وصول برمجي إلى عناصر المستند والتنسيق. تتكون واجهة برمجة التطبيقات الجديدة هذه من مساحات أسماء مختلفة كما هو موضح أدناه:

### Aspose.PDF

توفر هذه المساحة اسم الفئة Document التي تتيح لك فتح وحفظ مستند PDF. كما أن فئة License هي أيضًا جزء من هذه المساحة. كما توفر فئات تتعلق بصفحات PDF، والمرفقات، والإشارات المرجعية مثل Page، PageCollection، FileSpecification، EmbeddedFileCollection، OutlineItemCollection، وOutlineCollection، إلخ.

#### Aspose.Text

توفر هذه المساحة اسم فئات تساعدك في العمل مع النص وجوانبه المختلفة، على سبيل المثال Font، FontCollection، FontRepository، FontStyles، TextAbsorber، TextFragment، TextFragmentAbsorber، TextFragmentCollection، TextFragmentState، TextSegment وTextSegmentCollection، إلخ.

#### Aspose.Text.TextOptions

توفر هذه المساحة اسم فئات تسمح لك بتعيين خيارات مختلفة للبحث، والتحرير أو استبدال النص، على سبيل المثال TextEditOptions، TextReplaceOptions وTextSearchOptions.

#### Aspose.InteractiveFeatures

تحتوي هذه المساحة اسم على فئات تساعدك في العمل مع الميزات التفاعلية لمستند PDF، على سبيل المثال العمل مع المستند وإجراءات أخرى. تحتوي هذه المساحة اسم على فئات مثل GoToAction، GoToRemoteAction وGoToURIAction، إلخ.

#### Aspose.InteractiveFeatures.Annotations

التعليقات التوضيحية هي جزء من الميزات التفاعلية لمستند PDF. لقد خصصنا مساحة اسم للتعليقات التوضيحية. تحتوي هذه المساحة اسم على فئات تساعدك في العمل مع التعليقات التوضيحية، على سبيل المثال، Annotation، AnnotationCollection، CircleAnnotation وLinkAnnotation، إلخ.

#### Aspose.InteractiveFeatures.Forms

تحتوي هذه المساحة اسم على فئات تساعدك في العمل مع نماذج PDF وحقول النموذج، على سبيل المثال Form، Field، TextBoxField وOptionCollection، إلخ.

#### Aspose.Pdf.Devices

يمكننا إجراء عمليات مختلفة على مستندات PDF مثل تحويل مستند PDF إلى تنسيقات صور مختلفة. ومع ذلك، لا تنتمي مثل هذه العمليات إلى كائن المستند ولا يمكننا توسيع فئة Document لمثل هذه العمليات. لهذا السبب قدمنا مفهوم الجهاز في واجهة برمجة التطبيقات الجديدة DOM.

#### Aspose.Pdf.Facades

قبل Aspose.PDF for .NET، كنت بحاجة إلى Aspose.PDF.Kit لـ .NET للتلاعب بملفات PDF الموجودة. لتنفيذ كود Aspose.PDF.Kit القديم، يمكنك استخدام مساحة اسم Aspose.PDF.Facades.