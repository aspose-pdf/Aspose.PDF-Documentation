---
title: JavaScript를 통한 C++에서 PDF 파일 메타데이터 작업
linktitle: PDF 파일 메타데이터
type: docs
weight: 130
url: /ko/javascript-cpp/pdf-file-metadata/
description: 이 섹션은 PDF 파일 정보를 얻는 방법, PDF 파일에서 메타데이터를 얻는 방법, PDF 파일 정보를 설정하는 방법을 설명합니다.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일 정보 가져오기

1. 'FileReader'를 생성합니다.
1. [AsposePdfGetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetinfo/) 함수가 실행됩니다.
1. 얻을 수 있는 PDF 메타데이터:
- title - 제목
- creator - 작성자
- author - 저자
- subject - 주제
- keywords - 키워드
- creation - 생성 날짜
- mod - 수정 날짜
1. 다음으로, 'json.errorCode'가 0이면 PDF 파일 정보 목록을 가져올 수 있습니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있는 경우, 해당 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.

```js

  var ffilePdfGetInfo = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDF 파일에서 정보(메타데이터) 가져오기.*/
      const json = AsposePdfGetInfo(event.target.result, e.target.files[0].name);
      /* JSON
      title - 제목
      creator - 작성자
      author - 저자
      subject - 주제
      keywords - 키워드
      format - PDF 형식
      version - PDF 버전
      ispdfa - PDF는 PDF/A
      ispdfua - PDF는 PDF/UA
      islinearized - PDF는 선형화됨
      isencrypted - PDF는 암호화됨
      permission - PDF 권한
      size - PDF 페이지 크기
      pagecount - 페이지 수
      생성 날짜: json.creation
      수정 날짜:   json.mod
      annotationcount - 주석 수
      bookmarkcount - 북마크 수
      attachmentcount - 첨부 파일 수
      metadatacount - 메타데이터 수
      javascriptcount - JavaScript 수
      imagecount - 이미지 수
      */
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


### 웹 워커 사용

```js

    /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 오류: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ?
          `정보:\n${JSON.stringify(evt.data.json, null, 4)}` :
          `오류: ${evt.data.json.errorText}`; 

    /*이벤트 핸들러*/
    const ffilePdfGetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일에서 정보(메타데이터) 가져오기 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetInfo', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## 모든 폰트 가져오기

PDF 파일에서 폰트를 가져오는 것은 다른 문서나 애플리케이션에서 폰트를 재사용하는 유용한 방법이 될 수 있습니다.
 
PDF 문서에서 모든 글꼴을 가져오려는 경우, [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/)를 사용할 수 있습니다. 
JavaScript를 통해 C++로 기존 PDF 문서에서 모든 글꼴을 가져오는 방법에 대한 다음 코드 스니펫을 확인하세요.

1. 'FileReader'를 생성합니다.
1. [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/) 함수가 실행됩니다.
1. 다음으로, 'json.errorCode'가 0이면 PDF 파일에서 글꼴 목록을 가져올 수 있습니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있는 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.

```js

  var ffilePdfGetAllFonts = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /* PDF 파일에서 글꼴 목록을 가져옵니다. */
      const json = AsposePdfGetAllFonts(event.target.result, e.target.files[0].name);
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
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
        (evt.data.json.errorCode == 0) ?
          `폰트:\n${JSON.stringify(evt.data.json.fonts, null, 4)}` :
          `오류: ${evt.data.json.errorText}`; 

    /* 이벤트 핸들러 */
    const ffilePdfGetAllFonts = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /* PDF 파일의 폰트 목록 가져오기 - 웹 워커에 요청 */
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetAllFonts', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```
## PDF 파일 정보 설정

Aspose.PDF for JavaScript via C++를 사용하면 PDF의 파일별 정보를 설정할 수 있으며, 작성자, 생성 날짜, 주제 및 제목과 같은 정보를 포함합니다.
 이 정보를 설정하려면:

1. 'FileReader'를 생성합니다.
1. 값을 설정할 필요가 없으면 undefined 또는 "" (빈 문자열)을 사용합니다.
1. [AsposePdfSetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsetinfo/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정되며, 이 예제에서는 "ResultSetInfo.pdf"입니다.
1. 다음으로, 'json.errorCode'가 0이면 다운로드 파일에 이전에 지정한 이름이 부여됩니다. 'json.errorCode' 매개 변수가 0이 아니고, 따라서 파일에 오류가 있을 경우 해당 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수가 링크를 생성하고 사용자의 운영 체제로 결과 파일을 다운로드할 수 있게 합니다.

```js

    var ffilePdfSetInfo = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 정보 설정: 제목, 생성자, 저자, 주제, 키워드, 생성일 (날짜), 수정일 (날짜 수정)*/
        /*값을 설정할 필요가 없으면 undefined 또는 "" (빈 문자열)을 사용합니다.*/
        /*PDF 파일에 정보 (메타데이터)를 설정하고 "ResultSetInfo.pdf"로 저장합니다.*/
        const json = AsposePdfSetInfo(event.target.result, e.target.files[0].name, "PDF 문서 정보 설정", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "16/02/2023 11:55 PM", "ResultSetInfo.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드할 링크 생성*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

### 웹 워커 사용하기

```js

    /*웹 워커 생성하기*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커 에러: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '로드 완료!' :
        (evt.data.json.errorCode == 0) ?
          `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffilePdfSetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 정보: 제목, 생성자, 저자, 주제, 키워드, 생성 (날짜), 수정 (날짜 수정)*/
        const title = 'PDF 문서 정보 설정';
        const creator = ''; /*값을 설정할 필요가 없으면, undefined 또는 ""/'' (빈 문자열) 사용*/
        const author = 'Aspose';
        const subject = undefined;
        const keywords = 'Aspose.Pdf, DOM, API';
        const creation = undefined; /*생성 날짜*/
        const mod = '16/02/2023 11:55 PM'; /*수정 날짜*/
        /*PDF 파일에 정보 (메타데이터) 설정하고 "ResultSetInfo.pdf" 저장 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSetInfo',
            "params": [event.target.result, e.target.files[0].name, title, creator, author, subject, keywords, creation, mod, "ResultSetInfo.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*결과 파일 다운로드 링크 만들기*/
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


## PDF 파일 정보 제거

Aspose.PDF for JavaScript via C++를 사용하여 PDF 파일 메타데이터를 제거할 수 있습니다:

1. 'FileReader'를 생성합니다.
1. [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/javascript-cpp/metadata/asposepdfremovemetadata/) 함수가 실행됩니다.
1. 결과 파일의 이름이 설정됩니다. 이 예제에서는 "ResultPdfRemoveMetadata.pdf"입니다.
1. 다음으로, 'json.errorCode'가 0이면, 지정한 이름으로 DownloadFile이 설정됩니다. 'json.errorCode' 매개변수가 0이 아니고, 따라서 파일에 오류가 있을 경우, 그러한 오류에 대한 정보는 'json.errorText' 파일에 포함됩니다.
1. 결과적으로, [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 함수는 링크를 생성하고 사용자의 운영 체제에 결과 파일을 다운로드할 수 있도록 합니다.

```js

    var ffilePdfRemoveMetadata = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF 파일의 메타데이터를 제거하고 "ResultPdfRemoveMetadata.pdf"로 저장*/
        const json = AsposePdfRemoveMetadata(event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*결과 파일을 다운로드할 링크 생성*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


### 웹 워커 사용하기

```js

    /*웹 워커 생성*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`웹 워커에서 오류 발생: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '불러오기 완료!' :
        (evt.data.json.errorCode == 0) ? `결과:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `오류: ${evt.data.json.errorText}`;

    /*이벤트 핸들러*/
    const ffilePdfRemoveMetadata = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 파일의 메타데이터를 제거하고 "ResultPdfRemoveMetadata.pdf"로 저장 - 웹 워커 요청*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRemoveMetadata', "params": [event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [코드 스니펫]

    /*결과 파일을 다운로드할 링크 만들기*/
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