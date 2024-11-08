---
title: PDF에서 이미지 추출 JavaScript
linktitle: PDF에서 이미지 추출
type: docs
weight: 20
url: /ko/javascript-cpp/extract-images-from-the-pdf-file/
description: Aspose.PDF for JavaScript 툴킷을 사용하여 PDF에서 이미지의 일부를 추출하는 방법.
lastmod: "2023-09-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF의 웹 툴킷을 사용하면 PDF 파일에서 이미지를 쉽게 추출할 수 있습니다.

PDF 문서에서 이미지를 추출하려는 경우, [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/) 함수를 사용할 수 있습니다.
JavaScript를 통해 C++로 PDF 파일에서 이미지를 추출하려면 다음 코드 스니펫을 확인하십시오.

1. 'FileReader'를 만듭니다.
1. [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예에서는 "ResultPdfExtractImage{0:D2}.jpg"입니다.

1. 다음으로, 'json.errorCode'가 0이면 결과 파일에 대한 링크를 얻을 수 있습니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있는 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있게 합니다.

```js

    var ffileExtractImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
    /*해당 템플릿 "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... 형식 페이지 번호), 해상도 150 DPI로 PDF 파일에서 이미지를 추출하고 저장합니다.*/
    const json = AsposePdfExtractImage(event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150);
    if (json.errorCode == 0) {
        document.getElementById('output').textContent = "파일(이미지) 수: " + json.filesCount.toString();
        /*결과 파일에 대한 링크 생성*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
    }
    else document.getElementById('output').textContent = json.errorText;
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## 웹 워커 사용하기

```js

  /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드됨!' :
        (evt.data.json.errorCode == 0) ? 
          `파일(이미지) 수: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffileExtractImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*해상도 150 DPI로 PDF 파일에서 이미지를 추출하고 "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... 형식 페이지 번호) 템플릿으로 저장*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfExtractImage', "params": [event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150] }, [event.target.result]);
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