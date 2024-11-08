---
title: 有什么新功能
linktitle: 有什么新功能
type: docs
weight: 10
url: /zh/java/whatsnew/
description: 本页面介绍了Aspose.PDF for Java最近发布版本中引入的最受欢迎的新功能。
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-06-05"
---

## Aspose.PDF 24.8 中的新功能

自24.8以来，支持PDF/A-4格式：

```java

    Document document = new Document(inputPdf);
    // 只有PDF-2.x文档可以转换为PDF/A-4
    document.convert(new ByteArrayOutputStream(), PdfFormat.v_2_0, ConvertErrorAction.Delete);
    boolean converted = document.convert(logFile, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
    document.save(outputFile);
```

此外，可以为图像印章添加替代文本：

在ImageStamp中添加了AlternativeText属性——如果为其赋值，则在向文档添加ImageStamp时具有替代文本。

```java

    String p1_Alt1 = "*** 第1页，替代文本1 ***",
                    p1_Alt2 = "*** 第1页，替代文本2 ***",
                    p2_Alt1 = "--- 第1页，替代文本1 ---",
                    p2_Alt2 = "--- 第1页，替代文本2 ---";

    StructTreeRootElement structTreeRoot = document.getTaggedContent().getStructTreeRootElement();

    ImageStamp imageStamp = new ImageStamp(dataDir + "test.jpg");
    imageStamp.setXIndent(100);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setQuality(100);
    imageStamp.setAlternativeText(p1_Alt1);

    // 到第1页
    document.getPages().get_Item(1).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p1_Alt2);
    document.getPages().get_Item(1).addStamp(imageStamp);

    // 到第2页
    document.getPages().add();
    imageStamp.setXIndent(400);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setAlternativeText(p2_Alt1);
    document.getPages().get_Item(2).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p2_Alt2);
    document.getPages().get_Item(2).addStamp(imageStamp);

    // 保存文档
    document.save(outFile);
```


此外，以下代码显示了如何在 FigureElements 中的现有图像中添加替代文本。

```java

    String inFile = dataDir + "46040.pdf";
    String outFile = dataDir + "46040_1_out.pdf";

    Document document = new Document(inFile);

    ITaggedContent taggedContent = document.getTaggedContent();
    StructureElement rootElement = taggedContent.getRootElement();

    Iterator tmp0 = (rootElement.getChildElements()).iterator();
    while (tmp0.hasNext())
    {
        com.aspose.pdf.tagged.logicalstructure.elements.Element element = (com.aspose.pdf.tagged.logicalstructure.elements.Element)tmp0.next();
        if (element instanceof com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)
                {
            com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figureElement = (com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)element;

            // 设置替代文本
            figureElement.setAlternativeText("图像替代文本（技术1）");
        }
    }

    // 保存文档
    document.save(outFile);
```


## Aspose.PDF 24.7 有什么新功能

自24.7版本以来，作为编辑标记PDF的一部分，已在 **Aspose.Pdf.LogicalStructure.Element** 中添加了方法：

- Tag（向特定操作符如图像、文本和链接添加标签）
- InsertChild
- RemoveChild
- ClearChilds

这些方法允许您编辑PDF文件标签，例如：

