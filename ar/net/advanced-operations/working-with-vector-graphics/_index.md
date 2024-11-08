---
title: العمل مع الرسومات المتجهة
linktitle: العمل مع الرسومات المتجهة
type: docs
weight: 120
url: /ar/net/working-with-vector-graphics/
description: هذه المقالة تصف ميزات العمل مع أداة GraphicsAbsorber باستخدام C#.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع GraphicsAbsorber",
    "alternativeHeadline": "كيفية الحصول على موقع صورة في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, GraphicsAbsorber في pdf",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2022-02-04",
    "description": "هذا القسم يصف ميزات العمل مع ملف PDF GraphicsAbsorber باستخدام مكتبة C#."
}
</script>

في هذا الفصل، سنستكشف كيفية استخدام فئة `GraphicsAbsorber` القوية للتفاعل مع الرسومات المتجهة ضمن مستندات PDF. سواء كنت بحاجة إلى نقل، إزالة، أو إضافة رسومات، سيوضح لك هذا الدليل كيفية أداء هذه المهام بفعالية. لنبدأ!

## مقدمة<a name="introduction"></a>

الرسومات المتجهة هي مكون حيوي في العديد من مستندات PDF، تُستخدم لتمثيل الصور، الأشكال، وعناصر رسومية أخرى. يوفر Aspose.PDF فئة `GraphicsAbsorber`، التي تسمح للمطورين بالوصول إلى هذه الرسومات والتعامل معها برمجيًا. من خلال استخدام طريقة `Visit` الخاصة بـ `GraphicsAbsorber`، يمكنك استخراج الرسومات المتجهة من صفحة محددة وأداء عمليات مختلفة، مثل النقل، الإزالة، أو النسخ إلى صفحات أخرى.

## 1. استخراج الرسومات بواسطة `GraphicsAbsorber`<a name="extracting-graphics"></a>

الخطوة الأولى في العمل مع الرسومات المتجهة هي استخراجها من مستند PDF. إليك كيف يمكنك القيام بذلك باستخدام فئة `GraphicsAbsorber`:

```csharp
public static void UsingGraphicsAbsorber()
{
    // الخطوة 1: إنشاء كائن Document.
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");

    // الخطوة 2: إنشاء نموذج من GraphicsAbsorber.
    var graphicsAbsorber = new GraphicsAbsorber();

    // حدد الصفحة الأولى من المستند.
    var page = document.Pages[1];

    // الخطوة 3: استخدم طريقة `Visit` لاستخراج الرسومات من الصفحة.
    graphicsAbsorber.Visit(page);

    // عرض معلومات عن العناصر المستخرجة.
    foreach (var element in graphicsAbsorber.Elements)
    {
        Console.WriteLine($"رقم الصفحة: {element.SourcePage.Number}");
        Console.WriteLine($"الموقع: ({element.Position.X}, {element.Position.Y})");
        Console.WriteLine($"عدد المشغلين: {element.Operators.Count}");
    }
}
```
### شرح:

1. **إنشاء كائن مستند**: يتم تكوين كائن `Document` جديد مع مسار ملف PDF الهدف.
2. **إنشاء نموذج لـ `GraphicsAbsorber`**: تلتقط هذه الفئة جميع عناصر الرسومات من صفحة محددة.
3. **طريقة الزيارة**: يتم استدعاء طريقة `Visit` على الصفحة الأولى، مما يسمح لـ `GraphicsAbsorber` بامتصاص الرسومات المتجهة.
4. **التكرار خلال العناصر المستخرجة**: يقوم الكود بالتكرار عبر كل عنصر مستخرج، طباعة معلومات مثل رقم الصفحة، الموقع، وعدد عمليات الرسم المتورطة.

## 2. نقل الرسومات<a name="moving-graphics"></a>

بمجرد استخراج الرسومات، يمكنك نقلها إلى موقع مختلف على نفس الصفحة. إليك كيف يمكنك تحقيق ذلك:

