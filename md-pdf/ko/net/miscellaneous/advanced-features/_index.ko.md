---
title: 고급 기능
type: docs
weight: 210
url: /net/advanced-features/
---

## 브라우저로 PDF 다운로드 보내기

ASP.NET 애플리케이션을 개발할 때 때때로 물리적으로 저장하지 않고 웹 브라우저에 PDF 파일을 보내야 할 필요가 있습니다. 이를 달성하기 위해 PDF 문서를 생성한 후 MemoryStream 객체에 저장하고 그 MemoryStream에서 바이트를 Response 객체로 전달할 수 있습니다. 이렇게 하면 브라우저가 생성된 PDF 문서를 다운로드하게 됩니다.

다음 코드 스니펫은 위 기능을 보여줍니다:

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-Examples.Web-SendPdfToBrowserForDownload.aspx-1.cs" >}}

## PDF 파일에서 내장 파일 추출

Aspose.PDF는 PDF 형식 파일을 다루는 고급 기능에서 두드러집니다. 다른 도구가 제공하는 기능보다 내장 파일을 더 잘 추출합니다.

Aspose.PDF for .NET을 사용하면 내장된 글꼴, 이미지, 비디오 또는 오디오 등 어떤 내장 파일이든 효율적으로 추출할 수 있습니다.
Aspose.PDF for .NET을 사용하면 임베디드 글꼴, 이미지, 비디오 또는 오디오일 수 있는 임베디드 파일을 효율적으로 추출할 수 있습니다.

다음 코드 스니펫은 PDF 파일에서 모든 임베디드 파일을 추출합니다:

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-DocumentConversion-PDFToXML-PDFToXML.cs" >}}

## 라텍스 스크립트를 사용하여 수학 표현식 추가

Aspose.PDF를 사용하면 라텍스 스크립트를 사용하여 PDF 문서 내부에 수학 표현식/공식을 추가할 수 있습니다. 다음 예제는 표 셀 내부에 수학 공식을 추가하는 두 가지 방법을 보여줍니다:

### 서문과 문서 환경 없이

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript-WithoutPreambleanddocument.cs" >}}

### 서문과 문서 환경 포함

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript2-WithPreambleanddocument.cs" >}}

### 라텍스 태그 지원
### Latex 태그 지원

align 환경은 amsmath 패키지에 정의되어 있으며, proof 환경은 amsthm 패키지에 정의되어 있습니다. 따라서 문서 전문에 \usepackage 명령을 사용하여 이러한 패키지를 지정해야 합니다. 이는 LaTeX 텍스트를 다음 코드 샘플에 표시된 것처럼 문서 환경에 넣어야 함을 의미합니다.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Text-UseLatexScript3-UseLatexScript3.cs" >}}
