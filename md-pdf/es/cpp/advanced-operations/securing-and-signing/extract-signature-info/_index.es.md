---
title: Extraer Información de Imagen y Firma usando Aspose.PDF para C++
linktitle: Extraer Información de Imagen y Firma
type: docs
weight: 30
url: /cpp/extract-image-and-signature-information/
description: Puede extraer imágenes del campo de firma y extraer información de firma usando la clase SignatureField con C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extracción de Imagen del Campo de Firma

Aspose.PDF para C++ admite la función de firmar digitalmente los archivos PDF usando la clase [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) y al firmar el documento.

Para extraer información de la firma, hemos introducido el método [ExtractImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a63f492fa6d3f83f0265b8e4f4c850293) en la clase SignatureField.

Por favor, eche un vistazo al siguiente fragmento de código que demuestra los pasos para extraer una imagen del objeto [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field):

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

## Extraer Información de la Firma

Aspose.PDF para C++ permite extraer información de la firma. Para esto, hemos introducido el método [ExtractCertificate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a73686c960036f755b6e800b84c27bee1) en la clase [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field).

Por favor, eche un vistazo al siguiente fragmento de código que demuestra los pasos para extraer el certificado del objeto SignatureField:

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