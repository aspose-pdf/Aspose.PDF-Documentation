---
title: 使用运算符
linktitle: 使用运算符
type: docs
weight: 170
url: /java/operators/
description: 本主题解释了如何使用 Aspose.PDF 的运算符。运算符类为 PDF 操作提供了强大的功能。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 运算符及其用法介绍

运算符是一个 PDF 关键字，指定要执行的某些操作，例如在页面上绘制图形形状。运算符关键字通过没有初始斜线字符（2Fh）与命名对象区别开来。运算符只有在内容流中才有意义。

内容流是一个 PDF 流对象，其数据由描述要在页面上绘制的图形元素的指令组成。有关 PDF 运算符的更多详细信息可以在 [PDF 规范](https://www.adobe.com/devnet/pdf/pdf_reference.html) 中找到。

### 实施细节

本主题解释了如何使用 Aspose.PDF 的运算符。
 The selected example adds an image into a PDF file to illustrate the concept. To add an image in a PDF file, different operators are needed. This example uses [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do), and [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).

- The [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) operator saves the PDF's current graphical state.
- 本主题解释了如何使用 Aspose.PDF 的操作符。 选定的示例在 PDF 文件中添加了一张图片以说明这一概念。要在 PDF 文件中添加图片，需要使用不同的操作符。此示例使用了 [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave)、[ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix)、[Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) 和 [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore)。

- （连接矩阵）操作符用于定义图片应如何放置在 PDF 页面上。
- [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) 操作符在页面上绘制图片。
- [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) 操作符恢复图形状态。

要在 PDF 文件中添加图片：

1. 创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象并打开输入的 PDF 文档。
1. 获取要添加图像的特定页面。
1. 将图像添加到页面的资源集合中。
1. 使用操作符将图像放置在页面上：
   - 首先，使用 [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) 操作符保存当前图形状态。
   - 然后使用 [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix) 操作符指定图像的位置。
   - 使用 [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) 操作符在页面上绘制图像。
1. 最后，使用 [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) 操作符保存更新后的图形状态。

以下代码片段显示了如何使用 PDF 操作符。

```java
public class WorkingWithOperators {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Operators/";

    public static void AddImageUsingOpeartors() {

        // 创建一个新的 PDF 文档
        Document pdfDocument = new Document(_dataDir + "PDFOperators.pdf");

        // 获取需要添加图像的页面
        Page page = pdfDocument.getPages().get_Item(1);

        // 设置坐标
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // 将图像加载到流中
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(_dataDir + "PDFOperators.jpg");
        } catch (FileNotFoundException e) {
            // TODO 自动生成的 catch 块
            e.printStackTrace();
        }

        // 将图像添加到页面资源的图像集合中
        page.getResources().getImages().add(imageStream);

        // 使用 GSave 操作符：该操作符保存当前图形状态
        page.getContents().add(new GSave());
        // 创建 Rectangle 和 Matrix 对象
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // 使用 ConcatenateMatrix（连接矩阵）操作符：定义图像的放置方式
        page.getContents().add(new ConcatenateMatrix(matrix));

        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // 使用 Do 操作符：该操作符绘制图像
        page.getContents().add(new Do(ximage.getName()));
        // 使用 GRestore 操作符：该操作符恢复图形状态
        page.getContents().add(new GRestore());

        // 保存更新后的文档
        pdfDocument.save(_dataDir + "PDFOperators_out.pdf");
    }
```


## 使用操作符在页面上绘制XForm

本主题演示如何使用GSave/GRestore操作符、ContatenateMatrix操作符来定位xForm，以及Do操作符在页面上绘制xForm。

下面的代码使用GSave/GRestore操作符对PDF文件的现有内容进行包装。这种方法有助于在现有内容的末尾获取初始图形状态。没有这种方法，可能会在现有操作符链的末尾保留一些不需要的变换。

```java
    public static void DrawXFormUsingOpeartors() {
        String imageFile = _dataDir + "aspose-logo.jpg";
        String inFile = _dataDir + "DrawXFormOnPage.pdf";
        String outFile = _dataDir + "blank-sample2_out.pdf";

        Document pdfDocument = new Document(inFile);
        OperatorCollection pageContents = pdfDocument.getPages().get_Item(1).getContents();

        // 示例演示
        // GSave/GRestore 操作符的使用
        // ContatenateMatrix 操作符用于定位 xForm
        // Do 操作符用于在页面上绘制 xForm

        // 用 GSave/GRestore 操作符对现有内容进行包装
        // 这是为了在现有内容的末尾获取初始图形状态
        // 否则可能会在现有操作符链的末尾保留一些不需要的变换
        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());

        // 添加保存图形状态的操作符以在新命令后正确清除图形状态
        pageContents.add(new GSave());

        // 创建 xForm
        XForm form = XForm.createNewForm(pdfDocument.getPages().get_Item(1), pdfDocument);
        pdfDocument.getPages().get_Item(1).getResources().getForms().add(form);
        form.getContents().add(new GSave());

        // 定义图像宽度和高度
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // 将图像加载到流中
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(imageFile);
        } catch (FileNotFoundException e) {
            // TODO 自动生成的 catch 块
            e.printStackTrace();
        }

        // 将图像添加到 XForm 资源的图像集合中
        form.getResources().getImages().add(imageStream);
        XImage ximage = form.getResources().getImages().get_Item(form.getResources().getImages().size());
        // 使用 Do 操作符：该操作符绘制图像
        form.getContents().add(new Do(ximage.getName()));
        form.getContents().add(new GRestore());

        pageContents.add(new GSave());
        // 将表单放置在 x=100 y=500 坐标位置
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        // 使用 Do 操作符绘制表单
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        pageContents.add(new GSave());

        // 将表单放置在 x=100 y=300 坐标位置
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 300));

        // 使用 Do 操作符绘制表单
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        // // 在 GSave 之后使用 GRestore 恢复图形状态
        pageContents.add(new GRestore());
        pdfDocument.save(outFile);
    }
```


## 使用操作符类移除图形对象

操作符类为PDF操作提供了强大的功能。当PDF文件包含无法使用[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)类的[DeleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--)方法移除的图形时，可以使用操作符类来移除它们。

以下代码片段展示了如何移除图形。请注意，如果PDF文件包含图形的文本标签，使用这种方法它们可能会保留在PDF文件中。因此，搜索图形操作符以找到删除此类图像的替代方法。

```java
    public static void RemoveGraphicsOpeartors() {
        Document pdfDocument  = new Document(_dataDir+ "RemoveGraphicsObjects.pdf");
        Page page = pdfDocument.getPages().get_Item(2);
        OperatorCollection oc = page.getContents();

        // 使用路径绘制操作符
        Operator[] operators = new Operator[] {
                new Stroke(),
                new ClosePathStroke(),
                new Fill()
        };

        oc.delete(operators);
        pdfDocument.save(_dataDir+ "No_Graphics_out.pdf");
    }
```


## 更改PDF文档的颜色空间

{{% alert color="primary" %}}

Aspose.PDF for Java 9.0.0 支持更改PDF文档的颜色空间。可以将RGB颜色更改为CMYK，反之亦然。

{{% /alert %}}

在 [Operator](https://reference.aspose.com/java/pdf/com.aspose.pdf/Operator) 类中实现了以下方法，以允许您更改颜色空间。使用它可以将某些特定的RGB/CMYK颜色更改为CMYK/RGB颜色空间，保持其余的PDF文档不变。

{{% alert color="primary" %}}
**公共API更改**
实现了以下方法：

- com.aspose.pdf.Operator.SetRGBColorStroke.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetRGBColor.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetCMYKColorStroke.getRGBColor(new double[4], new double[3])
- com.aspose.pdf.Operator.SetCMYKColor.getRGBColor(new double[4], new double[3])

{{% /alert %}}

以下代码片段演示了如何使用Aspose.PDF for Java更改颜色空间。

```java
Document doc = new Document("input_color.pdf");
OperatorCollection contents = doc.getPages().get_Item(1).getContents();
System.out.println("PDF 文档中 RGB 颜色操作符的值");
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetRGBColor || oper instanceof Operator.SetRGBColorStroke)
        try {
            // 将 RGB 转换为 CMYK 颜色
            System.out.println(oper.toString());

            double[] rgbFloatArray = new double[] { Double.valueOf(oper.getParameters().get(0).toString()), Double.valueOf(oper.getParameters().get(1).toString()), Double.valueOf(oper.getParameters().get(2).toString()), };
            double[] cmyk = new double[4];
            if (oper instanceof Operator.SetRGBColor) {
                ((Operator.SetRGBColor) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColor(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else if (oper instanceof Operator.SetRGBColorStroke) {
                ((Operator.SetRGBColorStroke) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColorStroke(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else
                throw new java.lang.Throwable("不支持的命令");

        } catch (Throwable e) {
            e.printStackTrace();
        }
}
doc.save("input_colorout.pdf");

// 测试结果
System.out.println("结果 PDF 文档中转换后的 CMYK 颜色操作符的值");
doc = new Document("input_colorout.pdf");
contents = doc.getPages().get_Item(1).getContents();
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetCMYKColor || oper instanceof Operator.SetCMYKColorStroke) {
        System.out.println(oper.toString());
    }
}
```