```csharp
public static void MoveGraphics()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);

    // تعليق التحديثات مؤقتًا لتحسين الأداء.
    graphicsAbsorber.SuppressUpdate();

    foreach (var element in graphicsAbsorber.Elements)
    {
        var position = element.Position;
        // نقل الرسومات بتحريك إحداثيات X و Y.
        element.Position = new Point(position.X + 150, position.Y - 10);
    }

    // استئناف التحديثات وتطبيق التغييرات.
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### النقاط الرئيسية:

- **SuppressUpdate**: هذه الطريقة تعلق التحديثات مؤقتاً لتحسين الأداء عند إجراء تغييرات متعددة.
- **ResumeUpdate**: هذه الطريقة تستأنف التحديثات وتطبق التغييرات المدخلة على مواقع الرسومات.
- **تحديد موقع العنصر**: يتم ضبط موقع كل رسم بتغيير إحداثيات `X` و `Y`.

## 3. إزالة الرسومات<a name="removing-graphics"></a>

هناك سيناريوهات قد ترغب فيها بإزالة رسومات معينة من صفحة. توفر Aspose.PDF طريقتين لتحقيق ذلك:

### الطريقة 1: باستخدام حدود المستطيل

```csharp
public static void RemoveGraphicsMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        // تحقق مما إذا كان موقع الرسم ضمن المستطيل.
        if (rectangle.Contains(element.Position))
        {
            element.Remove(); // إزالة عنصر الرسم.
        }
    }
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### الطريقة 2: استخدام مجموعة من العناصر المحذوفة

```csharp
public static void RemoveGraphicsMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.Visit(page);
    var removedElementsCollection = new GraphicElementCollection();
    foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
    {
        removedElementsCollection.Add(item);
    }

    page.Contents.SuppressUpdate();
    page.DeleteGraphics(removedElementsCollection);
    page.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### الشرح:

- **حدود المستطيل**: تحديد منطقة مستطيلة لتحديد الرسومات التي سيتم إزالتها.
- **تعليق واستئناف التحديثات**: ضمان إزالة فعالة دون تقديم متوسط.

## 4. إضافة الرسومات إلى صفحة أخرى<a name="adding-graphics"></a>

يمكن إضافة الرسومات الممتصة من صفحة واحدة إلى صفحة أخرى ضمن نفس المستند.
يمكن إضافة الرسومات المستخرجة من صفحة إلى صفحة أخرى ضمن نفس الوثيقة.

### الطريقة الأولى: إضافة الرسومات بشكل فردي

```csharp
public static void AddToAnotherPageMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        element.AddOnPage(page2); // إضافة كل عنصر رسومي إلى الصفحة الثانية.
    }
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### الطريقة الثانية: إضافة الرسومات كمجموعة

```csharp
public static void AddToAnotherPageMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    page2.AddGraphics(graphicsAbsorber.Elements); // إضافة جميع الرسومات دفعة واحدة.
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### النقاط الرئيسية:

- **SuppressUpdate و ResumeUpdate**: تساعد هذه الأساليب في الحفاظ على الأداء أثناء إجراء تغييرات جماعية.
- **AddOnPage مقابل AddGraphics**: استخدم `AddOnPage` للإضافات الفردية و `AddGraphics` للإضافات الجماعية.

## الخاتمة

في هذا الفصل، استكشفنا كيفية استخدام فئة `GraphicsAbsorber` لاستخراج وتحريك وإزالة وإضافة الرسومات البيانية الفيكتورية ضمن مستندات PDF باستخدام Aspose.PDF. من خلال إتقان هذه التقنيات، يمكنك تعزيز العرض البصري لملفات PDF الخاصة بك وإنشاء مستندات ديناميكية وجذابة بصرياً.

لا تتردد في تجربة أمثلة الكود وتكييفها مع حالات استخدامك المحددة. عمل مبرمج سعيد!

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

