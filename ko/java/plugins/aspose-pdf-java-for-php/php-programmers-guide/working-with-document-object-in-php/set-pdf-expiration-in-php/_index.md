---
title: PHP에서 PDF 만료 설정
linktitle: PHP에서 PDF 만료 설정
type: docs
weight: 80
url: /java/set-pdf-expiration-in-php/
description: Aspose.PDF로 액세스를 제어하여 PHP에서 PDF 파일의 만료 날짜를 설정하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF 만료 설정



PHP용 **Aspose.PDF Java**를 사용하여 PDF 문서의 만료를 설정하려면 **SetExpiration** 클래스를 호출하기만 하면 됩니다.



PHP 코드


```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('The file is expired. You need a new one.');");
$doc->setOpenAction($javascript);

# save update document with new information
$doc->save($dataDir . "set_expiration.pdf");

print "Update document information, please check output file." . PHP_EOL;

```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서**PDF 만료 설정(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)
