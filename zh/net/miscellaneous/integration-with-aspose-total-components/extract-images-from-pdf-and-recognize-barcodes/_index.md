---
title: 从PDF提取图像并识别条形码
type: docs
weight: 20
url: zh/net/extract-images-from-pdf-and-recognize-barcodes/
---

{{% alert color="primary" %}}

PDF文档通常包括文本、图像、表格、附件、图表、注释以及其他相关对象。有些情况下，PDF文件内嵌入了条形码，一些客户需要识别PDF文件中存在的条形码。以下文章解释了如何从PDF页面提取图像以及如何识别其中的条形码的步骤。

{{% /alert %}}

根据Aspose.PDF for .NET的文档对象模型，一个PDF文件包含一个或多个页面，每个页面包含图像、表单和字体在资源对象中的集合。
根据 Aspose.PDF for .NET 的文档对象模型，一个 PDF 文件包含一个或多个页面，每个页面包含图像、表单和字体的资源对象集合。

**C#**

```csharp
//打开文档
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// 遍历 PDF 文件的各个页面
for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
{
    // 遍历从 PDF 页面提取的每个图像
    foreach (XImage xImage in pdfDocument.Pages[pageCount].Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            //保存输出图像
            xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
   
            // 将流位置设置到流的开始
            imageStream.Position = 0;
   
            // 实例化 BarCodeReader 对象
            Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
   
            while (barcodeReader.Read())
            {
                // 从条形码图像获取条形码文本
                string code = barcodeReader.GetCodeText();
   
                // 将条形码文本写入控制台输出
                Console.WriteLine("BARCODE : " + code);
            }
   
            // 关闭 BarCodeReader 对象以释放图像文件
            barcodeReader.Close();
        }
    }
}
```

有关本文所涵盖主题的更多详细信息，请访问以下链接：

- [从PDF文件提取图片](/net/extract-images-from-the-pdf-file/)
- [读取条形码](https://docs.aspose.com/barcode/net/read-barcodes/)
