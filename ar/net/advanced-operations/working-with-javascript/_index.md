---
title: العمل مع JavaScript
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /ar/net/working-with-javascript/
description: تعلم كيفية إضافة وتعديل وتنفيذ JavaScript في مستندات PDF باستخدام Aspose.PDF for .NET. تعزيز التفاعلية والأتمتة.
lastmod: "2025-02-07"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with JavaScript",
    "alternativeHeadline": "Enhance PDF with Custom JavaScript Actions",
    "abstract": "اكتشف القدرات المحسّنة لدمج JavaScript داخل مستندات PDF من خلال Aspose.PDF for .NET. تتيح هذه الميزة الجديدة للمطورين إضافة وإدارة إجراءات JavaScript على مستوى المستند والصفحة، مما يمكّن من تجارب PDF تفاعلية وديناميكية تهدف إلى تحسين تفاعل المستخدم والوظائف. افتح إمكانيات JavaScript لإنشاء نماذج PDF متطورة تحاكي سلوكيات الويب، مما يرفع من سير عمل توليد المستندات لديك.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "JavaScript, Acrobat JavaScript, PDF document generation, JavaScript collection, document level JavaScript, JavaScript Action, interactive PDF forms, manipulate PDF files, HTML JavaScript, Aspose.PDF for .NET",
    "wordcount": "423",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2025-02-07",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إضافة JavaScript (DOM)

### ما هو Acrobat JavaScript؟

Acrobat JavaScript هو لغة تعتمد على جوهر JavaScript الإصدار 1.5 من ISO-16262، والمعروفة سابقًا باسم ECMAScript، وهي لغة برمجة كائنية التوجه تم تطويرها بواسطة Netscape Communications. تم إنشاء JavaScript لتحميل معالجة صفحات الويب من الخادم إلى العميل في التطبيقات المستندة إلى الويب. يقوم Acrobat JavaScript بتنفيذ امتدادات، في شكل كائنات جديدة وطرقها وخصائصها المرافقة، إلى لغة JavaScript. تتيح هذه الكائنات الخاصة بـ Acrobat للمطور إدارة أمان المستند، والتواصل مع قاعدة بيانات، والتعامل مع مرفقات الملفات، ومعالجة ملف PDF بحيث يتصرف مثل نموذج تفاعلي مدعوم من الويب، وما إلى ذلك. نظرًا لأن الكائنات الخاصة بـ Acrobat تُضاف فوق JavaScript الأساسي، لا يزال لديك وصول إلى فئاتها القياسية، بما في ذلك Math وString وDate وArray وRegExp.

### Acrobat JavaScript مقابل JavaScript HTML (الويب)

تتمتع مستندات PDF بمرونة كبيرة حيث يمكن عرضها داخل برنامج Acrobat وكذلك في متصفح الويب. لذلك، من المهم أن تكون على دراية بالاختلافات بين Acrobat JavaScript وJavaScript المستخدم في متصفح الويب، المعروف أيضًا باسم JavaScript HTML:

- لا يمكن لـ Acrobat JavaScript الوصول إلى الكائنات داخل صفحة HTML. وبالمثل، لا يمكن لـ JavaScript HTML الوصول إلى الكائنات داخل ملف PDF.
- يمكن لـ JavaScript HTML معالجة كائنات مثل Window. لا يمكن لـ Acrobat JavaScript الوصول إلى هذا الكائن المحدد ولكنه يمكنه معالجة كائنات خاصة بـ PDF.

يمكنك إضافة JavaScript على مستوى المستند والصفحة باستخدام [Aspose.PDF for .NET](/pdf/ar/net/). لإضافة JavaScript:

### إضافة JavaScript إلى إجراء المستند أو الصفحة

1. قم بإعلان وإنشاء كائن JavascriptAction مع عبارة JavaScript المطلوبة كوسيط للبناء.
1. قم بتعيين كائن JavascriptAction إلى الإجراء المطلوب في مستند PDF أو الصفحة.

