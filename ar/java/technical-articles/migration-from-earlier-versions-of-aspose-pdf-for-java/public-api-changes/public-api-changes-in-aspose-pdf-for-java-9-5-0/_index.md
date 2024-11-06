---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.PDF لـ Java 9.5.0
type: docs
weight: 70
url: ar/java/public-api-changes-in-aspose-pdf-for-java-9-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تسرد هذه الصفحة تغييرات واجهة برمجة التطبيقات العامة التي تم تقديمها في [Aspose.PDF لـ Java 9.5.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry576058.aspx). وهي لا تشمل فقط الأساليب العامة الجديدة والمستبعدة، بل تشمل أيضًا وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.PDF لـ Java والتي قد تؤثر على الكود الحالي. أي سلوك تم تقديمه ويمكن اعتباره تراجعًا ويعدل السلوك الموجود يُعتبر مهمًا بشكل خاص ويتم توثيقه هنا.

{{% /alert %}}

**تمت إضافة خاصية CoordinateType إلى PdfViewer و PdfConverter**<p>
تسمح خاصية CoordinateType بتعيين منطقة الطباعة إلى MediaBox أو CropBox (القيمة الافتراضية)

**تمت إضافة طريقة SetFieldImage إلى فئة XFA:**

public void SetFieldImage(string fieldName, Stream image)

مثال:

يوضح الكود التالي كيفية تعيين صورة لحقل نموذج XFA:

```java

Document doc = new Document("doc.pdf");
InputStream fs = new FileInputStream("image.jpg");
doc.getForm().getXFA().setFieldImage("form1\[0\].ImageField1\[0\]", fs);
doc.save("37017-1.pdf");
```

تمت إضافة تعداد **ReplaceAdjustment** إلى فئة **TextReplaceOptions**

يوفر هذا التعداد القيم التالية:

- **None** - لا يوجد إجراء، قد يتغير طول السطر
- **AdjustSpaceWidth** - محاولة ضبط المسافات بين الكلمات للحفاظ على طول السطر

تمت إضافة خاصية **ReplaceAdjustmentAction** إلى فئة **TextReplaceOptions**

تمت إضافة منشئ جديد لفئة **TextReplaceOptions** يسمح بتعيين معلمة **ReplaceAdjustment**:

TextReplaceOptions(int adjustment, int scope)

تمت إضافة خاصية **TextReplaceOptions** إلى فئة **TextFragmentAbsorber**

تم تنفيذ فئة **Ellipse**:

المنشئ:

public Ellipse(float left, float bottom, float width, float height)

الخصائص:

- Left - قيمة من نوع float تشير إلى الموضع الأيسر للإهليلج.

- Bottom - قيمة من نوع float تشير إلى الموضع السفلي للإهليلج.
- العرض - قيمة عائمة تشير إلى عرض القطع الناقص.  
- الارتفاع - قيمة عائمة تشير إلى ارتفاع القطع الناقص.

مثال:  
يوضح مقتطف الشيفرة التالي كيفية إضافة القطع الناقص:

```java
String outFile = "Ellipse.pdf";
Document doc = new Document();
Page page = doc.getPages().add();
Graph canvas = new Graph(400, 100);
page.getParagraphs().add(canvas);
Ellipse ellipse1 = new Ellipse(50, 10, 100, 50);
canvas.getShapes().add(ellipse1);
doc.save(outFile);
```

تم تنفيذ فئة **Path**

المنشئون:

public Path()  
public Path(Shape[] shapes)

خاصية:

- الأشكال - مجموعة الأشكال

مثال:  
يوضح مقتطف الشيفرة التالي كيفية إضافة المسار:

```java
Document doc = new Document();
Page page = doc.getPages().add();
Graph graph = new Graph(100, 400);
page.getParagraphs().add(graph);

Path path = new Path();
path.getGraphInfo().setFillColor ( Color.getRed());
graph.getShapes().add(path);

Line line = new Line(new float[] { 200, 80, 200, 100 });
path.getShapes().add(line);
Arc arc = new Arc(200, 50, 50, 90, 270);
path.getShapes().add(arc);
float[] curPos = arc.getEndPosition();
line = new Line(new float[] { curPos[0], curPos[1], 200, 20 });
path.getShapes().add(line);
arc = new Arc(200, 50, 30, 270, 90);
path.getShapes().add(arc);
doc.Save(outFile);
```


**تمت إضافة فئة HtmlFragment إلى الحزمة com.aspose.pdf*

المنشئ:

- public HtmlFragment(string text)

المعلمة:

- النص - نص HTML
  الخاصية:
- النص - نص HTML

مثال:
يوضح مقتطف الشيفرة التالي كيفية إضافة جزء HTML:

```java
Document doc = new Document();
Page page = doc.getPages().add();
HtmlFragment titel = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
titel.setKeptWithNext (true);
titel.getMargin().setBottom (10);
titel.getMargin().setTop (200);
page.getParagraphs().add(titel);
doc.Save(outFile);
```

تمت إضافة طريقة **ContainsUsageRights()** إلى فئة **PdfFileSignature**

