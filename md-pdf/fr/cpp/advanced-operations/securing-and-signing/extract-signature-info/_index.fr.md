---
title: Extraire les informations d'image et de signature en utilisant Aspose.PDF pour C++
linktitle: Extraire les informations d'image et de signature
type: docs
weight: 30
url: /cpp/extract-image-and-signature-information/
description: Vous pouvez extraire des images à partir du champ de signature et extraire des informations de signature en utilisant la classe SignatureField avec C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraction de l'image du champ de signature

Aspose.PDF pour C++ prend en charge la fonctionnalité de signature numérique des fichiers PDF en utilisant la classe [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) et lors de la signature du document.

Afin d'extraire des informations de signature, nous avons introduit la méthode [ExtractImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a63f492fa6d3f83f0265b8e4f4c850293) à la classe SignatureField.

Veuillez consulter l'extrait de code suivant qui démontre les étapes pour extraire une image de l'objet [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) :

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

## Extraire les informations de signature

Aspose.PDF pour C++ permet d'extraire des informations de signature. Pour cela, nous avons introduit la méthode [ExtractCertificate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a73686c960036f755b6e800b84c27bee1) dans la classe [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field).

Veuillez consulter l'extrait de code suivant qui démontre les étapes pour extraire le certificat de l'objet SignatureField :

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