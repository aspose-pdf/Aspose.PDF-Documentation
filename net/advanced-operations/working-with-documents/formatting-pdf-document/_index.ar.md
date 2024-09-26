---
title: تنسيق مستند PDF باستخدام C#
linktitle: تنسيق مستند PDF
type: docs
weight: 11
url: /net/formatting-pdf-document/
description: قم بإنشاء وتنسيق مستند PDF باستخدام Aspose.PDF لـ .NET. استخدم الشفرة التالية لحل مهامك.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "تنسيق مستند PDF باستخدام C#",
    "alternativeHeadline": "كيفية تنسيق مستند PDF في .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "pdf, dotnet, تنسيق مستند pdf",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "قم بإنشاء وتنسيق مستند PDF باستخدام Aspose.PDF لـ .NET. استخدم الشفرة التالية لحل مهامك."
}
</script>

## تنسيق مستند PDF

### الحصول على خصائص نافذة المستند وعرض الصفحات

يساعدك هذا الموضوع على فهم كيفية الحصول على خصائص نافذة المستند، تطبيق المشاهدة، وكيفية عرض الصفحات. لضبط هذه الخصائص:

افتح ملف PDF باستخدام فئة [المستند](https://reference.aspose.com/pdf/net/aspose.pdf/document). الآن، يمكنك ضبط خصائص كائن المستند، مثل:

- CenterWindow – مركز نافذة المستند على الشاشة. الافتراضي: خطأ.
- Direction – ترتيب القراءة. يحدد هذا كيفية ترتيب الصفحات عند عرضها جنبًا إلى جنب. الافتراضي: من اليسار إلى اليمين.
- DisplayDocTitle – عرض عنوان المستند في شريط عنوان نافذة المستند. الافتراضي: خطأ (يتم عرض العنوان).
- HideMenuBar – إخفاء أو عرض شريط قائمة نافذة المستند. الافتراضي: خطأ (يتم عرض شريط القائمة).
- HideToolBar – إخفاء أو عرض شريط أدوات نافذة المستند. الافتراضي: خطأ (يتم عرض شريط الأدوات).
- HideWindowUI – إخفاء أو عرض عناصر نافذة المستند مثل شريط التمرير.
- HideWindowUI – إخفاء أو عرض عناصر نافذة المستند مثل شريط التمرير.
- NonFullScreenPageMode – كيفية عرض المستند عندما لا يكون في وضع الصفحة الكاملة.
- PageLayout – تخطيط الصفحة.
- PageMode – كيفية عرض المستند عند فتحه لأول مرة. الخيارات هي عرض الصور المصغرة، الشاشة الكاملة، عرض لوحة المرفقات.

يعمل الكود التالي أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

الكود التالي يوضح كيفية الحصول على الخصائص باستخدام فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "GetDocumentWindow.pdf");

// الحصول على خصائص المستند المختلفة
// موقع نافذة المستند - الافتراضي: false
Console.WriteLine("CenterWindow : {0}", pdfDocument.CenterWindow);

// ترتيب القراءة السائد؛ يحدد موقع الصفحة
// عند عرضها جنبًا إلى جنب - الافتراضي: L2R
Console.WriteLine("Direction : {0}", pdfDocument.Direction);

// ما إذا كان شريط العنوان النافذة يجب أن يعرض عنوان المستند
// إذا كان خطأ، يعرض شريط العنوان اسم ملف PDF - الافتراضي: false
Console.WriteLine("DisplayDocTitle : {0}", pdfDocument.DisplayDocTitle);

// ما إذا كان يجب تغيير حجم نافذة المستند لتناسب حجم
// الصفحة الأولى المعروضة - الافتراضي: false
Console.WriteLine("FitWindow : {0}", pdfDocument.FitWindow);

// ما إذا كان يجب إخفاء شريط القوائم لتطبيق العارض - الافتراضي: false
Console.WriteLine("HideMenuBar : {0}", pdfDocument.HideMenubar);

