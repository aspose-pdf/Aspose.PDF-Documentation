---
title: JavaScript로 PDF에 북마크 추가
linktitle: PDF의 북마크
type: docs
weight: 10
url: /ko/javascript-cpp/bookmark/
description: JavaScript로 PDF 문서에 북마크를 추가하거나 삭제할 수 있습니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에서 특정 북마크 삭제

Aspose.PDF for JavaScript via C++을 사용하여 PDF 파일에서 북마크를 삭제할 수 있습니다. 결과를 직접 브라우저에서 확인할 수 있습니다.

1. 'FileReader'를 생성합니다.
1. [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeletebookmarks/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예에서는 "ResultPdfDeleteBookmarks.pdf"입니다.
1. 다음으로, 'json.errorCode'가 0이면, 지정한 이름으로 DownloadFile이 제공됩니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있을 경우, 그러한 오류에 대한 정보가 'json.errorText' 파일에 포함됩니다.

1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있게 합니다.

```js

    var ffilePdfDeleteBookmarks = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*PDF 파일에서 책갈피를 삭제하고 "ResultPdfDeleteBookmarks.pdf"로 저장합니다.*/
        const json = AsposePdfDeleteBookmarks(event.target.result, e.target.files[0].name, "ResultPdfDeleteBookmarks.pdf");
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
        (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffilePdfDeleteBookmarks = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*PDF 파일에서 책갈피를 삭제하고 "ResultPdfDeleteBookmarks.pdf"로 저장합니다. - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteBookmarks', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteBookmarks.pdf"] }, [event.target.result]);
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일을 다운로드할 링크를 만듭니다.*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일 다운로드하려면 여기를 클릭하세요 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
        }
```