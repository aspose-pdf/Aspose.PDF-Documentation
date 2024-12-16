---
title: PDF에서 양식 필드 꾸미기
type: docs
weight: 20
url: /ko/java/decorate-form-field/
description: 이 섹션에서는 FormEditor 클래스를 사용하여 PDF에서 양식 필드를 꾸미는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일에서 특정 양식 필드 꾸미기

[FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 클래스에 있는 [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) 메서드는 PDF 파일에서 특정 양식 필드를 꾸밀 수 있게 해줍니다.
 특정 필드를 꾸미려면 이 메서드에 필드 이름을 전달해야 합니다. 그러나 이 메서드를 호출하기 전에 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 및 [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) 클래스의 객체를 생성해야 합니다. 그런 다음 [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) 객체에서 제공하는 모든 속성을 설정할 수 있습니다. 속성을 설정한 후 [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) 메서드를 호출하고 마지막으로 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 클래스의 Save 메서드를 사용하여 업데이트된 PDF를 저장할 수 있습니다. 다음 코드 스니펫은 특정 양식 필드를 꾸미는 방법을 보여줍니다.

```java
public static void DecorateField() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade cityDecoration = new FormFieldFacade();
        cityDecoration.setFont(FontStyle.Courier);
        cityDecoration.setFontSize(12);
        cityDecoration.setBorderColor(Color.BLACK);
        cityDecoration.setBorderWidth(2);

        editor.setFacade(cityDecoration);
        editor.decorateField("City");
        editor.save(_dataDir + "Sample-Form-02.pdf");
    }
```

## 기존 PDF 파일에서 특정 유형의 모든 필드 장식하기

[decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) 메서드는 PDF 파일에서 특정 유형의 모든 양식 필드를 한 번에 장식할 수 있도록 해줍니다.
 만약 특정 유형의 모든 필드를 장식하고 싶다면 이 메서드에 필드 유형을 전달해야 합니다. 그러나 이 메서드를 호출하기 전에 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 및 [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) 클래스의 객체를 생성해야 합니다. 그런 다음, [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) 객체가 제공하는 모든 속성을 설정할 수 있습니다. 속성을 설정한 후 [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) 메서드를 호출하고 마지막으로 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 클래스의 Save 메서드를 사용하여 업데이트된 PDF를 저장할 수 있습니다. 다음 코드 스니펫은 특정 유형의 모든 필드를 장식하는 방법을 보여줍니다.

```java
   public static void DecorateFields() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade textFieldDecoration = new FormFieldFacade();
        textFieldDecoration.setAlignment(FormFieldFacade.ALIGN_CENTER);

        editor.setFacade(textFieldDecoration);
        editor.decorateField(FieldType.Text);
        editor.save(_dataDir + "Sample-Form-01-align-text.pdf");
    }
```