```java

    Document document = new Document(dataDir + "test.pdf");

    // 检索文档的第一页。
    Page page = document.getPages().get_Item(1);

    // 初始化变量以保存用于不同目的的BDC（开始字典上下文）元素。
    BDC imageBdc = null;
    BDC pBdc = null;
    BDC link1Bdc = null;
    BDC link2Bdc = null;
    BDC helloBdc = null;

    // 迭代页面内容。
    for (int i = 1; i <= page.getContents().size(); i++)
    {
        // 从页面内容中获取当前操作符。
        Operator op = page.getContents().get_Item(i);

        // 检查操作符是否是BDC的实例。
        if (op instanceof BDC) {
        BDC bdc = (BDC)op; // 将操作符转换为BDC类型。
        if (bdc != null)
        {
            // 检查BDC的MCID（标记内容标识符）是否为0。
            if (bdc.getProperties().getMCID()[0] != null && bdc.getProperties().getMCID()[0] == 0)
            {
                helloBdc = bdc; // 存储BDC以备后用。
            }
        }
    }

    // 检查操作符是否是Do（绘制对象）的实例。
    if (op instanceof Do) {
        Do doXobj = (Do)op; // 将操作符转换为Do类型。
        if (doXobj != null)
        {
            // 为图像创建一个新的BDC并将其插入页面内容中。
            imageBdc = new BDC("Figure");
            page.getContents().insert(i - 2, imageBdc); // 在当前操作符之前插入。
            i++; // 增加索引以考虑插入的BDC。
            page.getContents().insert(i + 1, new EMC()); // 插入一个EMC（结束标记内容）。
            i++; // 再次增加索引。
        }
    }

    // 检查操作符是否为TextShowOperator（用于文本显示）的实例。
    if (op instanceof TextShowOperator) {
        TextShowOperator tx = (TextShowOperator)op; // 将操作符转换为TextShowOperator类型。
        if (tx != null)
        {
            // 检查特定文本内容并插入相应的BDC。
            if (tx.getText().contains("efter Ukendt forfatter er licenseret under"))
            {
                pBdc = new BDC("P");
                page.getContents().insert(i - 1, pBdc); // 在当前操作符之前插入。
                i++; // 增加索引。
                page.getContents().insert(i + 1, new EMC()); // 插入一个EMC。
                i++; // 增加索引。
            }
            if (tx.getText().contains("CC"))
            {
                link1Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link1Bdc); // 在当前操作符之前插入。
                i++; // 增加索引。
                page.getContents().insert(i + 1, new EMC()); // 插入一个EMC。
                i++; // 增加索引。
            }
            if (tx.getText().contains("Dette billede"))
            {
                link2Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link2Bdc); // 在当前操作符之前插入。
                i++; // 增加索引。
                page.getContents().insert(i + 1, new EMC()); // 插入一个EMC。
                i++; // 增加索引。
            }
        }
    }
}
 
    // 从文档中检索标记内容。
    ITaggedContent tagged = document.getTaggedContent();

    // 处理标记内容以修改结构属性。
    // 获取标记内容中根元素的第一个子元素。
    com.aspose.pdf.tagged.logicalstructure.elements.Element p = tagged.getRootElement().getChildElements().get_Item(1);
    p.clearChilds(); // 清除现有子元素。

    // 用父结构元素标记helloBdc。
    MCRElement mcr = p.tag(helloBdc);

    // 创建并设置标记元素的结构属性。
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
            .getAttributes().createAttributes(AttributeOwnerStandard.Layout);
    StructureAttribute attr = new StructureAttribute(AttributeKey.SpaceAfter);
    attr.setNumberValue(30.625); // 设置元素后的空白距离。
    attrs.setAttribute(attr); // 将属性应用于结构。

    // 在标记内容中创建一个新的FigureElement。
    com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figure = tagged.createFigureElement();
    tagged.getRootElement().insertChild(figure, 2); // 在第二个位置插入图元素。
    figure.setAlternativeText("A fly."); // 设置图的替代文本。

    // 用图元素标记imageBdc。
    MCRElement mcr = figure.tag(imageBdc);

    // 检索指定MCR（标记内容引用）的父结构元素
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // 为元素后的空间创建一个新的StructureAttribute
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(3.625); // 将元素后的空间设置为3.625单位
    attrs.setAttribute(spaceAfter); // 将空间后的属性分配给结构属性

    // 为边界框（BBox）创建一个新的StructureAttribute
    StructureAttribute bbox = new StructureAttribute(AttributeKey.BBox);
    bbox.setArrayNumberValue(new Double[][] { new Double[] { (71.9971) }, new Double[] { (375.839) }, new Double[] { (523.299) }, new Double[] { (714.345) } });
    // 设置结构属性的边界框值
    attrs.setAttribute(bbox); // 将边界框属性分配给结构属性

    // 为放置位置创建一个新的StructureAttribute
    StructureAttribute placement = new StructureAttribute(AttributeKey.Placement);
    placement.setNameValue(AttributeName.Placement_Block); // 将放置类型设置为块
    attrs.setAttribute(placement); // 将放置属性分配给结构属性

    // 从标记结构的根元素中检索第四个子元素
    StructureElement p2 = (StructureElement)tagged.getRootElement().getChildElements().get_Item(3);
    p2.clearChilds(); // 清除p2中任何现有的子元素

    // 创建一个新的SpanElement以添加到p2中
    SpanElement span1 = tagged.createSpanElement();

    // 为span元素创建结构属性
    StructureAttributes attrs = span1.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // 为文本装饰类型创建一个新的StructureAttribute
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // 将文本装饰设置为下划线
    attrs.setAttribute(textDecorationType); // 将文本装饰类型属性分配给结构属性

    // 为文本装饰厚度创建一个新的StructureAttribute
    StructureAttribute textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
    textDecorationThickness.setNumberValue(0); // 将文本装饰厚度设置为0
    attrs.setAttribute(textDecorationThickness); // 将文本装饰厚度属性分配给结构属性

    // 为文本装饰颜色创建一个新的StructureAttribute
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
    textDecorationColor.setArrayNumberValue(new Double[][] { new Double[] { (0.0196075) }, new Double[] { (0.384308) }, new Double[] { (0.756866) } });
    // 设置文本装饰的RGB颜色值
    attrs.setAttribute(textDecorationColor); // 将文本装饰颜色属性分配给结构属性

    p2.appendChild(span1); // 将span1元素附加到p2中


    // 创建一个新的MCR元素并用pBdc标记它
    MCRElement mcr = p2.tag(pBdc);
    // 检索MCR的父结构元素并创建布局属性
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // 为文本对齐创建一个新的StructureAttribute
    StructureAttribute textAlign = new StructureAttribute(AttributeKey.TextAlign);
    textAlign.setNameValue(AttributeName.TextAlign_Center); // 将文本对齐设置为居中
    attrs.setAttribute(textAlign); // 将文本对齐属性分配给结构属性

    // 为元素后的空间创建一个新的StructureAttribute
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(21.75); // 将元素后的空间设置为21.75单位
    attrs.setAttribute(spaceAfter); // 将空间后的属性分配给结构属性


    // 创建一个新的SpanElement以添加到p2中
    SpanElement span2 = tagged.createSpanElement();

    // 为span元素创建结构属性
    StructureAttributes attrs = span2.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // 为文本装饰类型创建一个新的StructureAttribute
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // 将文本装饰设置为下划线
    attrs.setAttribute(textDecorationType); // 将文本装饰类型属性分配给结构属性

    // 使用指定的键为文本装饰颜色创建一个新的StructureAttribute。
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);

    // 为文本装饰颜色属性设置数组数字值。
    // 颜色以RGB值数组表示，其中每个值都是一个Double。
    textDecorationColor.setArrayNumberValue(new Double[][] {
    new Double[] { (0.0196075) }, // 红色分量
    new Double[] { (0.384308) },  // 绿色分量
    new Double[] { (0.756866) }   // 蓝色分量
    });

    // 将文本装饰颜色属性设置为attrs对象。
    attrs.setAttribute(textDecorationColor);

    // 将子span元素附加到父元素p2。
    p2.appendChild(span2);

    // 为第二个链接创建一个新的LinkElement实例。
    LinkElement link2 = tagged.createLinkElement();

    // 使用随机生成的UUID为链接元素分配唯一ID。
    link2.setId(UUID.randomUUID().toString());

    // 将link2元素作为span2的子元素附加。
    span2.appendChild(link2);

    // 使用页面注释中的对应注释标记link2元素。
    link2.tag(page.getAnnotations().get_Item(1));

    // 用额外的元数据或上下文（link2Bdc）标记link2元素。
    link2.tag(link2Bdc);

    // 为第一个链接创建另一个LinkElement实例。
    LinkElement link1 = tagged.createLinkElement();

    // 使用随机生成的UUID为link1元素分配唯一ID。
    link1.setId(UUID.randomUUID().toString());

    // 将link1元素作为span1的子元素附加。
    span1.appendChild(link1);

    // 使用页面注释中的对应注释标记link1元素。
    link1.tag(page.getAnnotations().get_Item(2));

    // 用额外的元数据或上下文（link1Bdc）标记link1元素。
    link1.tag(link1Bdc);

    // 从标记文档的根元素中删除第一个子元素。
    tagged.getRootElement().removeChild(0);

    // 将文档保存到指定的输出目录，文件名为"_out.pdf"。
    document.save(dataDir + "_out.pdf");

```


## Aspose.PDF 24.6 中的新功能

自 24.6 起，Aspose.PDF for Java 允许使用 java.security.cert.X509Certificate, java.security.PrivateKey 对 PDF 进行签名：

此代码从证书存储中检索证书和私钥，然后使用它们对 PDF 文档的第一页应用数字签名。