تمت إضافة طريقة **RemoveUsageRights()** إلى فئة **PdfFileSignature**

مثال:

يوضح الكود التالي كيفية إزالة خاصية حقوق الاستخدام من المستند:

```java
PdfFileSignature pdfSign = new PdfFileSignature();

try

{
    String inputFile = "c:\\36908.pdf";

    String outputFile = "c:\\36908_output.pdf";

    pdfSign.bindPdf(inputFile);

    if (pdfSign.containsUsageRights())

    {
        pdfSign.removeUsageRights();
    }

    pdfSign.getDocument().save(outputFile);
}

finally

{
    pdfSign.dispose();
}
```


**طريقة isContainSignature()** تم إعادة تسميتها إلى **ContainsSignature(...)**

- لم يتم إزالة اسم الطريقة السابقة ولكن تم تحديدها على أنها قديمة ليتم إزالتها في المستقبل.
    **طريقة isCoversWholeDocument()** تم إعادة تسميتها إلى **CoversWholeDocument(...)**
- لم يتم إزالة اسم الطريقة السابقة ولكن تم تحديدها على أنها قديمة ليتم إزالتها في المستقبل.

تمت إضافة فئة **Measure** إلى حزمة **com.aspose.pdf**

تصف الفئة نظام إحداثيات القياس. أعضاء فئة Measure:

المنشئ:

- public Measure(Annotation annotation)

خصائص get/set:

- ScaleRatio - سلسلة نصية تعبر عن نسبة مقياس الرسم.
- XFormat - مصفوفة تنسيق أرقام لقياس التغيير على طول المحور السيني، وإذا لم يكن المحور الصادي موجودًا، أيضًا على طول المحور الصادي.
- YFormat - مصفوفة تنسيق أرقام لقياس التغيير على طول المحور الصادي.
- DistanceFormat - مصفوفة تنسيق أرقام لقياس المسافة في أي اتجاه.
- AreaFormat - مصفوفة تنسيق أرقام لقياس المساحة.

- AngleFormat - مصفوفة تنسيق أرقام لقياس الزوايا.
- SlopeFormat - مصفوفة تنسيق الأرقام لقياس ميل الخط.
- Origin - النقطة التي تحدد أصل نظام إحداثيات القياس في إحداثيات المستخدم الافتراضية.
- XYFactor - عامل يُستخدم لتحويل أكبر الوحدات على طول المحور y إلى أكبر الوحدات على طول المحور x.

تمت إضافة فئة **NumberFormat** إلى فئة **Measure**

تمثل الفئة تنسيق الأرقام للقياس.

الباني:

- public NumberFormat(Measure measure)

خصائص get/set:

- UnitLabel - سلسلة نصية تحدد تسمية لعرض الوحدات.
- ConvresionFactor - عامل التحويل المستخدم لضرب قيمة بوحدات جزئية لعنصر مصفوفة تنسيق الأرقام السابق للحصول على قيمة بوحدات تنسيق الأرقام هذا.
- FractionDisplayment - الطريقة التي تُعرض بها القيم الكسرية.
- Precision - إذا كان FractionDisplayment هو ShowAsDecimal، فإن هذه القيمة هي دقة القيمة الكسرية؛ يجب أن تكون مضاعفًا لـ 10. القيمة الافتراضية هي 100.
- Denominator - إذا كان FractionDisplayment هو ShowAsFraction، فإن هذه القيمة هي مقام الكسر.
 القيمة الافتراضية هي 16.
- ForceDenominator - إذا كان FractionDisplayment هو ShowAsFraction، فإن هذه القيمة تحدد ما إذا كان الكسر يمكن تبسيطه أم لا. إذا كانت القيمة true، فقد لا يتم تبسيط الكسر.
- ThousandsSeparator - النص الذي يجب استخدامه بين أوامر الآلاف في عرض القيم العددية. يشير النص الفارغ إلى عدم إضافة أي نص. الافتراضي هو الفاصلة.
- FractionSeparator - النص الذي يجب استخدامه كمكان عشري في عرض القيم العددية. يشير النص الفارغ إلى أن الافتراضي سيتم استخدامه. الافتراضي هو نقطة.
- BeforeText - النص الذي يجب دمجه إلى يسار التسمية.
- AfterText - النص الذي يجب دمجه بعد التسمية.

تمت إضافة التعداد **FractionStyle** إلى فئة **NumberFormat**

قيم FractionStyle:

- ShowAsDecimal - عرض القيم الكسرية ككسر عشري.
- ShowAsFraction - عرض القيمة الكسرية ككسر.
- Round - تقريب القيم الكسرية إلى أقرب عدد صحيح كامل.
- Truncate - اقتطاع لتحقيق وحدات كاملة.

تمت إضافة فئة **NumberFormatList** إلى فئة **Measure**
The class represents يمثل قائمة من تنسيقات الأرقام.

Constructor:

- public NumberFormatList(Measure measure)

Properties:

- get_Item(int) و set_Item(int index, NumberFormat value) - يحصل أو يعيّن تنسيق الرقم في القائمة بواسطة فهرسه.
- getCount()- عدد العناصر في القائمة.

