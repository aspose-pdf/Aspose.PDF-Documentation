---
title: Aspose.PDF for Java 9.5.0 中的公共 API 更改
type: docs
weight: 70
url: zh/java/public-api-changes-in-aspose-pdf-for-java-9-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

此页面列出了 [Aspose.PDF for Java 9.5.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry576058.aspx) 中引入的公共 API 更改。它不仅包括新的和已废弃的公共方法，还包括对 Aspose.PDF for Java 背后行为的任何更改的描述，这些更改可能会影响现有代码。任何被视为回归并修改现有行为的行为尤其重要，并在此记录。

{{% /alert %}}

**CoordinateType 属性已添加到 PdfViewer 和 PdfConverter**<p>
CoordinateType 属性允许将可打印区域设置为 MediaBox 或 CropBox（默认值）

**SetFieldImage 方法已添加到 XFA 类：**

public void SetFieldImage(string fieldName, Stream image)

示例：

以下代码片段显示如何为 XFA 表单字段设置图像：


```java

Document doc = new Document("doc.pdf");
InputStream fs = new FileInputStream("image.jpg");
doc.getForm().getXFA().setFieldImage("form1\[0\].ImageField1\[0\]", fs);
doc.save("37017-1.pdf");
```

**ReplaceAdjustment** 枚举已添加到 **TextReplaceOptions** 类中

此枚举提供以下值：

- **None** - 无操作，行的长度可能会改变
- **AdjustSpaceWidth** - 尝试调整单词之间的空格以保持行长度

**ReplaceAdjustmentAction** 属性已添加到 **TextReplaceOptions** 类中

**TextReplaceOptions** 类新增了一个构造函数，允许设置 **ReplaceAdjustment** 参数：

TextReplaceOptions(int adjustment, int scope)

**TextReplaceOptions** 属性已添加到 **TextFragmentAbsorber** 类中

**Ellipse** 类已实现：

构造函数：

public Ellipse(float left, float bottom, float width, float height)

属性：

- Left - 指示椭圆左侧位置的浮点值。

- Bottom - 指示椭圆底部位置的浮点值。

- Width - 表示椭圆宽度的浮点值。
- Height - 表示椭圆高度的浮点值。

示例：
以下代码片段显示了如何添加椭圆：

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

**Path** 类已实现

构造函数：

public Path()
public Path(Shape[] shapes)

属性：

- Shapes - 形状集合

示例：
以下代码片段显示了如何添加路径：

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


**HtmlFragment** 类已被添加到包 com.aspose.pdf*

构造函数：

- public HtmlFragment(string text)

参数：

- Text - HTML 文本  
  属性：
- Text - HTML 文本

示例：  
以下代码片段展示了如何添加 HTML 片段：

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

**ContainsUsageRights()** 方法已被添加到 **PdfFileSignature** 类中

**RemoveUsageRights()** 方法已被添加到 **PdfFileSignature** 类中

示例：

以下代码展示了如何从文档中移除使用权限功能：

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


**isContainSignature()** 方法被重命名为 **ContainsSignature(...)**

- 之前的方法名称没有被移除，但被标记为过时，将在未来移除。
    **isCoversWholeDocument()** 方法被重命名为 **CoversWholeDocument(...)**
- 之前的方法名称没有被移除，但被标记为过时，将在未来移除。

**Measure** 类被添加到 **com.aspose.pdf** 包中

该类描述了测量坐标系。Measure 类的成员：

构造函数：

- public Measure(Annotation annotation)

获取/设置属性：

- ScaleRatio - 表示图纸比例的文本字符串。
- XFormat - 用于测量沿 x 轴变化的数字格式数组，如果 Y 不存在，则也用于沿 y 轴变化。
- YFormat - 用于测量沿 y 轴变化的数字格式数组。
- DistanceFormat - 用于测量任意方向距离的数字格式数组。
- AreaFormat - 用于测量面积的数字格式数组。