```java

    KeyStore trustStore = KeyStore.getInstance("Windows");
    trustStore.load(null, null);
    java.security.cert.X509Certificate certificate = (java.security.cert.X509Certificate) trustStore.getCertificate("ProfMoriarty");
    PrivateKey key = (PrivateKey) trustStore.getKey("ProfMoriarty", null);

    PdfFileSignature pdfSign = new PdfFileSignature(getInputPdf());
    Signature signature = new ExternalSignature(certificate, key);
    pdfSign.sign(1, "reasonTest", "contactTest", "locationTest", true, new java.awt.Rectangle(1, 691, 100, 100), signature);

    pdfSign.save("PDFJAVA.pdf");
    pdfSign.close();
```

## Aspose.PDF 24.5 中的新功能

自从24.5版本发布以来，表单编辑器插件已实现。

**如何使用表单编辑器在PDF中编辑表单**

- 设置您的许可证密钥
- 创建一个FormEditor类的实例，该类提供用于操作PDF表单的方法
- 创建一个FormEditorAddOptions类的实例，该类指定向PDF文档添加表单字段的选项
- 使用代表文件路径或流的FileDataSource类向FormEditorAddOptions对象添加输入文件源和输出文件源
- 调用FormEditor对象的Process方法，将FormEditorAddOptions对象作为参数传递
- 使用ResultContainer.resultCollection访问结果

```java

    // 指定PDF文件的输入和输出路径。
    String inputPath = "sample.pdf";
    String outputPath = "out.pdf";

    // 创建FormEditor插件的实例。
    FormEditor pdfFormPlugin = new FormEditor();

    // 创建用于添加表单字段的选项。
    ArrayList<FormFieldCreateOptions> options = new ArrayList<FormFieldCreateOptions>();

    // 创建一个文本框表单字段。
    FormTextBoxFieldCreateOptions tmp1 = new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 600, 90, 610));
    tmp1.setValue("TextBoxField");
    tmp1.setColor(Color.getChocolate());
    tmp1.setPartialName("TexBoxField");
    options.add(tmp1);

    // 创建一个组合框表单字段。
    FormComboBoxFieldCreateOptions tmp2 = new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 800, 350, 815));

    tmp2.setColor(com.aspose.pdf.Color.getRed());
    tmp2.setEditable(new Boolean[]{true});
    tmp2.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    ArrayList<String> list1 = new ArrayList<String>();
    list1.add("p1");
    list1.add("p2");
    list1.add("p3");
    tmp2.setOptions(list1);
    tmp2.setSelected(new Integer[]{2});
    tmp2.setPartialName("ComboBoxField");
    options.add(tmp2);

    // 创建一个复选框表单字段。
    FormCheckBoxFieldCreateOptions tmp3 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715));
    tmp3.setValue("CheckBoxField 1");
    tmp3.setPartialName("CheckBoxField_1");
    tmp3.setColor(Color.getBlue());
    options.add(tmp3);


    // 创建一个复选框表单字段。
    FormCheckBoxFieldCreateOptions tmp4 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(100, 700, 190, 715));
    tmp4.setChecked(new Boolean[]{true});
    tmp4.setValue("CheckBoxField 2");
    tmp4.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    tmp4.setStyle(new Integer[]{BoxStyle.Cross});
    options.add(tmp4);


    // 创建一个复选框表单字段。
    FormCheckBoxFieldCreateOptions tmp5 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(200, 700, 390, 715));
    tmp5.setPartialName("CheckBoxField_3");
    tmp5.setValue("CheckBoxField 3");
    tmp5.setStyle(new Integer[]{BoxStyle.Star});
    tmp5.setChecked(new Boolean[]{true});
    tmp5.setTextHorizontalAlignment(new HorizontalAlignment[]{HorizontalAlignment.Center});
    options.add(tmp5);

    FormEditorAddOptions opt = new FormEditorAddOptions(options);

    // 向选项添加输入和输出文件。
    opt.addInput(new FileDataSource(inputPath));
    opt.addOutput(new FileDataSource(outputPath));

    // 使用插件处理表单字段。
    ResultContainer results = pdfFormPlugin.process(opt);
```


这个版本允许我们处理PDF图层。例如：

- 锁定PDF图层
- 提取PDF图层元素
- 扁平化分层PDF
- 将PDF中的所有图层合并为一个

**锁定PDF图层**

从24.5版本开始，您可以打开PDF，在第一页上锁定特定图层，并保存更改后的文档。新增了两个方法和一个属性：

Layer.Lock(); - 锁定图层。
Layer.Unlock(); - 解锁图层。
Layer.Locked; - 属性，指示图层的锁定状态。

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    Layer layer = page.getLayers().get(0);

    layer.lock();

    document.save(output);
```

**提取PDF图层元素**

Aspose.PDF for Java库允许从第一页提取每个图层，并将每个图层保存到一个单独的文件。

要从一个图层创建一个新的PDF，可以使用以下代码片段：

```java

    Document document = new Document(inputPath);
    java.util.List<Layer> layers = document.getPages().get_Item(1).getLayers();

    for (Layer layer : layers)
    {
        layer.save(outputPath);
    }
```


**将分层 PDF 扁平化**

Aspose.PDF for Java 库打开一个 PDF，遍历第一页上的每个图层，并将每个图层扁平化，使其在页面上永久保留。

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);

    for (Layer layer : page.getLayers())
    {
        layer.flatten(true);
    }
    document.save(output);
```

`Layer.flatten(boolean cleanupContentStream)` 方法接受一个布尔参数，该参数指定是否从内容流中删除可选内容组标记。将 `cleanupContentStream` 参数设置为 `false` 可以加速扁平化过程。

**将 PDF 内的所有图层合并为一个**

Aspose.PDF for Java 库允许将所有 PDF 图层或第一页上的特定图层合并到一个新图层中，并保存更新后的文档。

添加了两种方法来合并页面上的所有图层：

- void mergeLayers(String newLayerName);

- void mergeLayers(String newLayerName, String newOptionalContentGroupId);

第二个参数允许重命名可选内容组标记。默认值是 "oc1" (/OC /oc1 BDC)。

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    page.mergeLayers("NewLayerName");

    // 或者 page.mergeLayers("NewLayerName", "OC1");

    document.save(output);
