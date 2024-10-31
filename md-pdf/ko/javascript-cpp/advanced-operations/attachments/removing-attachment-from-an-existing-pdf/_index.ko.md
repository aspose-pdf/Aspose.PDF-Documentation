---
title: JavaScript로 PDF에서 첨부 파일 제거
linktitle: 기존 PDF에서 첨부 파일 제거
type: docs
weight: 10
url: /javascript-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF는 PDF 문서에서 첨부 파일을 제거할 수 있습니다. Aspose.PDF를 사용하여 PDF 파일에서 첨부 파일을 제거하기 위해 JavaScript 웹 툴킷을 사용하세요.
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for JavaScript via C++를 사용하여 PDF 파일에서 첨부 파일을 삭제할 수 있습니다. 결과를 브라우저에서 직접 얻을 수 있습니다.

1. 'FileReader'를 생성합니다.
1. [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteattachments/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예제에서는 "ResultPdfDeleteAttachments.pdf"입니다.

1. 다음으로, 'json.errorCode'가 0이면, DownloadFile은 이전에 지정한 이름이 부여됩니다. 'json.errorCode' 매개변수가 0과 같지 않으면 파일에 오류가 발생하며, 이러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있게 합니다.

```js

    var ffilePdfDeleteAttachments = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*PDF 파일에서 첨부 파일을 삭제하고 "ResultPdfDeleteAttachments.pdf"로 저장*/
        const json = AsposePdfDeleteAttachments(event.target.result, e.target.files[0].name, "ResultPdfDeleteAttachments.pdf");
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
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /* 이벤트 핸들러 */
    const ffilePdfDeleteAttachments = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /* PDF 파일에서 첨부 파일 삭제하고 "ResultPdfDeleteAttachments.pdf"로 저장 - 웹 워커에게 요청 */
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteAttachments', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteAttachments.pdf"] }, [event.target.result]);
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /* 결과 파일 다운로드 링크 생성 */
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