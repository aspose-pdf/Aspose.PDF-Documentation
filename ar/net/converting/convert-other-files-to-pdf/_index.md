---
title: تحويل تنسيقات الملفات الأخرى إلى PDF في .NET
linktitle: تحويل تنسيقات الملفات الأخرى إلى PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ar/net/convert-other-files-to-pdf/
lastmod: "2021-11-01"
description: يوضح هذا الموضوع كيفية استخدام Aspose.PDF لتحويل تنسيقات ملفات أخرى مثل EPUB و MD و PCL و XPS و PS و XML و LaTeX إلى مستند PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert other file formats to PDF in .NET",
    "alternativeHeadline": "Convert Multiple File Formats to PDF in C#",
    "abstract": "Aspose.PDF for .NET يقدم ميزة متعددة الاستخدامات تتيح للمستخدمين تحويل مجموعة من تنسيقات الملفات، بما في ذلك EPUB و Markdown و PCL و XPS و PS و XML و LaTeX، إلى مستندات PDF عالية الجودة. تعزز هذه الوظيفة إدارة المستندات من خلال ضمان التوافق والوصول عبر منصات مختلفة مع الحفاظ على سلامة المحتوى الأصلي",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "4627",
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
    "url": "/net/convert-other-files-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-other-files-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## نظرة عامة

تشرح هذه المقالة كيفية **تحويل أنواع مختلفة من تنسيقات الملفات إلى PDF باستخدام C#**. تغطي المواضيع التالية.

يعمل مقتطف الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

