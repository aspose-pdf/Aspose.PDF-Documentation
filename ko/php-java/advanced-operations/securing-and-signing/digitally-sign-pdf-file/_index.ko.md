---
title: PDF를 디지털 서명하는 방법
linktitle: PDF 디지털 서명
type: docs
weight: 10
url: /php-java/digitally-sign-pdf-file/
description: Java를 사용하여 PDF 문서에 디지털 서명합니다. Java 기반 애플리케이션과 PDF 라이브러리를 사용하여 디지털 서명이 있는 PDF를 검증하거나 확인합니다. PKCS1 인증서를 사용하여 PDF 파일을 인증할 수 있습니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 문서에 서명을 할 때, 기본적으로 그 내용이 "있는 그대로" 유지되어야 함을 확인합니다. 따라서, 이후에 이루어진 모든 변경은 서명을 무효화하며, 문서가 변경되었는지 알 수 있습니다. 문서를 먼저 인증하면, 사용자가 인증을 무효화하지 않고 문서에 할 수 있는 변경 사항을 지정할 수 있습니다.

다시 말해, 문서는 여전히 무결성을 유지하는 것으로 간주될 수 있으며 수신자는 여전히 문서를 신뢰할 수 있습니다. 자세한 정보는 PDF 인증 및 서명을 방문하십시오.

## 디지털 서명으로 PDF 서명하기

```php

    // 문서 열기
    $document = new Document($inputFile);    
    $signature = new facades_PdfFileSignature($document);
    $pkcs = new PKCS7($inputPKCS7, 'Pa$$w0rd2020'); // PKCS7/PKCS7Detached 사용
    $rectangle = new Rectangle(300,100,420,160);
    $signature->sign(1, true, $rectangle->toRect(), $pkcs);
    // 출력 PDF 파일 저장
    $signature->save($outputFile);    
    $document->close();
```