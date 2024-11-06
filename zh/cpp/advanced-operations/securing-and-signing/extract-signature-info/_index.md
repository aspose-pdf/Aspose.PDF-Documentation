---
title: 使用 Aspose.PDF for C++ 提取图像和签名信息
linktitle: 提取图像和签名信息
type: docs
weight: 30
url: zh/cpp/extract-image-and-signature-information/
description: 您可以使用 C++ 的 SignatureField 类从签名字段中提取图像和签名信息。
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从签名字段提取图像

Aspose.PDF for C++ 支持使用 [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) 类对 PDF 文件进行数字签名，并在签署文档时使用。

为了提取签名信息，我们在 SignatureField 类中引入了 [ExtractImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a63f492fa6d3f83f0265b8e4f4c850293) 方法。

请查看以下代码片段，其中展示了从 [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) 对象中提取图像的步骤：
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

## 提取签名信息

Aspose.PDF for C++ 允许提取签名信息。 为此，我们在 [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) 类中引入了 [ExtractCertificate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a73686c960036f755b6e800b84c27bee1) 方法。

请查看下面的代码片段，该代码片段演示了从 SignatureField 对象中提取证书的步骤：

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