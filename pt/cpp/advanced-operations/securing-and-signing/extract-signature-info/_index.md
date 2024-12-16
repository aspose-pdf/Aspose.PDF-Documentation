---
title: Extrair Informações de Imagem e Assinatura usando Aspose.PDF para C++
linktitle: Extrair Informações de Imagem e Assinatura
type: docs
weight: 30
url: /pt/cpp/extract-image-and-signature-information/
description: Você pode extrair imagens do campo de assinatura e extrair informações de assinatura usando a classe SignatureField com C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraindo Imagem do Campo de Assinatura

Aspose.PDF para C++ suporta a funcionalidade de assinar digitalmente os arquivos PDF usando a classe [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) e ao assinar o documento.

Para extrair informações de assinatura, introduzimos o método [ExtractImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a63f492fa6d3f83f0265b8e4f4c850293) na classe SignatureField.

Por favor, veja o seguinte trecho de código que demonstra os passos para extrair uma imagem do objeto [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field):

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

## Extrair Informações da Assinatura

Aspose.PDF para C++ permite extrair informações da assinatura. Para isso, introduzimos o método [ExtractCertificate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a73686c960036f755b6e800b84c27bee1) na classe [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field).

Por favor, veja o trecho de código a seguir que demonstra os passos para extrair o certificado do objeto SignatureField:

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