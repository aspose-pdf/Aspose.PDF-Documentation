---
title: Извлечение информации об изображении и подписи с использованием Aspose.PDF для C++
linktitle: Извлечение информации об изображении и подписи
type: docs
weight: 30
url: ru/cpp/extract-image-and-signature-information/
description: Вы можете извлечь изображения из поля подписи и извлечь информацию о подписи, используя класс SignatureField с C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение изображения из поля подписи

Aspose.PDF для C++ поддерживает функцию цифровой подписи PDF-файлов, используя класс [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) и при подписании документа.

Для извлечения информации о подписи мы добавили метод [ExtractImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a63f492fa6d3f83f0265b8e4f4c850293) в класс SignatureField.

Пожалуйста, ознакомьтесь с следующим фрагментом кода, который демонстрирует шаги по извлечению изображения из объекта [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field):
```

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

## Извлечение информации о подписи

Aspose.PDF для C++ позволяет извлекать информацию о подписи. Для этого мы ввели метод [ExtractCertificate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a73686c960036f755b6e800b84c27bee1) в класс [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field).

Пожалуйста, ознакомьтесь с следующим примером кода, который демонстрирует шаги для извлечения сертификата из объекта SignatureField:

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