// ما إذا كان يجب إخفاء شريط الأدوات لتطبيق العارض - الافتراضي: false
Console.WriteLine("HideToolBar : {0}", pdfDocument.HideToolBar);

// ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل شريط التمرير
// وترك محتويات الصفحة فقط معروضة - الافتراضي: false
Console.WriteLine("HideWindowUI : {0}", pdfDocument.HideWindowUI);

// وضع صفحة المستند. كيفية عرض المستند عند الخروج من وضع الشاشة الكاملة.
Console.WriteLine("NonFullScreenPageMode : {0}", pdfDocument.NonFullScreenPageMode);

// تخطيط الصفحة مثل صفحة واحدة، عمود واحد
Console.WriteLine("PageLayout : {0}", pdfDocument.PageLayout);

// كيف يجب أن يعرض المستند عند فتحه
// أي عرض الصور المصغرة، الشاشة الكاملة، عرض لوحة المرفقات
Console.WriteLine("pageMode : {0}", pdfDocument.PageMode);
```
### تعيين خصائص نافذة المستند وعرض الصفحة

يشرح هذا الموضوع كيفية تعيين خصائص نافذة المستند، تطبيق المشاهدة، وعرض الصفحة. لتعيين هذه الخصائص المختلفة:

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. اضبط خصائص كائن الوثيقة.
1. احفظ ملف PDF المحدث باستخدام طريقة الحفظ.

الخصائص المتاحة هي:

- مركز النافذة
- الاتجاه
- عرض عنوان الوثيقة
- ملاءمة النافذة
- إخفاء شريط القوائم
- إخفاء شريط الأدوات
- إخفاء واجهة المستخدم للنافذة
- وضع الصفحة غير الملء الكامل
- تخطيط الصفحة
- وضع الصفحة

يتم استخدام كل منها ووصفها في الكود أدناه. يُظهر الكود التالي كيفية تعيين الخصائص باستخدام فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// فتح المستند
Document pdfDocument = new Document(dataDir + "SetDocumentWindow.pdf");

// تعيين خصائص مختلفة للمستند
// تحديد لتموضع نافذة المستند - الافتراضي: خطأ
pdfDocument.CenterWindow = true;

// ترتيب القراءة الغالب؛ يحدد موضع الصفحة
// عند العرض جنبًا إلى جنب - الافتراضي: L2R
pdfDocument.Direction = Direction.R2L;

// تحديد ما إذا كان يجب عرض عنوان الوثيقة في شريط عنوان النافذة
// إذا كان خطأ، يعرض شريط العنوان اسم ملف PDF - الافتراضي: خطأ
pdfDocument.DisplayDocTitle = true;

// تحديد ما إذا كان يجب تغيير حجم نافذة المستند لتناسب حجم
// أول صفحة معروضة - الافتراضي: خطأ
pdfDocument.FitWindow = true;

// تحديد ما إذا كان يجب إخفاء شريط القوائم لتطبيق المشاهدة - الافتراضي: خطأ
pdfDocument.HideMenubar = true;

// تحديد ما إذا كان يجب إخفاء شريط الأدوات لتطبيق المشاهدة - الافتراضي: خطأ
pdfDocument.HideToolBar = true;

// تحديد ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل شريط التمرير
// ويترك فقط محتويات الصفحة معروضة - الافتراضي: خطأ
pdfDocument.HideWindowUI = true;

// وضع صفحة المستند. تحديد كيفية عرض المستند عند الخروج من وضع ملء الشاشة.
pdfDocument.NonFullScreenPageMode = PageMode.UseOC;

// تحديد تخطيط الصفحة مثل صفحة واحدة، عمود واحد
pdfDocument.PageLayout = PageLayout.TwoColumnLeft;

// تحديد كيفية عرض المستند عند فتحه
// مثل عرض الصور المصغرة، ملء الشاشة، عرض لوحة المرفقات
pdfDocument.PageMode = PageMode.UseThumbs;

dataDir = dataDir + "SetDocumentWindow_out.pdf";
// حفظ ملف PDF المحدث
pdfDocument.Save(dataDir);
```
### تضمين الخطوط في ملف PDF موجود