المثال أدناه يطبق OpenAction على مستند معين.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Adding JavaScript at Document Level
        // Instantiate JavascriptAction with desired JavaScript statement
        var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

        // Assign JavascriptAction object to desired action of Document
        document.OpenAction = javaScript;

        // Adding JavaScript at Page Level
        document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
        document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

        // Save PDF Document
        document.Save(dataDir + "JavaScriptAdded_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Adding JavaScript at Document Level
    // Instantiate JavascriptAction with desired JavaScript statement
    var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    // Assign JavascriptAction object to desired action of Document
    document.OpenAction = javaScript;

    // Adding JavaScript at Page Level
    document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
    document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

    // Save PDF Document
    document.Save(dataDir + "JavaScriptAdded_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### إضافة/إزالة JavaScript على مستوى المستند

تمت إضافة خاصية جديدة باسم JavaScript في فئة Document والتي تحتوي على نوع مجموعة JavaScript وتوفر الوصول إلى سيناريوهات JavaScript بواسطة مفتاحها. تُستخدم هذه الخاصية لإضافة JavaScript على مستوى المستند. تحتوي مجموعة JavaScript على الخصائص والطرق التالية:

- string this(string key)– يحصل أو يحدد JavaScript بواسطة اسمه.
- IList Keys – يوفر قائمة بالمفاتيح الموجودة في مجموعة JavaScript.
- bool Remove(string key) – يزيل JavaScript بواسطة مفتاحه.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();
        document.JavaScript["func1"] = "function func1() { hello(); }";
        document.JavaScript["func2"] = "function func2() { hello(); }";
        document.Save(dataDir + "AddJavascript.pdf");
    }

    // Remove Document level JavaScript
    using (var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf"))
    {
        var keys = (IList)document1.JavaScript.Keys;

        Console.WriteLine("=============================== ");

        foreach (string key in keys)
        {
            Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
        }

        document1.JavaScript.Remove("func1");

        Console.WriteLine("Key 'func1' removed ");
        Console.WriteLine("=============================== ");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();
    document.JavaScript["func1"] = "function func1() { hello(); }";
    document.JavaScript["func2"] = "function func2() { hello(); }";
    document.Save(dataDir + "AddJavascript.pdf");

    // Remove Document level JavaScript
    using var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf");
    IList keys = (IList)document1.JavaScript.Keys;

    Console.WriteLine("=============================== ");

    foreach (string key in keys)
    {
        Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
    }

    document1.JavaScript.Remove("func1");

    Console.WriteLine("Key 'func1' removed ");
    Console.WriteLine("=============================== ");
}
```
{{< /tab >}}
{{< /tabs >}}

### تعيين تاريخ انتهاء صلاحية مستند PDF باستخدام إجراءات JavaScript

تتيح لك Aspose.PDF تعيين تاريخ انتهاء صلاحية لمستند PDF عن طريق تضمين إجراءات JavaScript. تضمن هذه الوظيفة أن يصبح PDF غير متاح بعد تاريخ ووقت محددين، مما يعزز أمان المستند والتحكم فيه. من خلال الاستفادة من إجراءات JavaScript، يمكنك تحديد شروط انتهاء دقيقة حتى الثانية، مما يضمن تنظيم وصول المستند بشكل صارم.

**يمكنك تحقيق ذلك من خلال اتباع هذه الخطوات**

1. **تهيئة المستند:** قم بإنشاء مستند PDF جديد وأضف صفحة فارغة أو افتح مستند PDF موجود.
2. **تحديد تاريخ ووقت انتهاء الصلاحية:** قم بتعيين التاريخ والوقت بعدهما سينتهي المستند.
3. **تحضير كود JavaScript:** 
    - استرجع التاريخ والوقت الحاليين.
    - حدد تاريخ ووقت انتهاء الصلاحية بالضبط، مع الأخذ في الاعتبار أن الأشهر تبدأ من الصفر في JavaScript.
    - قارن التاريخ والوقت الحاليين مع تاريخ ووقت انتهاء الصلاحية.
    - إذا تجاوز التاريخ والوقت الحاليين تاريخ ووقت انتهاء الصلاحية، اعرض تنبيهًا وأغلق المستند.
4. **تعيين إجراء الفتح:** اربط إجراء JavaScript بإجراء فتح المستند.
5. **حفظ المستند:** احفظ PDF مع JavaScript المضمن الذي يفرض شرط انتهاء الصلاحية.

فيما يلي مقتطفات من الكود توضح هذه الوظيفة في كل من C# (.NET) وJava.

توضح مقتطفات كود C# التالية كيفية تعيين تاريخ ووقت انتهاء صلاحية لمستند PDF باستخدام إجراءات JavaScript مع Aspose.PDF:

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();

        // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
        DateTime expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

        // Create JavaScript code to enforce the expiry date and time
        string jsCode =
            // Get the current date and time
            "var rightNow = new Date();\n" +
            // Set the expiry date and time
            "var endDate = new Date(" +
            $"{expiryDateTime.Year}," +
            $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
            $"{expiryDateTime.Day}," +
            $"{expiryDateTime.Hour}," +
            $"{expiryDateTime.Minute}," +
            $"{expiryDateTime.Second}" +
            ");\n" +
            "if(rightNow > endDate)\n" +
            "{\n" +
            "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
            "    this.closeDoc();\n" +
            "}";

        // Create a JavascriptAction with the defined JavaScript code
        var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

        // Set the JavaScript action to execute when the document is opened
        document.OpenAction = javaScript;

        // Save PDF document
        document.Save(dataDir + "PDFExpiry_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();

    // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
    var expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

    // Create JavaScript code to enforce the expiry date and time
    string jsCode =
        // Get the current date and time
        "var rightNow = new Date();\n" +
        // Set the expiry date and time
        "var endDate = new Date(" +
        $"{expiryDateTime.Year}," +
        $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
        $"{expiryDateTime.Day}," +
        $"{expiryDateTime.Hour}," +
        $"{expiryDateTime.Minute}," +
        $"{expiryDateTime.Second}" +
        ");\n" +
        "if(rightNow > endDate)\n" +
        "{\n" +
        "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
        "    this.closeDoc();\n" +
        "}";

    // Create a JavascriptAction with the defined JavaScript code
    var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

    // Set the JavaScript action to execute when the document is opened
    document.OpenAction = javaScript;

    // Save PDF document
    document.Save(dataDir + "PDFExpiry_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

- **كائن تاريخ JavaScript:** في JavaScript، يبدأ فهرس الشهر عند `0` لشهر يناير وينتهي عند `11` لشهر ديسمبر. تأكد من ضبط قيمة الشهر وفقًا لذلك عند تعيين تاريخ ووقت انتهاء الصلاحية.
  
- **اعتبارات الأمان:** بينما يمكن أن تتحكم إجراءات JavaScript في سلوك مستند PDF، فإنها تعتمد على دعم عارض PDF لـ JavaScript. قد لا تحترم جميع عارضي PDF هذه السكربتات، وقد يكون لدى المستخدمين تعطيل تنفيذ JavaScript لأسباب أمنية.

- **التخصيص:** قم بتعديل كود JavaScript لأداء إجراءات إضافية عند انتهاء الصلاحية، مثل تعطيل ميزات معينة، أو إعادة التوجيه إلى صفحة معينة، أو تسجيل الحدث. بالإضافة إلى ذلك، إذا لزم الأمر، يمكنك التحقق فقط من تاريخ انتهاء الصلاحية دون تحديد الوقت.

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