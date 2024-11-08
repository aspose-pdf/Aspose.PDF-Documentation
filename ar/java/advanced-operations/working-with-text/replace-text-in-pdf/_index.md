---
title: استبدال النص في PDF 
linktitle: استبدال النص في PDF
type: docs
weight: 40
url: /ar/java/replace-text-in-a-pdf-document/
description: تعرف على المزيد حول طرق مختلفة لاستبدال وإزالة النص من PDF. يتيح Aspose.PDF استبدال النص في منطقة معينة أو باستخدام تعبير منتظم.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استبدال النص في جميع صفحات مستند PDF

{{% alert color="primary" %}}

يمكنك محاولة العثور على النص واستبداله في المستند باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت من خلال هذا [الرابط](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

لاستبدال النص في جميع صفحات مستند PDF باستخدام [Aspose.PDF for Java](https://products.aspose.com/pdf/java):

1. أولاً استخدم [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) للعثور على العبارة المحددة التي سيتم استبدالها.

1. ثم، قم بالمرور عبر جميع [TextFragments](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber#getTextFragments--) لاستبدال النص وتغيير أي خصائص أخرى.
1. أخيرًا، احفظ ملف PDF الناتج باستخدام فئة Document [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) الطريقة.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleReplaceText {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void ReplaceTextOnAllPages() {
        Document pdfDocument = new Document(_dataDir+"sample.pdf");

        // إنشاء كائن TextAbsorber للعثور على جميع حالات عبارة البحث المدخلة
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Web");
        
        // قبول المستوعب للصفحة الأولى من المستند
        pdfDocument.getPages().accept(textFragmentAbsorber);
        
        // الحصول على مقاطع النص المستخرجة في مجموعة
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
        
        // التكرار من خلال المقاطع
        for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
            // تحديث النص والخصائص الأخرى
            textFragment.setText("World Wide Web");
            textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getBlue());
            textFragment.getTextState().setBackgroundColor(Color.getGray());
        }
        // حفظ ملف PDF المحدث
        pdfDocument.save(_dataDir+"Updated_Text.pdf");
    }
}
```


## استبدال النص في منطقة معينة من الصفحة

من أجل استبدال النص في منطقة معينة من الصفحة، أولاً، نحتاج إلى إنشاء كائن TextFragmentAbsorber، وتحديد منطقة الصفحة باستخدام [TextSearchOptions.setRectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions#setRectangle-com.aspose.pdf.Rectangle-) ومن ثم التكرار عبر جميع TextFragments لاستبدال النص. بمجرد الانتهاء من هذه العمليات، نحتاج فقط إلى حفظ ملف PDF الناتج باستخدام طريقة الحفظ لكائن Document.

يوضح لك مقطع الشيفرة التالي كيفية استبدال النص في جميع صفحات مستند PDF.

```java
 public static void ReplaceTextInParticularRegion(){
    // تحميل ملف PDF
    Document pdfDocument = new Document(_dataDir+"sample.pdf");

    // إنشاء كائن TextFragment Absorber
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("PDF");

    // البحث عن النص ضمن حدود الصفحة
    textFragmentAbsorber.getTextSearchOptions().setLimitToPageBounds(true);

    // تحديد منطقة الصفحة لخيارات البحث عن النص
    textFragmentAbsorber.getTextSearchOptions().setRectangle(new Rectangle(100, 700, 400, 770));

    // البحث عن النص من الصفحة الأولى لملف PDF
    pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);

    // التكرار عبر كل TextFragment
    for(TextFragment tf : textFragmentAbsorber.getTextFragments())
    {
        // استبدال النص بـ "---"
        tf.setText("---");
    }

    // حفظ ملف PDF المحدث
    pdfDocument.save(_dataDir+"Updated_Text.pdf");
}
```


## استبدال النص بناءً على تعبير منتظم

إذا كنت تريد استبدال بعض العبارات بناءً على تعبير منتظم، تحتاج أولاً إلى العثور على جميع العبارات التي تطابق ذلك التعبير المنتظم باستخدام TextFragmentAbsorber. سيتعين عليك تمرير التعبير المنتظم كمعامل إلى منشئ TextFragmentAbsorber. تحتاج أيضًا إلى إنشاء كائن TextSearchOptions الذي يحدد ما إذا كان يتم استخدام التعبير المنتظم أم لا. بمجرد الحصول على العبارات المطابقة في TextFragments، تحتاج إلى التكرار عبر جميعها وتحديثها حسب الحاجة. أخيرًا، تحتاج إلى حفظ ملف PDF المحدث باستخدام طريقة Save لكائن Document.

يوضح لك مقطع الشيفرة التالي كيفية استبدال النص بناءً على تعبير منتظم.

```java
public static void ReplaceTextWithRegularExpression() {
    // تحميل ملف PDF
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // إنشاء كائن TextAbsorber للعثور على جميع مثيلات عبارة البحث المدخلة
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); 
    // مثل 1999-2000

    // تعيين خيار البحث عن النص لتحديد استخدام التعبير المنتظم
    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

    // قبول الممتص للصفحة الأولى من المستند
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // الحصول على المقاطع النصية المستخرجة إلى مجموعة
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // التكرار عبر المقاطع
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // تحديث النص والخصائص الأخرى
        textFragment.setText("ABCD-EFGH");
        textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }

    // حفظ ملف PDF المحدث
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


