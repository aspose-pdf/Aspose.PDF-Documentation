---
title: Ekstrak Teks Dari Stempel
linktitle: Ekstrak Teks Dari Stempel
type: docs
weight: 60
url: /id/cpp/extract-text-from-stamps/
---

## Ekstrak Teks dari Anotasi Stempel

Aspose.PDF untuk C++ memungkinkan Anda mengekstrak teks dari anotasi stempel. Untuk mengekstrak teks dari Anotasi Stempel dalam PDF, langkah-langkah berikut dapat digunakan.

1. Buat objek kelas Document
1. Dapatkan Anotasi yang diinginkan dari daftar anotasi sebuah halaman
1. Definisikan objek baru dari kelas TextAbsorber
1. Gunakan metode visit dari TextAbsorber untuk mendapatkan Teks

```cpp
void Parsing::ExtractTextFromStamp()
{
      std::clog << __func__ << ": Start" << std::endl;
      // String untuk nama path
      String _dataDir("C:\\Samples\\Parsing\\");

      // String untuk nama file
      String infilename("ExtractStampText.pdf");

      auto document = MakeObject<Document>(_dataDir + infilename);

      auto item = document->get_Pages()->idx_get(1)->get_Annotations()->idx_get(1);
      if (item->get_AnnotationType() == Annotations::AnnotationType::Stamp) {
            auto annot = System::DynamicCast<Aspose::Pdf::Annotations::StampAnnotation>(item);
            auto ta = MakeObject<TextAbsorber>();
            auto ap = annot->get_Appearance()->idx_get(u"N");
            ta->Visit(ap);
            Console::WriteLine(ta->get_Text());
      }
}
```