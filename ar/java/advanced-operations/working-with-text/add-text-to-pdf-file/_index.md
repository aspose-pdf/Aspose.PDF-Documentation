---
title: إضافة نص إلى ملف PDF 
linktitle: إضافة نص إلى ملف PDF
type: docs
weight: 10
url: ar/java/add-text-to-pdf-file/
description: يصف هذا المقال مختلف الجوانب المتعلقة بالعمل مع النص في Aspose.PDF. تعرف على كيفية إضافة النص إلى PDF، إضافة شظايا HTML، أو استخدام الخطوط المخصصة OTF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

لإضافة نص إلى ملف PDF موجود:

1. افتح ملف PDF المدخل باستخدام كائن Document.
2. احصل على الصفحة المحددة التي ترغب في إضافة النص إليها.
3. قم بإنشاء كائن TextFragment بالنص المدخل إلى جانب خصائص النص الأخرى. يتيح لك كائن TextBuilder الذي يتم إنشاؤه من تلك الصفحة المحددة – التي ترغب في إضافة النص إليها – إضافة كائن TextFragment إلى الصفحة باستخدام طريقة AppendText.
4. استدعاء طريقة Save لكائن Document واحفظ ملف PDF الناتج.

## إضافة نص

يظهر لك مقتطف الشيفرة التالي كيفية إضافة نص في ملف PDF موجود.

```java
public static void AddingText() {
    // تحميل ملف PDF
    Document document = new Document(_dataDir + "sample.pdf");

    // احصل على الصفحة المحددة
    Page pdfPage = document.getPages().get_Item(1);
    // إنشاء جزء النص
    TextFragment textFragment = new TextFragment("Aspose.PDF");
    textFragment.setPosition(new Position(80, 700));

    // تعيين خصائص النص
    textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
    textFragment.getTextState().setFontSize(14);
    textFragment.getTextState().setForegroundColor(Color.getBlue());
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());

    // إنشاء كائن TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // إلحاق جزء النص بصفحة PDF
    textBuilder.appendText(textFragment);

    // حفظ مستند PDF الناتج.
    document.save(_dataDir + "AddText_out.pdf");
}
```


## تحميل الخط من التدفق

يُظهر مقطع الشيفرة التالي كيفية تحميل الخط من كائن التدفق عند إضافة نص إلى مستند PDF.

```java
import com.aspose.pdf.*;
import com.aspose.pdf.text.FontTypes;

import java.io.FileInputStream;
import java.io.FileNotFoundException;  
//...
public static void LoadingFontFromStream() throws FileNotFoundException{
    
    String fontFile = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf";

    // تحميل ملف PDF المدخل
    Document doc = new Document(_dataDir + "input.pdf");
    // إنشاء كائن مُنشئ النص للصفحة الأولى من المستند
    TextBuilder textBuilder = new TextBuilder(doc.getPages().get_Item(1));
    // إنشاء قطعة نص مع سلسلة مثال
    TextFragment textFragment = new TextFragment("Hello world");
    
    if (fontFile != "")
    {
        // تحميل الخط TrueType إلى كائن التدفق
        FileInputStream fontStream=new FileInputStream(fontFile);            
        // تعيين اسم الخط لسلسلة النص
        textFragment.getTextState().setFont (FontRepository.openFont(fontStream, FontTypes.TTF));
        // تحديد الموقع لقطعة النص
        textFragment.setPosition(new Position(10, 10));
        // إضافة النص إلى مُنشئ النص بحيث يمكن وضعه فوق ملف PDF
        textBuilder.appendText(textFragment);
        
        _dataDir = _dataDir + "LoadingFontFromStream_out.pdf";
    
        // حفظ مستند PDF الناتج.
        doc.save(_dataDir); 
    }       
}
```


## إضافة نص باستخدام TextParagraph

يوضح لك مقتطف الشفرة التالي كيفية إضافة نص في مستند PDF باستخدام فئة [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph).

```java
public static void AddTextUsingTextParagraph() {
    // افتح المستند
    Document doc = new Document();
    // أضف صفحة إلى مجموعة صفحات كائن المستند
    Page page = doc.getPages().add();
    TextBuilder builder = new TextBuilder(page);
    // قم بإنشاء فقرة نصية
    TextParagraph paragraph = new TextParagraph();
    // قم بتعيين المسافة البادئة للأسطر اللاحقة
    paragraph.setSubsequentLinesIndent (20);
    // حدد الموقع لإضافة TextParagraph
    paragraph.setRectangle(new Rectangle(100, 300, 200, 700));
    // حدد وضع التفاف الكلمات
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    // أنشئ جزء نصي
    TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
    fragment1.getTextState().setFont (FontRepository.findFont("Times New Roman"));
    fragment1.getTextState().setFontSize (12);
    // أضف الجزء إلى الفقرة
    paragraph.appendLine(fragment1);
    // أضف الفقرة
    builder.appendParagraph(paragraph);

    _dataDir = _dataDir + "AddTextUsingTextParagraph_out.pdf";

    // احفظ مستند PDF الناتج.
    doc.save(_dataDir);        
}
```


## إضافة رابط تشعبي إلى TextSegment

قد تحتوي صفحة PDF على كائن أو أكثر من TextFragment، حيث يمكن لكل كائن TextFragment أن يحتوي على مثيل أو أكثر من TextSegment. من أجل تعيين رابط تشعبي لـ TextSegment، يمكن استخدام خاصية Hyperlink لفئة TextSegment أثناء توفير كائن من مثيل Aspose.Pdf.WebHyperlink. يرجى محاولة استخدام مقتطف الشيفرة التالي لتحقيق هذا المتطلب.

