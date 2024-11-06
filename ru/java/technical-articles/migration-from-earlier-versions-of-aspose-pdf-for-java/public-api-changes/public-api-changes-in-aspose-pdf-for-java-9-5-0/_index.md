---
title: Изменения публичного API в Aspose.PDF для Java 9.5.0
type: docs
weight: 70
url: ru/java/public-api-changes-in-aspose-pdf-for-java-9-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

На этой странице перечислены изменения публичного API, введенные в [Aspose.PDF для Java 9.5.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry576058.aspx). Она включает не только новые и устаревшие публичные методы, но также описание любых изменений в поведении Aspose.PDF для Java, которые могут повлиять на существующий код. Любое поведение, которое может рассматриваться как регрессия и изменяет существующее поведение, особенно важно и задокументировано здесь.

{{% /alert %}}

**Свойство CoordinateType добавлено в PdfViewer и PdfConverter**<p>
Свойство CoordinateType позволяет установить печатную область в MediaBox или CropBox (значение по умолчанию)

**Метод SetFieldImage был добавлен в класс XFA:** 

public void SetFieldImage(string fieldName, Stream image)

Пример:

Следующий фрагмент кода показывает, как установить изображение для поля формы XFA:

```java

Document doc = new Document("doc.pdf");
InputStream fs = new FileInputStream("image.jpg");
doc.getForm().getXFA().setFieldImage("form1\[0\].ImageField1\[0\]", fs);
doc.save("37017-1.pdf");
```

**Перечисление ReplaceAdjustment** добавлено в класс **TextReplaceOptions**

Это перечисление предоставляет следующие значения:

- **None** - Нет действия, длина строки может измениться
- **AdjustSpaceWidth** - Попытаться отрегулировать пробелы между словами, чтобы сохранить длину строки

Свойство **ReplaceAdjustmentAction** добавлено в класс **TextReplaceOptions**

Класс **TextReplaceOptions** имеет новый конструктор, который позволяет установить параметр **ReplaceAdjustment**:

TextReplaceOptions(int adjustment, int scope)

Свойство **TextReplaceOptions** добавлено в класс **TextFragmentAbsorber**

Реализован класс **Ellipse**:

Конструктор:

public Ellipse(float left, float bottom, float width, float height)

Свойства:

- Left - значение float, указывающее левую позицию эллипса.

- Bottom - значение float, указывающее нижнюю позицию эллипса.
- Width - значение типа float, указывающее ширину эллипса.  
- Height - значение типа float, указывающее высоту эллипса.  

Пример:  
Следующий фрагмент кода показывает, как добавить эллипс:  

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

Класс **Path** был реализован  

Конструкторы:  

public Path()  
public Path(Shape[] shapes)  

Свойство:  

- Shapes - коллекция фигур  

Пример:  
Следующий фрагмент кода показывает, как добавить путь:  

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


**Класс HtmlFragment** был добавлен в пакет com.aspose.pdf*

Конструктор:

- public HtmlFragment(string text)

Параметр:

- Text - HTML текст
  Свойство:
- Text - HTML текст

Пример:
Следующий фрагмент кода показывает, как добавить HTML фрагмент:

```java
Document doc = new Document();
Page page = doc.getPages().add();
HtmlFragment titel = new HtmlFragment("<fontsize=10><b><i>Таблица</i></b></fontsize>");
titel.setKeptWithNext (true);
titel.getMargin().setBottom (10);
titel.getMargin().setTop (200);
page.getParagraphs().add(titel);
doc.Save(outFile);
```

Метод **ContainsUsageRights()** был добавлен в класс **PdfFileSignature**

Метод **RemoveUsageRights()** был добавлен в класс **PdfFileSignature**

Пример:

Следующий код показывает, как удалить функцию прав использования из документа:

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


**метод isContainSignature()** был переименован в **ContainsSignature(...)**

- Предыдущее имя метода не было удалено, но помечено как устаревшее и будет удалено в будущем.
    **метод isCoversWholeDocument()** был переименован в **CoversWholeDocument(...)**
