---
title: JavaScript를 통해 C++로 PDF 페이지 삭제 
linktitle: PDF 페이지 삭제
type: docs
weight: 30
url: /javascript-cpp/delete-pages/
description: Aspose.PDF for JavaScript를 통해 C++로 PDF 파일에서 페이지를 삭제할 수 있습니다.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for JavaScript를 통해 C++로 PDF 파일에서 페이지를 삭제할 수 있습니다. 결과를 브라우저에서 직접 확인할 수 있습니다.

1. 'FileReader'를 생성합니다.
1. 삭제할 페이지 번호를 지정합니다.
1. [AsposePdfDeletePages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdeletepages/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예에서는 "ResultDeletePages.pdf"입니다.
1. 다음으로, 'json.errorCode'가 0이면, 지정한 이름으로 DownloadFile이 제공됩니다. 'json.errorCode' 매개변수가 0이 아니고, 그에 따라 파일에 오류가 발생하면, 이러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.

1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있게 합니다.

```js

  var ffileDeletePages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*문자열, 간격을 포함한 페이지 번호: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      const numPages = "1-3";
      /*배열, 페이지 번호의 배열*/
      /*const numPages = [1,3];*/
      /*번호, 페이지 번호*/
      /*const numPages = 1;*/
      /*1-3 페이지를 PDF 파일에서 삭제하고 "ResultOptimize.pdf"로 저장*/
      const json = AsposePdfDeletePages(event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages);
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*결과 파일을 다운로드할 수 있는 링크 생성*/
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
    const ffileDeletePages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /* 문자열, 페이지 번호를 포함한 구간: "7, 20, 22, 30-32, 33, 36-40, 46" */
        const numPages = "1-3";
        /* 배열, 페이지 번호의 배열 */
        /* const numPages = [1,3]; */
        /* 숫자, 페이지 번호 */
        /* const numPages = 1; */
        /* PDF 파일에서 페이지를 삭제하고 "ResultDeletePages.pdf - 웹 워커에 요청"으로 저장 */
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDeletePages',
            "params": [event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /* 결과 파일을 다운로드할 링크 만들기 */
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일을 다운로드하려면 여기를 클릭하세요 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```