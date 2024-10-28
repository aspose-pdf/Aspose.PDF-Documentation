---
title: Aspose.PDF for Java 9.5.0의 공개 API 변경 사항
type: docs
weight: 70
url: /java/public-api-changes-in-aspose-pdf-for-java-9-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

이 페이지는 [Aspose.PDF for Java 9.5.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry576058.aspx)에 도입된 공개 API 변경 사항을 나열합니다. 여기에는 새로운 공개 메소드와 사용되지 않는 공개 메소드뿐만 아니라 Aspose.PDF for Java의 내부 동작에 대한 변경 사항도 포함되어 있으며, 이는 기존 코드에 영향을 미칠 수 있습니다. 회귀로 볼 수 있고 기존 동작을 수정하는 동작은 특히 중요하며 여기에 문서화되어 있습니다.

{{% /alert %}}

**PdfViewer 및 PdfConverter에 CoordinateType 속성이 추가되었습니다**<p>
CoordinateType 속성은 인쇄 가능한 영역을 MediaBox 또는 CropBox(기본값)로 설정할 수 있게 합니다.

**XFA 클래스에 SetFieldImage 메소드가 추가되었습니다:**

public void SetFieldImage(string fieldName, Stream image)

예제:

다음 코드 스니펫은 XFA 양식 필드에 이미지를 설정하는 방법을 보여줍니다:

```java

Document doc = new Document("doc.pdf");
InputStream fs = new FileInputStream("image.jpg");
doc.getForm().getXFA().setFieldImage("form1\[0\].ImageField1\[0\]", fs);
doc.save("37017-1.pdf");
```

**ReplaceAdjustment** 열거형이 **TextReplaceOptions** 클래스에 추가되었습니다.

이 열거형은 다음 값을 제공합니다:

- **None** - 아무 작업도 하지 않으며, 줄의 길이가 변경될 수 있습니다.
- **AdjustSpaceWidth** - 단어 사이의 간격을 조정하여 줄 길이를 유지하려고 시도합니다.

**ReplaceAdjustmentAction** 속성이 **TextReplaceOptions** 클래스에 추가되었습니다.

**TextReplaceOptions** 클래스는 **ReplaceAdjustment** 매개변수를 설정할 수 있는 새로운 생성자를 가집니다:

TextReplaceOptions(int adjustment, int scope)

**TextReplaceOptions** 속성이 **TextFragmentAbsorber** 클래스에 추가되었습니다.

**Ellipse** 클래스가 구현되었습니다:

생성자:

public Ellipse(float left, float bottom, float width, float height)

속성:

- Left - 타원의 왼쪽 위치를 나타내는 float 값입니다.

- Bottom - 타원의 아래쪽 위치를 나타내는 float 값입니다.

- Width - 타원의 너비를 나타내는 부동 소수점 값입니다.
- Height - 타원의 높이를 나타내는 부동 소수점 값입니다.

예제:
다음 코드 스니펫은 타원을 추가하는 방법을 보여줍니다:

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

**Path** 클래스가 구현되었습니다

생성자:

public Path()
public Path(Shape[] shapes)

속성:

- Shapes - 도형 컬렉션

예제:
다음 코드 스니펫은 경로를 추가하는 방법을 보여줍니다:

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


**HtmlFragment** 클래스가 com.aspose.pdf 패키지에 추가되었습니다.

생성자:

- public HtmlFragment(string text)

매개변수:

- Text - HTML 텍스트
  속성:
- Text - HTML 텍스트

예제:
다음 코드 조각은 HTML 조각을 추가하는 방법을 보여줍니다:

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

**ContainsUsageRights()** 메서드가 **PdfFileSignature** 클래스에 추가되었습니다.

**RemoveUsageRights()** 메서드가 **PdfFileSignature** 클래스에 추가되었습니다.

예제:

다음 코드는 문서에서 사용 권한 기능을 제거하는 방법을 보여줍니다:

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


