---
title: Node.js에서 PDF를 PPTX로 변환
linktitle: PDF를 PowerPoint로 변환
type: docs
weight: 30
url: ko/nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-16"
description: Aspose.PDF는 Node.js 환경에서 직접 PDF를 PPTX 형식으로 변환할 수 있도록 합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**PDF를 PowerPoint로 온라인에서 변환해 보세요**

Aspose.PDF for Node.js는 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 작동 품질을 확인해 보실 수 있습니다.

[![Aspose.PDF 변환 PDF를 PPTX로 무료 앱과 함께](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## PDF를 PPTX로 변환

PDF 문서를 변환하려는 경우 [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/) 함수를 사용할 수 있습니다.

Node.js 환경에서 변환하기 위한 다음 코드 스니펫을 확인하세요.

**CommonJS:**

1. `require`을 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환될 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultPDFtoPptX.pptx"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 나타나면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 PptX로 변환하고 "ResultPDFtoPptX.pptx"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서, 'json.errorCode'가 0이면 작업 결과가 "ResultPDFtoPptX.pptx"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 PptX로 변환하고 "ResultPDFtoPptX.pptx"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```