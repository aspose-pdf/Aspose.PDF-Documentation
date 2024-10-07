---
title: 텍스트 상자 필드에서 텍스트 양쪽 맞춤
type: docs
weight: 20
url: /net/justify-text-in-a-textbox-field/
description: 이 기사는 Form Class를 사용하여 텍스트 상자 필드에서 텍스트를 양쪽 맞춤하는 방법을 보여줍니다.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

이 기사에서는 PDF 파일의 텍스트 상자 필드에서 텍스트를 양쪽 맞춤하는 방법을 보여드립니다.

{{% /alert %}}

## 구현 세부사항

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 클래스는 [Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)에서 PDF 양식 필드를 꾸밀 수 있는 기능을 제공합니다. 이제 텍스트 상자 필드에서 텍스트를 양쪽 정렬하려면 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 열거형의 [AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) 값을 사용하고 [FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/methods/decoratefield/index) 메서드를 호출하여 쉽게 달성할 수 있습니다. 아래 예제에서는 먼저 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 클래스의 [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.form/methods/fillfield/index) 메서드를 사용하여 텍스트 상자 필드를 채웁니다. 그 후에 FormEditor 클래스를 사용하여 텍스트 상자 필드의 텍스트를 양쪽 정렬합니다. 다음 코드 스니펫은 텍스트 상자 필드에서 텍스트를 양쪽 정렬하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-JustifyText-JustifyText.cs" >}}
```
PDF는 양쪽 맞춤을 지원하지 않으므로 텍스트 상자 필드에 텍스트를 입력할 때 텍스트는 왼쪽으로 정렬됩니다. 그러나 필드가 활성 상태가 아닐 때는 텍스트가 양쪽 맞춤으로 표시됩니다.
```