- Предыдущее имя метода не было удалено, но помечено как устаревшее и будет удалено в будущем.

**класс Measure** был добавлен в пакет **com.aspose.pdf**

Класс описывает систему координат Measure. Члены класса Measure:

Конструктор:

- public Measure(Annotation annotation)

get/set Свойства:

- ScaleRatio - Текстовая строка, выражающая масштабный коэффициент чертежа.
- XFormat - Массив форматов чисел для измерения изменений вдоль оси x и, если Y не присутствует, также вдоль оси y.
- YFormat - Массив форматов чисел для измерения изменений вдоль оси y.
- DistanceFormat - Массив форматов чисел для измерения расстояния в любом направлении.
- AreaFormat - Массив форматов чисел для измерения площади.

- AngleFormat - Массив форматов чисел для измерения углов.
- SlopeFormat - Массив числовых форматов для измерения наклона линии.
- Origin - Точка, которая должна указывать начало системы координат измерения в координатах пользовательского пространства по умолчанию.
- XYFactor - Коэффициент, который должен использоваться для преобразования наибольших единиц вдоль оси y в наибольшие единицы вдоль оси x.

Класс **NumberFormat** был добавлен в класс **Measure**

Класс представляет числовой формат для измерения.

Конструктор:

- public NumberFormat(Measure measure)

get/set Свойства:

- UnitLabel - Текстовая строка, указывающая метку для отображения единиц.
- ConvresionFactor - Коэффициент преобразования, используемый для умножения значения в частичных единицах предыдущего элемента массива числового формата для получения значения в единицах этого числового формата.
- FractionDisplayment - Способ отображения дробных значений.
- Precision - Если FractionDisplayment имеет значение ShowAsDecimal, это значение является точностью дробного значения; Оно должно быть кратно 10. По умолчанию 100.
- Denominator - Если FractionDisplayment имеет значение ShowAsFraction, это значение является знаменателем дроби.
  Значение по умолчанию - 16.
- ForceDenominator - Если FractionDisplayment установлено на ShowAsFraction, это значение определяет, может ли дробь быть сокращена или нет. Если значение истинно, дробь не может быть сокращена.
- ThousandsSeparator - Текст, который должен использоваться между порядками тысяч при отображении числовых значений. Пустая строка указывает на то, что текст не должен быть добавлен. Значение по умолчанию - запятая.
- FractionSeparator - Текст, который должен использоваться в качестве десятичной позиции при отображении числовых значений. Пустая строка указывает на то, что должно использоваться значение по умолчанию. Значение по умолчанию - символ точки.
- BeforeText - Текст, который должен быть конкатенирован слева от метки.
- AfterText - Текст, который должен быть конкатенирован после метки.

Перечисление **FractionStyle** было добавлено в класс **NumberFormat**

Значения FractionStyle:

- ShowAsDecimal - Показать дробные значения как десятичные дроби.
- ShowAsFraction - Показать дробное значение как дробь.
- Round - Округлить дробные значения до ближайшего целого числа.
- Truncate - Усекать для получения целых единиц.

Класс **NumberFormatList** был добавлен в класс **Measure**

The class represents list of number formats.

Конструктор:

- public NumberFormatList(Measure measure)

Свойства:

- get_Item(int) и set_Item(int index, NumberFormat value) - Получает или задает числовой формат в списке по его индексу.
- getCount() - Количество элементов в списке.

Методы:

- public void add(NumberFormat value)
- Добавляет числовой формат в список.
- public void insert(int index, NumberFormat value)
- Вставляет числовой формат в список.
- public void removeAt(int index)
- Удаляет числовой формат из списка.

Свойство **Measure** было добавлено в классы **LineAnnotation** и **PolyLineAnnotation**.

Примеры:

Следующий пример демонстрирует, как использовать Measure с LineAnnotation:

