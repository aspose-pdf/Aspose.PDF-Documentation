---
title: 아크로폼 채우기
linktitle: 아크로폼 채우기
type: docs
weight: 20
url: ko/java/fill-form/
description: 이 섹션에서는 Aspose.PDF for Java를 사용하여 PDF 문서의 양식 필드를 채우는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 문서는 양식을 만들기에 훌륭하며, 정말로 선호되는 파일 형식입니다.

Aspose.PDF for Java를 사용하면 문서 객체의 Form 컬렉션에서 필드를 가져와 양식 필드를 채울 수 있습니다.

다음 예제를 통해 이 작업을 해결하는 방법을 살펴보겠습니다:

```java
public class ExamplesFillForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void FillFormFieldPDFDocument() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // 필드 생성
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("텍스트 상자");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // 문서에 필드 추가
        pdfDocument.getForm().add(textBoxField, 1);

        // 수정된 PDF 저장
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }

    
}
```