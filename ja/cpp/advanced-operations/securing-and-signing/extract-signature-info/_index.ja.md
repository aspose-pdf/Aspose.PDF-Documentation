---
title: Aspose.PDF for C++ を使用して画像と署名情報を抽出する
linktitle: 画像と署名情報の抽出
type: docs
weight: 30
url: /cpp/extract-image-and-signature-information/
description: 署名フィールドから画像を抽出し、SignatureField クラスを使用して署名情報を抽出できます。
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 署名フィールドから画像を抽出する

Aspose.PDF for C++ は、[SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) クラスを使用して PDF ファイルにデジタル署名を行う機能をサポートしており、ドキュメントに署名する際に使用します。

署名情報を抽出するために、SignatureField クラスに [ExtractImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a63f492fa6d3f83f0265b8e4f4c850293) メソッドを導入しました。

次のコードスニペットをご覧ください。これは [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) オブジェクトから画像を抽出する手順を示しています。

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

## 署名情報の抽出

Aspose.PDF for C++ を使用すると、署名情報を抽出できます。 このために、[SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) クラスに [ExtractCertificate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a73686c960036f755b6e800b84c27bee1) メソッドを導入しました。

SignatureField オブジェクトから証明書を抽出する手順を示す次のコードスニペットをご覧ください。

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