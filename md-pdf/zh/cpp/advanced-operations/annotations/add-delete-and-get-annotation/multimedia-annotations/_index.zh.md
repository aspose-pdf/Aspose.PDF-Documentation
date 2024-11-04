---
title: PDF 多媒体注释使用 C++
linktitle: 多媒体注释
type: docs
weight: 40
url: /cpp/multimedia-annotation/
description: Aspose.PDF for C++ 允许您添加、获取和删除 PDF 文档中的多媒体注释。
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

添加视频、音频和交互内容将 PDF 转变为多维度的交流工具，提高了对文档的兴趣和参与度。PDF 格式文件中的此类内容称为多媒体注释。

PDF 文档中的注释包含在 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 对象的 Annotations 集合中。此集合仅包含该单独页面的所有注释：每个页面都有其自己的 Annotations 集合。要向特定页面添加注释，请使用 Add 方法将其添加到该页面的 Annotations 集合中。

使用 Aspose.PDF.InteractiveFeatures.Annotations 命名空间中的 [ScreenAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.screen_annotation) 类将 SWF 文件作为注释包含在 PDF 文档中。 一个屏幕注释指定了页面上的一个区域，可以在其上播放媒体剪辑。

当您需要在 PDF 文档中添加外部视频链接时，可以使用 [MovieAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.movie_annotation)。电影注释包含动画图形和声音，可以在计算机屏幕上和通过扬声器呈现。

[Sound Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.sound_annotation) 类似于文本注释，但它包含从计算机麦克风录制或从文件导入的声音，而不是文本注释。当注释被激活时，声音将被播放。注释在大多数情况下应像文本注释一样表现，使用不同的图标（默认情况下是扬声器）来表明它代表声音。

然而，当需要在 PDF 文档中嵌入媒体时，您需要使用 [RichMediaAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.rich_media_annotation)。
## 添加屏幕注释

以下代码片段演示了如何向PDF文件添加屏幕注释：

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MultimediaAnnotations::AddScreenAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // 加载PDF文件
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"input.swf";

    // 创建屏幕注释
    auto screenAnnotation = MakeObject<ScreenAnnotation>(page, MakeObject<Rectangle>(170, 190, 470, 380), mediaFile);
    page->get_Annotations()->Add(screenAnnotation);

    document->Save(_dataDir + u"sample_swf.pdf");
}
```

## 添加声音注释

以下代码片段演示了如何向PDF文件添加声音注释：

```cpp
  void MultimediaAnnotations::AddSoundAnnotation()
{

    String _dataDir("C:\\Samples\\");

    // 加载PDF文件
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"file_example_WAV_1MG.wav";

    // 创建声音注释
    auto soundAnnotation = MakeObject<SoundAnnotation>(page, new Rectangle(20, 700, 60, 740), mediaFile);
    soundAnnotation->set_Color(Color::get_Blue());
    soundAnnotation->set_Title(u"John Smith");
    soundAnnotation->set_Subject(u"声音注释演示");
    soundAnnotation->set_Popup(MakeObject<PopupAnnotation>(document));

    page->get_Annotations()->Add(soundAnnotation);

    document->Save(_dataDir + u"sample_wav.pdf");
}