_التنسيق_: **EPUB**
- [C# تحويل EPUB إلى PDF](#csharp-convert-epub-to-pdf)
- [C# تحويل EPUB إلى PDF](#csharp-convert-epub-to-pdf)
- [C# كيفية تحويل ملف EPUB إلى PDF](#csharp-convert-epub-to-pdf)

_التنسيق_: **Markdown**
- [C# تحويل Markdown إلى PDF](#csharp-convert-markdown-to-pdf)
- [C# تحويل Markdown إلى PDF](#csharp-convert-markdown-to-pdf)
- [C# كيفية تحويل ملف Markdown إلى PDF](#csharp-convert-markdown-to-pdf)

_التنسيق_: **MD**
- [C# تحويل MD إلى PDF](#csharp-convert-md-to-pdf)
- [C# تحويل MD إلى PDF](#csharp-convert-md-to-pdf)
- [C# كيفية تحويل ملف MD إلى PDF](#csharp-convert-md-to-pdf)

_التنسيق_: **PCL**
- [C# تحويل PCL إلى PDF](#csharp-convert-pcl-to-pdf)
- [C# تحويل PCL إلى PDF](#csharp-convert-pcl-to-pdf)
- [C# كيفية تحويل ملف PCL إلى PDF](#csharp-convert-pcl-to-pdf)

_التنسيق_: **نص**
- [C# تحويل نص إلى PDF](#csharp-convert-text-to-pdf)
- [C# تحويل نص إلى PDF](#csharp-convert-text-to-pdf)
- [C# كيفية تحويل ملف نص إلى PDF](#csharp-convert-text-to-pdf)

_التنسيق_: **TXT**
- [C# تحويل TXT إلى PDF](#csharp-convert-txt-to-pdf)
- [C# تحويل TXT إلى PDF](#csharp-convert-txt-to-pdf)
- [C# كيفية تحويل ملف TXT إلى PDF](#csharp-convert-txt-to-pdf)

_التنسيق_: **نص عادي**
- [C# تحويل نص عادي إلى PDF](#csharp-convert-plain-text-to-pdf)
- [C# تحويل نص عادي إلى PDF](#csharp-convert-plain-text-to-pdf)
- [C# كيفية تحويل ملف نص عادي إلى PDF](#csharp-convert-plain-text-to-pdf)

_التنسيق_: **نص مُنسق مسبقًا**
- [C# تحويل نص مُنسق مسبقًا إلى PDF](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# تحويل نص مُنسق مسبقًا إلى PDF](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# كيفية تحويل ملف نص مُنسق مسبقًا إلى PDF](#csharp-convert-pre-formatted-txt-to-pdf)

_التنسيق_: **نص مسبق**
- [C# تحويل نص مسبق إلى PDF](#csharp-convert-pre-text-to-pdf)
- [C# تحويل نص مسبق إلى PDF](#csharp-convert-pre-text-to-pdf)
- [C# كيفية تحويل ملف نص مسبق إلى PDF](#csharp-convert-pre-text-to-pdf)

_التنسيق_: **XPS**
- [C# تحويل XPS إلى PDF](#csharp-convert-xps-to-pdf)
- [C# تحويل XPS إلى PDF](#csharp-convert-xps-to-pdf)
- [C# كيفية تحويل ملف XPS إلى PDF](#csharp-convert-xps-to-pdf)

## تحويل EPUB إلى PDF

**Aspose.PDF for .NET** يتيح لك ببساطة تحويل ملفات EPUB إلى تنسيق PDF.

<abbr title="نشر إلكتروني">EPUB</abbr> (اختصار للنشر الإلكتروني) هو معيار كتاب إلكتروني مجاني ومفتوح من منتدى النشر الرقمي الدولي (IDPF). الملفات لها امتداد .epub. تم تصميم EPUB لمحتوى قابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين.

يدعم EPUB أيضًا محتوى بتنسيق ثابت. التنسيق مخصص كتنسيق واحد يمكن للناشرين وبيوت التحويل استخدامه داخليًا، بالإضافة إلى التوزيع والبيع. يحل محل معيار Open eBook. النسخة EPUB 3 مدعومة أيضًا من قبل مجموعة دراسة صناعة الكتب (BISG)، وهي جمعية تجارية رائدة للكتب لأفضل الممارسات القياسية، والبحث، والمعلومات، والفعاليات، لتغليف المحتوى.

{{% alert color="success" %}}
**حاول تحويل EPUB إلى PDF عبر الإنترنت**

Aspose.PDF for .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["EPUB إلى PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF EPUB إلى PDF مع تطبيق مجاني](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>الخطوات:</em> تحويل EPUB إلى PDF في C#</strong></a>

1. إنشاء مثيل من فئة [EpubLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/epubloadoptions).
2. إنشاء مثيل من فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document) مع ذكر اسم ملف المصدر والخيارات.
3. حفظ المستند بالاسم المطلوب.

يظهر مقتطف الكود التالي كيفية تحويل ملفات EPUB إلى تنسيق PDF باستخدام C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertEPUBtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.EpubLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "EPUBToPDF.epub", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertEPUBtoPDF_out.pdf");
    }
}
```

يمكنك أيضًا تعيين حجم الصفحة للتحويل. لتحديد حجم صفحة جديدة، تحتاج إلى كائن `SizeF` وتمريره إلى مُنشئ [EpubLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/epubloadoptions/constructors/main).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertEPUBtoPDFAdv()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.EpubLoadOptions(new SizeF(1190, 1684));

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "EPUBToPDF.epub", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertEPUBtoPDFAdv_out.pdf");
    }
}
```

## تحويل Markdown إلى PDF

**تدعم هذه الميزة الإصدار 19.6 أو أعلى.**

{{% alert color="success" %}}
**حاول تحويل Markdown إلى PDF عبر الإنترنت**

Aspose.PDF for .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["Markdown إلى PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF Markdown إلى PDF مع تطبيق مجاني](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Aspose.PDF for .NET يوفر الوظيفة لإنشاء مستند PDF بناءً على ملف بيانات [Markdown](https://daringfireball.net/projects/markdown/syntax) المدخل. من أجل تحويل Markdown إلى PDF، تحتاج إلى تهيئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document) باستخدام [MdLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/mdloadoptions).

يظهر مقتطف الكود التالي كيفية استخدام هذه الوظيفة مع مكتبة Aspose.PDF:

<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>الخطوات:</em> تحويل Markdown إلى PDF في C#</strong></a> |
<a name="csharp-convert-md-to-pdf" id="csharp-convert-md-to-pdf"><strong><em>الخطوات:</em> تحويل MD إلى PDF في C#</strong></a>

1. إنشاء مثيل من فئة [MdLoadOptions ](https://reference.aspose.com/pdf/ar/net/aspose.pdf/mdloadoptions/) .
2. إنشاء مثيل من فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document) مع ذكر اسم ملف المصدر والخيارات.
3. حفظ المستند بالاسم المطلوب.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertMarkdownToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.MdLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.md", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertMarkdownToPDF_out.pdf");
    }
}
```

## تحويل PCL إلى PDF

<abbr title="لغة أوامر الطابعة">PCL</abbr> (لغة أوامر الطابعة) هي لغة طابعة تم تطويرها بواسطة Hewlett-Packard للوصول إلى ميزات الطابعة القياسية. تعتبر مستويات PCL من 1 إلى 5e/5c لغات قائمة على الأوامر تستخدم تسلسلات تحكم تتم معالجتها وتفسيرها بالترتيب الذي تم استلامها به. على مستوى المستهلك، يتم إنشاء تدفقات بيانات PCL بواسطة برنامج تشغيل الطباعة. يمكن أيضًا إنشاء مخرجات PCL بسهولة بواسطة تطبيقات مخصصة.

{{% alert color="success" %}}
**حاول تحويل PCL إلى PDF عبر الإنترنت**

Aspose.PDF لـ .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PCL إلى PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF PCL إلى PDF مع تطبيق مجاني](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**حاليًا، يتم دعم PCL5 والإصدارات الأقدم فقط**

<table>
    <thead>
        <tr>
            <th>
                مجموعات الأوامر
            </th>
            <th>
                الدعم
            </th>
            <th>
                الاستثناءات
            </th>
            <th>
                الوصف
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                أوامر التحكم في الوظائف
            </td>
            <td>
                +
            </td>
            <td>
                وضع الطباعة المزدوج
            </td>
            <td>
                التحكم في عملية الطباعة: عدد النسخ، صندوق الإخراج، الطباعة البسيطة/المزدوجة، الهوامش اليسرى والعلوية، إلخ.
            </td>
        </tr>
        <tr>
            <td>
                أوامر التحكم في الصفحة
            </td>
            <td>
                +
            </td>
            <td>
                أمر تخطي التثقيب
            </td>
            <td>
                تحديد حجم الصفحة، الهوامش، اتجاه الصفحة، المسافات بين الأسطر، المسافات بين الأحرف، إلخ.
            </td>
        </tr>
        <tr>
            <td>
                أوامر تحديد موضع المؤشر
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                تحديد موضع المؤشر وبالتالي، أصول النص، الصور النقطية أو المتجهة والتفاصيل.
            </td>
        </tr>
        <tr>
            <td>
                أوامر اختيار الخط
            </td>
            <td>
                +
            </td>
            <td>
                <ol>
                    <li>أمر بيانات الطباعة الشفافة.</li>
                    <li>الخطوط الناعمة المدمجة. في الإصدار الحالي بدلاً من إنشاء خط ناعم، تختار مكتبتنا خطًا مناسبًا من "الخطوط" TrueType المثبتة على الجهاز المستهدف. <br/>
                        يتم تحديد الملاءمة بواسطة نسبة العرض/الارتفاع.<br/>
                        تعمل هذه الميزة فقط مع الخطوط النقطية وخطوط TrueType ولا تضمن أن النص المطبوع باستخدام الخط الناعم سيكون مطابقًا للنص في ملف المصدر.<br/>
                        لأن رموز الأحرف في الخط الناعم قد لا تتطابق مع الرموز الافتراضية.
                    </li>
                    <li>مجموعات الرموز المعرفة من قبل المستخدم.</li>
                </ol>
            </td>
            <td>
                السماح بتحميل الخطوط الناعمة (المضمنة) من ملف PCL وإدارتها في الذاكرة.
            </td>
        </tr>
        <tr>
            <td>
                أوامر الرسوميات النقطية
            </td>
            <td>
                +
            </td>
            <td>
                فقط بالأبيض والأسود
            </td>
            <td>
                السماح بتحميل الصور النقطية من ملف PCL إلى الذاكرة، وتحديد معلمات النقطية. <br
                    > مثل العرض، الارتفاع، نوع الضغط، الدقة، إلخ.
            </td>
        </tr>
        <tr>
            <td>
                أوامر الألوان
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                السماح بتلوين جميع الكائنات القابلة للطباعة.
            </td>
        </tr>
        <tr>
            <td>
                أوامر نموذج الطباعة
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                السماح بملء النص، الصور النقطية والمناطق المستطيلة بنمط نقطي محدد مسبقًا و <br>
                أنماط معرفة من قبل المستخدم، وتحديد وضع الشفافية للأنماط وصورة النقطية المصدر. <br> الأنماط المحددة مسبقًا هي الأنماط المتقاطعة، والتظليل.
            </td>
        </tr>
        <tr>
            <td>
                أوامر ملء منطقة مستطيلة
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                السماح بإنشاء وملء المناطق المستطيلة بأنماط.
            </td>
        </tr>
        <tr>
            <td>
                أوامر الرسوميات المتجهة HP-GL/2
            </td>
            <td>
                +
            </td>
            <td>
                أمر الرسوميات المتجهة المصفاة (SV)، أمر وضع الشفافية (TR)، أمر بيانات الشفافية (TD)، RO
                (تدوير نظام الإحداثيات)، أمر الخطوط القابلة للتعديل أو النقطية (SB)، أمر ميل الأحرف (SL) و
                المساحة الإضافية (ES) لم يتم تنفيذها وأوامر DV (تحديد مسار النص المتغير) تم تنفيذها في
                الإصدار التجريبي.
            </td>
            <td>
                السماح بتحميل صور HP-GL/2 المتجهة من ملف PCL إلى الذاكرة. تحتوي الصورة المتجهة على أصل في الزاوية السفلى اليسرى من منطقة الطباعة، ويمكن تغيير حجمها، وترجمتها، وتدويرها، وقصها. <br>
                يمكن أن تحتوي الصورة المتجهة على نص، كعلامات، وأشكال هندسية مثل
                المستطيل، الدائرة، البيضاوي، الخط، القوس، منحنى بيزييه والأشكال المعقدة المكونة من الأشكال البسيطة. <br> يمكن ملء الأشكال المغلقة بما في ذلك أحرف العلامات بالتعبئة الصلبة أو نمط متجه. <br> يمكن أن يكون النمط
                متقاطعًا، متقاطعًا، تظليلًا، نقطيًا معرفة من قبل المستخدم، تظليل PCL أو متقاطع PCL ونمط معرفة من قبل المستخدم. أنماط PCL هي نقطية. يمكن تدوير العلامات بشكل فردي، وتغيير حجمها، وتوجيهها في
                أربع اتجاهات: لأعلى، لأسفل، لليسار ولليمين. تشمل الاتجاهات اليسرى واليمنى ترتيب الأحرف واحدًا تلو الآخر. تشمل الاتجاهات لأعلى ولأسفل ترتيب الأحرف واحدًا تحت الآخر.
            </td>
        </tr>
        <tr>
            <td>
                الماكرو
            </td>
            <td>
                ―
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                السماح بتحميل تسلسل من أوامر PCL إلى الذاكرة واستخدام هذا التسلسل عدة مرات، على سبيل المثال،
                لطباعة رأس الصفحة أو تعيين تنسيق واحد لمجموعة من الصفحات.
            </td>
        </tr>
        <tr>
            <td>
                نص Unicode
            </td>
            <td>
                ―
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                السماح بطباعة الأحرف غير ASCII. لم يتم تنفيذها بسبب نقص ملفات عينة مع <br
                    > نص Unicode
            </td>
        </tr>
        <tr>
            <td>
                PCL6 (PCL-XL)
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                تم تنفيذها فقط في الإصدار التجريبي بسبب نقص في ملفات الاختبار. الخطوط المدمجة أيضًا غير
                مدعومة.<br> امتداد JetReady غير مدعوم لأنه من المستحيل الحصول على مواصفات JetReady.
            </td>
            <td>
                تنسيق ملف ثنائي.
            </td>
        </tr>
    </tbody>
</table>

### تحويل ملف PCL إلى تنسيق PDF

للسماح بالتحويل من PCL إلى PDF، تحتوي Aspose.PDF على فئة [`PclLoadOptions`](https://reference.aspose.com/pdf/ar/net/aspose.pdf/pclloadoptions) التي تُستخدم لتهيئة كائن LoadOptions. لاحقًا، يتم تمرير هذا الكائن كوسيط أثناء تهيئة كائن Document ويساعد محرك عرض PDF في تحديد تنسيق الإدخال لمستند المصدر.

يظهر مقتطف الكود التالي عملية تحويل ملف PCL إلى تنسيق PDF.

<a name="csharp-convert-pcl-to-pdf" id="csharp-convert-pcl-to-pdf"><strong><em>الخطوات:</em> تحويل PCL إلى PDF في C#</strong></a>

1. إنشاء مثيل من فئة [PclLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/pclloadoptions/) .
2. إنشاء مثيل من فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/) مع ذكر اسم ملف المصدر والخيارات.
3. حفظ المستند بالاسم المطلوب.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPCLtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.PclLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPCLtoPDF.pcl", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertPCLtoPDF_out.pdf");
    }
}
```

يمكنك أيضًا مراقبة اكتشاف الأخطاء أثناء عملية التحويل. للقيام بذلك، تحتاج إلى تكوين كائن PclLoadOptions: تعيين أو إلغاء تعيين SupressErrors.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPCLtoPDFAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.PclLoadOptions { SupressErrors = true };

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPCLtoPDFAdvanced.pcl", options))
    {
        if (options.Exceptions != null)
        {
            foreach (var ex in options.Exceptions)
            {
                Console.WriteLine(ex.Message);
            }
        }
        // Save PDF document
        document.Save(dataDir + "ConvertPCLtoPDFAdvanced_out.pdf");
    }
}
```

### المشكلات المعروفة

1. قد يختلف أصل سلاسل النصوص والصور قليلاً عن تلك الموجودة في ملف PCL المصدر إذا كانت اتجاه الطباعة ليست 0°. ينطبق نفس الشيء على الصور المتجهة إذا تم تدوير نظام الإحداثيات لرسم المتجه (تم تقديم أمر RO).
2. قد يختلف أصل العلامات في الصور المتجهة عن تلك الموجودة في ملف PCL المصدر إذا تأثرت العلامات بتسلسل من الأوامر: أصل العلامة (LO)، تحديد مسار النص المتغير (DV)، الاتجاه المطلق (DI) أو الاتجاه النسبي (DR).
3. قد يتم قراءة النص بشكل غير صحيح إذا كان يجب أن يتم عرضه باستخدام خط ناعم (مضمن) نقطي أو TrueType، لأن هذه الخطوط مدعومة حاليًا جزئيًا فقط (انظر الاستثناءات في "جدول الميزات المدعومة"). في هذه الحالة، يمكن قراءة النص بشكل صحيح فقط إذا كانت رموز الأحرف في الخط الناعم تتوافق مع الرموز الافتراضية. قد يختلف نمط النص المقروء أيضًا عن النمط في ملف PCL المصدر لأنه ليس من الضروري تعيين النمط في رأس الخط الناعم.
4. إذا كان ملف PCL الذي تم تحليله يحتوي على خطوط ناعمة Intellifont أو Universal، سيتم طرح استثناء، لأن خطوط Intellifont وUniversal غير مدعومة على الإطلاق.
5. إذا كان ملف PCL الذي تم تحليله يحتوي على أوامر ماكرو، فإن نتيجة التحليل ستختلف بشكل كبير عن ملف المصدر، لأن أوامر الماكرو غير مدعومة.

## تحويل النص إلى PDF

**Aspose.PDF for .NET** تدعم ميزة تحويل النص العادي وملف النص المُنسق مسبقًا إلى تنسيق PDF.

تحويل النص إلى PDF يعني إضافة مقاطع نصية إلى صفحة PDF. بالنسبة لملفات النص، نتعامل مع نوعين من النص: التنسيق المسبق (على سبيل المثال، 25 سطرًا مع 80 حرفًا في السطر) والنص غير المنسق (نص عادي). اعتمادًا على احتياجاتنا، يمكننا التحكم في هذه الإضافة بأنفسنا أو تركها لخوارزميات المكتبة.

{{% alert color="success" %}}
**حاول تحويل النص إلى PDF عبر الإنترنت**

Aspose.PDF for .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["نص إلى PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF النص إلى PDF مع تطبيق مجاني](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### تحويل ملف نص عادي إلى PDF

في حالة ملف النص العادي، يمكننا استخدام التقنية التالية:

<a name="csharp-convert-text-to-pdf" id="csharp-convert-text-to-pdf"><strong><em>الخطوات:</em> تحويل النص إلى PDF في C#</strong></a> |
<a name="csharp-convert-txt-to-pdf" id="csharp-convert-txt-to-pdf"><strong><em>الخطوات:</em> تحويل TXT إلى PDF في C#</strong></a> |
<a name="csharp-convert-plain-text-to-pdf" id="csharp-convert-plain-text-to-pdf"><strong><em>الخطوات:</em> تحويل النص العادي إلى PDF في C#</strong></a>

1. استخدم _TextReader_ لقراءة النص بالكامل.
2. إنشاء كائن [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/) وإضافة صفحة جديدة في مجموعة Pages.
3. إنشاء كائن جديد من [TextFragment](https://reference.aspose.com/pdf/ar/net/aspose.pdf.text/textfragment/) وتمرير كائن _TextReader_ إلى مُنشئه.
4. إضافة كائن _TextFragment_ كفقرة في مجموعة _Paragraphs_. إذا كانت كمية النص أكبر من الصفحة، تضيف خوارزمية المكتبة صفحات إضافية تلقائيًا.
5. استخدم طريقة **Save** من فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/) .

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPlainTextFileToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Read the source text file
    using (var streamReader = new StreamReader(dataDir + "TextToPDFInput.txt"))
    {
        // // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();
            // Create an instance of TextFragment and pass the text from reader object to its constructor as argument
            var text = new Aspose.Pdf.Text.TextFragment(streamReader.ReadToEnd());
            // Add a new text paragraph in paragraphs collection and pass the TextFragment object
            page.Paragraphs.Add(text);
            // Save PDF document
            document.Save(dataDir + "TextToPDF_out.pdf");
        }
    }
}
```

### تحويل ملف نص مُنسق مسبقًا إلى PDF

تحويل النص المُنسق مسبقًا يشبه النص العادي ولكن تحتاج إلى اتخاذ بعض الإجراءات الإضافية مثل تعيين الهوامش، ونوع الخط وحجمه. من الواضح أن الخط يجب أن يكون أحادي المسافة (على سبيل المثال Courier New).

اتبع هذه الخطوات لتحويل النص المُنسق مسبقًا إلى PDF باستخدام C#:

<a name="csharp-convert-pre-text-to-pdf" id="csharp-convert-pre-text-to-pdf"><strong><em>الخطوات:</em> تحويل النص المسبق إلى PDF في C#</strong></a> |
<a name="csharp-convert-pre-formatted-txt-to-pdf" id="csharp-convert-pre-formatted-txt-to-pdf"><strong><em>الخطوات:</em> تحويل TXT المُنسق مسبقًا إلى PDF في C#</strong></a>

1. قراءة النص بالكامل كمصفوفة من السلاسل.
2. إنشاء كائن [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/) وإضافة صفحة جديدة في مجموعة [Pages](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/pages/) .
3. تشغيل حلقة عبر مصفوفة السلاسل وإضافة كل سلسلة كفقرة في مجموعة [Paragraphs](https://reference.aspose.com/pdf/ar/net/aspose.pdf/paragraphs/) .

في هذه الحالة، تضيف خوارزمية المكتبة أيضًا صفحات إضافية، ولكن يمكننا التحكم في هذه العملية بأنفسنا.
يظهر المثال التالي كيفية تحويل ملف نص مُنسق مسبقًا إلى مستند PDF بحجم صفحة A4.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPreFormattedTextToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Read the text file as array of string
    var lines = File.ReadAllLines(dataDir + "ConvertPreFormattedTextToPdf.txt");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Set left and right margins for better presentation
        page.PageInfo.Margin.Left = 20;
        page.PageInfo.Margin.Right = 10;
        page.PageInfo.DefaultTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier New");
        page.PageInfo.DefaultTextState.FontSize = 12;

        foreach (var line in lines)
        {
            // check if line contains "form feed" character
            // see https://en.wikipedia.org/wiki/Page_break
            if (line.StartsWith("\x0c"))
            {
                page = document.Pages.Add();
                page.PageInfo.Margin.Left = 20;
                page.PageInfo.Margin.Right = 10;
                page.PageInfo.DefaultTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier New");
                page.PageInfo.DefaultTextState.FontSize = 12;
            }
            else
            {
                // Create an instance of TextFragment and pass the line to its constructor as argument
                var text = new Aspose.Pdf.Text.TextFragment(line);
                // Add a new text paragraph in paragraphs collection and pass the TextFragment object
                page.Paragraphs.Add(text);
            }
        }
        // Save PDF document
        document.Save(dataDir + "PreFormattedTextToPDF_out.pdf");
    }
}
```

## تحويل XPS إلى PDF

**Aspose.PDF for .NET** تدعم ميزة تحويل <abbr title="مواصفة الورق XML">XPS</abbr> إلى تنسيق PDF. تحقق من هذه المقالة لحل مهامك.

نوع ملف XPS مرتبط بشكل أساسي بمواصفة الورق XML من شركة Microsoft. مواصفة الورق XML (XPS)، التي كانت تُعرف سابقًا باسم Metro وتحتوي على مفهوم مسار الطباعة للجيل التالي (NGPP)، هي مبادرة Microsoft لدمج إنشاء المستندات وعرضها في نظام التشغيل Windows.

{{% alert color="primary" %}}

تنسيق الملف هو في الأساس ملف XML مضغوط يُستخدم بشكل أساسي للتوزيع والتخزين. من الصعب جدًا تحريره وغالبًا ما يتم تنفيذه بواسطة Microsoft.

{{% /alert %}}

لتحويل XPS إلى PDF باستخدام Aspose.PDF for .NET، قدمنا فئة تُسمى [XpsLoadOption](https://reference.aspose.com/pdf/ar/net/aspose.pdf/xpsloadoptions) التي تُستخدم لتهيئة كائن [LoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/loadoptions) . لاحقًا، يتم تمرير هذا الكائن كوسيط أثناء تهيئة كائن Document ويساعد محرك عرض PDF في تحديد تنسيق الإدخال لمستند المصدر.

{{% alert color="primary" %}}

في كل من XP و Windows 7، يجب أن تجد طابعة XPS مثبتة مسبقًا إذا نظرت في لوحة التحكم ثم الطابعات. لإنشاء هذه الملفات، يمكنك استخدام تلك الطابعة كجهاز إخراج. في Windows 7، يجب أن تكون قادرًا على النقر نقرًا مزدوجًا على الملف لفتحه في عارض XPS. يمكنك أيضًا تنزيل عارض XPS من موقع Microsoft على الويب.

{{% /alert %}}

يظهر مقتطف الكود التالي عملية تحويل ملف XPS إلى تنسيق PDF باستخدام C#.

<a name="csharp-convert-xps-to-pdf" id="csharp-convert-xps-to-pdf"><strong><em>الخطوات:</em> تحويل XPS إلى PDF في C#</strong></a>

1. إنشاء مثيل من فئة [XpsLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/xpsloadoptions/) .
2. إنشاء مثيل من فئة [Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/) مع ذكر اسم ملف المصدر والخيارات.
3. حفظ المستند بتنسيق PDF بالاسم المطلوب.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertXPSToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Instantiate Options object
    var options = new Aspose.Pdf.XpsLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "XPSToPDF.xps", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertXPSToPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**حاول تحويل تنسيق XPS إلى PDF عبر الإنترنت**

Aspose.PDF for .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["XPS إلى PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF XPS إلى PDF مع تطبيق مجاني](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## تحويل PostScript إلى PDF

**Aspose.PDF for .NET** تدعم ميزات تحويل ملفات PostScript إلى تنسيق PDF. واحدة من الميزات من Aspose.PDF هي أنه يمكنك تعيين مجموعة من مجلدات الخطوط التي سيتم استخدامها أثناء التحويل.

لتحويل ملف PostScript إلى تنسيق PDF، تقدم Aspose.PDF for .NET فئة [PsLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/psloadoptions) التي تُستخدم لتهيئة كائن LoadOptions. لاحقًا، يمكن تمرير هذا الكائن كوسيط إلى مُنشئ كائن Document، مما سيساعد محرك عرض PDF في تحديد تنسيق مستند المصدر.

يمكن استخدام مقتطف الكود التالي لتحويل ملف PostScript إلى تنسيق PDF باستخدام Aspose.PDF for .NET:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPostScriptToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new PsLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPostscriptInput.ps", options))
    {
        // Save PDF document
        document.Save(dataDir + "PSToPDF_out.pdf");
    }
}
```

بالإضافة إلى ذلك، يمكنك تعيين مجموعة من مجلدات الخطوط التي سيتم استخدامها أثناء التحويل:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPostscriptToPDFAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options with custom font folders
    var options = new Aspose.Pdf.PsLoadOptions
    {
        FontsFolders = new[] { dataDir + @"\fonts1", dataDir + @"\fonts2" }
    };

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPostscriptInput.ps", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertPostscriptToPDFAdvanced_out.pdf");
    }
}
```

## تحويل XML إلى PDF

يستخدم تنسيق XML لتخزين البيانات المهيكلة. هناك عدة طرق لتحويل <abbr title="لغة ترميز قابلة للتوسع">XML</abbr> إلى PDF في Aspose.PDF:

1. تحويل أي بيانات XML إلى HTML باستخدام XSLT وتحويل HTML إلى PDF كما هو موضح أدناه.
2. إنشاء مستند XML باستخدام مخطط XSD من Aspose.PDF.
3. استخدام مستند XML بناءً على معيار XSL-FO.

{{% alert color="success" %}}
**حاول تحويل XML إلى PDF عبر الإنترنت**

Aspose.PDF for .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["XML إلى PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF XML إلى PDF مع تطبيق مجاني](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}


## تحويل XSL-FO إلى PDF

يمكن تنفيذ تحويل ملفات XSL-FO إلى PDF باستخدام التقنية التقليدية من Aspose.PDF - إنشاء كائن [Document](https://reference.aspose.com/page/net/aspose.page/document) مع [XslFoLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/xslfoloadoptions). ولكن في بعض الأحيان يمكنك مواجهة هيكل ملف غير صحيح. في هذه الحالة، يسمح محول XSL-FO بتعيين استراتيجية معالجة الأخطاء. يمكنك اختيار `ThrowExceptionImmediately`، `TryIgnore` أو `InvokeCustomHandler`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Convert_XSLFO_to_PDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "XSLFOToPdfInput.xslt");
    // Set error handling strategy
    options.ParsingErrorsHandlingType = Aspose.Pdf.XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "XSLFOToPdfInput.xml", options))
    {
        // Save PDF document
        document.Save(dataDir + "XSLFOToPdf_out.pdf");
    }
}
```

## تحويل LaTeX/TeX إلى PDF

تنسيق ملف LaTeX هو تنسيق ملف نصي مع ترميز في مشتق LaTeX من عائلة لغات TeX و LaTeX هو تنسيق مشتق من نظام TeX. LaTeX (ˈleɪtɛk/lay-tek أو lah-tek) هو نظام إعداد مستندات ولغة ترميز مستندات. يُستخدم على نطاق واسع في التواصل ونشر المستندات العلمية في العديد من المجالات، بما في ذلك الرياضيات والفيزياء وعلوم الكمبيوتر. كما أن له دورًا بارزًا في إعداد ونشر الكتب والمقالات التي تحتوي على مواد متعددة اللغات معقدة، مثل السنسكريتية والعربية، بما في ذلك الإصدارات النقدية. يستخدم LaTeX برنامج تنسيق TeX لتنسيق مخرجاته، وهو مكتوب بنفسه بلغة ماكرو TeX.

{{% alert color="success" %}}
**حاول تحويل LaTeX/TeX إلى PDF عبر الإنترنت**

Aspose.PDF for .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["LaTex إلى PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل Aspose.PDF LaTeX/TeX إلى PDF مع تطبيق مجاني](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Aspose.PDF for .NET تدعم ميزة تحويل ملفات TeX إلى تنسيق PDF ومن أجل تحقيق هذا المتطلب، تحتوي مساحة أسماء Aspose.Pdf على فئة تُسمى [LatexLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/latexloadoptions) التي توفر القدرات لتحميل ملفات LaTex وعرض المخرجات بتنسيق PDF باستخدام [فئة Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document).
يظهر مقتطف الكود التالي عملية تحويل ملف LaTex إلى تنسيق PDF باستخدام C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertTeXtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.TeXLoadOptions();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "samplefile.tex", options))
    {
        // Save PDF document
        document.Save(dataDir + "TeXToPDF_out.pdf");
    }
}
```

## تحويل OFD إلى PDF

يشير تنسيق OFD إلى "مستند ثابت مفتوح"، الذي تم تأسيسه كمعيار وطني للصين لتخزين الملفات الإلكترونية، ويستخدم كبديل للتنسيق الشائع PDF. يدعم مستندات بتنسيق ثابت، مما يضمن عرضًا متسقًا عبر منصات مختلفة. تُستخدم ملفات OFD لأغراض متنوعة، بما في ذلك المستندات الرقمية وتطبيقات الأعمال.

Aspose.PDF for .NET تدعم ميزة تحويل ملفات OFD إلى تنسيق PDF ومن أجل تحقيق هذا المتطلب، تحتوي مساحة أسماء Aspose.Pdf على فئة تُسمى [OfdLoadOptions](https://reference.aspose.com/pdf/ar/net/aspose.pdf/ofdloadoptions/) التي توفر القدرات لتحميل ملفات OFD وعرض المخرجات بتنسيق PDF باستخدام [فئة Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document).

يظهر مقتطف الكود التالي عملية تحويل ملف OFD إلى تنسيق PDF باستخدام C#. 

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertOFDToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.OfdLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertOFDToPDF.ofd", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertOFDToPDF_out.pdf");
    }
}
```