Methods:

- public void add(NumberFormat value)
- يضيف تنسيق الرقم إلى القائمة.
- public void insert(int index, NumberFormat value)
- يُدرج تنسيق الرقم في القائمة.
- public void removeAt(int index)
- يزيل تنسيق الرقم من القائمة.

تمت إضافة خاصية **Measure** إلى الفئات **LineAnnotation** و **PolyLineAnnotation**.

Examples:

يُظهر المثال التالي كيفية استخدام Measure مع LineAnnotation:

```java
Document doc = new Document("source.pdf");
Rectangle rect = new Rectangle(260, 630, 451, 662);
LineAnnotation line = new LineAnnotation(doc.getPages().get_Item(1), rect, new Point(266, 657), new Point(446, 656));
line.setColor(Color.getRed());
// تعيين معلمات خط التمديد.
line.setLeaderLine(-15);
line.setLeaderLineExtension(5);
// تعيين نهايات الخط
line.setStartingStyle(LineEnding.OpenArrow);
line.setEndingStyle(LineEnding.OpenArrow);

// إنشاء عنصر Measure
line.setMeasure(new Measure(line));<p>
line.getMeasure().setDistanceFormat(newMeasure.NumberFormatList(line.getMeasure()));
line.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(line.getMeasure()));
line.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
line.getMeasure().getDistanceFormat().get_Item(1).setFractionSeparator(".");
line.getMeasure().getDistanceFormat().get_Item(1).setConvresionFactor(1);

// نص خط القياس
line.setContents("155 mm");
// يجب تعيين هذا لإظهار النص.
line.setShowCaption(true);
line.setCaptionPosition(CaptionPosition.Top);
doc.getPages().get_Item(1).getAnnotations().add(line);
doc.save("output.pdf");
```


يُظهر المثال التالي كيفية استخدام Measure مع PolylineAnnotation:

```java
 Document doc = new Document("source.pdf");

Point[] vertices = new Point[]

{


new Point(100, 600),

new Point(500, 600),

new Point(500, 500),

new Point(400, 300),

new Point(100, 500),

new Point(100, 600)

};

Rectangle rect = new Rectangle(100, 500, 500, 600);
// المساحة أو خط المحيط
PolylineAnnotation area = new PolylineAnnotation(doc.getPages().get_Item(1), rect, vertices);
area.setColor(Color.getRed());
// يمكن تعيين نهايات الخط لخط المحيط.
area.setStartingStyle(LineEnding.OpenArrow);
area.setEndingStyle(LineEnding.OpenArrow);
area.setMeasure(new Measure(area));
area.getMeasure().setDistanceFormat(new Measure.NumberFormatList(area.getMeasure()));
area.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(area.getMeasure()));
area.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
doc.getPages().get_Item(1).getAnnotations().add(area);
doc.save("output.pdf");
```

يُظهر مقطع الكود التالي كيفية قراءة خصائص Measure:

```java
// قراءة خصائص القياس

Document doc = new Document("measure.pdf");

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getScaleRatio());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getUnitLabel());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getConvresionFactor());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getFractionSeparator());
```

**تغيير كبير** - تم إعادة تسمية خاصية PdfPageEditor.Pages إلى **ProcessPages**

