---
title: Aspose.PDF for Java 9.5.0におけるパブリックAPIの変更
type: docs
weight: 70
url: ja/java/public-api-changes-in-aspose-pdf-for-java-9-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

このページでは、[Aspose.PDF for Java 9.5.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry576058.aspx)で導入されたパブリックAPIの変更点を一覧にしています。新しく追加されたパブリックメソッドや廃止されたメソッドだけでなく、Aspose.PDF for Javaの動作に関する変更点で、既存のコードに影響を与える可能性のあるものも含まれています。回帰と見なされる可能性があり、既存の動作を変更する動作は特に重要であり、ここに文書化されています。

{{% /alert %}}

**CoordinateTypeプロパティがPdfViewerとPdfConverterに追加されました**<p>
CoordinateTypeプロパティは、印刷可能領域をMediaBoxまたはCropBox（デフォルト値）に設定することができます。

**SetFieldImageメソッドがXFAクラスに追加されました：**

public void SetFieldImage(string fieldName, Stream image)

例:

次のコードスニペットは、XFAフォームフィールドに画像を設定する方法を示しています：

```java

Document doc = new Document("doc.pdf");
InputStream fs = new FileInputStream("image.jpg");
doc.getForm().getXFA().setFieldImage("form1\[0\].ImageField1\[0\]", fs);
doc.save("37017-1.pdf");
```

**ReplaceAdjustment** 列挙型が **TextReplaceOptions** クラスに追加されました

この列挙型は次の値を提供します：

- **None** - アクションなし、行の長さが変更される可能性があります
- **AdjustSpaceWidth** - 行の長さを保つために単語間のスペースを調整しようとします

**ReplaceAdjustmentAction** プロパティが **TextReplaceOptions** クラスに追加されました

**TextReplaceOptions** クラスには、新しいコンストラクタが追加され、**ReplaceAdjustment** パラメータを設定することができます：

TextReplaceOptions(int adjustment, int scope)

**TextReplaceOptions** プロパティが **TextFragmentAbsorber** クラスに追加されました

**Ellipse** クラスが実装されました：

コンストラクタ:

public Ellipse(float left, float bottom, float width, float height)

プロパティ:

- Left - 楕円の左位置を示す float 値です。

- Bottom - 楕円の下位置を示す float 値です。

- Width - 楕円の幅を示す浮動小数点値。
- Height - 楕円の高さを示す浮動小数点値。

例:
次のコードスニペットは、楕円を追加する方法を示しています:

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

**Path** クラスが実装されました

コンストラクタ:

public Path()
public Path(Shape[] shapes)

プロパティ:

- Shapes - 形状のコレクション

例:
次のコードスニペットは、Pathを追加する方法を示しています:

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


**HtmlFragment** クラスがパッケージ com.aspose.pdf に追加されました

コンストラクタ:

- public HtmlFragment(string text)

パラメータ:

- Text - HTML テキスト
  プロパティ:
- Text - HTML テキスト

例:
以下のコードスニペットは、HTMLフラグメントを追加する方法を示しています:

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

**ContainsUsageRights()** メソッドが **PdfFileSignature** クラスに追加されました

**RemoveUsageRights()** メソッドが **PdfFileSignature** クラスに追加されました

例:

以下のコードは、ドキュメントから使用権機能を削除する方法を示しています:

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


**isContainSignature()** メソッドは **ContainsSignature(...)** に名前が変更されました

- 以前のメソッド名は削除されていませんが、将来削除されるために非推奨としてマークされています。
    **isCoversWholeDocument()** メソッドは **CoversWholeDocument(...)** に名前が変更されました
- 以前のメソッド名は削除されていませんが、将来削除されるために非推奨としてマークされています。

**Measure** クラスが **com.aspose.pdf** パッケージに追加されました

このクラスは座標系を示します。Measure クラスのメンバー:

コンストラクタ:

