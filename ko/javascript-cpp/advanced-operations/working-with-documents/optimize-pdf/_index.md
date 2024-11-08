---
title: Optimize PDF using Aspose.PDF for JavaScript via C++ 
linktitle: Optimize PDF File
type: docs
weight: 10
url: /ko/javascript-cpp/optimize-pdf/
description: JavaScript 도구를 사용하여 빠른 웹 보기를 위해 PDF 파일을 최적화하고 압축합니다.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서 최적화

C++를 통한 JavaScript용 Aspose.PDF 툴킷을 사용하면 웹을 위해 PDF 콘텐츠를 최적화할 수 있습니다.

웹 최적화 또는 선형화는 웹 브라우저를 사용하여 온라인 브라우징에 적합하게 PDF 파일을 만드는 과정을 말합니다. 웹 디스플레이를 위해 파일을 최적화하려면:

1. 최적화할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfOptimize](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfoptimize/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예에서는 "ResultOptimize.pdf"입니다.

1. 다음으로, 'json.errorCode'가 0이면 DownloadFile은 이전에 지정한 이름이 부여됩니다. 'json.errorCode' 매개변수가 0이 아니면 파일에 오류가 발생하며, 이러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로 [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있도록 합니다.

다음 코드 스니펫은 PDF 문서를 최적화하는 방법을 보여줍니다.

```js

  var ffileOptimize = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일을 최적화하고 "ResultOptimize.pdf"로 저장합니다.*/
      const json = AsposePdfOptimize(event.target.result, e.target.files[0].name, "ResultOptimize.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*결과 파일을 다운로드할 링크를 만듭니다.*/
      DownloadFile(json.fileNameResult, "application/pdf");
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
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ?
          `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileOptimize = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일 최적화 및 "ResultOptimize.pdf"로 저장 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfOptimize', "params": [event.target.result, e.target.files[0].name, "ResultOptimize.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일 다운로드 링크 생성*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일을 다운로드하려면 여기를 클릭하십시오: " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```