- AngleFormat - 用于测量角度的数字格式数组。
- SlopeFormat - 用于测量直线斜率的数字格式数组。
- Origin - 指定测量坐标系原点的点，使用默认用户空间坐标。
- XYFactor - 用于将沿 y 轴的最大单位转换为沿 x 轴的最大单位的因子。

**NumberFormat** 类被添加到 **Measure** 类中

该类表示测量的数字格式。

构造函数：

- public NumberFormat(Measure measure)

获取/设置 属性：

- UnitLabel - 指定用于显示单位的标签的文本字符串。
- ConvresionFactor - 用于将上一数字格式数组元素的部分单位中的值乘以转换因子，以获得此数字格式单位中的值。
- FractionDisplayment - 分数值的显示方式。
- Precision - 如果 FractionDisplayment 是 ShowAsDecimal，此值为分数值的精度；它应为 10 的倍数。默认值为 100。
- Denominator - 如果 FractionDisplayment 是 ShowAsFraction，此值为分数的分母。
 默认值是16。

- ForceDenominator - 如果 FractionDisplayment 是 ShowAsFraction，此值决定分数是否可以约简。如果值为 true，则分数可能不会被约简。
- ThousandsSeparator - 用于在显示数值时的千位分隔符。空字符串表示不添加任何文本。默认是逗号。
- FractionSeparator - 用作显示数值时的小数位置的文本。空字符串表示将使用默认值。默认是句号字符。
- BeforeText - 将与标签左侧连接的文本。
- AfterText - 将与标签右侧连接的文本。

枚举 **FractionStyle** 被添加到 **NumberFormat** 类中

FractionStyle 值：

- ShowAsDecimal - 以小数形式显示分数值。
- ShowAsFraction - 以分数形式显示分数值。
- Round - 将分数值四舍五入到最接近的整数。
- Truncate - 截断以获得完整单位。

**NumberFormatList** 类被添加到 **Measure** 类中
该类表示数字格式的列表。

构造函数：

- public NumberFormatList(Measure measure)

属性：

- get_Item(int) 和 set_Item(int index, NumberFormat value) - 通过索引获取或设置列表中的数字格式。
- getCount()- 列表中的项目计数。

方法：

- public void add(NumberFormat value)
- 向列表中添加数字格式。
- public void insert(int index, NumberFormat value)
- 插入数字格式到列表中。
- public void removeAt(int index)
- 从列表中移除数字格式。

**Measure** 属性已添加到 **LineAnnotation** 和 **PolyLineAnnotation** 类。

示例：

以下示例演示如何在 LineAnnotation 中使用 Measure：

```java
Document doc = new Document("source.pdf");
Rectangle rect = new Rectangle(260, 630, 451, 662);
LineAnnotation line = new LineAnnotation(doc.getPages().get_Item(1), rect, new Point(266, 657), new Point(446, 656));
line.setColor(Color.getRed());
//设置延长线参数。
line.setLeaderLine(-15);
line.setLeaderLineExtension(5);
//设置线端样式
line.setStartingStyle(LineEnding.OpenArrow);
line.setEndingStyle(LineEnding.OpenArrow);

//创建 Measure 元素
line.setMeasure(new Measure(line));<p>
line.getMeasure().setDistanceFormat(new Measure.NumberFormatList(line.getMeasure()));
line.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(line.getMeasure()));
line.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
line.getMeasure().getDistanceFormat().get_Item(1).setFractionSeparator(".");
line.getMeasure().getDistanceFormat().get_Item(1).setConvresionFactor(1);

//测量线的文本
line.setContents("155 mm");
//必须设置以显示文本。
line.setShowCaption(true);
line.setCaptionPosition(CaptionPosition.Top);
doc.getPages().get_Item(1).getAnnotations().add(line);
doc.save("output.pdf");
```


