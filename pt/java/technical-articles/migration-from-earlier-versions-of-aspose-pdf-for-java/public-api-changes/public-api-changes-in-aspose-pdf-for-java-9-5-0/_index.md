---
title: Mudanças na API Pública no Aspose.PDF para Java 9.5.0
type: docs
weight: 70
url: /pt/java/public-api-changes-in-aspose-pdf-for-java-9-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página lista as mudanças na API pública introduzidas no [Aspose.PDF para Java 9.5.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry576058.aspx). Inclui não apenas novos métodos públicos e obsoletos, mas também uma descrição de quaisquer mudanças no comportamento por trás das cenas no Aspose.PDF para Java que podem afetar o código existente. Qualquer comportamento introduzido que possa ser visto como uma regressão e modificar o comportamento existente é especialmente importante e está documentado aqui.

{{% /alert %}}

**Propriedade CoordinateType foi adicionada ao PdfViewer e PdfConverter**<p>
A propriedade CoordinateType permite definir a área imprimível para MediaBox ou CropBox (valor padrão)

**Método SetFieldImage foi adicionado à classe XFA:** 

public void SetFieldImage(string fieldName, Stream image)

Exemplo:

O código a seguir mostra como definir uma imagem para o campo de formulário XFA:

```java

Document doc = new Document("doc.pdf");
InputStream fs = new FileInputStream("image.jpg");
doc.getForm().getXFA().setFieldImage("form1\[0\].ImageField1\[0\]", fs);
doc.save("37017-1.pdf");
```

A enumeração **ReplaceAdjustment** foi adicionada à classe **TextReplaceOptions**

Este enum fornece os seguintes valores:

- **None** - Nenhuma ação, o comprimento da linha pode ser alterado
- **AdjustSpaceWidth** - Tente ajustar os espaços entre as palavras para manter o comprimento da linha

A propriedade **ReplaceAdjustmentAction** foi adicionada à classe **TextReplaceOptions**

A classe **TextReplaceOptions** tem um novo construtor que permite definir o parâmetro **ReplaceAdjustment**:

TextReplaceOptions(int adjustment, int scope)

A propriedade **TextReplaceOptions** foi adicionada à classe **TextFragmentAbsorber**

A classe **Ellipse** foi implementada:

Construtor:

public Ellipse(float left, float bottom, float width, float height)

Propriedades:

- Left - valor float que indica a posição esquerda da elipse.

- Bottom - valor float que indica a posição inferior da elipse.

- Width - valor float que indica a largura da elipse.
- Height - valor float que indica a altura da elipse.

Exemplo:
O seguinte trecho de código mostra como adicionar Elipse:

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

A classe **Path** foi implementada

Construtores:

public Path()
public Path(Shape[] shapes)

Propriedade:

- Shapes - coleção de formas

Exemplo:
o seguinte trecho de código mostra como adicionar Path:

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


**Classe HtmlFragment** foi adicionada ao pacote com.aspose.pdf*

Construtor:

- public HtmlFragment(string text)

Parâmetro:

- Texto - Texto HTML
  Propriedade:
- Texto - Texto HTML

Exemplo:
O trecho de código a seguir mostra como adicionar um fragmento HTML:

```java
Document doc = new Document();
Page page = doc.getPages().add();
HtmlFragment titulo = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
titulo.setKeptWithNext (true);
titulo.getMargin().setBottom (10);
titulo.getMargin().setTop (200);
page.getParagraphs().add(titulo);
doc.Save(outFile);
```

O método **ContainsUsageRights()** foi adicionado à classe **PdfFileSignature**

O método **RemoveUsageRights()** foi adicionado à classe **PdfFileSignature**

Exemplo:

O código a seguir mostra como remover a funcionalidade de direitos de uso do documento:

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


**isContainSignature()** método foi renomeado para **ContainsSignature(...)**

