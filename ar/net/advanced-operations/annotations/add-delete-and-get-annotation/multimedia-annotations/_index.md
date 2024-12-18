---
title: تعليق توضيحي متعدد الوسائط لملفات PDF باستخدام C#
linktitle: التعليق التوضيحي المتعدد الوسائط
type: docs
weight: 40
url: /ar/net/multimedia-annotation/
description: يتيح لك Aspose.PDF لـ .NET إضافة، والحصول على، وحذف التعليق التوضيحي المتعدد الوسائط من مستند PDF الخاص بك.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تعليق توضيحي متعدد الوسائط لملفات PDF باستخدام C#",
    "alternativeHeadline": "كيفية إضافة التعليق التوضيحي المتعدد الوسائط في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, التعليق التوضيحي المتعدد الوسائط, التعليق التوضيحي للشاشة, التعليق التوضيحي بالصوت, التعليق التوضيحي بالأدوات, التعليق التوضيحي ثلاثي الأبعاد",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق توثيق Aspose.PDF",
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
    "dateModified": "2022-02-04",
    "description": "يتيح لك Aspose.PDF لـ .NET إضافة، والحصول على، وحذف التعليق التوضيحي المتعدد الوسائط من مستند PDF الخاص بك."
}
</script>
التعليقات التوضيحية في مستند PDF موجودة في مجموعة Annotations الخاصة بكائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). تحتوي هذه المجموعة على جميع التعليقات التوضيحية لتلك الصفحة الفردية فقط: كل صفحة لديها مجموعة Annotations الخاصة بها. لإضافة تعليق توضيحي إلى صفحة معينة، أضفه إلى مجموعة Annotations الخاصة بتلك الصفحة باستخدام طريقة الإضافة.

استخدم صف [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) في فضاء الأسماء Aspose.PDF.InteractiveFeatures.Annotations لتضمين ملفات SWF كتعليقات توضيحية في مستند PDF بدلاً من ذلك. يحدد التعليق التوضيحي للشاشة منطقة من الصفحة يمكن تشغيل مقاطع الوسائط عليها.

عندما تحتاج إلى إضافة رابط فيديو خارجي في مستند PDF، يمكنك استخدام [MovieAnnotaiton](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation).
يحتوي التعليق التوضيحي للفيلم على رسوم متحركة وصوت ليتم تقديمها على شاشة الكمبيوتر ومن خلال السماعات.

يجب أن يكون [Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) مماثلًا لتعليق نصي باستثناء أنه بدلاً من ملاحظة نصية، يحتوي على صوت مسجل من ميكروفون الكمبيوتر أو مستورد من ملف.
يجب أن يكون [تعليق الصوت](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) مماثلاً لتعليق النص باستثناء أنه بدلاً من ملاحظة نصية، يحتوي على صوت مسجل من ميكروفون الكمبيوتر أو مستورد من ملف.

ومع ذلك، عندما يكون هناك متطلب لتضمين وسائط داخل مستند PDF، يجب استخدام [تعليق وسائط غنية](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

يمكن استخدام الطرق/الخصائص التالية لفئة RichMediaAnnotation.

- Stream CustomPlayer { set; }: يسمح بتعيين اللاعب المستخدم لتشغيل الفيديو.
- string CustomFlashVariables { set; }: يسمح بتعيين المتغيرات التي يتم تمريرها إلى تطبيق الفلاش. هذا السطر عبارة عن مجموعة من أزواج "key=value" المفصولة بـ ‘&'.
- void AddCustomData(strig name, Stream data): إضافة بيانات إضافية للاعب. على سبيل المثال source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: الحدث ينشط اللاعب؛ القيم الممكنة هي Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): تعيين بيانات الفيديو/الصوت لتشغيلها.
 - void SetContent(Stream stream, string name): تعيين بيانات الفيديو / الصوت لتشغيلها.
