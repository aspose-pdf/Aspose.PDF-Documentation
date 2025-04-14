---
title: العمل مع الرسوميات المتجهة
linktitle: العمل مع الرسوميات المتجهة
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /ar/net/working-with-vector-graphics/
description: تصف هذه المقالة ميزات العمل مع أداة GraphicsAbsorber باستخدام C#.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Vector Graphics",
    "alternativeHeadline": "Enhance PDF Graphics Manipulation with С№",
    "abstract": "اكتشف القدرات المتقدمة لأداة GraphicsAbsorber في Aspose.PDF for .NET، مما يسمح للمطورين بالتلاعب بسلاسة بالرسوميات المتجهة في مستندات PDF. تتيح هذه الميزة استخراجًا دقيقًا، وتحريكًا، وإزالة الرسوميات، بالإضافة إلى القدرة على إضافتها إلى صفحات مختلفة، مما يعزز سير عمل معالجة PDF لديك مع مزيد من المرونة والتحكم.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "889",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2024-11-26",
    "description": "تصف هذه القسم ميزات العمل مع ملف PDF باستخدام مكتبة GraphicsAbsorber C#."
}
</script>

في هذا الفصل، سنستكشف كيفية استخدام فئة `GraphicsAbsorber` القوية للتفاعل مع الرسوميات المتجهة داخل مستندات PDF. سواء كنت بحاجة إلى تحريك، إزالة، أو إضافة الرسوميات، ستظهر لك هذه الدليل كيفية تنفيذ هذه المهام بفعالية.

## المقدمة<a name="introduction"></a>

تعتبر الرسوميات المتجهة مكونًا حيويًا في العديد من مستندات PDF، تُستخدم لتمثيل الصور، الأشكال، وعناصر رسومية أخرى. توفر Aspose.PDF فئة `GraphicsAbsorber`، التي تتيح للمطورين الوصول إلى هذه الرسوميات والتلاعب بها برمجيًا. من خلال استخدام طريقة `Visit` الخاصة بـ `GraphicsAbsorber`، يمكنك استخراج الرسوميات المتجهة من صفحة محددة وأداء عمليات متنوعة، مثل التحريك، الإزالة، أو النسخ إلى صفحات أخرى.

## استخراج الرسوميات باستخدام `GraphicsAbsorber`<a name="extracting-graphics"></a>

الخطوة الأولى في العمل مع الرسوميات المتجهة هي استخراجها من مستند PDF. إليك كيفية القيام بذلك باستخدام فئة `GraphicsAbsorber`:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UsingGraphicsAbsorber()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Display information about the extracted elements
            foreach (var element in graphicsAbsorber.Elements)
            {
                Console.WriteLine($"Page Number: {element.SourcePage.Number}");
                Console.WriteLine($"Position: ({element.Position.X}, {element.Position.Y})");
                Console.WriteLine($"Number of Operators: {element.Operators.Count}");
            }
        }
    }
}
```

1. **إنشاء كائن مستند**: يتم إنشاء كائن `Document` جديد مع مسار ملف PDF المستهدف.
2. **إنشاء مثيل من `GraphicsAbsorber`**: تلتقط هذه الفئة جميع عناصر الرسوميات من صفحة محددة.
3. **طريقة الزيارة**: يتم استدعاء طريقة `Visit` على الصفحة الأولى، مما يسمح لـ `GraphicsAbsorber` بامتصاص الرسوميات المتجهة.
4. **التكرار عبر العناصر المستخرجة**: يقوم الكود بالتكرار عبر كل عنصر مستخرج، مطبوعًا معلومات مثل رقم الصفحة، الموقع، وعدد مشغلات الرسم المعنية.

## تحريك الرسوميات<a name="moving-graphics"></a>

بمجرد أن تقوم باستخراج الرسوميات، يمكنك تحريكها إلى موقع مختلف على نفس الصفحة. إليك كيفية تحقيق ذلك:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveGraphics()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create a GraphicsAbsorber instance 
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Temporarily suspend updates to improve performance
            graphicsAbsorber.SuppressUpdate();

            // Loop through each extracted graphic element and shift its position
            foreach (var element in graphicsAbsorber.Elements)
            {
                var position = element.Position;
                // Move graphics by shifting its X and Y coordinates
                element.Position = new Aspose.Pdf.Point(position.X + 150, position.Y - 10);
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

- **SuppressUpdate**: تقوم هذه الطريقة بتعليق التحديثات مؤقتًا لتحسين الأداء عند إجراء تغييرات متعددة.
- **ResumeUpdate**: تستأنف هذه الطريقة التحديثات وتطبق التغييرات التي تم إجراؤها على مواقع الرسوميات.
- **تحديد موقع العنصر**: يتم تعديل موقع كل رسم عن طريق تغيير إحداثياته `X` و `Y`.

## إزالة الرسوميات<a name="removing-graphics"></a>

هناك سيناريوهات قد ترغب فيها في إزالة رسوميات معينة من صفحة. تقدم Aspose.PDF طريقتين لتحقيق ذلك:

### الطريقة 1: باستخدام حدود المستطيل

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod1()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Define the rectangle where graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Temporarily suspend updates for better performance
            graphicsAbsorber.SuppressUpdate();

            // Iterate through the extracted graphic elements and remove elements inside the rectangle
            foreach (var element in graphicsAbsorber.Elements)
            {
                // Check if the graphic's position falls within the rectangle
                if (rectangle.Contains(element.Position))
                {
                    // Remove the graphic element
                    element.Remove();
                }
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

### الطريقة 2: باستخدام مجموعة من العناصر المزالة

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod2()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Define the rectangle where graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Create a collection for the removed elements
            var removedElementsCollection = new Aspose.Pdf.Vector.GraphicElementCollection();

            // Add elements within the rectangle to the collection
            foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
            {
                removedElementsCollection.Add(item);
            }

            // Temporarily suppress updates for better performance
            page.Contents.SuppressUpdate();

            // Delete the selected graphic elements
            page.DeleteGraphics(removedElementsCollection);

            // Resume updates and apply changes
            page.Contents.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

- **حدود المستطيل**: حدد منطقة مستطيلة لتحديد الرسوميات التي يجب إزالتها.
- **تعطيل واستئناف التحديثات**: تأكد من إزالة فعالة دون عرض وسيط.

## إضافة الرسوميات إلى صفحة أخرى<a name="adding-graphics"></a>

يمكن إضافة الرسوميات الممتصة من صفحة واحدة إلى صفحة أخرى داخل نفس المستند. إليك طريقتين لتحقيق ذلك:

### الطريقة 1: إضافة الرسوميات بشكل فردي

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod1()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first and second pages
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphic elements from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add each graphic element from the first page to the second page
            foreach (var element in graphicsAbsorber.Elements)
            {
                element.AddOnPage(page2); // Add each graphic element to the second page.
            }

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

### الطريقة 2: إضافة الرسوميات كمجموعة

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod2()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first and second pages
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphic elements from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add all graphics at once from the first page to the second page
            page2.AddGraphics(graphicsAbsorber.Elements);

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

- **SuppressUpdate و ResumeUpdate**: تساعد هذه الطرق في الحفاظ على الأداء أثناء إجراء تغييرات جماعية.
- **AddOnPage مقابل AddGraphics**: استخدم `AddOnPage` للإضافات الفردية و `AddGraphics` للإضافات الجماعية.

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