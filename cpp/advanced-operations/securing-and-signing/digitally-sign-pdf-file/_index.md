---
title: How to digitally sign PDF
linktitle: Digitally sign PDF
type: docs
weight: 10
url: /cpp/digitally-sign-pdf-file/
description: Digitally sign PDF documents using C++. Verify, or validate the digitally sign PDFs using C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Sign PDF with digital signatures

You can sign the PDF document to confirm its content, or you can approve the document with Aspose.PDF.

Aspose.PDF for C++ supports the feature to digitally sign the PDF files using the SignatureField class. You can also certify a PDF file with a PKCS12-Certificate. Something similar to [Adding Signatures and Security in Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6). 

Use the [PdfFileSignature](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_signature) class for signing your PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SecuringAndSigning::SignDocument() {
	// String for path name.
	String _dataDir("C:\\Samples\\");

	String inFile = _dataDir + u"DigitallySign.pdf";
	String outFile = _dataDir + u"DigitallySign_out.pdf";

	auto document = MakeObject<Document>(inFile);

	auto signature = MakeObject<PdfFileSignature>(document);

	auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020"); // Use PKCS7/PKCS7Detached
																								// objects
	System::Drawing::Rectangle rect(300, 100, 400, 200);
	signature->Sign(1, true, rect, pkcs);
	// Save output PDF file
	signature->Save(outFile);
}
```

## Add timestamp to digital signature

### How to digitally sign a PDF with timestamp

Aspose.PDF for C++ supports to digitally sign the PDF with a timestamp server or Web service.

Timestamps are used to indicate the date and time when you signed the document. Reliable timestamping proves that the content of your PDFs existed at a specific point in time and has not changed since then.

Use the [TimestampSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.timestamp_settings) class for adding trusted time stamp to digital signatures or documents.

Please take a look at the following code snippet which obtains timestamp and adds it to PDF document:

```cpp
void SecuringAndSigning::SignWithTimeStampServer() {

	// String for path name.
	String _dataDir("C:\\Samples\\");
	auto document = MakeObject<Document>(_dataDir + u"SimpleResume.pdf");
	auto signature = MakeObject<PdfFileSignature>(document);

	auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020");

	auto timestampSettings = MakeObject<TimestampSettings>(u"https://freetsa.org/tsr", String::Empty); // User/Password can
																								// be omitted
	pkcs->set_TimestampSettings(timestampSettings);

	System::Drawing::Rectangle rect(100, 100, 200, 100);
	// Create any of the three signature types
	signature->Sign(1, u"Signature Reason", u"Contact", u"Location", true, rect, pkcs);
	// Save output PDF file
	signature->Save(_dataDir + u"DigitallySignWithTimeStamp_out.pdf");
}
```
