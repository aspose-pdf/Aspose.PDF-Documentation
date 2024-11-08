---
title: JavaScript를 통해 C++로 PDF 페이지 회전 
linktitle: PDF 페이지 회전
type: docs
weight: 50
url: /ko/javascript-cpp/rotate-pages/
description: 이 주제는 JavaScript를 통해 C++로 기존 PDF 파일에서 페이지 방향을 프로그래밍 방식으로 회전하는 방법을 설명합니다. 
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

이 섹션은 JavaScript를 통해 C++를 사용하여 기존 PDF 파일에서 페이지 방향을 가로에서 세로로 또는 그 반대로 변경하는 방법을 설명합니다.

1. 'FileReader'를 만듭니다.
1. [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfrotateallpages/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예에서는 "ResultRotation.pdf"입니다.

1. 다음으로, 'json.errorCode'가 0이면 DownloadFile은 이전에 지정한 이름으로 제공됩니다. 'json.errorCode' 매개 변수가 0이 아니면 파일에 오류가 발생하며, 이러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 생성된 파일을 사용자의 운영 체제로 다운로드할 수 있게 합니다.

```js

  var ffileRotateAllPages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*모든 페이지 PDF 파일을 회전하고 "ResultRotation.pdf"로 저장합니다.*/
      const json = AsposePdfRotateAllPages(event.target.result, e.target.files[0].name, Module.Rotation.on270, "ResultRotation.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*결과 파일을 다운로드할 링크를 만듭니다.*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## Web Workers 사용하기

```js

    /*Web Worker 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Worker에서 오류 발생: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ?
          `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileRotateAllPages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const rotation = 'Module.Rotation.on270';
        /*PDF 페이지 회전 및 "ResultRotation.pdf"로 저장 - Web Worker에 요청*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfRotateAllPages',
            "params": [event.target.result, e.target.files[0].name, rotation, "ResultRotation.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일을 다운로드할 링크 만들기*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일을 다운로드하려면 여기를 클릭하세요: " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```