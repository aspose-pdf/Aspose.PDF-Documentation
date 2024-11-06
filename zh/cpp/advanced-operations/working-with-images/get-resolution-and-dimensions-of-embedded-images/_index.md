---
title: 获取嵌入图像的分辨率和尺寸使用C++
linktitle: 获取分辨率和尺寸
type: docs
weight: 40
url: zh/cpp/get-resolution-and-dimensions-of-embedded-images/
description: 本节展示如何获取嵌入图像的分辨率和尺寸的详细信息
lastmod: "2021-12-18"
---

本主题解释了如何使用Aspose.PDF命名空间中的操作类，这些类提供了获取图像的分辨率和尺寸信息的功能，而无需提取它们。

有不同的方法来实现这一点。本文解释了如何使用`arraylist`和[图像放置类](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement)。

1. 首先，加载源PDF文件（包含图像）。
1. 然后创建一个ArrayList对象来保存文档中任何图像的名称。
1. 使用Page.Resources.Images属性获取图像。
1. 创建一个堆栈对象来保存图像的图形状态，并使用它来跟踪不同的图像状态。
1. 创建一个 ConcatenateMatrix 对象，该对象定义当前的转换。它还支持缩放、旋转和倾斜任何内容。它将新矩阵与先前的矩阵连接起来。请注意，我们不能从头定义转换，只能修改现有的转换。

1. 因为我们可以用 ConcatenateMatrix 修改矩阵，所以我们可能还需要恢复到原始图像状态。使用 [GSave 操作符](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) 和 [GRestore 操作符](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/)。这些操作符是成对的，因此应该一起调用。例如，如果您进行一些复杂转换的图形工作，最后将转换返回到初始状态，方法将是这样的：

以下代码片段向您展示了如何在不从 PDF 文档中提取图像的情况下获取图像的尺寸和分辨率。

```cpp
void WorkingWithImages::GetResolutionAndDimensionsOfEmbeddedImages()
{
    String _dataDir("C:\\Samples\\");
    // 加载源 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"ImageInformation.pdf");

    // 定义图像的默认分辨率
    int defaultResolution = 72;
    auto graphicsState = MakeObject<System::Collections::Generic::Stack<System::SmartPtr<object>>>();
    // 定义将保存图像名称的数组列表对象
    auto imageNames = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->get_Names();

    // 将对象插入堆栈
    graphicsState->Push(System::DynamicCast<object>(MakeObject<System::Drawing::Drawing2D::Matrix>(1, 0, 0, 1, 0, 0)));

    // 获取文档第一页的所有操作符
    for (auto op : document->get_Pages()->idx_get(1)->get_Contents())
    {
        // 使用 GSave/GRestore 操作符将转换还原到先前设置的状态
        auto opSaveState = System::DynamicCast<Aspose::Pdf::Operators::GSave>(op);
        auto opRestoreState = System::DynamicCast<Aspose::Pdf::Operators::GRestore>(op);

        // 实例化 ConcatenateMatrix 对象，因为它定义了当前的转换矩阵。
        auto opCtm = System::DynamicCast<Aspose::Pdf::Operators::ConcatenateMatrix>(op);

        // 创建 Do 操作符，从资源中绘制对象。它绘制 Form 对象和 Image 对象
        auto opDo = System::DynamicCast<Aspose::Pdf::Operators::Do>(op);

        if (opSaveState != nullptr)
        {
            // 保存以前的状态并将当前状态推到堆栈顶部
            graphicsState->Push(System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Clone());
        }
        else if (opRestoreState != nullptr)
        {
            // 丢弃当前状态并恢复以前的状态
            graphicsState->Pop();
        }
        else if (opCtm != nullptr)
        {
            auto cm = MakeObject<System::Drawing::Drawing2D::Matrix>(
                (float)opCtm->get_Matrix()->get_A(),
                (float)opCtm->get_Matrix()->get_B(),
                (float)opCtm->get_Matrix()->get_C(),
                (float)opCtm->get_Matrix()->get_D(),
                (float)opCtm->get_Matrix()->get_E(),
                (float)opCtm->get_Matrix()->get_F());

            // 将当前矩阵与状态矩阵相乘
            System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Multiply(cm);
            continue;
        }
        else if (opDo != nullptr)
        {
            // 如果这是一个图像绘制操作符
            if (imageNames->Contains(opDo->get_Name()))
            {
                auto lastCTM = System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek());
                // 创建 XImage 对象以保存第一页的图像
                auto image = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(opDo->get_Name());

                // 获取图像尺寸
                double scaledWidth = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(0), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(1), 2));
                double scaledHeight = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(2), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(3), 2));
                // 获取图像的高度和宽度信息
                double originalWidth = image->get_Width();
                double originalHeight = image->get_Height();

                // 基于以上信息计算分辨率
                double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                double resVertical = originalHeight * defaultResolution / scaledHeight;

                // 显示每个图像的尺寸和分辨率信息
                Console::Write(_dataDir);
                Console::Write(u" image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                    opDo->get_Name(), scaledWidth, scaledHeight, resHorizontal, resVertical);
            }
        }
    }
}
```