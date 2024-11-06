---
title: PDF를 디지털 서명하는 방법
linktitle: PDF 디지털 서명
type: docs
weight: 10
url: ko/cpp/digitally-sign-pdf-file/
description: C++를 사용하여 PDF 문서에 디지털 서명합니다. C++를 사용하여 디지털 서명된 PDF를 확인하거나 검증하십시오.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 디지털 서명을 사용하여 PDF 서명하기

PDF 문서를 서명하여 콘텐츠를 확인하거나 Aspose.PDF로 문서를 승인할 수 있습니다.

Aspose.PDF for C++는 SignatureField 클래스를 사용하여 PDF 파일에 디지털 서명을 지원합니다. 또한 PKCS12 인증서로 PDF 파일을 인증할 수 있습니다. [Adobe Acrobat에서 서명 및 보안 추가](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6)와 유사한 방식으로 가능합니다.

PDF 서명을 위해 [PdfFileSignature](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_signature) 클래스를 사용하십시오.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SecuringAndSigning::SignDocument() {

// 경로 이름을 위한 문자열.

String _dataDir("C:\\Samples\\");


String inFile = _dataDir + u"DigitallySign.pdf";

String outFile = _dataDir + u"DigitallySign_out.pdf";


auto document = MakeObject<Document>(inFile);


auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020"); // PKCS7/PKCS7Detached 사용
























// 객체

System::Drawing::Rectangle rect(300, 100, 400, 200);

signature->Sign(1, true, rect, pkcs);

// 출력 PDF 파일 저장

signature->Save(outFile);
}
```

## 디지털 서명에 타임스탬프 추가

### 타임스탬프와 함께 PDF 디지털 서명하는 방법

Aspose.PDF for C++는 타임스탬프 서버나 웹 서비스를 사용하여 PDF에 디지털 서명을 지원합니다.

타임스탬프는 문서에 서명한 날짜와 시간을 나타내는 데 사용됩니다. 신뢰할 수 있는 타임스탬프는 PDF의 내용이 특정 시점에 존재했으며 그 이후로 변경되지 않았음을 증명합니다.

신뢰할 수 있는 타임스탬프를 디지털 서명이나 문서에 추가하려면 [TimestampSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.timestamp_settings) 클래스를 사용하십시오.

다음 코드 스니펫은 타임스탬프를 얻고 PDF 문서에 추가하는 방법을 보여줍니다:

```cpp
void SecuringAndSigning::SignWithTimeStampServer() {

// 경로 이름을 위한 문자열.

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"SimpleResume.pdf");

auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020");


auto timestampSettings = MakeObject<TimestampSettings>(u"https://freetsa.org/tsr", String::Empty); // User/Password can
























// 생략될 수 있음

pkcs->set_TimestampSettings(timestampSettings);


System::Drawing::Rectangle rect(100, 100, 200, 100);

// 세 가지 서명 유형 중 하나 생성

signature->Sign(1, u"서명 이유", u"연락처", u"위치", true, rect, pkcs);

// 출력 PDF 파일 저장

signature->Save(_dataDir + u"DigitallySignWithTimeStamp_out.pdf");
}
```