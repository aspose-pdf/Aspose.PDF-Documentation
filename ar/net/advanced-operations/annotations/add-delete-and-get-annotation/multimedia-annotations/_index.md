---
title: التعليق المتعدد الوسائط على PDF باستخدام C#
linktitle: التعليق المتعدد الوسائط
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/multimedia-annotation/
description: Aspose.PDF for .NET يتيح لك إضافة واسترجاع وحذف التعليق المتعدد الوسائط من مستند PDF الخاص بك.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Multimedia Annotation using C#",
    "alternativeHeadline": "Enable Multimedia Annotations in PDF with C#",
    "abstract": "Aspose.PDF for .NET يقدم قدرات متقدمة للتعليق المتعدد الوسائط، مما يمكّن المستخدمين من إضافة واسترجاع وحذف أنواع متعددة من الوسائط في مستندات PDF بسلاسة. تدعم هذه الميزة التعليقات على الشاشة والصوت والوسائط الغنية، مما يعزز تفاعل المستند ويسمح بدمج محتوى الفيديو الخارجي، والملاحظات الصوتية، والوسائط المدمجة، مما يجعل مستندات PDF أكثر ديناميكية وجاذبية.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF multimedia annotation, Aspose.PDF, C# PDF features, screen annotation, sound annotation, rich media annotation, widget annotations, 3D annotation, document navigation, multimedia file embedding",
    "wordcount": "2247",
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
    "url": "/net/multimedia-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/multimedia-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

التعليقات في مستند PDF موجودة في مجموعة التعليقات الخاصة بكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). تحتوي هذه المجموعة على جميع التعليقات لتلك الصفحة الفردية فقط: كل صفحة لها مجموعتها الخاصة من التعليقات. لإضافة تعليق إلى صفحة معينة، أضفه إلى مجموعة التعليقات الخاصة بتلك الصفحة باستخدام طريقة Add.

استخدم فئة [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) في مساحة أسماء Aspose.PDF.InteractiveFeatures.Annotations لتضمين ملفات SWF كتعليقات في مستند PDF بدلاً من ذلك. يحدد التعليق على الشاشة منطقة من الصفحة يمكن تشغيل مقاطع الوسائط عليها.

عندما تحتاج إلى إضافة رابط فيديو خارجي في مستند PDF، يمكنك استخدام [MovieAnnotaiton](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation).
يحتوي التعليق على الفيلم على رسومات متحركة وصوت ليتم تقديمه على شاشة الكمبيوتر ومن خلال مكبرات الصوت.

يجب أن يكون [Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) مشابهًا لتعليق نصي باستثناء أنه بدلاً من ملاحظة نصية، يحتوي على صوت مسجل من ميكروفون الكمبيوتر أو مستورد من ملف. عند تفعيل التعليق، سيتم تشغيل الصوت. يجب أن يتصرف التعليق مثل التعليق النصي في معظم النواحي، مع أيقونة مختلفة (بشكل افتراضي، مكبر صوت) للإشارة إلى أنه يمثل صوتًا.

ومع ذلك، عندما تكون هناك حاجة لتضمين الوسائط داخل مستند PDF، تحتاج إلى استخدام [RichMediaAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

يمكن استخدام الطرق/الخصائص التالية من فئة RichMediaAnnotation.

- Stream CustomPlayer { set; }: يسمح بتعيين المشغل المستخدم لتشغيل الفيديو.
- string CustomFlashVariables { set; }: يسمح بتعيين المتغيرات التي يتم تمريرها إلى تطبيق الفلاش. هذه السطر هو مجموعة من أزواج "key=value" التي يتم فصلها بـ '&'.
- void AddCustomData(strig name, Stream data): أضف بيانات إضافية للمشغل. على سبيل المثال source=video.mp4&autoPlay=true&scale=100.
- ActivationEvent ActivateOn { get; set}: الحدث ينشط المشغل؛ القيم الممكنة هي Click، PageOpen، PageVisible.
- void SetContent(Stream stream, string name): تعيين بيانات الفيديو/الصوت التي سيتم تشغيلها.
- void Update(): إنشاء هيكل بيانات التعليق. يجب استدعاء هذه الطريقة أخيرًا.
- void SetPoster(Stream): تعيين ملصق الفيديو أي الصورة المعروضة عندما لا يكون المشغل نشطًا.

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## إضافة تعليق على الشاشة

تظهر مقتطفات الشيفرة التالية كيفية إضافة تعليق على الشاشة إلى ملف PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddScreenAnnotationWithMedia()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (cument = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Path to the media file (SWF)
        var mediaFile = dataDir + "input.swf";

        // Create Screen Annotation
        var screenAnnotation = new Aspose.Pdf.Annotations.ScreenAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(170, 190, 470, 380),
            mediaFile);

        // Add the annotation to the page
        document.Pages[1].Annotations.Add(screenAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddScreenAnnotationWithMedia_out.pdf");
    }
}
```

## إضافة تعليق صوتي

تظهر مقتطفات الشيفرة التالية كيفية إضافة تعليق صوتي إلى ملف PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddSoundAnnotation()
{
    // Open PDF document
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        var mediaFile = dataDir + "file_example_WAV_1MG.wav";

        // Create Sound Annotation
        var soundAnnotation = new Aspose.Pdf.Annotations.SoundAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(20, 700, 60, 740),
            mediaFile)
        {
            Color = Aspose.Pdf.Color.Blue,
            Title = "John Smith",
            Subject = "Sound Annotation demo",
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(20, 700, 60, 740))
        };

        document.Pages[1].Annotations.Add(soundAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddSoundAnnotation_out.pdf");
    }
}
```

