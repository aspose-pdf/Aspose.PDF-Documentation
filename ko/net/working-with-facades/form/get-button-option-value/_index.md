---
title: Get Button Option Value
type: docs
weight: 40
url: /ko/net/get-button-option-value/
description: 이 섹션에서는 Form Class를 사용하여 Aspose.PDF Facades로 버튼 옵션 값을 얻는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일에서 버튼 옵션 값 가져오기

라디오 버튼은 다양한 옵션을 보여주는 방법을 제공합니다. [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 클래스는 특정 라디오 버튼에 대한 모든 버튼 옵션 값을 가져올 수 있도록 합니다. [GetButtonOptionValues](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues) 메서드를 사용하여 이러한 값을 얻을 수 있습니다. 이 메서드는 입력 매개변수로 라디오 버튼의 이름을 필요로 하며 Hashtable을 반환합니다. 이 Hashtable을 반복하여 옵션 값을 얻을 수 있습니다. 다음 코드 스니펫은 기존 PDF 파일에서 버튼 옵션 값을 가져오는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetButtonOptionValue.cs" >}}

## 기존 PDF 파일에서 현재 버튼 옵션 값 가져오기

라디오 버튼은 옵션 값을 설정하는 방법을 제공하지만, 한 번에 하나만 선택할 수 있습니다. 현재 선택된 옵션 값을 얻으려면 [GetButtonOptionCurrentValue 메서드를 사용할 수 있습니다. [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 클래스는 이 메서드를 제공합니다. [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) 메서드는 라디오 버튼 이름을 입력 매개변수로 요구하며 문자열로 값을 반환합니다. 다음 코드 스니펫은 기존 PDF 파일에서 현재 버튼 옵션 값을 가져오는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetCurrentValue.cs" >}}