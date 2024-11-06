---
title: JavaScript를 통해 C++로 PDF에 페이지 번호 추가 
linktitle: 페이지 번호 추가
type: docs
weight: 100
url: ko/javascript-cpp/add-page-number/
description: Aspose.PDF for JavaScript via C++를 사용하여 AsposePdfAddPageNum을 통해 PDF 파일에 페이지 번호 스탬프를 추가할 수 있습니다.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

모든 문서에는 페이지 번호가 있어야 합니다. 페이지 번호는 독자가 문서의 여러 부분을 쉽게 찾을 수 있도록 해줍니다.

**Aspose.PDF for JavaScript via C++**는 [AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/)을 사용하여 페이지 번호를 추가할 수 있습니다.

1. 'FileReader'를 생성합니다.
1. [AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예제에서는 "ResultAddPageNum.pdf"입니다.

1. 다음으로, 'json.errorCode'가 0이면 DownloadFile은 이전에 지정한 이름을 갖게 됩니다. 'json.errorCode' 매개변수가 0이 아니고 파일에 오류가 있는 경우, 해당 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있게 해줍니다.

```js
  var ffileAddPageNum = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일에 페이지 번호 추가하고 "ResultAddPageNum.pdf"로 저장*/
      const json = AsposePdfAddPageNum(event.target.result, e.target.files[0].name, "ResultAddPageNum.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*결과 파일을 다운로드할 링크 생성*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## 웹 워커 사용하기

```js

    /* 웹 워커 생성 */
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ?
          `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `오류: ${evt.data.json.errorText}`;

    /* 이벤트 핸들러 */
    const ffileAddPageNum = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /* PDF 파일에 페이지 번호를 추가하고 "ResultAddPageNum.pdf"로 저장 - 웹 워커 요청 */
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddPageNum', "params": [event.target.result, e.target.files[0].name, "ResultAddPageNum.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /* 결과 파일을 다운로드할 링크 생성 */
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