**isContainSignature()** 메서드가 **ContainsSignature(...)**로 이름이 변경되었습니다.

- 이전 메서드 이름은 제거되지 않았지만, 향후 제거될 예정으로 사용 중단 표시가 되었습니다.
    **isCoversWholeDocument()** 메서드가 **CoversWholeDocument(...)**로 이름이 변경되었습니다.
- 이전 메서드 이름은 제거되지 않았지만, 향후 제거될 예정으로 사용 중단 표시가 되었습니다.

**Measure** 클래스가 **com.aspose.pdf** 패키지에 추가되었습니다.

클래스는 Measure 좌표 시스템을 설명합니다. Measure 클래스의 멤버:

생성자:

- public Measure(Annotation annotation)

get/set 속성:

- ScaleRatio - 도면의 축척 비율을 나타내는 문자열입니다.
- XFormat - x축을 따라, 그리고 Y가 없을 경우 y축을 따라 변화 측정을 위한 숫자 형식 배열
- YFormat - y축을 따라 변화 측정을 위한 숫자 형식 배열.
- DistanceFormat - 모든 방향의 거리 측정을 위한 숫자 형식 배열.
- AreaFormat - 면적 측정을 위한 숫자 형식 배열.

- AngleFormat - 각도 측정을 위한 숫자 형식 배열.
- SlopeFormat - 선의 기울기를 측정하기 위한 숫자 형식 배열입니다.
- Origin - 기본 사용자 공간 좌표계에서 측정 좌표계의 원점을 지정하는 점입니다.
- XYFactor - y축의 가장 큰 단위를 x축의 가장 큰 단위로 변환하는 데 사용되는 계수입니다.

**NumberFormat** 클래스가 **Measure** 클래스에 추가되었습니다.

이 클래스는 측정을 위한 숫자 형식을 나타냅니다.

생성자:

- public NumberFormat(Measure measure)

get/set 속성:

- UnitLabel - 단위를 표시하기 위한 레이블을 지정하는 텍스트 문자열입니다.
- ConvresionFactor - 이전 숫자 형식 배열 요소의 부분 단위로 된 값을 이 숫자 형식의 단위 값으로 변환하기 위해 사용되는 변환 계수입니다.
- FractionDisplayment - 분수 값이 표시되는 방식입니다.
- Precision - FractionDisplayment가 ShowAsDecimal인 경우, 이 값은 분수 값의 정밀도를 나타냅니다; 10의 배수여야 합니다. 기본값은 100입니다.
- Denominator - FractionDisplayment가 ShowAsFraction인 경우, 이 값은 분수의 분모입니다.
 기본 값은 16입니다.  
- ForceDenominator - FractionDisplayment가 ShowAsFraction인 경우, 이 값은 분수가 약분될지 여부를 결정합니다. 값이 true이면 분수가 약분되지 않을 수 있습니다.  
- ThousandsSeparator - 수치 값을 표시할 때 천 단위 사이에 사용할 텍스트입니다. 빈 문자열은 텍스트가 추가되지 않음을 나타냅니다. 기본값은 쉼표입니다.  
- FractionSeparator - 수치 값을 표시할 때 소수점 위치로 사용할 텍스트입니다. 빈 문자열은 기본값이 사용됨을 나타냅니다. 기본값은 마침표 문자입니다.  
- BeforeText - 레이블의 왼쪽에 연결될 텍스트입니다.  
- AfterText - 레이블 뒤에 연결될 텍스트입니다.  

**FractionStyle** 열거형이 **NumberFormat** 클래스에 추가되었습니다.

FractionStyle 값:

- ShowAsDecimal - 분수 값을 소수로 표시합니다.  
- ShowAsFraction - 분수 값을 분수로 표시합니다.  
- Round - 분수 값을 가장 가까운 정수로 반올림합니다.  
- Truncate - 전체 단위를 얻기 위해 잘라냅니다.  

**NumberFormatList** 클래스가 **Measure** 클래스에 추가되었습니다.  
클래스는 숫자 형식의 목록을 나타냅니다.