يدعم قارئات ملفات PDF [مجموعة أساسية من 14 خطًا](https://en.wikipedia.org/wiki/PDF#Text) حتى يمكن عرض الوثائق بنفس الطريقة بغض النظر عن المنصة التي يتم عرض الوثيقة عليها. عندما يحتوي ملف PDF على خط ليس من بين الخطوط الأساسية الـ 14، قم بتضمين الخط في ملف PDF لتجنب استبدال الخط.

يدعم Aspose.PDF لـ .NET تضمين الخطوط في ملفات PDF الموجودة. يمكنك تضمين خط كامل أو جزء من الخط. لتضمين الخط، افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). ثم استخدم فئة [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text) لتضمين الخط في ملف PDF. لتضمين الخط بالكامل، استخدم خاصية IsEmbeded في فئة الخط؛ لاستخدام جزء من الخط، استخدم خاصية IsSubset.

{{% alert color="primary" %}}

يضمن جزء الخط الأحرف المستخدمة فقط وهو مفيد حيث يتم استخدام الخطوط لجمل قصيرة أو شعارات، على سبيل المثال حيث يتم استخدام خط الشركة للشعار، ولكن ليس لنص الجسم.
يُدمج جزء الخط فقط الأحرف المستخدمة وهو مفيد حيث يتم استخدام الخطوط للجمل القصيرة أو الشعارات، على سبيل المثال حيث يتم استخدام خط الشركة للشعار، ولكن لا يُستخدم لنص الجسم.

{{% /alert %}}

يُظهر الشفرة التالية كيفية تضمين خط في ملف PDF.

### تضمين خطوط النوع 1 القياسية

تحتوي بعض مستندات PDF على خطوط من مجموعة خاصة من خطوط Adobe. تُعرف الخطوط من هذه المجموعة بـ "خطوط النوع 1 القياسية". تتضمن هذه المجموعة 14 خطًا ويتطلب تضمين هذا النوع من الخطوط استخدام علامات خاصة مثل [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts). فيما يلي الشفرة التي يمكن استخدامها للحصول على مستند بجميع الخطوط المضمنة بما في ذلك خطوط النوع 1 القياسية:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// تحميل مستند PDF موجود
Document pdfDocument = new Document(dataDir + "input.pdf");
// تعيين خاصية EmbedStandardFonts للمستند
pdfDocument.EmbedStandardFonts = true;
foreach (Aspose.Pdf.Page page in pdfDocument.Pages)
{
    if (page.Resources.Fonts != null)
    {
        foreach (Aspose.Pdf.Text.Font pageFont in page.Resources.Fonts)
        {
// التحقق إذا كان الخط مضمنًا بالفعل
if (!pageFont.IsEmbedded)
{
    pageFont.IsEmbedded = true;
}
        }
    }
}
pdfDocument.Save(dataDir + "EmbeddedFonts-updated_out.pdf");
```
### تضمين الخطوط عند إنشاء ملف PDF

إذا كنت بحاجة إلى استخدام خط غير الخطوط الأساسية الـ 14 المدعومة من قبل Adobe Reader، يجب عليك تضمين وصف الخط أثناء توليد ملف الـ Pdf. إذا لم يتم تضمين معلومات الخط، سيأخذ Adobe Reader الخط من نظام التشغيل إذا كان مثبتًا على النظام، أو سيقوم بإنشاء خط بديل وفقًا لمواصفات الخط في الـ Pdf.

> يرجى ملاحظة أنه يجب تثبيت الخط المضمن على جهاز المضيف، أي في حالة الكود التالي يكون خط 'Univers Condensed' مثبتًا على النظام.

نستخدم خاصية IsEmbedded من فئة Font لتضمين معلومات الخط في ملف الـ Pdf. تعيين قيمة هذه الخاصية إلى 'True' سيؤدي إلى تضمين ملف الخط بالكامل في الـ Pdf، مع العلم أن ذلك سيزيد من حجم ملف الـ Pdf. فيما يلي مقتطف الكود الذي يمكن استخدامه لتضمين معلومات الخط في الـ Pdf.

```csharp
// للحصول على الأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// تجسيد كائن Pdf من خلال استدعاء المنشئ الفارغ
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();

