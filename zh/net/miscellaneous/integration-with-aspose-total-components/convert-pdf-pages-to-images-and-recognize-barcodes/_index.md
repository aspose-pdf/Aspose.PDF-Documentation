---
title: 将PDF页面转换为图像并识别条形码
type: docs
weight: 10
url: /zh/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---

{{% alert color="primary" %}}

PDF文档通常包含文本、图像、表格、附件、图表、注释和其他对象。我们的一些客户需要在文档中嵌入条形码，然后在PDF文件中识别这些条形码。以下文章解释了如何将PDF文件中的页面转换为图像，并使用Aspose.Barcode for .NET识别图像中的条形码。

{{% /alert %}}
### **转换页面为图像并识别条形码**

{{% alert color="primary" %}}

Aspose.PDF for .NET是一个非常强大的PDF文档管理产品。它可以轻松地将PDF文档中的页面转换为图像。Aspose.BarCode for .NET同样是一个功能强大的产品，用于生成和识别条形码。
{{% /alert %}}

类PdfConverter位于Aspose.PDF.Facades命名空间下，支持将PDF页面转换为各种图像格式。
#### **使用 Aspose.PDF.Facades**

{{% alert color="primary" %}}

PdfConverter 类包含一个名为 GetNextImage 的方法，该方法从当前 PDF 页面生成图像。为了指定输出图像格式，这个方法接受来自 System.Drawing.Imaging.ImageFormat 枚举的参数。
{{% /alert %}}

Aspose.Barcode 包含一个命名空间，BarCodeRecognition，其中包含 BarCodeReader 类。BarCodeReader 类允许您从图像文件读取、确定和识别条形码。

为了本示例的目的，首先使用 Aspose.PDF.Facades.PdfConverter 将 PDF 文件中的一页转换为图像。
##### **编程示例**
**C#**

{{< highlight csharp >}}

 //创建一个PdfConverter对象

PdfConverter converter = new PdfConverter();

//绑定输入的PDF文件

converter.BindPdf("Source.pdf");

//指定要处理的起始页码

converter.StartPage = 1;

//指定要处理的结束页码

converter.EndPage = 1;

//创建一个Resolution对象，以指定结果图像的分辨率

converter.Resolution = new Aspose.PDF.Devices.Resolution(300);

//初始化转换过程

converter.DoConvert();

//创建一个MemoryStream对象，用来保存生成的图像

MemoryStream imageStream = new MemoryStream();

//检查是否存在页面，然后逐一转换成图像

while (converter.HasNextImage())

{

    //在给定的图像格式中保存图像

    converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

    //将流的位置设置到流的开始处

// 将流位置设置为流的开始

imageStream.Position = 0;

// 实例化一个BarCodeReader对象

Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

// String txtResult.Text = "";

while (barcodeReader.Read())

{

    // 从条形码图像获取条形码文本

    string code = barcodeReader.GetCodeText();

    // 将条形码文本写入控制台输出

    Console.WriteLine("BARCODE : " + code);

}

// 关闭BarCodeReader对象以释放图像文件

barcodeReader.Close();

}

// 关闭PdfConverter实例并释放资源

converter.Close();

// 关闭保存图像对象的流

imageStream.Close();

{{< /highlight >}}

{{% alert color="primary" %}}

在上述代码片段中，输出图像被保存到一个MemoryStream对象中。
```
在上述代码片段中，输出图像被保存到一个 MemoryStream 对象中。

{{% /alert %}}

{anchor:devices]
#### **使用 PngDevice 类**
在 Aspose.PDF.Devices 中，有一个 PngDevice 类。此类允许您将 PDF 文档中的页面转换为 PNG 图像。

为了本示例，将源 PDF 文件加载到 Document 中，并将文档的页面转换为 PNG 图像。当图像被创建后，使用 Aspose.BarCodeRecognition 下的 BarCodeReader 类来识别并读取图像中的条形码。

{{% alert color="primary" %}}

这里给出的代码示例通过遍历 PDF 文档的页面，并尝试在每个页面上识别条形码。

{{% /alert %}}
##### **编程示例**
**C#**

{{< highlight csharp >}}

 //打开 PDF 文档

Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// 遍历 PDF 文件的各个页面

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)

{

    using (MemoryStream imageStream = new MemoryStream())

使用 (MemoryStream imageStream = new MemoryStream())
{
    // 创建一个分辨率对象
    Aspose.PDF.Devices.Resolution resolution = new Aspose.PDF.Devices.Resolution(300);

    // 实例化一个 PngDevice 对象，并将分辨率对象作为参数传递给其构造函数
    Aspose.PDF.Devices.PngDevice pngDevice = new Aspose.PDF.Devices.PngDevice(resolution);

    // 转换特定页面并将图像保存到流中
    pngDevice.Process(pdfDocument.Pages[pageCount], imageStream);

    // 将流的位置设置到流的开始
    imageStream.Position = 0;

    // 实例化一个 BarCodeReader 对象
    Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

    // String txtResult.Text = "";

    while (barcodeReader.Read())
    {
        // 从条形码图像中获取条形码文本
        string code = barcodeReader.GetCodeText();
    }
}
```
```csharp
string code = barcodeReader.GetCodeText();

// 将条形码文本写入控制台输出

Console.WriteLine("BARCODE : " + code);

}

// 关闭BarCodeReader对象以释放图像文件

barcodeReader.Close();

}

}
```

{{< /highlight >}}

{{% alert color="primary" %}}
有关本文所涵盖主题的更多信息，请访问：

- 将PDF页面转换为不同图像格式（Facades）
- 将所有PDF页面转换为PNG图像
- [读取条形码](https://docs.aspose.com/barcode/net/read-barcodes/)

{{% /alert %}}