생성자:

- public NumberFormatList(Measure measure)

속성:

- get_Item(int) 및 set_Item(int index, NumberFormat value) - 인덱스로 숫자 형식을 리스트에서 가져오거나 설정합니다.
- getCount()- 리스트의 항목 수를 셉니다.

메서드:

- public void add(NumberFormat value)
- 리스트에 숫자 형식을 추가합니다.
- public void insert(int index, NumberFormat value)
- 리스트에 숫자 형식을 삽입합니다.
- public void removeAt(int index)
- 리스트에서 숫자 형식을 제거합니다.

**Measure** 속성이 **LineAnnotation** 및 **PolyLineAnnotation** 클래스에 추가되었습니다.

예제:

다음 예제는 LineAnnotation에서 Measure를 사용하는 방법을 보여줍니다:

```java
Document doc = new Document("source.pdf");
Rectangle rect = new Rectangle(260, 630, 451, 662);
LineAnnotation line = new LineAnnotation(doc.getPages().get_Item(1), rect, new Point(266, 657), new Point(446, 656));
line.setColor(Color.getRed());
//확장선 매개변수 설정
line.setLeaderLine(-15);
line.setLeaderLineExtension(5);
//선의 끝 스타일 설정
line.setStartingStyle(LineEnding.OpenArrow);
line.setEndingStyle(LineEnding.OpenArrow);

//Measure 요소 생성
line.setMeasure(new Measure(line));
line.getMeasure().setDistanceFormat(new Measure.NumberFormatList(line.getMeasure()));
line.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(line.getMeasure()));
line.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
line.getMeasure().getDistanceFormat().get_Item(1).setFractionSeparator(".");
line.getMeasure().getDistanceFormat().get_Item(1).setConvresionFactor(1);

//측정선의 텍스트
line.setContents("155 mm");
//텍스트를 표시하기 위해 설정해야 합니다.
line.setShowCaption(true);
line.setCaptionPosition(CaptionPosition.Top);
doc.getPages().get_Item(1).getAnnotations().add(line);
doc.save("output.pdf");
```


다음 예제는 Measure를 PolylineAnnotation과 함께 사용하는 방법을 보여줍니다:

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
// 면적 또는 둘레선
PolylineAnnotation area = new PolylineAnnotation(doc.getPages().get_Item(1), rect, vertices);
area.setColor(Color.getRed());
// 둘레선에 대한 선 끝을 설정할 수 있습니다.
area.setStartingStyle(LineEnding.OpenArrow);
area.setEndingStyle(LineEnding.OpenArrow);
area.setMeasure(new Measure(area));
area.getMeasure().setDistanceFormat(new Measure.NumberFormatList(area.getMeasure()));
area.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(area.getMeasure()));
area.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
doc.getPages().get_Item(1).getAnnotations().add(area);
doc.save("output.pdf");
```


다음 코드 스니펫은 Measure 속성을 읽는 방법을 보여줍니다:

```java
// Measure 속성 읽기

Document doc = new Document("measure.pdf");

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getScaleRatio());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getUnitLabel());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getConvresionFactor());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getFractionSeparator());
```

**주요 변경 사항** - PdfPageEditor.Pages 속성이 **ProcessPages**로 이름이 변경되었습니다.

다음 코드 스니펫은 속성 사용법을 보여줍니다 (문서의 페이지 #1에 대한 줌 계수를 설정합니다):

```java
PdfPageEditor editor = new PdfPageEditor();
editor.bindPdf("input.pdf");
editor.setZoom(0.5f);
editor.setProcessPages(new int[] { 1 });
editor.save("output.pdf");
```


**중대한 변경 사항** - RichTextBoxField.RValue 속성이 **RichTextValue**로 이름이 변경되었습니다

다음 코드 스니펫은 이름이 변경된 필드가 사용된 예를 보여줍니다:

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

**InsertBlankColumnAtFirst** 옵션이 **ExcelSaveOptions 클래스**에 추가되었습니다

다음 코드 스니펫은 첫 번째 빈 열의 표시를 억제하는 방법을 보여줍니다:

```java
Document doc = new Document(inFile);

