---
title: 将图像添加到 PDF 使用 C++
linktitle: 添加图像
type: docs
weight: 10
url: zh/cpp/add-image-to-existing-pdf-file/
description: 本节描述如何使用 C++ 库将图像添加到现有的 PDF 文件中。
lastmod: "2021-12-18"
---

## 在现有 PDF 文件中添加图像

每个 PDF 页面包含资源和内容属性。资源可以是图像和表单，例如，而内容由一组 PDF 操作符表示。每个操作符都有其名称和参数。此示例使用操作符将图像添加到 PDF 文件。

要将图像添加到现有 PDF 文件中：

- 创建一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 对象并打开输入 PDF 文档。
- 获取您想要添加图像的页面。
- 将图像添加到页面的资源集合中。
- 使用操作符将图像放置在页面上：
- 使用 [GSave 操作符](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) 保存当前图形状态。

- 使用 [ConcatenateMatrix 操作符](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix#a40ca09b1fa45560d57a1fd042d3fbe96) 指定图像要放置的位置。
- 使用 [Do 操作符](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do/) 在页面上绘制图像。
- 最后，使用 [GRestore 操作符](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/) 保存更新后的图形状态。
- 保存文件。
以下代码片段显示了如何在 PDF 文档中添加图像。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImages::AddImageToExistingPDF()
{
    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"AddImage.pdf");

    // 设置坐标
    int lowerLeftX = 50;
    int lowerLeftY = 750;
    int upperRightX = 100;
    int upperRightY = 800;

    // 获取要添加图像的页面
    auto page = document->get_Pages()->idx_get(1);

    // 将图像加载到流中
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"logo.png");

    // 将图像添加到页面资源的 Images 集合中
    page->get_Resources()->get_Images()->Add(imageStream);

    // 使用 GSave 操作符：该操作符保存当前图形状态
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // 创建 Rectangle 和 Matrix 对象
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

    auto matrix = MakeObject<Matrix>(
        MakeArray<double>({
            rectangle->get_URX() - rectangle->get_LLX(),
            0,                  0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(), rectangle->get_LLY() }));

    // 使用 ConcatenateMatrix（连接矩阵）操作符：
    // 定义图像的放置方式
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

    // 使用 Do 操作符：该操作符绘制图像
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));

    // 使用 GRestore 操作符：该操作符恢复图形状态
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // 保存新的 PDF
    document->Save(_dataDir + u"updated_document.pdf");

    // 关闭图像流
    imageStream->Close();
}
```

## 在 PDF 文档中多次添加单个图像的引用

有时我们需要在 PDF 文档中多次使用相同的图像。添加新的实例会增加生成的 PDF 文档的大小。[XImageCollection.Add(XImage)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image/) 方法允许添加对相同 PDF 对象的引用作为原始图像，从而优化 PDF 文档的大小。

```cpp
void WorkingWithImages::AddReferenceOfaSingleImageMultipleTimes() {

    String _dataDir("C:\\Samples\\");
    auto imageRectangle = MakeObject<Rectangle>(0, 0, 30, 15);

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    document->get_Pages()->Add();
    document->get_Pages()->Add();

    auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.png");

    SharedPtr<Aspose::Pdf::XImage> image;

    for (auto page : document->get_Pages()) {
        auto annotation = MakeObject<Aspose::Pdf::Annotations::WatermarkAnnotation>(page, page->get_Rect());
        auto form = annotation->get_Appearance()->idx_get(u"N");
        form->set_BBox(page->get_Rect());
        String name;
        if (image != nullptr) {
            name = form->get_Resources()->get_Images()->Add(imageStream);
            image = form->get_Resources()->get_Images()->idx_get(name);
        }
        else {
            form->get_Resources()->get_Images()->AddWithName(image);
        }
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
        form->get_Contents()->Add(
            MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(
                MakeObject<Matrix>(imageRectangle->get_Width(), 0, 0, imageRectangle->get_Height(), 0, 0)));

        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(name));
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
        page->get_Annotations()->Add(annotation, false);
        imageRectangle = MakeObject<Rectangle>(0, 0, imageRectangle->get_Width() * 1.01, imageRectangle->get_Height() * 1.01);
    }
    document->Save(_dataDir + u"AddReferenceOfaSingleImageMultipleTimes_out.pdf");
}
```

## 将图像放置在页面上并保持（控制）纵横比

如果我们不知道图像的尺寸，那么页面上很有可能会得到一个失真的图像。以下示例显示了避免这种情况的方法之一。

```cpp
void WorkingWithImages::AddingImageAndPreserveAspectRatioIntoPDF() {

    String _dataDir("C:\\Samples\\");

    auto bitmap = System::Drawing::Image::FromFile(_dataDir + u"3410492.jpg");

    int width;
    int height;

    width = bitmap->get_Width();
    height = bitmap->get_Height();

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page->AddImage(_dataDir + u"3410492.jpg", new Rectangle(10, 10, scaledWidth, scaledHeight));
    document->Save(_dataDir + u"sample_image.pdf");
}
```

## 确定PDF中的图像是彩色还是黑白

为了减少图像的大小，您需要压缩它。 在您确定图像的压缩类型之前，您需要知道它是彩色还是黑白。

图像应用的压缩类型取决于原始图像的ColorSpace，即如果图像是彩色（RGB），则使用JPEG2000压缩，如果是黑白，则使用JBIG2 / JBIG2000压缩。

PDF文件可以包含文本、图像、图形、附件、注释等元素，如果源PDF文件包含图像，我们可以确定图像的色彩空间并应用适当的压缩来减少PDF文件的大小。

以下代码片段显示了识别PDF内图像是彩色还是黑白的步骤。

```cpp
void WorkingWithImages::CheckColors() {

    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"test4.pdf");
    try {
        // 遍历PDF文件的所有页面
        for (auto page : document->get_Pages()) {
            // 创建图像放置吸收器实例
            auto abs = MakeObject<ImagePlacementAbsorber>();
            page->Accept(abs);

            for (auto ia : abs->get_ImagePlacements()) {
                /* ColorType */
                auto colorType = ia->get_Image()->GetColorType();
                switch (colorType) {
                case ColorType::Grayscale:
                    Console::WriteLine(u"灰度图像");
                    break;
                case ColorType::Rgb:
                    Console::WriteLine(u"彩色图像");
                    break;
                }
            }
        }
    }
    catch (Exception ex) {
        Console::WriteLine(u"读取文件错误 = {0}", document->get_FileName());
    }
}
```
## 控制图像质量

可以控制添加到 PDF 文件中的图像质量。使用 [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection) 类中的重载 [Replace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection#a698b65051b073f0f4b84b1235889bd72) 方法。

以下代码片段演示了如何将所有文档图像转换为使用 80% 质量进行压缩的 JPEG 格式。

```cpp
void WorkingWithImages::ControlImageQuality() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample_with_images.pdf");

    for (auto page : document->get_Pages())
    {
        int idx = 1;
        for (auto image : page->get_Resources()->get_Images())
        {
            auto imageStream = MakeObject<System::IO::MemoryStream>();
            image->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Jpeg());
            page->get_Resources()->get_Images()->Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }

    document->Save(_dataDir + u"sample_with_images_out.pdf");
}
```