// إنشاء قسم في كائن Pdf
Aspose.Pdf.Page page = doc.Pages.Add();

Aspose.Pdf.Text.TextFragment fragment = new Aspose.Pdf.Text.TextFragment("");

Aspose.Pdf.Text.TextSegment segment = new Aspose.Pdf.Text.TextSegment(" هذا نص تجريبي باستخدام خط مخصص.");
Aspose.Pdf.Text.TextState ts = new Aspose.Pdf.Text.TextState();
ts.Font = FontRepository.FindFont("Arial");
ts.Font.IsEmbedded = true;
segment.TextState = ts;
fragment.Segments.Add(segment);
page.Paragraphs.Add(fragment);

dataDir = dataDir + "EmbedFontWhileDocCreation_out.pdf";
// حفظ مستند PDF
doc.Save(dataDir);
```
### تعيين اسم الخط الافتراضي عند حفظ PDF

عندما يحتوي مستند PDF على خطوط غير متوفرة في المستند نفسه وعلى الجهاز، تقوم الواجهة البرمجية باستبدال هذه الخطوط بالخط الافتراضي. عندما يكون الخط متاحًا (مثبتًا على الجهاز أو مضمنًا في المستند)، يجب أن يحتوي ملف PDF الناتج على نفس الخط (لا ينبغي استبداله بالخط الافتراضي). يجب أن يحتوي قيمة الخط الافتراضي على اسم الخط (وليس مسار ملفات الخط). لقد قمنا بتنفيذ ميزة لتعيين اسم الخط الافتراضي أثناء حفظ المستند كـ PDF. يمكن استخدام قطعة الكود التالية لتعيين الخط الافتراضي:

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// تحميل مستند PDF موجود بخط مفقود
string documentName = dataDir + "input.pdf";
string newName = "Arial";
using (System.IO.FileStream fs = new System.IO.FileStream(documentName, System.IO.FileMode.Open))
using (Document document = new Document(fs))
{
    PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();
    // تحديد اسم الخط الافتراضي
    pdfSaveOptions.DefaultFontName = newName;
    document.Save(dataDir + "output_out.pdf", pdfSaveOptions);
}
```
### الحصول على جميع الخطوط من مستند PDF

في حال أردت الحصول على جميع الخطوط من مستند PDF، يمكنك استخدام طريقة FontUtilities.GetAllFonts() المتوفرة في فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). الرجاء التحقق من قطعة الكود التالية للحصول على جميع الخطوط من مستند PDF موجود:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

### الحصول على تحذيرات بخصوص استبدال الخط

Aspose.PDF for .NET يوفر طرقًا للحصول على إشعارات حول استبدال الخطوط للتعامل مع حالات استبدال الخطوط. تظهر قطع الكود أدناه كيفية استخدام الوظائف المقابلة.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

Document doc = new Document(dataDir + "input.pdf");

doc.FontSubstitution += new Document.FontSubstitutionHandler(OnFontSubstitution);
```
**طريقة OnFontSubstitution** مذكورة أدناه.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
Console.WriteLine(string.Format("تم استبدال الخط '{0}' بخط آخر '{1}'",
oldFont.FontName, newFont.FontName));
```

### تحسين تضمين الخطوط باستخدام استراتيجية FontSubsetStrategy

