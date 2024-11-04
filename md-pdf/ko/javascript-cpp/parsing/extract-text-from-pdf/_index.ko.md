---
title: PDF에서 텍스트 추출하기 (JavaScript 사용)
linktitle: PDF에서 텍스트 추출
type: docs
weight: 30
url: /javascript-cpp/extract-text-from-pdf/
description: 이 문서에서는 Aspose.PDF for JavaScript를 사용하여 PDF 문서에서 텍스트를 추출하는 다양한 방법을 설명합니다.
lastmod: "2023-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에서 텍스트 추출하기

PDF 문서에서 텍스트를 추출하는 것은 매우 일반적이고 유용한 작업입니다.
PDF에서 텍스트를 추출하는 것은 검색 및 가용성을 향상시키는 것부터 비즈니스, 연구, 정보 관리 등의 다양한 분야에서 데이터의 분석 및 자동화를 가능하게 하는 것까지 다양한 목적을 수행합니다.

PDF 문서에서 텍스트를 추출하고자 하는 경우, [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/) 함수를 사용할 수 있습니다.
다음 코드 스니핏을 확인하여 JavaScript를 통해 C++로 PDF 파일에서 텍스트를 추출하십시오.

1. 'FileReader' 생성하기.

1. [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/) 함수가 실행됩니다.
1. 다음으로, 'json.errorCode'가 0이면, 결과 파일에 대한 링크를 얻을 수 있습니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있을 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.

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

## 웹 워커 사용하기

```js

    /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
        (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ?
            evt.data.json.extractText :
            `오류: ${evt.data.json.errorText}`; 

    /*이벤트 핸들러*/
    const ffileExtract = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*PDF 파일에서 텍스트 추출 - 웹 워커에 요청*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
            [event.target.result]
        );
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```