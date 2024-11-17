---
title: Node.js에서 PDF를 Excel로 변환
linktitle: PDF를 Excel로 변환
type: docs
weight: 20
url: /ko/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-16"
description: Aspose.PDF for Node.js를 사용하여 PDF를 XLSX 형식으로 변환할 수 있습니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Node.js를 사용하여 PDF에서 스프레드시트 생성

**C++를 통한 Aspose.PDF for Node.js**는 PDF 파일을 Excel 파일로 변환하는 기능을 지원합니다.

{{% alert color="success" %}}
**온라인으로 PDF를 Excel로 변환해보세요**

Aspose.PDF for Node.js는 온라인 무료 애플리케이션 ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)를 제공하여 기능과 품질을 직접 확인해보실 수 있습니다.

[![Aspose.PDF 무료 앱을 사용한 PDF를 Excel로 변환](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## PDF를 XLSX로 변환

PDF 문서를 변환하려면 [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/) 함수를 사용할 수 있습니다.
 
다음 코드 스니펫을 확인하여 Node.js 환경으로 변환하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultPDFtoXlsX.xlsx"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보가 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 XlsX로 변환하고 "ResultPDFtoXlsX.xlsx"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultPDFtoXlsX.xlsx"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 XlsX로 변환하고 "ResultPDFtoXlsX.xlsx"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```