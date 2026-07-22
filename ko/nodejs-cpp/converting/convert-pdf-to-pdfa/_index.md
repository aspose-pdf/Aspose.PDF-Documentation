---
title: Node.js에서 PDF를 PDF/A 형식으로 변환합니다
linktitle: PDF를 PDF/A 형식으로 변환합니다
type: docs
weight: 100
url: /ko/nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2026-07-18"
description: 이 주제에서는 Aspose.PDF가 Node.js 환경에서 PDF 파일을 PDF/A 규격을 준수하는 PDF 파일로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Node.js**는 PDF 파일을 다음 형식으로 변환할 수 있게 해줍니다 <abbr title="Portable Document Format for Archiving of electronic documents">PDF/A</abbr> 규정 준수 PDF 파일. 

{{% alert color="success" %}}
**PDF를 PDF/A로 온라인 변환해 보세요**

Aspose.PDF for Node.js는 온라인 무료 애플리케이션을 제공합니다 ["PDF를 PDF/A-1A로"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), 여기서 기능과 품질을 직접 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 PDF/A로 무료 앱으로](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## PDF를 PDF/A 형식으로 변환

PDF 문서를 변환하려는 경우, 다음을 사용할 수 있습니다 [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/) 함수. 
Node.js 환경에서 변환하려면 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 변환될 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로 파일 변환 작업을 수행하고, 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. PDF 파일을 복구합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultConvertToPDFA.pdf"에 저장됩니다. 변환 과정에서 검증이 수행되며, 검증 결과는 "ResultConvertToPDFALog.xml"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 나타나는 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
      /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 변환될 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. PDF 파일을 복구합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultConvertToPDFA.pdf"에 저장됩니다. 변환 과정에서 검증이 수행되며, 검증 결과는 "ResultConvertToPDFALog.xml"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 나타나는 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
  /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```