```

## Aspose.PDF 24.4 的新功能

此版本为 PDF 引入了 Java 插件：

- 表单展平插件

```java

    FormFlattener pdfFormPlugin = new FormFlattener();

    FormFlattenAllFieldsOptions opt = new FormFlattenAllFieldsOptions();

    opt.addInput(new FileDataSource("sample.pdf"));
    opt.addOutput(new FileDataSource("sample-flat.pdf"));

    ResultContainer result = pdfFormPlugin.process(opt);

    // 检查结果。
    java.util.List < IOperationResult > resultCollectionInternal = result.getResultCollection();
```

- 表单导出器

```java

    Rectangle rect = new com.aspose.pdf.Rectangle(0, 220, 600, 330);

    // 插件使用。
    FormExporter pdfFormPlugin = new FormExporter();
    SelectField selectField = new SelectField() {
      public boolean invoke(Field field) {
        return field instanceof TextBoxField && field.getPageIndex() == 2 && rect.isInclude(field.getRect(), 0);
      }
    };
    FormExporterValuesToCsvOptions opt = new FormExporterValuesToCsvOptions(selectField, ';');

    opt.addInput(new FileDataSource(inputFileNameWithFields));
    opt.addInput(new FileDataSource(getInputPath("document-1.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-2.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-3.pdf")));
    opt.addOutput(new FileDataSource(getOutputPath("out.csv")));
    ResultContainer result = pdfFormPlugin.process(opt);

    // 检查结果。
    System.out.println(result.getResultCollectionInternal().size() > 0);
    System.out.println(result.getResultCollectionInternal().get_Item(0).isFile());
    System.out.println(result.getResultCollectionInternal().get_Item(0).getData().toString());
```


- 合并插件

```java

    String input1 = "sample.pdf";
    String input2 = "sample.pdf";

    String output = "TestMergeFileAndStream_ResultAsFile.pdf";

    Merger merger = new Merger();

    MergeOptions opt = new MergeOptions();
    opt.addInput(new FileDataSource(input1));
    opt.addInput(new StreamDataSource(new FileInputStream(input2)));

    opt.addOutput(new FileDataSource(output));

    ResultContainer results = merger.process(opt);

    System.out.println(results.getResultCollection().size());
    System.out.println(results.getResultCollection().get(0).isFile());
```

- 优化器插件

如何减小PDF文档的大小？

```java

    String input = "Test.pdf";
    String output = "Optimized.pdf";

    Optimizer optimizer = new Optimizer();

    OptimizeOptions opt = new OptimizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    optimizer.process(opt);
```

如何调整PDF文档的大小？

```java

    String input = "sample.pdf";
    String output = "ResizeMain.pdf";

    Optimizer organizer = new Optimizer();

    ResizeOptions opt = new ResizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    opt.setPageSize(PageSize.getA1());

    organizer.process(opt);
```


如何旋转PDF文档？

```java

    String input = "sample.pdf";
    String output = "OptimizerRotateMain.pdf";

    Optimizer optimizer = new Optimizer();

    RotateOptions opt = new RotateOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));
    opt.setRotation(Rotation.on90);

    ResultContainer results = optimizer.process(opt);
```

## Aspose.PDF 24.3 的新功能

从24.3开始，在TextFragmentAbsorber中实现通过短语列表的搜索。

```java

    String[] expressions = new String[] {
      //检测电话号码
      "\\b\\d{3}-\\d{3}-\\d{4}\\b",
      //检测卡号
      "\\b(?:\\d[ -]*?){13,16}\\b"
    };
    Document document = new Document(input);

    TextFragmentCollection newTextFragmentCollection = new TextFragmentCollection();

    Pattern[] regexes = new Pattern[6];
    for (int i = 0; i < expressions.length; i++) {
      regexes[i] = Pattern.compile(expressions[i], Pattern.CASE_INSENSITIVE);
    }
    TextFragmentAbsorber newAbsorber = new TextFragmentAbsorber(regexes, new TextSearchOptions(true));
    document.getPages().accept(newAbsorber);
    HashMap < Pattern, TextFragmentCollection > map = newAbsorber.getRegexResults();
```


接下来的功能是为PDF到Markdown转换器添加转换表格的功能

```java

    Document doc = new Document(dataDir + "56201.pdf");
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    doc.save(dataDir + "56201.md", saveOptions);
```

## Aspose.PDF 24.2中的新功能

从24.2版本开始，可以在带有AcroForms的PDF中添加水印。TextStamp适用于AcroForm文件。如果在XFA文件中使用TextStamp，文本会像普通PDF文件一样绘制在页面上（可以在无法读取XFA文件的PDF查看器中看到，例如在Chrome浏览器中）。要向XFA文件添加文本，必须在XFA文件的内部XML中更改。

```java

    String sourceName = dataDir + "551.3xfa.pdf";
    String targetName = dataDir + "output_2_" + BuildVersionInfo.AssemblyVersion + ".pdf";

    Document pdfDocument = new Document(sourceName);
    XFA xfa = pdfDocument.getForm().getXFA();

    String watermark =
    "<subform>" +
    "<draw rotate=\"90\" x=\"100px\" y=\"100px\">" +
    "<value>" +
    "<text>Sample Stamp</text>\n" +
    "</value>" +
    "<font typeface=\"Arial\" size=\"14px\" weight=\"bold\" posture=\"italic\">" +
    "<fill>" +
    "<color value=\"0,128,0\"/>" +
    "</fill>" +
    "</font>" +
    "</draw>" +
    "</subform>";

    xfa.appendToTemplate("//tpl:pageArea", watermark);

    pdfDocument.save(targetName);
    pdfDocument.close();
```


设置用于注释的状态模型  
我们可以使用 MarkupAnnotation 类中的 setReviewState 和 setMarkedState 来设置所需的状态。  
所有标记注释都有一个可用的设置状态选项。

```java

    // 打开源 PDF 文档
    Document pdfDocument = new Document();
    pdfDocument.getPages().add();
    // 创建注释
    TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.getPages().get_Item(1), new Rectangle(200,
            400, 400, 600));

    // 设置注释标题
    textAnnotation.setTitle("示例注释标题");

    // 设置注释主题
    textAnnotation.setSubject("示例主题");
    // 指定注释内容
    textAnnotation.setContents("注释的示例内容");
    textAnnotation.setOpen(true);
    textAnnotation.setIcon(TextIcon.Key);
    com.aspose.pdf.Border border = new com.aspose.pdf.Border(textAnnotation);
    border.setWidth(5);
    border.setDash(new Dash(1, 1));
    textAnnotation.setBorder(border);
    String userName1 = "Aspose1";
    textAnnotation.setReviewState(AnnotationState.Rejected, userName1);
    textAnnotation.setRect(new Rectangle(200, 400, 400, 600));

    // 添加注释到页面的注释集合中
    pdfDocument.getPages().get_Item(1).getAnnotations().add(textAnnotation);
    pdfDocument.processParagraphs();

    // 保存输出文件
    pdfDocument.save(dataDir + "output_24_2_Rejected.pdf");

    pdfDocument = new Document(dataDir + "output" + version + "3.pdf");
    TextAnnotation textAnnotation2 = (TextAnnotation) pdfDocument.getPages().get_Item(1).getAnnotations().get_Item(1);

    String userName2 = "Aspose2";
    textAnnotation2.setReviewState(AnnotationState.Accepted, userName2);
    pdfDocument.save(dataDir + "output_24_2_Rejected_and_Accepted.pdf");
