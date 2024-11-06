---
title: 양식 필드 이름 식별
type: docs
weight: 10
url: ko/net/identifying-form-fields-names/
description: Aspose.PDF.Facades를 사용하여 Form 클래스의 양식 필드 이름을 식별할 수 있습니다.
lastmod: "2021-06-05"
draft: false
---

[Aspose.PDF for .NET](/pdf/net/)은 이미 생성된 Pdf 양식을 생성, 편집 및 채우는 기능을 제공합니다. [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 네임스페이스에는 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 클래스가 포함되어 있으며, 이는 [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index)라는 함수를 포함하고 있으며 두 개의 인수, 즉 필드 이름과 필드 값을 필요로 합니다. 따라서 양식 필드를 채우기 위해서는 정확한 양식 필드 이름을 알고 있어야 합니다.

## 구현 세부사항

우리는 종종 어떤 도구에서 생성된 양식을 채워야 하는 상황에 직면합니다. Adobe Designer, 그리고 우리는 양식 필드 이름에 대해 확신이 없습니다. 따라서 양식 필드를 채우려면 먼저 모든 PDF 양식 필드의 이름을 읽어야 합니다. [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 클래스는 [FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames)라는 속성을 제공하며, 이 속성은 전체 필드의 이름을 반환하고 PDF에 필드가 없으면 null을 반환합니다. 그러나 이 속성을 사용할 때 PDF 양식의 전체 필드 이름을 얻을 수 있으며 어떤 이름이 양식의 어느 필드에 해당하는지 확신할 수 없습니다.

이 문제의 해결책으로, 우리는 각 필드의 외관 속성을 사용할 것입니다. Form 클래스에는 위치, 색상, 테두리 스타일, 글꼴, 목록 항목 등을 포함한 속성을 반환하는 [GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade)라는 함수가 있습니다. 이러한 값을 저장하려면 필드의 시각적 속성을 기록하는 데 사용되는 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade) 클래스를 사용해야 합니다. 이러한 속성을 얻은 후에는 필드 이름을 표시할 모든 필드 아래에 텍스트 필드를 추가할 수 있습니다.

{{% alert color="primary" %}}
이 시점에서 "텍스트 필드를 추가할 위치를 어떻게 결정할 것인가?"라는 질문이 제기됩니다.
{{% /alert %}}

{{% alert color="primary" %}}
이 문제에 대한 해결책은 필드의 위치를 ​​저장하는 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade) 클래스의 Box 속성입니다. 이 값을 직사각형 유형의 배열에 저장하고 이 값을 사용하여 새 텍스트 필드를 추가할 위치를 식별해야 합니다.

{{% /alert %}}

[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 네임스페이스에는 PDF 양식을 조작할 수 있는 기능을 제공하는 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor)라는 클래스가 있습니다. PDF 양식을 열고, 기존 양식 필드 아래에 텍스트 필드를 추가하고, 새로운 이름으로 PDF 양식을 저장합니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-IdentifyFormFields-IdentifyFormFields.cs" >}}