يعرض مقتطف الشيفرة التالي كيفية استخدام الخاصية (تعيين معامل التكبير للصفحة #1 من الوثيقة):

```java
PdfPageEditor editor = new PdfPageEditor();
editor.bindPdf("input.pdf");
editor.setZoom(0.5f);
editor.setProcessPages(new int[] { 1 });
editor.save("output.pdf");
```


**تغيير جذري** - تم تغيير اسم الخاصية RichTextBoxField.RValue إلى **RichTextValue**

يوضح مقتطف الشيفرة التالي مثالاً حيث تم استخدام الحقل الذي تم تغيير اسمه:

```java
Document doc = new Document("input.pdf");

RichTextBoxField rt = new RichTextBoxField(doc.getPages().get_Item(1), new Rectangle(50, 600, 250, 650));
rt.setPartialName("rt");
doc.getForm().add(rt);
doc.save("34834.pdf");
Document doc1 = new Document("34834.pdf");
((RichTextBoxField)doc1.getForm().get("rt")).setRichTextValue("<p>هذا هو <b>الفقرة</b> الخاصة بي</p>");

doc1.save("output.pdf");
```

تمت إضافة خيار **InsertBlankColumnAtFirst** إلى **ExcelSaveOptions class**

يوضح مقتطف الشيفرة التالي كيفية منع ظهور العمود الفارغ الأول:

```java
Document doc = new Document(inFile);

ExcelSaveOptions options = new ExcelSaveOptions();

options.setInsertBlankColumnAtFirst(false);

doc.save(outFile, options);
```

تمت إضافة خاصية **PageInfo** إلى **SvgLoadOptions class**.

يوضح مقتطف الشيفرة التالي كيفية استخدام SvgLoadOptions وتعيين معلومات الهامش باستخدام خاصية PageInfo:

```java
SvgLoadOptions options = new SvgLoadOptions();

options.ConversionEngine = SvgLoadOptions.ConversionEngines.NewEngine;
options.getPageInfo().getMargin().setTop(0);
options.getPageInfo().getMargin().setLeft(0);
options.getPageInfo().getMargin().setBottom(0);
options.getPageInfo().getMargin().setRight(0);
String inFile = "35730.svg";
String outFile = "35730.pdf";
Document pdfDocument = new Document(inFile, options);
pdfDocument.save(outFile);
```

تمت إضافة تعداد **ConversionEngines** إلى فئة **SvgLoadOptions**.

القيم التالية محددة:

- **LegacyEngine** - محرك قديم لمعالجة Svg
- **NewEngine** - محرك معالجة Svg جديد

تمت إضافة خاصية **ConversionEngine** إلى فئة **SvgLoadOptions**

لا يزال LegacyEngine هو القيمة الافتراضية لأن NewEngine في مراحل الاختبار B.
يوضح مقطع الشفرة التالي مثالاً على كيفية استخدام المحرك الجديد:

```java
SvgLoadOptions options = new SvgLoadOptions();

options.ConversionEngine = SvgLoadOptions.ConversionEngines.NewEngine;
String inFile = "36516_2_income.svg";
String outFile = "36516_2_income.pdf";
Document pdfDocument = new Document(inFile, options);
pdfDocument.save(outFile);
```


**خاصية ColumnAdjustment** تمت إضافتها إلى فئة **Table**

تمت إضافة تعداد ColumnAdjustment إلى حزمة com.aspose.pdf

تمت إضافة القيم التالية:

- **Customized** - يقوم المستخدم بتعيين عرض العمود يدويًا.
- **AutoFitToContent** - يقوم بضبط العرض تلقائيًا ليتناسب مع المحتوى

**خاصية ColumnAdjustment** تمت إضافتها إلى فئة **Table**

القيمة الافتراضية هي Customized.

يظهر مقتطف الكود التالي مثالاً على استخدام خاصية ColumnAdjustment:

```java
Table hTable = new Table();
hTable.getMargin().setTop(4);
hTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5F, Color.getBlack()));
hTable.setDefaultCellPadding(new MarginInfo(1, 1, 1, 1));
hTable.setAlignment(HorizontalAlignment.Left);
hTable.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
```

**خاصية MinimizeTheNumberOfWorksheets** تم تقديمها في كائن **ExcelSaveOptions**.

يظهر مقتطف الكود التالي كيفية تقليل العدد المحتمل من أوراق العمل:

```java
Document doc = new Document("Original.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
//Set this property to true
options.setMinimizeTheNumberOfWorksheets(true);
doc.save("output.xls", options);
```


**القيمة الافتراضية** أُضيفت إلى تعداد **PageLayout**.

المقطع البرمجي التالي يضبط PageLayout إلى القيمة الافتراضية:

```java
Document doc1 = new Document("input.pdf");
doc1.setPageLayout (PageLayout.Default);
doc1.save("output.pdf");
```

تم تنفيذ دعم **النهايات المستديرة** لـ **InkAnnotation**

أُضيف تعداد **CapStyle** إلى حزمة **com.aspose.pdf**
القيم التالية موجودة

- **Rectangular** - القيمة المحددة الافتراضية
- **Rounded** - زوايا مستديرة
- خاصية **CapStyle** أُضيفت إلى فئة **InkAnnotation**

المقطع البرمجي التالي يُظهر كيفية ضبط زوايا InkAnnotation لتكون مستديرة:

```java
Document doc = new Document("PdfWithText.pdf");
Page pdfPage = doc.getPages().get_Item(1);
java.awt.Rectangle drect = new java.awt.Rectangle();
drect.height = (int)pdfPage.getRect().getHeight();
drect.width = (int)pdfPage.getRect().getWidth();
drect.x = 0;
drect.y = 0;
com.aspose.pdf.Rectangle arect = com.aspose.pdf.Rectangle.fromRect(drect);
java.util.ArrayList inkList = new java.util.ArrayList();
com.aspose.pdf.Point[] arrpt = new com.aspose.pdf.Point[3];
inkList.add(arrpt);
arrpt[0] = new Point(100, 800);
arrpt[1] = new Point(200, 800);
arrpt[2] = new Point(200, 700);
InkAnnotation ia = new InkAnnotation(pdfPage, arect, inkList);
ia.setTitle("XXX");
ia.setColor(Color.getLightBlue());
ia.setCapStyle(CapStyle.Rounded);
Border border = new Border(ia);
border.setWidth(25);
ia.setOpacity(0.5);
pdfPage.getAnnotations().add(ia);
doc.save("37071.pdf");
```


**PDFNEWJAVA-33498** - توفير الدعم لإضافة صورة من BufferedImage إلى مستند PDF

يوضح مقطع الشيفرة التالي كيفية إضافة صورة من BufferedImage:

```java
BufferedImage originalImage = ImageIO.read(new File("c:\\image\\anyImage.jpg"));
Document pdfDocument1 = new Document();
Page page2 = pdfDocument1.getPages().add();
page2.getResources().getImages().add(originalImage)
```

**PDFNEWJAVA-34088** - تحويل PDF إلى HTML: لتحديد مجلد الصور

يوضح مقطع الشيفرة التالي كيفية تحديد مجلد الصور:

```java
Document pdfDocument = new Document(testdata + "PDFNEWJAVA_34088.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.SpecialFolderForAllImages = testdata + "SpecialFolderForAllImages";
pdfDocument.save(testout + "PDFNEWJAVA_34088.html", saveOptions);
```

**PDFNEWJAVA-33203** - ضبط DPI/PPI للصور في PDF

يوضح مقطع الشيفرة التالي كيفية تغيير دقة الصورة في ملف pdf:

```java
String myDir = "D:\\Temp\\";
File fileIn = new File(myDir+"image.jpg");
FileInputStream in = new FileInputStream(fileIn)

File fileOut = new File(myDir+"image.pdf");
FileOutputStream out = new FileOutputStream(fileOut);
// إنشاء pdf للاختبار
Document doc = new Document();
Page page = doc.getPages().add();
com.aspose.pdf.Image image1 = new com.aspose.pdf.Image();
image1.setImageStream(in);
image1.setFixHeight(page.getMediaBox().getHeight()/4);
image1.setFixWidth(page.getMediaBox().getWidth()/2);
NewParagraphPlacementInfo placementInfo = new NewParagraphPlacementInfo();
placementInfo.setStartNewPage(true);
page.getParagraphs().add(image1, placementInfo);
page.getPageInfo().getMargin().setLeft(5);
page.getPageInfo().getMargin().setRight(0);
page.getPageInfo().getMargin().setTop(0);
page.getPageInfo().getMargin().setBottom(0);
doc.save(out);
```


```java
// تغيير دقة الصورة الداخلية
doc = new Document(myDir+"image.pdf");
XImageCollection images = doc.getPages().get_Item(1).getResources().getImages();
ByteArrayOutputStream baos = new ByteArrayOutputStream();
images.get_Item(1).save(baos, 10, 10);// تحديد الدقة الأفقية والعمودية
images.get_Item(1).replace(new ByteArrayInputStream(baos.toByteArray()));
doc.save(myDir+"imageWithNewResolution.pdf");
```

**الملخص:**

**الفئات المضافة:**

- com.aspose.pdf.drawing.Ellipse
- com.aspose.pdf.drawing.Path
com.aspose.pdf.generator.legacyxmlmodel.BookmarkIncludeType
- com.aspose.pdf.generator.legacyxmlmodel.BorderSide
- com.aspose.pdf.generator.legacyxmlmodel.ColumnInfo
- com.aspose.pdf.generator.legacyxmlmodel.HeaderFooterType
- com.aspose.pdf.generator.legacyxmlmodel.HtmlInfo
- com.aspose.pdf.generator.legacyxmlmodel.ImportOptions
- com.aspose.pdf.generator.legacyxmlmodel.MediaType
- com.aspose.pdf.generator.legacyxmlmodel.PathArea
- com.aspose.pdf.generator.legacyxmlmodel.TableFormatInfo

- com.aspose.pdf.AutoDetectedFormatLoadOptions

 - com.aspose.pdf.CapStyle
- com.aspose.pdf.ColumnAdjustment
- com.aspose.pdf.ComHelper
- com.aspose.pdf.EpubLoadOptions
- com.aspose.pdf.EpubSaveOptions
- com.aspose.pdf.FileFontSource
- com.aspose.pdf.FontAbsorber
- com.aspose.pdf.HtmlFragment
- com.aspose.pdf.Measure
- com.aspose.pdf.MemoryFontSource

## التغييرات في الفئات:

**com.aspose.pdf.facades.Form**

التغييرات:

- public java.util.Map getButtonOptionValues(String fieldName) -> public java.util.Hashtable<String,String> getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfConverter** تمت الإضافة:

- public int getCoordinateType()
- public void setCoordinateType(int value) مهمل:
- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileInfo** التغييرات:

- public java.util.Map getHeader() -> public java.util.Map<String, String> getHeader()
- public void setHeader(java.util.Map value) -> public void setHeader(java.util.Map<String,String> value


**com.aspose.pdf.facades.PdfFileSignature**
Depricated:

- public boolean isContainSignature() - عام المنهج isContainSignature()
- public boolean isCoversWholeDocument(String signName) - عام المنهج isCoversWholeDocument(String signName)
  Added: - تمت الإضافة:
- public boolean containsSignature() - عام المنهج containsSignature()
- public boolean containsUsageRights() - عام المنهج containsUsageRights()
- public void removeUsageRights() - عام المنهج removeUsageRights()

**com.aspose.pdf.facades.PdfPageEditor**  
Changes:  
التغييرات:

- public int[] getPages_Rename_Namesake() -> public int[] getProcessPages() - public int[] getPages_Rename_Namesake() -> عام المنهج int[] getProcessPages()
- public void setPages(int[] value) -> public void setProcessPages(int[] value) - عام المنهج void setPages(int[] value) -> عام المنهج void setProcessPages(int[] value)
- public java.util.Map getPageRotations() -> public java.util.Map<Integer, Integer> getPageRotations() - عام المنهج java.util.Map getPageRotations() -> عام المنهج java.util.Map<Integer, Integer> getPageRotations()
- public void setPageRotations(java.util.Map value) -> public void setPageRotations(java.util.Map<Integer, Integer> value) - عام المنهج void setPageRotations(java.util.Map value) -> عام المنهج void setPageRotations(java.util.Map<Integer, Integer> value)

**com.aspose.pdf.facades.PdfViewer**  
Depricated:  
تم إهماله:

- public boolean getShowHiddenAreas() - عام المنهج getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value) - عام المنهج void setShowHiddenAreas(boolean value)
  Added: - تمت الإضافة:
- public int getCoordinateType() - عام المنهج getCoordinateType()
- public void setCoordinateType(int value) - عام المنهج void setCoordinateType(int value)

**com.aspose.pdf.facades.PdfXmpMetadata**  
Changes:  
التغييرات:

- public IDictionary getExtensionFields() -> public java.util.Hashtable<String, XmpPdfAExtensionSchema> getExtensionFields() - عام المنهج IDictionary getExtensionFields() -> عام المنهج java.util.Hashtable<String, XmpPdfAExtensionSchema> getExtensionFields()

**com.aspose.pdf.generator.legacyxmlmodel.Attachment**  
تمت الإضافة:

- public InputStream AttachedStream

**com.aspose.pdf.generator.legacyxmlmodel.BorderInfo**  
تمت الإضافة:

- public void setBorderStyle(int borderSide, int style)

**com.aspose.pdf.generator.legacyxmlmodel.BoxVerticalAlignmentType**

- تمت إزالة حالة Deprecated من الفئة

**com.aspose.pdf.generator.legacyxmlmodel.Cell**  
تمت الإضافة:

- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo value)
- public String getText()

