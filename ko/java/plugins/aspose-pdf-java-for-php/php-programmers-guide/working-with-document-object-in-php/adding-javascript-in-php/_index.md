---
title: PHP에 JavaScript 추가하기
linktitle: PHP에 JavaScript 추가하기
type: docs
weight: 10
url: /java/adding-javascript-in-php/
description: PHP 및 Aspose.PDF를 사용하여 PDF 파일에 JavaScript를 추가하여 문서 상호 작용을 향상시키는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - JavaScript 추가



**Aspose.PDF Java for PHP**를 사용하여 PDF 문서에 JavaScript를 추가하려면 **AddJavaScript** 클래스를 호출하기만 하면 됩니다.

PHP 코드


```php
# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Adding JavaScript at Document Level
# Instantiate JavascriptAction with desried JavaScript statement
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Assign JavascriptAction object to desired action of Document
$doc->setOpenAction($javaScript);

# Adding JavaScript at Page Level
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

# Save PDF Document
$doc->save($dataDir . "JavaScript-Added.pdf");

print "Added JavaScript Successfully, please check the output file.";
```


**실행 코드 다운로드**



아래 언급된 소셜 코딩 사이트 중 하나에서 В **JavaScript 추가(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)