## إضافة RichMediaAnnotation

تظهر مقتطفات الشيفرة التالية كيفية إضافة RichMediaAnnotation إلى ملف PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRichMediaAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
        Page page = document.Pages.Add();

        // Define video and poster names
        const string videoName = "file_example_MP4_480_1_5MG.mp4";
        const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
        string skinName = "SkinOverAllNoFullNoCaption.swf";

        // Create RichMediaAnnotation
        var rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600));

        // Specify the stream containing the video player code
        rma.CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp, "Players", "Videoplayer.swf"), FileMode.Open, FileAccess.Read);

        // Compose flash variables line for the player
        rma.CustomFlashVariables = $"source={videoName}&skin={skinName}";

        // Add skin code
        rma.AddCustomData(skinName, new FileStream(Path.Combine(pathToAdobeApp, skinName), FileMode.Open, FileAccess.Read));

        // Set poster for the video
        rma.SetPoster(new FileStream(Path.Combine(dataDir, posterName), FileMode.Open, FileAccess.Read));

        // Set video content
        using (Stream fs = new FileStream(Path.Combine(dataDir, videoName), FileMode.Open, FileAccess.Read))
        {
            rma.SetContent(videoName, fs);
        }

        // Set type of the content (video)
        rma.Type = RichMediaAnnotation.ContentType.Video;

        // Activate player by click
        rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

        // Update annotation data
        rma.Update();

        // Add annotation to the page
        page.Annotations.Add(rma);

        // Save PDF document
        document.Save(dataDir + "RichMediaAnnotation_out.pdf");
    }
}
```

### الحصول على MultimediaAnnotation

يرجى محاولة استخدام مقتطف الشيفرة التالية للحصول على MultimediaAnnotation من مستند PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetMultimediaAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
    {
        // Get multimedia annotations (Screen, Sound, RichMedia)
        var mediaAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Screen
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Sound
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
            .Cast<Aspose.Pdf.Annotations.Annotation>();

        // Iterate through the annotations and print their details
        foreach (var ma in mediaAnnotations)
        {
            Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
        }
    }
}
```

### حذف MultimediaAnnotation