```


从24.2开始实现OFD到PDF的转换：

```java

    Document document = new Document(inputPath, new OfdLoadOptions());
    document.save(outputPath);
```

## Aspose.PDF 24.1中的新增功能

从24.1版本开始实现PDF到Markdown的转换：

```java

    final Document doc = new Document(inputPdfPath);
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Outlines);
    doc.save(markdownOutputFilePath, saveOptions);
```

此外，在24.1中实现了使用InterruptMonitor的线程中断。

```java

    final InterruptMonitor monitor = new InterruptMonitor();

    new Thread(new Runnable() {

      public void run() {

        InterruptMonitor.setThreadLocalInstance(monitor);
        Document document = new Document();

        try {
          Page page = document.getPages().insert(1);
          PageInfo pageInfo = page.getPageInfo();
          pageInfo.setLandscape(true);
          Table topicTable = new Table();
          topicTable.setBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setColumnWidths("5% 10% 5% 60% 10% 10%");
          topicTable.setRepeatingRowsCount(1);

          Row topicRow = topicTable.getRows().add();

          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");
          topicRow.getCells().add("text");

          //foreach to while statements conversion
          Iterator tmp0 = (topicRow.getCells()).iterator();
          while (tmp0.hasNext()) {
            Cell cell = (Cell) tmp0.next();
            cell.setVerticalAlignment(VerticalAlignment.Center);
            cell.setAlignment(HorizontalAlignment.Center);
          }

          Row row2 = topicTable.getRows().add();
          row2.getCells().add("text");
          row2.getCells().add("text");
          row2.getCells().add("text");
          String LongText = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.";
          row2.getCells().add(LongText);
          row2.getCells().add("text");
          row2.getCells().add("text");
          page.getParagraphs().add(topicTable);
          document.save(dataDir + "out" + version + ".pdf");

        } catch (com.aspose.pdf.exceptions.OperationCanceledException ex) {
          System.out.println("Interrupting the save thread at " + System.currentTimeMillis());
        } finally {
          if (document != null) {
            document.close();
          }
        }

      }

    }).start();

    System.out.println("Process is started thread at " + System.currentTimeMillis());

    // The timeout should be less than the time required for full document save (without interruption).
    Thread.sleep(500);

    // Interrupt the process
    monitor.interrupt();

    System.out.println("Interrupted the save thread at " + System.currentTimeMillis());
```


## Aspose.PDF 23.12 中的新功能

可以使用以下代码片段找到表单并替换文本：

```java

    Document document = new Document(input);
    String expectedText = "This is a text added while creating new PDF in Kofx Power PDF Standard.";

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
      XForm form = (XForm) tmp0.next();
      if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(form);

        Iterator tmp1 = (absorber.getTextFragments()).iterator();
        while (tmp1.hasNext()) {
          TextFragment fragment = (TextFragment) tmp1.next();
          fragment.setText("");
        }
      }
    }

    document.save(output);
```

或者，可以完全删除表单：

```java

    Document document = new Document(input);
    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    //foreach 转换为 while 语句
    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
        XForm form = (XForm) tmp0.next();
        if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
            String name = forms.getFormName(form);
            forms.delete(name);
        }
    }

    document.save(output);
```


另一种删除表单的变体：

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    for (int i = 1; i <= forms.size(); i++) {
        if ("Typewriter".equals(forms.get_Item(i).getIT()) && "Form".equals(forms.get_Item(i).getSubtype())) {
            forms.delete(forms.get_Item(i).getName());
        }
    }

    document.save(output);
``` 

- 可以使用以下代码片段删除所有表单：

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    forms.clear();

    document.save(output);
```

## Aspose.PDF 23.11 的新功能

从这个版本开始，可以从 PDF 文件中删除隐藏文本：

```java

    Document document = new Document(inputFile);

    TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
    textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
    document.getPages().accept(textAbsorber);

    msStringBuilder result = new msStringBuilder();

    // foreach 循环转换为 while 语句
    Iterator tmp0 = (textAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext()) {
            TextFragment fragment = (TextFragment) tmp0.next();
            if (fragment.getTextState().isInvisible()) {
                result.append(fragment.getText());
                fragment.setText("");
            }
        }

    document.save(outputFile);
```


## Aspose.PDF 23.10 中的更新内容

当前更新提供了三种从标记的 PDF 中移除标签的方法。

- 从 documentElement（根树元素）中移除某个节点元素：

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element documentElement = structure.getChildren().get_Item(0);
    Element structElement = (documentElement.getChildren().getCount() > 1) ?  documentElement.getChildren().get_Item(1) : null;
    documentElement.getChildren().remove(structElement);
    // 您也可以删除 structElement 本身
                //if (structElement != null)
                //{
                //    structElement.remove();
                //}
    document.save(outputPath);
```

- 从文档中移除所有标记的元素标签，但保留结构元素：

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root= structure.getChildren().get_Item(0);
    Queue<Element> queue = new ArrayDeque<Element>();
    queue.add(root);
    for (Element element : structure.getChildren() ) {
        queue.add(element);
        for (Element child : element.getChildren())
        {
            queue.add(child);
        }
    }
    for (Element element:queue ) {
        if (element instanceof TextElement  || element instanceof FigureElement)
            element.remove();
    }
    document.save(outputPath);
```


- 完全删除标签：

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root = structure.getChildren().get_Item(0);
    root.remove();
    document.save(outputPath);
```

我们实现了一个新功能来测量字符高度。使用以下代码来测量字符的高度：

```java

    Document doc = new Document("input.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.visit(doc.getPages().get_Item(1));
    double height = absorber.getTextFragments().get_Item(1).getTextState().measureHeight('h')
```

