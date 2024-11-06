---
title: 필드 외관 및 속성
type: docs
weight: 20
url: ko/net/changing-field-appearance-and-attributes/
description: 이 섹션에서는 FormEditor 클래스를 사용하여 필드 외관과 속성을 변경하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) 클래스는 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)에서 폼 필드의 외관과 느낌뿐만 아니라 필드의 동작도 변경할 수 있게 해줍니다. 이 기사에서는 FormEditor 클래스를 사용하여 필드 외관, 필드 속성 및 필드 제한을 변경하는 방법을 살펴보겠습니다.

{{% /alert %}}

## 구현 세부 사항

[SetFieldAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) 메서드는 폼 필드의 외관을 변경하는 데 사용됩니다. 문서 주석에 대한 플래그를 매개변수로 받습니다. AnnotationFlag는 Hidden이나 NoRotate 등 다양한 멤버를 가진 열거형입니다.

[SetFieldAttributes](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) 메서드는 양식 필드의 속성을 변경하는 데 사용됩니다. 이 메서드에 전달되는 매개변수는 ReadOnly나 Required 등과 같은 멤버를 포함하는 PropertyFlag 열거형입니다.

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) 클래스는 필드 제한을 설정하는 메서드도 제공합니다. 이는 필드가 얼마나 많은 문자를 채울 수 있는지 알려줍니다. 아래 코드 스니펫은 이러한 모든 메서드를 어떻게 사용할 수 있는지를 보여줍니다.