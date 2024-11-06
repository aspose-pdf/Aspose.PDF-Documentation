---
title: تحويل صيغ الملفات الأخرى إلى PDF في .NET
linktitle: تحويل صيغ الملفات الأخرى إلى PDF
type: docs
weight: 80
url: ar/net/convert-other-files-to-pdf/
lastmod: "2021-11-01"
description: يوضح هذا الموضوع كيف يتيح Aspose.PDF تحويل صيغ ملفات أخرى مثل EPUB، MD، PCL، XPS، PS، XML و LaTeX إلى مستند PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## نظرة عامة

يشرح هذا المقال كيفية **تحويل أنواع مختلفة من صيغ الملفات إلى PDF باستخدام C#**. يغطي المواضيع التالية.

يعمل الشفرة البرمجية التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

_الصيغة_: **EPUB**
- [C# EPUB إلى PDF](#csharp-convert-epub-to-pdf)
- [C# تحويل EPUB إلى PDF](#csharp-convert-epub-to-pdf)
- [C# كيفية تحويل ملف EPUB إلى PDF](#csharp-convert-epub-to-pdf)

_الصيغة_: **Markdown**
- [C# Markdown إلى PDF](#csharp-convert-markdown-to-pdf)
- [C# تحويل Markdown إلى PDF](#csharp-convert-markdown-to-pdf)
- [C# كيفية تحويل ملف Markdown إلى PDF](#csharp-convert-markdown-to-pdf)
- [C# كيفية تحويل ملف Markdown إلى PDF](#csharp-convert-markdown-to-pdf)

_التنسيق_: **MD**
- [C# MD إلى PDF](#csharp-convert-md-to-pdf)
- [C# تحويل MD إلى PDF](#csharp-convert-md-to-pdf)
- [C# كيفية تحويل ملف MD إلى PDF](#csharp-convert-md-to-pdf)

_التنسيق_: **PCL**
- [C# PCL إلى PDF](#csharp-convert-pcl-to-pdf)
- [C# تحويل PCL إلى PDF](#csharp-convert-pcl-to-pdf)
- [C# كيفية تحويل ملف PCL إلى PDF](#csharp-convert-pcl-to-pdf)

_التنسيق_: **Text**
- [C# Text إلى PDF](#csharp-convert-text-to-pdf)
- [C# تحويل Text إلى PDF](#csharp-convert-text-to-pdf)
- [C# كيفية تحويل ملف Text إلى PDF](#csharp-convert-text-to-pdf)

_التنسيق_: **TXT**
- [C# TXT إلى PDF](#csharp-convert-txt-to-pdf)
- [C# تحويل TXT إلى PDF](#csharp-convert-txt-to-pdf)
- [C# كيفية تحويل ملف TXT إلى PDF](#csharp-convert-txt-to-pdf)

_التنسيق_: **Plain Text**
- [C# Plain Text إلى PDF](#csharp-convert-plain-text-to-pdf)
- [C# تحويل Plain Text إلى PDF](#csharp-convert-plain-text-to-pdf)
- [C# كيفية تحويل ملف Plain Text إلى PDF](#csharp-convert-plain-text-to-pdf)
- [C# كيفية تحويل ملف نص بسيط إلى PDF](#csharp-convert-plain-text-to-pdf)

_التنسيق_: **نص مُنسق مُسبقًا**
- [C# تحويل النص المُنسق مُسبقًا إلى PDF](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# تحويل النص المُنسق مُسبقًا إلى PDF](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# كيفية تحويل ملف نص مُنسق مُسبقًا إلى PDF](#csharp-convert-pre-formatted-txt-to-pdf)

_التنسيق_: **نص مُعد مُسبقًا**
- [C# تحويل النص المُعد مُسبقًا إلى PDF](#csharp-convert-pre-text-to-pdf)
- [C# تحويل النص المُعد مُسبقًا إلى PDF](#csharp-convert-pre-text-to-pdf)
- [C# كيفية تحويل ملف نص مُعد مُسبقًا إلى PDF](#csharp-convert-pre-text-to-pdf)

_التنسيق_: **XPS**
- [C# تحويل XPS إلى PDF](#csharp-convert-xps-to-pdf)
- [C# تحويل XPS إلى PDF](#csharp-convert-xps-to-pdf)
- [C# كيفية تحويل ملف XPS إلى PDF](#csharp-convert-xps-to-pdf)

## تحويل EPUB إلى PDF

**Aspose.PDF لـ .NET** يتيح لك تحويل ملفات EPUB إلى تنسيق PDF بسهولة.

<abbr title="النشر الإلكتروني">EPUB</abbr> (اختصار للنشر الإلكتروني) هو معيار كتاب إلكتروني مجاني ومفتوح من منتدى النشر الرقمي الدولي (IDPF).
<abbr title="النشر الإلكتروني">EPUB</abbr> (اختصار للنشر الإلكتروني) هو معيار مفتوح ومجاني للكتب الإلكترونية من المنتدى الدولي للنشر الرقمي (IDPF).

يدعم EPUB أيضًا المحتوى ذو التنسيق الثابت. يُقصد بالتنسيق أن يكون تنسيقًا وحيدًا يمكن للناشرين وبيوت التحويل استخدامه داخليًا، بالإضافة إلى استخدامه للتوزيع والبيع. يحل محل معيار الكتاب الإلكتروني المفتوح. كما يدعم الإصدار EPUB 3 من قِبل مجموعة دراسة صناعة الكتب (BISG)، وهي جمعية تجارية رائدة للممارسات الأفضل الموحدة، والبحوث، والمعلومات والأحداث، لتغليف المحتوى.

{{% alert color="success" %}}
**جرب تحويل EPUB إلى PDF عبر الإنترنت**

يقدم لك Aspose.PDF لـ .NET تطبيقًا مجانيًا عبر الإنترنت ["EPUB إلى PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)، حيث يمكنك تجربة استكشاف الوظائف وجودة عمله.

[![Aspose.PDF تحويل EPUB إلى PDF بتطبيق مجاني](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>الخطوات:</em> تحويل EPUB إلى PDF في C#</strong></a>
<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>الخطوات:</em> تحويل EPUB إلى PDF باستخدام C#</strong></a>

1. إنشاء مثيل من الفئة [EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions).
2. إنشاء مثيل من الفئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) مع ذكر اسم الملف المصدر والخيارات.
3. حفظ المستند بالاسم المطلوب للملف.

الكود التالي يوضح كيفية تحويل ملفات EPUB إلى صيغة PDF باستخدام C#.

```csharp
public static void ConvertEPUBtoPDF()
{
    EpubLoadOptions option = new EpubLoadOptions();
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```

يمكنك أيضاً تحديد حجم الصفحة للتحويل. لتعريف حجم صفحة جديد استخدم كائن `SizeF` وأمرره إلى مُنشئ [EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions/constructors/main).

```csharp
public static void ConvertEPUBtoPDFAdv()
{
    EpubLoadOptions option = new EpubLoadOptions(new SizeF(1190, 1684));
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```
## تحويل Markdown إلى PDF

**هذه الميزة مدعومة بواسطة الإصدار 19.6 أو أعلى.**

{{% alert color="success" %}}
**جرب تحويل Markdown إلى PDF عبر الإنترنت**

يقدم Aspose.PDF لـ .NET تطبيقًا مجانيًا عبر الإنترنت ["Markdown إلى PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF Markdown إلى PDF بواسطة تطبيق مجاني](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

يوفر Aspose.PDF لـ .NET الوظيفة لإنشاء مستند PDF استنادًا إلى ملف بيانات Markdown الذي تم إدخاله. لتحويل Markdown إلى PDF، تحتاج إلى تهيئة [المستند](https://reference.aspose.com/pdf/net/aspose.pdf/document) باستخدام [MdLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions).

يوضح الجزء التالي من الكود كيفية استخدام هذه الوظيفة مع مكتبة Aspose.PDF:

<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>الخطوات:</em> تحويل Markdown إلى PDF في C#</strong></a> |
<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>الخطوات:</em> تحويل Markdown إلى PDF في C#</strong></a> |
<a name="csharp-convert-md-to-pdf" id="csharp-convert-md-to-pdf"><strong><em>الخطوات:</em> تحويل MD إلى PDF في C#</strong></a>

1. قم بإنشاء نموذج من فئة [MdLoadOptions ](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions/).
2. قم بإنشاء نموذج من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) مع تحديد اسم الملف المصدر والخيارات.
3. احفظ المستند بالاسم المطلوب للملف.

```csharp
// مسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// فتح مستند Markdown
Document pdfDocument= new Document(dataDir + "sample.md", new MdLoadOptions());
// حفظ المستند بصيغة PDF
pdfDocument.Save(dataDir + "MarkdownToPDF.pdf");
```

## تحويل PCL إلى PDF

<abbr title="Printer Command Language">PCL</abbr> (لغة أوامر الطابعة) هي لغة طابعة طورتها شركة Hewlett-Packard للوصول إلى الميزات القياسية للطابعة.
<abbr title="لغة تحكم الطابعة">PCL</abbr> (لغة تحكم الطابعة) هي لغة طابعة تم تطويرها بواسطة هيوليت باكارد للوصول إلى ميزات الطابعة القياسية.

{{% alert color="success" %}}
**حاول تحويل PCL إلى PDF عبر الإنترنت**

تقدم لك Aspose.PDF لـ .NET تطبيقًا مجانيًا عبر الإنترنت ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF PCL إلى PDF بتطبيق مجاني](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**حاليًا فقط يتم دعم PCL5 والإصدارات الأقدم**

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
                أوامر التحكم في المهام

        <tr>
            <td>
                أوامر التحكم في الوظائف
            </td>
            <td>
                +
            </td>
            <td>
                وضع الطباعة الثنائية
            </td>
            <td>
                التحكم في عملية الطباعة: عدد النسخ، صندوق الخروج، طباعة بسيطة/ثنائية، الإزاحات اليسرى والعلوية وغيرها.
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
                تحديد حجم الصفحة، الهوامش، توجيه الصفحة، المسافات بين السطور، المسافات بين الأحرف وغيرها.
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
                تحديد موضع المؤشر وبالتالي أصول النصوص، الصور النقطية أو الصور المتجهة والتفاصيل.
            </td>
        </tr>
```

<tr>
    <td>
        تحديد موقع المؤشر وبالتالي مصادر النصوص، والصور النقطية أو الصور المتجهة والتفاصيل.
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
            <li>أمر طباعة البيانات الشفافة.</li>
            <li>الخطوط الناعمة المضمنة. في النسخة الحالية بدلاً من إنشاء خط ناعم، تختار مكتبتنا
                خطًا مناسبًا من الخطوط الصلبة الموجودة من نوع TrueType والمثبتة على جهاز الهدف. <br/>
                يتم تحديد الملاءمة بناءً على نسبة العرض إلى الارتفاع.<br/>
                هذه الميزة تعمل فقط لخطوط Bitmap وTrueType ولا
                تضمن أن النص المطبوع بالخط الناعم سيكون مطابقًا للنص الموجود في الملف المصدر.<br/>
                لأن رموز الأحرف في الخط الناعم قد لا تتطابق مع الرموز الافتراضية.
            </li>
            <li>مجموعات الرموز المعرفة من قبل المستخدم.</li>
        </ol>
    </td>
</tr>
```

<li>مجموعات الرموز المُعرّفة من قبل المستخدم.</li>
</ol>
</td>
<td>
السماح بتحميل الخطوط اللينة (المضمنة) من ملف PCL وإدارتها في الذاكرة.
</td>
</tr>
<tr>
<td>
أوامر الرسومات النقطية
</td>
<td>
+
</td>
<td>
أبيض وأسود فقط
</td>
<td>
السماح بتحميل الصور النقطية من ملف PCL إلى الذاكرة، تحديد معاملات النقطية. <br
> مثل العرض، الارتفاع، نوع الضغط، الدقة إلخ.
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
السماح بالتلوين لجميع الكائنات القابلة للطباعة.
</td>
</tr>
<tr>
<td>
أوامر نموذج الطباعة
```

                 أوامر طباعة النموذج
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                تسمح بملء النصوص والصور النقطية والمناطق المستطيلة بأنماط نقطية محددة مسبقًا وأنماط معرفة من المستخدم وتحديد وضع الشفافية للأنماط و
                صورة نقطية مصدر. <br> الأنماط المحددة مسبقًا هي الهاتشينج، الكروس-هاتش
                والتظليل.
            </td>
        </tr>
        <tr>
            <td>
                أوامر ملء منطقة المستطيل
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                تسمح بإنشاء وملء المناطق المستطيلة بالأنماط.
            </td>
        </tr>
        <tr>
            <td>
                أوامر الرسومات البيانية الناقلة HP-GL/2
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                أمر الرسم الناقل المغطى (SV)، أمر وضع الشفافية (TR)، أمر البيانات الشفافة (TD)، RO
```
```
أمر Vector المفحوص (SV)، أمر وضع الشفافية (TR)، أمر البيانات الشفافة (TD)، RO
(تدوير نظام الإحداثيات)، أمر الخطوط المتغيرة أو البتماب (SB)، أمر ميل الحروف (SL) و
مسافة إضافية (ES) غير مطبقة وأوامر DV (تعريف مسار النص المتغير) محققة في
نسخة تجريبية.
```
```
تتيح تحميل صور HP-GL/2 الناقلية من ملف PCL إلى الذاكرة. تمتلك الصورة الناقلية نقطة أصل في الزاوية السفلية اليسرى من المنطقة القابلة للطباعة، يمكن تحجيمها، ترجمتها، تدويرها وقصها. <br>
يمكن أن تحتوي الصورة الناقلية على نص، كما في التسميات، وأشكال هندسية مثل المستطيل، الدائرة، البيضوية، الخط، القوس، منحنى بيزييه وأشكال معقدة مكونة من البسيطة. <br> يمكن ملء الأشكال المغلقة بما في ذلك حروف التسميات بملء صلب أو نمط ناقل. <br> يمكن أن يكون النمط
التظليل،&nbsp;التقاطع، التظليل، الراستر المحدد من قبل المستخدم، تقاطع PCL أو تظليل وتقاطع PCL
```

<tr>
    <td>
        الفقس، التظليل المتقاطع، التظليل، النقش المحدد من قبل المستخدم، الفقس بـ PCL أو التظليل المتقاطع و PCL
        المحدد من قبل المستخدم. الأنماط في PCL هي نقش. يمكن تدوير العلامات وتكبيرها وتوجيهها بشكل فردي في
        أربع اتجاهات: لأعلى، لأسفل، لليسار، ولليمين. الاتجاهان اليسار واليمين يتضمنان ترتيب الحروف واحدة تلو الأخرى.
        الاتجاهان لأعلى ولأسفل يتضمنان ترتيب الحروف واحدة تحت الأخرى.
    </td>
</tr>
<tr>
    <td>
        ماكرو
    </td>
    <td>
        ―
    </td>
    <td>
        &nbsp;
    </td>
    <td>
        يسمح بتحميل تسلسل من أوامر PCL إلى الذاكرة واستخدام هذا التسلسل عدة مرات، على سبيل المثال،
        لطباعة رأس الصفحة أو تعيين تنسيق واحد لمجموعة من الصفحات.
    </td>
</tr>
<tr>
    <td>
        نص يونيكود
    </td>
    <td>
        ―
    </td>
```

</td>
<td>
    &nbsp;
</td>
<td>
    السماح بطباعة الأحرف غير ASCII. لم يتم تنفيذها بسبب عدم وجود ملفات عينة تحتوي على نص Unicode
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
    تم تحقيق ذلك فقط في النسخة التجريبية بسبب نقص في ملفات الاختبار. الخطوط المضمنة أيضاً غير مدعومة.<br> لا يدعم امتداد JetReady لأنه من المستحيل الحصول على مواصفات JetReady.
</td>
<td>
    صيغة ملف ثنائي.
</td>
</tr>
</tbody>
</table>

### تحويل ملف PCL إلى صيغة PDF

لتمكين التحويل من PCL إلى PDF، يوفر Aspose.PDF الصف [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) الذي يستخدم لتهيئة كائن LoadOptions.
```
للسماح بالتحويل من PCL إلى PDF، يوفر Aspose.PDF الفئة [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) التي تستخدم لتهيئة كائن LoadOptions.

الرمز التالي يوضح عملية تحويل ملف PCL إلى تنسيق PDF.

<a name="csharp-convert-pcl-to-pdf" id="csharp-convert-pcl-to-pdf"><strong><em>الخطوات:</em> تحويل PCL إلى PDF في C#</strong></a>

1. إنشاء نموذج من فئة [PclLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions/).
2. إنشاء نموذج من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) مع ذكر اسم الملف المصدر والخيارات.
3. حفظ المستند بالاسم المطلوب.

```csharp
public static void ConvertPCLtoPDF()
{
    PclLoadOptions options = new PclLoadOptions();
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

يمكنك أيضًا مراقبة اكتشاف الأخطاء خلال عملية التحويل.
يمكنك أيضاً مراقبة اكتشاف الأخطاء أثناء عملية التحويل.

```csharp
public static void ConvertPCLtoPDFAvdanced()
{
    PclLoadOptions options = new PclLoadOptions { SupressErrors = true };
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    if (options.Exceptions!=null)
        foreach (var ex in options.Exceptions)
        {
            Console.WriteLine(ex.Message);
        }
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

### المشكلات المعروفة

1. قد يختلف مصدر سلاسل النصوص والصور قليلاً عن تلك الموجودة في ملف PCL المصدر إذا لم تكن اتجاه الطباعة 0°. ينطبق الأمر نفسه على الصور المتجهة إذا تم تدوير نظام الإحداثيات للرسم المتجه (يسبقه أمر RO).
1. قد يختلف مصدر تسميات الصور المتجهة عن تلك الموجودة في ملف PCL المصدر إذا تأثرت التسميات بتسلسل الأوامر: أصل التسمية (LO)، تعريف مسار النص المتغير (DV)، الاتجاه المطلق (DI) أو الاتجاه النسبي (DR).
1.
1. إذا احتوى ملف PCL المحلل على خطوط Intellifont أو Universal soft فسيتم إلقاء استثناء، لأن خطوط Intellifont وUniversal غير مدعومة على الإطلاق.
1. إذا احتوى ملف PCL المحلل على أوامر الماكرو، فستختلف نتيجة التحليل اختلافًا كبيرًا عن الملف الأصلي، لأن أوامر الماكرو غير مدعومة.

## تحويل النص إلى PDF

**Aspose.PDF لـ .NET** تدعم ميزة تحويل ملفات النص العادي والنص المنسق مسبقًا إلى تنسيق PDF.

تحويل النص إلى PDF يعني إضافة فقرات النص إلى صفحة PDF. بالنسبة لملفات النص، نتعامل مع نوعين من النصوص: النص المنسق مسبقًا (على سبيل المثال، 25 سطرًا مع 80 حرفًا في كل سطر) والنص غير المنسق (النص العادي). حسب احتياجاتنا، يمكننا التحكم في هذه الإضافة بأنفسنا أو نتركها لخوارزميات المكتبة.

{{% alert color="success" %}}
**جرب تحويل النص إلى PDF عبر الإنترنت**

Aspose.PDF لـ .NET تقدم لك تطبيقًا مجانيًا عبر الإنترنت ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)، حيث يمكنك تجربة التحقيق في الوظائف والجودة التي يعمل بها.

Aspose.PDF لـ .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["نص إلى PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل أسبوز بي دي إف نص إلى PDF بواسطة تطبيق مجاني](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)

### تحويل ملف نص عادي إلى PDF

في حالة ملف النص العادي، يمكننا استخدام التقنية التالية:

<a name="csharp-convert-text-to-pdf" id="csharp-convert-text-to-pdf"><strong><em>الخطوات:</em> تحويل النص إلى PDF في C#</strong></a> |
<a name="csharp-convert-txt-to-pdf" id="csharp-convert-txt-to-pdf"><strong><em>الخطوات:</em> تحويل TXT إلى PDF في C#</strong></a> |
<a name="csharp-convert-plain-text-to-pdf" id="csharp-convert-plain-text-to-pdf"><strong><em>الخطوات:</em> تحويل النص العادي إلى PDF في C#</strong></a>

1. استخدم _TextReader_ لقراءة النص بالكامل;
2.

2.
3. قم بإنشاء كائن جديد من [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment/) وقم بتمرير كائن _TextReader_ إلى مُنشئه؛
4. أضف كائن _TextFragment_ كفقرة في مجموعة _Paragraphs_. إذا كان حجم النص أكبر من الصفحة، فإن خوارزمية المكتبة تضيف صفحات إضافية تلقائيًا؛
5. استخدم طريقة **Save** لفئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/);

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// قراءة ملف النص المصدر
TextReader tr = new StreamReader(dataDir + "log.txt");

// إنشاء كائن Document عن طريق استدعاء مُنشئه الفارغ
Document pdfDocument= new Document();

// إضافة صفحة جديدة في مجموعة Pages للوثيقة
Page page = pdfDocument.Pages.Add();

// إنشاء كائن من TextFragmet وتمرير النص من كائن القارئ إلى مُنشئه كوسيطة
TextFragment text = new TextFragment(tr.ReadToEnd());

// إضافة فقرة نصية جديدة في مجموعة الفقرات وتمرير كائن TextFragment
page.Paragraphs.Add(text);

// حفظ ملف PDF الناتج
pdfDocument.Save(dataDir + "TexttoPDF_out.pdf");
```
### تحويل ملف نصي مُنسق مسبقًا إلى PDF

تحويل النصوص المُنسقة مسبقًا مثل النص العادي لكن تحتاج إلى اتخاذ بعض الإجراءات الإضافية مثل تحديد الهوامش ونوع وحجم الخط. من الواضح أن الخط يجب أن يكون أحادي المسافة (مثل خط Courier New).

اتبع هذه الخطوات لتحويل نص مُنسق مسبقًا إلى PDF باستخدام C#:

<a name="csharp-convert-pre-text-to-pdf" id="csharp-convert-pre-text-to-pdf"><strong><em>الخطوات:</em> تحويل النص المُعد مسبقًا إلى PDF في C#</strong></a> |
<a name="csharp-convert-pre-formatted-txt-to-pdf" id="csharp-convert-pre-formatted-txt-to-pdf"><strong><em>الخطوات:</em> تحويل TXT المُنسق مسبقًا إلى PDF في C#</strong></a>

1. قراءة النص كاملاً كمصفوفة من السلاسل؛
2. إنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) وإضافة صفحة جديدة في مجموعة [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/pages/)؛
3.
في هذه الحالة، يضيف خوارزمية المكتبة صفحات إضافية أيضًا، ولكن يمكننا التحكم في هذه العملية بأنفسنا.
يوضح المثال التالي كيفية تحويل ملف نصي مُنسق مسبقًا (80x25) إلى مستند PDF بحجم A4.

```csharp
public static void ConvertPreFormattedTextToPdf()
{
    // قراءة ملف النص كمصفوفة من السلاسل
    var lines = System.IO.File.ReadAllLines(_dataDir + "rfc822.txt");

    // إنشاء كائن Document بالاستدعاء المنشئ الفارغ
    Document pdfDocument= new Document();

    // إضافة صفحة جديدة في مجموعة الصفحات للمستند
    Page page = pdfDocument.Pages.Add();

    // تعيين الهوامش اليسرى واليمنى لعرض أفضل
    page.PageInfo.Margin.Left = 20;
    page.PageInfo.Margin.Right = 10;
    page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
    page.PageInfo.DefaultTextState.FontSize = 12;

    foreach (var line in lines)
    {
        // فحص إذا كانت السطور تحتوي على حرف "تغذية النموذج"
        // انظر https://en.wikipedia.org/wiki/Page_break
        if (line.StartsWith("\x0c"))
        {
            page = pdfDocument.Pages.Add();
            page.PageInfo.Margin.Left = 20;
            page.PageInfo.Margin.Right = 10;
            page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
            page.PageInfo.DefaultTextState.FontSize = 12;
        }
        else
        {
            // إنشاء كائن TextFragment و
            // إرسال السطر إلى
            // المنشئ كحجة
            TextFragment text = new TextFragment(line);

            // إضافة فقرة نصية جديدة في مجموعة الفقرات وإرسال كائن TextFragment
            page.Paragraphs.Add(text);
        }
    }

    // حفظ الملف PDF الناتج
    pdfDocument.Save(_dataDir + "TexttoPDF_out.pdf");
}
```
## تحويل XPS إلى PDF

**Aspose.PDF لـ .NET** يدعم ميزة تحويل ملفات <abbr title="مواصفات الورق XML">XPS</abbr> إلى صيغة PDF. راجع هذا المقال لحل مهامك.

نوع ملف XPS مرتبط أساسًا بمواصفات الورق XML من قبل شركة مايكروسوفت. مواصفات الورق XML (XPS)، التي كانت تُعرف سابقًا بالاسم الرمزي ميترو وتضم مفهوم تسويق مسار الطباعة الجيل القادم (NGPP)، هي مبادرة مايكروسوفت لدمج إنشاء الوثائق وعرضها في نظام التشغيل ويندوز.

{{% alert color="primary" %}}

صيغة الملف عبارة عن ملف XML مضغوط يستخدم أساسًا للتوزيع والتخزين. من الصعب جدًا تعديله وتنفيذه في الغالب من قبل مايكروسوفت.

{{% /alert %}}

لتحويل XPS إلى PDF باستخدام Aspose.PDF لـ .NET، قمنا بتقديم فئة تُسمى [XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions) والتي تُستخدم لتهيئة كائن [LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions).
لتحويل XPS إلى PDF باستخدام Aspose.PDF لـ .NET، قدمنا فئة تُسمى [XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions) والتي تُستخدم لتهيئة كائن [LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions).

{{% alert color="primary" %}}

في كل من XP وWindows 7، يجب أن تجد طابعة XPS مُثبتة مُسبقًا إذا نظرت في لوحة التحكم ثم الطابعات. يمكنك استخدام تلك الطابعة كجهاز إخراج لإنشاء هذه الملفات. في Windows 7، يجب أن تتمكن ببساطة من النقر المزدوج على الملف لفتحه في مستعرض XPS. يمكنك أيضًا تنزيل مستعرض XPS من موقع مايكروسوفت.

{{% /alert %}}

يُظهر الجزء التالي من الكود عملية تحويل ملف XPS إلى تنسيق PDF باستخدام C#.

<a name="csharp-convert-xps-to-pdf" id="csharp-convert-xps-to-pdf"><strong><em>الخطوات:</em> تحويل XPS إلى PDF في C#</strong></a>

1. إنشاء نسخة من فئة [XpsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions/).
2.
3. احفظ الوثيقة بتنسيق PDF باسم الملف المطلوب.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// إنشاء كائن LoadOption باستخدام خيار تحميل XPS
Aspose.Pdf.LoadOptions options = new XpsLoadOptions();

// إنشاء كائن الوثيقة
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "XPSToPDF.xps", options);

// حفظ وثيقة PDF الناتجة
document.Save(dataDir + "XPSToPDF_out.pdf");
```

{{% alert color="success" %}}
**جرب تحويل تنسيق XPS إلى PDF عبر الإنترنت**

يقدم لك Aspose.PDF for .NET تطبيقًا مجانيًا عبر الإنترنت ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)، حيث يمكنك تجربة استكشاف الوظائف وجودة عمله.

[![Aspose.PDF تحويل XPS إلى PDF بتطبيق مجاني](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}
{{% /alert %}}

## تحويل PostScript إلى PDF

**Aspose.PDF لـ .NET** يدعم ميزات تحويل ملفات PostScript إلى تنسيق PDF. إحدى الميزات من Aspose.PDF هي أنك يمكنك تحديد مجموعة من مجلدات الخطوط لاستخدامها أثناء التحويل.

لتحويل ملف PostScript إلى تنسيق PDF، يقدم Aspose.PDF لـ .NET فئة [PsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/psloadoptions) التي تُستخدم لتهيئة كائن LoadOptions. يمكن بعد ذلك تمرير هذا الكائن كوسيطة إلى مُنشئ كائن Document، والذي سيساعد محرك تقديم PDF على تحديد تنسيق المستند المصدر.

يمكن استخدام الشفرة التالية لتحويل ملف PostScript إلى تنسيق PDF باستخدام Aspose.PDF لـ .NET:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string _dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// إنشاء نسخة جديدة من PsLoadOptions
PsLoadOptions options = new PsLoadOptions();
// فتح مستند .ps باستخدام خيارات التحميل المُنشأة
Document pdfDocument = new Document(_dataDir + "input.ps", options);
// حفظ المستند
pdfDocument.Save(dataDir + "PSToPDF.pdf");
```
بالإضافة إلى ذلك، يمكنك تعيين مجموعة من مجلدات الخطوط التي سيتم استخدامها أثناء التحويل:

```csharp
public static void ConvertPostscriptToPDFAvdanced()
{
    PsLoadOptions options = new PsLoadOptions
    {
        FontsFolders = new [] { @"c:\tmp\fonts1", @"c:\tmp\fonts2"}
    };
    Document pdfDocument = new Document(_dataDir + "input.ps", options);
    pdfDocument.Save(_dataDir + "ps_test.pdf");
}
```

## تحويل XML إلى PDF

يُستخدم تنسيق XML لتخزين البيانات المنظمة. هناك عدة طرق لتحويل XML إلى PDF في Aspose.PDF:

1. تحويل أي بيانات XML إلى HTML باستخدام XSLT وتحويل HTML إلى PDF كما هو موضح أدناه
1. إنشاء مستند XML باستخدام مخطط Aspose.PDF XSD
1. استخدام مستند XML بناءً على معيار XSL-FO

{{% alert color="success" %}}
**جرب تحويل XML إلى PDF عبر الإنترنت**

يقدم Aspose.PDF لـ .NET تطبيقًا مجانيًا عبر الإنترنت ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.
Aspose.PDF لـ .NET يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["XML إلى PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)، حيث يمكنك تجربة استكشاف الوظائف وجودة عمله.

[![تحويل Aspose.PDF من XML إلى PDF بتطبيق مجاني](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

## تحويل XSL-FO إلى PDF

يمكن تنفيذ تحويل ملفات XSL-FO إلى PDF باستخدام تقنية Aspose.PDF التقليدية - استخدم كائن [Document](https://reference.aspose.com/page/net/aspose.page/document) مع [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). ولكن أحيانًا قد تواجه هيكل الملف غير الصحيح. في هذه الحالة، يسمح محول XSL-FO بتعيين استراتيجية معالجة الأخطاء. يمكنك اختيار `ThrowExceptionImmediately`، `TryIgnore` أو `InvokeCustomHandler`.

```csharp
public static void Convert_XSLFO_to_PDF()
{
    // إنشاء كائن XslFoLoadOption
    var options = new XslFoLoadOptions(".\\samples\\employees.xslt");
    // تعيين استراتيجية معالجة الأخطاء
    options.ParsingErrorsHandlingType = XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately;
    // إنشاء كائن Document
    var pdfDocument = new Aspose.Pdf.Document(".\\samples\\employees.xml", options);
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```
## تحويل LaTeX/TeX إلى PDF

تنسيق ملف LaTeX هو تنسيق ملف نصي يحتوي على ترميز في مشتق LaTeX من عائلة لغات TeX وLaTeX هو تنسيق مشتق من نظام TeX. LaTeX (ˈleɪtɛk/lay-tek أو lah-tek) هو نظام إعداد الوثائق ولغة ترميز الوثائق. يستخدم على نطاق واسع للتواصل والنشر العلمي في العديد من المجالات، بما في ذلك الرياضيات، والفيزياء، وعلوم الكمبيوتر. له دور بارز أيضًا في إعداد ونشر الكتب والمقالات التي تحتوي على مواد متعددة اللغات معقدة، مثل السنسكريتية والعربية، بما في ذلك الطبعات النقدية. يستخدم LaTeX برنامج تنسيق TeX لتنسيق مخرجاته، وهو مكتوب بنفسه في لغة ماكرو TeX.

{{% alert color="success" %}}
**جرب تحويل LaTeX/TeX إلى PDF عبر الإنترنت**

يقدم لك Aspose.PDF for .NET تطبيقًا مجانيًا عبر الإنترنت ["LaTex إلى PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF LaTeX/TeX إلى PDF مع تطبيق مجاني](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
[![تحويل Aspose.PDF LaTeX/TeX إلى PDF باستخدام التطبيق المجاني](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Aspose.PDF لـ .NET يدعم ميزة تحويل ملفات TeX إلى تنسيق PDF ولتحقيق هذا المطلب، فضاء الأسماء Aspose.Pdf يحتوي على فئة تُسمى [LatexLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexloadoptions) التي توفر القدرات لتحميل ملفات LaTex وعرض الناتج بتنسيق PDF باستخدام [فئة المستند](https://reference.aspose.com/pdf/net/aspose.pdf/document).
يوضح الجزء التالي من الكود عملية تحويل ملف LaTex إلى تنسيق PDF باستخدام C#.

```csharp
public static void ConvertTeXtoPDF()
{
    // إنشاء كائن خيار تحميل Latex
    TeXLoadOptions options = new TeXLoadOptions();
    // إنشاء كائن المستند
    Aspose.Pdf.Document pdfDocument= new Aspose.Pdf.Document(_dataDir + "samplefile.tex", options);
    // حفظ الناتج في ملف PDF
    pdfDocument.Save(_dataDir + "TeXToPDF_out.pdf");
}
```
