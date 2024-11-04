---
title: JavaScript를 통해 PDF 파일에서 이미지 삭제
linktitle: 이미지 삭제
type: docs
weight: 20
url: /javascript-cpp/delete-images-from-pdf-file/
description: 이 섹션에서는 Aspose.PDF for JavaScript를 사용하여 PDF 파일에서 이미지를 삭제하는 방법을 설명합니다.
lastmod: "2022-02-17"
---

JavaScript를 통해 C++로 Aspose.PDF를 사용하여 PDF 파일에서 이미지를 삭제할 수 있습니다. 결과를 브라우저에서 직접 얻을 수 있습니다.

1. 'FileReader'를 생성합니다.
1. [AsposePdfDeleteImages](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteimages/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예에서는 "ResultPdfDeleteImages.pdf"입니다.
1. 다음으로, 'json.errorCode'가 0이면, DownloadFile에 이전에 지정한 이름이 부여됩니다. 'json.errorCode' 매개변수가 0이 아니고, 그에 따라 파일에 오류가 있는 경우에는 이러한 오류에 대한 정보가 'json.errorText' 파일에 포함됩니다.

1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있게 합니다.

```js

    var ffilePdfDeleteImages = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*PDF 파일에서 이미지를 삭제하고 "ResultPdfDeleteImages.pdf"로 저장합니다.*/
        const json = AsposePdfDeleteImages(event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드할 수 있는 링크를 만듭니다.*/
        DownloadFile(json.fileNameResult, "application/pdf");
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## 웹 워커 사용하기

```js

    /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
        (evt.data == 'ready') ? '로드됨!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffilePdfDeleteImages = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*PDF 파일에서 이미지를 삭제하고 "ResultPdfDeleteImages.pdf"로 저장합니다 - 웹 워커에 요청합니다.*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteImages', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf"] }, [event.target.result]);
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일을 다운로드할 수 있는 링크를 만듭니다.*/
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