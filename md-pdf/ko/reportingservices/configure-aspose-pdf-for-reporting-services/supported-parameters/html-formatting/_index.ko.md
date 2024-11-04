---
title: HTML Formatting
type: docs
weight: 20
url: /reportingservices/html-formatting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

때때로 텍스트 상자에서 서식을 사용하여 텍스트를 내보내고 싶을 수 있습니다. 불행히도 Reporting Services는 이를 지원하지 않습니다. 그러나 Aspose.PDF for Reporting Services를 사용하여 이를 구현할 수 있습니다. 모든 텍스트 상자의 텍스트가 HTML로 처리되는 특수 모드를 활성화하고 출력 문서에서 텍스트를 서식 지정하기 위해 필요한 HTML 태그를 넣습니다. 예를 들어, 같은 텍스트 상자에 일반, 굵게 및 기울임꼴 텍스트를 넣으려면 다음 텍스트 상자 값을 입력하십시오:

Some of this text is ```<b>bold</b>``` and other text is ```<i>italic</i>```.

내보낸 후 텍스트는 일부 텍스트가 **볼드**이고 다른 텍스트가 *이탤릭체*인 것처럼 보일 것입니다.

이 방법에는 몇 가지 제한 사항이 있음을 유의하십시오.

{{% /alert %}}

{{% alert color="primary" %}}

- 디자인 시간에는 서식이 보이지 않습니다(Report Builder, Reporting Services 웹 포털 등). HTML 태그 형태의 일반 텍스트로 표시됩니다.
- Aspose.PDF for Reporting Services 렌더링 확장은 텍스트 상자에서 HTML 코드를 인식하고 적절히 포맷합니다. Reporting Services의 기본 PDF 렌더러는 이 마크업을 일반 텍스트로 내보냅니다.

**매개변수 이름**: IsHtmlTagSupported  
**데이터 유형**: Boolean  
**지원되는 값**: True, False (기본값)   

**예시**

{{< highlight csharp >}}

 <Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

보고서 디자이너에 이 매개변수를 추가하려면 'Boolean' 데이터 유형을 사용하세요.

현재 Aspose.Pdf for Reporting Services는 모든 HTML 태그의 일부를 지원합니다. 더 많은 정보는 Aspose.PDF [문서](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom)에서 확인할 수 있습니다. 

{{% /alert %}}