تظهر مقتطفات الشيفرة التالية كيفية حذف MultimediaAnnotation من ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePolyAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
    {
        // Get RichMedia annotations
        var richMediaAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
            .Cast<Aspose.Pdf.Annotations.RichMediaAnnotation>();

        // Delete each RichMedia annotation
        foreach (var rma in richMediaAnnotations)
        {
            document.Pages[1].Annotations.Delete(rma);
        }

        // Save PDF document
        document.Save(dataDir + "DeletePolyAnnotation_out.pdf");
    }
}
```

## إضافة تعليقات الأدوات

تستخدم النماذج التفاعلية [تعليقات الأدوات](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) لتمثيل مظهر الحقول وإدارة تفاعلات المستخدم.
نستخدم هذه العناصر النموذجية التي تضيف إلى PDF لتسهيل إدخال المعلومات أو تقديمها، أو إجراء بعض التفاعلات الأخرى مع المستخدم.

تعليقات الأدوات هي تمثيل رسومي لحقل نموذج على صفحات معينة، لذا لا يمكننا إنشاؤها مباشرة كتعليق.

ستحتوي كل تعليق أداة على رسومات مناسبة (مظهر) اعتمادًا على نوعها. بعد الإنشاء، يمكن تغيير بعض الجوانب المرئية، مثل نمط الحدود ولون الخلفية.
يمكن تغيير خصائص أخرى مثل لون النص والخط من خلال الحقل، بمجرد ربطه بأحدها.

في بعض الحالات، قد ترغب في أن يظهر حقل ما على أكثر من صفحة واحدة، مكررًا نفس القيمة. في هذه الحالة، قد تحتوي الحقول التي عادةً ما تحتوي على أداة واحدة فقط على أدوات متعددة مرتبطة: عادةً ما تحتوي TextField وListBox وComboBox وCheckBox على واحدة فقط، بينما تحتوي RadioGroup على أدوات متعددة، واحدة لكل زر راديو.
يمكن لشخص يملأ النموذج استخدام أي من تلك الأدوات لتحديث قيمة الحقل، وهذا ينعكس في جميع الأدوات الأخرى أيضًا.

يمثل كل حقل نموذج لكل مكان في المستند تعليق أداة واحدة. تتم إضافة بيانات التعليق الخاصة بموقع التعليق إلى الصفحة المعينة. يحتوي كل حقل نموذج على عدة متغيرات. يمكن أن يكون الزر زر راديو أو مربع اختيار أو زر ضغط. يمكن أن تكون أداة الاختيار مربع قائمة أو مربع مدمج.

في هذه العينة، سنتعلم كيفية إضافة أزرار الضغط للتنقل في المستند.

### إضافة زر إلى المستند

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPrintButton()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Define the rectangle for the button
        var rect = new Aspose.Pdf.Rectangle(72, 748, 164, 768);

        // Create a button field
        var printButton = new Aspose.Pdf.Forms.ButtonField(page, rect)
        {
            AlternateName = "Print current document",
            Color = Aspose.Pdf.Color.Black,
            PartialName = "printBtn1",
            NormalCaption = "Print Document"
        };

        // Set the border style for the button
        var border = new Aspose.Pdf.Annotations.Border(printButton)
        {
            Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
            Width = 2
        };
        printButton.Border = border;

        // Set the border and background color characteristics
        printButton.Characteristics.Border = System.Drawing.Color.FromArgb(255, 0, 0, 255);
        printButton.Characteristics.Background = System.Drawing.Color.FromArgb(255, 0, 191, 255);

        // Add the button to the form
        document.Form.Add(printButton);

        // Save PDF document
        document.Save(dataDir + "PrintButton_out.pdf");
    }
}
```

هذا الزر له حدود ويحدد خلفية. كما نقوم بتعيين اسم الزر (Name)، ونص تلميح (AlternateName)، وتسمية (NormalCaption)، ولون نص التسمية (Color).

### استخدام إجراءات تنقل المستند

يوجد مثال أكثر تعقيدًا لاستخدام تعليقات الأدوات - تنقل المستند في مستند PDF. قد يكون هذا مطلوبًا لإعداد عرض تقديمي لمستند PDF.

