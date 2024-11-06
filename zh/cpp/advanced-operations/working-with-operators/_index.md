---
title: 使用运算符与C++协作
linktitle: 使用运算符
type: docs
weight: 170
url: zh/cpp/operators/
description: 本主题解释如何在C++中使用Aspose.PDF的运算符。运算符类为PDF操作提供了强大的功能。
lastmod: "2021-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF运算符及其用法简介

运算符是一个PDF关键字，指定要执行的某些操作，例如在页面上绘制图形形状。运算符关键字与命名对象的区别在于没有初始的斜杠字符（2Fh）。运算符仅在内容流中有意义。

内容流是一个PDF流对象，其数据由描述要在页面上绘制的图形元素的指令组成。有关PDF运算符的更多详细信息，请参阅[PDF规范](https://opensource.adobe.com/dc-acrobat-sdk-docs/)。

### 实现细节

本主题解释如何使用Aspose.PDF的运算符。 选择的示例将图像添加到 PDF 文件中以说明该概念。要在 PDF 文件中添加图像，需要不同的操作符。此示例使用 [GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save)、[ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix)、[Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do) 和 [GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore)。

- **GSave** 操作符保存 PDF 的当前图形状态。
- **ConcatenateMatrix**（连接矩阵）操作符用于定义图像应如何放置在 PDF 页面上。
- **Do** 操作符在页面上绘制图像。
- **GRestore** 操作符恢复图形状态。

要在 PDF 文件中添加图像：

1. 创建一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 对象并打开输入的 PDF 文档。
1. 获取要添加图像的特定页面。
1. 将图像添加到页面的资源集合中。
1. 使用操作符将图像放置在页面上：
   - 首先，使用GSave操作符保存当前的图形状态。
   - 然后使用ConcatenateMatrix操作符指定图像要放置的位置。
   - 使用Do操作符在页面上绘制图像。
1. 最后，使用GRestore操作符保存更新后的图形状态。

以下代码片段展示了如何使用PDF操作符。

```cpp
void ExampleUsingOperators()
{
    // 打开文档
    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"PDFOperators.pdf");

    // 设置坐标
    int lowerLeftX = 100;
    int lowerLeftY = 100;
    int upperRightX = 200;
    int upperRightY = 200;

    // 获取需要添加图像的页面
    auto page = document->get_Pages()->idx_get(1);

    // 将图像加载到流中
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"PDFOperators.jpg");
    // 将图像添加到页面资源的Images集合中
    page->get_Resources()->get_Images()->Add(imageStream);

    // 使用GSave操作符：此操作符保存当前图形状态
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // 创建矩形和矩阵对象
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
    auto matrix = MakeObject<Matrix>(
        new double[] {
            rectangle->get_URX() - rectangle->get_LLX(), 0, 0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(),  rectangle->get_LLY() });
    // 使用ConcatenateMatrix（连接矩阵）操作符：定义图像必须放置的位置
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());
    // 使用Do操作符：此操作符绘制图像
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    // 使用GRestore操作符：此操作符恢复图形状态
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());


    // 保存更新后的文档
    document->Save(_dataDir + u"PDFOperators_out.pdf");
}
```
## 使用操作符在页面上绘制XForm

本主题演示如何使用GSave/GRestore操作符、ConcatenateMatrix操作符来定位xForm，以及Do操作符在页面上绘制xForm。

下面的代码使用GSave/GRestore操作符对包裹PDF文件的现有内容。这种方法有助于在现有内容的末尾获取初始图形状态。如果不使用这种方法，可能会在现有操作符链的末尾保留一些不需要的变换。

```cpp
void DrawXFormOnPageUsingOperators() {
    // 打开文档
    String _dataDir("C:\\Samples\\");

    String imageFile(_dataDir + u"aspose-logo.jpg");
    String inFile(_dataDir + u"DrawXFormOnPage.pdf");
    String outFile(_dataDir + u"blank-sample2_out.pdf");

    auto document = MakeObject<Document>(inFile);
    auto pageContents = document->get_Pages()->idx_get(1)->get_Contents();

    // 示例演示
    // GSave/GRestore操作符的使用
    // ConcatenateMatrix操作符用于定位xForm
    // Do操作符用于在页面上绘制xForm

    // 用GSave/GRestore操作符对包裹现有内容
    // 这是为了在现有内容的末尾获取初始图形状态
    // 否则可能会在现有操作符链的末尾保留一些不需要的变换
    pageContents->Insert(1, MakeObject<Aspose::Pdf::Operators::GSave>());
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // 添加保存图形状态操作符，以便在新命令后正确清除图形状态
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // 创建xForm

    auto form = XForm::CreateNewForm(document->get_Pages()->idx_get(1), document);
    document->get_Pages()->idx_get(1)->get_Resources()->get_Forms()->Add(form);
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // 定义图像宽度和高度
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(200, 0, 0, 200, 0, 0));
    // 将图像加载到流中
    auto imageStream = System::IO::File::OpenRead(imageFile);
    // 将图像添加到XForm资源的Images集合中
    form->get_Resources()->get_Images()->Add(imageStream);
    auto ximage = form->get_Resources()->get_Images()->idx_get(form->get_Resources()->get_Images()->get_Count());
    // 使用Do操作符：此操作符绘制图像
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // ----------------------------------------------------

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // 将表单放置在x=100 y=500坐标
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 500));
    // 使用Do操作符绘制表单
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // 将表单放置在x=100 y=300坐标
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 300));
    // 使用Do操作符绘制表单
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // 使用GRestore恢复图形状态
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
    document->Save(outFile);
}
```

## 使用操作符类移除图形对象

操作符类为PDF操作提供了强大的功能。当PDF文件包含无法通过[PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor)类的[DeleteImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor#af7d23ef932737bf606f008ad5ec48380)方法移除的图形时，可以使用操作符类来移除它们。

以下代码片段展示了如何移除图形。请注意，如果PDF文件包含图形的文本标签，使用这种方法它们可能会保留在PDF文件中。因此，请搜索图形操作符以找到删除此类图像的替代方法。

```cpp
void RemoveGraphicsObjects() {
    // 打开文档
    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"RemoveGraphicsObjects.pdf");

    auto page = document->get_Pages()->idx_get(2);
    auto oc = page->get_Contents();

    // 使用路径绘制操作符
    auto operators = MakeArray<System::SmartPtr<Operator>>({
            MakeObject<Aspose::Pdf::Operators::Stroke>(),
            MakeObject<Aspose::Pdf::Operators::ClosePathStroke>(),
            MakeObject<Aspose::Pdf::Operators::Fill>()
    });

    oc->Delete(operators);
    document->Save(_dataDir + u"No_Graphics_out.pdf");
}
```