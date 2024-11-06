---
title: تنسيق النص داخل PDF 
linktitle: تنسيق النص داخل PDF
type: docs
weight: 30
url: ar/java/text-formatting-inside-pdf/
description: توضح هذه الصفحة كيفية تنسيق النص داخل ملف PDF الخاص بك. هناك إضافة مسافة بادئة للسطر، إضافة حدود للنص، إضافة نص مسطر، إضافة إطار حول النص المضاف، محاذاة النص لمحتويات الصندوق العائم إلخ.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## كيفية إضافة مسافة بادئة للسطر إلى PDF

يقدم Aspose.PDF for Java خاصية SubsequentLinesIndent في فئة [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions). والتي يمكن استخدامها لتحديد المسافة البادئة للسطر في سيناريوهات إنشاء PDF مع TextFragment ومجموعة الفقرات.

يرجى استخدام الشيفرة البرمجية التالية لاستخدام الخاصية:

```java
public static void AddLineIndentToPDF() {
        // إنشاء كائن مستند جديد
        Document document = new Document();
        Page page = document.getPages().add();

        TextFragment text = new TextFragment(
                "A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

        // تهيئة TextFormattingOptions لمقطع النص وتحديد
        // قيمة SubsequentLinesIndent
        TextFormattingOptions textOptions = new TextFormattingOptions();
        textOptions.setSubsequentLinesIndent(20);
        text.getTextState().setFormattingOptions(textOptions);

        page.getParagraphs().add(text);

        text = new TextFragment("Line2");
        page.getParagraphs().add(text);

        text = new TextFragment("Line3");
        page.getParagraphs().add(text);

        text = new TextFragment("Line4");
        page.getParagraphs().add(text);

        text = new TextFragment("Line5");
        page.getParagraphs().add(text);

        document.save(_dataDir + "SubsequentIndent_out.pdf");
    }
```


## كيفية إضافة حدود للنص

يوضح مقتطف الشيفرة التالي كيفية إضافة حدود للنص باستخدام TextBuilder وتعيين طريقة DrawTextRectangleBorder في TextState:

```java
public static void AddTextBorder() {
    // إنشاء كائن مستند جديد
    Document pdfDocument = new Document();
    // الحصول على صفحة معينة
    Page pdfPage = pdfDocument.getPages().add();
    // إنشاء جزء نصي
    TextFragment textFragment = new TextFragment("النص الرئيسي");
    textFragment.setPosition(new Position(100, 600));
    // تعيين خصائص النص
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());
    // استخدام setStrokingColor لرسم الحدود (stroking) حول مستطيل النص
    textFragment.getTextState().setStrokingColor (Color.getDarkRed());
    // استخدام طريقة setDrawTextRectangleBorder لتعيين القيمة إلى true
    textFragment.getTextState().setDrawTextRectangleBorder(true);
    TextBuilder tb = new TextBuilder(pdfPage);
    tb.appendText(textFragment);
    // حفظ المستند
    pdfDocument.save(_dataDir + "PDFWithTextBorder_out.pdf");
}
```


## كيفية إضافة نص مسطر

يظهر لك مقتطف الشيفرة التالي كيفية إضافة نص مسطر أثناء إنشاء ملف PDF جديد.

```java
public static void AddUnderlineText(){
    // إنشاء كائن الوثيقة
    Document pdfDocument = new Document();
    // إضافة صفحة جديدة إلى وثيقة PDF
    Page page = pdfDocument.getPages().add();
    // إنشاء TextBuilder للصفحة الأولى
    TextBuilder tb = new TextBuilder(page);
    // TextFragment مع نص نموذجي
    TextFragment fragment = new TextFragment("نص مع زخرفة تسطير");
    // ضبط الخط لـ TextFragment
    fragment.getTextState().setFont (FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize (10);
    // ضبط تنسيق النص كتسطير
    fragment.getTextState().setUnderline(true);
    // تحديد الموضع الذي يحتاج فيه TextFragment إلى أن يوضع
    fragment.setPosition (new Position(10, 800));
    // إلحاق TextFragment إلى ملف PDF
    tb.appendText(fragment);

    // حفظ مستند PDF الناتج.
    pdfDocument.save(_dataDir + "AddUnderlineText_out.pdf");
}
```