请注意，测量是基于文档中嵌入的字体。如果缺少任何尺寸信息，此方法将返回0。

## Aspose.PDF 23.9 中的新功能

从23.9开始支持从可填写字段中删除子注释。

示例1：

```java

    String input = "55343_1.pdf";
    Document doc = new Document(input);
    final String fieldName = "1 Vehicle Identification Number";
    Field field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
    Rectangle rect = field.getRect();
    doc.getForm().addFieldAppearance(field, 2, rect);
    System.out.println(2 == field.size());

    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(2 == field.size());
    doc.getForm().removeFieldAppearance(field, 1);

    System.out.println(0 == field.size());
    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
```


example 2:

```java

    {
    String option1 = "选项 1";
    String option2 = "选项 2";
    String outputPdf = "输出.pdf";

    final Document document = new Document();
    try /*JAVA: 使用中*/ {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

        // 设置第一个复选框组的选项值
        checkbox.setExportValue(option1);
        checkbox.addOption(option2);
        document.getForm().add(checkbox);
        java.util.List < String > tmp0 = new ArrayList < String > ();
        tmp0.add("Off");
        tmp0.add(option1);
        tmp0.add(option2);
        System.out.println(collectionAssert_AreEqual(tmp0, checkbox.getAllowedStates()));
        checkbox.setValue(option2);

        WidgetAnnotation f = document.getForm().get_Item(1);
        document.getForm().removeFieldAppearance((Field) f, 2);

        checkbox = (CheckboxField) document.getForm().get_Item(1);
        java.util.List < String > tmp1 = new java.util.ArrayList < String > ();
        tmp1.add("Off");
        tmp1.add(option1);
        System.out.println(collectionAssert_AreEqual(tmp1, checkbox.getAllowedStates()));

        document.save(outputPdf);
    } finally {
        if (document != null)(document).close();
    }
    }
    public static boolean collectionAssert_AreEqual(java.util.List < String > value1,
    java.util.List < String > value2) {
    if (value1.size() == value2.size()) {
        for (int i = 0; i < value1.size(); i++) {
        if (!value1.get(i).equals(value2.get(i)))
            return false;
        }
    } else {
        return false;
    }
    return true;
    }
```


添加使用 ImageFilterType.Flate 的图像不保留透明度。

```java

    Document document = new Document();
    Page page = document.getPages().add();

    FileInputStream stream = new FileInputStream(("55037_1.png"));

    page.getResources().getImages().addWithImageFilterType(stream, ImageFilterType.Flate);
    page.getContents().add(new GSave());
    Rectangle rectangle = new Rectangle(413, 428, 548, 564);
    Matrix matrix = new Matrix(
      new double[] {
        rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY()
      });

    page.getContents().add(new ConcatenateMatrix(matrix));
    XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
    page.getContents().add(new Do(ximage.getName()));
    page.getContents().add(new GRestore());
    document.save(getOutputPath("55157.pdf"));
    stream.close();
```

## Aspose.PDF 23.8 中的新功能是什么

在23.8中添加了检测PDF文档增量更新的功能。此功能在文档以增量更新保存时返回“true”，否则返回“false”。

```java

    Document doc = new Document(dataDir+"PDF_Support_Tech_Note.pdf");
    boolean not_updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(not_updatedIncrementally);

    doc.getPages().add();
    doc.saveIncrementally(dataDir+"PDF_updatedIncrementally.pdf");

    doc = new Document(dataDir+"PDF_updatedIncrementally.pdf");
    boolean updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(updatedIncrementally);
    doc.close();
```    

另一个功能是将输入PDF中的输出意图复制到目标PDF中。

我们添加了一个新的公共属性Document.getOutputIntents()，以允许访问文档中的输出意图。目前仅支持使用某些文档中已存在的输出意图，用户无法从头创建OutputIntent。

```java

    Document document1 = new Document(dataDir+"pdfa.pdf");
    Document resultDocument = new Document();
    resultDocument.getPages().add(document1.getPages());

    for (OutputIntent intent : document1.getOutputIntents())
    {
        resultDocument.getOutputIntents().addItem(intent);
    }

    resultDocument.save(dataDir+"resultpath.pdf");
```  


从 Aspose.PDF 23.8 支持添加形状提取：

```java

{
    String input1 = getInputPdf("46298_1");
    String input2 = getInputPdf("46298_2");

    Document source = new Document(input1);
    Document dest = new Document(input2);

    Page destPage = dest.getPages().get_Item(1);

    TextFragmentAbsorber tfAbsorber = new TextFragmentAbsorber();
    tfAbsorber.visit(source.getPages().get_Item(1));

    // foreach 转换为 while 语句
    Iterator tmp0 = ( tfAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext())
        {
            TextFragment textFragment = (TextFragment)tmp0.next();
            System.out.println(textFragment.getText());
            addTextImproved(destPage, textFragment);
        }

    ImagePlacementAbsorber imageAbsorber = new ImagePlacementAbsorber();
    imageAbsorber.visit(source);

    Iterator tmp1 = ( imageAbsorber.getImagePlacements()).iterator();
        while (tmp1.hasNext())
        {
            ImagePlacement image = (ImagePlacement)tmp1.next();
            destPage.addImage(image.getImage().toStream(), image.getRectangle());
        }

    GraphicsAbsorber vectorAbsorber = new GraphicsAbsorber();
    vectorAbsorber.visit(source.getPages().get_Item(1));
    Rectangle area = new Rectangle(90, 250, 300, 400);
    dest.getPages().get_Item(1).addGraphics(vectorAbsorber.getElements(), area);
    dest.save(getOutputPath("46298-out.pdf"));
    }

    private static void addTextImproved(Page page, TextFragment textFragment)
    {
        TextFragment local = new TextFragment();
        local.setPosition(textFragment.getPosition());

        // 重新计算新位置，因为页面大小与原始 PDF 不同
        local.getPosition().setXIndent(textFragment.getPosition().getXIndent());//2.5 * 72;
        double newPageHeight = page.getPageRect(true).getHeight();
        double oldPageHeight = textFragment.getPage().getPageRect(true).getHeight();
        local.getPosition().setYIndent(textFragment.getPosition().getYIndent());

        local.setText(textFragment.getText());
        local.getTextState().setFont(textFragment.getTextState().getFont());
        local.getTextState().setFontSize(textFragment.getTextState().getFontSize());

        local.getTextState().setFormattingOptions(textFragment.getTextState().getFormattingOptions());
        local.getTextState().setForegroundColor(textFragment.getTextState().getForegroundColor());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(local);
    }
```


还支持在添加文本时检测溢出的能力：

```java

    Document doc = new Document();
    String paragraphContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan.";
    Rectangle rectangle = new Rectangle(100, 600, 500, 700, false);
    TextParagraph paragraph = new TextParagraph();
    TextFragment fragment = new TextFragment(paragraphContent);
    paragraph.setVerticalAlignment(VerticalAlignment.Top);
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    paragraph.setRectangle(rectangle);
    boolean isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    while (!isFitRectangle)
    {
        fragment.getTextState().setFontSize(fragment.getTextState().getFontSize() - 0.5f);
        isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    }
    paragraph.appendLine(fragment);
    TextBuilder builder = new TextBuilder(doc.getPages().add());
    builder.appendParagraph(paragraph);
    doc.save(output);
```


## Aspose.PDF 23.7 中的新增功能

从23.7版本开始支持打印对话框预设页面缩放：

```java

    Document document = new Document();
    document.getPages().add();
    document.setPrintScaling(PrintScaling.None);//PrintScaling.Default
    document.save(outputPdf);

    Document documentOutput = new Document(outputPdf);
    int printScaling = documentOutput.getPrintScaling();
    System.out.println("PrintScaling: " + printScaling);
```

## Aspose.PDF 23.6 中的新增功能

从23.6版本开始支持设置HTML、Epub页面标题的功能。

HTML代码：

```java

    HtmlSaveOptions options = new HtmlSaveOptions();
    options.setFixedLayout(true);
    options.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
    options.setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml);
    options.setTitle("</title>NEW PAGE & TITILE</head>");

    Document document = new Document(inputPath);
    document.save(outPath, options);
```


代码用于 EPUB:

```java

    EpubSaveOptions epubSaveOptions = new EpubSaveOptions();
    epubSaveOptions.setTitle("</title>新页面 & 标题</head>");
    epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

    Document document = new Document(inputPath);
    document.save(outPath, epubSaveOptions);
```

从 23.6 开始支持提供定位矢量图形的 API:

```java

    Document document = new Document(input);
    VectorGraphicsAbsorber vectorAbsorber = new VectorGraphicsAbsorber();
    vectorAbsorber.visit(document.getPages().get_Item(1));

    SubPath subPath1 = vectorAbsorber.getSubPaths().get_Item(2);
    SubPath subPath2 = vectorAbsorber.getSubPaths().get_Item(3);
    SubPath subPath3 = vectorAbsorber.getSubPaths().get_Item(4);

    Point point1 = new Point(subPath1.getPosition().getX() + 200, subPath1.getPosition().getY() - 100);
    Point point2 = new Point(subPath2.getPosition().getX() + 200, subPath2.getPosition().getY() - 100);
    Point point3 = new Point(subPath3.getPosition().getX() + 200, subPath3.getPosition().getY() - 100);

    subPath1.setPosition(point1);
    subPath2.setPosition(point2);
    subPath3.setPosition(point3);

    document.save(output);
```

## Aspose.PDF 23.1 中的新增功能

从23.1版本开始支持创建PrinterMark注释。添加了一种注释变体：ColorBarAnnotation。

```java

    Document doc = new Document();
    Page page = doc.getPages().add();
    page.setTrimBox(new com.aspose.pdf.Rectangle(20, 20, 580, 820));
    Rectangle rectBlack = new com.aspose.pdf.Rectangle(100, 300, 300, 320);
    Rectangle rectCyan = new com.aspose.pdf.Rectangle(200, 600, 260, 690);
    Rectangle rectMagenta = new com.aspose.pdf.Rectangle(10, 650, 140, 670);

    ColorBarAnnotation colorBarBlack = new ColorBarAnnotation(page, rectBlack);
    ColorBarAnnotation colorBarCyan = new ColorBarAnnotation(page, rectCyan, ColorsOfCMYK.Cyan);
    ColorBarAnnotation colorBaMagenta = new ColorBarAnnotation(page, rectMagenta);
    colorBaMagenta.setColorOfCMYK(ColorsOfCMYK.Magenta);
    ColorBarAnnotation colorBarYellow = new ColorBarAnnotation(page, new com.aspose.pdf.Rectangle(400, 250, 450, 700), ColorsOfCMYK.Yellow);

    page.getAnnotations().add(colorBarBlack);
    page.getAnnotations().add(colorBarCyan);
    page.getAnnotations().add(colorBaMagenta);
    page.getAnnotations().add(colorBarYellow);
    doc.save("outFile.pdf");
```


## Aspose.PDF 22.12 中的新功能

从此版本开始支持将 PDF 转换为 DICOM 图像：

```java

    DicomDevice device = new DicomDevice(PageSize.getA4());
    Document doc = new Document("Input.pdf");
    ByteArrayOutputStream stream = new ByteArrayOutputStream();
    device.process(doc.getPages().get_Item(1), stream);
```

## Aspose.PDF 22.9 中的新功能

从 22.09 开始支持添加属性以修改签名中的主题标题顺序 (E=, CN=, O=, OU=)。

```java

    String inputPdf = getInputPath("input.pdf");
    String inputPfx = getInputPath("input.pfx");
    String outputPdf = getOutputPath("out.pdf");

    final PdfFileSignature fileSign = new PdfFileSignature();
    try 
    {
        fileSign.bindPdf(inputPdf);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 400, 100);
        PKCS7Detached signature = new PKCS7Detached(inputPfx, "123456789");
        signature.setDate(new Date());
        signature.setCustomAppearance( new SignatureCustomAppearance());
        signature.getCustomAppearance().setUseDigitalSubjectFormat(true);
        signature.getCustomAppearance().setDigitalSubjectFormat(new /*SubjectNameElements*/int[] { SubjectNameElements.CN, SubjectNameElements.O });

        fileSign.sign(1, true, rect, signature);
        fileSign.save(outputPdf);
    }
    finally { 
        if (fileSign != null) 
            fileSign.close(); 
    }
```

## Aspose.PDF 22.8 的新功能

从 Aspose.PDF 23.8 开始支持添加重建 xref 表的方法：

```java

    PdfFileSanitization sanitizer = new PdfFileSanitization();
    try {
        sanitizer.bindPdf(dataDir + "50528_1.pdf");
        sanitizer.rebuildXrefAndTrailer();
        sanitizer.save(dataDir + "50528_1" + version + ".pdf");
    } finally {
        if (sanitizer != null) ( sanitizer).close();
    }
```


