---
title: PDF 양식 필드 추가
type: docs
weight: 10
url: /ko/net/add-form-fields/
description: 이 주제는 FormEditor 클래스를 사용하여 Aspose.PDF Facades로 양식 필드를 작업하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일에 양식 필드 추가

기존 PDF 파일에 양식 필드를 추가하려면 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 클래스의 [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) 메서드를 사용해야 합니다. 이 방법은 추가하려는 필드의 유형을 이름 및 위치와 함께 지정해야 합니다. [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 클래스의 객체를 생성하고, [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) 메서드를 사용하여 PDF에 새 필드를 추가합니다. 또한, [SetFieldLimit](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldlimit)을 사용하여 필드의 문자 수 제한을 지정할 수 있으며, 마지막으로 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 기존 PDF 파일에 양식 필드를 추가하는 방법을 보여줍니다.

```csharp
   public static void AddField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir+"Sample-Form-01.pdf");
            editor.AddField(FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);
            editor.SetFieldLimit("Country", 20);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```
## 기존 PDF 파일에 제출 버튼 URL 추가하기

[AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) 메소드는 PDF 파일에 제출 버튼의 URL을 설정할 수 있도록 해줍니다. 이는 제출 버튼이 클릭될 때 데이터가 게시되는 URL입니다. 예제 코드에서는 URL, 필드의 이름, 추가할 페이지 번호 및 버튼 배치 좌표를 지정합니다. [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) 메소드는 제출 버튼 필드의 이름과 URL이 필요합니다. 이 메소드는 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 클래스에 의해 제공됩니다. 다음 코드 조각은 제출 버튼 URL을 설정하는 방법을 보여줍니다.

```csharp
public static void AddSubmitBtn()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## 푸시 버튼에 자바스크립트 추가

[AddFieldScript](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfieldscript) 메서드는 PDF 파일의 푸시 버튼에 자바스크립트를 추가할 수 있게 해줍니다. 이 메서드는 푸시 버튼의 이름과 자바스크립트를 필요로 합니다. 이 메서드는 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 클래스에 의해 제공됩니다. 다음 코드 스니펫은 푸시 버튼에 자바스크립트를 설정하는 방법을 보여줍니다.

```csharp
     public static void AddFieldScript()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```