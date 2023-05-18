---
title: Working with PDF File Metadata using JavaScript via C++
linktitle: PDF File Metadata
type: docs
weight: 30
url: /javascript-cpp/pdf-file-metadata/
description: This section explains how to get PDF file information, how to get metadata from a PDF file, set PDF File Information.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get PDF File Information

1. Create a 'FileReader'.
1. The [AsposePdfGetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetinfo/) function is executed.
1. PDF metadata that can be obtained:
- title - title
- creator - creator
- author - author
- subject - subject
- keywords - keywords
- creation - creation date
- mod - modify date
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.

```js

  var ffilePdfGetInfo = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Get info (metadata) from PDF file.*/
      const json = AsposePdfGetInfo(event.target.result, e.target.files[0].name);
      /* JSON
       Title:    json.title
       Creator:  json.creator
       Author:   json.author 
       Subject:  json.subject
       Keywords: json.keywords
       Creation Date: json.creation
       Modify Date:   json.mod
      */
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

## Set PDF File Information

Aspose.PDF for JavaScript via C++ allows you to set file-specific information for a PDF, information like author, creation date, subject, and title. To set this information:

1. Create a 'FileReader'.
1. If not need to set value, use undefined or "" (empty string).
1. The [AsposePdfSetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsetinfo/) function is executed.
1. The name of the resulting file is set, in this example "ResultSetInfo.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffilePdfSetInfo = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Set info (metadata) in PDF file.*/
      /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
      /*if not need to set value, use undefined or "" (empty string)*/
      /*set info a PDF-file and save the "ResultSetInfo.pdf"*/
      const json = AsposePdfSetInfo(event.target.result, e.target.files[0].name, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "16/02/2023 11:55 PM", "ResultSetInfo.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*make a link to download the result file*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

