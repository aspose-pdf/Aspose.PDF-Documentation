---
title: مقارنة مستندات PDF
linktitle: مقارنة PDF
type: docs
weight: 180
url: /net/compare-pdf-documents/
description: منذ إصدار 24.7 أصبح من الممكن مقارنة محتوى مستندات PDF مع علامات التعليقات والعرض جنبًا إلى جنب
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## مقارنة مستندات PDF باستخدام Aspose.PDF لـ .NET

عند العمل مع مستندات PDF، قد تحتاج أحيانًا إلى مقارنة محتوى مستندين لتحديد الاختلافات. توفر مكتبة Aspose.PDF لـ .NET مجموعة أدوات قوية لهذا الغرض. في هذا المقال، سنستكشف كيفية مقارنة مستندات PDF باستخدام بعض الأمثلة البسيطة للأكواد.

تتيح وظيفة المقارنة في Aspose.PDF مقارنة مستندين PDF صفحة بصفحة. يمكنك اختيار مقارنة صفحات معينة أو المستندات بأكملها. يبرز المستند الناتج عن المقارنة الاختلافات، مما يسهل تحديد التغييرات بين الملفين.

### مقارنة صفحات محددة

يوضح الجزء الأول من الكود كيفية مقارنة الصفحات الأولى من مستندين PDF.

خطوات:

1. تهيئة المستند.
يبدأ الكود بتهيئة مستندي PDF باستخدام مساري الملفات الخاصين بهما (documentPath1 و documentPath2). يتم تحديد المسارات كسلاسل نصية فارغة في الوقت الحالي، ولكن في الواقع، يجب استبدال هذه بمسارات الملفات الفعلية.
2. عملية المقارنة.
- اختيار الصفحة - تقتصر المقارنة على الصفحة الأولى من كل مستند ('Pages[1]').
- خيارات المقارنة:

'AdditionalChangeMarks = true'- تضمن هذه الخيار عرض علامات تغيير إضافية. تسلط هذه العلامات الضوء على الاختلافات التي قد تكون موجودة في صفحات أخرى، حتى لو لم تكن على الصفحة الحالية المقارنة.

'ComparisonMode = ComparisonMode.IgnoreSpaces' - يخبر هذا الوضع المقارن بتجاهل المسافات في النص، مركزًا فقط على التغييرات داخل الكلمات.
```
```cs
    string documentPath1 = "";
    string documentPath2= "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

### مقارنة الوثائق بأكملها

الشفرة الثانية توسع نطاق المقارنة لتشمل محتوى وثيقتي PDF بالكامل.

خطوات:

1. تهيئة الوثيقة.
كما في المثال الأول، يتم تهيئة وثيقتي PDF بمسارات ملفاتهما.
2. عملية المقارنة.
- مقارنة الوثيقة بأكملها - على عكس الشفرة الأولى، هذه الشفرة تقارن محتوى الوثيقتين بالكامل.
- خيارات المقارنة - الخيارات هي نفسها كما في الشفرة الأولى، مع التأكد من تجاهل الفراغات وعرض علامات التغيير الإضافية.

3.
```cs
    string documentPath1 = "";
    string documentPath2 = "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1, document2, resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

نتائج المقارنة التي يتم توليدها بواسطة هذه الأجزاء هي مستندات PDF يمكنك فتحها في معاين مثل Adobe Acrobat. إذا استخدمت عرض الصفحتين في Adobe Acrobat، سترى التغييرات جنبًا إلى جنب:

- الحذف - يتم تسجيلها على الصفحة اليسرى.
- الإدراجات - يتم تسجيلها على الصفحة اليمنى.

من خلال تعيين 'AdditionalChangeMarks' إلى 'true'، يمكنك أيضًا رؤية علامات للتغييرات التي قد تحدث في صفحات أخرى، حتى لو لم تكن هذه التغييرات على الصفحة الحالية المعروضة.

**Aspose.PDF for .NET** توفر أدوات قوية لمقارنة مستندات PDF، سواء كنت بحاجة لمقارنة صفحات محددة أو مستندات كاملة.
**Aspose.PDF لـ .NET** يوفر أدوات قوية لمقارنة مستندات PDF، سواء كنت بحاجة لمقارنة صفحات محددة أو المستندات بأكملها.
