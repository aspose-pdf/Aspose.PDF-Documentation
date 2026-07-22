---
title: Node.js에서 PDF 병합하는 방법
linktitle: PDF 파일 병합
type: docs
weight: 20
url: /ko/nodejs-cpp/merge-pdf/
description: 이 페이지에서는 Aspose.PDF for Node.js via C++를 사용하여 PDF 문서를 하나의 PDF 파일로 병합하는 방법을 설명합니다.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Node.js에서 두 개의 PDF를 하나의 PDF로 병합하거나 결합하기

다수의 문서를 다룰 때 파일을 결합하고 병합하는 작업은 매우 흔한 작업입니다. 때때로 문서와 이미지 작업을 하면서 스캔, 처리 및 정리 과정에서 여러 파일이 생성됩니다.
하지만 모든 것을 하나의 파일에 저장해야 한다면 어떨까요? 여러 문서를 인쇄하고 싶지 않다면요? Aspose.PDF for Node.js via C++를 사용하여 두 개의 PDF 파일을 연결하십시오.

두 개의 PDF를 병합하려는 경우, 사용할 수 있습니다. [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/) 함수. 
Node.js 환경에서 두 개의 PDF 파일을 병합하기 위해 다음 코드 스니펫을 확인하십시오.

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 병합될 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 병합 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. 두 PDF 파일을 병합합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultMerge.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 나타나는 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Merge two PDF-files and save the "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 병합될 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 함수를 호출합니다. [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. 두 PDF 파일을 병합합니다. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultMerge.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 나타나는 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Merge two PDF-files and save the "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```