- void Update(): إنشاء هيكل بيانات التعليق التوضيحي. يجب استدعاء هذه الطريقة أخيرًا.
- void SetPoster(Stream): تعيين ملصق الفيديو أي الصورة المعروضة عندما لا يكون المشغل نشطًا.

يعمل الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## إضافة تعليق توضيحي للشاشة

يُظهر الكود التالي كيفية إضافة تعليق توضيحي للشاشة إلى ملف PDF:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.IO;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleMultimediaAnnotation
    {
        // مسار إلى دليل المستندات.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddScreenAnnotation()
        {
            // تحميل ملف PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "input.swf");
            // إنشاء تعليق توضيحي للشاشة
            var screenAnnotation = new ScreenAnnotation(
                document.Pages[1],
                new Rectangle(170, 190, 470, 380),
                mediaFile);
            document.Pages[1].Annotations.Add(screenAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_swf.pdf"));
        }
    }
}
```
## إضافة تعليق صوتي

الكود التالي يوضح كيفية إضافة تعليق صوتي إلى ملف PDF:

```csharp
        public static void AddSoundAnnotation()
        {
            // تحميل ملف PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "file_example_WAV_1MG.wav");
            // إنشاء تعليق صوتي
            var soundAnnotation = new SoundAnnotation(
                document.Pages[1],
                new Rectangle(20, 700, 60, 740),
                mediaFile)
            {
                Color = Color.Blue,
                Title = "John Smith",
                Subject = "عرض تعليق صوتي",
                Popup = new PopupAnnotation(document)
            };

            document.Pages[1].Annotations.Add(soundAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_wav.pdf"));
        }
```

## إضافة تعليق وسائط غنية

الكود التالي يوضح كيفية إضافة تعليق وسائط غنية إلى ملف PDF:
يوضح المقتطف التالي من الرمز كيفية إضافة RichMediaAnnotation إلى ملف PDF:

```csharp
        public static void AddRichMediaAnnotation()
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
            var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
            Page page = doc.Pages.Add();
            // إعطاء اسم لبيانات الفيديو. سيتم تضمين هذه البيانات في المستند بهذا الاسم والرجوع إليها من متغيرات فلاش بهذا الاسم.
            // يجب ألا يحتوي videoName على مسار الملف؛ هذا هو بالأحرى "مفتاح" للوصول إلى البيانات داخل مستند PDF
            const string videoName = "file_example_MP4_480_1_5MG.mp4";
            const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
            // نستخدم أيضاً جلد لمشغل الفيديو
            string skinName = "SkinOverAllNoFullNoCaption.swf";
            RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600))
            {
                // هنا يجب تحديد تيار يحتوي على رمز مشغل الفيديو
                CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp,"Players","Videoplayer.swf"), FileMode.Open, FileAccess.Read),
                // تكوين خط متغيرات فلاش للمشغل. يرجى ملاحظة أن مشغلات مختلفة قد تحتوي على تنسيقات مختلفة لخط متغيرات الفلاش. راجع التوثيق الخاص بمشغلك.
                CustomFlashVariables = $"source={videoName}&skin={skinName}"
            };
            // إضافة رمز الجلد.
            rma.AddCustomData(skinName,
                new FileStream(Path.Combine(pathToAdobeApp,"SkinOverAllNoFullNoCaption.swf"), FileMode.Open, FileAccess.Read));
            // تعيين ملصق للفيديو
            rma.SetPoster(new FileStream(Path.Combine(_dataDir, posterName), FileMode.Open, FileAccess.Read));

            Stream fs = new FileStream(Path.Combine(_dataDir,videoName), FileMode.Open, FileAccess.Read);

            // تعيين محتوى الفيديو
            rma.SetContent(videoName, fs);

            // تعيين نوع المحتوى (فيديو)
            rma.Type = RichMediaAnnotation.ContentType.Video;

            // تفعيل المشغل بالنقر
            rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

            // تحديث بيانات التعليق التوضيحي. يجب استدعاء هذه الطريقة بعد جميع التعيينات/الإعدادات. تقوم هذه الطريقة بتهيئة هيكل بيانات التعليق التوضيحي وتضمين البيانات المطلوبة.
            rma.Update();

            // إضافة التعليق التوضيحي على الصفحة.
            page.Annotations.Add(rma);

            doc.Save(Path.Combine(_dataDir,"RichMediaAnnotation.pdf"));
        }
