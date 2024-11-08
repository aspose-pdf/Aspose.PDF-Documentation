---
title: Bekerja dengan Judul di PDF
type: docs
weight: 90
url: /id/cpp/working-with-headings/
lastmod: "2021-11-11"
description: Buat penomoran dalam judul dokumen PDF Anda dengan C++. Aspose.PDF untuk C++ menunjukkan berbagai jenis gaya penomoran.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Terapkan Gaya Penomoran dalam Judul

Teks apa pun dalam dokumen dimulai dengan judul. Judul adalah bagian integral dari konten, terlepas dari gaya dan tema.
Judul membantu menarik perhatian pada teks dan membantu pengguna menemukan informasi yang mereka butuhkan dalam dokumen, meningkatkan keterbacaan dan persepsi visual. Dengan menggunakan gaya judul, Anda juga dapat dengan cepat membuat daftar isi, mengubah struktur dokumen.
Jadi, mari kita lihat bagaimana cara bekerja dengan judul menggunakan pustaka Aspose.PDF untuk C++.

[Aspose.PDF untuk C++](/pdf/id/cpp/) menawarkan banyak gaya penomoran yang sudah ditentukan sebelumnya. 
Gaya penomoran yang telah ditentukan sebelumnya disimpan dalam enumerasi, NumberingStyle. Nilai-nilai yang telah ditentukan dari enumerasi NumberingStyle dan deskripsinya diberikan di bawah ini:

|**Jenis Heading**|**Deskripsi**|
| :- | :- |
|NumeralsArabic|Tipe Arab, misalnya, 1,1.1,...|
|NumeralsRomanUppercase|Tipe Romawi atas, misalnya, I,I.II, ...|
|NumeralsRomanLowercase|Tipe Romawi bawah, misalnya, i,i.ii, ...|
|LettersUppercase|Tipe Inggris atas, misalnya, A,A.B, ...|
|LettersLowercase|Tipe Inggris bawah, misalnya, a,a.b, ...|
Properti **Style** dari kelas **Aspose.PDF.Heading** digunakan untuk mengatur gaya penomoran dari heading.

|**Gambar: Gaya penomoran yang telah ditentukan**|
| :- |
Kode sumber, untuk mendapatkan keluaran yang ditunjukkan pada gambar di atas, diberikan di bawah ini dalam contoh.

```cpp
void WorkingWithHeadingsInPDF() {
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String outputFileName("ApplyNumberStyle_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>();

    document->get_PageInfo()->set_Width(612.0);
    document->get_PageInfo()->set_Height(792.0);
    document->get_PageInfo()->set_Margin (MakeObject<MarginInfo>());
    document->get_PageInfo()->get_Margin()->set_Left(72);
    document->get_PageInfo()->get_Margin()->set_Right(72);
    document->get_PageInfo()->get_Margin()->set_Top (72);
    document->get_PageInfo()->get_Margin()->set_Bottom (72);
            
    auto pdfPage = document->get_Pages()->Add();
    pdfPage->get_PageInfo()->set_Width (612.0);
    pdfPage->get_PageInfo()->set_Height (792.0);
    pdfPage->get_PageInfo()->set_Margin(MakeObject<MarginInfo>());
    pdfPage->get_PageInfo()->get_Margin()->set_Left(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Right(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Top(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Bottom(72);

    auto floatBox = MakeObject<FloatingBox>();
    floatBox->set_Margin(pdfPage->get_PageInfo()->get_Margin());

    pdfPage->get_Paragraphs()->Add(floatBox);

    auto textFragment = MakeObject<TextFragment>();
    auto segment = MakeObject<TextSegment>();

    auto heading = MakeObject<Heading>(1);
    heading->set_IsInList(true);
    heading->set_StartNumber(1);
    heading->set_Text (u"Daftar 1");
    heading->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading);

    auto heading2 = MakeObject<Heading>(1);
    heading2->set_IsInList (true);
    heading2->set_StartNumber(13);
    heading2->set_Text (u"Daftar 2");
    heading2->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading2->set_IsAutoSequence(true);;

    floatBox->get_Paragraphs()->Add(heading2);

    auto heading3 = MakeObject<Heading>(2);
    heading3->set_IsInList (true);
    heading3->set_StartNumber(1);
    heading3->set_Text (u"nilai, pada tanggal efektif rencana, dari properti yang akan didistribusikan di bawah rencana terkait dengan setiap yang diizinkan");
    heading3->set_Style(NumberingStyle::LettersLowercase);
    heading3->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading3); 

    // Simpan file keluaran yang digabungkan
    document->Save(_dataDir + outputFileName);
}
```