- O nome do método anterior não foi removido, mas marcado como obsoleto para ser removido no futuro.
    **isCoversWholeDocument()** método foi renomeado para **CoversWholeDocument(...)**
- O nome do método anterior não foi removido, mas marcado como obsoleto para ser removido no futuro.

A classe **Measure** foi adicionada ao pacote **com.aspose.pdf**

A classe descreve o sistema de coordenadas Measure. Membros da classe Measure:

Construtor:

- public Measure(Annotation annotation)

Propriedades get/set:

- ScaleRatio - Uma string de texto expressando a razão de escala do desenho.
- XFormat - Um array de formato numérico para medição de mudança ao longo do eixo x e, se Y não estiver presente, ao longo do eixo y também.
- YFormat - Um array de formato numérico para medição de mudança ao longo do eixo y.
- DistanceFormat - Um array de formato numérico para medição de distância em qualquer direção.
- AreaFormat - Um array de formato numérico para medição de área.

- AngleFormat - Um array de formato numérico para medição de ângulos.
- SlopeFormat - Um array de formato numérico para medição da inclinação de uma linha.
- Origin - Ponto que deve especificar a origem do sistema de coordenadas de medição em coordenadas padrão do espaço do usuário.
- XYFactor - Um fator que deve ser usado para converter as maiores unidades ao longo do eixo y nas maiores unidades ao longo do eixo x.

A classe **NumberFormat** foi adicionada à classe **Measure**

A classe representa o formato numérico para medição.

Construtor:

- public NumberFormat(Measure measure)

get/set Propriedades:

- UnitLabel - Uma string de texto especificando um rótulo para exibir as unidades.
- ConvresionFactor - O fator de conversão usado para multiplicar um valor em unidades parciais do elemento do array de formato numérico anterior para obter um valor nas unidades deste formato numérico.
- FractionDisplayment - De que maneira os valores fracionários são exibidos.
- Precision - Se FractionDisplayment for ShowAsDecimal, este valor é a precisão do valor fracionário; Deve ser múltiplo de 10. O padrão é 100.
- Denominator - Se FractionDisplayment for ShowAsFraction, este valor é o denominador da fração.
 Valor padrão é 16.
- ForceDenominator - Se FractionDisplayment for ShowAsFraction, este valor determina se a fração pode ou não ser reduzida. Se o valor for verdadeiro, a fração não pode ser reduzida.
- ThousandsSeparator - Texto que será usado entre ordens de milhares na exibição de valores numéricos. Uma string vazia indica que nenhum texto será adicionado. O padrão é vírgula.
- FractionSeparator - Texto que será usado como a posição decimal na exibição de valores numéricos. Uma string vazia indica que o padrão será usado. O padrão é o caractere de ponto.
- BeforeText - Texto que será concatenado à esquerda do rótulo.
- AfterText - Texto que será concatenado após o rótulo.

A enumeração **FractionStyle** foi adicionada à classe **NumberFormat**

Valores de FractionStyle:

- ShowAsDecimal - Mostrar valores fracionários como fração decimal.
- ShowAsFraction - Mostrar valor fracionário como fração.
- Round - Arredondar valores fracionários para o inteiro mais próximo.
- Truncate - Truncar para obter unidades inteiras.

A classe **NumberFormatList** foi adicionada à classe **Measure**
A classe representa Representa uma lista de formatos numéricos.

Construtor:

- public NumberFormatList(Measure measure)

Propriedades:

- get_Item(int) e set_Item(int index, NumberFormat value) - Obtém ou define o formato numérico na lista pelo seu índice.
- getCount()- Conta o número de itens na lista.

Métodos:

- public void add(NumberFormat value)
- Adiciona formato numérico à lista.
- public void insert(int index, NumberFormat value)
- Insere formato numérico na lista.
- public void removeAt(int index)
- Remove formato numérico da lista.

A propriedade **Measure** foi adicionada às classes **LineAnnotation** e **PolyLineAnnotation**.

