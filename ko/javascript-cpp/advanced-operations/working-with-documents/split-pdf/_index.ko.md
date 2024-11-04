---
title: 자바스크립트를 사용하여 PDF 분할
linktitle: PDF 파일 분할
type: docs
weight: 30
url: /javascript-cpp/split-pdf/
description: 이 주제는 C++를 통한 Aspose.PDF를 사용하여 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.
lastmod: "2022-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 자바스크립트를 사용하여 PDF를 두 파일로 분할

이 주제는 자바스크립트를 사용하여 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다. 현재, 우리는 두 부분으로 분할하는 것을 지원합니다. 이는 `pageToSplit`이 분할을 위한 마커임을 의미합니다. 첫 번째 파일은 1부터 `pageToSplit`까지의 모든 페이지를 포함하고, 두 번째 파일은 나머지 페이지를 가집니다.

분할 작업은 문서의 페이지 수에 따라 달라지며 매우 시간이 많이 소요될 수 있습니다. 따라서, 우리는 웹 워커 사용을 강력히 권장합니다.

제공된 코드 스니펫은 자바스크립트에서 웹 워커를 사용하여 PDF 파일을 두 개의 개별 PDF 파일로 분할하고 결과 파일을 다운로드할 수 있는 옵션을 사용자에게 제공하는 예제입니다.
 다음은 코드 단계입니다:

1. 웹 워커 생성. 웹 워커는 "AsposePDFforJS.js" 스크립트 파일을 사용하여 초기화됩니다. 이 웹 워커는 PDF 파일 분할 작업을 백그라운드에서 처리합니다. 우리의 예제에서는 워커에서 발생하는 모든 오류가 캡처되어 콘솔에 기록됩니다.
1. 메시지 처리. 웹 워커는 onmessage 이벤트 핸들러를 사용하여 메시지를 수신 대기하도록 설정됩니다. 웹 페이지로부터 메시지를 받으면 요청을 처리하고 응답을 메인 스레드로 다시 보냅니다.
1. 파일 분할 이벤트 핸들러. 사용자가 분할할 PDF 파일을 선택할 때 ffileSplit 이벤트 핸들러가 트리거됩니다. 선택된 PDF 파일을 FileReader를 사용하여 읽고 파일 내용 및 관련 매개변수(예: 분할할 페이지 수 및 출력 파일 이름)를 웹 워커로 postMessage 호출을 통해 전송합니다.
1. 파일 다운로드 함수. [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 사용자가 파일을 다운로드할 수 있는 링크를 생성하는 역할을 합니다. 이 함수는 파일 이름, MIME 타입, 파일 내용을 인수로 받습니다. 이 함수는 다운로드 링크를 생성하고, 파일 내용을 링크에 연결하며, 파일 이름을 설정하고 문서에 추가합니다. 이를 통해 사용자는 생성된 PDF 파일을 다운로드할 수 있습니다.

1. 웹 워커에서의 메시지 처리. 다음으로, 'json.errorCode'가 0일 경우, json.fileNameResult에는 이전에 지정한 이름이 포함됩니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있을 경우, 그러한 오류에 대한 정보는 'json.errorText' 속성에 포함됩니다.

1. 결과 표시. 메인 페이지에는 'output'이라는 ID를 가진 요소가 포함되어 있습니다. 웹 워커가 결과와 함께 메시지를 보내면 'output' 요소를 업데이트합니다. 작업이 성공하면 두 개의 분할된 PDF 파일에 대한 다운로드 링크를 표시합니다. 오류가 발생하면 오류 메시지를 표시합니다.

이 코드는 리소스를 많이 사용하는 PDF 파일 분할 작업을 웹 워커로 오프로드하여 메인 UI 스레드가 차단되지 않도록 하는 방법을 보여줍니다. 또한 분할된 PDF 파일을 다운로드하는 사용자 친화적인 방법을 제공합니다.

```js

    /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ?
          `결과:\n${DownloadFile(evt.data.json.fileNameResult1, "application/pdf", evt.data.params[0])}
                  \n${DownloadFile(evt.data.json.fileNameResult2, "application/pdf", evt.data.params[1])}` :
          `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileSplit = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*분할할 페이지 번호 설정*/
        const pageToSplit = 1;
        /*두 개의 PDF 파일로 분할하고 "ResultSplit1.pdf", "ResultSplit2.pdf"로 저장 - 웹 워커에 요청*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSplit2Files',
            "params": [event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일을 다운로드할 링크 생성*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일 " + filename + " 다운로드하려면 여기를 클릭하세요";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```

다음 JavaScript 코드 스니펫은 PDF 페이지를 개별 PDF 파일로 분할하는 간단한 예제를 보여줍니다:

1. 분할할 PDF 파일을 선택합니다.
1. 핸들러에서 'FileReader' 객체를 생성합니다.
1. 분할할 페이지 번호를 설정합니다.
1. 마지막 핸들러에서 [AsposePdfSplit2Files](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsplit2files/)를 호출합니다.
1. 결과를 분석합니다. 결과 파일의 이름은 이 예제에서 "ResultSplit2.pdf"로 설정됩니다.
1. 다음으로, 'json.errorCode'가 0이면, json.fileNameResult에 이전에 지정한 이름이 포함됩니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있는 경우, 그러한 오류에 대한 정보는 'json.errorText' 속성에 포함됩니다.
1. [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 도우미 함수를 사용할 수 있습니다.

```js
  var ffileSplit = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*분할할 페이지 번호 설정*/
      const pageToSplit = 1;
      /*두 개의 PDF 파일로 분할하고 "ResultSplit1.pdf", "ResultSplit2.pdf"로 저장*/
      const json = AsposePdfSplit2Files(event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = e.target.files[0].name + " split: " + json.fileNameResult1 + ", " + json.fileNameResult2;
      else document.getElementById('output').textContent = json.errorText;
      /*첫 번째 결과 파일을 다운로드하는 링크 생성*/
      DownloadFile(json.fileNameResult1, "application/pdf");
      /*두 번째 결과 파일을 다운로드하는 링크 생성*/
      DownloadFile(json.fileNameResult2, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```