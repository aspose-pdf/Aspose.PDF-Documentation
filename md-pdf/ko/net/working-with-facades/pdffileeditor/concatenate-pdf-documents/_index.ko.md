---
title: C#에서 PDF 문서 연결
linktitle: PDF 문서 연결
type: docs
weight: 20
url: /net/concatenate-pdf-documents/
description: 이 섹션은 PdfFileEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 문서를 연결하는 방법을 설명합니다.
aliases:
    - /pdf/net/concatenate-multiple-pdf-files-using-memorystreams/
    - /pdf/net/concatenate-pdf-files-and-create-table-of-contents/
    - /pdf/net/concatenate-pdf-forms-and-keep-fields-names-unique/
    - /pdf/net/concatenating-all-pdf-files-in-particular-folder/
    - /pdf/net/how-to-concatenate-pdf-files-in-different-ways/
    - /pdf/net/append-pdf-files/
lastmod: "2021-06-05"
---

## **개요**

이 문서는 C#을 사용하여 서로 다른 PDF 파일을 하나의 PDF로 병합, 결합 또는 연결하는 방법을 설명합니다. 다음과 같은 주제를 다룹니다.

- [C# PDF 파일 병합](#concatenate-pdf-files-using-file-paths)
- [C# PDF 파일 결합](#concatenate-pdf-files-using-file-paths)

- [C# 여러 PDF 파일을 하나의 PDF로 병합](#concatenate-array-of-pdf-files-using-file-paths)
- [C# 여러 PDF 파일을 하나의 PDF로 결합](#concatenate-array-of-pdf-files-using-file-paths)
- [C# 폴더 내 모든 PDF 파일 병합](#concatenating-all-pdf-files-in-particular-folder)
- [C# 폴더 내 모든 PDF 파일 결합](#concatenating-all-pdf-files-in-particular-folder)
- [C# 파일 경로를 사용하여 PDF 파일 병합](#concatenate-pdf-files-using-file-paths)
- [C# 스트림을 사용하여 PDF 파일 결합](#concatenate-array-of-pdf-files-using-streams)
- [C# 폴더의 모든 PDF 파일 연결](#concatenate-pdf-files-in-folder)

## 파일 경로를 사용하여 PDF 파일 연결

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)는 여러 PDF 파일을 연결할 수 있도록 하는 [Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 내의 클래스입니다. 파일 스트림을 사용하여 파일을 연결할 수 있을 뿐만 아니라 메모리 스트림을 사용하여도 가능합니다. 이 문서에서는 메모리 스트림을 사용하여 파일을 연결하는 과정을 설명하고 코드 스니펫을 사용하여 이를 보여줍니다.

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메소드는 두 개의 PDF 파일을 연결하는 데 사용할 수 있습니다. [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메소드는 첫 번째 입력 PDF, 두 번째 입력 PDF, 출력 PDF의 세 가지 매개변수를 전달할 수 있습니다. 최종 출력 PDF에는 두 입력 PDF 파일이 모두 포함됩니다.

다음 C# 코드 스니펫은 파일 경로를 사용하여 PDF 파일을 연결하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-ConcatenateUsingPath.cs" >}}

경우에 따라 많은 개요가 있을 때, 사용자는 CopyOutlines를 false로 설정하여 성능을 향상시키고 연결을 수행할 수 있습니다.
{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-CopyOutline.cs" >}}

## MemoryStreams를 사용하여 여러 PDF 파일 연결

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메서드는 소스 PDF 파일과 대상 PDF 파일을 매개변수로 사용합니다. 이러한 매개변수는 디스크에 있는 PDF 파일의 경로일 수도 있고 MemoryStreams일 수도 있습니다. 이제 이 예제에서는 먼저 두 개의 파일 스트림을 만들어 디스크에서 PDF 파일을 읽습니다. 그런 다음 이러한 파일을 바이트 배열로 변환합니다. PDF 파일의 이러한 바이트 배열은 MemoryStreams로 변환됩니다. PDF 파일에서 MemoryStreams를 얻으면 이를 연결 메서드로 전달하고 하나의 출력 파일로 병합할 수 있습니다.

다음 C# 코드 스니펫은 MemoryStreams를 사용하여 여러 PDF 파일을 연결하는 방법을 보여줍니다:

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenateMultiplePDFUsingMemoryStream-ConcatenateMultiplePDFUsingMemoryStream.cs" >}}

## 파일 경로를 사용하여 PDF 파일 배열 연결

여러 개의 PDF 파일을 연결하려면 PDF 파일 배열을 전달할 수 있는 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메서드의 오버로드를 사용할 수 있습니다. 최종 출력은 배열의 모든 파일에서 생성된 병합 파일로 저장됩니다. 다음 C# 코드 스니펫은 파일 경로를 사용하여 PDF 파일 배열을 연결하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfFilesWithPath-ConcatenateArrayOfFilesWithPath.cs" >}}

## 스트림을 사용하여 PDF 파일 배열 연결

PDF 파일 배열을 연결하는 것은 디스크에 있는 파일에만 국한되지 않습니다. 당신은 또한 스트림에서 PDF 파일 배열을 연결할 수 있습니다. 여러 PDF 파일을 연결하려면 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메서드의 적절한 오버로드를 사용할 수 있습니다. 먼저 입력 스트림 배열과 출력 PDF를 위한 하나의 스트림을 생성한 다음 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 메서드를 호출해야 합니다. 출력은 출력 스트림에 저장됩니다. 다음 C# 코드 스니펫은 스트림을 사용하여 PDF 파일 배열을 연결하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfPdfUsingStreams-ConcatenateArrayOfPdfUsingStreams.cs" >}}

## 특정 폴더의 모든 PDF 파일 연결

실행 시간에 특정 폴더의 모든 PDF 파일을 읽고 파일 이름을 알지 못하더라도 연결할 수 있습니다. 디렉토리를 포함하는 경로를 제공하십시오. 이 디렉토리에는 연결하려는 PDF 문서가 포함되어 있습니다.

이 기능을 구현하기 위해 다음 C# 코드 스니펫을 사용해 보십시오.

## PDF 양식 연결 및 필드 이름 고유 유지

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스는 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)에서 PDF 파일을 연결할 수 있는 기능을 제공합니다. 이제, 결합할 Pdf 파일들에 유사한 필드 이름을 가진 양식 필드가 있는 경우, Aspose.PDF는 결과 Pdf 파일에서 필드를 고유하게 유지할 수 있는 기능을 제공합니다. 또한, 필드 이름을 고유하게 만들기 위해 접미사를 지정할 수도 있습니다. [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)의 [KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) 속성을 true로 설정하면 Pdf 양식이 결합될 때 필드 이름이 고유해집니다. 또한, PdfFileEditor의 [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) 속성을 사용하여 결합 시 필드 이름에 추가되어 고유하게 만드는 사용자 정의 형식의 접미사를 지정할 수 있습니다. 이 문자열은 결과 파일에서 숫자로 대체될 `%NUM%` 부분 문자열을 포함해야 합니다.

이 기능을 구현하기 위한 간단한 코드 예제를 참조하십시오.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePDFForms-ConcatenatePDFForms.cs" >}}
## PDF 파일 병합 및 목차 생성

## PDF 파일 병합

PDF 파일을 병합하는 방법에 대한 정보는 다음 코드 스니펫을 참조하십시오.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-ConcatenatePdfFilesAndCreateTOC.cs" >}}

### 빈 페이지 삽입

PDF 파일이 병합된 후, 문서의 시작 부분에 빈 페이지를 삽입할 수 있습니다. 이 페이지에 목차를 생성할 수 있습니다. 이 요구 사항을 충족하려면 병합된 파일을 **Document** 객체에 로드하고 Page.Insert(...) 메서드를 호출하여 빈 페이지를 삽입해야 합니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-InsertBlankPage.cs" >}}

### 텍스트 스탬프 추가

목차를 생성하려면, 첫 페이지에 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp) 객체를 사용하여 텍스트 스탬프를 추가해야 합니다. Stamp 클래스는 `BindLogo(...)` 메서드를 제공하여 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)를 추가할 수 있으며, `SetOrigin(..)` 메서드를 사용하여 이러한 텍스트 스탬프를 추가할 위치를 지정할 수 있습니다. 이 기사에서는 두 개의 PDF 파일을 연결하고 있으므로, 이 개별 문서를 가리키는 두 개의 텍스트 스탬프 객체를 생성해야 합니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-AddTextStamps.cs" >}}

### 로컬 링크 생성

이제 연결된 파일 내부의 페이지로 향하는 링크를 추가해야 합니다. 이 요구 사항을 충족하기 위해, [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 `CreateLocalLink(..)` 메서드를 사용할 수 있습니다. 다음 코드 스니펫에서는 링크 주위의 사각형이 보이지 않도록 하기 위해 네 번째 인수로 Transparent를 전달했습니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CreateLocalLinks.cs" >}}
### Complete code

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CompletedCode.cs" >}}


## 폴더 내 PDF 파일 연결

Aspose.Pdf.Facades 네임스페이스의 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스는 PDF 파일을 연결할 수 있는 기능을 제공합니다. 실행 시 특정 폴더에 있는 모든 PDF 파일을 읽고 파일 이름을 알지 못하더라도 연결할 수 있습니다. 연결하고자 하는 PDF 문서를 포함하는 디렉토리의 경로를 제공하기만 하면 됩니다.

다음 C# 코드 조각을 사용하여 Aspose.PDF의 이 기능을 구현해 보십시오:

```csharp
// 문서 디렉토리의 경로.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

// 특정 디렉토리의 모든 PDF 파일 이름을 검색합니다.
string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

// 현재 시스템 날짜를 가져와 형식을 설정합니다.
string date = DateTime.Now.ToString("MM-dd-yyyy");
// 현재 시스템 시간을 가져와 형식을 설정합니다.
string hoursSeconds = DateTime.Now.ToString("hh-mm");
// 최종 결과 PDF 문서의 값을 설정합니다.
string masterFileName = date + "_" + hoursSeconds + "_out.pdf";

// PdfFileEditor 객체를 인스턴스화합니다.
Aspose.Pdf.Facades.PdfFileEditor pdfEditor = new PdfFileEditor();

// PdfFileEditor 객체의 Concatenate 메서드를 호출하여 모든 입력 파일을
// 단일 출력 파일로 연결합니다.
pdfEditor.Concatenate(fileEntries, dataDir + masterFileName);
```