## Aspose.PDF 22.6 的新功能

PDF 转换为 PDF_A_1A - 实现去除透明色的选项以避免输出文件过大。

从版本 22.5 开始，客户能够控制转换后的透明度质量，以及由此产生的输出文件大小：

```java
    opts.setTransparencyResolution(300);
```

## Aspose.PDF 22.5 的新功能

在 PDF/A 转换过程中，透明内容被移除并替换为图像。我们实现了一个新功能，现在客户可以通过 TransparencyResolution 参数控制图像质量：

```java

    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
    PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
    options.setTransparencyResolution(300);
    pdfDocument.convert(options);
    pdfDocument.save("finalOutput.pdf");
```


## Aspose.PDF 22.4 中的新功能

此版本包含有关 Aspose.PDF for Java 的信息：

- PDF 到 ODS：识别下标和上标中的文本；

**示例**

```java

    Document pdfDocument = new Document("Superscript-Subscript.pdf");
    ExcelSaveOptions options = new ExcelSaveOptions();
    options.Format = ExcelSaveOptions.ExcelFormat.ODS;
    pdfDocument.Save("output.ods"), options);
```

- PDF 到 XMLSpreadSheet2003：识别下标和上标中的文本；

- PDF 到 Excel：识别下标和上标中的文本；

## Aspose.PDF 22.3 中的新功能

PDF 到 ODS：版本 22.3 中提供了对 RTL 的支持

```java

    ExcelSaveOptions options = new ExcelSaveOptions();
    options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
    pdfDocument.save("output.ods", options);
```

## Aspose.PDF 22.2 中的新功能

此版本包括 PDF 到 XSLX：支持 RTL（希伯来语，阿拉伯语）。

## Aspose.PDF 22.1 中的新功能

Aspose.PDF for Java 允许加载文档便携式文档格式 (PDF) 版本 2.0。

## Aspose.PDF 21.10 中的新功能

### 如何检测隐藏文本？

请使用以下代码：

```java

Document pdf = new Document(inFile);
        Page page = pdf.getPages().get_Item(1);
        TextFragmentAbsorber textFragmentAbsorber = new com.aspose.pdf.TextFragmentAbsorber();
        page.accept(textFragmentAbsorber);
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

        int fragmentsCount = textFragmentAbsorber.getTextFragments().size();
        int invisibleCount = 0;

        Iterator tmp0 = ( textFragmentCollection).iterator();
            while (tmp0.hasNext())
            {
                com.aspose.pdf.TextFragment fragment = (com.aspose.pdf.TextFragment)tmp0.next();
                System.out.println(fragment.getText());
                System.out.println(fragment.getTextState().isInvisible());
                if (fragment.getTextState().isInvisible())
                    invisibleCount++;
            }
```


## Aspose.PDF 21.8 中的新功能

### 如何更改数字签名中的文字颜色？

在21.8版本中，setForegroundColor允许更改数字签名中的文字颜色：

```java
请使用以下代码：

                    PdfFileSignature pdfSign = new PdfFileSignature();                
                    pdfSign.bindPdf(inFile);
                    //创建一个用于签名位置的矩形
                    java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);
                    PKCS7 pkcs = new PKCS7(inPfxFile, "");

                    pkcs.setCustomAppearance( new SignatureCustomAppearance());
//设置文字颜色
                    pkcs.getCustomAppearance().setForegroundColor(Color.getGreen());

                    // 签署PDF文件
                    pdfSign.sign(1, true, rect, pkcs);
                    //保存输出的PDF文件
                    pdfSign.save(outFile);
```

## Aspose.PDF 21.6 中的新功能

### 使用 ImagePlacementAbsorber 隐藏文档中的图像

使用 Aspose.PDF for Java，您可以使用 ImagePlacementAbsorber 从文档中隐藏图像：

```java
      Document doc = new Document("input.pdf");

        for (Page page : doc.getPages()) {
            ImagePlacementAbsorber ipa = new ImagePlacementAbsorber();
            ipa.visit(page);
            for (ImagePlacement ip : ipa.getImagePlacements()) {
                ip.hide();
            }
        }

        doc.save("out.pdf");
```

## Aspose.PDF 21.5 有什么新功能

### 添加用于合并图像的 API

Aspose.PDF 21.4 允许您组合图像。将图像流列表合并为一个图像流。支持的输出格式包括 Png/jpg/tiff，如果使用不支持的格式，输出流默认编码为 Jpeg。
请参见下面的代码片段：

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile300dpi = new FileInputStream("image1.jpg");
        try  {
            inputImagesStreams.add(inputFile300dpi);
            InputStream inputFile600dpi = new FileInputStream("image2.jpg");
            try {
                inputImagesStreams.add(inputFile600dpi);
                inputStream = PdfConverter.mergeImages(
                        inputImagesStreams,
                        com.aspose.pdf.ImageFormat.Jpeg,
                        ImageMergeMode.Vertical,
                        new Integer(1),
                        new Integer(1)
                );
            } finally {
                if (inputFile600dpi != null) (inputFile600dpi).close();
            }
        } finally {
            if (inputFile300dpi != null) (inputFile300dpi).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out.pdf");
        inputStream.close();
```


也可以将您的图像合并为Tiff格式：

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile1 = new FileInputStream("1.tif");
        try  {
            inputImagesStreams.add(inputFile1);
            InputStream inputFile2 = new FileInputStream("2.tif");
            try {
                inputImagesStreams.add(inputFile2);
                inputStream = PdfConverter.mergeImagesAsTiff(inputImagesStreams);
            } finally {
                if (inputFile2 != null) (inputFile2).close();
            }
        } finally {
            if (inputFile1 != null) (inputFile1).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out2.pdf");
        inputStream.close();
```

## Aspose.PDF 21.02 中的新功能是什么

Aspose.PDF v21.02 使用 PAdES LTV 签名签署 PDF

```java
final Document document = new Document(inputPdf);
    try 
    {
        PdfFileSignature signature = new PdfFileSignature(document);
        PKCS7 pkcs7 = new PKCS7(getInputPath("cert.pfx"), "password");
        //使用 PAdES LTV 签名签署 PDF
        pkcs7.setUseLtv(true);

        signature.sign(1, true, new Rectangle(100, 100, 300, 300), pkcs7);
        signature.save(outputPdf);
    }
    finally { if (document != null) (document).dispose(); }
```