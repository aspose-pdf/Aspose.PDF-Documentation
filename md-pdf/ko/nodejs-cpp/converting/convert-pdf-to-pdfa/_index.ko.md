---
title: PDF를 PDF/A 형식으로 변환하기 (Node.js)
linktitle: PDF를 PDF/A 형식으로 변환하기
type: docs
weight: 100
url: /nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-16"
description: 이 주제는 Node.js 환경에서 PDF 파일을 PDF/A 규격의 PDF 파일로 변환할 수 있도록 Aspose.PDF를 사용하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Node.js**를 사용하면 PDF 파일을 <abbr title="전자 문서의 아카이빙을 위한 휴대용 문서 형식">PDF/A</abbr> 규격의 PDF 파일로 변환할 수 있습니다.

{{% alert color="success" %}}
**PDF를 PDF/A로 온라인 변환 시도하기**

Aspose.PDF for Node.js는 ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)라는 무료 온라인 애플리케이션을 제공하며, 이곳에서 기능과 품질을 확인해볼 수 있습니다.

[![무료 앱으로 Aspose.PDF를 사용하여 PDF를 PDF/A로 변환하기](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## PDF를 PDF/A 형식으로 변환

PDF 문서를 변환하려는 경우 [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/) 함수를 사용할 수 있습니다.
 
다음 코드 스니펫을 확인하여 Node.js 환경으로 변환하세요.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환될 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/)를 호출합니다.
1. PDF 파일을 복구합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과가 "ResultConvertToPDFA.pdf"에 저장됩니다. 변환 과정에서 검증이 수행되며, 검증 결과는 "ResultConvertToPDFALog.xml"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 PDF/A(1A)로 변환하고 "ResultConvertToPDFA.pdf"로 저장합니다*/
      /*변환 과정에서 검증도 수행되며, 결과는 "ResultConvertToPDFALog.xml"에 저장됩니다*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/)를 호출합니다.
1. PDF 파일을 복구합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과가 "ResultConvertToPDFA.pdf"에 저장됩니다. 변환 과정에서 검증이 수행되며, 검증 결과는 "ResultConvertToPDFALog.xml"로 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 PDF/A(1A)로 변환하고 "ResultConvertToPDFA.pdf"로 저장합니다.*/
  /*변환 과정에서 검증도 수행되며, "ResultConvertToPDFA.xml"에 저장됩니다.*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```