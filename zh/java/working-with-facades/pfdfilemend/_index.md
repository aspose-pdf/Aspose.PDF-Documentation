---

title: PdfFileMend 类
type: docs
weight: 20
url: zh/java/pdffilemend-class/
description: 本节介绍如何使用 PdfFileMend 类处理 Aspose.PDF Facades。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

插入 [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) 到 PDF 文档中似乎不是一项困难的任务，前提是您拥有该文档的原始可编辑版本。假设您创建了一个文档，然后想起需要添加另一行或者我们讨论的是更大体积的文档，在这两种情况下，Aspose.PDF Facades 都会帮助您。让我们考虑使用 [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend) 类在现有 PDF 文件中添加文本的可能性。

## 在现有 PDF 文件中添加文本 (facades)

我们可以通过几种方式添加文本。
 考虑第一个。我们获取[FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText)并将其添加到页面中。之后，我们指明左下角的坐标，然后将文本添加到页面。

```java
    public static void AddText01()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("欢迎来到 Aspose!");

        mender.AddText(message, 1, 10, 750);

        // 保存输出文件
        mender.Save(_dataDir + "PdfFileMend01_output.pdf");
    }
```

检查它的外观：

![Add Text](/pdf/net/images/add_text.png)

第二种添加[FormattedText](https://reference.aspose.com/pdf//java/com.aspose.pdf.facades/formattedtext)的方法。此外，我们指明一个矩形，文本应该适合其中。

```java
public static void AddText02()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("欢迎来到 Aspose! 欢迎来到 Aspose!");

        mender.AddText(message, 1, 10, 700, 55, 810);
        mender.WrapMode = WordWrapMode.ByWords;

        // 保存输出文件
        mender.Save(_dataDir + "PdfFileMend02_output.pdf");
    }
```

第三个示例提供了向指定页面添加文本的功能。在我们的示例中，让我们在文档的第1页和第3页添加一个标题。

```java
public static void AddText03()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(document);
        FormattedText message = new FormattedText("欢迎使用Aspose!");
        int[] pageNums = new int[] { 1, 3 };
        mender.AddText(message, pageNums, 10, 750, 310, 760);

        // 保存输出文件
        mender.Save(_dataDir + "PdfFileMend03_output.pdf");
    }
```

## 在现有PDF文件中添加图像（facades）

你是否曾尝试在现有的PDF文件中添加图像？
 我们确信您知道这不是一项简单的任务。也许您正在在线填写表格，并且需要附上一张用于识别的照片，或者将您的照片附加到现有的简历上。以前，这样的任务是通过创建照片、将其附加到文档、进一步扫描和发送来解决的。这个过程非常麻烦且耗时。

在现有的PDF文件中添加图像和文本是一个常见的需求，而com.aspose.pdf.facades命名空间很好地满足了这一需求。它提供了一个类[PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend)，允许您在PDF文件中添加图像。

这篇文章将向您展示如何使用com.aspose.pdf.facades将图像插入PDF。此外，还有几种将图像添加到PDF的方法。

通过设置矩形的参数将图像插入PDF文档。

```java
public static void AddImage01()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        PdfFileMend mender = new PdfFileMend();

        // 将图像加载到流中
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        mender.AddImage(imageStream, 1, 10, 650, 110, 750);

        // 保存输出文件
        mender.Save(_dataDir + "PdfFileMend04_output.pdf");
    }
```

![Add Image](/pdf/net/images/add_image1.png)

让我们考虑第二个代码片段。通过使用 [CompositingParameters](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters) 类参数的变体，我们可以获得不同的设计效果。我们尝试了其中之一。

```java
 public static void AddImage02()
    {
        Document document = new Document(_dataDir + "sample_color.pdf");
        PdfFileMend mender = new PdfFileMend();
        // 将图像加载到流中
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        int pageNum = 1;
        int lowerLeftX = 10;
        int lowerLeftY = 650;
        int upperRightX = 110;
        int upperRightY = 750;
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // 保存输出文件
        mender.Save(_dataDir + "PdfFileMend05_output.pdf");
    }
```


![Add Image](/pdf/net/images/add_image2.png)

在以下代码片段中，我们使用 [ImageFilterType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageFilterType)。ImageFilterType 指示将用于编码的流编解码器的类型，默认情况下为 Jpeg。如果您从 PNG 格式加载图像，那么它将在文档中保存为 JPEG（或我指定的其他格式）。

```java
    public static void AddImage03()
    {
        Document document = new Document(_dataDir + "sample_color.pdf");
        PdfFileMend mender = new PdfFileMend();
        // 将图像加载到流中
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        int pageNum = 1;
        int lowerLeftX = 10;
        int lowerLeftY = 650;
        int upperRightX = 110;
        int upperRightY = 750;
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // 保存输出文件
        mender.Save(_dataDir + "PdfFileMend06_output.pdf");
    }
```


在下一个代码片段中，您可以注意到 [IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--) 方法的使用。

[IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--) 是一个标志，用于指示是否对图像应用蒙版以实现原始图像的透明度

```java
public static void AddImage04()
{
    Document document = new Document(_dataDir + "sample_color.pdf");
    PdfFileMend mender = new PdfFileMend();
    // 将图像加载到流中
    var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
    mender.BindPdf(document);
    int pageNum = 1;
    int lowerLeftX = 10;
    int lowerLeftY = 650;
    int upperRightX = 110;
    int upperRightY = 750;
    CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
    mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

    // 保存输出文件
    mender.Save(_dataDir + "PdfFileMend07_output.pdf");
}
```