```

## 添加 RichMediaAnnotation

以下代码片段展示了如何向 PDF 文件添加 RichMediaAnnotation：

```cpp
       void MultimediaAnnotations::AddRichMediaAnnotation()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();

    String pathToAdobeApp (u"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins");
    auto page = document->get_Pages()->Add();

    // 为视频数据命名。此数据将以此名称嵌入到文档中，并通过此名称从 flash 变量中引用。
    // videoName 不应包含文件的路径；这只是访问 PDF 文档内部数据的“键”。

    String videoName (u"file_example_MP4_480_1_5MG.mp4");
    String posterName (u"file_example_MP4_480_1_5MG_poster.jpg");

    // 我们还使用视频播放器的皮肤
    String skinName (u"SkinOverAllNoFullNoCaption.swf");

    auto rma = MakeObject<RichMediaAnnotation>(page, MakeObject<Rectangle>(100, 500, 300, 600));

    // 在这里我们应该指定包含视频播放器代码的流
    rma->set_CustomPlayer(System::IO::File::OpenRead(pathToAdobeApp + u"Players\\" + u"Videoplayer.swf"));

    // 为播放器组成 flash 变量行。请注意，不同的播放器可能具有不同格式的 flash 变量行。
    // 请参考您播放器的文档。
    rma->set_CustomFlashVariables(u"source=" + videoName + u"&skin=" + skinName);

    // 添加皮肤代码。
    rma->AddCustomData(skinName, System::IO::File::OpenRead(pathToAdobeApp + u"SkinOverAllNoFullNoCaption.swf"));
    // 为视频设置海报
    rma->SetPoster(System::IO::File::OpenRead(_dataDir + posterName));

    // 设置视频内容
    rma->SetContent(videoName, System::IO::File::OpenRead(_dataDir + videoName));

    // 设置内容类型（视频）
    rma->set_Type(RichMediaAnnotation::ContentType::Video);

    // 点击激活播放器
    rma->set_ActivateOn(RichMediaAnnotation::ActivationEvent::Click);

    // 更新注释数据。此方法应在所有赋值/设置之后调用。此方法初始化注释的数据结构并嵌入所需的数据。
    rma->Update();

    // 在页面上添加注释。
    page->get_Annotations()->Add(rma);

    document->Save(_dataDir + u"RichMediaAnnotation.pdf");
}
```

### 获取 MultimediaAnnotation

请尝试使用以下代码片段从 PDF 文档中获取 MultimediaAnnotation。

```cpp
void MultimediaAnnotations::GetMultimediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        Console::WriteLine(u"{0} {1}", ma->get_AnnotationType(), ma->get_Rect());
    }
}
```

### 删除 MultimediaAnnotation

以下代码片段展示了如何从 PDF 文件中删除 MultimediaAnnotation。

```cpp
void MultimediaAnnotations::DeleteRichMediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        page->get_Annotations()->Delete(ma);
    }
    document->Save(_dataDir + u"RichMediaAnnotation_del.pdf");
}
```

## 添加3D注释

如今，PDF文件可以包含多种内容，而不仅仅是简单的文本和图形，包括逻辑结构、交互元素（如注释和表单字段）、图层、多媒体（包括视频内容）和3D对象。

这种3D内容可以通过3D注释在PDF文件中查看。

本节展示了使用Aspose.PDF的C++库在PDF文档中创建3D注释的基本步骤。

3D注释是使用U3D格式创建的模型添加的。

1. 创建一个新的[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/)
1. 加载所需3D模型的数据（在我们的例子中是"Ring.u3d"）以创建[PDF3DContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_content/)
1. 创建[3dArtWork](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_artwork/)对象并将其链接到文档和3DContent
1. 调整pdf3dArtWork对象：

```cpp
void MultimediaAnnotation::Add3DAnnottaion()
{
    public static void Add3dAnnotation()
    {
        // 加载PDF文件
        Document document = new Document();
        PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
        PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
        pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        var topMatrix = new Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        var page = document.getPages().add();

        var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
        pdf3dAnnotation.setDefaultViewIndex(1);
        pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
        pdf3dAnnotation.setName("Ring.u3d");
        //如果需要，设置预览图像
        //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
        document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

        document.save(_dataDir + "sample_3d.pdf");
    }
}
```

这个代码示例向我们展示了这样一个模型：

![3D Annotation demo](3d_demo.png)


## 添加小部件注释

小部件注释表示交互式 PDF 表单中表单字段的外观。

自 PDF v 1.2 我们可以使用小部件注释。这些是我们可以添加到 PDF 的交互式表单元素，使其更容易输入、提交信息或与用户执行其他操作。尽管小部件是一种特殊类型的注释，但我们不能直接将它们创建为注释，因为小部件注释是在特定页面上以图形方式表示表单字段。

文档中每个位置的每个表单字段代表一个注释小部件。为小部件添加与位置相关的注释数据到特定页面。每个表单字段有多个选项。按钮可以是切换、复选框或按钮。选择小部件可以是列表框或组合框。

Aspose.PDF for C++ 允许您使用 [Widget Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.widget_annotation/) 类来添加此注释。

要向页面添加按钮，我们需要使用以下代码片段： 

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;

void ExampleWidgetAnnotation::AddButton() {

    String _dataDir("C:\\Samples\\");

    // 加载PDF文件
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto rect = MakeObject<Rectangle>(72, 748, 164, 768);

    auto printButton = MakeObject<ButtonField>(page, rect);
    printButton->set_AlternateName(u"打印当前文档");
    printButton->set_Color(Color::get_Black());
    printButton->set_PartialName(u"printBtn1");
    printButton->set_NormalCaption(u"打印文档");

    auto border = MakeObject<Border>(printButton);
    border->set_Style(BorderStyle::Solid);
    border->set_Width(2);

    printButton->set_Border(border);
    printButton->get_Characteristics()->set_Border(System::Drawing::Color::FromArgb(255, 0, 0, 255));
    printButton->get_Characteristics()->set_Background(System::Drawing::Color::FromArgb(255, 0, 191, 255));
    auto wa = System::DynamicCast<Field>(printButton);
    document->get_Form()->Add(wa);

    document->Save(_dataDir + u"sample_widgetannot.pdf");
}
```

