---
title: Add Image to PDF using JavaScript via C++ 
linktitle: Add Image
type: docs
weight: 10
url: /javascript-cpp/add-image-to-pdf/
description: 이 섹션에서는 C++를 통해 Aspose.PDF for JavaScript를 사용하여 기존 PDF 파일에 이미지를 추가하는 방법을 설명합니다.
lastmod: "2023-12-15"
---

## 기존 PDF 파일에 이미지 추가

PDF에 이미지를 첨부해야 하나요? PDF의 가독성을 높이고 싶으신가요? PDF에 이미지를 추가하면 프레젠테이션이나 이력서가 더 돋보입니다.

일반적으로 PDF 파일에 이미지를 추가하려면 복잡한 특수 도구가 필요하다고 믿어집니다. 그러나 Aspose.PDF for JavaScript를 사용하면 브라우저에서 JavaScript를 사용하여 필요한 이미지를 PDF에 빠르고 쉽게 추가할 수 있습니다.

기존 PDF 파일에 이미지를 추가하려면 다음 단계를 따르세요:

1. 기본 이미지 파일 이름을 설정합니다.
1. 'FileReader'를 생성합니다.
1. 이미지 파일 이름을 설정합니다.
1. BLOB에서 이미지 파일을 준비합니다.
1. [AsposePdfAddImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddimage/) 함수가 실행됩니다.

1. 이미지 파일을 PDF 파일 끝에 추가하고 "ResultImage.pdf"로 저장합니다.
1. 다음으로, 'json.errorCode'가 0이면, DownloadFile은 이전에 지정한 이름을 갖게 됩니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 발생하면, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제로 결과 파일을 다운로드할 수 있도록 합니다.

다음 코드 스니펫은 PDF 문서에 이미지를 추가하는 방법을 보여줍니다.

```js

  /*기본 이미지 파일 이름 설정*/
  var fileImage = "/Aspose.jpg";

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*이미지 파일 이름 설정*/
    fileImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*BLOB에서 이미지 파일 준비(저장)*/
      AsposePdfPrepare(event.target.result, fileImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

다음 예제에서는 처리할 이미지를 선택합니다:

```js

  var ffileAddImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*이미지 파일을 PDF 파일의 끝에 추가하고 "ResultImage.pdf"로 저장합니다*/
      const json = AsposePdfAddImage(event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*결과 파일을 다운로드할 링크를 만듭니다*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

## 웹 워커 사용

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

    /*기본 이미지 파일명 설정: 'Aspose.jpg' 이미 로드됨, 'settings.json'에서 설정 확인*/
    var fileImage = "Aspose.jpg";

    /*이벤트 핸들러*/
    const ffileAddImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*이미지를 PDF 파일의 끝에 추가하고 "ResultImage.pdf"로 저장합니다 - 웹 워커에 요청*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddImage',
            "params": [event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*이미지 파일명 설정*/
      fileImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*처리를 위해 메모리 FS에 BLOB 저장*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일을 다운로드할 링크를 만듭니다*/
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