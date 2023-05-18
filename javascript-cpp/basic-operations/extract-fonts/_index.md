---
title: Extract fonts from PDF with JavaScript via C++ 
linktitle: Extract fonts from PDF
type: docs
weight: 10
url: /javascript-cpp/extract-fonts-from-pdf/
description: This topic describes how to rotate the page orientation in an existing PDF file programmatically via JavaScript via C++ 
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Extracting fonts from a PDF file can be a useful way to reuse fonts in other documents or applications. 

In case you want to get all fonts from a PDF document, you can use [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/) class. 
Please check following code snippet in order to get all fonts from an existing PDF document using JavaScript via C++.

1. Create a 'FileReader'.
1. The [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/) function is executed.
1. Next, if the 'json.errorCode' is 0, then you can get list of fonts from PDF file. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.

```js

  var ffilePdfGetAllFonts = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*get list of fonts from PDF file.*/
      const json = AsposePdfGetAllFonts(event.target.result, e.target.files[0].name);
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```