**com.aspose.pdf.generator.legacyxmlmodel.HeaderFooter**  
تمت الإضافة:

- public Object completeClone()
- public Object completeCloneAll()

**com.aspose.pdf.generator.legacyxmlmodel.Heading**  
تمت إزالة حالة Deprecated من:

- public int getBulletAlignment()
- public void setBulletAlignment(int value)

**com.aspose.pdf.generator.legacyxmlmodel.Image**  
تمت الإضافة:

- public Image(HeaderFooter hf)

**com.aspose.pdf.generator.legacyxmlmodel.JavaScripts**  
تمت الإضافة:

- public void remove(Cell jsToRemove)

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**
تمت الإضافة:

- public boolean DigitSubstitution
- public boolean IsAutoFontAdjusted
- public boolean IsBuffered
- public InputStream TruetypeFontMapStream
- public boolean IsImageNotFoundErrorIgnored
- public boolean Linearized;
- public int getPageCount()
- public void save(OutputStream output)
- public byte[] getBuffer()
- public void save(String pdfFile)
- public void bindXML(String xmlFile, String xslFileIfAny)
- public void bindXML(InputStream xmlStream, InputStream xslStream)
- public void setUnicode()
- public Object getObjectByID(String ID)
- public HtmlInfo HtmlInfo

