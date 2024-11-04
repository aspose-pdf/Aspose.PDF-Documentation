---
title: Ekstrak Informasi Gambar dan Tanda Tangan menggunakan Aspose.PDF untuk C++
linktitle: Ekstrak Informasi Gambar dan Tanda Tangan
type: docs
weight: 30
url: /cpp/extract-image-and-signature-information/
description: Anda dapat mengekstrak gambar dari bidang tanda tangan dan mengekstrak informasi tanda tangan menggunakan kelas SignatureField dengan C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mengekstrak Gambar dari Bidang Tanda Tangan

Aspose.PDF untuk C++ mendukung fitur untuk menandatangani file PDF secara digital menggunakan kelas [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) dan saat menandatangani dokumen.

Untuk mengekstrak informasi tanda tangan, kami telah memperkenalkan metode [ExtractImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a63f492fa6d3f83f0265b8e4f4c850293) ke kelas SignatureField.

Silakan lihat potongan kode berikut yang menunjukkan langkah-langkah untuk mengekstrak gambar dari objek [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field):

```cpp
void SecuringAndSigning::ExtractingImageFromSignatureField() {


// String for path name.

String _dataDir("C:\\Samples\\");

auto pdfDocument = MakeObject<Document>(_dataDir + u"ExtractingImage.pdf");


int i = 0;

try {


for (auto& field : pdfDocument->get_Form()->get_Fields()) {



auto sf = System::DynamicCast<Aspose::Pdf::Forms::SignatureField>(field);



if (sf != nullptr) {




auto output = System::IO::File::OpenWrite(_dataDir + u"im" + i + u".jpeg");




auto tempStream = sf->ExtractImage();




tempStream->CopyTo(output);




output->Close();



}


}

}

catch (System::IO::IOException e) {


Console::WriteLine(e->get_Message());

}
}
```

## Ekstraksi Informasi Tanda Tangan

Aspose.PDF untuk C++ memungkinkan ekstraksi informasi tanda tangan. Untuk ini, kami telah memperkenalkan metode [ExtractCertificate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a73686c960036f755b6e800b84c27bee1) ke dalam kelas [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field).

Silakan lihat cuplikan kode berikut yang menunjukkan langkah-langkah untuk mengekstrak sertifikat dari objek SignatureField:

```cpp
void SecuringAndSigning::ExtractSignatureInformation() {


String _dataDir("C:\\Samples\\");


String input = _dataDir + u"ExtractSignatureInfo.pdf";

auto pdfDocument = MakeObject<Document>(input);


for (auto& field : pdfDocument->get_Form()->get_Fields()) {


auto sf = System::DynamicCast<Aspose::Pdf::Forms::SignatureField>(field);


if (sf != nullptr) {



auto cerStream = sf->ExtractCertificate();



if (cerStream != nullptr) {




auto outStream = System::IO::File::OpenWrite(_dataDir + u"targetFile.cer");




cerStream->CopyTo(outStream);




outStream->Close();



}


}

}
}
```