---
title: JavaScript를 통해 C++로 PDF 병합하는 방법
linktitle: PDF 파일 병합
type: docs
weight: 20
url: /ko/javascript-cpp/merge-pdf/
description: 이 페이지는 Aspose.PDF for JavaScript를 통해 C++로 PDF 문서를 단일 PDF 파일로 병합하는 방법을 설명합니다.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## JavaScript에서 두 개의 PDF를 하나의 PDF로 병합 또는 결합

많은 문서와 작업할 때 파일을 결합하고 병합하는 것은 매우 인기 있는 작업입니다. 때로는 문서와 이미지를 작업할 때 스캔, 처리, 정리되며 여러 파일이 생성됩니다.
하지만 모든 것을 하나의 파일에 저장해야 할 경우는 어떨까요? 또는 여러 문서를 인쇄하고 싶지 않은 경우는 어떻게 하나요? Aspose.PDF for JavaScript를 통해 C++로 두 개의 PDF 파일을 연결하세요.

이 JavaScript 도구는 Aspose.PDF for JavaScript를 통해 C++로 두 개의 PDF 파일을 단일 PDF 문서로 병합할 수 있습니다. 예제는 JavaScript로 작성되었습니다.

1. 병합할 PDF 파일을 선택합니다.
1. 'FileReader'를 만듭니다.

1. [AsposePdfMerge2Files](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfmerge2files/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정되며, 이 예제에서는 "ResultMerge.pdf"입니다.
1. 다음으로 'json.errorCode'가 0인 경우, DownloadFile은 이전에 지정한 이름을 갖게 됩니다. 'json.errorCode' 매개변수가 0이 아니면 파일에 오류가 발생하며, 이러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로 [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자 운영 체제에 결과 파일을 다운로드할 수 있도록 합니다.

다음 코드 스니펫은 PDF 파일을 연결하는 방법을 보여줍니다:

```js

  var ffileMerge = function (e) {
    const file_reader = new FileReader();
    function readFile(index) {
      /*단 두 개의 파일만*/
      if (index >= e.target.files.length || index >= 2) {
        /*두 PDF 파일을 병합하고 "ResultMerge.pdf"로 저장*/
        const json = AsposePdfMerge2Files(undefined, undefined, e.target.files[0].name, e.target.files[1].name, "ResultMerge.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드할 링크 생성*/
        DownloadFile(json.fileNameResult, "application/pdf");
        return;
      }
      const file = e.target.files[index];
      file_reader.onload = function (event) {
        /*BLOB에서 파일 준비(저장)*/
        AsposePdfPrepare(event.target.result, file.name);
        readFile(index + 1)
      }
      file_reader.readAsArrayBuffer(file);
    }
    readFile(0);
  }
```


### 웹 워커 사용하기

```js

    /* 웹 워커 생성하기 */
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ? 
          `결과:\n${(evt.data.operation == 'AsposePdfPrepare') ? 
                      fileProcess('AsposePdfMerge2Files', evt.data.json.optdata[0].file, {"fileName2": evt.data.json.fileNameResult}) ?? '잠시 기다려 주세요...' : 
                      DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0]) /*AsposePdfMerge2Files*/
                    }` :
          `오류: ${evt.data.json.errorText}`;

    /* 이벤트 핸들러. 두 파일만 병합됩니다. 파일이 하나만 선택되면, 해당 파일을 사용합니다. 두 번째 파일을 위해서는 AsposePdfPrepare을 수행해야 합니다. */
    const ffileMerge = evt => fileProcess('AsposePdfPrepare',  evt.target.files[(evt.target.files.length == 1) ? 0 : 1],
                                          [{"operation": 'AsposePdfMerge2Files', "file": evt.target.files[0]}])
    /* 웹 워커 요청 */
    const fileProcess = (operation, ffile, optdata) => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        if (operation == 'AsposePdfPrepare')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, "params": [event.target.result, ffile.name, optdata] },
                  [event.target.result]
                );
        else if (operation == 'AsposePdfMerge2Files')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, 
                    "params": [event.target.result, undefined, ffile.name, (optdata === undefined) ? ffile.name : optdata.fileName2,
                                `Result${operation}.pdf`] },
                  [event.target.result]
                );
      }
      file_reader.readAsArrayBuffer(ffile);
    }

    /* 결과 파일을 다운로드할 수 있는 링크 생성하기 */
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일 다운로드를 위해 여기를 클릭하세요: " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```