### 使用文档导航操作

此示例展示如何创建4个按钮：

```cpp
void ExampleWidgetAnnotation::AddDocumentNavigationActions() {

    String _dataDir("C:\\Samples\\");

    // 加载PDF文件
    auto document = MakeObject<Document>(_dataDir + u"JSON Fundamenals.pdf");

    auto buttons = MakeArray<System::SmartPtr<ButtonField>>(4);
    auto alternateNames = MakeArray<String>({ u"跳转到第一页", u"跳转到上一页", u"跳转到下一页", u"跳转到最后一页" });
    auto normalCaptions = MakeArray<String>({ u"第一页", u"上一页", u"下一页", u"最后一页" });
    PredefinedAction actions[] = { PredefinedAction::FirstPage, PredefinedAction::PrevPage,
                                    PredefinedAction::NextPage, PredefinedAction::LastPage };
    auto clrBorder = System::Drawing::Color::FromArgb(255, 0, 255, 0);
    auto clrBackGround = System::Drawing::Color::Color::FromArgb(255, 0, 96, 70);

// 我们应该创建这些按钮而不将它们附加到页面。

    for (int i = 0; i < 4; i++) {
        buttons[i] = MakeObject<ButtonField>(document, MakeObject<Rectangle>(32 + i * 80, 28, 104 + i * 80, 68));
        buttons[i]->set_AlternateName(alternateNames[i]);
        buttons[i]->set_Color(Color::get_White());
        buttons[i]->set_NormalCaption(normalCaptions[i]);
        buttons[i]->set_OnActivated(new NamedAction(actions[i]));
        auto border = MakeObject<Border>(buttons[i]);
        border->set_Style(BorderStyle::Solid);
        border->set_Width(2);
        buttons[i]->set_Border(border);
        buttons[i]->get_Characteristics()->set_Border(clrBorder);
        buttons[i]->get_Characteristics()->set_Background(clrBackGround);
    }

// 我们应该在文档的每一页上复制这个按钮数组。

    for (int pageIndex = 1; pageIndex <= 4; pageIndex++)
        for (int i = 0; i < 4; i++)
            document->get_Form()->Add(buttons[i], String::Format(u"btn{0}_{1}", pageIndex,(i + 1)), pageIndex);

    document->get_Form()->idx_get(u"btn1_1")->set_ReadOnly(true);
    document->get_Form()->idx_get(u"btn1_2")->set_ReadOnly(true);

    document->get_Form()->idx_get(String::Format(u"btn{0}_3", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->get_Form()->idx_get(String::Format(u"btn{0}_4", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->Save(_dataDir + u"sample_widgetannot_2.pdf");
}
```

### 删除小部件注释

```cpp
void ExampleWidgetAnnotation::DeleteWidgetAnnotation() {

    String _dataDir("C:\\Samples\\");

    // 加载PDF文件
    auto document = MakeObject<Document>(_dataDir + u"sample_widgetannot.pdf");
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(MakeObject<ButtonField>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto buttonFields = annotationSelector->get_Selected();

    // 删除注释
    for (auto wa : buttonFields) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_widgetannot_del.pdf");
}
```