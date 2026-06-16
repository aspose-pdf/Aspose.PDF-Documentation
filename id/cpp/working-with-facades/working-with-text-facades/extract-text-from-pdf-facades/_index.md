---
title: Extract Text from PDF - Facades
type: docs
weight: 10
url: /id/cpp/extract-text-from-pdf-facades/
---

## <ins>**Ekstrak Teks dari Semua Halaman Dokumen**
Untuk mengekstrak teks dari semua halaman dokumen PDF, **Aspose.PDF untuk C++** menawarkan kelas PdfExtractor di bawah namespace Facades. Anda dapat mengekstrak semua teks dari dokumen PDF, menyimpannya ke dalam objek MemoryStream dan mendapatkan sebagai string, jika Anda ingin menggunakannya untuk manipulasi lebih lanjut. Cuplikan kode berikut akan menunjukkan kepada Anda, bagaimana menggunakan kelas PdfExtractor untuk mengekstrak teks dari semua halaman dokumen PDF.

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