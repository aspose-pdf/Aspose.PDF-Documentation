---
title: FDF를 XML 형식으로 변환
type: docs
weight: 10
url: /ko/net/converting-an-fdf-to-xml-format/
description: 이 섹션은 FormDataConverter 클래스를 사용하여 FDF를 XML 형식으로 변환하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/ko/net/)의 [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 네임스페이스는 AcroForms를 매우 잘 지원합니다. 또한 FDF, XFDF 및 XML과 같은 다양한 파일 형식으로 양식 데이터를 가져오고 내보내는 것도 지원합니다. 그러나 때때로 개발자는 한 형식을 다른 형식으로 변환해야 할 수도 있습니다. 이 문서는 FDF를 XML로 변환하는 기능을 살펴봅니다.

{{% /alert %}}

## Details

FDF는 Forms Data Format을 의미하며, FDF 파일은 키/값 쌍으로 양식 값을 포함합니다.
``` 우리는 또한 XML 파일이 값을 태그로 포함하고 있다는 것을 알고 있습니다. 여기서 주로 키는 태그 이름으로, 값은 해당 태그 내의 값으로 표현됩니다. 이제 [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)는 FDF 파일 형식을 XML 형식으로 변환할 수 있는 유연성을 제공합니다.

이 목적을 위해 [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter) 클래스를 사용할 수 있습니다. 이 클래스는 한 데이터 형식을 다른 형식으로 변환하는 다양한 메소드를 제공합니다. 이 기사에서는 [ConvertFdfToXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml)이라는 하나의 메소드만 사용할 것입니다. 이 메소드는 FDF 파일을 입력 또는 소스 스트림으로 받아 XML 형식으로 저장합니다.

다음 코드 스니펫은 FDF 파일을 XML 파일로 변환하는 방법을 보여줍니다: