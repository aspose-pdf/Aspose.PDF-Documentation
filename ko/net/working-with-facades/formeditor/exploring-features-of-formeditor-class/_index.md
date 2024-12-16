---
title: FormEditor 클래스의 기능 탐색
type: docs
weight: 10
url: /ko/net/exploring-features-of-formeditor-class/
description: Aspose. PDF for .NET 라이브러리를 사용하여 FormEditor 클래스의 기능 탐색에 대한 세부 정보를 배울 수 있습니다.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

PDF 문서에는 때때로 AcroForm으로 알려진 대화형 폼이 포함되어 있습니다. 이는 웹 페이지에서 사용되는 폼과 유사합니다. 이러한 폼에는 텍스트 상자, 체크 상자, 버튼 등 다양한 유형의 컨트롤이 포함됩니다. PDF 파일을 다루는 개발자는 때때로 이러한 폼을 편집해야 할 수도 있습니다. 이 기사에서는 [Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)가 이를 가능하게 하는 방법에 대해 자세히 살펴보겠습니다.

{{% /alert %}}

## 구현 세부 사항

개발자는 [Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)를 사용하여 PDF 문서에 새 폼과 폼 필드를 추가할 수 있을 뿐만 아니라 기존 필드를 편집할 수도 있습니다. 이 문서의 범위는 양식 편집을 처리하는 [Aspose.PDF for .NET](/pdf/ko/net/)의 기능으로 제한됩니다.

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)는 양식 필드를 편집할 수 있는 대부분의 메서드와 속성을 포함하는 클래스입니다. 새로운 필드를 추가할 수 있을 뿐만 아니라 기존 필드를 제거하거나 한 필드를 다른 위치로 이동하거나 필드 이름이나 속성을 변경하는 등의 작업이 가능합니다. 이 클래스에서 제공하는 기능 목록은 상당히 포괄적이며, 이 클래스를 사용하여 양식 필드를 매우 쉽게 작업할 수 있습니다.

이러한 메서드는 필드를 조작하는 데 사용되는 것과 이 필드의 새로운 속성을 설정하는 데 사용되는 두 가지 주요 범주로 나눌 수 있습니다. 첫 번째 범주에 포함할 수 있는 메서드에는 AddField, AddListItem, RemoveListItem, CopyInnerField, CopyOuterField, DelListItem, MoveField, RemoveField, RenameField 등이 있습니다. 두 번째 범주의 메서드에는 SetFieldAlignment, SetFieldAppearance, SetFieldAttribute, SetFieldLimit, SetFieldScript가 포함될 수 있습니다. 다음 코드 스니펫은 FormEditor 클래스의 일부 메서드가 작동하는 것을 보여줍니다:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-FormEditorFeatures-FormEditorFeatures.cs" >}}