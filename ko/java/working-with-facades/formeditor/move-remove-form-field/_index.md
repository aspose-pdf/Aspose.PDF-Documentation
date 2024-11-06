---
title: 양식 필드 이동 및 제거
type: docs
weight: 50
url: ko/java/move-remove-form-field/
description: 이 섹션에서는 FormEditor 클래스를 사용하여 양식 필드를 이동하고 제거하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일에서 양식 필드를 새 위치로 이동

양식 필드를 새 위치로 이동하려면 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 클래스의 [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-) 메서드를 사용할 수 있습니다.
 필드 이름과 이 필드의 새 위치만 [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-) 메서드에 제공하면 됩니다. 또한 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 클래스의 Save 메서드를 사용하여 업데이트된 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 PDF 파일에서 양식 필드를 새 위치로 이동하는 방법을 보여줍니다.

```java
 public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## 기존 PDF 파일에서 양식 필드 삭제

기존 PDF 파일에서 양식 필드를 삭제하려면 FormEditor 클래스의 RemoveField 메서드를 사용할 수 있습니다. 이 메서드는 하나의 인수만 받습니다: 필드 이름. FormEditor 클래스의 객체를 생성하고, [removeField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#removeField-java.lang.String-) 메서드를 호출하여 PDF에서 특정 필드를 제거한 후, Save 메서드를 호출하여 업데이트된 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 기존 PDF 파일에서 양식 필드를 삭제하는 방법을 보여줍니다.

```java
 public static void RemoveFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RemoveField("First Name");
            editor.RemoveField("Last Name");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```

## PDF에서 양식 필드 이름 변경하기

또한 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 클래스의 [renameField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#renameField-java.lang.String-java.lang.String-) 메서드를 사용하여 필드의 이름을 변경할 수 있습니다.
```java
    public static void RenameFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RenameField("성", "LastName");
            editor.RenameField("이름", "FirstName");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```