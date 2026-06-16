---
title: استخراج النص من PDF - الواجهات
type: docs
weight: 10
url: /ar/cpp/extract-text-from-pdf-facades/
---

## <ins>**استخراج النص من جميع صفحات المستند**
لاستخراج النص من جميع صفحات مستند PDF، توفر **Aspose.PDF for C++** فئة PdfExtractor تحت مساحة الأسماء Facades. يمكنك استخراج كل النص من مستند PDF، حفظه في كائن MemoryStream والحصول عليه كسلسلة نصية، في حال كنت ترغب في استخدامه لمزيد من المعالجات. سيوضح لك مقتطف الشيفرة التالي كيفية استخدام فئة PdfExtractor لاستخراج النص من جميع صفحات مستند PDF.



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