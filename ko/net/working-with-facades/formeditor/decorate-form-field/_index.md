---
title: PDF에서 폼 필드 장식하기
type: docs
weight: 20
url: /ko/net/decorate-form-field/
description: 이 섹션은 FormEditor 클래스를 사용하여 PDF에서 폼 필드를 장식하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일에서 특정 폼 필드를 장식하기

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 클래스에 있는 [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) 메소드는 PDF 파일에서 특정 폼 필드를 장식할 수 있게 해줍니다. 
특정 필드를 꾸미려면 이 메서드에 필드 이름을 전달해야 합니다.
``` However, before calling this method, you need to create objects of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) and [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) classes. 

그러나 이 메서드를 호출하기 전에 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 및 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 클래스의 객체를 생성해야 합니다. 당신은 또한 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 객체를 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 객체의 [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) 속성에 할당해야 합니다. 그 후, [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 객체가 제공하는 모든 속성을 설정할 수 있습니다. 속성을 설정한 후, [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) 메서드를 호출하고 마지막으로 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) 메서드를 사용하여 업데이트된 PDF를 저장할 수 있습니다. 다음 코드 스니펫은 특정 폼 필드를 장식하는 방법을 보여줍니다.

```csharp
public static void DecorateField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var cityDecoration = new FormFieldFacade
            {
                Font = FontStyle.Courier,
                FontSize = 12,
                BorderColor = System.Drawing.Color.Black,
                BorderWidth = 2
            };

            editor.Facade = cityDecoration;
            editor.DecorateField("City");
            editor.Save(_dataDir + "Sample-Form-02.pdf");
        }
```
## 특정 유형의 기존 PDF 파일의 모든 필드 꾸미기

[DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) 메서드를 사용하면 PDF 파일에서 특정 유형의 모든 양식 필드를 한 번에 꾸밀 수 있습니다. If you want to decorate all fields of a particular type then you need to pass the field type to this method.
특정 유형의 모든 필드를 꾸미려면 이 메서드에 필드 유형을 전달해야 합니다. 그러나 이 메서드를 호출하기 전에 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 및 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 클래스의 객체를 생성해야 합니다. 문서의 텍스트는 다음과 같습니다:  
[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 객체를 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 객체의 [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) 속성에 할당해야 합니다. 그런 다음, [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 객체에서 제공하는 모든 속성을 설정할 수 있습니다. 속성을 설정한 후에는 [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) 메소드를 호출하고 마지막으로 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) 메소드를 사용하여 업데이트된 PDF를 저장할 수 있습니다. 다음 코드 스니펫은 특정 유형의 모든 필드를 장식하는 방법을 보여줍니다.

```csharp
        public static void DecorateField2()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var textFieldDecoration = new FormFieldFacade
            {
                Alignment = FormFieldFacade.AlignCenter,
            };

            editor.Facade = textFieldDecoration;
            editor.DecorateField(FieldType.Text);
            editor.Save(_dataDir + "Sample-Form-01-align-text.pdf");
        }
```