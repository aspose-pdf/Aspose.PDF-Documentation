---
title: 在C++中使用Artifacts
linktitle: 使用Artifacts
type: docs
weight: 110
url: zh/cpp/artifacts/
description: 本页描述了如何使用Aspose.PDF for C++处理Artifact类。代码片段展示了如何向PDF页面添加背景图像以及如何获取PDF文件第一页的每个水印。
lastmod: "2021-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 如何在PDF中获取水印？

**什么是PDF中的artifact？**

根据PDF / UA ISO参考，不重要的内容或在后台不显示的内容不携带相关信息，应该标记为artifact，以便辅助技术可以忽略它。
如果在创建程序中无法识别artifact，则必须使用Aspose.PDF for C++手动完成此操作。

[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) 类包含以下属性：

- **Artifact.Type** – 获取artifact类型（支持Artifact.ArtifactType枚举的值，其中值包括Background, Layout, Page, Pagination和Undefined）。
- **Artifact.Subtype** – 获取工件子类型（支持Artifact.ArtifactSubtype枚举的值，其中包括Background, Footer, Header, Undefined, Watermark）。

{{% alert color="primary" %}}

请注意，使用Adobe Acrobat创建的水印类型为Pagination，子类型为Watermark。

{{% /alert %}}

- **Artifact.Contents** – 获取工件内部操作符的集合。其支持的类型为System.Collections.ICollection。
- **Artifact.Form** – 获取工件的XForm（如果使用了XForm）。水印、页眉和页脚工件包含显示所有工件内容的XForm。
- **Artifact.Image** – 获取工件的图像（如果图像存在，否则为空）。
- **Artifact.Text** – 获取工件的文本。
- **Artifact.Rectangle** – 获取页面上工件的位置。
- **Artifact.Rotation** – 获取工件的旋转（以度为单位，正值表示逆时针旋转）。
- **Artifact.Opacity** – 获取工件的不透明度。 可能的取值范围是0...1，其中1是完全不透明。

为了在PDF文件中处理工件的示例，我们来看一个水印。

使用Adobe Acrobat支持创建的水印被称为工件（如14.8.2.2节“当前内容和PDF规范工件”中所述）。为了处理工件，Aspose.PDF包含2个类：[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact)和[ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection)。

为了获取特定页面上的所有工件，[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)类具有Artifacts属性。本主题展示了如何在PDF文件中处理水印工件。

以下代码片段展示了如何使用C++获取PDF文件第一页上的每个水印：

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
void Artifacts::SetWatermark() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto artifact = MakeObject<WatermarkArtifact>();
    String text(u"WATERMARK");    
    artifact->set_Text(text);
    artifact->get_TextState()->set_ForegroundColor(Color::get_Blue());
    artifact->get_TextState()->set_FontSize(72);
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment(VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(_dataDir + u"watermark.pdf");
}
```
背景图像可以用于在 PDF 文档中添加水印或专属设计。Aspose.PDF for C++ 使用 [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) 类来为页面对象添加背景图像。

下面的代码片段展示了如何使用 BackgroundArtifact 对象向 PDF 页面添加背景图像：

```cpp
void Artifacts::SetBackground() {

    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto pdfDocument = MakeObject<Document>();

    // 向文档对象添加 MakeObject<page
    auto page = pdfDocument->get_Pages()->Add();

    // 创建背景工件对象
    auto background = MakeObject<BackgroundArtifact>();

    // 为 backgroundartifact 对象指定图像
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // 将 BackgroundArtifact 添加到页面的工件集合中
    page->get_Artifacts()->Add(background);

    // 保存修改后的 PDF
    pdfDocument->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```

### 编程示例：获取水印

以下代码片段展示了如何获取 PDF 文件第一页上的每个水印。

```cpp
void Artifacts::GettingWatermarks() {
    
    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    // 迭代并获取工件的子类型、文本和位置
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        Console::WriteLine(u"{0} {1} {2}", artifact->get_Subtype(), 
            artifact->get_Text(), artifact->get_Rectangle());
    }

}
```

### 编程示例：计算特定类型的工件

要计算特定类型的工件总数（例如，水印的总数），请使用以下代码：

```cpp
void Artifacts::CountingArtifacts() {

    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    int count = 0;
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        // 如果工件类型是水印，则增加计数器
        if (artifact->get_Subtype() == Artifact::ArtifactSubtype::Watermark) count++;
    }
    Console::WriteLine(u"Page contains {0} watermarks", count);
}
```