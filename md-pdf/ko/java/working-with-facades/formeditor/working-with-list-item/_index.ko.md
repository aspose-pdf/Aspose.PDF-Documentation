---
title: 목록 항목 작업
type: docs
weight: 30
url: /java/working-with-list-item/
description: 이 섹션은 FormEditor 클래스를 사용하여 com.aspose.pdf.facades로 목록 항목을 작업하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일에 목록 항목 추가

[addListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addListItem-java.lang.String-java.lang.String-) 메소드는 ListBox 필드에 항목을 추가할 수 있게 해줍니다. 첫 번째 인수는 필드 이름이고 두 번째 인수는 필드 항목입니다. 단일 필드 항목을 전달하거나 항목 목록이 포함된 문자열 배열을 전달할 수 있습니다. 이 메소드는 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 클래스에 의해 제공됩니다. 다음 코드 스니펫은 PDF 파일에 목록 항목을 추가하는 방법을 보여줍니다.

```java
public static void AddListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        editor.addField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
        editor.addListItem("Country", "USA");
        editor.addListItem("Country", "Canada");
        editor.addListItem("Country", "France");
        editor.addListItem("Country", "Spain");
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## 기존 PDF 파일에서 항목 삭제

[delListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#delListItem-java.lang.String-java.lang.String-) 메서드를 사용하면 ListBox에서 특정 항목을 삭제할 수 있습니다. 첫 번째 매개변수는 필드 이름이고, 두 번째 매개변수는 목록에서 삭제하려는 항목입니다. 이 메서드는 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 클래스에서 제공됩니다. 다음 코드 스니펫은 PDF 파일에서 목록 항목을 삭제하는 방법을 보여줍니다.

```java
    public static void DelListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-04.pdf");
        // -----
        editor.delListItem("Country", "France");
        // -----
        editor.save(_dataDir + "Sample-Form-04-mod.pdf");
    }
```