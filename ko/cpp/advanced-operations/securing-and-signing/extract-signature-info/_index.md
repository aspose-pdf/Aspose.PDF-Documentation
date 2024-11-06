---
title: Aspose.PDF for C++를 사용하여 이미지 및 서명 정보 추출
linktitle: 이미지 및 서명 정보 추출
type: docs
weight: 30
url: ko/cpp/extract-image-and-signature-information/
description: 서명 필드에서 이미지를 추출하고 C++의 SignatureField 클래스를 사용하여 서명 정보를 추출할 수 있습니다.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 서명 필드에서 이미지 추출

Aspose.PDF for C++는 [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) 클래스를 사용하여 PDF 파일에 디지털 서명을 지원하며 문서에 서명할 수 있습니다.

서명 정보를 추출하기 위해 SignatureField 클래스에 [ExtractImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a63f492fa6d3f83f0265b8e4f4c850293) 메서드를 도입했습니다.

다음 코드 스니펫은 [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) 객체에서 이미지를 추출하는 단계를 보여줍니다:

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

## 서명 정보 추출

Aspose.PDF for C++는 서명 정보를 추출할 수 있습니다. 이를 위해 [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) 클래스에 [ExtractCertificate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a73686c960036f755b6e800b84c27bee1) 메서드를 도입했습니다.

SignatureField 객체에서 인증서를 추출하는 단계를 보여주는 다음 코드 조각을 확인하십시오:

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