- public Measure(Annotation annotation)

get/set プロパティ:

- ScaleRatio - 描画のスケール比を表すテキスト文字列。
- XFormat - x軸に沿った変化の測定のための数値形式の配列であり、Yが存在しない場合はy軸に沿った変化の測定にも使われます。
- YFormat - y軸に沿った変化の測定のための数値形式の配列。
- DistanceFormat - 任意の方向の距離の測定のための数値形式の配列。
- AreaFormat - 面積の測定のための数値形式の配列。

- AngleFormat - 角度の測定のための数値形式の配列。
- SlopeFormat - 線の傾きの測定のための数値フォーマット配列。
- Origin - デフォルトのユーザースペース座標で測定座標系の原点を指定する点。
- XYFactor - y軸に沿った最大単位をx軸に沿った最大単位に変換するために使用される係数。

**NumberFormat** クラスは **Measure** クラスに追加されました

このクラスは測定のための数値フォーマットを表します。

コンストラクタ:

- public NumberFormat(Measure measure)

取得/設定プロパティ:

- UnitLabel - 単位を表示するためのラベルを指定するテキスト文字列。
- ConvresionFactor - 前の数値フォーマット配列要素の部分単位での値を、この数値フォーマットの単位での値に変換するために使用される変換係数。
- FractionDisplayment - 分数値がどのように表示されるか。
- Precision - FractionDisplayment が ShowAsDecimal の場合、この値は分数値の精度です。10の倍数である必要があります。デフォルトは100です。
- Denominator - FractionDisplayment が ShowAsFraction の場合、この値は分数の分母です。
 デフォルト値は16です。

- ForceDenominator - FractionDisplaymentがShowAsFractionの場合、この値は分数が約分されるかどうかを決定します。値がtrueの場合、分数は約分されない可能性があります。
- ThousandsSeparator - 数値の表示において、千の位の間に使用されるテキストです。空の文字列は、テキストが追加されないことを示します。デフォルトはカンマです。
- FractionSeparator - 数値の表示において、小数点として使用されるテキストです。空の文字列は、デフォルトが使用されることを示します。デフォルトはピリオド文字です。
- BeforeText - ラベルの左に連結されるテキストです。
- AfterText - ラベルの後に連結されるテキストです。

列挙型**FractionStyle**が**NumberFormat**クラスに追加されました。

FractionStyleの値：

- ShowAsDecimal - 分数値を小数として表示します。
- ShowAsFraction - 分数値を分数として表示します。
- Round - 分数値を最も近い整数に丸めます。
- Truncate - 整数単位を達成するために切り捨てます。

**NumberFormatList**クラスが**Measure**クラスに追加されました。
The class represents Represents list of number formats.

クラスは数値フォーマットのリストを表します。

Constructor:

- public NumberFormatList(Measure measure)

コンストラクタ:

- public NumberFormatList(Measure measure)

Properties:

- get_Item(int) and set_Item(int index, NumberFormat value) - Gets or sets number format in list by its index.
- getCount()- Count if items in the list.

プロパティ:

- get_Item(int) と set_Item(int index, NumberFormat value) - インデックスによってリスト内の数値フォーマットを取得または設定します。
- getCount() - リスト内のアイテムの数をカウントします。

Methods:

- public void add(NumberFormat value)
- Adds number format to list.
- public void insert(int index, NumberFormat value)
- Inserts number format into list.
- public void removeAt(int index)
- Removes number format from list.

メソッド:

- public void add(NumberFormat value)
- 数値フォーマットをリストに追加します。
- public void insert(int index, NumberFormat value)
- 数値フォーマットをリストに挿入します。
- public void removeAt(int index)
- リストから数値フォーマットを削除します。

**Measure** property was added to **LineAnnotation** and **PolyLineAnnotation** classes.

**Measure** プロパティが **LineAnnotation** および **PolyLineAnnotation** クラスに追加されました。

Examples:

Following example demonstrates how to use Measure with LineAnnotation:

例:

以下の例は、LineAnnotationでMeasureを使用する方法を示しています:

```java
Document doc = new Document("source.pdf");
Rectangle rect = new Rectangle(260, 630, 451, 662);
LineAnnotation line = new LineAnnotation(doc.getPages().get_Item(1), rect, new Point(266, 657), new Point(446, 656));
line.setColor(Color.getRed());
//set extension line parameters.
line.setLeaderLine(-15);
line.setLeaderLineExtension(5);
//set line endings
line.setStartingStyle(LineEnding.OpenArrow);
line.setEndingStyle(LineEnding.OpenArrow);

//create Measure element
line.setMeasure(new Measure(line));
// メジャー要素を作成する
line.getMeasure().setDistanceFormat(newMeasure.NumberFormatList(line.getMeasure()));
line.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(line.getMeasure()));
line.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
line.getMeasure().getDistanceFormat().get_Item(1).setFractionSeparator(".");
line.getMeasure().getDistanceFormat().get_Item(1).setConvresionFactor(1);

//text of measure line
line.setContents("155 mm");
//this must be set to show the text.
line.setShowCaption(true);
line.setCaptionPosition(CaptionPosition.Top);
doc.getPages().get_Item(1).getAnnotations().add(line);
doc.save("output.pdf");
```


以下の例は、PolylineAnnotationでMeasureを使用する方法を示しています。

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
//エリアまたは周囲線
PolylineAnnotation area = new PolylineAnnotation(doc.getPages().get_Item(1), rect, vertices);
area.setColor(Color.getRed());
//線の端を周囲線に設定できます。
area.setStartingStyle(LineEnding.OpenArrow);
area.setEndingStyle(LineEnding.OpenArrow);
area.setMeasure(new Measure(area));
area.getMeasure().setDistanceFormat(new Measure.NumberFormatList(area.getMeasure()));
area.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(area.getMeasure()));
area.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
doc.getPages().get_Item(1).getAnnotations().add(area);
doc.save("output.pdf");
```

以下のコードスニペットは、Measureプロパティを読み取る方法を示しています。

```java
// 測定プロパティの読み取り

Document doc = new Document("measure.pdf");

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getScaleRatio());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getUnitLabel());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getConvresionFactor());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getFractionSeparator());
```

**重大な変更** - PdfPageEditor.Pages プロパティは **ProcessPages** に名前が変更されました

次のコードスニペットはプロパティの使用法を示しています（ドキュメントのページ#1のズーム係数を設定します）:

```java
PdfPageEditor editor = new PdfPageEditor();
editor.bindPdf("input.pdf");
editor.setZoom(0.5f);
editor.setProcessPages(new int[] { 1 });
editor.save("output.pdf");
```


**破壊的変更** - RichTextBoxField.RValue プロパティは **RichTextValue** に名前が変更されました

次のコードスニペットは、名前が変更されたフィールドが使用されたサンプルを示しています:

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

**InsertBlankColumnAtFirst** オプションが **ExcelSaveOptions クラス** に追加されました

次のコードスニペットは、最初の空白列の出現を抑制する方法を示しています:

```java
Document doc = new Document(inFile);

ExcelSaveOptions options = new ExcelSaveOptions();

options.setInsertBlankColumnAtFirst(false);

doc.save(outFile, options);
```

**PageInfo** プロパティが **SvgLoadOptions** クラスに追加されました。

次のコードスニペットは、SvgLoadOptions を使用し、PageInfo プロパティで余白情報を設定する方法を示しています:

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

**ConversionEngines** 列挙型が **SvgLoadOptions** クラスに追加されました。

以下の値が定義されています：

- **LegacyEngine** - Svg処理のレガシーエンジン
- **NewEngine** - 新しいSvg処理エンジン

**ConversionEngine** プロパティが **SvgLoadOptions** クラスに追加されました。

レガシーエンジンはまだデフォルト値です。なぜなら、新しいエンジンはBテスト段階にあるからです。
以下のコードスニペットは新しいエンジンを使用するサンプルを示しています：

```java
SvgLoadOptions options = new SvgLoadOptions();

