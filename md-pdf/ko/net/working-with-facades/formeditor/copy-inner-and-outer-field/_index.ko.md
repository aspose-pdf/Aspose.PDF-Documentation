---
title: 내부 및 외부 필드 복사
type: docs
weight: 40
url: /net/copy-inner-and-outer-field/
description: 이 섹션에서는 FormEditor 클래스를 사용하여 Aspose.PDF Facades로 내부 및 외부 필드를 복사하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

[CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) 메서드를 사용하면 동일한 파일의 지정된 페이지에서 동일한 좌표에 필드를 복사할 수 있습니다. 이 메서드는 복사하려는 필드 이름, 새 필드 이름 및 필드를 복사할 페이지 번호가 필요합니다. [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 클래스는 이 메서드를 제공합니다. 다음 코드 스니펫은 동일한 파일의 동일한 위치에 필드를 복사하는 방법을 보여줍니다.

```csharp
  public static void CopyInnerField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document(_dataDir + "Sample-Form-01.pdf");
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyInnerField("Last Name", "Last Name 2", 2);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## 기존 PDF 파일에서 외부 필드 복사

[CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) 메소드는 외부 PDF 파일에서 양식 필드를 복사한 후 입력 PDF 파일의 동일한 위치와 지정된 페이지 번호에 추가할 수 있도록 합니다. 이 메소드는 필드를 복사해야 하는 PDF 파일, 필드 이름 및 필드를 복사해야 하는 페이지 번호가 필요합니다. 이 메소드는 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 클래스에서 제공됩니다. 다음 코드 조각은 외부 PDF 파일에서 필드를 복사하는 방법을 보여줍니다.

```csharp
   public static void CopyOuterField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document();
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
            editor.Save(_dataDir + "Sample-Form-02-mod.pdf");
        }
```