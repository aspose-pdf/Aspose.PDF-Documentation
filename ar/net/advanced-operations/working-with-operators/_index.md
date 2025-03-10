---
title: العمل مع المشغلين
linktitle: العمل مع المشغلين
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /ar/net/working-with-operators/
description: يشرح هذا الموضوع كيفية استخدام المشغلين مع Aspose.PDF. توفر فئات المشغلين ميزات رائعة لمعالجة PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-operators/
    - /net/operator/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Operators",
    "alternativeHeadline": "Empowered PDF Manipulation with Operators Integration",
    "abstract": "تعمل ميزة المشغلين في Aspose.PDF for .NET على تعزيز قدرات معالجة PDF من خلال السماح للمستخدمين باستخدام فئات مشغل معينة لمهام مثل إضافة الصور وإزالة الرسومات. تبسط هذه الوظيفة عملية تعريف العناصر الرسومية وحالاتها داخل PDF، مما يوفر للمطورين أدوات قوية لتحرير المستندات ومعالجتها بدقة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "operators, Aspose.PDF, PDF manipulation, GSave operator, ConcatenateMatrix operator, Do operator, GRestore operator, graphics state, remove graphics",
    "wordcount": "1233",
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
    "url": "/net/working-with-operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-operators/"
    },
    "dateModified": "2024-11-26",
    "description": "يشرح هذا الموضوع كيفية استخدام المشغلين مع Aspose.PDF. توفر فئات المشغلين ميزات رائعة لمعالجة PDF."
}
</script>

## مقدمة إلى مشغلات PDF واستخدامها

المشغل هو كلمة مفتاحية في PDF تحدد بعض الإجراءات التي يجب تنفيذها، مثل رسم شكل رسومي على الصفحة. يتم تمييز كلمة المشغل عن كائن مسمى من خلال غياب حرف السوليدوس الأولي (2Fh). تكون المشغلين ذات معنى فقط داخل تدفق المحتوى.

تدفق المحتوى هو كائن تدفق PDF تتكون بياناته من تعليمات تصف العناصر الرسومية التي يجب رسمها على الصفحة. يمكن العثور على مزيد من التفاصيل حول مشغلات PDF في [مواصفات PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### تفاصيل التنفيذ

يشرح هذا الموضوع كيفية استخدام المشغلين مع Aspose.PDF. يضيف المثال المختار صورة إلى ملف PDF لتوضيح المفهوم. لإضافة صورة في ملف PDF، هناك حاجة إلى مشغلين مختلفين. يستخدم هذا المثال [GSave](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/28)، [ConcatenateMatrix](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/10)، [Do](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/14)، و [GRestore](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/26).

- يقوم مشغل **GSave** بحفظ الحالة الرسومية الحالية لـ PDF.
- يستخدم مشغل **ConcatenateMatrix** (دمج المصفوفة) لتحديد كيفية وضع الصورة على صفحة PDF.
- يقوم مشغل **Do** برسم الصورة على الصفحة.
- يقوم مشغل **GRestore** باستعادة الحالة الرسومية.

لإضافة صورة إلى ملف PDF:

1. أنشئ كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) وافتح مستند PDF المدخل.
1. احصل على الصفحة المحددة التي ستتم إضافة الصورة إليها.
1. أضف الصورة إلى مجموعة موارد الصفحة.
1. استخدم المشغلين لوضع الصورة على الصفحة:
   - أولاً، استخدم مشغل GSave لحفظ الحالة الرسومية الحالية.
   - ثم استخدم مشغل ConcatenateMatrix لتحديد مكان وضع الصورة.
   - استخدم مشغل Do لرسم الصورة على الصفحة.
1. أخيرًا، استخدم مشغل GRestore لحفظ الحالة الرسومية المحدثة.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