أُضيفت إلى المهملات:

- public int getBookMarkLevel()
- public void setBookMarkLevel(int value)
- public int getDirectModeItemType()
- public void setDirectModeItemType(int value)
- public int getDirectModeItemsCount()
- public void setDirectModeItemsCount(int value)

**com.aspose.pdf.generator.legacyxmlmodel.LinkAction**
تمت الإضافة:

- public String SoundFileName

**com.aspose.pdf.generator.legacyxmlmodel.Paragraphs**
تمت الإضافة:

- public void add(Paragraph paragraph)
 - void addHeading(فقرة paragraph)
- public int indexOf(فقرة paragraph)
- public void copyTo(فقرة[] paraArray, int index)
- public void insert(فقرة paragraphToInsertAfter, فقرة جديدة newParagraph)

**com.aspose.pdf.generator.legacyxmlmodel.Row**  
تم التغيير:

- DefaultCellTextInfo إلى حقل getter و setter
  تمت الإضافة:
- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo value)
- public Object deepClone()

**com.aspose.pdf.generator.legacyxmlmodel.Section**  
تمت الإضافة:

- public ColumnInfo ColumnInfo
- public int getPageCount()
- public void setPageCount(int value)
- public String BreakParaText
- public Object deepClone()
- public Object completeClone()
- public HeaderFooter insertHeader(int type)
- public HeaderFooter insertFooter(int type)
- public Object getObjectByID(String ID)

**com.aspose.pdf.generator.legacyxmlmodel.Sections**  
تمت الإضافة:

- public Sections()
- public Section add()
- public void insert(int index, Section section)

- public void insert(قسم sectionToInsertAfter, قسم جديد newSection)
- public void remove(Section sectionToRemove)  
- public void copyTo(Section[] secArray, int index)  
- public int indexOf(Section section)  
- public void set_Item(int index, Section value)  
- public Section get_Item(String sectionID)  
- public void set_Item(String sectionID, Section value)  