Exemplos:

O exemplo a seguir demonstra como usar Measure com LineAnnotation:

```java
Document doc = new Document("source.pdf");
Rectangle rect = new Rectangle(260, 630, 451, 662);
LineAnnotation line = new LineAnnotation(doc.getPages().get_Item(1), rect, new Point(266, 657), new Point(446, 656));
line.setColor(Color.getRed());
//definir parâmetros de linha de extensão.
line.setLeaderLine(-15);
line.setLeaderLineExtension(5);
//definir terminações de linha
line.setStartingStyle(LineEnding.OpenArrow);
line.setEndingStyle(LineEnding.OpenArrow);

//criar elemento Measure
line.setMeasure(new Measure(line));<p>
line.getMeasure().setDistanceFormat(newMeasure.NumberFormatList(line.getMeasure()));
line.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(line.getMeasure()));
line.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
line.getMeasure().getDistanceFormat().get_Item(1).setFractionSeparator(".");
line.getMeasure().getDistanceFormat().get_Item(1).setConvresionFactor(1);

//texto da linha de medida
line.setContents("155 mm");
//isso deve ser configurado para mostrar o texto.
line.setShowCaption(true);
line.setCaptionPosition(CaptionPosition.Top);
doc.getPages().get_Item(1).getAnnotations().add(line);
doc.save("output.pdf");
```


Exemplo a seguir demonstra como usar Measure com PolylineAnnotation:

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
//área ou linha de perímetro
PolylineAnnotation area = new PolylineAnnotation(doc.getPages().get_Item(1), rect, vertices);
area.setColor(Color.getRed());
//estilos de linha podem ser definidos para linha de perímetro.
area.setStartingStyle(LineEnding.OpenArrow);
area.setEndingStyle(LineEnding.OpenArrow);
area.setMeasure(new Measure(area));
area.getMeasure().setDistanceFormat(new Measure.NumberFormatList(area.getMeasure()));
area.getMeasure().getDistanceFormat().add(new Measure.NumberFormat(area.getMeasure()));
area.getMeasure().getDistanceFormat().get_Item(1).setUnitLabel("mm");
doc.getPages().get_Item(1).getAnnotations().add(area);
doc.save("output.pdf");
```

O trecho de código a seguir demonstra como ler propriedades de Measure:

```java
//ler propriedades de Medida

Document doc = new Document("measure.pdf");

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getScaleRatio());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getUnitLabel());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getConvresionFactor());

System.out.println(((LineAnnotation)doc.getPages().get_Item(1).getAnnotations().get_Item(1)).getMeasure().getAreaFormat().get_Item(1).getFractionSeparator());
```

**Alteração importante** - A propriedade PdfPageEditor.Pages foi renomeada para **ProcessPages**

O trecho de código a seguir mostra o uso da propriedade (define o coeficiente de zoom para a página #1 do documento):

```java
PdfPageEditor editor = new PdfPageEditor();
editor.bindPdf("input.pdf");
editor.setZoom(0.5f);
editor.setProcessPages(new int[] { 1 });
editor.save("output.pdf");
```


**Mudança de interrupção** - A propriedade RichTextBoxField.RValue foi renomeada para **RichTextValue**

O trecho de código a seguir mostra um exemplo onde o campo renomeado foi usado:

```java
Document doc = new Document("input.pdf");

RichTextBoxField rt = new RichTextBoxField(doc.getPages().get_Item(1), new Rectangle(50, 600, 250, 650));
rt.setPartialName("rt");
doc.getForm().add(rt);
doc.save("34834.pdf");
Document doc1 = new Document("34834.pdf");
((RichTextBoxField)doc1.getForm().get("rt")).setRichTextValue("<p>Este é o meu <b>parágrafo</b></p>");

