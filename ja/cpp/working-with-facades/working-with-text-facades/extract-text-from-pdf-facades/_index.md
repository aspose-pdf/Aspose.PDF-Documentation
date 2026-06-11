---
title: PDFからテキストを抽出 - Facades
type: docs
weight: 10
url: /ja/cpp/extract-text-from-pdf-facades/
---

## <ins>**ドキュメントのすべてのページからテキストを抽出する**
PDFドキュメントのすべてのページからテキストを抽出するために、**Aspose.PDF for C++**はFacades名前空間の下でPdfExtractorクラスを提供します。PDFドキュメントからすべてのテキストを抽出して、MemoryStreamオブジェクトに保存し、文字列として取得することができます。これは、さらなる操作に使用したい場合に便利です。次のコードスニペットは、PDFドキュメントのすべてのページからテキストを抽出するためにPdfExtractorクラスを使用する方法を示します。



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