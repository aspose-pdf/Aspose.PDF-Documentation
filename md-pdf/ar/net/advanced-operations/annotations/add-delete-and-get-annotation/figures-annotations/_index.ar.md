---
title: إضافة تعليقات توضيحية على الأشكال باستخدام C#
linktitle: تعليقات توضيحية للأشكال
type: docs
weight: 30
url: /net/figures-annotation/
description: يصف هذا المقال كيفية إضافة، الحصول على، وحذف التعليقات التوضيحية للأشكال من مستند PDF الخاص بك باستخدام Aspose.PDF لـ.NET
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة تعليقات توضيحية على الأشكال باستخدام C#",
    "alternativeHeadline": "كيفية إضافة تعليقات توضيحية للأشكال في PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, تعليقات توضيحية للأشكال، تعليق توضيحي للمضلع، تعليق توضيحي للخط، تعليق توضيحي للمربع، تعليق توضيحي للدائرة",
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
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "يصف هذا المقال كيفية إضافة، الحصول على، وحذف التعليقات التوضيحية للأشكال من مستند PDF الخاص بك باستخدام Aspose.PDF لـ.NET"
}
</script>
تطبيق إدارة مستندات PDF يوفر أدوات متنوعة لتعليق على المستندات. من منظور البنية الداخلية لملف PDF، هذه الأدوات هي التعليقات التوضيحية. نحن ندعم أنواع الأدوات التالية للرسم.

* تعليق خطي - أداة لرسم الخطوط والأسهم
* تعليق مربع - لرسم المربعات والمستطيلات
* تعليق دائري - للبيضاويات والدوائر
* تعليق نص حر - للتعليق المنبثق
* تعليق مضلع - للمضلعات والسحب
* تعليق خطوط متعددة - للخطوط المتصلة

## إضافة الأشكال والأرقام على الصفحة

النهج لإضافة التعليق التوضيحي هو نموذجي لأي منها.

الشفرة التالية تعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

1. تحميل ملف PDF أو إنشاء جديد بواسطة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. إنشاء التعليق التوضيحي الجديد وتعيين المعاملات (مستطيل جديد، نقطة جديدة، العنوان، اللون، العرض، إلخ).

type: docs
changefreq: "monthly"
1. ربط تعليق توضيحي بالنوع الأصلي.
1. إضافة تعليق توضيحي إلى الصفحة

## إضافة خطوط أو أسهم

الغرض من التعليق التوضيحي للخط هو عرض خط مستقيم أو سهم على الصفحة.
لإنشاء خط نحتاج إلى كائن تعليق توضيحي جديد للخط.
يأخذ مُنشئ فئة LineAnnotation أربعة معاملات:

* الصفحة التي سيتم إضافة التعليق التوضيحي إليها،
* المستطيل الذي يحدد حدود التعليق التوضيحي،
* والنقطتان اللتان تحددان بداية ونهاية الخط.

أيضًا نحتاج إلى تهيئة بعض الخصائص:

* `Title` - عادةً ما يكون اسم المستخدم الذي قام بإضافة هذا التعليق
* `Subject` - يمكن أن يكون أي سلسلة، ولكن في الحالات الشائعة هو اسم التعليق التوضيحي

لتصميم خطنا نحتاج إلى تعيين اللون، العرض، نمط البداية، ونمط النهاية.
لتصميم خطنا نحتاج إلى تحديد اللون، العرض، نمط البداية، ونمط النهاية.

الكود التالي يوضح كيفية إضافة تعليق توضيحي للخط إلى ملف PDF:

```csharp
// تحميل ملف PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

// إنشاء تعليق توضيحي للخط
var lineAnnotation = new LineAnnotation(
    document.Pages[1],
    new Rectangle(550, 93, 562, 439),
    new Point(556, 99), new Point(556, 443))
{
    Title = "John Smith",
    Color = Color.Red,
    Width = 3,
    StartingStyle = LineEnding.OpenArrow,
    EndingStyle = LineEnding.OpenArrow,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
};

// إضافة التعليق إلى الصفحة
document.Pages[1].Annotations.Add(lineAnnotation);
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
```