options.ConversionEngine = SvgLoadOptions.ConversionEngines.NewEngine;
String inFile = "36516_2_income.svg";
String outFile = "36516_2_income.pdf";
Document pdfDocument = new Document(inFile, options);
pdfDocument.save(outFile);
```


**ColumnAdjustment** プロパティが **Table** クラスに追加されました

ColumnAdjustment 列挙型が com.aspose.pdf パッケージに追加されました

以下の値が追加されました:

- **Customized** - ユーザーが手動で ColumnWidth を設定します。
- **AutoFitToContent** - コンテンツに自動フィットを行います

**ColumnAdjustment** プロパティが **Table** クラスに追加されました

デフォルト値は Customized です。

次のコードスニペットは、ColumnAdjustment プロパティの使用例を示しています:

```java
Table hTable = new Table();
hTable.getMargin().setTop(4);
hTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5F, Color.getBlack()));
hTable.setDefaultCellPadding(new MarginInfo(1, 1, 1, 1));
hTable.setAlignment(HorizontalAlignment.Left);
hTable.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
```

**MinimizeTheNumberOfWorksheets** プロパティが **ExcelSaveOptions** オブジェクトに導入されました。

次のコードスニペットは、可能な限りワークシートの数を最小限に抑える方法を示しています:

```java
Document doc = new Document("Original.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
//このプロパティを true に設定します
options.setMinimizeTheNumberOfWorksheets(true);
doc.save("output.xls", options);
```


**Default** 値が **PageLayout** 列挙型に追加されました。

次のコードスニペットは、PageLayoutをDefault値に設定します:

```java
Document doc1 = new Document("input.pdf");
doc1.setPageLayout(PageLayout.Default);
doc1.save("output.pdf");
```

**Rounded Ends** のサポートが **InkAnnotation** に実装されました。

**CapStyle** 列挙型が **com.aspose.pdf** パッケージに追加されました。以下の値が存在します。

- **Rectangular** - デフォルトの指定値
- **Rounded** - 角が丸くなる
- **CapStyle** プロパティが **InkAnnotation** クラスに追加されました。

次のコードスニペットは、InkAnnotationの角を丸くする方法を示しています:

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


**PDFNEWJAVA-33498** - BufferedImageからPDFドキュメントに画像を追加するサポートを提供

次のコードスニペットは、BufferedImageから画像を追加する方法を示しています:

```java
BufferedImage originalImage = ImageIO.read(new File("c:\\image\\anyImage.jpg"));
Document pdfDocument1 = new Document();
Page page2 = pdfDocument1.getPages().add();
page2.getResources().getImages().add(originalImage)
```

**PDFNEWJAVA-34088** - PDFからHTMLへの変換: 画像フォルダーを指定する

次のコードスニペットは、画像フォルダーを指定する方法を示しています:

```java
Document pdfDocument = new Document(testdata + "PDFNEWJAVA_34088.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.SpecialFolderForAllImages = testdata + "SpecialFolderForAllImages";
pdfDocument.save(testout + "PDFNEWJAVA_34088.html", saveOptions);
```

**PDFNEWJAVA-33203** - PDF内の画像のDPI/PPIを設定

次のコードスニペットは、PDFファイル内の画像解像度を変更する方法を示しています:

```java
String myDir = "D:\\Temp\\";
File fileIn = new File(myDir+"image.jpg");
FileInputStream in = new FileInputStream(fileIn)

File fileOut = new File(myDir+"image.pdf");
FileOutputStream out = new FileOutputStream(fileOut);
//テスト用PDF作成
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
//内部画像解像度の変更
doc = new Document(myDir+"image.pdf");
XImageCollection images = doc.getPages().get_Item(1).getResources().getImages();
ByteArrayOutputStream baos = new ByteArrayOutputStream();
images.get_Item(1).save(baos, 10, 10);//水平および垂直解像度を定義
images.get_Item(1).replace(new ByteArrayInputStream(baos.toByteArray()));
doc.save(myDir+"imageWithNewResolution.pdf");
```

**概要:**

**追加されたクラス:**

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

## クラスの変更:

**com.aspose.pdf.facades.Form**

変更:

- public java.util.Map getButtonOptionValues(String fieldName) -> public java.util.Hashtable<String,String> getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfConverter**
追加:

- public int getCoordinateType()
- public void setCoordinateType(int value)
  廃止:
- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileInfo**
変更:

- public java.util.Map getHeader() -> public java.util.Map<String, String> getHeader()
- public void setHeader(java.util.Map value) -> public void setHeader(java.util.Map<String,String> value

**com.aspose.pdf.facades.PdfFileSignature**
非推奨:

- public boolean isContainSignature() 
- public boolean isCoversWholeDocument(String signName) 
  追加: 
- public boolean containsSignature() 
- public boolean containsUsageRights() 
- public void removeUsageRights()

**com.aspose.pdf.facades.PdfPageEditor** 変更点:

- public int[] getPages_Rename_Namesake() -> public int[] getProcessPages() 
- public void setPages(int[] value) -> public void setProcessPages(int[] value) 
- public java.util.Map getPageRotations() -> public java.util.Map<Integer, Integer> getPageRotations() 
- public void setPageRotations(java.util.Map value) -> public void setPageRotations(java.util.Map<Integer, Integer> value)

**com.aspose.pdf.facades.PdfViewer** 非推奨:

- public boolean getShowHiddenAreas() 
- public void setShowHiddenAreas(boolean value) 
  追加: 
- public int getCoordinateType() 
- public void setCoordinateType(int value)

**com.aspose.pdf.facades.PdfXmpMetadata** 変更点:

- public IDictionary getExtensionFields() -> public java.util.Hashtable<String, XmpPdfAExtensionSchema> getExtensionFields()

**com.aspose.pdf.generator.legacyxmlmodel.Attachment**  
追加:

- public InputStream AttachedStream

**com.aspose.pdf.generator.legacyxmlmodel.BorderInfo**  
追加:

- public void setBorderStyle(int borderSide, int style)

**com.aspose.pdf.generator.legacyxmlmodel.BoxVerticalAlignmentType**  

- クラスから非推奨ステータスを削除

**com.aspose.pdf.generator.legacyxmlmodel.Cell**  
追加:

- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo value)
- public String getText()

**com.aspose.pdf.generator.legacyxmlmodel.HeaderFooter**  
追加:

- public Object completeClone()
- public Object completeCloneAll()

**com.aspose.pdf.generator.legacyxmlmodel.Heading**  
非推奨ステータスを削除:

- public int getBulletAlignment()
- public void setBulletAlignment(int value)

**com.aspose.pdf.generator.legacyxmlmodel.Image**  
追加:

- public Image(HeaderFooter hf)

**com.aspose.pdf.generator.legacyxmlmodel.JavaScripts**  
追加:

- public void remove(Cell jsToRemove)

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**
追加:

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

追加 非推奨:

- public int getBookMarkLevel()
- public void setBookMarkLevel(int value)
- public int getDirectModeItemType()
- public void setDirectModeItemType(int value)
- public int getDirectModeItemsCount()
- public void setDirectModeItemsCount(int value)

**com.aspose.pdf.generator.legacyxmlmodel.LinkAction**
追加:

- public String SoundFileName

**com.aspose.pdf.generator.legacyxmlmodel.Paragraphs**
追加:

- public void add(Paragraph paragraph)
- void addHeading(段落 段落)
- public int indexOf(段落 段落)
- public void copyTo(段落[] 段落配列, int インデックス)
- public void insert(挿入後の段落 段落, 新しい段落 段落)

**com.aspose.pdf.generator.legacyxmlmodel.Row**  
変更:

- DefaultCellTextInfo をゲッターとセッターのフィールドに変更  
  追加:
- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo 値)
- public Object deepClone()

**com.aspose.pdf.generator.legacyxmlmodel.Section**  
追加:

- public ColumnInfo ColumnInfo
- public int getPageCount()
- public void setPageCount(int 値)
- public String BreakParaText
- public Object deepClone()
- public Object completeClone()
- public HeaderFooter insertHeader(int タイプ)
- public HeaderFooter insertFooter(int タイプ)
- public Object getObjectByID(String ID)

**com.aspose.pdf.generator.legacyxmlmodel.Sections**  
追加:

- public Sections()
- public Section add()
- public void insert(int インデックス, Section セクション)

- public void insert(挿入後のセクション セクション, 新しいセクション セクション)
- public void remove(セクション sectionToRemove)
- public void copyTo(セクション[] secArray, int index)
- public int indexOf(セクション section)
- public void set_Item(int index, セクション value)
- public セクション get_Item(String sectionID)
- public void set_Item(String sectionID, セクション value)

**com.aspose.pdf.generator.legacyxmlmodel.Security** 追加:

- public boolean isDefaultAllAllowed()
- public void setDefaultAllAllowed(boolean value)

**com.aspose.pdf.generator.legacyxmlmodel.Shapes** 追加:

- public void add(形状 shape)
- public void remove(形状 shapeToRemove)
- public void copyTo(形状[] shapeArray, int index)
- public int indexOf(形状 shape)

**com.aspose.pdf.generator.legacyxmlmodel.Table** 変更:

- FixedWidth を getter および setter フィールドに
- DefaultCellTextInfo を getter および setter フィールドに
  追加:
- public float getFixedWidth()
- public void setFixedWidth(float value)
- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo value)

- public セル getCell(int row, int column, boolean isTableChanged)
- public void formatColumnsWithFormatInfo(TableFormatInfo info, int firstColumn, int maxColumns)  
  パブリックボイドformatColumnsWithFormatInfo(TableFormatInfo info, int firstColumn, int maxColumns)

- public void formatTableWithFormatInfo(TableFormatInfo info, int firstColumn, int firstRow, int maxRows, int maxColumns)  
  パブリックボイドformatTableWithFormatInfo(TableFormatInfo info, int firstColumn, int firstRow, int maxRows, int maxColumns)

- public void formatRowsWithFormatInfo(TableFormatInfo info, int firstRow, int maxRows)  
  パブリックボイドformatRowsWithFormatInfo(TableFormatInfo info, int firstRow, int maxRows)

- public void setColumnWidth(int columnNumber, float width)  
  パブリックボイドsetColumnWidth(int columnNumber, float width)

- public String getColumnWidths()  
  パブリックストリングgetColumnWidths()

- public void setColumnWidths(String value)  
  パブリックボイドsetColumnWidths(String value)

**com.aspose.pdf.generator.legacyxmlmodel.TabStops**  
追加済み:

- public int getCapacity()  
  パブリックイントgetCapacity()

- public void setCapacity(int value)  
  パブリックボイドsetCapacity(int value)

**com.aspose.pdf.generator.legacyxmlmodel.TextInfo**  
変更済み:

- The next list of the fields was changed to the separate getter and setter field:  
  次のフィールドのリストは、個別のゲッターおよびセッターフィールドに変更されました:

```java

 FontSize, FontName, TruetypeFontFileName, IsUnicode, FontAfmFile, FontPfmFile, FontOutlineFile, FontEncodingFile,
 IsTrueTypeFontBold, IsTrueTypeFontItalic,{color} {color:#222222}FontEncoding, IsFontEmbedded, IsUnderline,{color}
 {color:#222222}IsOverline,{color} {color:#222222}CharSpace, WordSpace, LineSpacing, OverlineOffset, UnderlineOffset, RenderingMode,
 Color, BackgroundColor, IsRightToLeft, StrokeWidth, StrokeColor, IsBaseline, Alignment.

```


追加:

- public float getFontSize()  
  フォントサイズを取得します

- public void setFontSize(float value)  
  フォントサイズを設定します

- public String getFontName()  
  フォント名を取得します

- public void setFontName(String value)  
  フォント名を設定します

- public String getTruetypeFontFileName()  
  TrueTypeフォントファイル名を取得します

- public void setTruetypeFontFileName(String value)  
  TrueTypeフォントファイル名を設定します

- public boolean isUnicode()  
  Unicodeかどうかを確認します

- public void setUnicode(boolean value)  
  Unicodeかどうかを設定します

- public String getFontAfmFile()  
  フォントAFMファイルを取得します

- public void setFontAfmFile(String value)  
  フォントAFMファイルを設定します

- public String getFontPfmFile()  
  フォントPFMファイルを取得します

- public void setFontPfmFile(String value)  
  フォントPFMファイルを設定します

- public String getFontOutlineFile()  
  フォントアウトラインファイルを取得します

- public void setFontOutlineFile(String value)  
  フォントアウトラインファイルを設定します

- public String getFontEncodingFile()  
  フォントエンコーディングファイルを取得します

- public void setFontEncodingFile(String value)  
  フォントエンコーディングファイルを設定します

- public boolean isTrueTypeFontBold()  
  TrueTypeフォントが太字かどうかを確認します

- public void setTrueTypeFontBold(boolean value)  
  TrueTypeフォントを太字に設定します

- public boolean isTrueTypeFontItalic()  
  TrueTypeフォントが斜体かどうかを確認します

- public void setTrueTypeFontItalic(boolean value)  
  TrueTypeフォントを斜体に設定します

- public String getFontEncoding()  
  フォントエンコーディングを取得します

- public void setFontEncoding(String value)  
  フォントエンコーディングを設定します

- public boolean isFontEmbedded()  
  フォントが埋め込まれているかどうかを確認します

- public void setFontEmbedded(boolean value)  
  フォントを埋め込むかどうかを設定します

- public boolean isUnderline()  
  下線が引かれているかどうかを確認します

- public void setUnderline(boolean value)  
  下線を引くかどうかを設定します
- public boolean isOverline() // オーバーラインがあるかどうかを返す
- public void setOverline(boolean value) // オーバーラインの有無を設定する
- public float getCharSpace() // 文字間隔を取得する
- public void setCharSpace(float value) // 文字間隔を設定する
- public float getWordSpace() // 単語間隔を取得する
- public void setWordSpace(float value) // 単語間隔を設定する
- public float getLineSpacing() // 行間隔を取得する
- public void setLineSpacing(float value) // 行間隔を設定する
- public float getOverlineOffset() // オーバーラインのオフセットを取得する
- public void setOverlineOffset(float value) // オーバーラインのオフセットを設定する
- public float getUnderlineOffset() // 下線のオフセットを取得する
- public void setUnderlineOffset(float value) // 下線のオフセットを設定する
- public int getRenderingMode() // レンダリングモードを取得する
- public void setRenderingMode(int value) // レンダリングモードを設定する
- public Color getColor() // 色を取得する
- public void setColor(Color value) // 色を設定する
- public Color getBackgroundColor() // 背景色を取得する
- public void setBackgroundColor(Color value) // 背景色を設定する
- public boolean isRightToLeft() // 右から左への書字方向かどうかを返す
- public void setRightToLeft(boolean value) // 右から左への書字方向を設定する
- public float getStrokeWidth() // ストローク幅を取得する
- public void setStrokeWidth(float value) // ストローク幅を設定する
- public Color getStrokeColor() // ストロークの色を取得する
- public void setStrokeColor(Color value) // ストロークの色を設定する
- public boolean isBaseline() // ベースラインかどうかを返す
- public void setBaseline(boolean value) // ベースラインを設定する
- public int getAlignment() // 整列を取得する
- public void setAlignment(int value) // 整列を設定する

**com.aspose.pdf.BaseOperatorCollection** 変更:

- implements ICollection -> implements ICollection< Operator >

**com.aspose.pdf.Border** 変更:

- public int getVCornerRaduis() -> public int getVCornerRadius()
- public void setVCornerRaduis(int value) -> public void setVCornerRadius(int value)
  追加された非推奨:
- public int getVCornerRaduis()
- public void setVCornerRaduis(int value)

**com.aspose.pdf.DataUtils** 変更:

- 内部化

**com.aspose.pdf.ExcelSaveOptions** 追加:

- public boolean getMinimizeTheNumberOfWorksheets()
- public void setMinimizeTheNumberOfWorksheets(boolean value)
- public boolean getInsertBlankColumnAtFirst()
- public void setInsertBlankColumnAtFirst(boolean value)
- public boolean getUniformWorksheets()
- public void setUniformWorksheets(boolean value)

**com.aspose.pdf.Font** 追加:

- public void save(OutputStream stream)

**com.aspose.pdf.Form** 追加:

- public FieldsEnumerator(IDocument document, List< Object > fields)

**com.aspose.pdf.HtmlSaveOptions:** 追加:


- public FontSourceCollection getFontSources()

**com.aspose.pdf.InkAnnotation**  
追加:

- public int getCapStyle()  
- public void setCapStyle(int value)

**com.aspose.pdf.LineAnnotation**  
追加:

- public Measure getMeasure()  
- public void setMeasure(Measure value)

**com.aspose.pdf.LoadFormat:**  
変更:

- public static final int InfoPath - 削除されました  
- public static final int AutoDetect - 追加されました

**com.aspose.pdf.Metadata**  
変更:

- public IDictionary getExtensionFields() -> public java.util.Hashtable< String, XmpPdfAExtensionSchema > getExtensionFields() 

**com.aspose.pdf.PageLayout**  
追加:

- public static final int Default

**com.aspose.pdf.PolylineAnnotation**  
追加:

- public Measure getMeasure()  
- public void setMeasure(Measure value)

**com.aspose.pdf.PopupAnnotation**  
追加:

- public MarkupAnnotation getParent()  
- public void setParent(MarkupAnnotation value)

**com.aspose.pdf.RichTextBoxField**  
変更:

- public String getRValue() -> public String getRichTextValue()

- public void setRValue(String value) -> public void setRichTextValue(String value)

**com.aspose.pdf.SaveOptions.BorderPartStyle**  
追加:

- public java.awt.Color color

**com.aspose.pdf.SvgLoadOptions**  
追加:

- public static final class ConversionEngines
- public int ConversionEngine
- public PageInfo getPageInfo()
- public void setPageInfo(PageInfo value)

**com.aspose.pdf.Table**  
追加:

- public int getColumnAdjustment()
- public void setColumnAdjustment(int value)

**com.aspose.pdf.TextFragmentAbsorber**  
追加:

- public TextReplaceOptions getTextReplaceOptions()
- public void setTextReplaceOptions(TextReplaceOptions value)

**com.aspose.pdf.TextReplaceOptions**  
追加:

- public static final class ReplaceAdjustment
- public int getReplaceAdjustmentAction()
- public void setReplaceAdjustmentAction(int value)
- public TextReplaceOptions(int adjustment, int scope)

**com.aspose.pdf.XFA**  
追加:

- public void setFieldImage(String fieldName, InputStream image)