**com.aspose.pdf.generator.legacyxmlmodel.Security**  
تمت الإضافة:

- public boolean isDefaultAllAllowed()  
- public void setDefaultAllAllowed(boolean value)  

**com.aspose.pdf.generator.legacyxmlmodel.Shapes**  
تمت الإضافة:

- public void add(Shape shape)  
- public void remove(Shape shapeToRemove)  
- public void copyTo(Shape[] shapeArray, int index)  
- public int indexOf(Shape shape)  

**com.aspose.pdf.generator.legacyxmlmodel.Table**  
تم التغيير:

- FixedWidth إلى حقل getter وsetter  
- DefaultCellTextInfo إلى حقل getter وsetter  
  تمت الإضافة:
- public float getFixedWidth()  
- public void setFixedWidth(float value)  
- public TextInfo getDefaultCellTextInfo()  
- public void setDefaultCellTextInfo(TextInfo value)  

- public Cell getCell(int row, int column, boolean isTableChanged)  
- public void formatColumnsWithFormatInfo(TableFormatInfo info, int firstColumn, int maxColumns)
- public void formatTableWithFormatInfo(TableFormatInfo info, int firstColumn, int firstRow, int maxRows, int maxColumns)
- public void formatRowsWithFormatInfo(TableFormatInfo info, int firstRow, int maxRows)
- public void setColumnWidth(int columnNumber, float width)
- public String getColumnWidths()
- public void setColumnWidths(String value)

**com.aspose.pdf.generator.legacyxmlmodel.TabStops**  
تمت الإضافة:

- public int getCapacity()
- public void setCapacity(int value)

**com.aspose.pdf.generator.legacyxmlmodel.TextInfo**  
تم التغيير:

- تم تغيير القائمة التالية من الحقول إلى حقل getter و setter منفصل:

```java

 FontSize, FontName, TruetypeFontFileName, IsUnicode, FontAfmFile, FontPfmFile, FontOutlineFile, FontEncodingFile,
 IsTrueTypeFontBold, IsTrueTypeFontItalic,{color} {color:#222222}FontEncoding, IsFontEmbedded, IsUnderline,{color}
 {color:#222222}IsOverline,{color} {color:#222222}CharSpace, WordSpace, LineSpacing, OverlineOffset, UnderlineOffset, RenderingMode,
 Color, BackgroundColor, IsRightToLeft, StrokeWidth, StrokeColor, IsBaseline, Alignment.

```


تمت الإضافة:

- public float getFontSize() // الحصول على حجم الخط
- public void setFontSize(float value) // تعيين حجم الخط
- public String getFontName() // الحصول على اسم الخط
- public void setFontName(String value) // تعيين اسم الخط
- public String getTruetypeFontFileName() // الحصول على اسم ملف خط TrueType
- public void setTruetypeFontFileName(String value) // تعيين اسم ملف خط TrueType
- public boolean isUnicode() // التحقق مما إذا كان Unicode
- public void setUnicode(boolean value) // تعيين Unicode
- public String getFontAfmFile() // الحصول على ملف الخط AFM
- public void setFontAfmFile(String value) // تعيين ملف الخط AFM
- public String getFontPfmFile() // الحصول على ملف الخط PFM
- public void setFontPfmFile(String value) // تعيين ملف الخط PFM
- public String getFontOutlineFile() // الحصول على ملف الخط العريض
- public void setFontOutlineFile(String value) // تعيين ملف الخط العريض
- public String getFontEncodingFile() // الحصول على ملف ترميز الخط
- public void setFontEncodingFile(String value) // تعيين ملف ترميز الخط
- public boolean isTrueTypeFontBold() // التحقق مما إذا كان خط TrueType غامق
- public void setTrueTypeFontBold(boolean value) // تعيين خط TrueType غامق
- public boolean isTrueTypeFontItalic() // التحقق مما إذا كان خط TrueType مائل
- public void setTrueTypeFontItalic(boolean value) // تعيين خط TrueType مائل
- public String getFontEncoding() // الحصول على ترميز الخط
- public void setFontEncoding(String value) // تعيين ترميز الخط
- public boolean isFontEmbedded() // التحقق مما إذا كان الخط مضمنًا
- public void setFontEmbedded(boolean value) // تعيين الخط كمضمن
- public boolean isUnderline() // التحقق مما إذا كان تحت الخط