以下示例演示了如何使用 Measure 与 PolylineAnnotation：

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
// 区域或周长线
PolylineAnnotation area = new PolylineAnnotation(doc.getPages().get_Item(1), rect, vertices);
area.setColor(Color.getRed());
// 可以为周长线设置线端样式。
area.setStartingStyle(LineEnding.OpenArrow);
area.setEndingStyle(LineEnding.OpenArrow);
area.setMeasure(new Measure(area));
area.getMeasure().setDistanceFormat(new Measure.NumberFormatList(area.getMeasure()));
area.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(area.getMeasure()));
area.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
doc.getPages().get_Item(1).getAnnotations().add(area);
doc.save("output.pdf");
```

以下代码片段演示了如何读取 Measure 属性：

```java
//读取测量属性

Document doc = new Document("measure.pdf");

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getScaleRatio());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getUnitLabel());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getConvresionFactor());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getFractionSeparator());
```

**重大变更** - PdfPageEditor.Pages 属性重命名为 **ProcessPages**

以下代码片段显示属性的用法（设置文档第1页的缩放系数）：

```java
PdfPageEditor editor = new PdfPageEditor();
editor.bindPdf("input.pdf");
editor.setZoom(0.5f);
editor.setProcessPages(new int[] { 1 });
editor.save("output.pdf");
```


**重大更改** - RichTextBoxField.RValue 属性被重命名为 **RichTextValue**

以下代码片段展示了重命名字段的使用示例：

```java
Document doc = new Document("input.pdf");

RichTextBoxField rt = new RichTextBoxField(doc.getPages().get_Item(1), new Rectangle(50, 600, 250, 650));
rt.setPartialName("rt");
doc.getForm().add(rt);
doc.save("34834.pdf");
Document doc1 = new Document("34834.pdf");
((RichTextBoxField)doc1.getForm().get("rt")).setRichTextValue("<p>This is my <b>paragraph</b></p>");

doc1.save("output.pdf");
```

**InsertBlankColumnAtFirst** 选项已添加到 **ExcelSaveOptions 类**

以下代码片段展示了如何抑制第一个空白列的出现：

```java
Document doc = new Document(inFile);

ExcelSaveOptions options = new ExcelSaveOptions();

options.setInsertBlankColumnAtFirst(false);

doc.save(outFile, options);
```

**PageInfo** 属性已添加到 **SvgLoadOptions 类**

以下代码片段展示了如何使用 SvgLoadOptions 并通过 PageInfo 属性设置边距信息：

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

**ConversionEngines** 枚举被添加到 **SvgLoadOptions** 类。

定义了以下值：

- **LegacyEngine** - Svg 处理的旧引擎
- **NewEngine** - 新的 Svg 处理引擎

**ConversionEngine** 属性被添加到 **SvgLoadOptions** 类中

LegacyEngine 仍然是默认值，因为 NewEngine 处于 B 测试阶段。
以下代码片段展示了如何使用新引擎的示例：

```java
SvgLoadOptions options = new SvgLoadOptions();

