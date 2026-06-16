---

title: Извлечение текста из PDF - Фасады
type: docs
weight: 10
url: /ru/cpp/extract-text-from-pdf-facades/
---
## <ins>**Извлечение текста со всех страниц документа**  
Для извлечения текста со всех страниц PDF-документа **Aspose.PDF for C++** предлагает класс PdfExtractor в пространстве имен Facades. Вы можете извлечь весь текст из PDF-документа, сохранить его в объект MemoryStream и получить в виде строки, если вы хотите использовать его для дальнейших манипуляций. Следующий фрагмент кода покажет вам, как использовать класс PdfExtractor для извлечения текста со всех страниц PDF-документа.

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