---
title: 从PDF提取文本 - Facades
type: docs
weight: 10
url: /zh/cpp/extract-text-from-pdf-facades/
---

## <ins>**从文档的所有页面提取文本**
为了从PDF文档的所有页面提取文本，**Aspose.PDF for C++** 在Facades命名空间下提供了PdfExtractor类。您可以从PDF文档中提取所有文本，保存到MemoryStream对象中，并以字符串形式获取，以便您进行进一步的操作。下面的代码片段将向您展示如何使用PdfExtractor类从PDF文档的所有页面提取文本。



```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
auto extractor = MakeObject<Facades::PdfExtractor>();	
extractor->BindPdf(L"..\\Data\\Text\\input.pdf");
extractor->ExtractText();
	
auto memStream = MakeObject<IO::MemoryStream>();
extractor->GetText(memStream);

auto unicode = System::Text::Encoding::get_Unicode();

String allText = unicode->GetString(memStream->ToArray());	
Console::WriteLine(allText);
```