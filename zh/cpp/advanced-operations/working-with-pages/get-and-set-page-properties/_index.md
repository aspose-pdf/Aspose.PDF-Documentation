---
title: 获取和设置页面属性
type: docs
weight: 20
url: /zh/cpp/get-and-set-page-properties/
description: 您可以使用C++库从PDF文件中获取和设置页面属性。
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** 允许您在C++应用程序中读取和设置PDF文件中页面的属性。本节展示了如何获取PDF文件中的页数，获取有关PDF页面属性的信息，如颜色和设置页面属性，获取PDF文件的特定页面等。

## 获取PDF文件中的页数

在处理文档时，您通常想知道它们包含多少页。使用Aspose.PDF，只需两行代码即可完成此操作。

要获取PDF文件中的页数：

1. 使用[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)类打开PDF文件。
1. 然后使用[PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)集合的Count属性（来自Document对象）来获取文档中的总页数。

以下代码片段展示了如何获取PDF文件的页数。

```cpp
void GetNumberOfPages() {
    // 打开文档
    String _dataDir("C:\\Samples\\");
    String srcFileName("GetNumberofPages.pdf");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);

    // 获取页数
    std::cout << "Page Count : " << srcDocument->get_Pages()->get_Count() << std::endl;
}
```

### 在不保存文档的情况下获取页数

有时我们会即时生成PDF文件，并且在创建PDF文件的过程中，可能会遇到需要获取PDF文件页数的要求（创建目录等），而不需要将文件保存到系统或流中。 为了满足这一需求，在Document类中引入了一个方法[ProcessParagraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a1773e7b6a887eaddd602073e29939a6f)。请查看下面的代码片段，该片段展示了在不保存文档的情况下获取页数的步骤。

```cpp
void GetPageCountWithoutSavingTheDocument() {
    // 实例化Document实例
    auto document = MakeObject<Document>();

    // 向PDF文件的页面集合中添加页面
    auto page = document->get_Pages()->Add();
    // 创建循环实例
    for (int i = 0; i < 300; i++)
        // 向页面对象的段落集合中添加TextFragment
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Pages count test"));
    // 处理PDF文件中的段落以获取准确的页数
    document->ProcessParagraphs();
    // 打印文档中的页数
    std::cout << "Number of pages in document = " << document->get_Pages()->get_Count();
}
```

## 获取页面属性
### 访问页面属性

[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 类提供了与特定 PDF 页面相关的所有属性。PDF 文件的所有页面都包含在 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象的 [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 集合中。

从那里，可以使用索引访问单个 Page 对象，或者使用 foreach 循环遍历集合以获取所有页面。一旦访问到单个页面，我们就可以获取其属性。以下代码片段展示了如何获取页面属性。

```cpp
void AccessingPageProperties() {

    String _dataDir("C:\\Samples\\");
    String pdfDocument("GetProperties.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + pdfDocument);

    // 获取特定页面
    auto pdfPage = document->get_Pages()->idx_get(1);
    // 获取页面属性
    Console::WriteLine(u"ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_ArtBox()->get_Height(), pdfPage->get_ArtBox()->get_Width(),
        pdfPage->get_ArtBox()->get_LLX(), pdfPage->get_ArtBox()->get_LLY(),
        pdfPage->get_ArtBox()->get_URX(), pdfPage->get_ArtBox()->get_URY());

    Console::WriteLine(u"->get_BleedBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_BleedBox()->get_Height(), pdfPage->get_BleedBox()->get_Width(),
        pdfPage->get_BleedBox()->get_LLX(), pdfPage->get_BleedBox()->get_LLY(),
        pdfPage->get_BleedBox()->get_URX(), pdfPage->get_BleedBox()->get_URY());

    Console::WriteLine(u"get_CropBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_CropBox()->get_Height(), pdfPage->get_CropBox()->get_Width(),
        pdfPage->get_CropBox()->get_LLX(), pdfPage->get_CropBox()->get_LLY(),
        pdfPage->get_CropBox()->get_URX(), pdfPage->get_CropBox()->get_URY());

    Console::WriteLine(u"get_MediaBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_MediaBox()->get_Height(), pdfPage->get_MediaBox()->get_Width(),
        pdfPage->get_MediaBox()->get_LLX(), pdfPage->get_MediaBox()->get_LLY(),
        pdfPage->get_MediaBox()->get_URX(), pdfPage->get_MediaBox()->get_URY());

    Console::WriteLine(u"get_TrimBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_TrimBox()->get_Height(), pdfPage->get_TrimBox()->get_Width(),
        pdfPage->get_TrimBox()->get_LLX(), pdfPage->get_TrimBox()->get_LLY(),
        pdfPage->get_TrimBox()->get_URX(), pdfPage->get_TrimBox()->get_URY());

    Console::WriteLine(u"Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_Rect()->get_Height(), pdfPage->get_Rect()->get_Width(),
        pdfPage->get_Rect()->get_LLX(), pdfPage->get_Rect()->get_LLY(),
        pdfPage->get_Rect()->get_URX(), pdfPage->get_Rect()->get_URY());

    Console::WriteLine(u"Page Number : {0}", pdfPage->get_Number());
    Console::WriteLine(u"Rotate : {0}", pdfPage->get_Rotate());
}
```