```java
public static void AddHyperlinkToTextSegment() {
    // إنشاء مثيل للمستند
    Document doc = new Document();
    // إضافة صفحة إلى مجموعة الصفحات لملف PDF
    Page page1 = doc.getPages().add();

    // إنشاء مثيل TextFragment
    TextFragment tf = new TextFragment("Sample Text Fragment");
    // تعيين المحاذاة الأفقية لـ TextFragment
    tf.setHorizontalAlignment(HorizontalAlignment.Right);

    // إنشاء TextSegment مع نص عينة
    TextSegment segment = new TextSegment(" ... Text Segment 1...");
    // إضافة المقطع إلى مجموعة المقاطع لـ TextFragment
    tf.getSegments().add(segment);

    // إنشاء TextSegment جديد
    segment = new TextSegment("Link to Google");
    // إضافة المقطع إلى مجموعة المقاطع لـ TextFragment

    tf.getSegments().add(segment);

    // تعيين الرابط التشعبي لـ TextSegment
    segment.setHyperlink(new com.aspose.pdf.WebHyperlink("www.aspose.com"));

    // تعيين اللون الأمامي لمقطع النص
    segment.getTextState().setForegroundColor(com.aspose.pdf.Color.getBlue());

    // تعيين تنسيق النص كميلان
    segment.getTextState().setFontStyle(FontStyles.Italic);

    // إنشاء كائن TextSegment آخر
    segment = new TextSegment("TextSegment without hyperlink");

    // إضافة المقطع إلى مجموعة المقاطع لـ TextFragment
    tf.getSegments().add(segment);

    // إضافة TextFragment إلى مجموعة الفقرات لكائن الصفحة
    page1.getParagraphs().add(tf);

    _dataDir = _dataDir + "AddHyperlinkToTextSegment_out.pdf";

    // حفظ مستند PDF الناتج.
    doc.save(_dataDir);

}
```


## استخدام خط OTF

تقدم Aspose.PDF لبرنامج Java ميزة استخدام الخطوط المخصصة/TrueType أثناء إنشاء/معالجة محتويات ملف PDF بحيث يتم عرض محتويات الملف باستخدام محتويات أخرى غير الخطوط الافتراضية للنظام. بدءًا من إصدار Aspose.PDF for Java 10.4.0، قمنا بتوفير الدعم للخطوط المفتوحة.

```java
public static void UseOTFFont() {
    // إنشاء مثيل وثيقة جديد
    Document pdfDocument = new Document();
    // إضافة صفحة إلى مجموعة صفحات ملف PDF
    Page page = pdfDocument.getPages().add();
    // إنشاء مثيل TextFragment مع نص عينة
    TextFragment fragment = new TextFragment("نص عينة في خط OTF");
    // أو يمكنك حتى تحديد مسار خط OTF في دليل النظام
    fragment.getTextState().setFont(FontRepository.openFont("/home/aspose/.fonts/Montserrat-Black.otf"));
    // تحديد تضمين الخط داخل ملف PDF، بحيث يتم عرضه بشكل صحيح،
    // حتى إذا لم يتم تثبيت الخط المحدد / الموجود على الجهاز الهدف
    fragment.getTextState().getFont().setEmbedded(true);
    // إضافة TextFragment إلى مجموعة الفقرات المثيل الصفحة
    page.getParagraphs().add(fragment);
    // حفظ الوثيقة PDF الناتجة.
    pdfDocument.save(_dataDir + "OTFFont_out.pdf");
}
```


## إضافة سلسلة HTML باستخدام DOM

تحتوي فئة Aspose.Pdf.Generator.Text على خاصية تسمى IsHtmlTagSupported والتي تجعل من الممكن إضافة علامات/محتويات HTML إلى ملفات PDF. يتم عرض المحتوى المضاف في علامات HTML الأصلية بدلاً من الظهور كسلسلة نصية بسيطة. لدعم ميزة مماثلة في نموذج كائن المستند الجديد (DOM) في مساحة الأسماء Aspose.Pdf، تم تقديم فئة HtmlFragment.

يمكن استخدام كائن [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlFragment) لتحديد محتويات HTML التي يجب وضعها داخل ملف PDF. مشابهًا لـ TextFragment، يعتبر HtmlFragment كائنًا على مستوى الفقرة ويمكن إضافته إلى مجموعة الفقرات لكائن الصفحة. تعرض الشيفرات البرمجية التالية الخطوات اللازمة لوضع محتويات HTML داخل ملف PDF باستخدام نهج DOM.

