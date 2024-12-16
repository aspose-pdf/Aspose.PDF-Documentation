---
title: استبدال النص في PDF عبر بايثون
linktitle: استبدال النص في PDF
type: docs
weight: 40
url: /ar/python-net/replace-text-in-pdf/
description: تعرف على المزيد حول الطرق المختلفة لاستبدال وإزالة النص من Aspose.PDF لبايثون عبر مكتبة .NET.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "استبدال النص في PDF",
    "alternativeHeadline": "استبدال وإزالة النص في ملف PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثائق PDF",
    "keywords": "pdf، python، استبدال النص، إزالة النص",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/replace-text-in-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "تعرف على المزيد حول الطرق المختلفة لاستبدال وإزالة النص من Aspose.PDF لبايثون عبر مكتبة .NET."
}
</script>


## استبدال النص في جميع صفحات وثيقة PDF

{{% alert color="primary" %}}

يمكنك محاولة العثور على النص واستبداله في الوثيقة باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت من خلال هذا [الرابط](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

من أجل استبدال النص في جميع صفحات وثيقة PDF، تحتاج أولاً إلى استخدام [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) للعثور على العبارة المحددة التي تريد استبدالها. بعد ذلك، تحتاج إلى المرور عبر جميع عناصر TextFragments لاستبدال النص وتغيير أي سمات أخرى. بمجرد القيام بذلك، تحتاج فقط إلى حفظ ملف PDF الناتج باستخدام طريقة Save لكائن Document. يوضح لك مقتطف الشيفرة التالي كيفية استبدال النص في جميع صفحات وثيقة PDF.

```python

    import aspose.pdf as ap

    # فتح الوثيقة
    document = ap.Document(input_pdf)

    # إنشاء كائن TextAbsorber للعثور على جميع حالات عبارة البحث المدخلة
    absorber = ap.text.TextFragmentAbsorber("format")

    # قبول الكائن لجميع الصفحات
    document.pages.accept(absorber)

    # الحصول على أجزاء النص المستخرجة
    collection = absorber.text_fragments

    # حلقة خلال الأجزاء
    for text_fragment in collection:
        # تحديث النص وخصائص أخرى
        text_fragment.text = "FORMAT"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
        text_fragment.text_state.font_size = 22
        text_fragment.text_state.foreground_color = ap.Color.blue
        text_fragment.text_state.background_color = ap.Color.green

    # حفظ الوثيقة
    document.save(output_pdf)
```


## استبدال النص في منطقة معينة من الصفحة

من أجل استبدال النص في منطقة معينة من الصفحة، أولاً، نحتاج إلى إنشاء كائن TextFragmentAbsorber، تحديد منطقة الصفحة باستخدام خاصية TextSearchOptions.Rectangle ومن ثم التكرار عبر جميع TextFragments لاستبدال النص. بمجرد إتمام هذه العمليات، نحتاج فقط إلى حفظ ملف PDF الناتج باستخدام طريقة Save لكائن Document. يوضح لك مثال الشيفرة التالي كيفية استبدال النص في جميع صفحات مستند PDF.

```python
// تحميل ملف PDF
Aspose.PDF.Document pdf  = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// إنشاء كائن TextFragment Absorber
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// البحث عن النص ضمن حدود الصفحة
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// تحديد منطقة الصفحة لخيارات البحث عن النص
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// البحث عن النص من الصفحة الأولى لملف PDF
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// التكرار عبر كل TextFragment
foreach( Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // تحديث النص إلى أحرف فارغة
    tf.Text = "";
}

// حفظ ملف PDF المحدث بعد استبدال النص
pdf.Save("c:/pdftest/TextUpdated.pdf");
```


## استبدال النص بناءً على تعبير منتظم

إذا كنت ترغب في استبدال بعض العبارات بناءً على تعبير منتظم، فيجب عليك أولاً العثور على جميع العبارات التي تطابق ذلك التعبير المنتظم باستخدام TextFragmentAbsorber. ستحتاج إلى تمرير التعبير المنتظم كمعامل إلى منشئ TextFragmentAbsorber. تحتاج أيضًا إلى إنشاء كائن TextSearchOptions لتحديد ما إذا كان يتم استخدام التعبير المنتظم أم لا. بمجرد الحصول على العبارات المطابقة في TextFragments، تحتاج إلى التكرار خلالها وتحديثها حسب الحاجة. أخيرًا، تحتاج إلى حفظ ملف PDF المحدث باستخدام طريقة Save لكائن Document. يوضح لك مقتطف الكود التالي كيفية استبدال النص بناءً على تعبير منتظم.

```python
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الانتقال إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح المستند
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// إنشاء كائن TextAbsorber للعثور على جميع العبارات التي تطابق التعبير المنتظم
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // مثل 1999-2000

// تعيين خيار البحث عن النص لتحديد استخدام التعبير المنتظم
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// قبول الماص لجملة واحدة
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// الحصول على أجزاء النص المستخرجة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// التكرار من خلال الأجزاء
foreach (TextFragment textFragment in textFragmentCollection)
{
    // تحديث النص والخصائص الأخرى
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

يدعم Aspose.PDF for Python عبر .NET القدرة على استبدال النص في مستند PDF. ومع ذلك، في بعض الأحيان قد يكون لديك متطلب لاستبدال الخط المستخدم داخل مستند PDF فقط. لذلك بدلاً من استبدال النص، يتم استبدال الخط المستخدم فقط. يقبل أحد التحميلات الزائدة لبناء TextFragmentAbsorber كائن TextEditOptions كمعامل ويمكننا استخدام القيمة RemoveUnusedFonts من تعداد TextEditOptions.FontReplace لتحقيق متطلباتنا. يوضح مقتطف الشيفرة التالي كيفية استبدال الخط داخل مستند PDF.

```python
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// تحميل ملف PDF المصدر
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// البحث عن أجزاء النص وتعيين خيار التحرير كإزالة الخطوط غير المستخدمة
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// قبول الممتص لجميع الصفحات
pdfDocument.Pages.Accept(absorber);
// التجول خلال جميع أجزاء النص
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // إذا كان اسم الخط ArialMT، استبدل اسم الخط بـ Arial
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// حفظ المستند المحدث
pdfDocument.Save(dataDir);
```


## يجب أن تعيد ميزة استبدال النص ترتيب محتويات الصفحة تلقائيًا

Aspose.PDF لـ Python عبر .NET يدعم ميزة البحث واستبدال النص داخل ملف PDF. ومع ذلك، واجه بعض العملاء مؤخرًا مشاكل أثناء استبدال النص عندما يتم استبدال TextFragment معين بمحتويات أصغر وتظهر بعض المساحات الإضافية في PDF الناتج أو في حالة استبدال TextFragment بسلسلة أطول، فإن الكلمات تتداخل مع محتويات الصفحة الموجودة. لذلك كانت الحاجة إلى تقديم آلية بمجرد استبدال النص داخل مستند PDF، يجب إعادة ترتيب المحتويات.

من أجل تلبية السيناريوهات المذكورة أعلاه، تم تحسين Aspose.PDF لـ Python عبر .NET بحيث لا تظهر مثل هذه المشاكل عند استبدال النص داخل ملف PDF. يوضح مقطع الشفرة التالي كيفية استبدال النص داخل ملف PDF ويجب إعادة ترتيب محتويات الصفحة تلقائيًا.

```python
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الانتقال إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// تحميل ملف PDF المصدر
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// إنشاء كائن TextFragment Absorber مع تعبير منتظم
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// استبدال كل TextFragment
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // تعيين خط الجزء النصي الذي يتم استبداله
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // تعيين حجم الخط
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // استبدال النص بسلسلة أكبر من العنصر النائب
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// حفظ PDF الناتج
doc.Save(dataDir);
```


## عرض الرموز القابلة للاستبدال أثناء إنشاء PDF

الرموز القابلة للاستبدال هي رموز خاصة في سلسلة النص يمكن استبدالها بالمحتوى المقابل في وقت التشغيل. الرموز القابلة للاستبدال المدعومة حاليًا بواسطة نموذج كائن المستند الجديد في مساحة الأسماء Aspose.PDF هي `$P`, `$p,` `\n`, `\r`. يتم استخدام `$p` و `$P` للتعامل مع ترقيم الصفحات في وقت التشغيل. يتم استبدال `$p` برقم الصفحة التي توجد فيها الفقرة الحالية. ويتم استبدال `$P` بعدد الصفحات الإجمالي في المستند. عند إضافة `TextFragment` إلى مجموعة الفقرات في مستندات PDF، فإنه لا يدعم تغذية السطر داخل النص. ومع ذلك، لإضافة نص مع تغذية السطر، يرجى استخدام `TextFragment` مع `TextParagraph`:

- استخدم "\r\n" أو Environment.NewLine في TextFragment بدلاً من "\n" الفردي؛
- إنشاء كائن TextParagraph. سيضيف النص مع تقسيم السطر؛
- أضف TextFragment مع TextParagraph.AppendLine؛
- أضف TextParagraph مع TextBuilder.AppendParagraph.

```python
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// تهيئة TextFragment جديد مع النص الذي يحتوي على علامات الانتقال اللازمة
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("اسم المتقدم: " + Environment.NewLine + " جو سمو");

// ضبط خصائص جزء النص إذا لزم الأمر
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// إنشاء كائن TextParagraph
TextParagraph par = new TextParagraph();

// إضافة TextFragment الجديد إلى الفقرة
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


## الرموز القابلة للاستبدال في منطقة الرأس/التذييل

يمكن وضع الرموز القابلة للاستبدال أيضًا داخل قسم الرأس/التذييل في ملف PDF. يُرجى إلقاء نظرة على مقتطف الشيفرة التالي للحصول على تفاصيل حول كيفية إضافة رمز قابل للاستبدال في قسم التذييل.

```python
// للحصول على أمثلة كاملة وملفات البيانات، يُرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// تعيين مثيل marginInfo إلى خاصية هامش الصفحة
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// إنشاء فقرة نصية ستخزن المحتوى المعروض كرأس
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
// تعيين كائن HeaderFooter للتذييل الفردي والزوجي
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// إضافة فقرة نصية تحتوي على رقم الصفحة الحالي من إجمالي عدد الصفحات
TextFragment t3 = new TextFragment("تم الإنشاء في تاريخ الاختبار");
TextFragment t4 = new TextFragment("اسم التقرير ");
TextFragment t5 = new TextFragment("صفحة $p من $P");

// إنشاء كائن جدول
Table tab2 = new Table();

// إضافة الجدول إلى مجموعة الفقرات في القسم المطلوب
hfFoot.Paragraphs.Add(tab2);

// تعيين عرض الأعمدة في الجدول
tab2.ColumnWidths = "165 172 165";

// إنشاء صفوف في الجدول ثم خلايا في الصفوف
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// تعيين محاذاة النص الرأسية كمحاذاة وسط
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

// Sec1.Paragraphs.Add(New Text("Aspose.Total for Java هو تجميع لكل مكونات جافا التي تقدمها Aspose. يتم تجميعه على أساس يومي لضمان احتوائه على أحدث إصدارات كل مكونات جافا الخاصة بنا. باستخدام Aspose.Total for Java يمكن للمطورين إنشاء مجموعة واسعة من التطبيقات." + CRLF + "Aspose.Total for Java هو تجميع لكل مكونات جافا التي تقدمها Aspose. يتم تجميعه على أساس يومي لضمان احتوائه على أحدث إصدارات كل مكونات جافا الخاصة بنا. باستخدام Aspose.Total for Java يمكن للمطورين إنشاء مجموعة واسعة من التطبيقات." + CRLF + "Aspose.Total for Java هو تجميع لكل مكونات جافا التي تقدمها Aspose. يتم تجميعه على أساس يومي لضمان احتوائه على أحدث إصدارات كل مكونات جافا الخاصة بنا. باستخدام Aspose.Total for Java يمكن للمطورين إنشاء مجموعة واسعة من التطبيقات."))
Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// إضافة الجدول إلى مجموعة الفقرات في القسم المطلوب
page.Paragraphs.Add(table);

// تعيين الحدود الافتراضية للخلية باستخدام كائن BorderInfo
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
            c1 = row.Cells.Add("Aspose.Total for Java هو تجميع لكل مكونات جافا التي تقدمها Aspose. يتم تجميعه على أساس يومي لضمان احتوائه على أحدث إصدارات كل مكونات جافا الخاصة بنا." + CRLF + "يتم تجميعه على أساس يومي لضمان احتوائه على أحدث إصدارات كل مكونات جافا الخاصة بنا." + CRLF + "باستخدام Aspose.Total for Java يمكن للمطورين إنشاء مجموعة واسعة من التطبيقات.");
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

تدعم Aspose.PDF for Python عبر .NET ميزة تضمين الخطوط أثناء إنشاء مستند PDF، بالإضافة إلى القدرة على تضمين الخطوط في ملفات PDF الموجودة. اعتبارًا من Aspose.PDF for Python عبر .NET 7.3.0، فإنه يتيح لك أيضًا إزالة الخطوط المكررة أو غير المستخدمة من مستندات PDF.

لاستبدال الخطوط، استخدم النهج التالي:

1. استدعاء فئة [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. استدعاء معلمة TextFragmentAbsorber في TextEditOptions.FontReplace.RemoveUnusedFonts. (هذا يزيل الخطوط التي أصبحت غير مستخدمة أثناء استبدال الخطوط).
1. تعيين الخط بشكل فردي لكل جزء نصي.

يستبدل مقتطف الشيفرة التالي الخط لجميع الأجزاء النصية من جميع صفحات المستند ويزيل الخطوط غير المستخدمة.

```python
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الانتقال إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// تحميل ملف PDF المصدر
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// التكرار عبر جميع الأجزاء النصية
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// حفظ المستند المحدث
doc.Save(dataDir);
```


## إزالة كل النص من مستند PDF

### إزالة كل النص باستخدام المشغلين

في بعض عمليات النص، تحتاج إلى إزالة كل النص من مستند PDF ولهذا، تحتاج عادةً إلى تعيين النص الموجود كقيمة سلسلة فارغة. النقطة هي أن تغيير النص لعدد كبير من الأجزاء النصية يستدعي عددًا من عمليات التحقق وتعديل موضع النص. إنها أساسية في سيناريوهات تحرير النص. الصعوبة تكمن في أنك لا يمكنك تحديد عدد الأجزاء النصية التي سيتم إزالتها في السيناريو حيث تتم معالجتها في حلقة.

لذلك، نوصي باستخدام نهج آخر في سيناريو إزالة كل النص من صفحات PDF. يرجى النظر في الكود التالي الذي يعمل بسرعة كبيرة.

```python
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الانتقال إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// افتح المستند
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// حلقة عبر جميع صفحات مستند PDF
for (int i = 1; i <= pdfDocument.Pages.Count; i++)
{
    Page page = pdfDocument.Pages[i];
    OperatorSelector operatorSelector = new OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
    // حدد كل النص في الصفحة
    page.Contents.Accept(operatorSelector);
    // احذف كل النص
    page.Contents.Delete(operatorSelector.Selected);
}
// احفظ المستند
pdfDocument.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
```


{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF لبايثون عبر مكتبة .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "بريطانيا",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة معالجة PDF لبايثون",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "ويندوز، ماك أو إس، لينكس",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}