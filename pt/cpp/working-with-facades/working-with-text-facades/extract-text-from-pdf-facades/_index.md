---
title: Extrair Texto do PDF - Fachadas
type: docs
weight: 10
url: /pt/cpp/extract-text-from-pdf-facades/
---

## <ins>**Extrair Texto de Todas as Páginas do Documento**
Para extrair texto de todas as páginas do documento PDF, **Aspose.PDF for C++** oferece a classe PdfExtractor no namespace Facades. Você pode extrair todo o texto do documento PDF, salvar em um objeto MemoryStream e obter como uma string, caso queira usá-lo para manipulações adicionais. O seguinte trecho de código mostrará como usar a classe PdfExtractor para extrair texto de todas as páginas do documento PDF.



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