doc1.save("output.pdf");
```

A opção **InsertBlankColumnAtFirst** foi adicionada à classe **ExcelSaveOptions**

O trecho de código a seguir mostra como suprimir o aparecimento da primeira coluna em branco:

```java
Document doc = new Document(inFile);

ExcelSaveOptions options = new ExcelSaveOptions();

options.setInsertBlankColumnAtFirst(false);

doc.save(outFile, options);
```

A propriedade **PageInfo** foi adicionada à classe **SvgLoadOptions**.

O trecho de código a seguir mostra como usar SvgLoadOptions e definir informações de margem com a propriedade PageInfo:

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

A enumeração **ConversionEngines** foi adicionada à classe **SvgLoadOptions**.

Os seguintes valores são definidos:

- **LegacyEngine** - motor legado de processamento de Svg
- **NewEngine** - novo motor de processamento de Svg

A propriedade **ConversionEngine** foi adicionada à classe **SvgLoadOptions**

O LegacyEngine ainda é o valor padrão porque o NewEngine está em estágios de teste B.
O trecho de código a seguir mostra um exemplo de como usar o novo motor:

```java
SvgLoadOptions options = new SvgLoadOptions();

options.ConversionEngine = SvgLoadOptions.ConversionEngines.NewEngine;
String inFile = "36516_2_income.svg";
String outFile = "36516_2_income.pdf";
Document pdfDocument = new Document(inFile, options);
pdfDocument.save(outFile);
```


**Propriedade ColumnAdjustment** foi adicionada à classe **Table**

Enumeração ColumnAdjustment foi adicionada ao pacote com.aspose.pdf

os seguintes valores foram adicionados:

- **Customized** - O usuário define a largura da coluna manualmente.
- **AutoFitToContent** - Realiza ajuste automático ao conteúdo

**Propriedade ColumnAdjustment** foi adicionada à classe **Table**

O valor padrão é Customized.

O snippet de código a seguir mostra um exemplo de uso da propriedade ColumnAdjustment:

```java
Table hTable = new Table();
hTable.getMargin().setTop(4);
hTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5F, Color.getBlack()));
hTable.setDefaultCellPadding(new MarginInfo(1, 1, 1, 1));
hTable.setAlignment(HorizontalAlignment.Left);
hTable.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
```

**Propriedade MinimizeTheNumberOfWorksheets** foi introduzida no objeto **ExcelSaveOptions**.

O snippet de código a seguir mostra como minimizar o número possível de planilhas:

```java
Document doc = new Document("Original.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
//Defina esta propriedade como true
options.setMinimizeTheNumberOfWorksheets(true);
doc.save("output.xls", options);
```


**Valor Padrão** foi adicionado à enumeração **PageLayout**.

O seguinte trecho de código define PageLayout para o valor Padrão:

```java
Document doc1 = new Document("input.pdf");
doc1.setPageLayout (PageLayout.Default);
doc1.save("output.pdf");
```

Suporte para **Extremidades Arredondadas** foi implementado para **InkAnnotation**

A enumeração **CapStyle** foi adicionada ao pacote **com.aspose.pdf**
Os seguintes valores estão presentes

- **Rectangular** - Valor padrão especificado
- **Rounded** - cantos arredondados
- Propriedade **CapStyle** foi adicionada à classe **InkAnnotation**

O seguinte trecho de código mostra como definir os cantos do InkAnnotation como arredondados:

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


**PDFNEWJAVA-33498** - Fornecer suporte para adicionar Imagem de BufferedImage em documento PDF

O seguinte trecho de código mostra como adicionar Imagem de BufferedImage:

```java
BufferedImage originalImage = ImageIO.read(new File("c:\\image\\anyImage.jpg"));
Document pdfDocument1 = new Document();
Page page2 = pdfDocument1.getPages().add();
page2.getResources().getImages().add(originalImage)
```

**PDFNEWJAVA-34088** - Conversão de PDF para HTML: Especificar pasta de imagens

O seguinte trecho de código mostra como especificar a pasta de imagens:

```java
Document pdfDocument = new Document(testdata + "PDFNEWJAVA_34088.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.SpecialFolderForAllImages = testdata + "SpecialFolderForAllImages";
pdfDocument.save(testout + "PDFNEWJAVA_34088.html", saveOptions);
```

**PDFNEWJAVA-33203** - Configurando DPI/PPI de imagens em PDF

O seguinte trecho de código mostra como alterar a resolução da imagem no arquivo pdf:

```java
String myDir = "D:\\Temp\\";
File fileIn = new File(myDir+"image.jpg");
FileInputStream in = new FileInputStream(fileIn)

File fileOut = new File(myDir+"image.pdf");
FileOutputStream out = new FileOutputStream(fileOut);
//teste de criação de pdf
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
//alteração interna da resolução da imagem
doc = new Document(myDir+"image.pdf");
XImageCollection images = doc.getPages().get_Item(1).getResources().getImages();
ByteArrayOutputStream baos = new ByteArrayOutputStream();
images.get_Item(1).save(baos, 10, 10);//definir resoluções horizontal e vertical
images.get_Item(1).replace(new ByteArrayInputStream(baos.toByteArray()));
doc.save(myDir+"imageWithNewResolution.pdf");
```

**Resumo:**

**Classes adicionadas:**

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

## Alterações nas classes:

**com.aspose.pdf.facades.Form**

Alterações:

- public java.util.Map getButtonOptionValues(String fieldName) -> public java.util.Hashtable<String,String> getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfConverter**  
Adicionado:

- public int getCoordinateType()
- public void setCoordinateType(int value)  
  Obsoleto:
- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)

**com.aspose.pdf.facades.PdfFileInfo**  
Alterações:

- public java.util.Map getHeader() -> public java.util.Map<String, String> getHeader()
- public void setHeader(java.util.Map value) -> public void setHeader(java.util.Map<String,String> value

**com.aspose.pdf.facades.PdfFileSignature**
Depricado:

- public boolean isContainSignature()
- public boolean isCoversWholeDocument(String signName)
  Adicionado:
- public boolean containsSignature()
- public boolean containsUsageRights()
- public void removeUsageRights()

**com.aspose.pdf.facades.PdfPageEditor**
Alterações:

- public int[] getPages_Rename_Namesake() -> public int[] getProcessPages()
- public void setPages(int[] value) -> public void setProcessPages(int[] value)
- public java.util.Map getPageRotations() -> public java.util.Map<Integer, Integer> getPageRotations()
- public void setPageRotations(java.util.Map value) -> public void setPageRotations(java.util.Map<Integer, Integer> value)

**com.aspose.pdf.facades.PdfViewer**
Depricado:

- public boolean getShowHiddenAreas()
- public void setShowHiddenAreas(boolean value)
  Adicionado:
- public int getCoordinateType()
- public void setCoordinateType(int value)

**com.aspose.pdf.facades.PdfXmpMetadata**
Alterações:

- public IDictionary getExtensionFields() -> public java.util.Hashtable<String, XmpPdfAExtensionSchema> getExtensionFields()

**com.aspose.pdf.generator.legacyxmlmodel.Attachment**  
Adicionado:

- public InputStream AttachedStream

**com.aspose.pdf.generator.legacyxmlmodel.BorderInfo**  
Adicionado:

- public void setBorderStyle(int borderSide, int style)

**com.aspose.pdf.generator.legacyxmlmodel.BoxVerticalAlignmentType**

- Removido status de Depreciado da classe

**com.aspose.pdf.generator.legacyxmlmodel.Cell**  
Adicionado:

- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo value)
- public String getText()

**com.aspose.pdf.generator.legacyxmlmodel.HeaderFooter**  
Adicionado:

- public Object completeClone()
- public Object completeCloneAll()

**com.aspose.pdf.generator.legacyxmlmodel.Heading**  
Removido status de Depreciado de:

- public int getBulletAlignment()
- public void setBulletAlignment(int value)

**com.aspose.pdf.generator.legacyxmlmodel.Image**  
Adicionado:

- public Image(HeaderFooter hf)

**com.aspose.pdf.generator.legacyxmlmodel.JavaScripts**  
Adicionado:

- public void remove(Cell jsToRemove)  

**com.aspose.pdf.generator.legacyxmlmodel.LegacyPdf**
Adicionado:

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

Adicionado Obsoleto:

- public int getBookMarkLevel()
- public void setBookMarkLevel(int value)
- public int getDirectModeItemType()
- public void setDirectModeItemType(int value)
- public int getDirectModeItemsCount()
- public void setDirectModeItemsCount(int value)

**com.aspose.pdf.generator.legacyxmlmodel.LinkAction**  
Adicionado:

- public String SoundFileName

**com.aspose.pdf.generator.legacyxmlmodel.Paragraphs**  
Adicionado:

- public void add(Paragraph paragraph)
- void adicionarTítulo(Parágrafo parágrafo)
- public int índiceDe(Parágrafo parágrafo)
- public void copiarPara(Parágrafo[] arrayDeParágrafos, int índice)
- public void inserir(Parágrafo parágrafoParaInserirApós, Parágrafo novoParágrafo)

**com.aspose.pdf.generator.legacyxmlmodel.Row**  
Alterado:

- DefaultCellTextInfo em campo getter e setter  
  Adicionado:
- public TextInfo obterDefaultCellTextInfo()
- public void definirDefaultCellTextInfo(TextInfo valor)
- public Object cloneProfundo()

**com.aspose.pdf.generator.legacyxmlmodel.Section**  
Adicionado:

- public ColumnInfo InformaçõesDaColuna
- public int obterContagemDePáginas()
- public void definirContagemDePáginas(int valor)
- public String TextoQuebraParágrafo
- public Object cloneProfundo()
- public Object cloneCompleto()
- public HeaderFooter inserirCabeçalho(int tipo)
- public HeaderFooter inserirRodapé(int tipo)
- public Object obterObjetoPorID(String ID)

**com.aspose.pdf.generator.legacyxmlmodel.Sections**  
Adicionado:

- public Sections()
- public Section adicionar()
- public void inserir(int índice, Section seção)

- public void inserir(Section seçãoParaInserirApós, Section novaSeção)
- public void remove(Section seçãoARemover)
- public void copyTo(Section[] secArray, int índice)
- public int indexOf(Section seção)
- public void set_Item(int índice, Section valor)
- public Section get_Item(String seçãoID)
- public void set_Item(String seçãoID, Section valor)

**com.aspose.pdf.generator.legacyxmlmodel.Security**  
Adicionado:

- public boolean isDefaultAllAllowed()
- public void setDefaultAllAllowed(boolean valor)

**com.aspose.pdf.generator.legacyxmlmodel.Shapes**  
Adicionado:

- public void add(Shape forma)
- public void remove(Shape formaARemover)
- public void copyTo(Shape[] arrayDeFormas, int índice)
- public int indexOf(Shape forma)

**com.aspose.pdf.generator.legacyxmlmodel.Table**  
Alterado:

- FixedWidth em campo getter e setter
- DefaultCellTextInfo em campo getter e setter  
  Adicionado:
- public float getFixedWidth()
- public void setFixedWidth(float valor)
- public TextInfo getDefaultCellTextInfo()
- public void setDefaultCellTextInfo(TextInfo valor)

- public Cell getCell(int linha, int coluna, boolean isTableChanged)
- public void formatColumnsWithFormatInfo(TableFormatInfo info, int firstColumn, int maxColumns)
- public void formatTableWithFormatInfo(TableFormatInfo info, int firstColumn, int firstRow, int maxRows, int maxColumns)
- public void formatRowsWithFormatInfo(TableFormatInfo info, int firstRow, int maxRows)
- public void setColumnWidth(int columnNumber, float width)
- public String getColumnWidths()
- public void setColumnWidths(String value)

**com.aspose.pdf.generator.legacyxmlmodel.TabStops**  
Adicionado:

- public int getCapacity()
- public void setCapacity(int value)

**com.aspose.pdf.generator.legacyxmlmodel.TextInfo**  
Alterado:

- A próxima lista de campos foi alterada para o campo getter e setter separado:

```java

 FontSize, FontName, TruetypeFontFileName, IsUnicode, FontAfmFile, FontPfmFile, FontOutlineFile, FontEncodingFile,
 IsTrueTypeFontBold, IsTrueTypeFontItalic,{color} {color:#222222}FontEncoding, IsFontEmbedded, IsUnderline,{color}
 {color:#222222}IsOverline,{color} {color:#222222}CharSpace, WordSpace, LineSpacing, OverlineOffset, UnderlineOffset, RenderingMode,
 Color, BackgroundColor, IsRightToLeft, StrokeWidth, StrokeColor, IsBaseline, Alignment.

```


Adicionado:

- public float getFontSize() // Obtém o tamanho da fonte
- public void setFontSize(float value) // Define o tamanho da fonte
- public String getFontName() // Obtém o nome da fonte
- public void setFontName(String value) // Define o nome da fonte
- public String getTruetypeFontFileName() // Obtém o nome do arquivo da fonte TrueType
- public void setTruetypeFontFileName(String value) // Define o nome do arquivo da fonte TrueType
- public boolean isUnicode() // Verifica se é Unicode
- public void setUnicode(boolean value) // Define se é Unicode
- public String getFontAfmFile() // Obtém o arquivo AFM da fonte
- public void setFontAfmFile(String value) // Define o arquivo AFM da fonte
- public String getFontPfmFile() // Obtém o arquivo PFM da fonte
- public void setFontPfmFile(String value) // Define o arquivo PFM da fonte
- public String getFontOutlineFile() // Obtém o arquivo de contorno da fonte
- public void setFontOutlineFile(String value) // Define o arquivo de contorno da fonte
- public String getFontEncodingFile() // Obtém o arquivo de codificação da fonte
- public void setFontEncodingFile(String value) // Define o arquivo de codificação da fonte
- public boolean isTrueTypeFontBold() // Verifica se a fonte TrueType é negrito
- public void setTrueTypeFontBold(boolean value) // Define se a fonte TrueType é negrito
- public boolean isTrueTypeFontItalic() // Verifica se a fonte TrueType é itálica
- public void setTrueTypeFontItalic(boolean value) // Define se a fonte TrueType é itálica
- public String getFontEncoding() // Obtém a codificação da fonte
- public void setFontEncoding(String value) // Define a codificação da fonte
- public boolean isFontEmbedded() // Verifica se a fonte está incorporada
- public void setFontEmbedded(boolean value) // Define se a fonte está incorporada
- public boolean isUnderline() // Verifica se está sublinhado

- public void setUnderline(boolean value) // Define se está sublinhado
- public boolean isOverline()  
- public void setOverline(boolean value)  
- public float getCharSpace()  
- public void setCharSpace(float value)  
- public float getWordSpace()  
- public void setWordSpace(float value)  
- public float getLineSpacing()  
- public void setLineSpacing(float value)  
- public float getOverlineOffset()  
- public void setOverlineOffset(float value)  
- public float getUnderlineOffset()  
- public void setUnderlineOffset(float value)  
- public int getRenderingMode()  
- public void setRenderingMode(int value)  
- public Color getColor()  
- public void setColor(Color value)  
- public Color getBackgroundColor()  
- public void setBackgroundColor(Color value)  
- public boolean isRightToLeft()  
- public void setRightToLeft(boolean value)  
- public float getStrokeWidth()  
- public void setStrokeWidth(float value)  
- public Color getStrokeColor()  
- public void setStrokeColor(Color value)  
- public boolean isBaseline()  
- public void setBaseline(boolean value)  
- public int getAlignment()  

- public void setAlignment(int value)  

**com.aspose.pdf.BaseOperatorCollection**  
Alterações:

- implements ICollection -> implements ICollection< Operator >

**com.aspose.pdf.Border**  
Alterações:

- public int getVCornerRaduis() -> public int getVCornerRadius()
- public void setVCornerRaduis(int value) -> public void setVCornerRadius(int value)  
  Adicionado Obsoleto:
- public int getVCornerRaduis()
- public void setVCornerRaduis(int value)

**com.aspose.pdf.DataUtils**  
Alterações:

- Internalizado

**com.aspose.pdf.ExcelSaveOptions**  
Adicionado:

- public boolean getMinimizeTheNumberOfWorksheets()
- public void setMinimizeTheNumberOfWorksheets(boolean value)
- public boolean getInsertBlankColumnAtFirst()
- public void setInsertBlankColumnAtFirst(boolean value)
- public boolean getUniformWorksheets()
- public void setUniformWorksheets(boolean value)

**com.aspose.pdf.Font**  
Adicionado:

- public void save(OutputStream stream)

**com.aspose.pdf.Form**  
Adicionado:

- public FieldsEnumerator(IDocument document, List< Object > fields)

**com.aspose.pdf.HtmlSaveOptions:**  
Adicionado:


- public FontSourceCollection getFontSources()

**com.aspose.pdf.InkAnnotation**  
Adicionado:

- public int getCapStyle()
- public void setCapStyle(int value)

**com.aspose.pdf.LineAnnotation**  
Adicionado:

- public Measure getMeasure()
- public void setMeasure(Measure value)

**com.aspose.pdf.LoadFormat:**  
Alterações:

- public static final int InfoPath - foi removido
- public static final int AutoDetect - Adicionado

**com.aspose.pdf.Metadata**  
Alterações:

- public IDictionary getExtensionFields() -> public java.util.Hashtable< String, XmpPdfAExtensionSchema > getExtensionFields()

**com.aspose.pdf.PageLayout**  
Adicionado:

- public static final int Default

**com.aspose.pdf.PolylineAnnotation**  
Adicionado:

- public Measure getMeasure()
- public void setMeasure(Measure value)

**com.aspose.pdf.PopupAnnotation**  
Adicionado:

- public MarkupAnnotation getParent()
- public void setParent(MarkupAnnotation value)

**com.aspose.pdf.RichTextBoxField**  
Alterações:

- public String getRValue() -> public String getRichTextValue()

- public void setRValue(String value) -> public void setRichTextValue(String value)

**com.aspose.pdf.SaveOptions.BorderPartStyle**  
Adicionado:

- public java.awt.Color color

**com.aspose.pdf.SvgLoadOptions**  
Adicionado:

- public static final class ConversionEngines
- public int ConversionEngine
- public PageInfo getPageInfo()
- public void setPageInfo(PageInfo value)

**com.aspose.pdf.Table**  
Adicionado:

- public int getColumnAdjustment()
- public void setColumnAdjustment(int value)

**com.aspose.pdf.TextFragmentAbsorber**  
Adicionado:

- public TextReplaceOptions getTextReplaceOptions()
- public void setTextReplaceOptions(TextReplaceOptions value)

**com.aspose.pdf.TextReplaceOptions**  
Adicionado:

- public static final class ReplaceAdjustment
- public int getReplaceAdjustmentAction()
- public void setReplaceAdjustmentAction(int value)
- public TextReplaceOptions(int adjustment, int scope)

**com.aspose.pdf.XFA**  
Adicionado:

- public void setFieldImage(String fieldName, InputStream image)