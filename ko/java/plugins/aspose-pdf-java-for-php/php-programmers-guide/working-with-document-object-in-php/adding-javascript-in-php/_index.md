---
title: PHP에 JavaScript 추가
type: docs
weight: 10
url: /ko/java/adding-javascript-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - JavaScript 추가

**Aspose.PDF Java for PHP**를 사용하여 Pdf 문서에 JavaScript를 추가하려면, **AddJavaScript** 클래스를 호출하세요.

PHP 코드

```php
# PDF 문서를 엽니다.
$doc = new Document($dataDir . "input1.pdf");

# 문서 레벨에서 JavaScript 추가
# 원하는 JavaScript 문장으로 JavascriptAction 인스턴스화
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Document의 원하는 동작에 JavascriptAction 객체 할당
$doc->setOpenAction($javaScript);

# 페이지 레벨에서 JavaScript 추가
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

# PDF 문서 저장
$doc->save($dataDir . "JavaScript-Added.pdf");

print "JavaScript가 성공적으로 추가되었습니다. 출력 파일을 확인하세요.";
```


**코드 실행 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **JavaScript 추가 (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)