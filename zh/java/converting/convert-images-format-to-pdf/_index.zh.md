---
title: 将各种图像格式转换为PDF
linktitle: 将图像转换为PDF
type: docs
weight: 60
url: /java/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: 本主题向您展示如何使用Aspose.PDF for Java库将各种图像格式转换为PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for Java** 允许您将不同格式的图像转换为PDF文件。我们的库展示了转换最流行图像格式的代码片段，例如 - BMP、CGM、DICOM、EMF、JPG、PNG、SVG和TIFF格式。

## 将BMP转换为PDF

使用 **Aspose.PDF for Java** 库将BMP文件转换为PDF文档。

<abbr title="Bitmap Image File">BMP</abbr> 图像是扩展名为.BMP的文件，表示用于存储位图数字图像的位图图像文件。这些图像独立于图形适配器，也称为设备独立位图（DIB）文件格式。您可以使用Aspose.PDF for Java API将BMP转换为PDF。
 因此，您可以遵循以下步骤将 BMP 图像转换为 PDF：

1. 初始化一个新的 Document
1. 加载示例 BMP 图像文件
1. 最后，保存输出的 PDF 文件

因此，下面的代码片段遵循这些步骤，并展示了如何使用 Java 将 BMP 转换为 PDF：

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertBMPtoPDF {

    private ConvertBMPtoPDF() {
    }

    private static Path _dataDir = Paths.get("<set path to samples>");

    public static void main(String[] args) throws FileNotFoundException {
        // 初始化文档对象
        Document document = new Document();

        Page page = document.getPages().add();        
        Image image = new Image();
        
        // 加载示例 BMP 图像文件
        image.setFile(Paths.get(_dataDir.toString(), "Sample.bmp").toString());
        page.getParagraphs().add(image);
        
        // 保存输出的 PDF 文档
        document.save(Paths.get(_dataDir.toString(),"BMPtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**尝试在线将 BMP 转换为 PDF**

Aspose 为您提供在线免费应用程序 ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 BMP 转换为 PDF](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## 将 CGM 转换为 PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> 是一个 ISO 标准，提供了一种基于矢量的 2D 图像文件格式，用于存储和检索图形信息。CGM 是一种设备无关格式。CGM 是一种矢量图形格式，支持三种不同的编码方法：二进制（最适合程序读取速度）、基于字符（生成最小的文件大小并允许更快的数据传输）或明文编码（允许用户使用文本编辑器读取和修改文件）

以下代码片段向您展示了如何使用 Aspose.PDF for Java 将 CGM 文件转换为 PDF 格式。

1. 创建一个 [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) 类。
1. 创建一个带有指定源文件名和选项的 [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) 类的实例。
1. 使用期望的文件名保存文档。

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertCGMtoPDF {

    private ConvertCGMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // 创建一个 CGM LoadOptions
        CgmLoadOptions options = new CgmLoadOptions();

        // 初始化文档对象
        String cgmFileName = Paths.get(_dataDir.toString(), "corvette.cgm").toString();
        Document document = new Document(cgmFileName, options);

        // 保存输出 PDF 文档
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


## 将 DICOM 转换为 PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> 是用于处理、存储、打印和传输医学影像信息的标准。它包括一个文件格式定义和一个网络通信协议。

Aspose.PDF for Java 允许您将 DICOM 文件转换为 PDF 格式，请查看下一个代码片段：

1. 将图像加载到流中
1. 初始化 [文档对象](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. 加载示例 DICOM 图像文件
1. 保存输出 PDF 文档

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertDICOMtoPDF {

    private ConvertDICOMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // 将图像加载到流中
        FileInputStream imageStream = new FileInputStream(
            new java.io.File(Paths.get(_dataDir.toString(),"0002.dcm").toString()));

        // 初始化文档对象
        Document document = new Document();
        document.getPages().add();
        
        // 加载示例 DICOM 图像文件
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setImageStream(imageStream);

        document.getPages().get_Item(1).getParagraphs().add(image);

        // 保存输出 PDF 文档
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**尝试在线将 DICOM 转换为 PDF**

Aspose 向您推出在线免费应用程序 ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)，您可以在此尝试调查其功能和质量。

[![Aspose.PDF 转换 DICOM 到 PDF 使用免费应用程序](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## 将 EMF 转换为 PDF

增强图元文件格式 (<abbr title="增强图元文件格式">EMF</abbr>) 存储设备独立的图形图像。EMF 的图元文件由按时间顺序排列的可变长度记录组成，可以在任何输出设备上解析后呈现存储的图像。

我们有几种方法可以将 EMF 转换为 PDF。

## 使用 Image 类

PDF 文档由页面组成，每个页面包含一个或多个段落对象。段落可以是文本、图像、表格、浮动框、图形、标题、表单字段或附件。

要将图像文件转换为 PDF 格式，请将其封闭在段落中。

可以在本地硬盘的物理位置、在网页URL或在Stream实例中转换图像。

要添加图像：

1. 创建一个com.aspose.pdf.Image类的对象。
2. 将图像添加到页面实例的[Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs)集合中。
3. 指定图像的路径或来源。
    - 如果图像在硬盘上的某个位置，使用[Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image)方法指定路径位置。
    - 如果图像放在FileInputStream中，将持有图像的对象传递给[Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image)方法。

以下代码片段显示了如何加载图像对象，设置页面边距，将图像放置在页面上，并将输出保存为PDF。

```java
package com.aspose.pdf.examples;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;

/**
 * 将EMF转换为PDF
 */

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;

public final class ConvertEMFtoPDF {

    private ConvertEMFtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        convertEMFtoPDF_01();
        convertEMFtoPDF_02();
    }

    

    public static void convertEMFtoPDF_01() throws FileNotFoundException {                
        // 实例化Document对象
        Document doc = new Document();
        // 向文档的页面集合中添加一个页面
        Page page = doc.getPages().add();
        // 将源图像文件加载到Stream对象
        java.io.FileInputStream fs = new java.io.FileInputStream(
            Paths.get(_dataDir.toString(),"source.emf").toString());

        // 设置边距以便适应图像等
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);

        page.setCropBox(new Rectangle(0, 0, 400, 400));
        // 创建图像对象
        Image image1 = new Image();
        // 将图像添加到段落集合中
        page.getParagraphs().add(image1);
        // 设置图像文件流
        image1.setImageStream(fs);
        // 保存生成的PDF文件
        doc.save("EMFtoPDF_01.pdf");
    }   
    public static void convertEMFtoPDF_02() throws IOException {
        // 查看下面的代码
    } 
}
```


### 从 BufferedImage 添加图像

Aspose.PDF for Java 还提供了从 Stream 实例加载图像的功能，其中图像可以加载到 BufferedImage 对象中，并可以放置在 Pdf 文件的段落集合中。

```java
public static void convertEMFtoPDF_02() throws IOException {    
    Document doc = new Document();
    // 向 Pdf 文件的页面集合中添加一个页面
    Page page = doc.getPages().add();
    // 创建图像实例
    Image image1 = new Image();
    // 创建 BufferedImage 实例
    java.awt.image.BufferedImage bufferedImage = ImageIO.read(new File("source.emf"));
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    // 将缓冲图像写入 OutputStream 实例
    ImageIO.write(bufferedImage, "emf", baos);
    baos.flush();
    ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
    // 将图像添加到第一页的段落集合中
    page.getParagraphs().add(image1);
    // 设置图像流为持有缓冲图像的 OutputStream
    image1.setImageStream(bais);
    // 保存生成的 PDF 文件
    doc.save("BufferedImage.pdf");
}
```


## 使用 PDF 操作符添加图像

每个 PDF 页面对象都包含 [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) 和 [getContents()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getContents--) 方法。资源可以是图像和表单，而内容则由一组 PDF 操作符表示。每个操作符都有其名称和参数。

此示例使用操作符向 PDF 文件添加图像。

要向现有 PDF 文件添加图像：

1. 创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象并打开输入的 PDF 文档。
1. 获取要添加图像的页面。
1. 将图像添加到页面的 [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) 集合中。
1. 使用操作符将图像放置在页面上：
   1. 使用 GSave 操作符保存当前图形状态。
   1. 使用 ConcatenateMatrix 操作符指定图像放置的位置。

1. 使用 Do 操作符在页面上绘制图像。
   1. 最后，使用 GRestore 操作符保存更新的图形状态。
1. 保存文件。

以下代码片段展示了如何将图像添加到 PDF 文档中。

```java
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.Pdf-for-Java
// 打开文档
Document pdfDocument1 = new Document("input.pdf");

// 设置坐标
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// 获取要添加图像的页面
Page page = pdfDocument1.getPages().get_Item(1);

// 将图像加载到流中
java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));

// 将图像添加到页面资源的 Images 集合中
page.getResources().getImages().add(imageStream);

// 使用 GSave 操作符：该操作符保存当前图形状态
page.getContents().add(new Operator.GSave());

// 创建 Rectangle 和 Matrix 对象
Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

// 使用 ConcatenateMatrix (连接矩阵) 操作符：定义图像的放置方式
page.getContents().add(new Operator.ConcatenateMatrix(matrix));
XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

// 使用 Do 操作符：该操作符绘制图像
page.getContents().add(new Operator.Do(ximage.getName()));

// 使用 GRestore 操作符：该操作符恢复图形状态
page.getContents().add(new Operator.GRestore());

// 保存新的 PDF
pdfDocument1.save("Updated_document.pdf");

// 关闭图像流
imageStream.close();
```


{{% alert color="success" %}}
**尝试将 EMF 在线转换为 PDF**

Aspose 为您提供在线免费应用程序 ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/)，您可以在此尝试研究其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 EMF 转换为 PDF](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## 转换 JPG 为 PDF

无需再疑惑如何将 JPG 转换为 PDF，因为 Apose.PDF for Java 库有最佳的解决方案。

使用 Aspose.PDF for Java 可以非常轻松地将 JPG 图像转换为 PDF，步骤如下：

1. 初始化 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类的对象
1. 加载 JPG 图像并添加到段落
1. 保存输出 PDF

下面的代码片段展示了如何使用 Java 将 JPG 图像转换为 PDF：

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertJPEGtoPDF {

    private static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // 初始化文档对象
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // 加载示例 JPEG 图像文件
        image.setFile(Paths.get(_dataDir.toString(), "Sample.jpg").toString());
        page.getParagraphs().add(image);

        // 保存输出 PDF 文档
        document.save(Paths.get(_dataDir.toString(),"JPEGtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**尝试在线将 JPG 转换为 PDF**

Aspose 为您提供了在线免费的 ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/) 应用程序，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 JPG 转换为 PDF](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## 将 PNG 转换为 PDF

**Aspose.PDF for Java** 支持将 PNG 图像转换为 PDF 格式的功能。查看下一个代码片段以实现您的任务。

<abbr title="可移植网络图形">PNG</abbr> 指的是一种使用无损压缩的光栅图像文件格式，这使得它在用户中很受欢迎。

您可以使用以下步骤将 PNG 转换为 PDF 图像：

1. 加载输入 PNG 图像
1. 读取高度和宽度值
1. 创建新文档并添加页面
1. 设置页面尺寸
1. 保存输出文件

此外，下面的代码片段展示了如何在您的 Java 应用程序中将 PNG 转换为 PDF：

```java
package com.aspose.pdf.examples;

/**
 * 将 PNG 转换为 PDF
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPNGtoPDF {

    private ConvertPNGtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // 初始化文档对象
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // 加载示例 BMP 图像文件
        image.setFile(Paths.get(_dataDir.toString(), "Sample.png").toString());

        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getParagraphs().add(image);

        // 保存输出 PDF 文档
        document.save(Paths.get(_dataDir.toString(), "PNGtoPDF.pdf").toString());
    }
}

```


{{% alert color="success" %}}
**尝试在线将PNG转换为PDF**

Aspose为您提供在线免费应用程序["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将PNG转换为PDF](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## 将SVG转换为PDF

可缩放矢量图形 (SVG) 是一种基于XML的二维矢量图形文件格式的规格家族，包含静态和动态（交互或动画）的图形。SVG规格是一个开放标准，自1999年以来一直由万维网联盟 (W3C) 开发。

SVG图像及其行为在XML文本文件中定义。
 这意味着它们可以被搜索、索引、脚本化，如果需要，还可以被压缩。作为XML文件，SVG图像可以用任何文本编辑器创建和编辑，但通常使用诸如Inkscape这样的绘图程序来创建它们更加方便。

## 如何将SVG文件转换为PDF格式

要将SVG文件转换为PDF，请使用名为[SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions)的类，该类用于初始化[LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions)对象。随后，此对象在[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)对象初始化过程中作为参数传递，并帮助PDF渲染引擎确定源文档的输入格式。

以下代码片段显示了将SVG文件转换为PDF格式的过程。

```java
// 初始化文档对象

String pdfDocumentFileName = Paths.get(_dataDir.toString(), "svg_test.pdf").toString();
String svgDocumentFileName = Paths.get(_dataDir.toString(), "car.svg").toString();

SvgLoadOptions option = new SvgLoadOptions();
Document pdfDocument = new Document(svgDocumentFileName, option);
pdfDocument.save(pdfDocumentFileName);
```

{{% alert color="success" %}}
**尝试在线将SVG格式转换为PDF**

Aspose.PDF for Java 为您提供免费的在线应用程序 ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 SVG 到 PDF 免费应用](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## 转换TIFF为PDF

**Aspose.PDF for Java** 文件格式支持，无论是单帧还是多帧<abbr title="标记图像文件格式">TIFF</abbr>图像。这意味着您可以在Java应用程序中将TIFF图像转换为PDF。

TIFF或TIF，标记图像文件格式，代表用于多种符合此文件格式标准的设备的光栅图像。
 TIFF 图像可以包含多个帧，每个帧有不同的图像。Aspose.PDF 文件格式也被支持，无论是单帧还是多帧 TIFF 图像。所以你可以在你的 Java 应用程序中将 TIFF 图像转换为 PDF。因此，我们将考虑一个将多页 TIFF 图像转换为多页 PDF 文档的示例，步骤如下：

1. 实例化 Document 类的一个实例
1. 加载输入的 TIFF 图像
1. 最后，将图像保存为 PDF 页面

此外，下面的代码片段展示了如何将多页或多帧的 TIFF 图像转换为 PDF：

```java
import com.aspose.pdf.Document;
import com.aspose.pdf.Image;
import com.aspose.pdf.Page;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * 将 TIFF 转换为 PDF。
 */
public final class ConvertTIFFtoPDF {

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertTIFFtoPDF() {
    }

    public static void run() throws IOException {
        // 初始化文档对象
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        image.setFile(Paths.get(DATA_DIR.toString(), "Sample.tiff").toString());
        page.getParagraphs().add(image);

        // 保存输出 PDF 文档
        document.save(Paths.get(DATA_DIR.toString(), "TIFFtoPDF.pdf").toString());
        document.close();
    }    
}
```