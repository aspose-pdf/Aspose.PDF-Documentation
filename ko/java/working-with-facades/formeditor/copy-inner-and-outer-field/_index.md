---
title: 내부 및 외부 필드 복사
type: docs
weight: 40
url: /ko/java/copy-inner-and-outer-field/
description: 이 섹션은 FormEditor 클래스를 사용하여 com.aspose.pdf.facades로 내부 및 외부 필드를 복사하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

[copyInnerField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyInnerField-java.lang.String-java.lang.String-int-) 메소드는 같은 파일의 동일한 좌표에 지정된 페이지에 필드를 복사할 수 있게 해줍니다. 이 메소드는 복사하려는 필드 이름, 새로운 필드 이름, 필드를 복사할 페이지 번호가 필요합니다. [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 클래스는 이 메소드를 제공합니다. 다음 코드 스니펫은 동일한 파일의 동일한 위치에 필드를 복사하는 방법을 보여줍니다.

```java
    public static void CopyInnerField() {
        FormEditor editor = new FormEditor();
        Document document = new Document(_dataDir + "Sample-Form-01.pdf");
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyInnerField("Last Name", "Last Name 2", 2);
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## 기존 PDF 파일에서 외부 필드 복사

[copyOuterField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyOuterField-java.lang.String-java.lang.String-) 메서드를 사용하면 외부 PDF 파일에서 양식 필드를 복사한 후 입력 PDF 파일에 동일한 위치와 지정된 페이지 번호에 추가할 수 있습니다. 이 메서드는 필드를 복사할 PDF 파일, 필드 이름 및 필드를 복사할 페이지 번호가 필요합니다. 이 메서드는 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 클래스에서 제공합니다. 다음 코드 스니펫은 외부 PDF 파일에서 필드를 복사하는 방법을 보여줍니다.

```java
  public static void CopyOuterField() {
        FormEditor editor = new FormEditor();
        Document document = new Document();
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
        editor.save(_dataDir + "Sample-Form-02-mod.pdf");
    }
```