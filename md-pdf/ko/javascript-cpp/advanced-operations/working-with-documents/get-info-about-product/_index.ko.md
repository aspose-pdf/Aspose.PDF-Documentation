---
title: JavaScript를 사용하여 제품 정보 가져오기
linktitle: 제품 정보 가져오기
type: docs
weight: 70
url: /javascript-cpp/get-info-about-product/
description: 이 주제는 C++을 통한 Aspose.PDF for JavaScript로 제품 정보를 얻는 방법을 보여줍니다.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

이 주제는 JavaScript를 사용하여 제품 정보를 얻는 방법을 설명합니다.

```js

    /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode !== 0) ? `오류: ${evt.data.json.errorText}` :
                          "제품      : " + evt.data.json.product
                      + "\n가족       : " + evt.data.json.family
                      + "\n버전      : " + evt.data.json.version
                      + "\n출시일 : " + evt.data.json.releasedate
                      + "\n생산자     : " + evt.data.json.producer
                      + "\n라이센스 여부  : " + evt.data.json.islicensed;

    /*이벤트 핸들러*/
    const onAsposePdfAbout = e => {
      /*제품 정보 가져오기 - 웹 워커에 요청*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAbout', "params": [] }, []);
    };
```


다음 JavaScript 코드 스니펫은 제품에 대한 정보를 얻는 간단한 예를 보여줍니다:

1. [AsposePdfAbout](https://reference.aspose.com/pdf/javascript-cpp/misc/asposepdfabout/) 함수가 실행됩니다.
1. 얻을 수 있는 제품 정보:
- 제품 이름
- 제품군
- 제품 버전
- 출시일
- 전체 이름/제작자
- 제품이 라이센스됨
1. 다음으로, 'json.errorCode'가 0이면 제품에 대한 정보를 얻을 수 있습니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있는 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.

```js

  var onAsposePdfAbout = function () {
    /*제품에 대한 정보 얻기*/
    const json = AsposePdfAbout();
    /* JSON
    제품 이름          : json.product
    제품군             : json.family
    제품 버전          : json.version
    출시일             : json.releasedate
    전체 이름/제작자   : json.producer
    제품이 라이센스됨  : json.islicensed
    */
    if (json.errorCode == 0) document.getElementById('output').textContent = 
                    "제품         : " + json.product
                + "\n제품군       : " + json.family
                + "\n버전         : " + json.version
                + "\n출시일       : " + json.releasedate
                + "\n제작자       : " + json.producer
                + "\n라이센스됨   : " + json.islicensed;
    else document.getElementById('output').textContent = json.errorText;
  }
```