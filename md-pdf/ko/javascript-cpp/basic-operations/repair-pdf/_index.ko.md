---
title: JavaScript를 통한 PDF 복구(C++ 사용)
linktitle: PDF 복구
type: docs
weight: 10
url: /javascript-cpp/repair-pdf/
description: 이 주제에서는 JavaScript를 통해 PDF를 C++로 복구하는 방법을 설명합니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for JavaScript는 고품질의 PDF 복구를 제공합니다. 프로그램이나 브라우저에 관계없이 PDF 파일이 열리지 않을 수 있습니다. 경우에 따라 문서를 복원할 수 있으며, 다음 코드를 시도해 보고 직접 확인하십시오.

1. 'FileReader'를 생성합니다.
1. [AsposePdfRepair](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfrepair/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정되며, 이 예제에서는 "ResultPdfRepair.pdf"입니다.
1. 다음으로, 'json.errorCode'가 0이면 결과 파일에 대한 링크를 얻을 수 있습니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있는 경우 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.

1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제로 결과 파일을 다운로드할 수 있게 해줍니다.

```js

    var ffilePdfRepair = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일을 복구하고 "ResultPdfRepair.pdf"로 저장합니다.*/
        const json = AsposePdfRepair(event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드할 링크를 만듭니다.*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## 웹 워커 사용하기

```js

    /*웹 워커 생성하기*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '불러옴!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffilePdfRepair = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일을 복구하고 "ResultPdfRepair.pdf"로 저장합니다 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRepair', "params": [event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [코드 스니펫]

    /*결과 파일을 다운로드할 링크를 만듭니다.*/
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