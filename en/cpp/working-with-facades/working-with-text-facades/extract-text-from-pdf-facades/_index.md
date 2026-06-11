---

title: Extract Text from PDF - Facades

linktitle: Extract Text from PDF - Facades

type: docs

weight: 10

url: /cpp/extract-text-from-pdf-facades/

description: Learn how to extract text from PDF documents using the Facades API in C++ with Aspose.PDF for efficient content extraction.

---



## <ins>**Extract Text from all Pages of the Document**

In order to extract text from all pages of the PDF document, **Aspose.PDF for C++** offers PdfExtractor class under Facades namespace. You can extract all text from PDF document, save into MemoryStream object and get as a string, in case you want to use it for further manipulations. Following code snippet will show you, how to use PdfExtractor class to extract text from all pages of PDF document.

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