- public void setUnderline(boolean value) // تعيين تحت الخط
- public boolean isOverline() // هل النص يحتوي على خط علوي
- public void setOverline(boolean value) // تعيين وجود خط علوي
- public float getCharSpace() // الحصول على المسافة بين الأحرف
- public void setCharSpace(float value) // تعيين المسافة بين الأحرف
- public float getWordSpace() // الحصول على المسافة بين الكلمات
- public void setWordSpace(float value) // تعيين المسافة بين الكلمات
- public float getLineSpacing() // الحصول على المسافة بين الأسطر
- public void setLineSpacing(float value) // تعيين المسافة بين الأسطر
- public float getOverlineOffset() // الحصول على إزاحة الخط العلوي
- public void setOverlineOffset(float value) // تعيين إزاحة الخط العلوي
- public float getUnderlineOffset() // الحصول على إزاحة الخط السفلي
- public void setUnderlineOffset(float value) // تعيين إزاحة الخط السفلي
- public int getRenderingMode() // الحصول على وضعية العرض
- public void setRenderingMode(int value) // تعيين وضعية العرض
- public Color getColor() // الحصول على اللون
- public void setColor(Color value) // تعيين اللون
- public Color getBackgroundColor() // الحصول على لون الخلفية
- public void setBackgroundColor(Color value) // تعيين لون الخلفية
- public boolean isRightToLeft() // هل النص من اليمين إلى اليسار
- public void setRightToLeft(boolean value) // تعيين اتجاه النص من اليمين إلى اليسار
- public float getStrokeWidth() // الحصول على عرض الخط
- public void setStrokeWidth(float value) // تعيين عرض الخط
- public Color getStrokeColor() // الحصول على لون الخط
- public void setStrokeColor(Color value) // تعيين لون الخط
- public boolean isBaseline() // هل النص على خط الأساس
- public void setBaseline(boolean value) // تعيين وجود النص على خط الأساس
- public int getAlignment() // الحصول على محاذاة النص

- public void setAlignment(int value) // تعيين محاذاة النص

**com.aspose.pdf.BaseOperatorCollection** التغييرات:

- implements ICollection -> implements ICollection< Operator >

**com.aspose.pdf.Border** التغييرات:

- public int getVCornerRaduis() -> public int getVCornerRadius() - public void setVCornerRaduis(int value) -> public void setVCornerRadius(int value) تمت إضافة مهمل: - public int getVCornerRaduis() - public void setVCornerRaduis(int value)

**com.aspose.pdf.DataUtils** التغييرات:

- داخلي

**com.aspose.pdf.ExcelSaveOptions** تمت الإضافة:

- public boolean getMinimizeTheNumberOfWorksheets() - public void setMinimizeTheNumberOfWorksheets(boolean value) - public boolean getInsertBlankColumnAtFirst() - public void setInsertBlankColumnAtFirst(boolean value) - public boolean getUniformWorksheets() - public void setUniformWorksheets(boolean value)

**com.aspose.pdf.Font** تمت الإضافة:

- public void save(OutputStream stream)

**com.aspose.pdf.Form** تمت الإضافة:

- public FieldsEnumerator(IDocument document, List< Object > fields)

**com.aspose.pdf.HtmlSaveOptions:** تمت الإضافة:


- public FontSourceCollection getFontSources()

**com.aspose.pdf.InkAnnotation**  
أضيف:

- public int getCapStyle()  
- public void setCapStyle(int value)  

**com.aspose.pdf.LineAnnotation**  
أضيف:

- public Measure getMeasure()  
- public void setMeasure(Measure value)  

**com.aspose.pdf.LoadFormat:**  
التغييرات:

- public static final int InfoPath - تمت إزالته  
- public static final int AutoDetect - أضيف  

**com.aspose.pdf.Metadata**  
التغييرات:

- public IDictionary getExtensionFields() -> public java.util.Hashtable< String, XmpPdfAExtensionSchema > getExtensionFields()  

**com.aspose.pdf.PageLayout**  
أضيف:

- public static final int Default  

**com.aspose.pdf.PolylineAnnotation**  
أضيف:

- public Measure getMeasure()  
- public void setMeasure(Measure value)  

**com.aspose.pdf.PopupAnnotation**  
أضيف:

- public MarkupAnnotation getParent()  
- public void setParent(MarkupAnnotation value)  

**com.aspose.pdf.RichTextBoxField**  
التغييرات:

- public String getRValue() -> public String getRichTextValue()  

- public void setRValue(String value) -> public void setRichTextValue(String value)  

**com.aspose.pdf.SaveOptions.BorderPartStyle**  
تمت الإضافة:

- public java.awt.Color اللون

**com.aspose.pdf.SvgLoadOptions**  
تمت الإضافة:

- public static final class ConversionEngines
- public int ConversionEngine
- public PageInfo getPageInfo()
- public void setPageInfo(PageInfo القيمة)

**com.aspose.pdf.Table**  
تمت الإضافة:

- public int getColumnAdjustment()
- public void setColumnAdjustment(int القيمة)

**com.aspose.pdf.TextFragmentAbsorber**  
تمت الإضافة:

- public TextReplaceOptions getTextReplaceOptions()
- public void setTextReplaceOptions(TextReplaceOptions القيمة)

**com.aspose.pdf.TextReplaceOptions**  
تمت الإضافة:

- public static final class ReplaceAdjustment
- public int getReplaceAdjustmentAction()
- public void setReplaceAdjustmentAction(int القيمة)
- public TextReplaceOptions(int التعديل, int النطاق)

**com.aspose.pdf.XFA**  
تمت الإضافة:

- public void setFieldImage(String اسم_الحقل, InputStream الصورة)