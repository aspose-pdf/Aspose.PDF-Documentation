---
title: PDF/A를 PDF 형식으로 변환하기
linktitle: PDF/A를 PDF 형식으로 변환하기
type: docs
weight: 110
url: ko/nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-16"
description: 이 주제에서는 Aspose.PDF가 Node.js 환경에서 PDF/A 파일을 PDF 문서로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF/A를 PDF 형식으로 변환하기

PDF 문서를 변환하려는 경우, [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/) 함수를 사용할 수 있습니다. Node.js 환경에서 변환하기 위한 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.

1. 함수 [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면, 작업의 결과는 "ResultConvertToPDF.pdf"로 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF/A 파일을 PDF로 변환하고 "ResultConvertToPDF.pdf"로 저장*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환될 PDF/A 파일의 이름을 지정합니다.

1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultConvertToPDF.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나는 경우 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*PDF/A 파일을 PDF로 변환하고 "ResultConvertToPDF.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```