```java
Document doc = new Document("source.pdf");
Rectangle rect = new Rectangle(260, 630, 451, 662);
LineAnnotation line = new LineAnnotation(doc.getPages().get_Item(1), rect, new Point(266, 657), new Point(446, 656));
line.setColor(Color.getRed());
//установить параметры линии выноски.
line.setLeaderLine(-15);
line.setLeaderLineExtension(5);
//установить окончания линии
line.setStartingStyle(LineEnding.OpenArrow);
line.setEndingStyle(LineEnding.OpenArrow);

//создать элемент Measure
line.setMeasure(new Measure(line));<p>
line.getMeasure().setDistanceFormat(newMeasure.NumberFormatList(line.getMeasure()));
line.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(line.getMeasure()));
line.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
line.getMeasure().getDistanceFormat().get_Item(1).setFractionSeparator(".");
line.getMeasure().getDistanceFormat().get_Item(1).setConvresionFactor(1);

//текст линии измерения
line.setContents("155 mm");
//это должно быть установлено, чтобы показать текст.
line.setShowCaption(true);
line.setCaptionPosition(CaptionPosition.Top);
doc.getPages().get_Item(1).getAnnotations().add(line);
doc.save("output.pdf");
```


Следующий пример демонстрирует, как использовать Measure с PolylineAnnotation:

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
//площадь или линия периметра
PolylineAnnotation area = new PolylineAnnotation(doc.getPages().get_Item(1), rect, vertices);
area.setColor(Color.getRed());
//линейные окончания могут быть установлены для линии периметра.
area.setStartingStyle(LineEnding.OpenArrow);
area.setEndingStyle(LineEnding.OpenArrow);
area.setMeasure(new Measure(area));
area.getMeasure().setDistanceFormat(new Measure.NumberFormatList(area.getMeasure()));
area.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(area.getMeasure()));
area.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("мм");
doc.getPages().get_Item(1).getAnnotations().add(area);
doc.save("output.pdf");
```

Следующий фрагмент кода демонстрирует, как считывать свойства Measure:

```java
//читать свойства Measure

Document doc = new Document("measure.pdf");

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getScaleRatio());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getUnitLabel());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getConvresionFactor());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getFractionSeparator());
```

**Кардинальное изменение** - Свойство PdfPageEditor.Pages было переименовано в **ProcessPages**

Следующий фрагмент кода показывает использование свойства (устанавливает коэффициент увеличения для страницы №1 документа):

```java
PdfPageEditor editor = new PdfPageEditor();
editor.bindPdf("input.pdf");
editor.setZoom(0.5f);
editor.setProcessPages(new int[] { 1 });
editor.save("output.pdf");
```


**Ломающее изменение** - Свойство RichTextBoxField.RValue было переименовано в **RichTextValue**

Следующий фрагмент кода показывает пример, где использовалось переименованное поле:

```java
Document doc = new Document("input.pdf");

RichTextBoxField rt = new RichTextBoxField(doc.getPages().get_Item(1), new Rectangle(50, 600, 250, 650));
rt.setPartialName("rt");
doc.getForm().add(rt);
doc.save("34834.pdf");
Document doc1 = new Document("34834.pdf");
((RichTextBoxField)doc1.getForm().get("rt")).setRichTextValue("<p>Это мой <b>абзац</b></p>");

doc1.save("output.pdf");
```

Опция **InsertBlankColumnAtFirst** была добавлена в **ExcelSaveOptions class**

Следующий фрагмент кода показывает, как подавить появление первого пустого столбца:

```java
Document doc = new Document(inFile);

ExcelSaveOptions options = new ExcelSaveOptions();

options.setInsertBlankColumnAtFirst(false);

doc.save(outFile, options);
```

Свойство **PageInfo** было добавлено в **SvgLoadOptions** class.

Следующий фрагмент кода показывает, как использовать SvgLoadOptions и установить информацию о полях с помощью свойства PageInfo:

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

Перечисление **ConversionEngines** было добавлено в класс **SvgLoadOptions**.

Определены следующие значения:

- **LegacyEngine** - устаревший механизм обработки Svg
- **NewEngine** - новый механизм обработки Svg

Свойство **ConversionEngine** было добавлено в класс **SvgLoadOptions**

LegacyEngine все еще является значением по умолчанию, так как NewEngine находится на стадии B-тестирования. Следующий фрагмент кода показывает пример использования нового механизма:

```java
SvgLoadOptions options = new SvgLoadOptions();

