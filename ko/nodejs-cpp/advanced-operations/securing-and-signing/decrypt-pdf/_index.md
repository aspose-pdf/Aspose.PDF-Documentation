---
title: Node.js에서 PDF 복호화
linktitle: PDF 파일 복호화
type: docs
weight: 40
url: /ko/nodejs-cpp/decrypt-pdf/
description: C++를 통한 Aspose.PDF로 PDF 파일 복호화.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 소유자 비밀번호를 사용하여 PDF 파일 복호화

최근 들어, 점점 더 많은 사용자들이 인터넷 사기의 피해자가 되지 않고 문서를 보호하기 위해 암호화된 문서를 교환하고 있습니다.
이와 관련하여, 암호화된 PDF 파일에 접근하는 것이 필요해지며, 이러한 접근은 권한이 있는 사용자만이 얻을 수 있습니다. 또한, 사람들은 PDF 파일을 복호화할 수 있는 다양한 솔루션을 찾고 있습니다. 

PDF 파일을 복호화하려는 경우, [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 함수를 사용할 수 있습니다.
PDF 파일을 복호화하려면 다음 코드 스니펫을 시도해 보세요:

**CommonJS:**

1. `require`를 호출하고 `asposepdfnodejs` 모듈을 `AsposePdf` 변수로 가져옵니다.
1. 복호화될 PDF 파일의 이름을 지정합니다.

1. `AsposePdf`를 Promise로 호출하고 파일을 해독하는 작업을 수행합니다. 성공하면 객체를 받습니다.
1. [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 함수를 호출합니다.
1. 비밀번호가 "owner"인 PDF 파일을 해독합니다.
1. 따라서 'json.errorCode'가 0이면 작업의 결과는 "ResultDecrypt.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 파일에 오류가 나타나는 경우, 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*비밀번호가 "owner"인 PDF 파일을 해독하고 "ResultDecrypt.pdf"로 저장합니다.*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` 모듈을 가져옵니다.
1. 암호가 해제될 PDF 파일의 이름을 지정합니다.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 함수를 호출합니다.
1. PDF 파일의 암호를 "owner"로 해제합니다.
1. 따라서 'json.errorCode'가 0이면 작업의 결과가 "ResultDecrypt.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고, 그에 따라 파일에 오류가 나타나면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*PDF 파일의 암호를 "owner"로 해제하고 "ResultDecrypt.pdf"로 저장합니다.*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```