يوضح هذا المثال كيفية إنشاء 4 أزرار:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddNavigationButtons()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "JSON Fundamenals.pdf"))
    {
        // Create an array of button fields
        var buttons = new Aspose.Pdf.Forms.ButtonField[4];

        // Define alternate names and normal captions for the buttons
        var alternateNames = new[] { "Go to first page", "Go to prev page", "Go to next page", "Go to last page" };
        var normalCaptions = new[] { "First", "Prev", "Next", "Last" };

        // Define predefined actions for the buttons
        PredefinedAction[] actions = {
            PredefinedAction.FirstPage,
            PredefinedAction.PrevPage,
            PredefinedAction.NextPage,
            PredefinedAction.LastPage
        };

        // Define border and background colors
        var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
        var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);

        // We should create the buttons without attaching them to the page.
        for (var i = 0; i < 4; i++)
        {
            buttons[i] = new Aspose.Pdf.Forms.ButtonField(document, new Aspose.Pdf.Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
            {
                AlternateName = alternateNames[i],
                Color = Aspose.Pdf.Color.White,
                NormalCaption = normalCaptions[i],
                OnActivated = new Aspose.Pdf.Annotations.NamedAction(actions[i])
            };

            // Set the border style for the button
            buttons[i].Border = new Aspose.Pdf.Annotations.Border(buttons[i])
            {
                Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
                Width = 2
            };

            // Set the border and background color characteristics
            buttons[i].Characteristics.Border = clrBorder;
            buttons[i].Characteristics.Background = clrBackGround;
        }

        // Duplicate the array of buttons on each page in the document
        for (var pageIndex = 1; pageIndex <= document.Pages.Count; pageIndex++)
        {
            for (var i = 0; i < 4; i++)
            {
                document.Form.Add(buttons[i], $"btn{pageIndex}_{i + 1}", pageIndex);
            }
        }

        // Save PDF document
        document.Save(dataDir + "NavigationButtons_out.pdf");

        // We call Form.Add method with the following parameters: field, name, and the index of the pages that this field will be added to.
        // And to get the full result, we need disable the “First” and “Prev” buttons on the first page and the “Next” and “Last” buttons on the last page.

        document.Form["btn1_1"].ReadOnly = true;
        document.Form["btn1_2"].ReadOnly = true;

        document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
        document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
    }
}
```

للحصول على معلومات أكثر تفصيلًا وإمكانيات هذه الميزات، راجع أيضًا [العمل مع النماذج](/pdf/net/acroforms/).

في مستندات PDF، يمكنك عرض وإدارة محتوى ثلاثي الأبعاد عالي الجودة تم إنشاؤه باستخدام برامج CAD ثلاثية الأبعاد أو برامج النمذجة ثلاثية الأبعاد ومدمج في مستند PDF. يمكنك تدوير العناصر ثلاثية الأبعاد في جميع الاتجاهات كما لو كنت تحملها في يديك.

لماذا تحتاج إلى عرض ثلاثي الأبعاد للصور على الإطلاق؟

على مدار السنوات القليلة الماضية، حققت التكنولوجيا تقدمًا هائلًا في جميع المجالات بفضل الطباعة ثلاثية الأبعاد. يمكن تطبيق تقنيات الطباعة ثلاثية الأبعاد لتعليم المهارات التكنولوجية في البناء والهندسة الميكانيكية والتصميم كأداة رئيسية. يمكن أن تسهم هذه التقنيات بفضل ظهور أجهزة الطباعة الشخصية في إدخال أشكال جديدة من تنظيم العملية التعليمية، وزيادة الدافع، وتشكيل الكفاءات اللازمة للخريجين والمعلمين.

تتمثل المهمة الرئيسية للنمذجة ثلاثية الأبعاد في فكرة كائن أو عنصر مستقبلي لأنه، من أجل إصدار كائن، تحتاج إلى فهم ميزاته التصميمية بالتفصيل من أجل التجديد المتتابع في التصميم الصناعي أو الهندسة المعمارية.

## إضافة تعليق ثلاثي الأبعاد

يتم إضافة التعليق ثلاثي الأبعاد باستخدام نموذج تم إنشاؤه بتنسيق U3D.

1. إنشاء [مستند](https://reference.aspose.com/pdf/net/aspose.pdf/document) جديد.
1. تحميل بيانات نموذج ثلاثي الأبعاد المطلوب (في حالتنا "Ring.u3d") لإنشاء [PDF3DContent](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent).
1. إنشاء كائن [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) وربطه بالمستند و3DContent.
1. ضبط كائن pdf3dArtWork:

    - 3DLightingScheme - (سنقوم بتعيين `CAD` في المثال)
    - 3DRenderMode - (سنقوم بتعيين `Solid` في المثال)
    - ملء `ViewArray`، وإنشاء على الأقل [عرض ثلاثي الأبعاد](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) وإضافته إلى المصفوفة.

1. تعيين 3 معلمات أساسية في التعليق:
    - `page` التي سيتم وضع التعليق عليها.
    - `rectangle`، داخلها التعليق.
    - و`3dArtWork` كائن.
1. للحصول على عرض أفضل للكائن ثلاثي الأبعاد، قم بتعيين إطار الحدود.
1. تعيين العرض الافتراضي (على سبيل المثال - TOP).
1. إضافة بعض المعلمات الإضافية: الاسم، ملصق المعاينة، إلخ.
1. إضافة التعليق إلى [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
1. حفظ النتيجة.

### مثال

يرجى مراجعة مقتطف الشيفرة التالية لإضافة تعليق ثلاثي الأبعاد.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Add3dAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Load 3D content
        var pdf3DContent = new Aspose.Pdf.Annotations.PDF3DContent(dataDir + "Ring.u3d");

        // Create 3D artwork
        var pdf3dArtWork = new Aspose.Pdf.Annotations.PDF3DArtwork(document, pdf3DContent)
        {
            LightingScheme = new Aspose.Pdf.Annotations.PDF3DLightingScheme(Aspose.Pdf.Annotations.LightingSchemeType.CAD),
            RenderMode = new Aspose.Pdf.Annotations.PDF3DRenderMode(Aspose.Pdf.Annotations.RenderModeType.Solid),
        };

        // Define matrices for different views
        var topMatrix = new Aspose.Pdf.Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Aspose.Pdf.Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);

        // Add views to the 3D artwork
        pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        // Add page
        var page = document.Pages.Add();

        // Create a 3D annotation
        var pdf3dAnnotation = new Aspose.Pdf.Annotations.PDF3DAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.Border = new Aspose.Pdf.Annotations.Border(pdf3dAnnotation);
        pdf3dAnnotation.SetDefaultViewIndex(1);
        pdf3dAnnotation.Flags = Aspose.Pdf.Annotations.AnnotationFlags.NoZoom;
        pdf3dAnnotation.Name = "Ring.u3d";

        // Set preview image if needed
        // pdf3dAnnotation.SetImagePreview(dataDir + "sample_3d.png");

        // Add the 3D annotation to the page
        document.Pages[1].Annotations.Add(pdf3dAnnotation);

        // Save PDF document
        document.Save(dataDir + "Add3dAnnotation_out.pdf");
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