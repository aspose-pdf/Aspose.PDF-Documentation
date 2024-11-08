---
title: JavaScript를 통해 C++로 PDF에 배경 추가
linktitle: 배경 추가
type: docs
weight: 10
url: /ko/javascript-cpp/add-backgrounds/
description: JavaScript를 통해 C++로 PDF 파일에 배경 이미지를 추가합니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

다음 코드 스니펫은 JavaScript를 사용하여 [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) 함수를 통해 PDF 페이지에 배경 이미지를 추가하는 방법을 보여줍니다.

다음 코드 스니펫에서는 내부 파일 시스템에서 추가 작업을 위해 이미지를 업로드합니다:

1. 'FileReader' 생성.
1. 이미지 파일 이름 설정.
1. BLOB에서 이미지 파일 준비.

```js

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*이미지 파일 이름 설정*/
    fileBackgroundImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*BLOB에서 이미지 파일 준비(저장)*/
      AsposePdfPrepare(event.target.result, fileBackgroundImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


다음 예제에서는 처리할 PDF 파일을 선택합니다.
1. 'FileReader'를 생성합니다.
1. [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) 함수가 실행됩니다.
1. 이미지 파일을 PDF에 추가하고 "ResultBackgroundImage.pdf"로 저장합니다.
1. 다음으로, 'json.errorCode'가 0이면, DownloadFile은 이전에 지정한 이름을 갖게 됩니다. 'json.errorCode' 매개 변수가 0이 아니고, 따라서 파일에 오류가 있으면, 해당 오류에 대한 정보가 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자 운영 체제에 결과 파일을 다운로드할 수 있도록 합니다.

```js

  var ffileAddBackgroundImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*배경 이미지 파일을 PDF에 추가하고 "ResultBackgroundImage.pdf"로 저장합니다.*/
      const json = AsposePdfAddBackgroundImage(event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf");
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
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ? 
          `결과:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            '이미지 준비 완료!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `오류: ${evt.data.json.errorText}`;

    /*기본 이미지 파일명 설정: 'Aspose.jpg' 이미 로드됨, 'settings.json'의 설정 참조*/
    var fileBackgroundImage = "Aspose.jpg";

    /*이벤트 핸들러*/
    const ffileAddBackgroundImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일에 배경 이미지 추가하고 "ResultBackgroundImage.pdf"로 저장 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddBackgroundImage',
            "params": [event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*이미지 파일명 설정*/
      fileBackgroundImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*처리를 위해 메모리 FS에 BLOB 저장*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
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