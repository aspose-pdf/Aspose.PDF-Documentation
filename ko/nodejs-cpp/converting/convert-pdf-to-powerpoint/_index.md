---
title: Node.js에서 PDF를 PPTX로 변환
linktitle: PDF를 PowerPoint로 변환
type: docs
weight: 30
url: /ko/nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-18"
description: Aspose.PDF는 Node.js 환경에서 직접 Node.js를 사용하여 PDF를 PPTX 형식으로 변환할 수 있게 합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**온라인에서 PDF를 PowerPoint로 변환해 보세요**

Aspose.PDF for Node.js는 온라인 무료 애플리케이션을 제공합니다 ["PDF를 PPTX로"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), 여기서 기능과 품질을 직접 확인해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 PPTX로 무료 앱으로](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## PDF를 PPTX로 변환

PDF 문서를 변환하려는 경우, 다음을 사용할 수 있습니다 [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/) 함수. 
Node.js 환경에서 변환하려면 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 변환될 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로 파일 변환 작업을 수행하고, 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. PDF 파일을 변환합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 “ResultPDFtoPptX.pptx”에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 발생하면 오류 정보가 ‘json.errorText’에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 변환될 PDF 파일의 이름을 지정하십시오
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. PDF 파일을 변환합니다. 따라서 ‘json.errorCode’가 0이면 작업 결과가 “ResultPDFtoPptX.pptx”에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 발생하면 오류 정보가 ‘json.errorText’에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```