options.ConversionEngine = SvgLoadOptions.ConversionEngines.NewEngine;
String inFile = "36516_2_income.svg";
String outFile = "36516_2_income.pdf";
Document pdfDocument = new Document(inFile, options);
pdfDocument.save(outFile);
```


**Свойство ColumnAdjustment** было добавлено в класс **Table**

Перечисление ColumnAdjustment было добавлено в пакет com.aspose.pdf

были добавлены следующие значения:

- **Customized** - Пользователь устанавливает ширину столбца вручную.
- **AutoFitToContent** - Выполняет автоматическое подгонку под содержимое

**Свойство ColumnAdjustment** было добавлено в класс **Table**

Значение по умолчанию - Customized.

Следующий фрагмент кода показывает пример использования свойства ColumnAdjustment:

```java
Table hTable = new Table();
hTable.getMargin().setTop(4);
hTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5F, Color.getBlack()));
hTable.setDefaultCellPadding(new MarginInfo(1, 1, 1, 1));
hTable.setAlignment(HorizontalAlignment.Left);
hTable.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
```

**Свойство MinimizeTheNumberOfWorksheets** было введено в объект **ExcelSaveOptions**.

Следующий фрагмент кода показывает, как минимизировать возможное количество рабочих листов:

```java
Document doc = new Document("Original.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
//Установите это свойство в true
options.setMinimizeTheNumberOfWorksheets(true);
doc.save("output.xls", options);
```


**Значение по умолчанию** было добавлено в перечисление **PageLayout**.

Следующий фрагмент кода устанавливает PageLayout в значение по умолчанию:

```java
Document doc1 = new Document("input.pdf");
doc1.setPageLayout (PageLayout.Default);
doc1.save("output.pdf");
```

Была реализована поддержка **Округлённых концов** для **InkAnnotation**

Перечисление **CapStyle** было добавлено в пакет **com.aspose.pdf**
Присутствуют следующие значения

- **Rectangular** - Значение по умолчанию
- **Rounded** - округлённые углы
- Свойство **CapStyle** было добавлено в класс **InkAnnotation**

Следующий фрагмент кода показывает, как установить углы InkAnnotation как округлённые:

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


**PDFNEWJAVA-33498** - Обеспечить поддержку добавления изображения из BufferedImage в PDF документ

Следующий фрагмент кода показывает добавление изображения из BufferedImage:

```java
BufferedImage originalImage = ImageIO.read(new File("c:\\image\\anyImage.jpg"));
Document pdfDocument1 = new Document();
Page page2 = pdfDocument1.getPages().add();
page2.getResources().getImages().add(originalImage)
```

**PDFNEWJAVA-34088** - Конвертация PDF в HTML: Указать папку для изображений

Следующий фрагмент кода показывает, как указать папку для изображений:

```java
Document pdfDocument = new Document(testdata + "PDFNEWJAVA_34088.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.SpecialFolderForAllImages = testdata + "SpecialFolderForAllImages";
pdfDocument.save(testout + "PDFNEWJAVA_34088.html", saveOptions);
```

**PDFNEWJAVA-33203** - Установка DPI/PPI изображений в PDF

Следующий фрагмент кода показывает, как изменить разрешение изображения в pdf файле:

```java
String myDir = "D:\\Temp\\";
File fileIn = new File(myDir+"image.jpg");
FileInputStream in = new FileInputStream(fileIn)

File fileOut = new File(myDir+"image.pdf");
FileOutputStream out = new FileOutputStream(fileOut);
//тестовое создание pdf
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
//внутреннее изменение разрешения изображения
doc = new Document(myDir+"image.pdf");
XImageCollection images = doc.getPages().get_Item(1).getResources().getImages();
ByteArrayOutputStream baos = new ByteArrayOutputStream();
images.get_Item(1).save(baos, 10, 10);//определить горизонтальное и вертикальное разрешения
images.get_Item(1).replace(new ByteArrayInputStream(baos.toByteArray()));
doc.save(myDir+"imageWithNewResolution.pdf");
```

**Резюме:**

**Добавленные классы:**

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

## Изменения в классах:

**com.aspose.pdf.facades.Form**

Изменения:

- public java.util.Map getButtonOptionValues(String fieldName) -> public java.util.Hashtable<String,String> getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfConverter**
Добавлено:

- public int getCoordinateType()
- public void setCoordinateType(int value)
  Устарело:
- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileInfo**
Изменения:

- public java.util.Map getHeader() -> public java.util.Map<String, String> getHeader()
- public void setHeader(java.util.Map value) -> public void setHeader(java.util.Map<String,String> value


**com.aspose.pdf.facades.PdfFileSignature**

Устарело:

- public boolean isContainSignature()
- public boolean isCoversWholeDocument(String signName)
  Добавлено:
- public boolean containsSignature()
- public boolean containsUsageRights()
- public void removeUsageRights()

**com.aspose.pdf.facades.PdfPageEditor**
Изменения:

- public int[] getPages_Rename_Namesake() -> public int[] getProcessPages()
- public void setPages(int[] value) -> public void setProcessPages(int[] value)
- public java.util.Map getPageRotations() -> public java.util.Map<Integer, Integer> getPageRotations()
- public void setPageRotations(java.util.Map value) -> public void setPageRotations(java.util.Map<Integer, Integer> value)

**com.aspose.pdf.facades.PdfViewer**
Устарело:

- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)
  Добавлено:
- public int getCoordinateType()
- public void setCoordinateType(int value)

**com.aspose.pdf.facades.PdfXmpMetadata**
Изменения:

- public IDictionary getExtensionFields() -> public java.util.Hashtable<String, XmpPdfAExtensionSchema> getExtensionFields()

**com.aspose.pdf.generator.legacyxmlmodel.Attachment**  
Добавлено:

- public InputStream AttachedStream

**com.aspose.pdf.generator.legacyxmlmodel.BorderInfo**  
Добавлено:

- public void setBorderStyle(int borderSide, int style)

**com.aspose.pdf.generator.legacyxmlmodel.BoxVerticalAlignmentType**

- Удален статус Deprecated из класса

**com.aspose.pdf.generator.legacyxmlmodel.Cell**  
Добавлено:

- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo value)
- public String getText()

**com.aspose.pdf.generator.legacyxmlmodel.HeaderFooter**  
Добавлено:

- public Object completeClone()
- public Object completeCloneAll()

**com.aspose.pdf.generator.legacyxmlmodel.Heading**  
Удален статус Deprecated из:

- public int getBulletAlignment()
- public void setBulletAlignment(int value)

**com.aspose.pdf.generator.legacyxmlmodel.Image**  
Добавлено:

- public Image(HeaderFooter hf)

**com.aspose.pdf.generator.legacyxmlmodel.JavaScripts**  
Добавлено:

- public void remove(Cell jsToRemove)

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**
Добавлено:

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

Добавлено Устаревшее:

- public int getBookMarkLevel()
- public void setBookMarkLevel(int value)
- public int getDirectModeItemType()
- public void setDirectModeItemType(int value)
- public int getDirectModeItemsCount()
- public void setDirectModeItemsCount(int value)

**com.aspose.pdf.generator.legacyxmlmodel.LinkAction**
Добавлено:

- public String SoundFileName

**com.aspose.pdf.generator.legacyxmlmodel.Paragraphs**
Добавлено:

- public void add(Paragraph paragraph)
- void addHeading(Paragraph параграф)
- public int indexOf(Paragraph параграф)
- public void copyTo(Paragraph[] paraArray, int индекс)
- public void insert(Paragraph paragraphToInsertAfter, Paragraph новыйПараграф)

**com.aspose.pdf.generator.legacyxmlmodel.Row**  
Изменено:

- DefaultCellTextInfo в поле с геттерами и сеттерами  
  Добавлено:
- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo значение)
- public Object deepClone()

**com.aspose.pdf.generator.legacyxmlmodel.Section**  
Добавлено:

- public ColumnInfo ColumnInfo
- public int getPageCount()
- public void setPageCount(int значение)
- public String BreakParaText
- public Object deepClone()
- public Object completeClone()
- public HeaderFooter insertHeader(int тип)
- public HeaderFooter insertFooter(int тип)
- public Object getObjectByID(String ID)

**com.aspose.pdf.generator.legacyxmlmodel.Sections**  
Добавлено:

- public Sections()
- public Section add()
- public void insert(int индекс, Section раздел)

- public void insert(Section sectionToInsertAfter, Section новыйРаздел)
- public void remove(Section sectionToRemove)  
- public void copyTo(Section[] secArray, int index)  
- public int indexOf(Section section)  
- public void set_Item(int index, Section value)  
- public Section get_Item(String sectionID)  
- public void set_Item(String sectionID, Section value)  

**com.aspose.pdf.generator.legacyxmlmodel.Security**  
Добавлено:

- public boolean isDefaultAllAllowed()  
- public void setDefaultAllAllowed(boolean value)  

**com.aspose.pdf.generator.legacyxmlmodel.Shapes**  
Добавлено:

- public void add(Shape shape)  
- public void remove(Shape shapeToRemove)  
- public void copyTo(Shape[] shapeArray, int index)  
- public int indexOf(Shape shape)  

**com.aspose.pdf.generator.legacyxmlmodel.Table**  
Изменено:

- FixedWidth в поле с методами чтения и записи  
- DefaultCellTextInfo в поле с методами чтения и записи  
  Добавлено:
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
Добавлено:

- public int getCapacity()
- public void setCapacity(int value)

**com.aspose.pdf.generator.legacyxmlmodel.TextInfo**  
Изменено:

- Следующий список полей был изменен на отдельные геттеры и сеттеры для каждого поля:

```java

 FontSize, FontName, TruetypeFontFileName, IsUnicode, FontAfmFile, FontPfmFile, FontOutlineFile, FontEncodingFile,
 IsTrueTypeFontBold, IsTrueTypeFontItalic,{color} {color:#222222}FontEncoding, IsFontEmbedded, IsUnderline,{color}
 {color:#222222}IsOverline,{color} {color:#222222}CharSpace, WordSpace, LineSpacing, OverlineOffset, UnderlineOffset, RenderingMode,
 Color, BackgroundColor, IsRightToLeft, StrokeWidth, StrokeColor, IsBaseline, Alignment.

```


Добавлено:

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
- public boolean isOverline() // проверяет, есть ли надчеркивание
- public void setOverline(boolean value) // устанавливает, будет ли надчеркивание
- public float getCharSpace() // получает межсимвольный интервал
- public void setCharSpace(float value) // устанавливает межсимвольный интервал
- public float getWordSpace() // получает интервал между словами
- public void setWordSpace(float value) // устанавливает интервал между словами
- public float getLineSpacing() // получает межстрочный интервал
- public void setLineSpacing(float value) // устанавливает межстрочный интервал
- public float getOverlineOffset() // получает смещение надчеркивания
- public void setOverlineOffset(float value) // устанавливает смещение надчеркивания
- public float getUnderlineOffset() // получает смещение подчеркивания
- public void setUnderlineOffset(float value) // устанавливает смещение подчеркивания
- public int getRenderingMode() // получает режим рендеринга
- public void setRenderingMode(int value) // устанавливает режим рендеринга
- public Color getColor() // получает цвет
- public void setColor(Color value) // устанавливает цвет
- public Color getBackgroundColor() // получает цвет фона
- public void setBackgroundColor(Color value) // устанавливает цвет фона
- public boolean isRightToLeft() // проверяет, используется ли направление текста справа налево
- public void setRightToLeft(boolean value) // устанавливает направление текста справа налево
- public float getStrokeWidth() // получает ширину обводки
- public void setStrokeWidth(float value) // устанавливает ширину обводки
- public Color getStrokeColor() // получает цвет обводки
- public void setStrokeColor(Color value) // устанавливает цвет обводки
- public boolean isBaseline() // проверяет, используется ли базовая линия
- public void setBaseline(boolean value) // устанавливает использование базовой линии
- public int getAlignment() // получает выравнивание

- public void setAlignment(int value) // устанавливает выравнивание

**com.aspose.pdf.BaseOperatorCollection** Изменения:

- implements ICollection -> implements ICollection< Operator >

**com.aspose.pdf.Border** Изменения:

- public int getVCornerRaduis() -> public int getVCornerRadius()
- public void setVCornerRaduis(int value) -> public void setVCornerRadius(int value) Добавлено Устаревшее:
- public int getVCornerRaduis()
- public void setVCornerRaduis(int value)

**com.aspose.pdf.DataUtils** Изменения:

- Внутренний

**com.aspose.pdf.ExcelSaveOptions** Добавлено:

- public boolean getMinimizeTheNumberOfWorksheets()
- public void setMinimizeTheNumberOfWorksheets(boolean value)
- public boolean getInsertBlankColumnAtFirst()
- public void setInsertBlankColumnAtFirst(boolean value)
- public boolean getUniformWorksheets()
- public void setUniformWorksheets(boolean value)

**com.aspose.pdf.Font** Добавлено:

- public void save(OutputStream stream)

**com.aspose.pdf.Form** Добавлено:

- public FieldsEnumerator(IDocument document, List< Object > fields)

**com.aspose.pdf.HtmlSaveOptions:** Добавлено:


- public FontSourceCollection getFontSources()

**com.aspose.pdf.InkAnnotation**  
Добавлено:

- public int getCapStyle()  
- public void setCapStyle(int value)  

**com.aspose.pdf.LineAnnotation**  
Добавлено:

- public Measure getMeasure()  
- public void setMeasure(Measure value)  

**com.aspose.pdf.LoadFormat:**  
Изменения:

- public static final int InfoPath - был удален  
- public static final int AutoDetect - добавлено  

**com.aspose.pdf.Metadata**  
Изменения:

- public IDictionary getExtensionFields() -> public java.util.Hashtable< String, XmpPdfAExtensionSchema > getExtensionFields()  

**com.aspose.pdf.PageLayout**  
Добавлено:

- public static final int Default  

**com.aspose.pdf.PolylineAnnotation**  
Добавлено:

- public Measure getMeasure()  
- public void setMeasure(Measure value)  

**com.aspose.pdf.PopupAnnotation**  
Добавлено:

- public MarkupAnnotation getParent()  
- public void setParent(MarkupAnnotation value)  

**com.aspose.pdf.RichTextBoxField**  
Изменения:

- public String getRValue() -> public String getRichTextValue()  

- public void setRValue(String value) -> public void setRichTextValue(String value)  

**com.aspose.pdf.SaveOptions.BorderPartStyle**  
Добавлено:

- public java.awt.Color color

**com.aspose.pdf.SvgLoadOptions**  
Добавлено:

- public static final class ConversionEngines
- public int ConversionEngine
- public PageInfo getPageInfo()
- public void setPageInfo(PageInfo value)

**com.aspose.pdf.Table**  
Добавлено:

- public int getColumnAdjustment()
- public void setColumnAdjustment(int value)

**com.aspose.pdf.TextFragmentAbsorber**  
Добавлено:

- public TextReplaceOptions getTextReplaceOptions()
- public void setTextReplaceOptions(TextReplaceOptions value)

**com.aspose.pdf.TextReplaceOptions**  
Добавлено:

- public static final class ReplaceAdjustment
- public int getReplaceAdjustmentAction()
- public void setReplaceAdjustmentAction(int value)
- public TextReplaceOptions(int adjustment, int scope)

**com.aspose.pdf.XFA**  
Добавлено:

- public void setFieldImage(String fieldName, InputStream image)