---
title: Node.js에서 PDF에서 표 추출하기
linktitle: PDF에서 표 추출하기
type: docs
weight: 10
url: /nodejs-cpp/extract-tables-from-the-pdf-file/
description: Aspose.PDF for Node.js via C++ 툴킷을 사용하여 PDF를 CSV로 변환하는 방법.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF를 CSV 파일로 변환하면서 표 추출하기

### PDF를 CSV로 변환하기

PDF에 표가 있는 경우 별도의 CSV 파일에 저장됩니다. PDF 문서를 변환하려면 [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/) 함수를 사용할 수 있습니다.
다음 코드 스니펫을 확인하여 Node.js 환경에서 PDF 파일을 변환하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 변환할 PDF 파일의 이름을 지정합니다.
1. `AsposePdf`를 Promise로 호출하고 파일 변환 작업을 수행합니다. 성공하면 객체를 수신합니다.

1. 함수 [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultPDFtoXlsX.xlsx"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*템플릿 "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... 형식 페이지 번호), TAB을 구분자로 사용하여 PDF 파일을 CSV로 변환(테이블 추출)하고 저장합니다.*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.

1. 변환할 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/)를 호출합니다.
1. PDF 파일을 변환합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultPDFtoXlsX.xlsx"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 CSV로 변환(테이블 추출)하고 "ResultPdfTablesToCSV{0:D2}.csv" 템플릿으로 저장합니다. 구분자는 TAB이며, 페이지 번호는 {0}, {0:D2}, {0:D3}, ... 형식입니다.*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```