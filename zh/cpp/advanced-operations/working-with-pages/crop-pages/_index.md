---
title: 使用 C++ 编程裁剪 PDF 页面
linktitle: 裁剪页面
type: docs
weight: 80
url: /zh/cpp/crop-pages/
description: 您可以使用 Aspose.PDF for C++ 获取页面属性，例如宽度、高度、出血框、裁剪框和修整框。
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 获取页面属性

PDF 文件中的每一页都有多个属性，例如宽度、高度、出血框、裁剪框和修整框。Aspose.PDF 允许您访问这些属性。

- **媒体框**: 媒体框是最大的页面框。它对应于将文档打印到 PostScript 或 PDF 时选择的页面大小（例如 A4、A5、美国信纸等）。换句话说，媒体框决定了显示或打印 PDF 文档的媒体的物理大小。
- **出血框**: 如果文档有出血，PDF 也将有一个出血框。 出血是指超出页面边缘的颜色（或艺术作品）的量。它用于确保当文档被打印和裁剪到尺寸（“修剪”）时，油墨会一直延伸到页面的边缘。即使页面裁剪不当 - 略微偏离修剪标记 - 页面上也不会出现白色边缘。
- **修剪框**：修剪框指示文档在打印和修剪后的最终尺寸。
- **艺术框**：艺术框是围绕文档中页面实际内容绘制的框。当在其他应用程序中导入PDF文档时使用此页面框。
- **裁剪框**：裁剪框是您的PDF文档在Adobe Acrobat中显示的“页面”尺寸。在正常视图中，Adobe Acrobat中仅显示裁剪框的内容。有关这些属性的详细描述，请阅读Adobe.Pdf规范，特别是10.10.1页面边界。
- **Page.Rect**：MediaBox和DropBox的交集（通常为可见矩形）。 下面的图片展示了这些属性。  
有关详细信息，请访问[此页面](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)。

下面的代码片段展示了如何裁剪页面：

```cpp
void CropPagesPDF()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("crop_page.pdf");
    String outputFileName("crop_page_out.pdf");

    // 打开源文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    Console::WriteLine(document->get_Pages()->idx_get(1)->get_CropBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_TrimBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_ArtBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_BleedBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_MediaBox());

    // 创建新的矩形框
    auto newBox = MakeObject<Rectangle>(200, 220, 2170, 1520);
    document->get_Pages()->idx_get(1)->set_CropBox(newBox);
    document->get_Pages()->idx_get(1)->set_TrimBox(newBox);
    document->get_Pages()->idx_get(1)->set_ArtBox (newBox);
    document->get_Pages()->idx_get(1)->set_BleedBox (newBox);

    // 保存更新后的文档
    document->Save(_dataDir + outputFileName);
}
```
In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.  
在这个例子中，我们使用了一个示例文件[在这里](crop_page.pdf)。最初我们的页面看起来如图1所示。  
![Figure 1. Cropped Page](crop_page.png)

After the change, the page will look like Figure 2.  
更改后，页面将如图2所示。  
![Figure 2. Cropped Page](crop_page2.png)