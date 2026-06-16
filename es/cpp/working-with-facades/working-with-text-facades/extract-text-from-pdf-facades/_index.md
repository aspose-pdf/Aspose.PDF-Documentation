---
title: Extract Text from PDF - Facades
type: docs
weight: 10
url: /es/cpp/extract-text-from-pdf-facades/
---

## <ins>**Extraer texto de todas las páginas del documento**
Para extraer texto de todas las páginas del documento PDF, **Aspose.PDF para C++** ofrece la clase PdfExtractor bajo el espacio de nombres Facades. Puedes extraer todo el texto del documento PDF, guardarlo en un objeto MemoryStream y obtenerlo como una cadena, en caso de que desees usarlo para manipulaciones adicionales. El siguiente fragmento de código te mostrará cómo usar la clase PdfExtractor para extraer texto de todas las páginas del documento PDF.



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