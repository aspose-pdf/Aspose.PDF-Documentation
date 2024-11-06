---
title: التلاعب بمستند PDF 
linktitle: التلاعب بمستند PDF
type: docs
weight: 30
url: ar/java/manipulate-pdf-document/
description: تحتوي هذه المقالة على معلومات حول كيفية التحقق من صحة مستند PDF لمعيار PDF A، وكيفية العمل مع TOC، وكيفية تعيين تاريخ انتهاء صلاحية PDF، وكيفية تحديد تقدم إنشاء ملف PDF.
lastmod: "2021-06-05"
---

## التحقق من صحة مستند PDF لمعيار PDF A (A 1A و A 1B)

للتحقق من صحة مستند PDF للتوافق مع PDF/A-1a أو PDF/A-1b، استخدم أسلوب [validate(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#validate-java.io.OutputStream-int-) في فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). يتيح لك هذا الأسلوب تحديد اسم الملف الذي سيتم حفظ النتيجة فيه ونوع التحقق المطلوب [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat) تعداد: PDF_A_1A أو PDF_A_1B.

تنسيق XML الناتج هو تنسيق مخصص لـ Aspose.
 يحتوي XML على مجموعة من العلامات باسم Problem؛ تحتوي كل علامة على تفاصيل مشكلة معينة. تمثل سمة ObjectID في علامة Problem مُعرّف الكائن المحدد الذي تتعلق به هذه المشكلة. تمثل سمة Clause قاعدة مقابلة في مواصفات PDF.

```java
  public static void ValidatePDFDocumentForPDF_A_Standard() {
    // افتح المستند
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // تحقق من PDF لـ PDF/A-1a
    pdfDocument.validate(_dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);

    // حفظ ملف PDF المحدث
    // document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```
## العمل مع جدول المحتويات

### إضافة جدول محتويات إلى PDF موجود

تسمح لك فئة ListSection في حزمة aspose.pdf بإنشاء جدول محتويات عند إنشاء مستند PDF من البداية. لإضافة العناوين، وهي عناصر جدول المحتويات، استخدم فئة [aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading).

لإضافة جدول محتويات إلى ملف PDF موجود، استخدم فئة [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) في حزمة com.aspose.pdf. حزمة com.aspose.pdf يمكنها إنشاء ملفات PDF جديدة والتعامل مع الملفات الموجودة. لإضافة جدول محتويات إلى ملف PDF موجود، استخدم حزمة com.aspose.pdf.

يوضح مقتطف الكود التالي كيفية إنشاء جدول محتويات داخل ملف PDF موجود.

```java
public static void AddTOCtoExistingPDF() {
    // تحميل ملف PDF موجود
    Document document = new Document(_dataDir + "sample.pdf");

    // الوصول إلى الصفحة الأولى من ملف PDF
    Page tocPage = document.getPages().insert(1);

    // إنشاء كائن لتمثيل معلومات جدول المحتويات
    com.aspose.pdf.TocInfo tocInfo = new com.aspose.pdf.TocInfo();
    com.aspose.pdf.TextFragment title = new com.aspose.pdf.TextFragment("جدول المحتويات");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(com.aspose.pdf.FontStyles.Bold);

    // تعيين العنوان لجدول المحتويات
    tocInfo.setTitle(title);
    tocPage.setTocInfo(tocInfo);

    // إنشاء كائنات سلسلة سيتم استخدامها كعناصر لجدول المحتويات
    String[] titles = new String[4];
    titles[0] = "الصفحة الأولى";
    titles[1] = "الصفحة الثانية";
    titles[2] = "الصفحة الثالثة";
    titles[3] = "الصفحة الرابعة";
    for (int i = 0; i < 4; i++) {
      // إنشاء كائن عنوان
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(1);

      com.aspose.pdf.TextSegment segment2 = new com.aspose.pdf.TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);

      // تحديد الصفحة المستهدفة لكائن العنوان
      heading2.setDestinationPage(document.getPages().get_Item(i + 2));

      // الصفحة المستهدفة
      heading2.setTop(document.getPages().get_Item(i + 2).getRect().getHeight());

      // إحداثيات الوجهة
      segment2.setText(titles[i]);

      // إضافة العنوان إلى الصفحة التي تحتوي على جدول المحتويات
      tocPage.getParagraphs().add(heading2);
    }
    // حفظ المستند المحدث
    document.save("TOC_Output_Java.pdf");
  }
```
### تعيين أنواع مختلفة من TabLeaderType لمستويات TOC مختلفة

يسمح Aspose.PDF أيضًا بتعيين أنواع مختلفة من TabLeaderType لمستويات TOC المختلفة. تحتاج إلى تعيين خاصية LineDash لـ FormatArray مع القيمة المناسبة لتعداد TabLeaderType كما يلي.

```java
  public static void SetDifferentTabLeaderTypeForTOCLevels() {

    String outFile = "TOC.pdf";

    Document document = new Document();
    Page tocPage = document.getPages().add();

    TocInfo tocInfo = new TocInfo();

    // تعيين LeaderType

    tocInfo.setLineDash(TabLeaderType.Solid);

    TextFragment title = new TextFragment("جدول المحتويات");
    title.getTextState().setFontSize(30);
    tocInfo.setTitle(title);

    // أضف قسم القائمة إلى مجموعة الأقسام في مستند Pdf

    tocPage.setTocInfo(tocInfo);

    // تحديد تنسيق قائمة المستويات الأربعة من خلال تعيين الهوامش اليسرى وإعدادات تنسيق النص لكل مستوى

    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setLeft(0);
    tocInfo.getFormatArray()[0].getMargin().setRight(30);
    tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
    tocInfo.getFormatArray()[1].getMargin().setLeft(10);
    tocInfo.getFormatArray()[1].getMargin().setRight(30);
    tocInfo.getFormatArray()[1].setLineDash(TabLeaderType.None);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
    tocInfo.getFormatArray()[2].getMargin().setLeft(20);
    tocInfo.getFormatArray()[2].getMargin().setRight(0);
    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
    tocInfo.getFormatArray()[3].getMargin().setLeft(30);
    tocInfo.getFormatArray()[3].getMargin().setRight(30);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    // إنشاء قسم في مستند Pdf
    Page page = document.getPages().add();

    // أضف أربعة عناوين في القسم
    for (int Level = 1; Level <= 4; Level++) {
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(Level);
      TextSegment segment2 = new TextSegment();

      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      heading2.setTocPage(tocPage);

      segment2.setText("العنوان التجريبي" + Level);
      heading2.getTextState().setFont(FontRepository.findFont("Arial UnicodeMS"));

      // أضف العنوان إلى جدول المحتويات.
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }

    // حفظ ملف PDF
    document.save(outFile);
  }
```

### إخفاء أرقام الصفحات في جدول المحتويات

في حال عدم الرغبة في عرض أرقام الصفحات مع العناوين في جدول المحتويات، يمكنك استخدام خاصية [IsShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/TocInfo) من [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) كاذبة. يرجى التحقق من مقتطف الشيفرة التالي لإخفاء أرقام الصفحات في جدول المحتويات:

```java
public static void HidePageNumbersInTOC() {
    String outFile = _dataDir + "HiddenPageNumbers_out.pdf";
    Document doc = new Document();
    Page tocPage = doc.getPages().add();
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Table Of Contents");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.setTitle(title);

    // إضافة قسم القائمة إلى مجموعة الأقسام في مستند Pdf
    tocPage.setTocInfo(tocInfo);

    // تحديد تنسيق قائمة المستويات الأربعة عن طريق ضبط الهامش الأيسر
    // وإعدادات تنسيق النص لكل مستوى

    tocInfo.setShowPageNumbers(false);
    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setRight(0);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);

    tocInfo.getFormatArray()[1].getMargin().setLeft(30);
    tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);

    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    Page page = doc.getPages().add();

    // إضافة أربعة عناوين في القسم
    for (int Level = 1; Level != 5; Level++) {
      Heading heading2 = new Heading(Level);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      segment2.setText("this is heading of level " + Level);
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }
    doc.save(_dataDir + outFile);
  }
```


### تخصيص أرقام الصفحات أثناء إضافة جدول المحتويات

من الشائع تخصيص ترقيم الصفحات في جدول المحتويات أثناء إضافة جدول المحتويات في مستند PDF. على سبيل المثال، قد نحتاج إلى إضافة بعض البادئات قبل رقم الصفحة مثل P1، P2، P3 وهكذا. في مثل هذه الحالة، يوفر Aspose.PDF لـ Java خاصية PageNumbersPrefix لفئة TocInfo التي يمكن استخدامها لتخصيص أرقام الصفحات كما هو موضح في نموذج الكود التالي.

```java
  public static void CustomizePageNumbersWhileAddingTOC() {

    String inFile = _dataDir + "sample.pdf";
    String outFile = _dataDir + "42824_out.pdf";

    // تحميل ملفات PDF موجودة
    Document doc = new Document(inFile);
    // الوصول إلى الصفحة الأولى من ملف PDF
    Page tocPage = doc.getPages().insert(1);
    // إنشاء كائن لتمثيل معلومات جدول المحتويات
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("جدول المحتويات");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);

    // تعيين العنوان لجدول المحتويات
    tocInfo.setTitle(title);
    tocInfo.setPageNumbersPrefix("P");
    tocPage.setTocInfo(tocInfo);

    for (int i = 1; i < doc.getPages().size(); i++) {
      // إنشاء كائن العنوان
      Heading heading2 = new Heading(1);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      // تحديد صفحة الوجهة لكائن العنوان
      heading2.setDestinationPage(doc.getPages().get_Item(i + 1));
      // صفحة الوجهة
      heading2.setTop(doc.getPages().get_Item(i + 1).getRect().getHeight());
      // إحداثيات الوجهة
      segment2.setText("الصفحة " + i);
      // إضافة العنوان إلى الصفحة التي تحتوي على جدول المحتويات
      tocPage.getParagraphs().add(heading2);
    }

    // حفظ المستند المحدث
    doc.save(outFile);
  }
```


## إضافة طبقات إلى ملف PDF

يمكن استخدام الطبقات في مستندات PDF بطرق متعددة. قد يكون لديك ملف متعدد اللغات تريد توزيعه وتريد أن يظهر النص في كل لغة على طبقات مختلفة، مع ظهور التصميم الخلفي على طبقة منفصلة. قد تقوم أيضًا بإنشاء مستندات تحتوي على رسوم متحركة تظهر على طبقة منفصلة. يمكن أن يكون أحد الأمثلة هو إضافة اتفاقية ترخيص إلى ملفك، ولا تريد أن يرى المستخدم المحتوى حتى يوافق على شروط الاتفاقية.

يدعم Aspose.PDF for Java إضافة طبقات إلى ملفات PDF.

لاستخدام الطبقات في ملفات PDF، استخدم أعضاء API التالية.

تمثل فئة [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) طبقة وتحتوي على الخصائص التالية:

- **Name** – اسم الطبقة.
- **Id** – معرف الطبقة.
- **Contents** – قائمة بمشغلي الطبقة.

بمجرد تعريف كائنات [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer)، قم بإضافتها إلى مجموعة الطبقات لكائن [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 يوضح الكود أدناه كيفية إضافة طبقات إلى مستند PDF.

```java
public static void AddLayersToPDFFile() {
    Document doc = new Document();
    Page page = doc.getPages().add();
    Layer layer = new Layer("oc1", "خط أحمر");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(1, 0, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 700));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 700));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.setLayers(new ArrayList<Layer>());
    page.getLayers().add(layer);
    layer = new Layer("oc2", "خط أخضر");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 1, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 750));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 750));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    layer = new Layer("oc3", "خط أزرق");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 0, 1));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 800));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 800));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    doc.save("output.pdf");
  
```
## تعيين انتهاء صلاحية ملف PDF

تحدد ميزة انتهاء صلاحية ملف PDF مدة صلاحية الملف. في تاريخ معين، إذا حاول شخص ما الوصول إليه، يظهر نافذة منبثقة توضح أن الملف قد انتهت صلاحيته وأنه يحتاج إلى ملف جديد.

تسمح لك Aspose.PDF بتعيين انتهاء الصلاحية عند إنشاء وتحرير ملفات PDF.

يوضح مقتطف الشيفرة أدناه كيفية تعيين تاريخ انتهاء الصلاحية لملف PDF. تحتاج إلى استخدام JavaScript حيث لا يمكن عرض الملفات المحفوظة بواسطة مكونات الجهات الخارجية (مثل OwnerGuard) على محطات العمل الأخرى بدون تلك الأداة المساعدة.

يمكن إنشاء ملف PDF باستخدام PDF OwnerGuard باستخدام ملف موجود مع تاريخ انتهاء الصلاحية. ولكن يمكن فتح الملف الجديد فقط على محطة عمل تحتوي على PDF OwnerGuard مثبت. ستعطي محطات العمل بدون PDF OwnerGuard خطأ ExpirationFeatureError. على سبيل المثال، يقوم PDF Reader بفتح الملف إذا كان OwnerGuard مثبتًا، ولكن Adobe Acrobat يعيد خطأ.

```java
  public static void SetPDFExpiration() {
    Document document = new Document(_dataDir+"sample.pdf");    
    JavascriptAction javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" + 
      "expiry = new Date(year, month);" + 
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('The file is expired. You need a new one.');"
      );
    document.setOpenAction(javaScript);
    document.save(_dataDir + "JavaScript-Added.pdf");
  }
```