تظهر مقتطفات الكود التالية كيفية استخدام مشغلات PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageUsingPDFOperators()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFOperators.pdf"))
    {
        // Set coordinates for the image placement
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Get the page where the image needs to be added
        var page = document.Pages[1];

        // Load the image into a file stream
        using (var imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open))
        {
            // Add the image to the page's Resources collection
            page.Resources.Images.Add(imageStream);
        }

        // Save the current graphics state using the GSave operator
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Create a rectangle and matrix for positioning the image
        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0,
            0, rectangle.URY - rectangle.LLY,
            rectangle.LLX, rectangle.LLY
        });

        // Define how the image must be placed using the ConcatenateMatrix operator
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));

        // Get the image from the Resources collection
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Draw the image using the Do operator
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state using the GRestore operator
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "PDFOperators_out.pdf");
    }
}
```

## رسم XForm على الصفحة باستخدام المشغلين

يظهر هذا الموضوع كيفية استخدام مشغلات GSave/GRestore، ومشغل ConcatenateMatrix لتحديد موقع xForm ومشغل Do لرسم xForm على الصفحة.

تغلف الشيفرة أدناه محتويات ملف PDF الموجودة باستخدام زوج مشغلات GSave/GRestore. تساعد هذه الطريقة في الحصول على الحالة الرسومية الأولية في نهاية المحتويات الموجودة. بدون هذه الطريقة، قد تبقى تحويلات غير مرغوب فيها في نهاية سلسلة المشغلين الموجودة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DrawXFormOnPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DrawXFormOnPage.pdf"))
    {
        var pageContents = document.Pages[1].Contents;

        // Wrap existing contents with GSave/GRestore operators to preserve graphics state
        pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Add GSave operator to start new graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GSave());

        // Create an XForm
        var form = Aspose.Pdf.XForm.CreateNewForm(document.Pages[1], document);
        document.Pages[1].Resources.Forms.Add(form);

        form.Contents.Add(new Aspose.Pdf.Operators.GSave());
        // Define image width and height
        form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // Load image into stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the XForm's resources
            form.Resources.Images.Add(imageStream);
        }

        var ximage = form.Resources.Images[form.Resources.Images.Count];
        // Draw the image on the XForm
        form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
        form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Place and draw the XForm at two different coordinates

        // Draw the XForm at (100, 500)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Draw the XForm at (100, 300)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Restore graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "DrawXFormOnPage_out.pdf");
    }
}
```

## إزالة كائنات الرسومات باستخدام فئات المشغلين

توفر فئات المشغلين ميزات رائعة لمعالجة PDF. عندما يحتوي ملف PDF على رسومات لا يمكن إزالتها باستخدام طريقة [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) لفئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)، يمكن استخدام فئات المشغلين لإزالتها بدلاً من ذلك.

تظهر مقتطفات الكود التالية كيفية إزالة الرسومات. يرجى ملاحظة أنه إذا كان ملف PDF يحتوي على تسميات نصية للرسومات، فقد تستمر في ملف PDF باستخدام هذه الطريقة. لذلك ابحث عن مشغلات الرسومات للحصول على طريقة بديلة لحذف مثل هذه الصور.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
  private static void RemoveGraphicsObjects()
  {
      // The path to the documents directory
      var dataDir = RunExamples.GetDataDir_AsposePdf();

      // Open PDF document
      using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphicsObjects.pdf"))
      {
          // Get the specific page (page 2 in this case)
          var page = document.Pages[2];

          // Get the operator collection from the page contents
          var oc = page.Contents;

          // Define the path-painting operators to be removed
          var operators = new Aspose.Pdf.Operator[]
          {
              new Aspose.Pdf.Operators.Stroke(),
              new Aspose.Pdf.Operators.ClosePathStroke(),
              new Aspose.Pdf.Operators.Fill()
          };

          // Delete the specified operators from the page contents
          oc.Delete(operators);

          // Save PDF document
          document.Save(dataDir + "NoGraphics_out.pdf");
      }
  }
```

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