---
title: JavaScript를 통한 C++로 PDF에 이미지 스탬프 추가
linktitle: PDF 파일의 이미지 스탬프
type: docs
weight: 60
url: /ko/javascript-cpp/stamping/
description: JavaScript 툴킷을 사용하여 AsposePdfAddStamp 함수를 통해 PDF 문서에 이미지 스탬프를 추가합니다.
lastmod: "2023-04-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에 이미지 스탬프 추가

PDF 문서에 스탬프를 찍는 것은 종이 문서에 스탬프를 찍는 것과 유사합니다. PDF 파일의 스탬프는 다른 사람들이 PDF 파일을 사용하고 PDF 파일의 내용의 보안을 확인하는 등의 추가 정보를 제공합니다. JavaScript를 사용하여 PDF 파일에 이미지 스탬프를 추가하려면 [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) 함수를 사용할 수 있습니다.

이미지 스탬프를 추가하려면:

1. 기본 이미지 파일 이름을 설정합니다.
1. 'FileReader'를 생성합니다.
1. 이미지 파일 이름을 설정합니다.
1. BLOB에서 스탬프 파일을 준비합니다.

다음 코드는 PDF 파일에 이미지 스탬프를 추가하는 방법을 보여줍니다.

```js

  /*기본 스탬프 파일 이름 설정*/
  var fileStamp = "/Aspose.jpg";

  var ffileStamp = function (e) {
    const file_reader = new FileReader();
    /*스탬프 파일 이름 설정*/
    fileStamp = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*BLOB에서 스탬프 파일 준비(저장)*/
      AsposePdfPrepare(event.target.result, fileStamp);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


1. 'FileReader'를 생성합니다.
1. [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) 함수가 실행됩니다.
1. 이미지 파일을 PDF 파일 끝에 추가하고 "ResultImage.pdf"로 저장합니다.
1. 다음으로, 'json.errorCode'가 0이면, DownloadFile에 이전에 지정한 이름이 부여됩니다. 'json.errorCode' 매개변수가 0이 아닌 경우에는 파일에 오류가 발생하며, 이러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제로 결과 파일을 다운로드할 수 있도록 합니다.

```js
  var ffileAddStamp = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*stamp 파일을 PDF 파일에 삽입하고 "ResultImage.pdf"로 저장합니다.*/
      const json = AsposePdfAddStamp(event.target.result, e.target.files[0].name, fileStamp, 0, 5, 5, 40, 40, Module.Rotation.on270, 0.5, "ResultStamp.pdf");
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
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ?
          `결과:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            '이미지 준비 완료!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `오류: ${evt.data.json.errorText}`;

    /*기본 스탬프 파일 이름 설정: 'Aspose.jpg' 이미 로드됨, 'settings.json'에서 설정 참조*/
    var fileStamp = "Aspose.jpg";

    /*이벤트 핸들러*/
    const ffileAddStamp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const setBackground = 0;
        const setXIndent_ = 5;
        const setYIndent_ = 5;
        const setHeight_ = 40;
        const setWidth_ = 40;
        const rotation_ = 'Module.Rotation.on270';
        const setOpacity = 0.5;
        /*PDF 파일에 스탬프 추가하고 "ResultStamp.pdf"로 저장 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddStamp',
            "params": [event.target.result, e.target.files[0].name, fileStamp, setBackground, setXIndent_, setYIndent_,
                      setHeight_, setWidth_, rotation_, setOpacity, "ResultStamp.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileStamp = e => {
      const file_reader = new FileReader();
      /*스탬프 파일 이름 설정*/
      fileStamp = e.target.files[0].name;
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
        link.innerHTML = "여기를 클릭하여 파일 " + filename + "을(를) 다운로드하세요";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```