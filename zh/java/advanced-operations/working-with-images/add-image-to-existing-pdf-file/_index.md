---
title: 将图像添加到现有PDF文件
linktitle: 添加图像
type: docs
weight: 10
url: /zh/java/add-image-to-existing-pdf-file/
description: 本节介绍如何使用Java库将图像添加到现有PDF文件。
lastmod: "2021-06-05"
---

每个PDF页面包含资源和内容属性。资源可以是图像和表单，例如，内容由一组PDF操作符表示。每个操作符都有其名称和参数。本示例使用操作符将图像添加到PDF文件中。

要将图像添加到现有PDF文件：

- 创建一个[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象并打开输入的PDF文档。
- 获取要添加图像的页面。
- 将图像添加到页面的[getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--)集合中。
- 使用操作符将图像放置在页面上：
- 使用GSave操作符保存当前图形状态。

- 使用[ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/concatenatematrix)操作符指定图像的位置。
- 使用 [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/class-use/Do) 操作符在页面上绘制图像。
- 最后，使用 [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/grestore) 操作符保存更新后的图形状态。
- 保存文件。

以下代码片段展示了如何在 PDF 文档中添加图像。

```java
package com.aspose.pdf.examples;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfFileMend;
import com.aspose.pdf.operators.*;

public class ExampleAddImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddImageToExistingPDF() throws IOException {
        // 打开一个文档
        Document pdfDocument1 = new Document(_dataDir + "sample.pdf");

        // 设置坐标
        int lowerLeftX = 50;
        int lowerLeftY = 750;
        int upperRightX = 100;
        int upperRightY = 800;

        // 获取要添加图像的页面
        Page page = pdfDocument1.getPages().get_Item(1);

        // 将图像加载到流中
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(_dataDir + "logo.png"));

        // 将图像添加到页面资源的 Images 集合中
        page.getResources().getImages().add(imageStream);

        // 使用 GSave 操作符：此操作符保存当前图形状态
        page.getContents().add(new GSave());

        // 创建 Rectangle 和 Matrix 对象
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // 使用 ConcatenateMatrix（连接矩阵）操作符：定义图像必须如何放置
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

        // 使用 Do 操作符：此操作符绘制图像
        page.getContents().add(new Do(ximage.getName()));

        // 使用 GRestore 操作符：此操作符恢复图形状态
        page.getContents().add(new GRestore());

        // 保存新的 PDF
        pdfDocument1.save(_dataDir + "updated_document.pdf");

        // 关闭图像流
        imageStream.close();
    }
```


## 将 BufferedImage 中的图像添加到 PDF 中

从 Aspose.PDF for Java 9.5.0 开始，我们引入了从 BufferedImage 实例中添加图像到 PDF 文档的支持。为了支持这一需求，实现了一个方法：[XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection).add(BufferedImage image);

```java
    public static void AddingImageFromBufferedImageIntoPDF() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();
        page.getResources().getImages().add(originalImage);
    }
```
您可以使用任何 InputStream，而不仅仅是 FileInputStream 对象来添加图像。因此，当使用 java.io.ByteArrayInputStream 对象时，您不需要在系统上存储任何文件：

```java
    public static void AddingImageFromBufferedImageIntoPDF2() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        ByteArrayOutputStream baos = new ByteArrayOutputStream();

        Document pdfDocument = new Document();
        ImageIO.write(originalImage, "jpg", baos);
        baos.flush();
        Page page = pdfDocument.getPages().get_Item(1);
        page.getResources().getImages().add(new ByteArrayInputStream(baos.toByteArray()));
    }
```


## 在现有 PDF 文件中添加图像（Facades）

还有一种替代的、更简单的方法可以将图像添加到 PDF 文件中。您可以使用 [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend) 类的 AddImage 方法。AddImage 方法需要添加的图像、需要添加图像的页码和坐标信息。之后，使用 Close 方法保存更新后的 PDF 文件。

下面的代码片段展示了如何在现有的 PDF 文件中添加图像。

```java
    public static void AddImageInAnExistingPDFFile_Facades() {
        // 打开文档
        PdfFileMend mender = new PdfFileMend();

        // 创建 PdfFileMend 对象以添加文本
        mender.bindPdf(_dataDir + "AddImage.pdf");

        // 在 PDF 文件中添加图像
        mender.addImage(_dataDir + "aspose-logo.jpg", 1, 100, 600, 200, 700);

        // 保存更改
        mender.save(_dataDir + "AddImage_out.pdf");

        // 关闭 PdfFileMend 对象
        mender.close();
    }
```


## 在 PDF 文档中多次引用单个图像

有时我们需要在 PDF 文档中多次使用相同的图像。添加新实例会增加生成的 PDF 文档的大小。我们添加了一个新方法 XImageCollection.add(XImage)，支持将 Ximage 对象添加到 Images 集合中。此方法允许引用与原始图像相同的 PDF 对象，从而优化 PDF 文档大小。

```java
    public static void AddReferenceOfaSingleImageMultipleTimes() throws FileNotFoundException {
        Rectangle imageRectangle = new Rectangle(0, 0, 30, 15);
        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        document.getPages().add();
        java.io.FileInputStream imageStream = new java.io.FileInputStream(
                new java.io.File(_dataDir + "aspose-logo.png"));

        XImage image = null;

        for (Page page : document.getPages()) {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.getRect());
            XForm form = annotation.getAppearance().get_Item("N");
            form.setBBox(page.getRect());
            String name;
            if (image == null) {
                name = form.getResources().getImages().add(imageStream);
                image = form.getResources().getImages().get_Item(name);
            } else {
                name = form.getResources().getImages().add(image);
            }
            form.getContents().add(new GSave());
            form.getContents().add(new ConcatenateMatrix(
                    new Matrix(imageRectangle.getWidth(), 0, 0, imageRectangle.getHeight(), 0, 0)));
            form.getContents().add(new Do(name));
            form.getContents().add(new GRestore());
            page.getAnnotations().add(annotation, false);
            imageRectangle = new Rectangle(0, 0, imageRectangle.getWidth() * 1.01, imageRectangle.getHeight() * 1.01);
        }
        document.save(_dataDir + "output.pdf");
    }
```


## 确定 PDF 中的图像是彩色还是黑白

可以对图像应用不同类型的压缩来减小它们的大小。应用于图像的压缩类型取决于源图像的颜色空间，即如果图像是彩色（RGB），则应用 JPEG2000 压缩，如果是黑白，则应应用 JBIG2/JBIG2000 压缩。因此，识别每种图像类型并使用适当的压缩类型将创建最佳/优化的输出。

PDF 文件可能包含文本、图像、图形、附件、注释等元素，如果源 PDF 文件包含图像，我们可以确定图像的颜色空间并应用适当的图像压缩来减小 PDF 文件的大小。以下代码片段显示了确定 PDF 中的图像是彩色还是黑白的步骤。

```java
    public static void CheckColors() {

        Document document = new Document(_dataDir + "test4.pdf");
        try {
            // 迭代 PDF 文件的所有页面
            for (Page page : (Iterable<Page>) document.getPages()) {
                // 创建图像放置吸收器实例
                ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
                page.accept(abs);
                for (ImagePlacement ia : (Iterable<ImagePlacement>) abs.getImagePlacements()) {
                    /* ColorType */
                    int colorType = ia.getImage().getColorType();
                    switch (colorType) {
                    case ColorType.Grayscale:
                        System.out.println("灰度图像");
                        break;
                    case ColorType.Rgb:
                        System.out.println("彩色图像");
                        break;
                    }
                }
            }
        } catch (Exception ex) {
            System.out.println("读取文件时出错 = " + document.getFileName());
        }
    }
}
```