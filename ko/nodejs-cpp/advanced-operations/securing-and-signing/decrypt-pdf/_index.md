---
title: Node.js에서 PDF 복호화
linktitle: PDF 파일 복호화
type: docs
weight: 40
url: /ko/nodejs-cpp/decrypt-pdf/
description: Aspose.PDF for Node.js via C++로 PDF 파일 복호화.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 소유자 비밀번호를 사용하여 PDF 파일 복호화

최근에는 인터넷 사기의 피해자가 되지 않고 문서를 보호하기 위해 점점 더 많은 사용자가 암호화된 문서를 교환하고 있습니다.
이와 관련하여 암호화된 PDF 파일에 접근해야 하는데, 이러한 접근은 허가된 사용자만이 얻을 수 있기 때문입니다. 또한 사람들은 PDF 파일을 복호화하기 위한 다양한 솔루션을 찾고 있습니다. 

PDF 파일을 복호화하려는 경우, 사용할 수 있습니다 [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 함수. 
PDF 파일을 복호화하려면 다음 코드 스니펫을 시도하십시오:

**CommonJS:**

1. 호출 `require` 그리고 가져오기 `asposepdfnodejs` 모듈로 `AsposePdf` 변수.
1. 복호화될 PDF 파일의 이름을 지정하십시오.
1. 호출 `AsposePdf` Promise로서 파일 복호화 작업을 수행합니다. 성공하면 객체를 받습니다.
1. 호출하십시오 [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 함수.
1. 비밀번호가 "owner"인 PDF 파일을 복호화합니다.
1. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultDecrypt.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 가져오기 `asposepdfnodejs` 모듈.
1. 복호화될 PDF 파일의 이름을 지정하십시오.
1. AsposePdf 모듈을 초기화합니다. 성공하면 객체를 받습니다.
1. 호출하십시오 [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 함수.
1. 비밀번호가 "owner"인 PDF 파일을 복호화합니다.
1. 따라서 'json.errorCode'가 0이면 작업 결과가 "ResultDecrypt.pdf"에 저장됩니다. json.errorCode 매개변수가 0이 아니고 그에 따라 파일에 오류가 발생하면 오류 정보는 'json.errorText'에 포함됩니다.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```