يمكن إنجاز ميزة تضمين الخطوط كمجموعة جزئية باستخدام خاصية IsSubset، ولكن أحيانًا ترغب في تقليص مجموعة الخطوط المضمنة بالكامل إلى المجموعات الجزئية فقط التي تُستخدم في المستند. يحتوي مستند Aspose.Pdf على خاصية FontUtilities التي تتضمن طريقة SubsetFonts(FontSubsetStrategy subsetStrategy). في طريقة SubsetFonts()، يساعد المعامل subsetStrategy في ضبط استراتيجية المجموعة الجزئية. تدعم FontSubsetStrategy البديلين التاليين لتجميع الخطوط الجزئية:

- SubsetAllFonts - سيتم تجميع جميع الخطوط المستخدمة في المستند.
- SubsetEmbeddedFontsOnly - سيتم تجميع الخطوط المضمنة بالكامل في المستند فقط.

يوضح الجزء التالي من الكود كيفية ضبط FontSubsetStrategy:
شفرة البرمجة التالية تظهر كيفية تعيين استراتيجية FontSubsetStrategy:

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
// سيتم تضمين جميع الخطوط كمجموعة جزئية داخل الوثيقة في حالة SubsetAllFonts.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetAllFonts);
// سيتم تضمين مجموعة جزئية من الخطوط للخطوط المضمنة بالكامل ولكن الخطوط التي لم تُضمن في الوثيقة لن يتأثر بها.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
doc.Save(dataDir + "Output_out.pdf");
```

### الحصول على وضع عامل التكبير لملف PDF

أحيانًا، قد ترغب في تحديد ما هو عامل التكبير الحالي لمستند PDF. مع Aspose.Pdf، يمكنك معرفة القيمة الحالية وكذلك تعيين واحدة.

خاصية Destination لفئة [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) تتيح لك الحصول على قيمة التكبير المرتبطة بملف PDF.
خاصية Destination في فئة [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) تمكنك من الحصول على قيمة التكبير المرتبطة بملف PDF.

#### تعيين عامل التكبير

يوضح الكود التالي كيفية تعيين عامل تكبير لملف PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// إنشاء كائن جديد للوثيقة
Document doc = new Document(dataDir + "SetZoomFactor.pdf");

GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0, 0, .5));
doc.OpenAction = action;
dataDir = dataDir + "Zoomed_pdf_out.pdf";
// حفظ الوثيقة
doc.Save(dataDir);
```

#### الحصول على عامل التكبير

يوضح الكود التالي كيفية الحصول على عامل تكبير ملف PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// إنشاء كائن جديد للوثيقة
Document doc = new Document(dataDir + "Zoomed_pdf.pdf");

// إنشاء كائن GoToAction
GoToAction action = doc.OpenAction as GoToAction;

// الحصول على عامل التكبير لملف PDF
System.Console.WriteLine((action.Destination as XYZExplicitDestination).Zoom); // قيمة تكبير الوثيقة;
```
### إعداد خصائص مربع حوار الطباعة المسبق

يتيح Aspoose.PDF إعداد خصائص مربع حوار الطباعة المسبق لمستند PDF. يتيح لك تغيير خاصية DuplexMode لمستند PDF المضبوط افتراضيًا على simplex. يمكن تحقيق ذلك باستخدام منهجيتين مختلفتين كما هو موضح أدناه.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

using (Document doc = new Document())
{
    doc.Pages.Add();
    doc.Duplex = PrintDuplex.DuplexFlipLongEdge;
    doc.Save(dataDir + "35297_out.pdf", SaveFormat.Pdf);
}
```

### إعداد خصائص مربع حوار الطباعة المسبق باستخدام محرر محتوى PDF

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

string outputFile = dataDir + "input.pdf";
using (PdfContentEditor ed = new PdfContentEditor())
{
    ed.BindPdf(outputFile);
    if ((ed.GetViewerPreference() & ViewerPreference.DuplexFlipShortEdge) > 0)
    {
        Console.WriteLine("الملف لديه تقليب ثنائي على الحافة القصيرة");
    }

    ed.ChangeViewerPreference(ViewerPreference.DuplexFlipShortEdge);
    ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
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
    "applicationCategory": "مكتبة التلاعب بملفات PDF لـ .NET",
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
```