## استبدال الخطوط في ملف PDF موجود

يدعم Aspose.PDF for Java القدرة على استبدال النص في مستند PDF. ومع ذلك، في بعض الأحيان قد تحتاج فقط إلى استبدال الخط المستخدم داخل مستند PDF. لذلك بدلاً من استبدال النص، يتم استبدال الخط المستخدم فقط. إحدى التحميلات الزائدة لباني TextFragmentAbsorber تقبل كائن TextEditOptions كحجة ويمكننا استخدام القيمة RemoveUnusedFonts من تعداد TextEditOptions.FontReplace لتحقيق متطلباتنا.

يوضح مقطع الشيفرة التالي كيفية استبدال الخط داخل مستند PDF.

```java
public static void ReplaceFonts() {
    // إنشاء كائن Document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // البحث عن شظايا النص وتعيين خيار التحرير كإزالة الخطوط غير المستخدمة
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(
            new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

    // قبول الممتص لكل صفحات المستند
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // التنقل عبر جميع شظايا النص
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection)
    {
        String fontName = textFragment.getTextState().getFont().getFontName();
        // إذا كان اسم الخط هو ArialMT، استبدل اسم الخط بـ Arial
        if (fontName.equals("ArialMT")) {
            textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        }
    }

    // حفظ ملف PDF المحدث
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


### استخدم الخط غير الإنجليزي (الياباني) عند استبدال النص

يُظهر مقتطف الشيفرة التالي كيفية استبدال النص بالحروف اليابانية. يرجى ملاحظة أنه لإضافة نص ياباني، تحتاج إلى استخدام خط يدعم الحروف اليابانية (على سبيل المثال MSGothic).

```java
public static void UseNonEnglishFontWhenReplacingText() {

    // إنشاء كائن المستند
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // دعونا نغير كل كلمة "page" إلى بعض النص الياباني مع خط محدد
    // TakaoMincho الذي قد يكون مثبتًا في نظام التشغيل
    // أيضًا، يمكن أن يكون خطًا آخر يدعم الرموز
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("page");

    // إنشاء مثيل لخيارات البحث عن النص
    TextSearchOptions searchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(searchOptions);

    // قبول مستخرج النص لجميع صفحات المستند
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // الحصول على أجزاء النص المستخرجة إلى مجموعة
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    
    // التكرار عبر الأجزاء
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // تحديث النص والخصائص الأخرى
        textFragment.setText("ファイル");
        textFragment.getTextState().setFont(FontRepository.findFont("MSGothic"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }
    // حفظ المستند المحدث
    pdfDocument.save(_dataDir + "Japanese_Text.pdf");
}
```


## يجب أن يعيد استبدال النص تلقائيًا ترتيب محتويات الصفحة

Aspose.PDF for Java يدعم ميزة البحث واستبدال النص داخل ملف PDF. ومع ذلك، مؤخرًا واجه بعض العملاء مشكلات أثناء استبدال النص عندما يتم استبدال TextFragment معين بمحتويات أصغر وتظهر بعض المسافات الإضافية في ملف PDF الناتج أو في حالة استبدال TextFragment بسلسلة أطول، فإن الكلمات تتداخل مع محتويات الصفحة الحالية. لذا كانت الحاجة إلى إدخال آلية بحيث بمجرد استبدال النص داخل مستند PDF، يجب إعادة ترتيب المحتويات.

من أجل تلبية السيناريوهات المذكورة أعلاه، تم تحسين Aspose.PDF for Java بحيث لا تظهر مثل هذه المشكلات عند استبدال النص داخل ملف PDF. يظهر مقتطف الشيفرة التالي كيفية استبدال النص داخل ملف PDF ويجب إعادة ترتيب محتويات الصفحة تلقائيًا.

```java
public static void RearrangeContent() {
    // تحميل ملف PDF المصدر
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // إنشاء كائن TextFragment Absorber مع تعبير عادي
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[PDF,Web]");

    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
    
    // يمكنك أيضًا تحديد خيار ReplaceAdjustment.WholeWordsHyphenation لتغليف النص في السطر التالي أو الحالي
    // إذا أصبح السطر الحالي طويلًا جدًا أو قصيرًا بعد الاستبدال:
    //textFragmentAbsorber.getTextReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.WholeWordsHyphenation);

    // قبول المستخرج لجميع صفحات المستند
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // الحصول على الأجزاء النصية المستخرجة في مجموعة
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // استبدال كل TextFragment
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // تعيين خط الجزء النصي الذي يتم استبداله
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        // تعيين حجم الخط
        textFragment.getTextState().setFontSize(10);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
        // استبدال النص بسلسلة أكبر من العنصر النائب
        textFragment.setText("This is a larger string for the testing of this feature");
    }
    // حفظ ملف PDF الناتج
    pdfDocument.save(_dataDir + "RearrangeContentsUsingTextReplacement_out.pdf");
}
```


## إنشاء رموز قابلة للاستبدال أثناء إنشاء PDF

الرموز القابلة للاستبدال هي رموز خاصة في سلسلة نصية يمكن استبدالها بمحتوى مطابق أثناء وقت التشغيل. الرموز القابلة للاستبدال المدعومة حاليًا بواسطة نموذج كائن الوثيقة الجديد في مساحة الأسماء Aspose.PDF هي `$P`، `$p`، `\n`، `\r`. يتم استخدام `$p` و`$P` للتعامل مع ترقيم الصفحات أثناء وقت التشغيل. يتم استبدال `$p` برقم الصفحة حيث توجد الفئة الحالية Paragraph. يتم استبدال `$P` بالعدد الإجمالي للصفحات في الوثيقة. عند إضافة [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) إلى مجموعة الفقرات في مستندات PDF، فإنه لا يدعم إدخال سطر داخل النص. ومع ذلك، لإضافة نص مع إدخال سطر، يرجى استخدام [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) مع [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph):

- استخدم "\r\n" أو Environment.NewLine في TextFragment بدلاً من "\n" الفردية؛
- أنشئ كائن TextParagraph.
 سيضيف نصًا مع تقسيم الأسطر؛
- إضافة TextFragment مع TextParagraph.AppendLine؛
- إضافة TextParagraph مع TextBuilder.AppendParagraph.

```java
public static void RenderingReplaceableSymbols() {
    // تحميل ملف PDF
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    Page page = pdfDocument.getPages().add();

    // تهيئة TextFragment جديد بنص يحتوي على علامات انتقال للسطر المطلوبة
    TextFragment textFragment = new TextFragment("اسم المتقدم: " + System.lineSeparator() + " جو سمو");

    // ضبط خصائص تجزئة النص إذا لزم الأمر
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());

    // إنشاء كائن TextParagraph
    TextParagraph par = new TextParagraph();

    // إضافة TextFragment جديد إلى الفقرة
    par.appendLine(textFragment);

    // ضبط موضع الفقرة
    par.setPosition (new Position(100, 600));

    // إنشاء كائن TextBuilder
    TextBuilder textBuilder = new TextBuilder(page);
    // إضافة TextParagraph باستخدام TextBuilder
    textBuilder.appendParagraph(par);

    _dataDir = _dataDir + "RenderingReplaceableSymbols_out.pdf";
    pdfDocument.save(_dataDir);
}
```

## الرموز القابلة للاستبدال في منطقة الرأس/التذييل

يمكن أيضًا وضع الرموز القابلة للاستبدال داخل قسم الرأس/التذييل في ملف PDF. يرجى الاطلاع على المقتطف البرمجي التالي للحصول على تفاصيل حول كيفية إضافة رمز قابل للاستبدال في قسم التذييل.

```java
public static void ReplaceableSymbolsInHeaderFooterArea() {
    Document doc = new Document();
    Page page = doc.getPages().add();

    MarginInfo marginInfo = new MarginInfo();
    marginInfo.setTop(90);
    marginInfo.setBottom(50);
    marginInfo.setLeft(50);
    marginInfo.setRight(50);

    // تعيين مثيل marginInfo إلى خاصية الهامش في sec1.PageInfo
    page.getPageInfo().setMargin(marginInfo);

    HeaderFooter hfFirst = new HeaderFooter();
    page.setHeader(hfFirst);
    hfFirst.getMargin().setLeft(50);
    hfFirst.getMargin().setRight(50);

    // إنشاء فقرة نصية ستخزن المحتوى لعرضه كرأس
    TextFragment t1 = new TextFragment("عنوان التقرير");
    t1.getTextState().setFont(FontRepository.findFont("Arial"));
    t1.getTextState().setFontSize(16);
    t1.getTextState().setForegroundColor(Color.getBlack());
    t1.getTextState().setFontStyle(FontStyles.Bold);
    t1.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t1.getTextState().setLineSpacing(5f);
    hfFirst.getParagraphs().add(t1);

    TextFragment t2 = new TextFragment("اسم التقرير");
    t2.getTextState().setFont(FontRepository.findFont("Arial"));
    t2.getTextState().setForegroundColor(Color.getBlack());
    t2.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t2.getTextState().setLineSpacing(5f);
    t2.getTextState().setFontSize(12);
    hfFirst.getParagraphs().add(t2);

    // إنشاء كائن HeaderFooter للقسم
    HeaderFooter hfFoot = new HeaderFooter();

    // تعيين كائن HeaderFooter إلى تذييل فردي وزوجي
    page.setFooter(hfFoot);
    hfFoot.getMargin().setLeft(50);
    hfFoot.getMargin().setRight(50);

    // إضافة فقرة نصية تحتوي على رقم الصفحة الحالي من إجمالي عدد الصفحات
    TextFragment t3 = new TextFragment("تم التوليد في تاريخ الاختبار");
    TextFragment t4 = new TextFragment("اسم التقرير ");
    TextFragment t5 = new TextFragment("الصفحة $p من $P");

    // إنشاء كائن جدول
    Table tab2 = new Table();

    // إضافة الجدول في مجموعة الفقرات للقسم المرغوب
    hfFoot.getParagraphs().add(tab2);

    // تعيين عرض الأعمدة للجدول
    tab2.setColumnWidths("165 172 165");

    // إنشاء صفوف في الجدول ثم خلايا في الصفوف
    Row row3 = tab2.getRows().add();

    row3.getCells().add();
    row3.getCells().add();
    row3.getCells().add();

    // تعيين المحاذاة العمودية للنص كمحاذاة في المنتصف
    row3.getCells().get_Item(0).setAlignment(HorizontalAlignment.Left);
    row3.getCells().get_Item(1).setAlignment(HorizontalAlignment.Center);
    row3.getCells().get_Item(2).setAlignment(HorizontalAlignment.Right);

    row3.getCells().get_Item(0).getParagraphs().add(t3);
    row3.getCells().get_Item(1).getParagraphs().add(t4);
    row3.getCells().get_Item(2).getParagraphs().add(t5);

    Table table = new Table();

    table.setColumnWidths("33% 33% 34%");
    table.setDefaultCellPadding(new MarginInfo());
    table.getDefaultCellPadding().setTop(10);
    table.getDefaultCellPadding().setBottom(10);

    // إضافة الجدول في مجموعة الفقرات للقسم المرغوب
    page.getParagraphs().add(table);

    // تعيين الحدود الافتراضية للخلايا باستخدام كائن BorderInfo
    table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));

    // تعيين حدود الجدول باستخدام كائن BorderInfo مخصص آخر
    table.setBorder(new BorderInfo(BorderSide.All, 1f));

    table.setRepeatingRowsCount(1);

    // إنشاء صفوف في الجدول ثم خلايا في الصفوف
    Row row1 = table.getRows().add();

    row1.getCells().add("col1");
    row1.getCells().add("col2");
    row1.getCells().add("col3");
    String CRLF = "\r\n";

    for (int i = 0; i <= 10; i++) {
        Row row = table.getRows().add();
        row.setRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            Cell c1;
            if (c == 2)
                c1 = row.getCells().add(
                        "Aspose.Total for Java هو تجميع لكل مكون جافا مقدم من قبل Aspose. يتم تجميعه على"
                                + CRLF
                                + "أساس يومي لضمان أنه يحتوي على أحدث الإصدارات من كل مكونات جافا الخاصة بنا. "
                                + CRLF
                                + "أساس يومي لضمان أنه يحتوي على أحدث الإصدارات من كل مكونات جافا الخاصة بنا. "
                                + CRLF
                                + "باستخدام Aspose.Total for Java يمكن للمطورين إنشاء مجموعة واسعة من التطبيقات.");
            else
                c1 = row.getCells().add("item1" + c);
            c1.setMargin(new MarginInfo());
            c1.getMargin().setLeft(30);
            c1.getMargin().setTop(10);
            c1.getMargin().setBottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```


## إزالة كل النص من مستند PDF

### إزالة كل النص باستخدام المشغلين

في بعض عمليات النص، تحتاج إلى إزالة كل النص من مستند PDF، ولأجل ذلك، تحتاج إلى تعيين النص الموجود كقيمة سلسلة فارغة عادةً. النقطة هي أن تغيير النص لعدد كبير من أجزاء النص يستدعي عددًا من عمليات التحقق وتعديل موضع النص. هذه العمليات ضرورية في سيناريوهات تحرير النصوص. الصعوبة تكمن في أنك لا تستطيع تحديد عدد أجزاء النص التي ستتم إزالتها في السيناريو حيث يتم معالجتها في حلقة.

لذلك، نوصي باستخدام نهج آخر في سيناريو إزالة كل النص من صفحات PDF. يرجى النظر في المقتطف البرمجي التالي الذي يعمل بسرعة كبيرة.

```java
public static void RemoveAllTextUsingOperators() {
    // فتح المستند
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // حلقة عبر جميع صفحات مستند PDF
    for (int i = 1; i <= pdfDocument.getPages().size(); i++) {
        Page page = pdfDocument.getPages().get_Item(i);
        OperatorSelector operatorSelector = new OperatorSelector(new com.aspose.pdf.operators.TextShowOperator());
        // تحديد كل النص في الصفحة
        page.getContents().accept(operatorSelector);
        // حذف كل النص
        page.getContents().delete(operatorSelector.getSelected());
    }
    // حفظ المستند
    pdfDocument.save(_dataDir + "RemoveAllText_out.pdf");
}
```