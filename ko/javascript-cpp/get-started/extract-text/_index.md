---
title: JavaScript를 사용하여 PDF에서 텍스트 추출
linktitle: PDF에서 텍스트 추출
type: docs
weight: 10
url: /ko/javascript-cpp/extract-text/
description: 이 섹션은 JavaScript 도구를 사용하여 PDF 문서에서 텍스트를 추출하는 방법을 설명합니다.
lastmod: "2022-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서의 모든 페이지에서 텍스트 추출

PDF에서 텍스트를 추출하는 것은 쉽지 않습니다. 많은 PDF 리더가 PDF 이미지나 스캔된 PDF에서 텍스트를 추출할 수 없습니다. 그러나 **Aspose.PDF for JavaScript via C++** 도구를 사용하면 모든 PDF 파일에서 텍스트를 쉽게 추출할 수 있습니다.

코드 스니펫을 확인하고 PDF에서 텍스트를 추출하는 단계를 따르십시오:

1. 텍스트를 추출할 PDF 파일을 선택합니다.
1. 텍스트를 읽기 위한 'FileReader'를 생성합니다.
1. [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfextracttext/) 함수가 실행됩니다.

1. 다음으로, 'json.errorCode'가 0이면 'json.extractText'는 추출된 내용을 포함합니다. 'json.errorCode' 매개변수가 0이 아니고, 그에 따라 파일에 오류가 있는 경우, 그러한 오류에 대한 정보는 'json.errorText'에 포함됩니다.
1. 결과적으로, PDF에서 추출된 텍스트가 포함된 문자열을 받게 됩니다.

```js

    var ffileExtract = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일에서 텍스트 추출*/
        const json = AsposePdfExtractText(event.target.result, e.target.files[0].name);
        if (json.errorCode == 0) document.getElementById('output').textContent = json.extractText;
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## 웹 워커 사용

```js

    /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ?
          evt.data.json.extractText :
          `오류: ${evt.data.json.errorText}`; 

    /*이벤트 핸들러*/
    const ffileExtract = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일에서 텍스트 추출 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```