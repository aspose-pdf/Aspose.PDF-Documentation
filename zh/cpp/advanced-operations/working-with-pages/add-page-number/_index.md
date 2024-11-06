---
title: 向PDF添加页码使用C++
linktitle: 添加页码
type: docs
weight: 100
url: zh/cpp/add-page-number/
description: Aspose.PDF for C++允许您使用PageNumber Stamp类向PDF文件添加页码戳。
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 如何向现有PDF添加页码

所有文档都必须有页码。页码使读者更容易定位文档的不同部分。
**Aspose.PDF for C++**允许您使用PageNumberStamp添加页码。

以下步骤和示例代码说明了如何使用[PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp)页面元素自动向PDF添加页码标签。

向现有PDF文档添加页码的步骤：

为了添加页码戳，您需要使用所需属性创建一个[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象和一个[PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp)对象。

在此之后，您可以调用 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 的 [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) 方法在 PDF 中添加印章。

您还可以设置页码印章的字体属性。

下面的代码片段向您展示了如何在 PDF 文件中添加页码。

```cpp
void AddPageNumberToPDF() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("PageNumberStamp.pdf");
    String outputFileName("PageNumberStamp_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 创建页码印章
    auto pageNumberStamp = MakeObject<PageNumberStamp>();
    //// 印章是否为背景
    //pageNumberStamp.Background = false;
    //pageNumberStamp.Format = "Page # of " + pdfDocument.Pages.Count;
    //pageNumberStamp.BottomMargin = 10;
    //pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
    //pageNumberStamp.StartingNumber = 1;

    //// 设置文本属性
    //pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
    //pageNumberStamp.TextState.FontSize = 14.0F;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
    //pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

    // 将印章添加到特定页面
    document->get_Pages()->idx_get(1)->AddStamp(pageNumberStamp);

    // 保存输出文档
    document->Save(_dataDir+ outputFileName);
}
```

## 现场示例

[添加 PDF 页码](https://products.aspose.app/pdf/page-number) 是一个免费的在线网络应用程序，允许您研究添加页码功能的工作原理。

[![如何使用 C++ 在 PDF 中添加页码](page_number.png)](https://products.aspose.app/pdf/page-number)

## 添加/删除 Bates 编号

**Bates 编号**（也称为 Bates 印记）用于法律、医疗和商业领域，在图像和文档扫描或处理时放置识别号码和/或日期/时间标记，例如在审判准备的发现阶段或识别商业收据时。此过程提供图像或文档的识别、保护和自动连续编号。

Aspose.PDF 目前对 Bates 编号的支持有限。此功能将根据客户的要求进行更新。

### 如何删除 Bates 编号

```cpp
void WorkingWithPages::RemoveBatesNubmering()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("BatesNumbering.pdf");
    String outputFileName("BatesNumbering_out.pdf");
    String customSubtype("BatesN");
    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    for (auto page : document->get_Pages())
    {
        auto coll = page->get_Artifacts();
        for (auto batesNum : coll)
        {
        if (batesNum->get_CustomSubtype() == customSubtype)
            page->get_Artifacts()->Delete(batesNum);
        }
    }

    // 保存输出文档
    document->Save(_dataDir + outputFileName);
}
```