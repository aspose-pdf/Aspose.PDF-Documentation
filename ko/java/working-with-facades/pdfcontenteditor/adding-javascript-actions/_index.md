---
title: 기존 PDF 파일에 Javascript 액션 추가
type: docs
weight: 10
url: ko/java/adding-javascript-actions/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 기존 PDF 파일에 Javascript 액션을 추가하는 방법을 설명합니다.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 클래스는 com.aspose.pdf.facades 패키지에 속하며 PDF 파일에 Javascript 액션을 추가할 수 있는 유연성을 제공합니다. PDF 뷰어에서 메뉴 항목을 실행하는 일련의 액션을 가진 링크를 생성할 수 있습니다. 이 클래스는 문서 이벤트에 대한 추가 액션을 생성하는 기능도 제공합니다.

우선, 객체는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)에 그려지며, 우리 예제에서는 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle)을 사용합니다.
 그리고 사각형에 [createJavaScriptLink](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createJavaScriptLink-java.lang.String-java.awt.Rectangle-int-java.awt.Color-) 작업을 설정합니다. 그런 다음 문서를 저장할 수 있습니다.

```java
public static void AddingJavascriptActions() {
    PdfContentEditor editor = new PdfContentEditor();
    editor.bindPdf(_dataDir+"sample.pdf");
    // Javascript 링크 생성
    java.awt.Rectangle rect = new java.awt.Rectangle(50, 750, 50, 50);
    String code = "app.alert('Aspose에 오신 것을 환영합니다!');";
    editor.createJavaScriptLink(code, rect, 1, java.awt.Color.GREEN);
    // 출력 파일 저장
    editor.save(_dataDir+"JavaScriptAdded_output.pdf");
}
```