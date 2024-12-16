---
title: Extract Image and Signature Information using Aspose.PDF for C++
linktitle: Extract Image and Signature Information
type: docs
weight: 30
url: /cpp/extract-image-and-signature-information/
description: You may extract images from the signature field and extract signature information using the SignatureField class with C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extracting Image from Signature Field

Aspose.PDF for C++ supports the feature to digitally sign the PDF files using the [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) class and while signing the document.

In order to extract signature information, we have introduced the [ExtractImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a63f492fa6d3f83f0265b8e4f4c850293) method to the SignatureField class.

Please take a look at the following code snippet which demonstrates the steps to extract an image from the [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) object:

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

## Extract Signature Information

Aspose.PDF for C++ allows extracting signature information. For this, we have introduced the [ExtractCertificate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field#a73686c960036f755b6e800b84c27bee1) method to the [SignatureField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.signature_field) class. 

Please take a look at the following code snippet which demonstrates the steps to extract the certificate from SignatureField object:

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
