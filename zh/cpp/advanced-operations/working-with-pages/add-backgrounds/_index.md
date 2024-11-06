---
title: 使用C++为PDF添加背景
linktitle: 添加背景
type: docs
weight: 110
url: zh/cpp/add-backgrounds/
descriptions: 使用C++将背景图像添加到PDF文件。使用BackgroundArtifact对象。
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

为PDF文件添加背景有助于提高文档的整体可读性。PDF中的内容更具吸引力，如果文档外观良好，读者将会注意到。背景也可以用来突出PDF的亮点。

可以使用背景图像为文档添加水印或其他细微设计。在Aspose.PDF for C++中，每个PDF文档是一个页面的集合，每个页面包含一个工件的集合。[BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact)类可用于向页面对象添加背景图像。

以下代码片段展示了如何使用C++中的BackgroundArtifact对象向PDF页面添加背景图像。

```cpp
void WorkingWithPages::AddBackgrounds()
{
    String _dataDir("C:\\Samples\\");

    // 创建一个新的 Document 对象
    auto document = MakeObject<Document>();

    // 向文档对象添加一个新页面
    auto page = document->get_Pages()->Add();

    // 创建 Background Artifact 对象
    auto background = MakeObject<BackgroundArtifact>();

    // 为 backgroundartifact 对象指定图像
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // 将 backgroundartifact 添加到页面的 artifacts 集合中
    page->get_Artifacts()->Add(background);

    // 保存文档
    document->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```