```
### الحصول على تعليق توضيحي متعدد الوسائط

يرجى محاولة استخدام قطعة الكود التالية للحصول على تعليق توضيحي متعدد الوسائط من مستند PDF.

```csharp
        public static void GetMultimediaAnnotation()
        {
            // تحميل ملف PDF
            Document document = new Document(
                Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var mediaAnnotations = document.Pages[1].Annotations
                .Where(a => (a.AnnotationType == AnnotationType.Screen)
                || (a.AnnotationType == AnnotationType.Sound)
                || (a.AnnotationType == AnnotationType.RichMedia))
                .Cast<Annotation>();
            foreach (var ma in mediaAnnotations)
            {
                Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
            }
        }
```

### حذف التعليق التوضيحي متعدد الوسائط

قطعة الكود التالية توضح كيفية حذف التعليق التوضيحي متعدد الوسائط من ملف PDF.

```csharp
        public static void DeletePolyAnnotation()
        {
            // تحميل ملف PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var richMediaAnnotations = document.Pages[1].Annotations
                            .Where(a => a.AnnotationType == AnnotationType.RichMedia)
                            .Cast<RichMediaAnnotation>();

            foreach (var rma in richMediaAnnotations)
            {
                document.Pages[1].Annotations.Delete(rma);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation_del.pdf"));
        }
```
## إضافة تعليقات توضيحية للأداة

النماذج التفاعلية تستخدم [تعليقات توضيحية للأداة](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) لتمثيل مظهر الحقول ولإدارة التفاعلات مع المستخدم.
نحن نستخدم هذه العناصر النموذجية التي نضيفها إلى ملف PDF لتسهيل إدخال المعلومات أو إرسالها، أو لأداء بعض التفاعلات الأخرى مع المستخدم.

تعليقات توضيحية للأداة هي تمثيل بصري لحقل نموذج على صفحات محددة، لذا لا يمكننا إنشاؤها مباشرة كتعليق توضيحي.

سيكون لكل تعليق توضيحي للأداة رسومات مناسبة (مظهر) تعتمد على نوعها. بعد الإنشاء، يمكن تغيير بعض الجوانب البصرية مثل نمط الحدود ولون الخلفية.
يمكن تغيير خصائص أخرى مثل لون النص والخط من خلال الحقل، بمجرد إرفاقه بواحد.

في بعض الحالات، قد ترغب في ظهور حقل على أكثر من صفحة، مع تكرار نفس القيمة.
في بعض الحالات، قد ترغب في ظهور حقل على أكثر من صفحة واحدة، مع تكرار نفس القيمة.
الشخص الذي يملأ النموذج قد يستخدم أي من هذه الأدوات لتحديث قيمة الحقل، وينعكس ذلك في جميع الأدوات الأخرى أيضًا.

كل حقل نموذج لكل مكان في الوثيقة يمثل واحدة من التوضيحات الخاصة بالأدوات. يتم إضافة البيانات المحددة الموقع لتوضيح الأداة إلى الصفحة المعينة. لكل حقل نموذج عدة تنويعات. يمكن أن يكون الزر زر راديو، مربع اختيار، أو زر ضغط. يمكن أن يكون الأداة المختارة صندوق قائمة أو صندوق تحرير مركب.

في هذا المثال، سنتعلم كيفية إضافة الأزرار للتنقل في الوثيقة.

### إضافة زر إلى الوثيقة

```csharp
document = new Document();
var page = document.Pages.Add();
var rect = new Rectangle(72, 748, 164, 768);
var printButton = new ButtonField(page, rect)
{
    AlternateName = "طباعة الوثيقة الحالية",
    Color = Color.Black,
    PartialName = "printBtn1",
    NormalCaption = "طباعة الوثيقة"
};
var border = new Border(printButton)
{
    Style = BorderStyle.Solid,
    Width = 2
};
printButton.Border = border;
printButton.Characteristics.Border =
    System.Drawing.Color.FromArgb(255, 0, 0, 255);
printButton.Characteristics.Background =
    System.Drawing.Color.FromArgb(255, 0, 191, 255);
document.Form.Add(printButton);
```
هذا الزر يحتوي على حدود ويتم تعيين خلفية. كما نقوم بتعيين اسم الزر (الاسم)، وتلميح (الاسم البديل)، وتسمية (التسمية العادية)، ولون نص التسمية (اللون).

### استخدام إجراءات التنقل في المستندات

هناك مثال أكثر تعقيدًا لاستخدام تعليقات الأدوات - التنقل في المستند في مستند PDF. قد يكون هذا مطلوبًا لإعداد عرض تقديمي لمستند PDF.

هذا المثال يوضح كيفية إنشاء 4 أزرار:

```csharp
var document = new Document(@"C:\\tmp\\JSON Fundamenals.pdf");
var buttons = new ButtonField[4];
var alternateNames = new[] { "Go to first page", "Go to prev page", "Go to next page", "Go to last page" };
var normalCaptions = new[] { "First", "Prev", "Next", "Last" };
PredefinedAction[] actions = {
PredefinedAction.FirstPage,
PredefinedAction.PrevPage,
PredefinedAction.NextPage,
PredefinedAction.LastPage };
var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);
```

يجب أن نقوم بإنشاء الأزرار دون ربطها بالصفحة.
يجب أن نقوم بإنشاء الأزرار دون ربطها بالصفحة.

```csharp
for (var i = 0; i < 4; i++)
{
    buttons[i] = new ButtonField(document,
           new Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
    {
       AlternateName = alternateNames[i],
       Color = Color.White,
       NormalCaption = normalCaptions[i],
       OnActivated = new NamedAction(actions[i])
    };
    buttons[i].Border = new Border(buttons[i])
    {
       Style = BorderStyle.Solid,
       Width = 2
    };
    buttons[i].Characteristics.Border = clrBorder;
    buttons[i].Characteristics.Background = clrBackGround;
}
```

يجب أن نقوم بتكرار هذا المصفوفة من الأزرار على كل صفحة في المستند.

```csharp
for (var pageIndex = 1; pageIndex <= document.Pages.Count;
                                                        pageIndex++)
    for (var i = 0; i < 4; i++)
        document.Form.Add(buttons[i],
          $"btn{pageIndex}_{i + 1}", pageIndex);

```

نقوم بدعوة [Form.Add method](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) مع الباراميترات التالية: الحقل، الاسم، ومؤشر الصفحات التي سيتم إضافة هذا الحقل إليها.
نحن نستدعي [طريقة Form.Add](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) مع المعاملات التالية: الحقل، الاسم، وفهرس الصفحات التي سيتم إضافة هذا الحقل إليها.

وللحصول على النتيجة الكاملة، نحتاج إلى تعطيل أزرار "الأول" و"السابق" في الصفحة الأولى وأزرار "التالي" و"الأخير" في الصفحة الأخيرة.

```csharp
document.Form["btn1_1"].ReadOnly = true;
document.Form["btn1_2"].ReadOnly = true;

document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
```

لمزيد من المعلومات التفصيلية وإمكانيات هذه الميزات، انظر أيضًا إلى [العمل مع النماذج](/pdf/ar/net/acroforms/).

في مستندات PDF، يمكنك عرض وإدارة محتوى ثلاثي الأبعاد عالي الجودة الذي تم إنشاؤه باستخدام برنامج CAD ثلاثي الأبعاد أو برنامج نمذجة ثلاثية الأبعاد وتضمينه في مستند PDF. يمكن تدوير عناصر ثلاثية الأبعاد في جميع الاتجاهات كما لو كنت تمسك بها بيديك.

لماذا تحتاج إلى عرض الصور ثلاثية الأبعاد على الإطلاق؟

خلال السنوات القليلة الماضية، قامت التكنولوجيا بتحقيق اختراقات هائلة في جميع المجالات بفضل الطباعة ثلاثية الأبعاد.
على مدار السنوات القليلة الماضية، حققت التكنولوجيا اختراقات كبيرة في جميع المجالات بفضل الطباعة ثلاثية الأبعاد.

المهمة الرئيسية للنمذجة ثلاثية الأبعاد هي فكرة الكائن المستقبلي أو الكائن لأنه، من أجل إصدار كائن، تحتاج إلى فهم ميزات تصميمه بكل التفاصيل لإعادة تكوينها المتتالية في التصميم الصناعي أو الهندسة المعمارية.

## إضافة تعليق توضيحي ثلاثي الأبعاد

يتم إضافة التعليق التوضيحي ثلاثي الأبعاد باستخدام نموذج تم إنشاؤه بتنسيق U3D.

1. إنشاء [مستند](https://reference.aspose.com/pdf/net/aspose.pdf/document) جديد
1. تحميل بيانات النموذج ثلاثي الأبعاد المطلوب (في حالتنا "Ring.u3d") لإنشاء [محتوى PDF3D](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent)
1. إنشاء كائن [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) وربطه بالمستند و3DContent
1. ضبط كائن pdf3dArtWork:

    - 3DLightingScheme - (سنضبط `CAD` في المثال)
    - 3DRenderMode - (سنضبط `Solid` في المثال)
    - ملء `ViewArray`، إنشاء على الأقل واحدة [عرض ثلاثي الأبعاد](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) وإضافتها إلى المصفوفة.

changefreq: "monthly"
type: docs
- املأ `ViewArray`، أنشئ على الأقل رؤية [3D View](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) واحدة وأضفها إلى المصفوفة.

1. حدد ثلاثة معاملات أساسية في التعليق التوضيحي:
    - ال`صفحة` التي سيوضع عليها التعليق التوضيحي،
    - ال`مستطيل`، داخل الذي التعليق التوضيحي،
    - وكائن `3dArtWork`.
1. لعرض أفضل للكائن ثلاثي الأبعاد، حدد إطار الحدود
1. حدد العرض الافتراضي (على سبيل المثال - TOP)
1. أضف بعض المعاملات الإضافية: الاسم، ملصق المعاينة إلخ.
1. أضف التعليق التوضيحي إلى ال[صفحة](https://reference.aspose.com/pdf/net/aspose.pdf/page)
1. احفظ النتيجة

### مثال

يرجى التحقق من الكود التالي لإضافة تعليق توضيحي ثلاثي الأبعاد.

```csharp
    public static void Add3dAnnotation()
    {
    // تحميل ملف PDF
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(System.IO.Path.Combine(_dataDir,"Ring.u3d"));
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent)
    {
        LightingScheme = new PDF3DLightingScheme(LightingSchemeType.CAD),
        RenderMode = new PDF3DRenderMode(RenderModeType.Solid),
    };
    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.Pages.Add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.Border = new Border(pdf3dAnnotation);
    pdf3dAnnotation.SetDefaultViewIndex(1);
    pdf3dAnnotation.Flags = AnnotationFlags.NoZoom;
    pdf3dAnnotation.Name = "Ring.u3d";
    //تعيين صورة المعاينة إذا لزم الأمر
    //pdf3dAnnotation.SetImagePreview(System.IO.Path.Combine(_dataDir, "sample_3d.png"));
    document.Pages[1].Annotations.Add(pdf3dAnnotation);

    document.Save(System.IO.Path.Combine(_dataDir, "sample_3d.pdf"));
    }
```
هذا المثال بالكود أظهر لنا هذا النموذج:

![عرض توضيحي ثلاثي الأبعاد](3d_demo.png)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "مكتبة Aspose.PDF لـ .NET",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة تعديل PDF لـ .NET",
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