options.ConversionEngine = SvgLoadOptions.ConversionEngines.NewEngine;
String inFile = "36516_2_income.svg";
String outFile = "36516_2_income.pdf";
Document pdfDocument = new Document(inFile, options);
pdfDocument.save(outFile);
```


**ColumnAdjustment** 属性已添加到 **Table** 类中

ColumnAdjustment 枚举已添加到 com.aspose.pdf 包中

添加了以下值：

- **Customized** - 用户手动设置 ColumnWidth。
- **AutoFitToContent** - 自动适应内容

**ColumnAdjustment** 属性已添加到 **Table** 类中

默认值是 Customized。

以下代码片段显示了 ColumnAdjustment 属性的用法示例：

```java
Table hTable = new Table();
hTable.getMargin().setTop(4);
hTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5F, Color.getBlack()));
hTable.setDefaultCellPadding(new MarginInfo(1, 1, 1, 1));
hTable.setAlignment(HorizontalAlignment.Left);
hTable.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
```

**MinimizeTheNumberOfWorksheets** 属性已引入 **ExcelSaveOptions** 对象。

以下代码片段显示了如何尽量减少工作表的数量：

```java
Document doc = new Document("Original.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
//将此属性设置为 true
options.setMinimizeTheNumberOfWorksheets(true);
doc.save("output.xls", options);
```


**默认**值已添加到**PageLayout**枚举中。

以下代码片段将PageLayout设置为默认值：

```java
Document doc1 = new Document("input.pdf");
doc1.setPageLayout(PageLayout.Default);
doc1.save("output.pdf");
```

**圆角端点**支持已实现于**InkAnnotation**

**CapStyle**枚举已添加到**com.aspose.pdf**包中
以下是可用的值

- **Rectangular** - 默认指定值
- **Rounded** - 圆角
- **CapStyle**属性已添加到**InkAnnotation**类中

以下代码片段展示了如何将InkAnnotation的角设置为圆角：

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


**PDFNEWJAVA-33498** - 提供支持从 BufferedImage 添加图像到 PDF 文档

以下代码片段显示了如何从 BufferedImage 添加图像：

```java
BufferedImage originalImage = ImageIO.read(new File("c:\\image\\anyImage.jpg"));
Document pdfDocument1 = new Document();
Page page2 = pdfDocument1.getPages().add();
page2.getResources().getImages().add(originalImage)
```

**PDFNEWJAVA-34088** - PDF 到 HTML 转换：指定图像文件夹

以下代码片段显示了如何指定图像文件夹：

```java
Document pdfDocument = new Document(testdata + "PDFNEWJAVA_34088.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.SpecialFolderForAllImages = testdata + "SpecialFolderForAllImages";
pdfDocument.save(testout + "PDFNEWJAVA_34088.html", saveOptions);
```

**PDFNEWJAVA-33203** - 设置 PDF 中图像的 DPI/PPI

以下代码片段显示了如何更改 PDF 文件中的图像分辨率：

```java
String myDir = "D:\\Temp\\";
File fileIn = new File(myDir+"image.jpg");
FileInputStream in = new FileInputStream(fileIn)

File fileOut = new File(myDir+"image.pdf");
FileOutputStream out = new FileOutputStream(fileOut);
//测试 PDF 创建
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
//内部图像分辨率更改
doc = new Document(myDir+"image.pdf");
XImageCollection images = doc.getPages().get_Item(1).getResources().getImages();
ByteArrayOutputStream baos = new ByteArrayOutputStream();
images.get_Item(1).save(baos, 10, 10);//定义水平和垂直分辨率
images.get_Item(1).replace(new ByteArrayInputStream(baos.toByteArray()));
doc.save(myDir+"imageWithNewResolution.pdf");
```

**总结：**

**添加的类：**

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

## 类的更改：

**com.aspose.pdf.facades.Form**

更改：

- public java.util.Map getButtonOptionValues(String fieldName) -> public java.util.Hashtable<String,String> getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfConverter**
添加：

- public int getCoordinateType()
- public void setCoordinateType(int value)
  弃用：
- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileInfo**
更改：

- public java.util.Map getHeader() -> public java.util.Map<String, String> getHeader()
- public void setHeader(java.util.Map value) -> public void setHeader(java.util.Map<String,String> value

**com.aspose.pdf.facades.PdfFileSignature**
弃用：

- public boolean isContainSignature()
- public boolean isCoversWholeDocument(String signName)
  新增：
- public boolean containsSignature()
- public boolean containsUsageRights()
- public void removeUsageRights()

**com.aspose.pdf.facades.PdfPageEditor**
更改：

- public int[] getPages_Rename_Namesake() -> public int[] getProcessPages()
- public void setPages(int[] value) -> public void setProcessPages(int[] value)
- public java.util.Map getPageRotations() -> public java.util.Map<Integer, Integer> getPageRotations()
- public void setPageRotations(java.util.Map value) -> public void setPageRotations(java.util.Map<Integer, Integer> value)

**com.aspose.pdf.facades.PdfViewer**
弃用：

- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)
  新增：
- public int getCoordinateType()
- public void setCoordinateType(int value)

**com.aspose.pdf.facades.PdfXmpMetadata**
更改：

- public IDictionary getExtensionFields() -> public java.util.Hashtable<String, XmpPdfAExtensionSchema> getExtensionFields()

**com.aspose.pdf.generator.legacyxmlmodel.Attachment** 添加:

- public InputStream AttachedStream

**com.aspose.pdf.generator.legacyxmlmodel.BorderInfo** 添加:

- public void setBorderStyle(int borderSide, int style)

**com.aspose.pdf.generator.legacyxmlmodel.BoxVerticalAlignmentType**

- 从类中移除已弃用状态

**com.aspose.pdf.generator.legacyxmlmodel.Cell** 添加:

- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo value)
- public String getText()

**com.aspose.pdf.generator.legacyxmlmodel.HeaderFooter** 添加:

- public Object completeClone()
- public Object completeCloneAll()

**com.aspose.pdf.generator.legacyxmlmodel.Heading** 从以下内容中移除已弃用状态:

- public int getBulletAlignment()
- public void setBulletAlignment(int value)

**com.aspose.pdf.generator.legacyxmlmodel.Image** 添加:

- public Image(HeaderFooter hf)

**com.aspose.pdf.generator.legacyxmlmodel.JavaScripts** 添加:

- public void remove(Cell jsToRemove)

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**
已添加：

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

已废弃：

- public int getBookMarkLevel()
- public void setBookMarkLevel(int value)
- public int getDirectModeItemType()
- public void setDirectModeItemType(int value)
- public int getDirectModeItemsCount()
- public void setDirectModeItemsCount(int value)

**com.aspose.pdf.generator.legacyxmlmodel.LinkAction**
已添加：

- public String SoundFileName

**com.aspose.pdf.generator.legacyxmlmodel.Paragraphs**
已添加：

- public void add(Paragraph paragraph)
- void addHeading(段落 段落)
- public int indexOf(段落 段落)
- public void copyTo(段落[] 段落数组, int 索引)
- public void insert(段落 插入后的段落, 段落 新段落)

**com.aspose.pdf.generator.legacyxmlmodel.Row**  
已更改：

- DefaultCellTextInfo 转换为 getter 和 setter 字段  
  新增：
- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo 值)
- public Object deepClone()

**com.aspose.pdf.generator.legacyxmlmodel.Section**  
新增：

- public ColumnInfo 列信息
- public int getPageCount()
- public void setPageCount(int 值)
- public String 断开段落文本
- public Object deepClone()
- public Object completeClone()
- public HeaderFooter insertHeader(int 类型)
- public HeaderFooter insertFooter(int 类型)
- public Object getObjectByID(String ID)

**com.aspose.pdf.generator.legacyxmlmodel.Sections**  
新增：

- public Sections()
- public Section add()
- public void insert(int 索引, Section 部分)

- public void insert(插入后的部分, Section 新部分)
- public void remove(Section sectionToRemove)  
- public void copyTo(Section[] secArray, int index)  
- public int indexOf(Section section)  
- public void set_Item(int index, Section value)  
- public Section get_Item(String sectionID)  
- public void set_Item(String sectionID, Section value)  

**com.aspose.pdf.generator.legacyxmlmodel.Security**  
添加:  

- public boolean isDefaultAllAllowed()  
- public void setDefaultAllAllowed(boolean value)  

**com.aspose.pdf.generator.legacyxmlmodel.Shapes**  
添加:  

- public void add(Shape shape)  
- public void remove(Shape shapeToRemove)  
- public void copyTo(Shape[] shapeArray, int index)  
- public int indexOf(Shape shape)  

**com.aspose.pdf.generator.legacyxmlmodel.Table**  
更改:  

- FixedWidth 转换为 getter 和 setter 字段  
- DefaultCellTextInfo 转换为 getter 和 setter 字段  
  添加:  
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
新增：  

- public int getCapacity()  
- public void setCapacity(int value)  

**com.aspose.pdf.generator.legacyxmlmodel.TextInfo**  
更改：  

- 以下字段列表已更改为单独的getter和setter字段：  

```java

 FontSize, FontName, TruetypeFontFileName, IsUnicode, FontAfmFile, FontPfmFile, FontOutlineFile, FontEncodingFile,
 IsTrueTypeFontBold, IsTrueTypeFontItalic,{color} {color:#222222}FontEncoding, IsFontEmbedded, IsUnderline,{color}
 {color:#222222}IsOverline,{color} {color:#222222}CharSpace, WordSpace, LineSpacing, OverlineOffset, UnderlineOffset, RenderingMode,
 Color, BackgroundColor, IsRightToLeft, StrokeWidth, StrokeColor, IsBaseline, Alignment.

```


添加了：

- public float getFontSize() // 获取字体大小
- public void setFontSize(float value) // 设置字体大小
- public String getFontName() // 获取字体名称
- public void setFontName(String value) // 设置字体名称
- public String getTruetypeFontFileName() // 获取TrueType字体文件名
- public void setTruetypeFontFileName(String value) // 设置TrueType字体文件名
- public boolean isUnicode() // 是否为Unicode
- public void setUnicode(boolean value) // 设置是否为Unicode
- public String getFontAfmFile() // 获取字体AFM文件
- public void setFontAfmFile(String value) // 设置字体AFM文件
- public String getFontPfmFile() // 获取字体PFM文件
- public void setFontPfmFile(String value) // 设置字体PFM文件
- public String getFontOutlineFile() // 获取字体轮廓文件
- public void setFontOutlineFile(String value) // 设置字体轮廓文件
- public String getFontEncodingFile() // 获取字体编码文件
- public void setFontEncodingFile(String value) // 设置字体编码文件
- public boolean isTrueTypeFontBold() // 是否为TrueType字体加粗
- public void setTrueTypeFontBold(boolean value) // 设置TrueType字体加粗
- public boolean isTrueTypeFontItalic() // 是否为TrueType字体斜体
- public void setTrueTypeFontItalic(boolean value) // 设置TrueType字体斜体
- public String getFontEncoding() // 获取字体编码
- public void setFontEncoding(String value) // 设置字体编码
- public boolean isFontEmbedded() // 是否嵌入字体
- public void setFontEmbedded(boolean value) // 设置嵌入字体
- public boolean isUnderline() // 是否有下划线

- public void setUnderline(boolean value) // 设置下划线
- public boolean isOverline() // 是否有上划线
- public void setOverline(boolean value) // 设置上划线
- public float getCharSpace() // 获取字符间距
- public void setCharSpace(float value) // 设置字符间距
- public float getWordSpace() // 获取单词间距
- public void setWordSpace(float value) // 设置单词间距
- public float getLineSpacing() // 获取行间距
- public void setLineSpacing(float value) // 设置行间距
- public float getOverlineOffset() // 获取上划线偏移量
- public void setOverlineOffset(float value) // 设置上划线偏移量
- public float getUnderlineOffset() // 获取下划线偏移量
- public void setUnderlineOffset(float value) // 设置下划线偏移量
- public int getRenderingMode() // 获取渲染模式
- public void setRenderingMode(int value) // 设置渲染模式
- public Color getColor() // 获取颜色
- public void setColor(Color value) // 设置颜色
- public Color getBackgroundColor() // 获取背景颜色
- public void setBackgroundColor(Color value) // 设置背景颜色
- public boolean isRightToLeft() // 是否从右到左
- public void setRightToLeft(boolean value) // 设置从右到左
- public float getStrokeWidth() // 获取描边宽度
- public void setStrokeWidth(float value) // 设置描边宽度
- public Color getStrokeColor() // 获取描边颜色
- public void setStrokeColor(Color value) // 设置描边颜色
- public boolean isBaseline() // 是否为基线
- public void setBaseline(boolean value) // 设置基线
- public int getAlignment() // 获取对齐方式

- public void setAlignment(int value) // 设置对齐方式

**com.aspose.pdf.BaseOperatorCollection**  
更改：

- implements ICollection -> implements ICollection< Operator >

**com.aspose.pdf.Border**  
更改：

- public int getVCornerRaduis() -> public int getVCornerRadius()
- public void setVCornerRaduis(int value) -> public void setVCornerRadius(int value)  
  添加已弃用：
- public int getVCornerRaduis()
- public void setVCornerRaduis(int value)

**com.aspose.pdf.DataUtils**  
更改：

- 内部化

**com.aspose.pdf.ExcelSaveOptions**  
添加：

- public boolean getMinimizeTheNumberOfWorksheets()
- public void setMinimizeTheNumberOfWorksheets(boolean value)
- public boolean getInsertBlankColumnAtFirst()
- public void setInsertBlankColumnAtFirst(boolean value)
- public boolean getUniformWorksheets()
- public void setUniformWorksheets(boolean value)

**com.aspose.pdf.Font**  
添加：

- public void save(OutputStream stream)

**com.aspose.pdf.Form**  
添加：

- public FieldsEnumerator(IDocument document, List< Object > fields)

**com.aspose.pdf.HtmlSaveOptions:**  
添加：


- public FontSourceCollection getFontSources()

**com.aspose.pdf.InkAnnotation**  
新增：

- public int getCapStyle()  
- public void setCapStyle(int value)

**com.aspose.pdf.LineAnnotation**  
新增：

- public Measure getMeasure()  
- public void setMeasure(Measure value)

**com.aspose.pdf.LoadFormat:**  
变更：

- public static final int InfoPath - 已移除  
- public static final int AutoDetect - 新增

**com.aspose.pdf.Metadata**  
变更：

- public IDictionary getExtensionFields() -> public java.util.Hashtable< String, XmpPdfAExtensionSchema > getExtensionFields() 

**com.aspose.pdf.PageLayout**  
新增：

- public static final int Default

**com.aspose.pdf.PolylineAnnotation**  
新增：

- public Measure getMeasure()  
- public void setMeasure(Measure value)

**com.aspose.pdf.PopupAnnotation**  
新增：

- public MarkupAnnotation getParent()  
- public void setParent(MarkupAnnotation value)

**com.aspose.pdf.RichTextBoxField**  
变更：

- public String getRValue() -> public String getRichTextValue()  

- public void setRValue(String value) -> public void setRichTextValue(String value)

**com.aspose.pdf.SaveOptions.BorderPartStyle**  
已添加：

- public java.awt.Color color

**com.aspose.pdf.SvgLoadOptions**  
已添加：

- public static final class ConversionEngines
- public int ConversionEngine
- public PageInfo getPageInfo()
- public void setPageInfo(PageInfo value)

**com.aspose.pdf.Table**  
已添加：

- public int getColumnAdjustment()
- public void setColumnAdjustment(int value)

**com.aspose.pdf.TextFragmentAbsorber**  
已添加：

- public TextReplaceOptions getTextReplaceOptions()
- public void setTextReplaceOptions(TextReplaceOptions value)

**com.aspose.pdf.TextReplaceOptions**  
已添加：

- public static final class ReplaceAdjustment
- public int getReplaceAdjustmentAction()
- public void setReplaceAdjustmentAction(int value)
- public TextReplaceOptions(int adjustment, int scope)

**com.aspose.pdf.XFA**  
已添加：

- public void setFieldImage(String fieldName, InputStream image)