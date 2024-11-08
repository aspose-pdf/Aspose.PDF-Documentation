---
title: استبدال النص في ملف PDF
linktitle: استبدال النص في ملف PDF
type: docs
weight: 40
url: /ar/net/replace-text-in-pdf/
description: تعرف على المزيد حول الطرق المختلفة لاستبدال وإزالة النص من مكتبة Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/replace-text-in-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "استبدال النص في ملف PDF",
    "alternativeHeadline": "استبدال وإزالة النص في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"أناستاسيا هولوب",
        "givenName": "أناستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, استبدال النص, إزالة النص",
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
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "تعرف على المزيد حول الطرق المختلفة لاستبدال وإزالة النص من مكتبة Aspose.PDF لـ .NET."
}
</script>
الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

## استبدال النص في جميع صفحات مستند PDF

{{% alert color="primary" %}}

يمكنك محاولة البحث واستبدال النص في المستند باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت من خلال هذا [الرابط](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

لكي تستطيع استبدال النص في جميع صفحات مستند PDF، عليك أولًا استخدام TextFragmentAbsorber للعثور على العبارة المحددة التي ترغب في استبدالها. بعد ذلك، تحتاج إلى المرور عبر جميع القطع النصية لاستبدال النص وتغيير أي خصائص أخرى. بمجرد الانتهاء من ذلك، كل ما تحتاجه هو حفظ ملف PDF الناتج باستخدام طريقة الحفظ في كائن المستند. الشفرة التالية توضح لك كيفية استبدال النص في جميع الصفحات من مستند PDF.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح المستند
Document pdfDocument = new Document(dataDir + "ReplaceTextAll.pdf");

// إنشاء كائن TextAbsorber للعثور على جميع حالات العبارة المدخلة
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// قبول الامتصاص لجميع الصفحات
pdfDocument.Pages.Accept(textFragmentAbsorber);

// الحصول على قطع النص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// التكرار عبر القطع النصية
foreach (TextFragment textFragment in textFragmentCollection)
{
    // تحديث النص وخصائص أخرى
    textFragment.Text = "TEXT";
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}

dataDir = dataDir + "ReplaceTextAll_out.pdf";
// حفظ مستند PDF الناتج.
pdfDocument.Save(dataDir);
```
## استبدال النص في منطقة معينة بالصفحة

لكي نقوم باستبدال نص في منطقة معينة بالصفحة، أولاً يجب علينا أن نقوم بإنشاء كائن TextFragmentAbsorber، وتحديد منطقة الصفحة باستخدام خاصية TextSearchOptions.Rectangle ثم نقوم بتكرار عملية المرور على جميع الـ TextFragments لاستبدال النص. بمجرد اكتمال هذه العمليات، كل ما يتبقى هو حفظ ملف PDF الناتج باستخدام طريقة Save لكائن الوثيقة. يوضح الجزء التالي من الكود كيفية استبدال النص في جميع صفحات مستند PDF.

```csharp
// تحميل ملف PDF
Aspose.PDF.Document pdf  = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// إنشاء كائن TextFragment Absorber
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// البحث عن النص داخل حدود الصفحة
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// تحديد منطقة الصفحة لخيارات البحث عن النص
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// البحث عن النص من الصفحة الأولى لملف PDF
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// تكرار المرور على كل TextFragment
foreach( Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // تحديث النص إلى أحرف فارغة
    tf.Text = "";
}

// حفظ ملف PDF بعد استبدال النص
pdf.Save("c:/pdftest/TextUpdated.pdf");
```
## استبدال النص بناءً على تعبير نظامي

إذا كنت ترغب في استبدال بعض العبارات بناءً على تعبير نظامي، يجب أولاً أن تجد كل العبارات التي تطابق التعبير النظامي المحدد باستخدام TextFragmentAbsorber. ستحتاج إلى تمرير التعبير النظامي كمعامل إلى مُنشئ TextFragmentAbsorber. كما تحتاج إلى إنشاء كائن TextSearchOptions الذي يحدد ما إذا كان يتم استخدام التعبير النظامي أم لا. بمجرد حصولك على العبارات المطابقة في TextFragments، تحتاج إلى التكرار على كل منها وتحديثها حسب الحاجة. أخيرًا، تحتاج إلى حفظ PDF المُحدث باستخدام طريقة الحفظ في كائن الوثيقة. يوضح لك الشفرة التالية كيفية استبدال النص بناءً على تعبير نظامي.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح الوثيقة
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// إنشاء كائن TextAbsorber للعثور على كل العبارات التي تطابق التعبير النظامي
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // مثل 1999-2000

// تعيين خيار البحث عن النص لتحديد استخدام التعبير النظامي
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// قبول الامتصاص لصفحة واحدة
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// الحصول على مجموعات النصوص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// التكرار عبر القطع
foreach (TextFragment textFragment in textFragmentCollection)
{
    // تحديث النص وخصائص أخرى
    textFragment.Text = "عبارة جديدة";
    // تعيين إلى مثيل لكائن.
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```
## استبدال الخطوط في ملف PDF موجود

Aspose.PDF for .NET يدعم القدرة على استبدال النص في مستند PDF. ومع ذلك، أحيانًا لديك متطلب لاستبدال الخط المستخدم داخل مستند PDF فقط. لذا بدلاً من استبدال النص، يتم استبدال الخط المستخدم فقط. أحد التحميلات الزائدة لمنشئ TextFragmentAbsorber يقبل كائن TextEditOptions كوسيط ويمكننا استخدام قيمة RemoveUnusedFonts من تعداد TextEditOptions.FontReplace لتحقيق متطلباتنا. يوضح الشريط البرمجي التالي كيفية استبدال الخط داخل مستند PDF.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// تحميل ملف PDF المصدر
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// البحث عن فقرات النص وتعيين خيار التحرير كإزالة الخطوط غير المستخدمة
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// قبول الامتصاص لجميع الصفحات
pdfDocument.Pages.Accept(absorber);
// العبور عبر جميع فقرات النص
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // إذا كان اسم الخط هو ArialMT، استبدل اسم الخط بـ Arial
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// حفظ المستند المحدث
pdfDocument.Save(dataDir);
```
## يجب أن يعيد ترتيب محتويات الصفحة تلقائيًا استبدال النص

يدعم Aspose.PDF لـ .NET ميزة البحث واستبدال النص داخل ملف PDF. ومع ذلك، واجه بعض العملاء مؤخرًا مشاكل أثناء استبدال النص عندما يتم استبدال TextFragment معين بمحتويات أصغر ويظهر بعض المسافات الإضافية في PDF الناتج أو في حالة استبدال TextFragment بسلسلة أطول، ثم تتداخل الكلمات مع محتويات الصفحة الحالية. لذا كانت الحاجة لتقديم آلية تضمن أنه بمجرد استبدال النص داخل مستند PDF، يجب إعادة ترتيب المحتويات.

من أجل استيعاب السيناريوهات المذكورة أعلاه، تم تحسين Aspose.PDF لـ .NET بحيث لا تظهر مثل هذه المشاكل عند استبدال النص داخل ملف PDF. يوضح الجزء التالي من الكود كيفية استبدال النص داخل ملف PDF ويجب إعادة ترتيب محتويات الصفحة تلقائيًا.

```csharp
// لأمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// تحميل ملف PDF المصدر
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// إنشاء كائن TextFragment Absorber مع التعبير العادي
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// استبدال كل TextFragment
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // تعيين خط النص الذي يتم استبداله
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // تعيين حجم الخط
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // استبدال النص بسلسلة أكبر من النص الأصلي
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// حفظ PDF الناتج
doc.Save(dataDir);
```
## تقديم الرموز القابلة للاستبدال أثناء إنشاء PDF

الرموز القابلة للاستبدال هي رموز خاصة في سلسلة نصية يمكن استبدالها بمحتوى مقابل في وقت التشغيل. الرموز القابلة للاستبدال التي يدعمها حاليًا نموذج كائن المستند الجديد في فضاء الأسماء Aspose.PDF هي `$P`، `$p`، `\n`، `\r`. يستخدم `$p` و `$P` للتعامل مع ترقيم الصفحات في وقت التشغيل. يتم استبدال `$p` برقم الصفحة التي توجد فيها فئة الفقرة الحالية. يتم استبدال `$P` بإجمالي عدد الصفحات في المستند. عند إضافة `TextFragment` إلى مجموعة الفقرات لمستندات PDF، فإنه لا يدعم تغذية السطر داخل النص. ومع ذلك، من أجل إضافة نص مع تغذية سطر، يرجى استخدام `TextFragment` مع `TextParagraph`:

- استخدم "\r\n" أو Environment.NewLine في TextFragment بدلاً من "\n" الفردي؛
- قم بإنشاء كائن TextParagraph. سيضيف نصًا مع تقسيم النص؛
- أضف TextFragment مع TextParagraph.AppendLine؛
- أضف TextParagraph مع TextBuilder.AppendParagraph.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// تهيئة TextFragment جديد بنص يحتوي على علامات تغذية سطر مطلوبة
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("اسم المتقدم: " + Environment.NewLine + " جو سمو");

// إعداد خصائص الجزء النصي إذا لزم الأمر
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// إنشاء كائن TextParagraph
TextParagraph par = new TextParagraph();

// إضافة TextFragment جديد إلى الفقرة
par.AppendLine(textFragment);

// تعيين موضع الفقرة
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// إنشاء كائن TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// إضافة TextParagraph باستخدام TextBuilder
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```
## الرموز القابلة للتبديل في منطقة الرأس/التذييل

يمكن وضع الرموز القابلة للتبديل أيضًا داخل قسم الرأس/التذييل في ملف PDF. يرجى الاطلاع على المقتطف البرمجي التالي لمعرفة التفاصيل حول كيفية إضافة رمز قابل للتبديل في قسم التذييل.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// تعيين مثيل marginInfo إلى خاصية Margin من sec1.PageInfo
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// إنشاء فقرة نصية تخزن المحتوى لعرضه كرأس
TextFragment t1 = new TextFragment("عنوان التقرير");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("اسم_التقرير");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// إنشاء كائن HeaderFooter للقسم
HeaderFooter hfFoot = new HeaderFooter();
// تعيين كائن HeaderFooter لتذييل الصفحات الفردية والزوجية
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// إضافة فقرة نصية تحتوي على رقم الصفحة الحالي من إجمالي عدد الصفحات
TextFragment t3 = new TextFragment("تم الإنشاء في تاريخ الاختبار");
TextFragment t4 = new TextFragment("اسم التقرير ");
TextFragment t5 = new TextFragment("الصفحة $p من $P");

// إنشاء كائن جدول
Table tab2 = new Table();

// إضافة الجدول إلى مجموعة الفقرات في القسم المطلوب
hfFoot.Paragraphs.Add(tab2);

// تعيين عرض الأعمدة للجدول
tab2.ColumnWidths = "165 172 165";

// إنشاء صفوف في الجدول ثم خلايا في الصفوف
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// تعيين المحاذاة العمودية للنص كمحاذاة وسط
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// إضافة الجدول في مجموعة الفقرات للقسم المطلوب
page.Paragraphs.Add(table);

// تعيين حدود الخلية الافتراضية باستخدام كائن BorderInfo
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// تعيين حدود الجدول باستخدام كائن BorderInfo مخصص آخر
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// إنشاء صفوف في الجدول ثم خلايا في الصفوف
Row row1 = table.Rows.Add();

row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
const string CRLF = "\r\n";
for (int i = 0; i <= 10; i++)
{
    Row row = table.Rows.Add();
    row.IsRowBroken = true;
    for (int c = 0; c <= 2; c++)
    {
        Cell c1;
        if (c == 2)
            c1 = row.Cells.Add("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a" + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "Using Aspose.Total for Java developers can create a wide range of applications.");
        else
            c1 = row.Cells.Add("item1" + c);
        c1.Margin = new MarginInfo();
        c1.Margin.Left = 30;
        c1.Margin.Top = 10;
        c1.Margin.Bottom = 10;
    }
}

dataDir = dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
doc.Save(dataDir);
```
## إزالة الخطوط غير المستخدمة من ملف PDF

يدعم Aspose.PDF لـ .NET ميزة تضمين الخطوط أثناء إنشاء مستند PDF، فضلاً عن القدرة على تضمين الخطوط في ملفات PDF الموجودة. من Aspose.PDF لـ .NET 7.3.0، أصبح يتيح لك أيضًا إزالة الخطوط المكررة أو غير المستخدمة من مستندات PDF.

لتبديل الخطوط، استخدم النهج التالي:

1. استدعاء الفئة [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber).
1. استدعي معلمة TextFragmentAbsorber class’ TextEditOptions.FontReplace.RemoveUnusedFonts. (تزيل الخطوط التي أصبحت غير مستخدمة أثناء استبدال الخط).
1. حدد الخط بشكل فردي لكل قطعة نص.

يستبدل الشيفرة التالية الخط لكل قطع النص لكل صفحات المستند ويزيل الخطوط غير المستخدمة.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// تحميل ملف PDF المصدر
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// تكرار عبر كل قطع النص
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// حفظ المستند المحدث
doc.Save(dataDir);
```

## إزالة كل النصوص من مستند PDF

### إزالة كل النصوص باستخدام العمليات

في بعض عمليات النص، قد تحتاج إلى إزالة كل النصوص من مستند PDF ولهذا، عليك تعيين النص الموجود كقيمة سلسلة فارغة عادةً. النقطة هي أن تغيير النص لكثير من أجزاء النص يستدعي عددًا من عمليات التحقق وتعديل موضع النص. هذه ضرورية في سيناريوهات تحرير النص. الصعوبة هي أنك لا تستطيع تحديد كم عدد أجزاء النص التي سيتم إزالتها في السيناريو الذي يتم فيه معالجتها في حلقة.

لذلك، نوصي باستخدام نهج آخر لسيناريو إزالة كل النصوص من صفحات PDF. يرجى النظر في الشفرة التالية التي تعمل بسرعة كبيرة.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح المستند
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// التكرار عبر جميع صفحات مستند PDF
for (int i = 1; i <= pdfDocument.Pages.Count; i++)
{
    Page page = pdfDocument.Pages[i];
    OperatorSelector operatorSelector = new OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
    // اختيار كل النص في الصفحة
    page.Contents.Accept(operatorSelector);
    // حذف كل النص
    page.Contents.Delete(operatorSelector.Selected);
}
// حفظ المستند
pdfDocument.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
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
```

