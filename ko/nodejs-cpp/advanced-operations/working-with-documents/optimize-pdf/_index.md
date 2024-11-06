---

title: Aspose.PDF를 사용하여 Node.js용 PDF 최적화 via C++  
linktitle: PDF 파일 최적화  
type: docs  
weight: 10  
url: ko/nodejs-cpp/optimize-pdf/  
description: Node.js 환경에서 빠른 웹 뷰를 위해 PDF 파일을 최적화하고 압축합니다.  
lastmod: "2023-11-16"  
sitemap:  
    changefreq: "monthly"  
    priority: 0.7  
---

## PDF 문서 최적화

Aspose.PDF for Node.js via C++ 툴킷은 Node.js 환경에 맞춰 PDF 내용을 최적화할 수 있게 해줍니다.

최적화 또는 선형화는 PDF 파일을 웹 브라우저를 사용한 온라인 검색에 적합하게 만드는 과정을 의미합니다.

PDF를 최적화하려는 경우 [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/) 함수를 사용할 수 있습니다.  
Node.js 환경에서 PDF 파일을 최적화하기 위한 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.  
1. 최적화할 PDF 파일의 이름을 지정합니다.  

1. `AsposePdf`를 Promise로 호출하고 파일 최적화 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/)를 호출합니다.
1. PDF 파일을 최적화합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultOptimize.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 발생한 경우 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDF 파일을 최적화하고 "ResultOptimize.pdf"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 최적화할 PDF 파일의 이름을 지정합니다.

1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수 [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/)를 호출합니다.
1. PDF 파일을 최적화합니다. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultOptimize.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 따라서 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF 파일을 최적화하고 "ResultOptimize.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```