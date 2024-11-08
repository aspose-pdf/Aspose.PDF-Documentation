---
title: FDF, XML, XFDF 형식의 차이점은 무엇인가
type: docs
weight: 30
url: /ko/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: 이 섹션은 Aspose.PDF Facades에서 Form Class를 사용하여 XML, FDF 및 XFDF 양식의 차이점을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

우리는 FDF, XML 및 XFDF와 같은 다양한 용어들을 혼합하여 사용했습니다. 이 모든 용어들은 어느 정도 서로 관련이 있습니다. 이 기사는 이러한 개념과 서로의 관계를 탐구합니다.

{{% /alert %}}

## 양식 해체

Aspose.PDF for .NET은 Adobe에서 표준화한 PDF 문서를 조작하는 데 사용됩니다. 그리고 PDF 문서는 AcroForms라고 불리는 대화형 양식을 포함하고 있습니다. 이러한 대화형 양식에는 콤보, 텍스트 상자 및 라디오 버튼과 같은 여러 양식 필드가 있습니다. Adobe의 대화형 양식 및 양식 필드는 HTML 양식 및 그 양식 필드와 동일한 방식으로 작동합니다.

양식 필드의 값을 별도의 파일에 저장하는 것이 가능합니다: FDF (Forms Data Format) 파일. 이 문서에는 키/값 방식으로 양식 필드의 값이 포함되어 있습니다. FDF 파일은 여전히 이 목적으로 사용됩니다. 하지만 Adobe는 XFDF라는 XML 인코딩된 FDF 유형도 제공합니다. XFDF 파일은 XML 태그를 사용하여 계층적 방식으로 양식 필드의 값을 저장합니다.

Aspose.PDF를 사용하면 개발자가 PDF 양식 필드의 값을 FDF 또는 XFDF 파일뿐만 아니라 XML 파일로도 내보낼 수 있습니다. 이러한 모든 파일은 PDF 양식 필드 값을 저장하기 위해 서로 다른 구문을 사용합니다. 아래 예시는 그 차이점을 설명합니다.

PDF 양식 필드의 값이 FDF, XML 및 XFDF 형식으로 표현되어야 하는 경우를 가정해 보겠습니다. 해당 필드 이름과 값이 포함된 가정된 양식 필드는 아래와 같습니다:

|**필드 이름**|**필드 값**|
| :- | :- |
|Company|Aspose.com|
|Address.1|Sydney, Australia|
|Address.2|Additional Address Line|
이제 이러한 값을 FDF, XML 및 XFDF 형식으로 어떻게 표현하는지 살펴보겠습니다.

### FDF 형식이란 무엇인가요?

FDF 파일이 /T가 키를 나타내고, /V가 값을 나타내며, 괄호 ()에 있는 데이터가 키 또는 값의 내용을 나타내는 키/값 방식으로 데이터를 저장한다는 것을 알고 있습니다. 예를 들어, /T(Company)는 Company가 필드 키를 의미하고 /V(Aspose.com)은 필드 값을 의미합니다.

/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Additional Address Line)

### XML 형식이란 무엇입니까?

개발자는 각 PDF 폼 필드를 `<field>` 태그 형태로 나타낼 수 있습니다. 각 필드 태그는 필드 이름을 나타내는 이름 속성과 아래와 같이 필드 값을 나타내는 `<value>` 하위 태그를 가집니다:

```xml
 <?xml version="1.0" ?>
 <fields>
  <field name="Company">
    <value>Aspose.com</value>
  </field>
  <field name="Address.1">
    <value>Sydney, Australia</value>
  </field>
  <field name="Address.2">
    <value>Additional Address Line</value>
  </field>
 </fields>
```

### XFDF 형식이란 무엇입니까?

위의 데이터를 XFDF 형식으로 표현하는 것은 몇 가지 차이점을 제외하고 XML 형식과 유사합니다. XFDF 파일에서는 XML 네임스페이스를 추가합니다. 이는 <http://ns.adpbe.com/xfdf/>이며, PDF 양식 필드가 포함된 PDF 문서를 가리키기 위해 사용되는 추가 태그 `<f>`가 있습니다. XML과 마찬가지로, XFDF도 필드 태그 `<field>`의 형태로 필드를 포함합니다. 아래와 같이 표시됩니다:

```xml

<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">   
   <f href="CompanyForm.pdf"/> 
   <fields>
      <field name="Company">
         <value>Aspose.com</value>
      </field>
      <field name="Address">
         <field name="1">
            <value>Sydney, Australia</value>
         </field>
         <field name="2">
            <value>Additional Address Line</value>
         </field>
      </field>
   </fields>
 </xfdf>
```

### 양식 필드 이름 식별

Aspose.PDF for .NET는 이미 생성된 PDF 양식을 생성, 편집 및 채울 수 있는 기능을 제공합니다. It contains [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) class, which has the function named [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) , and it takes two parameters i.e. Field name that needs to be filled, and the field value. So in-order to fill the form fields, you must be aware of the exact form field name.  
[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 클래스는 [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index)라는 이름의 기능을 포함하고 있으며, 이는 두 가지 매개변수, 즉 채워야 할 필드 이름과 필드 값을 필요로 합니다. 따라서 양식 필드를 채우려면 정확한 양식 필드 이름을 알고 있어야 합니다.  
We often come across the scenario in which we need to fill the form which is created in some tool i.e.  
종종 우리는 일부 도구에서 생성된 양식을 채워야 하는 상황에 직면합니다. Adobe Designer, 그리고 우리는 양식 필드 이름에 대해 확신하지 못합니다. 우리의 요구 사항을 충족시키기 위해, 우리는 모든 PDF 양식 필드의 이름을 읽어야 합니다. [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 클래스는 [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames)라는 속성을 제공하며, 이는 모든 필드의 이름을 반환하고 PDF에 필드가 없으면 null을 반환합니다. 그러나 이 속성은 모든 PDF 양식 필드의 이름을 반환하므로, 어떤 이름이 양식의 어떤 필드에 해당하는지 확신할 수 없습니다.

이 문제에 대한 해결책으로, 우리는 각 필드의 외관 속성이 필요할 것입니다. [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) 클래스에는 위치, 색상, 테두리 스타일, 글꼴, 목록 항목 등을 포함한 속성을 반환하는 GetFieldFacade라는 함수가 있습니다. 이러한 값을 저장하기 위해 필드의 시각적 속성을 기록하는 데 사용되는 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 클래스를 사용할 것입니다. 이러한 속성을 얻은 후 모든 필드 아래에 필드 이름을 표시하는 텍스트 필드를 추가할 수 있습니다. 여기서 텍스트 필드를 추가할 위치를 어떻게 결정할 것인가에 대한 질문이 생깁니다. 이 문제의 해결책은 필드의 위치를 ​​저장하는 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 클래스의 Box 속성입니다. 이러한 값을 사각형 유형의 배열로 저장하고 이러한 값을 사용하여 새 텍스트 필드를 추가할 위치를 식별합니다. Aspose.Pdf.Facades 네임스페이스에는 PDF 양식을 조작할 수 있는 기능을 제공하는 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)라는 클래스가 있습니다. Open a PDF form add a text field beneath every existing form field and save the PDF form with new name.

PDF 양식을 열고 모든 기존 양식 필드 아래에 텍스트 필드를 추가하고 새 이름으로 PDF 양식을 저장합니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-DifferenceBetweenFile-DifferenceBetweenFile.cs" >}}