## كيفية إضافة حد حول النص المضاف

لديك التحكم في المظهر والشعور بالنص الذي تضيفه. المثال أدناه يوضح كيفية إضافة حد حول قطعة من النص الذي قمت بإضافته عن طريق رسم مستطيل حوله. اكتشف المزيد عن فئة [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor).

```java
public static void AddBorderAroundAddedText() {
    PdfContentEditor editor = new PdfContentEditor();
    editor.bindPdf(_dataDir + "input.pdf");
    LineInfo lineInfo = new LineInfo();
    lineInfo.setLineWidth(2);
    lineInfo.setVerticeCoordinate (new float[] { 0, 0, 100, 100, 50, 100 });
    lineInfo.setVisibility(true);
    editor.createPolygon(lineInfo, 1, new java.awt.Rectangle(0, 0, 0, 0), "");

    // احفظ مستند PDF الناتج.
    editor.save(_dataDir + "AddingBorderAroundAddedText_out.pdf");
}
```

## كيفية إضافة تغذية سطر جديد

TextFragment لا يدعم تغذية السطر داخل النص.
 ومع ذلك، لإضافة نص مع تغذية سطر، يرجى استخدام TextFragment مع TextParagraph:

- استخدم "\r\n" أو Environment.NewLine في TextFragment بدلاً من "\n" منفردة;
- قم بإنشاء كائن TextParagraph. سيضيف النص مع تقسيم الأسطر;
- أضف TextFragment مع TextParagraph.AppendLine;
- أضف TextParagraph مع TextBuilder.AppendParagraph.
يرجى استخدام مقتطف الشيفرة أدناه.

```java
public static void AddNewLineFeed() {        
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    // تهيئة TextFragment جديد يحتوي على نص يحتوي على علامات الانتقال إلى السطر المطلوبة
    TextFragment textFragment = new TextFragment("اسم المتقدم: " + System.lineSeparator() + " جو سمو");

    // تعيين خصائص نص المقطع إذا لزم الأمر
    textFragment.getTextState().setFontSize (12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());

    // إنشاء كائن TextParagraph
    TextParagraph par = new TextParagraph();

    // إضافة TextFragment جديد إلى الفقرة
    par.appendLine(textFragment);

    // تعيين موضع الفقرة
    par.setPosition (new Position(100, 600));

    // إنشاء كائن TextBuilder
    TextBuilder textBuilder = new TextBuilder(page);
    // إضافة TextParagraph باستخدام TextBuilder
    textBuilder.appendParagraph(par);

    // حفظ وثيقة PDF الناتجة.
    pdfDocument.save(_dataDir + "AddNewLineFeed_out.pdf");
}
```

## كيفية إضافة نص مشطوب

توفر فئة TextState القدرات اللازمة لتعيين تنسيق للـ TextFragments التي يتم وضعها داخل مستند PDF. يمكنك استخدام هذه الفئة لتعيين تنسيق النص كـ Bold، Italic، Underline وابتداءً من هذا الإصدار، قدمت API القدرات لوضع علامة تنسيق النص كـ Strikeout. يرجى محاولة استخدام مقتطف الشفرة التالي لإضافة TextFragment مع تنسيق Strikeout.

يرجى استخدام مقتطف الشفرة الكامل:

```java
public static void AddStrikeOutText(){
    // افتح المستند
    Document pdfDocument = new Document();
    // احصل على صفحة معينة
    Page pdfPage = (Page)pdfDocument.getPages().add();

    // إنشاء جزء نص
    TextFragment textFragment = new TextFragment("main text");
    textFragment.setPosition (new Position(100, 600));

    // تعيين خصائص النص
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());
    // استخدم طريقة setStrikeOut لتمكين النص المشطوب
    textFragment.getTextState().setStrikeOut(true);
    // ضع علامة على النص كـ Bold
    textFragment.getTextState().setFontStyle(FontStyles.Bold);

    // إنشاء كائن TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // أضف جزء النص إلى صفحة PDF
    textBuilder.appendText(textFragment);

    // احفظ مستند PDF الناتج.
    pdfDocument.save(_dataDir + "AddStrikeOutText_out.pdf");        
}
```


## تطبيق تظليل متدرج على النص

تم تحسين تنسيق النص بشكل أكبر في واجهة برمجة التطبيقات لسيناريوهات تحرير النصوص ويمكنك الآن إضافة نص بلون نمط الفضاء داخل مستند PDF. تم تحسين فئة `com.aspose.pdf.Color` بشكل أكبر من خلال تقديم طرق جديدة `setPatternColorSpace`، والتي يمكن استخدامها لتحديد ألوان التظليل للنص. تضيف هذه الطريقة الجديدة تظليلًا متدرجًا مختلفًا للنص مثل تظليل محوري، تظليل شعاعي (النوع 3) كما هو موضح في مقطع الشيفرة التالي:

```java
public static void ApplyGradientShading() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("always print correctly");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));

    // إنشاء لون جديد بنمط الفضاء اللوني
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```


من أجل تطبيق تدرج شعاعي، يمكنك استخدام طريقة `setPatternColorSpace` مساوية لـ `GradientRadialShading(startingColor, endingColor)` في الكود أعلاه.

```java
public static void ApplyGradientShadingRadial() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("always print correctly");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));

    // إنشاء لون جديد مع فضاء الألوان النمطي
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```

## كيفية محاذاة النص بمحتوى عائم

يدعم Aspose.PDF ضبط محاذاة النص للمحتويات داخل عنصر مربع عائم.
 خصائص المحاذاة لكائن Aspose.Pdf.FloatingBox يمكن استخدامها لتحقيق ذلك كما هو موضح في مثال الكود التالي.

```java
public static void AlignTextToFloatContent() {
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    FloatingBox floatBox = new FloatingBox(100, 100);
    floatBox.setVerticalAlignment(VerticalAlignment.Bottom); // محاذاة عمودية إلى الأسفل
    floatBox.setHorizontalAlignment (HorizontalAlignment.Right); // محاذاة أفقية إلى اليمين
    floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
    floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue())); // تعيين الحدود باللون الأزرق
    
    page.getParagraphs().add(floatBox);

    FloatingBox floatBox1 = new FloatingBox(100, 100);
    floatBox1.setVerticalAlignment(VerticalAlignment.Center); // محاذاة عمودية إلى المركز
    floatBox1.setHorizontalAlignment (HorizontalAlignment.Right); // محاذاة أفقية إلى اليمين
    floatBox1.getParagraphs().add(new TextFragment("FloatingBox_center"));
    floatBox1.setBorder (new BorderInfo(BorderSide.All, Color.getBlue())); // تعيين الحدود باللون الأزرق
    page.getParagraphs().add(floatBox1);

    FloatingBox floatBox2 = new FloatingBox(100, 100);
    floatBox2.setVerticalAlignment(VerticalAlignment.Top); // محاذاة عمودية إلى الأعلى
    floatBox2.setHorizontalAlignment (HorizontalAlignment.Right); // محاذاة أفقية إلى اليمين
    floatBox2.getParagraphs().add(new TextFragment("FloatingBox_top"));
    floatBox2.setBorder (new BorderInfo(BorderSide.All, Color.getBlue())); // تعيين الحدود باللون الأزرق
    page.getParagraphs().add(floatBox2);

    pdfDocument.save(_dataDir + "FloatingBox_alignment_review_out.pdf"); // حفظ المستند بصيغة PDF          
}
```