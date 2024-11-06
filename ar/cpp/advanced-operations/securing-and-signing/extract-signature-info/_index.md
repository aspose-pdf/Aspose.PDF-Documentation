---
title: استخراج معلومات الصورة والتوقيع باستخدام Aspose.PDF لـ C++
linktitle: استخراج معلومات الصورة والتوقيع
type: docs
weight: 30
url: ar/cpp/extract-image-and-signature-information/
description: يمكنك استخراج الصور من حقل التوقيع واستخراج معلومات التوقيع باستخدام فئة SignatureField مع C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج الصورة من حقل التوقيع

يدعم Aspose.PDF لـ C++ ميزة التوقيع الرقمي لملفات PDF باستخدام فئة [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) وأثناء توقيع المستند.

لاستخراج معلومات التوقيع، قمنا بتقديم طريقة [ExtractImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a63f492fa6d3f83f0265b8e4f4c850293) إلى فئة SignatureField.

يرجى الاطلاع على مقتطف الشيفرة التالي الذي يوضح خطوات استخراج صورة من كائن [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field):

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

## استخراج معلومات التوقيع

تتيح Aspose.PDF for C++ استخراج معلومات التوقيع. ```
لهذا، قمنا بتقديم الطريقة [ExtractCertificate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a73686c960036f755b6e800b84c27bee1) إلى فئة [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field).

يرجى إلقاء نظرة على مقتطف الكود التالي الذي يوضح الخطوات لاستخراج الشهادة من كائن SignatureField:

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
```