ExcelSaveOptions options = new ExcelSaveOptions();

options.setInsertBlankColumnAtFirst(false);

doc.save(outFile, options);
```

**PageInfo** 속성이 **SvgLoadOptions** 클래스에 추가되었습니다.

다음 코드 스니펫은 SvgLoadOptions를 사용하고 PageInfo 속성을 사용하여 여백 정보를 설정하는 방법을 보여줍니다:

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

**ConversionEngines** 열거형이 **SvgLoadOptions** 클래스에 추가되었습니다.

다음 값들이 정의되어 있습니다:

- **LegacyEngine** - Svg 처리의 레거시 엔진
- **NewEngine** - 새로운 Svg 처리 엔진

**ConversionEngine** 속성이 **SvgLoadOptions** 클래스에 추가되었습니다.

레거시 엔진은 여전히 기본값으로 남아 있습니다. 왜냐하면 NewEngine은 B-테스팅 단계에 있기 때문입니다. 다음 코드 스니펫은 새 엔진을 사용하는 예제를 보여줍니다:

```java
SvgLoadOptions options = new SvgLoadOptions();

options.ConversionEngine = SvgLoadOptions.ConversionEngines.NewEngine;
String inFile = "36516_2_income.svg";
String outFile = "36516_2_income.pdf";
Document pdfDocument = new Document(inFile, options);
pdfDocument.save(outFile);
```


**ColumnAdjustment** 속성이 **Table** 클래스에 추가되었습니다

ColumnAdjustment 열거형이 com.aspose.pdf 패키지에 추가되었습니다

다음 값들이 추가되었습니다:

- **Customized** - 사용자가 ColumnWidth를 수동으로 설정합니다.
- **AutoFitToContent** - 내용에 맞게 자동 조정합니다

**ColumnAdjustment** 속성이 **Table** 클래스에 추가되었습니다

기본 값은 Customized입니다.

다음 코드 스니펫은 ColumnAdjustment 속성 사용 예를 보여줍니다:

```java
Table hTable = new Table();
hTable.getMargin().setTop(4);
hTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5F, Color.getBlack()));
hTable.setDefaultCellPadding(new MarginInfo(1, 1, 1, 1));
hTable.setAlignment(HorizontalAlignment.Left);
hTable.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
```

**MinimizeTheNumberOfWorksheets** 속성이 **ExcelSaveOptions** 객체에 도입되었습니다.

다음 코드 스니펫은 가능한 워크시트 수를 최소화하는 방법을 보여줍니다:

```java
Document doc = new Document("Original.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
//이 속성을 true로 설정합니다
options.setMinimizeTheNumberOfWorksheets(true);
doc.save("output.xls", options);
```


**기본값**이 **PageLayout** 열거형에 추가되었습니다.

다음 코드 스니펫은 PageLayout을 기본값으로 설정합니다:

```java
Document doc1 = new Document("input.pdf");
doc1.setPageLayout (PageLayout.Default);
doc1.save("output.pdf");
```

**둥근 끝** 지원이 **InkAnnotation**에 구현되었습니다.

**CapStyle** 열거형이 **com.aspose.pdf** 패키지에 추가되었습니다. 다음 값들이 포함되어 있습니다

- **Rectangular** - 기본 지정 값
- **Rounded** - 둥근 모서리
- **CapStyle** 속성이 **InkAnnotation** 클래스에 추가되었습니다.

다음 코드 스니펫은 InkAnnotation 모서리를 둥글게 설정하는 방법을 보여줍니다:

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


**PDFNEWJAVA-33498** - BufferedImage에서 PDF 문서로 이미지 추가 지원 제공

다음 코드 조각은 BufferedImage에서 이미지 추가를 보여줍니다:

```java
BufferedImage originalImage = ImageIO.read(new File("c:\\image\\anyImage.jpg"));
Document pdfDocument1 = new Document();
Page page2 = pdfDocument1.getPages().add();
page2.getResources().getImages().add(originalImage)
```

**PDFNEWJAVA-34088** - PDF를 HTML로 변환: 이미지 폴더 지정

다음 코드 조각은 이미지 폴더를 지정하는 방법을 보여줍니다:

```java
Document pdfDocument = new Document(testdata + "PDFNEWJAVA_34088.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.SpecialFolderForAllImages = testdata + "SpecialFolderForAllImages";
pdfDocument.save(testout + "PDFNEWJAVA_34088.html", saveOptions);
```

**PDFNEWJAVA-33203** - PDF 내 이미지의 DPI/PPI 설정

다음 코드 조각은 PDF 파일에서 이미지 해상도를 변경하는 방법을 보여줍니다:

```java
String myDir = "D:\\Temp\\";
File fileIn = new File(myDir+"image.jpg");
FileInputStream in = new FileInputStream(fileIn)

File fileOut = new File(myDir+"image.pdf");
FileOutputStream out = new FileOutputStream(fileOut);
// PDF 생성 테스트
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
//내부 이미지 해상도 변경
doc = new Document(myDir+"image.pdf");
XImageCollection images = doc.getPages().get_Item(1).getResources().getImages();
ByteArrayOutputStream baos = new ByteArrayOutputStream();
images.get_Item(1).save(baos, 10, 10);//수평 및 수직 해상도 정의
images.get_Item(1).replace(new ByteArrayInputStream(baos.toByteArray()));
doc.save(myDir+"imageWithNewResolution.pdf");
```

**요약:**

**추가된 클래스:**

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

## 클래스의 변경 사항:

**com.aspose.pdf.facades.Form**

변경 사항:

- public java.util.Map getButtonOptionValues(String fieldName) -> public java.util.Hashtable<String,String> getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfConverter**
추가됨:

- public int getCoordinateType()
- public void setCoordinateType(int value)
  사용되지 않음:
- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileInfo**
변경 사항:

- public java.util.Map getHeader() -> public java.util.Map<String, String> getHeader()
- public void setHeader(java.util.Map value) -> public void setHeader(java.util.Map<String,String> value


**com.aspose.pdf.facades.PdfFileSignature**
Depricated:

- public boolean isContainSignature() // 서명이 포함되어 있는지 확인하는 메서드
- public boolean isCoversWholeDocument(String signName) // 주어진 서명 이름이 문서 전체를 덮고 있는지 확인하는 메서드
  Added:
- public boolean containsSignature() // 서명이 포함되어 있는지 확인하는 메서드
- public boolean containsUsageRights() // 사용 권한이 포함되어 있는지 확인하는 메서드
- public void removeUsageRights() // 사용 권한을 제거하는 메서드

**com.aspose.pdf.facades.PdfPageEditor**
Changes:

- public int[] getPages_Rename_Namesake() -> public int[] getProcessPages() // 페이지 처리 메서드로 이름 변경
- public void setPages(int[] value) -> public void setProcessPages(int[] value) // 페이지 설정 메서드로 이름 변경
- public java.util.Map getPageRotations() -> public java.util.Map<Integer, Integer> getPageRotations() // 페이지 회전 정보 반환 메서드
- public void setPageRotations(java.util.Map value) -> public void setPageRotations(java.util.Map<Integer, Integer> value) // 페이지 회전 정보 설정 메서드

**com.aspose.pdf.facades.PdfViewer**
Depricated:

- public boolean getShowHiddenAreas() // 숨겨진 영역 표시 여부를 반환하는 메서드
- public void setShowHiddenAreas(boolean value) // 숨겨진 영역 표시 여부를 설정하는 메서드
  Added:
- public int getCoordinateType() // 좌표 유형을 반환하는 메서드
- public void setCoordinateType(int value) // 좌표 유형을 설정하는 메서드

**com.aspose.pdf.facades.PdfXmpMetadata**
Changes:

- public IDictionary getExtensionFields() -> public java.util.Hashtable<String, XmpPdfAExtensionSchema> getExtensionFields() // 확장 필드를 반환하는 메서드로 변경

**com.aspose.pdf.generator.legacyxmlmodel.Attachment** 추가됨:

- public InputStream AttachedStream

**com.aspose.pdf.generator.legacyxmlmodel.BorderInfo** 추가됨:

- public void setBorderStyle(int borderSide, int style)

**com.aspose.pdf.generator.legacyxmlmodel.BoxVerticalAlignmentType**

- 클래스에서 사용 중단 상태 제거됨

**com.aspose.pdf.generator.legacyxmlmodel.Cell** 추가됨:

- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo value)
- public String getText()

**com.aspose.pdf.generator.legacyxmlmodel.HeaderFooter** 추가됨:

- public Object completeClone()
- public Object completeCloneAll()

**com.aspose.pdf.generator.legacyxmlmodel.Heading** 사용 중단 상태 제거됨:

- public int getBulletAlignment()
- public void setBulletAlignment(int value)

**com.aspose.pdf.generator.legacyxmlmodel.Image** 추가됨:

- public Image(HeaderFooter hf)

**com.aspose.pdf.generator.legacyxmlmodel.JavaScripts** 추가됨:

- public void remove(Cell jsToRemove)

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**
추가됨:

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

추가됨 사용 중단됨:

- public int getBookMarkLevel()
- public void setBookMarkLevel(int value)
- public int getDirectModeItemType()
- public void setDirectModeItemType(int value)
- public int getDirectModeItemsCount()
- public void setDirectModeItemsCount(int value)

**com.aspose.pdf.generator.legacyxmlmodel.LinkAction**  
추가됨:

- public String SoundFileName

**com.aspose.pdf.generator.legacyxmlmodel.Paragraphs**  
추가됨:

- public void add(Paragraph paragraph)
- void addHeading(문단 문단)
- public int indexOf(문단 문단)
- public void copyTo(문단[] 문단배열, int 인덱스)
- public void insert(문단 삽입할문단후, 문단 새문단)

**com.aspose.pdf.generator.legacyxmlmodel.Row**
변경됨:

- DefaultCellTextInfo를 getter 및 setter 필드로
  추가됨:
- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo 값)
- public Object deepClone()

**com.aspose.pdf.generator.legacyxmlmodel.Section**
추가됨:

- public ColumnInfo ColumnInfo
- public int getPageCount()
- public void setPageCount(int 값)
- public String BreakParaText
- public Object deepClone()
- public Object completeClone()
- public HeaderFooter insertHeader(int 타입)
- public HeaderFooter insertFooter(int 타입)
- public Object getObjectByID(String ID)

**com.aspose.pdf.generator.legacyxmlmodel.Sections**
추가됨:

- public Sections()
- public Section add()
- public void insert(int 인덱스, Section 섹션)

- public void insert(섹션 삽입할섹션후, Section 새섹션)
- public void remove(제거할 섹션)
- public void copyTo(섹션 배열, 인덱스)
- public int indexOf(섹션)
- public void set_Item(인덱스, 섹션 값)
- public Section get_Item(섹션 ID)
- public void set_Item(섹션 ID, 섹션 값)

**com.aspose.pdf.generator.legacyxmlmodel.Security**  
추가됨:

- public boolean isDefaultAllAllowed()
- public void setDefaultAllAllowed(불리언 값)

**com.aspose.pdf.generator.legacyxmlmodel.Shapes**  
추가됨:

- public void add(도형)
- public void remove(제거할 도형)
- public void copyTo(도형 배열, 인덱스)
- public int indexOf(도형)

**com.aspose.pdf.generator.legacyxmlmodel.Table**  
변경됨:

- FixedWidth를 getter 및 setter 필드로 변경
- DefaultCellTextInfo를 getter 및 setter 필드로 변경  
  추가됨:
- public float getFixedWidth()
- public void setFixedWidth(실수 값)
- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo 값)

- public Cell getCell(행, 열, 테이블 변경 여부)
- public void formatColumnsWithFormatInfo(TableFormatInfo info, int firstColumn, int maxColumns)
- public void formatTableWithFormatInfo(TableFormatInfo info, int firstColumn, int firstRow, int maxRows, int maxColumns)
- public void formatRowsWithFormatInfo(TableFormatInfo info, int firstRow, int maxRows)
- public void setColumnWidth(int columnNumber, float width)
- public String getColumnWidths()
- public void setColumnWidths(String value)

**com.aspose.pdf.generator.legacyxmlmodel.TabStops**
추가됨:

- public int getCapacity()
- public void setCapacity(int value)

**com.aspose.pdf.generator.legacyxmlmodel.TextInfo**
변경됨:

- 다음 필드 목록이 개별 getter 및 setter 필드로 변경되었습니다:

```java

 FontSize, FontName, TruetypeFontFileName, IsUnicode, FontAfmFile, FontPfmFile, FontOutlineFile, FontEncodingFile,
 IsTrueTypeFontBold, IsTrueTypeFontItalic,{color} {color:#222222}FontEncoding, IsFontEmbedded, IsUnderline,{color}
 {color:#222222}IsOverline,{color} {color:#222222}CharSpace, WordSpace, LineSpacing, OverlineOffset, UnderlineOffset, RenderingMode,
 Color, BackgroundColor, IsRightToLeft, StrokeWidth, StrokeColor, IsBaseline, Alignment.

```


추가됨:

- public float getFontSize()
- public void setFontSize(float value)
- public String getFontName()
- public void setFontName(String value)
- public String getTruetypeFontFileName()
- public void setTruetypeFontFileName(String value)
- public boolean isUnicode()
- public void setUnicode(boolean value)
- public String getFontAfmFile()
- public void setFontAfmFile(String value)
- public String getFontPfmFile()
- public void setFontPfmFile(String value)
- public String getFontOutlineFile()
- public void setFontOutlineFile(String value)
- public String getFontEncodingFile()
- public void setFontEncodingFile(String value)
- public boolean isTrueTypeFontBold()
- public void setTrueTypeFontBold(boolean value)
- public boolean isTrueTypeFontItalic()
- public void setTrueTypeFontItalic(boolean value)
- public String getFontEncoding()
- public void setFontEncoding(String value)
- public boolean isFontEmbedded()
- public void setFontEmbedded(boolean value)
- public boolean isUnderline()

- public void setUnderline(boolean value)
- public boolean isOverline() // public boolean isOverline() 
- public void setOverline(boolean value) // public void setOverline(boolean value)
- public float getCharSpace() // public float getCharSpace()
- public void setCharSpace(float value) // public void setCharSpace(float value)
- public float getWordSpace() // public float getWordSpace()
- public void setWordSpace(float value) // public void setWordSpace(float value)
- public float getLineSpacing() // public float getLineSpacing()
- public void setLineSpacing(float value) // public void setLineSpacing(float value)
- public float getOverlineOffset() // public float getOverlineOffset()
- public void setOverlineOffset(float value) // public void setOverlineOffset(float value)
- public float getUnderlineOffset() // public float getUnderlineOffset()
- public void setUnderlineOffset(float value) // public void setUnderlineOffset(float value)
- public int getRenderingMode() // public int getRenderingMode()
- public void setRenderingMode(int value) // public void setRenderingMode(int value)
- public Color getColor() // public Color getColor()
- public void setColor(Color value) // public void setColor(Color value)
- public Color getBackgroundColor() // public Color getBackgroundColor()
- public void setBackgroundColor(Color value) // public void setBackgroundColor(Color value)
- public boolean isRightToLeft() // public boolean isRightToLeft()
- public void setRightToLeft(boolean value) // public void setRightToLeft(boolean value)
- public float getStrokeWidth() // public float getStrokeWidth()
- public void setStrokeWidth(float value) // public void setStrokeWidth(float value)
- public Color getStrokeColor() // public Color getStrokeColor()
- public void setStrokeColor(Color value) // public void setStrokeColor(Color value)
- public boolean isBaseline() // public boolean isBaseline()
- public void setBaseline(boolean value) // public void setBaseline(boolean value)
- public int getAlignment() // public int getAlignment()

- public void setAlignment(int value) // public void setAlignment(int value)

**com.aspose.pdf.BaseOperatorCollection**  
변경 사항:

- implements ICollection -> implements ICollection< Operator >

**com.aspose.pdf.Border**  
변경 사항:

- public int getVCornerRaduis() -> public int getVCornerRadius()
- public void setVCornerRaduis(int value) -> public void setVCornerRadius(int value)  
  추가된 Deprecated:
- public int getVCornerRaduis()
- public void setVCornerRaduis(int value)

**com.aspose.pdf.DataUtils**  
변경 사항:

- Internalized

**com.aspose.pdf.ExcelSaveOptions**  
추가됨:

- public boolean getMinimizeTheNumberOfWorksheets()
- public void setMinimizeTheNumberOfWorksheets(boolean value)
- public boolean getInsertBlankColumnAtFirst()
- public void setInsertBlankColumnAtFirst(boolean value)
- public boolean getUniformWorksheets()
- public void setUniformWorksheets(boolean value)

**com.aspose.pdf.Font**  
추가됨:

- public void save(OutputStream stream)

**com.aspose.pdf.Form**  
추가됨:

- public FieldsEnumerator(IDocument document, List< Object > fields)

**com.aspose.pdf.HtmlSaveOptions:**  
추가됨:


- public FontSourceCollection getFontSources()

**com.aspose.pdf.InkAnnotation**  
추가됨:

- public int getCapStyle()
- public void setCapStyle(int value)

**com.aspose.pdf.LineAnnotation**  
추가됨:

- public Measure getMeasure()
- public void setMeasure(Measure value)

**com.aspose.pdf.LoadFormat:**  
변경 사항:

- public static final int InfoPath - 제거됨
- public static final int AutoDetect - 추가됨

**com.aspose.pdf.Metadata**  
변경 사항:

- public IDictionary getExtensionFields() -> public java.util.Hashtable< String, XmpPdfAExtensionSchema > getExtensionFields()

**com.aspose.pdf.PageLayout**  
추가됨:

- public static final int Default

**com.aspose.pdf.PolylineAnnotation**  
추가됨:

- public Measure getMeasure()
- public void setMeasure(Measure value)

**com.aspose.pdf.PopupAnnotation**  
추가됨:

- public MarkupAnnotation getParent()
- public void setParent(MarkupAnnotation value)

**com.aspose.pdf.RichTextBoxField**  
변경 사항:

- public String getRValue() -> public String getRichTextValue()

- public void setRValue(String value) -> public void setRichTextValue(String value)

**com.aspose.pdf.SaveOptions.BorderPartStyle**  
추가됨:

- public java.awt.Color color

**com.aspose.pdf.SvgLoadOptions**  
추가됨:

- public static final class ConversionEngines
- public int ConversionEngine
- public PageInfo getPageInfo()
- public void setPageInfo(PageInfo value)

**com.aspose.pdf.Table**  
추가됨:

- public int getColumnAdjustment()
- public void setColumnAdjustment(int value)

**com.aspose.pdf.TextFragmentAbsorber**  
추가됨:

- public TextReplaceOptions getTextReplaceOptions()
- public void setTextReplaceOptions(TextReplaceOptions value)

**com.aspose.pdf.TextReplaceOptions**  
추가됨:

- public static final class ReplaceAdjustment
- public int getReplaceAdjustmentAction()
- public void setReplaceAdjustmentAction(int value)
- public TextReplaceOptions(int adjustment, int scope)

**com.aspose.pdf.XFA**  
추가됨:

- public void setFieldImage(String fieldName, InputStream image)