---
title: PHP에서 PDF 만료 설정
type: docs
weight: 80
url: /ko/java/set-pdf-expiration-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF 만료 설정

**Aspose.PDF Java for PHP**를 사용하여 Pdf 문서의 만료를 설정하려면, **SetExpiration** 클래스를 호출하십시오.

PHP 코드

```php

# PDF 문서를 엽니다.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('파일이 만료되었습니다. 새로운 파일이 필요합니다.');");
$doc->setOpenAction($javascript);

# 새로운 정보로 문서 업데이트 저장
$doc->save($dataDir . "set_expiration.pdf");

print "문서 정보가 업데이트되었습니다. 출력 파일을 확인하십시오." . PHP_EOL;

```

**실행 코드 다운로드**

아래에 언급된 소셜 코딩 사이트 중 하나에서 **Set PDF Expiration (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)