```java
public static void AddingHtmlString() {
    // إنشاء كائن المستند
    Document doc = new Document();
    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    Page page = doc.getPages().add();
    // إنشاء كائن HtmlFragment مع محتويات HTML
    HtmlFragment title = new HtmlFragment("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");
    // تعيين MarginInfo لتفاصيل الهوامش
    MarginInfo Margin = new MarginInfo();
    Margin.setBottom(10);
    Margin.setTop(200);
    // تعيين معلومات الهوامش
    title.setMargin(Margin);
    // إضافة كائن HTML Fragment إلى مجموعة الفقرات في الصفحة
    page.getParagraphs().add(title);
    // حفظ ملف PDF
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


الكود المقتطف التالي يوضح الخطوات لكيفية إضافة قوائم HTML مرتبة إلى المستند:

```java
public static void AddHTMLOrderedListIntoDocuments() {
    // إنشاء كائن Document
    Document doc = new Document();
    // إنشاء كائن HtmlFragment مع الجزء المقابل من HTML
    HtmlFragment t = new HtmlFragment(
            "<div style=\"font-family: sans-serif\"><ul><li>الأول</li><li>الثاني</li><li>الثالث</li><li>الرابع</li><li>الخامس</li></ul><p>نص بعد القائمة.</p><p>السطر التالي<br/>السطر الأخير</p></div>");
    // إضافة صفحة في مجموعة الصفحات
    Page page = doc.getPages().add();
    // إضافة HtmlFragment داخل الصفحة
    page.getParagraphs().add(t);
    // حفظ ملف PDF الناتج
    doc.save(_dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
}
```

يمكنك أيضًا تعيين تنسيق سلسلة HTML باستخدام كائن TextState كما يلي:

```java
public static void AddHTMLStringFormatting() {
    // إنشاء كائن Document
    Document doc = new Document();
    // إضافة صفحة إلى مجموعة صفحات ملف PDF
    Page page = doc.getPages().add();
    // إنشاء HtmlFragment مع محتويات HTML
    HtmlFragment title = new HtmlFragment("<h1><strong>عرض سلسلة HTML</strong></h1>");
    TextState textState = new TextState(12);
    textState.setFont(FontRepository.findFont("Calibri"));
    textState.setForegroundColor(Color.getGreen());
    textState.setBackgroundColor(Color.getCoral());
    title.setTextState(textState);

    // إضافة HTML Fragment إلى مجموعة الفقرات في الصفحة
    page.getParagraphs().add(title);
    // حفظ ملف PDF
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


في حالة إذا قمت بتعيين قيم سمات النص عبر ترميز HTML ثم قدمت نفس القيم في خصائص TextState، فإنها ستقوم بالكتابة فوق معلمات HTML بواسطة خصائص من نموذج TextState. توضح مقتطفات الشيفرة التالية السلوك الموضح.

```java
public static void AddHTMLUsingDOMAndOverwrite() {
    // إنشاء كائن المستند
    Document doc = new Document();
    // إضافة صفحة إلى مجموعة صفحات ملف PDF
    Page page = doc.getPages().add();
    // إنشاء HtmlFragment مع محتويات HTML
    HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");
    // سيتم إعادة تعيين نوع الخط من 'Verdana' إلى 'Arial'
    title.setTextState(new TextState("Arial Black"));
    title.setTextState(new TextState(20));
    // تعيين معلومات الهامش السفلي
    title.getMargin().setBottom(10);
    // تعيين معلومات الهامش العلوي
    title.getMargin().setTop(400);
    // إضافة جزء HTML إلى مجموعة الفقرات في الصفحة
    page.getParagraphs().add(title);
    // حفظ ملف PDF
    doc.save(_dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
}
```


## الهوامش والتذييلات (DOM)

تشير الهوامش إلى ملاحظات في نص ورقتك باستخدام أرقام متسلسلة صغيرة. يتم إزاحة الملاحظة الفعلية ويمكن أن تظهر كحاشية في أسفل الصفحة.

### إضافة حاشية

في نظام الإشارة بالحواشي، أشر إلى مرجع بواسطة:

- وضع رقم صغير فوق السطر مباشرة بعد المادة المصدرية. يُطلق على هذا الرقم معرف الملاحظة. يجلس قليلاً فوق سطر النص.
- وضع نفس الرقم، يتبعه اقتباس لمصدره، في أسفل الصفحة. يجب أن تكون الحواشي رقمية وتسلسلية: المرجع الأول هو 1، والثاني هو 2، وهكذا.

ميزة استخدام الحواشي هي أن القارئ يمكنه ببساطة إلقاء نظره إلى أسفل الصفحة لاكتشاف مصدر المرجع الذي يهمه.

يرجى اتباع الخطوات المحددة أدناه لإنشاء حاشية:

- إنشاء مثيل لوثيقة
- إنشاء كائن صفحة
- إنشاء كائن TextFragment

- إنشاء مثيل لملاحظة وتمرير قيمتها إلى خاصية TextFragment.FootNote
 - أضف TextFragment إلى مجموعة الفقرات في مثيل الصفحة

### نمط خط مخصص لـ FootNote

يوضح المثال التالي كيفية إضافة الحواشي السفلية إلى أسفل صفحة Pdf وتحديد نمط خط مخصص.

```java
public static void AddFootNote() {
    // إنشاء مثيل وثيقة
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Demo");
    t.setFootNote(note);

    // إنشاء مثيل TextFragment
    TextFragment text = new TextFragment("Hello World");
    // تعيين قيمة FootNote لـ TextFragment
    text.setFootNote(new Note("foot note for test text 1"));
    // أضف TextFragment إلى مجموعة الفقرات في الصفحة الأولى من الوثيقة
    page.getParagraphs().add(text);
    // إنشاء TextFragment الثاني
    text = new TextFragment("Aspose.Pdf for Java");
    // تعيين FootNote للجزء النصي الثاني
    text.setFootNote(new Note("foot note for test text 2"));
    // أضف الجزء النصي الثاني إلى مجموعة الفقرات في ملف PDF
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


يمكننا تعيين تنسيق تسمية الحاشية (معرف الملاحظة) باستخدام كائن TextState كما يلي:

```java
public static void AddCustomFootNoteLabel() {
    // إنشاء مثيل للمستند
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Demo");
    t.setFootNote(note);

    // إنشاء مثيل لـ TextFragment
    TextFragment text = new TextFragment("Hello World");
    // تعيين قيمة الحاشية لـ TextFragment
    text.setFootNote(new Note("foot note for test text 1"));
    text.getFootNote().setText("21");
    TextState ts = new TextState();
    ts.setForegroundColor(Color.getBlue());
    ts.setFontStyle(FontStyles.Italic);
    text.getFootNote().setTextState(ts);

    // إضافة TextFragment إلى مجموعة الفقرات في الصفحة الأولى من المستند
    page.getParagraphs().add(text);
    // إنشاء TextFragment ثاني
    text = new TextFragment("Aspose.Pdf for Java");
    // تعيين حاشية لنص الفقرة الثانية
    text.setFootNote(new Note("foot note for test text 2"));
    // إضافة النص الثاني إلى مجموعة الفقرات في ملف PDF
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


### تخصيص تسمية الحاشية السفلية

بشكل افتراضي، يبدأ ترقيم الحاشية السفلية من 1 ويتزايد. ومع ذلك، قد يكون لدينا متطلب لتعيين تسمية حاشية سفلية مخصصة. من أجل تحقيق هذا المتطلب، يرجى تجربة استخدام مقتطف الشيفرة التالي

```java
public static void CustomFootNote_Label() {
    // إنشاء مثيل للمستند
    Document document = new Document();
    // إضافة صفحة إلى مجموعة صفحات PDF
    Page page = document.getPages().add();
    // إنشاء كائن GraphInfo
    GraphInfo graph = new GraphInfo();
    // تعيين عرض الخط كـ 2
    graph.setLineWidth(2);
    // تعيين اللون لكائن الرسم
    graph.setColor(Color.getRed());
    // تعيين قيمة مصفوفة الشرطات كـ 3
    graph.setDashArray(new int[] { 3 });
    // تعيين قيمة مرحلة الشرطات كـ 1
    graph.setDashPhase(1);
    // تعيين نمط خط الحاشية السفلية للصفحة كـ graph
    page.setNoteLineStyle(graph);

    // إنشاء مثيل TextFragment
    TextFragment text = new TextFragment("Hello World");
    // تعيين قيمة الحاشية السفلية لـ TextFragment
    text.setFootNote(new Note("حاشية سفلية لنص الاختبار 1"));
    // تحديد تسمية مخصصة للحاشية السفلية
    text.getFootNote().setText(" Aspose(2021)");
    // إضافة TextFragment إلى مجموعة الفقرات في الصفحة الأولى من المستند
    page.getParagraphs().add(text);

    document.save(_dataDir + "CustomizeFootNoteLabel_out.pdf");
}
```


## إضافة صورة وجدول إلى الحاشية

في الإصدارات السابقة، تم توفير دعم الحاشية ولكن كان ينطبق فقط على كائن TextFragment. ومع ذلك، بدءًا من إصدار Aspose.PDF for Java 10.7.0، يمكنك أيضًا إضافة حاشية إلى كائنات أخرى داخل مستند PDF مثل الجدول والخلايا وغيرها. يوضح مقتطف الشيفرة التالي الخطوات لإضافة حاشية إلى كائن TextFragment ثم إضافة كائن صورة وجدول إلى مجموعة الفقرات في قسم الحاشية.

```java
public static void AddingImageAndTableToFootnote() {
    // إنشاء مثيل للمستند
    Document document = new Document();
    // إضافة صفحة إلى مجموعة الصفحات في PDF
    Page page = document.getPages().add();
    // إنشاء مثيل TextFragment
    TextFragment text = new TextFragment("Hello World");

    page.getParagraphs().add(text);

    text.setFootNote(new Note());
    Image image = new Image();
    image.setFile(_dataDir + "aspose-logo.jpg");
    image.setFixHeight(20);
    text.getFootNote().getParagraphs().add(image);
    TextFragment footNote = new TextFragment("footnote text");
    footNote.getTextState().setFontSize(20);
    footNote.setInLineParagraph(true);
    text.getFootNote().getParagraphs().add(footNote);
    Table table = new Table();
    table.getRows().add().getCells().add().getParagraphs().add(new TextFragment("Row 1 Cell 1"));
    text.getFootNote().getParagraphs().add(table);

    page.getParagraphs().add(text);

    document.save(_dataDir + "AddImageAndTable_out.pdf");
}
```


## كيفية إنشاء الحواشي الختامية

الحاشية الختامية هي إشارة مصدر تشير القراء إلى مكان محدد في نهاية الورقة حيث يمكنهم العثور على مصدر المعلومات أو الكلمات المقتبسة أو المذكورة في الورقة. عند استخدام الحواشي الختامية، تتبع جملتك المقتبسة أو المفهرسة أو المواد الملخصة برقم مرتفع.

يوضح المثال التالي كيفية إضافة حاشية ختامية في صفحة PDF.

```java
public static void HowToCreateEndNotes() {
    Document doc = new Document();
    // إضافة صفحة إلى مجموعة الصفحات في PDF
    Page page = doc.getPages().add();
    // إنشاء مثيل TextFragment
    TextFragment text = new TextFragment("Hello World");
    // تعيين قيمة الحاشية الختامية لـ TextFragment
    text.setEndNote(new Note("sample End note"));
    // تحديد تسمية مخصصة للحاشية الختامية
    text.getEndNote().setText(" Aspose(2021)");
    // إضافة TextFragment إلى مجموعة الفقرات في الصفحة الأولى من المستند
    page.getParagraphs().add(text);
    // حفظ ملف PDF
    doc.save(_dataDir + "EndNote.pdf");
}
```


## نص وصورة كفقرة مدمجة

التخطيط الافتراضي لملف PDF هو تخطيط تدفق (من الأعلى إلى اليسار إلى الأسفل إلى اليمين). لذلك، تتم إضافة كل عنصر جديد يتم إضافته إلى ملف PDF في تدفق الزاوية السفلية اليمنى. ومع ذلك، قد يكون لدينا متطلب لعرض عناصر صفحة متنوعة مثل الصورة والنص على نفس المستوى (واحد بعد الآخر). يمكن أن يكون أحد الأساليب هو إنشاء مثيل للجدول وإضافة كلا العنصرين إلى كائنات الخلايا الفردية. ومع ذلك، يمكن أن يكون هناك نهج آخر وهو الفقرة المدمجة. من خلال تعيين خاصية IsInLineParagraph للصورة والنص كصحيح، ستظهر هذه الفقرات كمدمجة مع عناصر الصفحة الأخرى.

يوضح لك الكود التالي كيفية إضافة نص وصورة كفقرات مدمجة في ملف PDF.

```java
 public static void TextAndImageAsInLineParagraph() {
    // إنشاء مثيل Document
    Document doc = new Document();
    // إضافة صفحة إلى مجموعة الصفحات لمثيل Document
    Page page = doc.getPages().add();
    // إنشاء TextFragmnet
    TextFragment text = new TextFragment("Hello World.. ");
    // إضافة جزء النص إلى مجموعة الفقرات لكائن Page
    page.getParagraphs().add(text);
    // إنشاء مثيل للصورة
    Image image = new Image();
    // تعيين الصورة كفقرة مدمجة بحيث تظهر مباشرة بعد
    // كائن الفقرة السابق (TextFragment)
    image.setInLineParagraph (true);
    // تحديد مسار ملف الصورة
    image.setFile(_dataDir + "aspose-logo.jpg");
    // تعيين ارتفاع الصورة (اختياري)
    image.setFixHeight(30);
    // تعيين عرض الصورة (اختياري)
    image.setFixWidth(100);
    // إضافة الصورة إلى مجموعة الفقرات لكائن الصفحة
    page.getParagraphs().add(image);
    // إعادة تهيئة كائن TextFragment بمحتويات مختلفة
    text = new TextFragment(" Hello Again..");
    // تعيين TextFragment كفقرة مدمجة
    text.setInLineParagraph (true);
    // إضافة TextFragment المنشأ حديثًا إلى مجموعة الفقرات للصفحة
    page.getParagraphs().add(text);
    
    doc.save(_dataDir+"TextAndImageAsParagraph_out.pdf");
}
```


## تحديد تباعد الأحرف عند إضافة نص

يمكن إضافة النص داخل مجموعة الفقرات في ملفات PDF باستخدام كائن TextFragment أو باستخدام كائن TextParagraph وحتى يمكنك ختم النص داخل PDF باستخدام فئة TextStamp. عند إضافة النص، قد يكون لدينا حاجة لتحديد تباعد الأحرف لكائنات النص. لتحقيق هذا المتطلب، تم تقديم خاصية جديدة تسمى خاصية CharacterSpacing. يرجى إلقاء نظرة على الطرق التالية لتحقيق هذا المتطلب.

تظهر الطرق التالية الخطوات لتحديد تباعد الأحرف عند إضافة نص داخل مستند PDF.

## استخدام TextBuilder وTextFragment

```java
 public static void CharacterSpacing_TextFragment(){
    // إنشاء كائن المستند
    Document pdfDocument = new Document();
    // إضافة صفحة إلى مجموعة الصفحات للمستند
    Page page = pdfDocument.getPages().add();
    // إنشاء كائن TextBuilder
    TextBuilder builder = new TextBuilder(page);
    // إنشاء كائن نصي مع محتويات نموذجية
    TextFragment wideFragment = new TextFragment("نص بتباعد أحرف متزايد");
    wideFragment.getTextState().applyChangesFrom(new TextState("Arial", 12));
    // تحديد تباعد الأحرف لـ TextFragment
    wideFragment.getTextState().setCharacterSpacing(2.0f);
    // تحديد موضع TextFragment
    wideFragment.setPosition(new Position(100, 650));
    // إضافة TextFragment إلى كائن TextBuilder
    builder.appendText(wideFragment);        
    // حفظ مستند PDF الناتج.
    pdfDocument.save(_dataDir+ "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
}
```


## استخدام TextBuilder و TextParagraph

```java
public static void CharacterSpacing_TextParagraph() {
    // إنشاء مثيل Document
    Document pdfDocument = new Document();
    // إضافة صفحة إلى مجموعة الصفحات في Document
    Page page = pdfDocument.getPages().add();
    // إنشاء مثيل TextBuilder
    TextBuilder builder = new TextBuilder(page);
    // إنشاء مثيل TextParagraph
    TextParagraph paragraph = new TextParagraph();
    // إنشاء مثيل TextState لتحديد اسم الخط والحجم
    TextState state = new TextState("Arial", 12);
    // تحديد تباعد الأحرف
    state.setCharacterSpacing (1.5f);
    // إضافة نص إلى كائن TextParagraph
    paragraph.appendLine("هذا فقرة مع تباعد الأحرف", state);
    // تحديد الموقع لـ TextParagraph
    paragraph.setPosition (new Position(100, 550));
    // إضافة TextParagraph إلى مثيل TextBuilder
    builder.appendParagraph(paragraph);
    // حفظ مستند PDF الناتج.
    pdfDocument.save(_dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
}
```


## استخدام TextStamp

```java
public static void CharacterSpacing_TextStamp() {
    // إنشاء مثيل Document
    Document pdfDocument = new Document();
    // إضافة صفحة إلى مجموعة صفحات الوثيقة
    Page page = pdfDocument.getPages().add();
    // إنشاء مثيل TextStamp مع نص تجريبي
    TextStamp stamp = new TextStamp("هذه طباعة نص مع تباعد الحروف");
    // تحديد اسم الخط لكائن الطباعة
    stamp.getTextState().setFont(FontRepository.findFont("Arial"));
    // تحديد حجم الخط لـ TextStamp
    stamp.getTextState().setFontSize(12);
    // تحديد تباعد الحروف كـ 1f
    stamp.getTextState().setCharacterSpacing (1f);
    // تعيين XIndent للطباعة
    stamp.setXIndent(100);
    // تعيين YIndent للطباعة
    stamp.setYIndent(500);
    // إضافة طباعة نصية إلى مثيل الصفحة
    stamp.put(page);        
    // حفظ وثيقة PDF الناتجة.
    pdfDocument.save(_dataDir+"CharacterSpacingUsingTextStamp_out.pdf");        
}
```

## إنشاء وثيقة PDF متعددة الأعمدة

في المجلات والصحف، نرى غالبًا أن الأخبار تُعرض في أعمدة متعددة على الصفحات الفردية بدلاً من الكتب حيث تُطبع الفقرات النصية في الغالب على الصفحات الكاملة من اليسار إلى اليمين.
 تسمح العديد من تطبيقات معالجة المستندات مثل Microsoft Word وAdobe Acrobat Writer للمستخدمين بإنشاء أعمدة متعددة على صفحة واحدة ثم إضافة البيانات إليها.

تقدم Aspose.PDF for Java أيضًا ميزة إنشاء أعمدة متعددة داخل صفحات مستندات PDF. لإنشاء ملف PDF متعدد الأعمدة، يمكننا استخدام فئة Aspose.Pdf.FloatingBox لأنها توفر خاصية ColumnInfo.ColumnCount لتحديد عدد الأعمدة داخل FloatingBox ويمكننا أيضًا تحديد التباعد بين الأعمدة وعرض الأعمدة باستخدام خصائص ColumnInfo.ColumnSpacing وColumnInfo.ColumnWidths وفقًا لذلك. يرجى ملاحظة أن FloatingBox هو عنصر داخل نموذج كائن المستند ويمكن أن يكون له تموضع قديم مقارنة بالتموضع النسبي (أي النص، الرسم، الصورة، إلخ).
تباعد الأعمدة يعني المسافة بين الأعمدة والتباعد الافتراضي بين الأعمدة هو 1.25 سم. إذا لم يتم تحديد عرض العمود، فإن Aspose.PDF لـ Java يحسب العرض لكل عمود تلقائيًا وفقًا لحجم الصفحة وتباعد الأعمدة.

يوضح المثال أدناه كيفية إنشاء عمودين مع كائنات الرسوم البيانية (الخط) ويتم إضافتها إلى مجموعة الفقرات في FloatingBox، والتي تُضاف بعد ذلك إلى مجموعة الفقرات في كائن Page.

```java
public static void CreateMultiColumn() {
    Document doc = new Document();
    // تحديد معلومات الهامش الأيسر لملف PDF
    doc.getPageInfo().getMargin().setLeft(40);
    
    // تحديد معلومات الهامش الأيمن لملف PDF
    doc.getPageInfo().getMargin().setRight(40);
    
    Page page = doc.getPages().add();

    com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500, 2);
    
    // إضافة الخط إلى مجموعة الفقرات في كائن القسم
    page.getParagraphs().add(graph1);

    // تحديد الإحداثيات للخط
    float[] posArr = new float[] { 1, 2, 500, 2 };
    com.aspose.pdf.drawing.Line l1 = new com.aspose.pdf.drawing.Line(posArr);
    graph1.getShapes().add(l1);
    
    // إنشاء متغيرات نصية تحتوي على علامات HTML
    String s = "<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">"
                +"<strong> كيفية تجنب الاحتيال المالي</<strong> </span>";
    
    // إنشاء فقرات نصية تحتوي على نصوص HTML

    HtmlFragment heading_text = new HtmlFragment(s);
    page.getParagraphs().add(heading_text);

    FloatingBox box = new FloatingBox();
    
    // إضافة أربعة أعمدة في القسم
    box.getColumnInfo().setColumnCount(2);
    // تعيين التباعد بين الأعمدة
    box.getColumnInfo().setColumnSpacing("5");

    box.getColumnInfo().setColumnWidths("105 105");
    TextFragment text1 = new TextFragment("بواسطة شخص من جوجل (المدونة الرسمية لجوجل)");
    text1.getTextState().setFontSize (8);
    text1.getTextState().setLineSpacing (2);
    text1.getTextState().setFontSize (10);
    text1.getTextState().setFontStyle (FontStyles.Italic);

    box.getParagraphs().add(text1);
    
    // إنشاء كائن رسوم بيانية لرسم خط
    com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50, 10);
    // تحديد الإحداثيات للخط
    float[] posArr2 = new float[] { 1, 10, 100, 10 };
    com.aspose.pdf.drawing.Line l2 = new com.aspose.pdf.drawing.Line(posArr2);
    graph2.getShapes().add(l2);

    // إضافة الخط إلى مجموعة الفقرات في كائن القسم
    box.getParagraphs().add(graph2);

    TextFragment text2 = new TextFragment("سيد أوجو تور، صودالس إد، لوكتوس إت، بولفينار أوت، إيروس. سوسبينديسي فيل دولور. "
    +"سيد كووام. كورابيتور أوت ماسا فيتاي إيروس يوموسود أليكوام. بيلينتيسكوي سيت أميت إليت. فيستيبولوم إينتردوم بيلينتيسكوي أوجو."
    +"كراس مووليس أركو سيت أميت بوروس. دونيك أوجو. نام مووليس تورتر أ إليت. نولا فيفيرا نيسل فيل موريس. فيفاموس سابيين. ناسيتور "
    +"ريدكولوس موس. نام جستو لوريم، أليكوام لوكتوس، صودالس إت، سيمبر سيد، إينيم. نام جستو لوريم، أليكوام لوكتوس، صودالس إت، سيمبر سيد، إينيم. نان جستو لوريم، أليكوام لوكتوس، "
    +"صودالس إت، سيمبر سيد، إينيم. نآن بوسوير أنتي أوت نيكيو. موربي سوليستودين كونج فيليس. برايسنت توربيس ديام، إياكوليس سيد، فارترا نون، مولليس آك، موريس. "
    +"فاسيليس نيسي إيبسوم، بريتيوم فيتاي، تيمبور سيد، مولستيي إيو، دوو. دوييس لاكوس بوروس، تريستيكو أوت، إياكوليس كورسوس، تيندونت فيتاي، "
    +"ريزوس. سيد كومودو. *** سوسيس ناتووك بيناتيبوس إت ماجنس ديس بارتوريينت مونتيس، ناسيتور ريديكولوس موس. نام جستو لوريم، أليكوام "
    +"لوكتوس، صودالس إت، سيمبر سيد، إينيم. نام جستو لوريم، أليكوام لوكتوس، صودالس إت، سيمبر سيد، إينيم. نان جستو لوريم، أليكوام لوكتوس، "
    +"صودالس إت، سيمبر سيد، إينيم نآن بوسوير أنتي أوت نيكيو. موربي سوليستودين كونج فيليس. برايسنت توربيس ديام، إياكوليس سيد، "
    +"فارترا نون، مولليس آك، موريس. فاسيليس نيسي إيبسوم، بريتيوم فيتاي، تيمبور سيد، مولستيي إيو، دوو. دوييس لاكوس بوروس، تريستيكو أوت،"
    +"إياكوليس كورسوس، تيندونت فيتاي، ريزوس. سيد كومودو. *** سوسيس ناتووك بيناتيبوس إت ماجنس ديس بارتوريينت مونتيس، ناسيتور ريديكولوس "
    +"موس. سيد أورنا. . دوييس كونفاليس أولتريسيس نيسي. مايسيناس نون ليغولا. نونك نيب إست، تيندونت إن، بليسيرات سيت أميت، فيستيبولوم آ، نولا."
    +"برايسنت بورتتور توربيس إليفند أنتي. موربي صودالس. نآن بوسوير أنتي أوت نيكيو. موربي سوليستودين كونج فيليس. برايسنت توربيس ديام،"
    +"إياكوليس سيد، فارترا نون، مولليس آك، موريس. فاسيليس نيسي إيبسوم، بريتيوم فيتاي، تيمبور سيد، مولستيي إيو، دوو. دوييس لاكوس بوروس، تريستيكو"
    +"أوت، إياكوليس كورسوس، تيندونت فيتاي، ريزوس. سيد كومودو. *** سوسيس ناتووك بيناتيبوس إت ماجنس ديس بارتوريينت مونتيس، ناسيتور ريديكولوس موس."
    +"سيد أورنا. . دوييس كونفاليس أولتريسيس نيسي. مايسيناس نون ليغولا. نونك نيب إست، تيندونت إن، بليسيرات سيت أميت، فيستيبولوم آ، نولا. "
    +"برايسنت بورتتور توربيس إليفند أنتي. موربي صودالس.");
    box.getParagraphs().add(text2);

    page.getParagraphs().add(box);

    // حفظ ملف PDF
    doc.save(_dataDir + "CreateMultiColumnPdf_out.pdf");        
}
```


## العمل مع نقاط التوقف المخصصة لعلامة التبويب

نقطة توقف علامة التبويب هي نقطة توقف لعملية التبويب. في معالجة النصوص، تحتوي كل سطر على عدد من نقاط التوقف لعلامة التبويب الموضوعة على فترات منتظمة (مثلاً، كل نصف بوصة). ومع ذلك، يمكن تغييرها، حيث تسمح لك معظم معالجات النصوص بتعيين نقاط توقف علامة التبويب أينما تريد. عندما تضغط على مفتاح التبويب، يقفز المؤشر أو نقطة الإدراج إلى نقطة التوقف التالية لعلامة التبويب، والتي تكون غير مرئية بنفسها. على الرغم من أن نقاط التوقف لعلامة التبويب لا توجد في ملف النص، إلا أن معالج النصوص يتتبعها بحيث يمكنه التفاعل بشكل صحيح مع مفتاح التبويب.

يسمح [Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) للمطورين باستخدام نقاط توقف مخصصة لعلامة التبويب في مستندات PDF. يتم استخدام فئة Aspose.Pdf.Text.TabStop لتعيين نقاط توقف مخصصة لعلامة التبويب في فئة [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment).

كما يقدم [Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) بعض أنواع قادة التبويب المحددة مسبقاً كإعدادات تعداد باسم TabLeaderType التي تحتوي على قيم محددة مسبقاً ووصفها كما هو موضح أدناه:

|**نوع القائد الجدولي**|**الوصف**|
| :- | :- |
|None|بدون قائد جدولي|
|Solid|قائد جدولي متصل|
|Dash|قائد جدولي متقطع|
|Dot|قائد جدولي بنقاط|

إليك مثال حول كيفية تعيين توقفات الجدولة المخصصة.

```java
public static void CustomTabStops() {
    Document pdfdocument = new Document();
    Page page = pdfdocument.getPages().add();

    com.aspose.pdf.TabStops ts = new com.aspose.pdf.TabStops();
    com.aspose.pdf.TabStop ts1 = ts.add(100);
    ts1.setAlignmentType(TabAlignmentType.Right);
    ts1.setLeaderType (TabLeaderType.Solid);
    
    com.aspose.pdf.TabStop ts2 = ts.add(200);
    ts2.setAlignmentType(TabAlignmentType.Center);
    ts2.setLeaderType (TabLeaderType.Dash);

    com.aspose.pdf.TabStop ts3 = ts.add(300);
    ts3.setAlignmentType(TabAlignmentType.Left);
    ts3.setLeaderType (TabLeaderType.Dot);

    TextFragment header = new TextFragment("هذا مثال حول تكوين جدول باستخدام توقفات الجدولة", ts);
    TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data22 "));
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data23"));

    page.getParagraphs().add(header);
    page.getParagraphs().add(text0);
    page.getParagraphs().add(text1);
    page.getParagraphs().add(text2);
    
    pdfdocument.save(_dataDir + "CustomTabStops_out.pdf"); 
}
```


## كيفية إضافة نص شفاف في PDF

يحتوي ملف PDF على كائنات صورة ونص ورسم وملحقات وتعليقات توضيحية، وعند إنشاء TextFragment، يمكنك تعيين معلومات اللون الأمامي والخلفي وكذلك تنسيق النص. يدعم Aspose.PDF for Java ميزة إضافة نص مع قناة لون Alpha. يوضح مقتطف الشيفرة التالي كيفية إضافة نص بلون شفاف.

```java
  public static void AddTransparentText() {
    // إنشاء مثيل للمستند
    Document pdfdocument = new Document();
    // إنشاء صفحة لمجموعة الصفحات في ملف PDF
    Page page = pdfdocument.getPages().add();

    // إنشاء كائن الرسم
    Graph canvas = new Graph(100, 400);
    // إنشاء مثيل مستطيل بأبعاد معينة
    com.aspose.pdf.drawing.Rectangle rect = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
    // إنشاء كائن لون من قناة لون Alpha
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;
    Color alphaColor = Color.fromArgb(alpha, red, green, blue);
    rect.getGraphInfo().setFillColor(alphaColor);
    // إضافة المستطيل إلى مجموعة الأشكال في كائن الرسم
    canvas.getShapes().add(rect);
    // إضافة كائن الرسم إلى مجموعة الفقرات في كائن الصفحة
    page.getParagraphs().add(canvas);
    // تعيين القيمة لعدم تغيير موضع كائن الرسم
    canvas.setChangePosition(false);

    // إنشاء مثيل TextFragment بقيمة مثال
    TextFragment text = new TextFragment(
            "نص شفاف نص شفاف نص شفاف نص شفاف نص شفاف نص شفاف نص شفاف نص شفاف نص شفاف نص شفاف نص شفاف نص شفاف نص شفاف نص شفاف نص شفاف نص شفاف ");
    // إنشاء كائن لون من قناة Alpha
    alpha = 30;
    alphaColor = Color.fromArgb(alpha, red, green, blue);
    // تعيين معلومات اللون لمثيل النص
    text.getTextState().setForegroundColor (alphaColor);
    // إضافة النص إلى مجموعة الفقرات في مثيل الصفحة
    page.getParagraphs().add(text);
    
    pdfdocument.save(_dataDir + "AddTransparentText_out.pdf");
}
```


## تحديد تباعد الأسطر للخطوط

كل خط يحتوي على مربع مجرد، ارتفاعه هو المسافة المقصودة بين سطور النص في نفس حجم الخط. يسمى هذا المربع `مربع em` وهو شبكة التصميم التي تُعرّف عليها حدود الحروف. تحتوي العديد من أحرف الخط المدخل على نقاط توضع خارج حدود `مربع em` للخط، لذا من أجل عرض الخط بشكل صحيح، هناك حاجة لاستخدام إعداد خاص. يحتوي كائن TextFragment على مجموعة من خيارات تنسيق النص التي يمكن الوصول إليها عبر الطريقة [TextState.getFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#getFormattingOptions--).
تقوم هذه الطريقة بإرجاع فئة [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions).
 هذه الفئة تحتوي على تعداد [LineSpacingMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions.LineSpacingMode) الذي تم تصميمه لخطوط معينة مثل الخط المدخل "HPSimplified.ttf". كما أن الفئة [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) تحتوي على طريقة [setLineSpacing](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions#setLineSpacing-int-) من نوع LineSpacingMode. تحتاج فقط إلى ضبط LineSpacing إلى LineSpacingMode.FullSize. سيكون نموذج الكود للحصول على خط معروض بشكل صحيح كما يلي:

```java
public static void SpecifyLineSpacingForFonts() {
    String fontFile = _dataDir + "hp-simplified.ttf";
    // تحميل ملف PDF المدخل
    Document doc = new Document();
    // إنشاء TextFormattingOptions مع LineSpacingMode.FullSize
    TextFormattingOptions formattingOptions = new TextFormattingOptions();
    formattingOptions.setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);

    // إنشاء كائن بناء النص للصفحة الأولى من المستند
    // TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
    // إنشاء شظية نص مع سلسلة عينة
    TextFragment textFragment = new TextFragment("Hello world");

    // تحميل الخط TrueType إلى كائن التدفق
    FileInputStream fontStream;
    try {
        fontStream = new FileInputStream(fontFile);
    } catch (FileNotFoundException e) {
        e.printStackTrace();
        return;
    }

    // تعيين اسم الخط لسلسلة النص
    textFragment.getTextState().setFont(FontRepository.openFont(fontStream, FontTypes.TTF));
    // تحديد الموضع لشظية النص
    textFragment.setPosition(new Position(100, 600));
    // تعيين TextFormattingOptions للشظية الحالية إلى المحددة مسبقاً (التي تشير إلى
    // LineSpacingMode.FullSize)
    textFragment.getTextState().setFormattingOptions(formattingOptions);
    // إضافة النص إلى TextBuilder بحيث يمكن وضعه على ملف PDF
    // textBuilder.AppendText(textFragment);
    Page page = doc.getPages().add();
    page.getParagraphs().add(textFragment);

    // حفظ مستند PDF الناتج
    doc.save(_dataDir + "SpecifyLineSpacing_out.pdf");
}
```

## الحصول على عرض النص ديناميكيًا

في بعض الأحيان، يتطلب الأمر الحصول على عرض النص ديناميكيًا. يتضمن Aspose.PDF لـ Java طريقتين لقياس عرض السلسلة النصية. يمكنك استدعاء طريقة [MeasureString](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState#measureString--) من فئة com.aspose.pdf.Font أو com.aspose.pdf.TextState (أو كلاهما). يوضح مقتطف الشيفرة أدناه كيفية استخدام هذه الوظيفة.

```java
public static void GetTextWidthDynamicaly() {
    Font font = FontRepository.findFont("Arial");
    TextState ts = new TextState();
        ts.setFont(font);
        ts.setFontSize(14);
        if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001)
            System.out.println("قياس غير متوقع لسلسلة الخط!");

        if (Math.abs(ts.measureString("z") - 7.0) > 0.001)
        System.out.println("قياس غير متوقع لسلسلة الخط!");

        for (char c = 'A'; c <= 'z'; c++)
        {
            double fnMeasure = font.measureString(String.valueOf(c), 14);
            double tsMeasure = ts.measureString(String.valueOf(c));

            if (Math.abs(fnMeasure - tsMeasure) > 0.001)
                System.out.println("قياس سلسلة الخط والحالة لا يتطابق!");
        }
}
```