## إضافة مربع أو دائرة

التعليقات التوضيحية [Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) و [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) ستعرض مستطيل أو بيضوي على الصفحة.
[Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) و [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) ستعرض الشكل البيضاوي أو المستطيل على الصفحة.

### إضافة تعليق توضيحي دائري

لرسم تعليق توضيحي جديد على شكل دائرة أو بيضاوي، نحتاج إلى إنشاء كائن CircleAnnotation جديد. يأخذ مُنشئ فئة `CircleAnnotation` معاملين:

* الصفحة التي سيُضاف إليها التعليق التوضيحي،
* والمستطيل الذي يحدد حدود التعليق التوضيحي

كما يمكننا تعيين بعض خصائص كائن `CircleAnnotation`، مثل العنوان، اللون، لون الداخل، الشفافية. تتحكم هذه الخصائص في مظهر وسلوك التعليق التوضيحي داخل عارض PDF. هنا وفيما بعد في المربع، يكون لون `InteriorColor` هو لون التعبئة و`Color` هو لون الحدود.

### إضافة تعليق توضيحي مربع

رسم المستطيل يشبه رسم الدائرة.
رسم مستطيل هو نفسه رسم دائرة.

```csharp
var dataDir = "<path-to-file>";
// تحميل ملف PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// إنشاء تعليق توضيحي دائري
var circleAnnotation = new CircleAnnotation(document.Pages[1], new Rectangle(270, 160, 483, 383))
{
    Title = "John Smith",
    Subject = "Circle",
    Color = Color.Red,
    InteriorColor = Color.MistyRose,
    Opacity = 0.5,        
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 316, 1021, 459))
};

// إنشاء تعليق توضيحي مربع
var squareAnnotation = new SquareAnnotation(document.Pages[1], new Rectangle(67, 317, 261, 459))
{
    Title = "John Smith",
    Subject = "Rectangle",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// إضافة التعليق التوضيحي إلى الصفحة
document.Pages[1].Annotations.Add(circleAnnotation);
document.Pages[1].Annotations.Add(squareAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
كمثال، سنرى النتيجة التالية لإضافة تعليقات توضيحية على شكل مربع ودائرة إلى مستند PDF:

![عرض توضيحي للتعليق التوضيحي للدائرة والمربع](circle_demo.png)

## إضافة تعليقات توضيحية للمضلع والخط المتعدد

أداة Poly- تتيح لك إنشاء أشكال ومخططات بعدد غير محدد من الجوانب على المستند.

**تعليقات توضيحية للمضلع** تمثل المضلعات على صفحة. يمكن أن يكون لها أي عدد من الرؤوس المتصلة بخطوط مستقيمة.
**تعليقات توضيحية للخط المتعدد** مشابهة أيضاً للمضلعات، الاختلاف الوحيد هو أن الرأس الأول والأخير ليسا متصلين بشكل ضمني.

### إضافة تعليق توضيحي للمضلع

PolygonAnnotation مسؤول عن التعليقات التوضيحية للمضلع. يأخذ مُنشئ فئة PolygonAnnotation ثلاثة معاملات:

* الصفحة التي سيتم إضافة التعليق التوضيحي إليها،
* المستطيل الذي يحدد حدود التعليق التوضيحي،
* ومصفوفة من النقاط التي تحدد رؤوس المضلع.

`Color` و `InteriorColor` تُستخدمان لألوان الحدود والتعبئة على التوالي.

### إضافة تعليق توضيحي للخط المتعدد
### إضافة تعليق توضيحي على شكل خطوط متعددة

PolygonAnnotation مسؤول عن التعليقات التوضيحية على شكل مضلع. يأخذ المنشئ في فئة PolygonAnnotation ثلاثة معاملات:

* الصفحة التي سيتم إضافة التعليق التوضيحي إليها،
* المستطيل الذي يحدد حدود التعليق التوضيحي،
* ومصفوفة النقاط التي تحدد رؤوس المضلع.

بدلاً من `PolygonAnnotation` لا يمكننا ملء هذا الشكل، لذا لا نحتاج إلى استخدام `InteriorColor`.

يظهر الشفرة التالية كيفية إضافة تعليقات توضيحية على شكل مضلع وخطوط متعددة إلى ملف PDF:

```csharp
// تحميل ملف PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// إنشاء تعليق توضيحي على شكل مضلع
var polygonAnnotation = new PolygonAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(274, 381),
        new Point(555, 381),
        new Point(555, 304),
        new Point(570, 304),
        new Point(570, 195),
        new Point(274, 195)})
{
    Title = "جون سميث",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// إنشاء تعليق توضيحي على شكل خطوط متعددة
var polylineAnnotation = new PolylineAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(545,150),
        new Point(545,190),
        new Point(667,190),
        new Point(667,110),
        new Point(626,111)
        })
{
    Title = "جون سميث",
    Color = Color.Red,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// إضافة التعليق التوضيحي إلى الصفحة
document.Pages[1].Annotations.Add(polygonAnnotation);
document.Pages[1].Annotations.Add(polylineAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
## الحصول على الأشكال

جميع التعليقات الوصفية مخزنة في مجموعة `Annotations`. يمكن لأي تعليق وصفي أن يعرّف نوعه من خلال خاصية `AnnotationType`. وبالتالي، يمكننا إجراء استعلام LINQ لتصفية التعليقات الوصفية المطلوبة.

### الحصول على تعليقات الخطوط

المثال أدناه يشرح كيفية الحصول على جميع تعليقات الخطوط من الصفحة الأولى لمستند PDF.

```csharp
// تحميل ملف PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();
foreach (var la in lineAnnotations)
{
    Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
}   
```

### الحصول على تعليقات الدوائر

المثال أدناه يشرح كيفية الحصول على جميع تعليقات الخطوط المتعددة من الصفحة الأولى لمستند PDF.

```csharp
// تحميل ملف PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var circleAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<CircleAnnotation>();
foreach (var ca in circleAnnotations)
{
    Console.WriteLine($"[{ca.Rect}]");
}   
```
### الحصول على تعليقات المربع

المثال أدناه يشرح كيفية الحصول على جميع تعليقات المربع من الصفحة الأولى لمستند PDF.

```csharp
// تحميل ملف PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var squareAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Square)
    .Cast<SquareAnnotation>();
foreach (var sq in squareAnnotations)
{
    Console.WriteLine($"[{sq.Rect}]");
}
```

### الحصول على تعليقات الخطوط المتعددة

المثال أدناه يشرح كيفية الحصول على جميع تعليقات الخطوط المتعددة من الصفحة الأولى لمستند PDF.

```csharp
// تحميل ملف PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.PolyLine)
    .Cast<PolylineAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
}     
```

### الحصول على تعليقات المضلع
المثال أدناه يشرح كيفية الحصول على جميع تعليقات الضلع من الصفحة الأولى لمستند PDF.

```csharp
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Polygon)
    .Cast<PolygonAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
} 
```

## حذف الأشكال

طريقة إزالة التعليق من PDF بسيطة جدًا:

* اختر التعليقات لحذفها (اصنع بعض المجموعات)
* كرر على المجموعة باستخدام حلقة foreach، واحذف كل تعليق من مجموعة التعليقات باستخدام طريقة الحذف.

### حذف تعليق الخط

```csharp
// تحميل ملف PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();

foreach (var la in lineAnnotations)
{
    document.Pages[1].Annotations.Delete(la);
}
```

### حذف التعليقات التوضيحية للدائرة والمربع

```csharp
// Load the PDF file
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var figures = document.Pages[1].Annotations
    .Where(a =>
        a.AnnotationType == AnnotationType.Circle
        || a.AnnotationType == AnnotationType.Square);

foreach (var fig in figures)
{
    document.Pages[1].Annotations.Delete(fig);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```

### حذف التعليقات التوضيحية للمضلع وخطوط متعددة

يوضح الجزء التالي من الشفرة كيفية حذف التعليقات التوضيحية للمضلع وخطوط متعددة من ملف PDF.

```csharp
// Load the PDF file
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.PolyLine
                || a.AnnotationType == AnnotationType.Polygon);

foreach (var pa in polyAnnotations)
{
    document.Pages[1].Annotations.Delete(pa);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```
## كيفية إضافة تعليق بالحبر إلى ملف PDF

يمثل التعليق بالحبر "خربشة" باليد تتألف من مسار واحد أو أكثر غير متصلة. عند فتحه، يجب أن يعرض نافذة منبثقة تحتوي على نص الملاحظة المرتبطة.

التعليق بالحبر يمثل خربشة باليد مكونة من نقطة واحدة أو أكثر غير متصلة. يرجى محاولة استخدام مقتطف الكود التالي لإضافة تعليق بالحبر في مستند PDF.

```csharp
// تحميل ملف PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "appartments.pdf"));
Page page = document.Pages[1];

Rectangle arect = new Rectangle(156.574, 521.316, 541.168, 575.703);

IList<Point[]> inkList = new List<Point[]>();
Point[] arrpt = new[]
{
    new Point(209.727,542.263),
    new Point(209.727,541.94),
    new Point(209.727,541.616)
};
inkList.Add(arrpt);

InkAnnotation ia = new InkAnnotation(page, arect, inkList)
{
    Title = "John Smith",
    Subject = "Pencil",
    Color = Color.LightBlue,
    CapStyle = CapStyle.Rounded,
    Opacity = 0.5
};
Border border = new Border(ia)
{
    Width = 25
};
ia.Border = border;
page.Annotations.Add(ia);

// حفظ الملف الناتج
document.Save(System.IO.Path.Combine(_dataDir, "appartments_mod.pdf"));
```
### تعيين عرض خط التعليق الحبري

يمكن تغيير عرض [InkAnnottion](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) باستخدام كائني LineInfo و Border.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
doc.Pages.Add();
IList<Point[]> inkList = new List<Point[]>();
LineInfo lineInfo = new LineInfo();
lineInfo.VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 };
lineInfo.Visibility = true;
lineInfo.LineColor = System.Drawing.Color.Red;
lineInfo.LineWidth = 2;
int length = lineInfo.VerticeCoordinate.Length / 2;
Aspose.Pdf.Point[] gesture = new Aspose.Pdf.Point[length];
for (int i = 0; i < length; i++)
{
   gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
}

inkList.Add(gesture);
InkAnnotation a1 = new InkAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList);
a1.Subject = "Test";
a1.Title = "Title";
a1.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
Border border = new Border(a1);
border.Width = 3;
border.Effect = BorderEffect.Cloudy;
border.Dash = new Dash(1, 1);
border.Style = BorderStyle.Solid;
doc.Pages[1].Annotations.Add(a1);

dataDir = dataDir + "lnkAnnotationLineWidth_out.pdf";
// حفظ الملف الناتج
doc.Save(dataDir);
```

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
    "applicationCategory": "مكتبة تعديل ملفات PDF لـ .NET",
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
### حذف تعليق دائري

الشفرة التالية توضح كيفية حذف تعليق دائري من ملف PDF.

```csharp
public static void DeleteCircleAnnotation()
{
    // تحميل ملف PDF
    Document document = new Document(System.IO.Path.Combine(dataDir, "Appartments_mod.pdf"));
    var circleAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Circle)
        .Cast<CircleAnnotation>();

    foreach (var ca in circleAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(dataDir, "Appartments_del.pdf"));
}
```
