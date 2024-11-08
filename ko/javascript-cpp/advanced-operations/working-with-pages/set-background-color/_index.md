---
title: JavaScript를 통해 C++로 PDF의 배경색 설정
linktitle: 배경색 설정
type: docs
weight: 80
url: /ko/javascript-cpp/set-background-color/
description: JavaScript를 통해 C++로 PDF 파일의 배경색을 설정합니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

다음 코드 스니펫은 JavaScript를 사용하여 [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsetbackgroundcolor/) 함수를 통해 PDF 페이지의 배경색을 설정하는 방법을 보여줍니다.

다음 예제에서는 처리할 PDF 파일을 선택합니다.

1. 'FileReader'를 생성합니다.
1. [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsetbackgroundcolor/) 함수가 실행됩니다 (16진수 형식 “#RRGGBB”, 여기서 RR-빨강, GG-초록 및 BB-파랑 16진수 정수).
1. PDF 파일의 배경색을 설정하고 "ResultPdfSetBackgroundColor.pdf"로 저장합니다.

1. 다음으로, 'json.errorCode'가 0이면, DownloadFile은 이전에 지정한 이름을 갖습니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면, 해당 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있게 합니다.

```js
var ffilePdfSetBackgroundColor = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일의 배경색을 설정하고 "ResultPdfSetBackgroundColor.pdf"로 저장합니다.*/
      const json = AsposePdfSetBackgroundColor(event.target.result, e.target.files[0].name, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
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

    /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커에서 오류 발생: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '불러왔습니다!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffilePdfSetBackgroundColor = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const backgroundColor= "#426bf4";
        /*PDF 파일의 배경색을 설정하고 "ResultPdfSetBackgroundColor.pdf"로 저장 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfSetBackgroundColor', "params": [event.target.result, e.target.files[0].name, backgroundColor, "ResultPdfSetBackgroundColor.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일을 다운로드할 링크 생성*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "파일 " + filename + " 다운로드를 위해 여기를 클릭하세요";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```