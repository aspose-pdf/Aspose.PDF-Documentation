---
title:  C#를 사용하여 AcroForm에서 데이터 추출
linktitle:  AcroForm에서 데이터 추출
type: docs
weight: 50
url: /ko/net/extract-data-from-acroform/
description: Aspose.PDF를 사용하면 PDF 파일에서 양식 필드 데이터를 쉽게 추출할 수 있습니다. AcroForms에서 데이터를 추출하고 JSON, XML 또는 FDF 형식으로 저장하는 방법을 알아보세요.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에서 양식 필드 추출

Aspose.PDF for .NET을 사용하면 양식 필드를 생성하고 채우는 것뿐만 아니라 PDF 파일에서 양식 필드 데이터 또는 양식 필드에 대한 정보를 쉽게 추출할 수 있습니다.

아래의 샘플 코드에서는 PDF의 각 페이지를 반복하여 PDF의 모든 AcroForm에 대한 정보와 양식 필드 값들을 추출하는 방법을 보여줍니다. 이 샘플 코드는 사전에 양식 필드의 이름을 모르는 것을 가정합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 함께 작동합니다.

```csharp
public static void ExtractFormFields()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    // 모든 필드에서 값을 가져옵니다
    foreach (Field formField in document.Form)
    {
        Console.WriteLine("필드 이름 : {0} ", formField.PartialName);
        Console.WriteLine("값 : {0} ", formField.Value);
    }
}
```
## 이름을 알고 있는 폼 필드에서 값 추출하기

폼 필드에서 값을 추출하고자 하는 필드의 이름을 알고 있다면, Documents.Form 컬렉션의 인덱서를 사용하여 이 데이터를 빠르게 검색할 수 있습니다. 이 기능을 사용하는 방법에 대한 샘플 코드는 이 글의 하단을 참조하세요.

## 제목으로 폼 필드 값 검색

폼 필드의 Value 속성을 사용하면 특정 필드의 값을 얻을 수 있습니다. 값을 얻으려면 Document 객체의 Form 컬렉션에서 폼 필드를 가져옵니다. 이 예제에서는 TextBoxField를 선택하고 Value 속성을 사용하여 그 값을 검색합니다.

## PDF 문서의 폼 필드를 JSON으로 추출

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
public static void ExtractFormFieldsToJson()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    var formData = document.Form.Cast<Field>().Select(f => new { Name = f.PartialName, f.Value });
    string jsonString = JsonSerializer.Serialize(formData);
    Console.WriteLine(jsonString);
}
```
## PDF 파일에서 XML로 데이터 추출

Form 클래스를 사용하여 PDF 파일에서 XML 파일로 데이터를 내보낼 수 있습니다. XML로 데이터를 내보내려면 Form 클래스의 객체를 생성하고 FileStream 객체를 사용하여 ExportXml 메서드를 호출해야 합니다. 마지막으로 FileStream 객체를 닫고 Form 객체를 폐기할 수 있습니다. 다음 코드 스니펫은 XML 파일로 데이터를 내보내는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET 를 참조하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

// 문서 열기
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "input.pdf");
// xml 파일 생성.
System.IO.FileStream xmlOutputStream = new FileStream( dataDir + "input.xml", FileMode.Create);
// 데이터 내보내기
form.ExportXml(xmlOutputStream);
// 파일 스트림 닫기
xmlOutputStream.Close();

// 문서 닫기
form.Dispose();
```
## PDF 파일에서 FDF로 데이터 내보내기

Form 클래스를 사용하여 PDF 파일에서 FDF 파일로 데이터를 내보낼 수 있습니다. FDF로 데이터를 내보내려면 Form 클래스의 객체를 생성하고 FileStream 객체를 사용하여 ExportFdf 메서드를 호출해야 합니다. 마지막으로 Form 클래스의 Save 메서드를 사용하여 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 FDF 파일로 데이터를 내보내는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// 문서 열기
form.BindPdf(dataDir + "input.pdf");

// fdf 파일 생성.
System.IO.FileStream fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create);

// 데이터 내보내기
form.ExportFdf(fdfOutputStream);

// 파일 스트림 닫기
fdfOutputStream.Close();

// 업데이트된 문서 저장
form.Save(dataDir + "ExportDataToPdf_out.pdf");
```
## PDF 파일에서 XFDF로 데이터 내보내기

Form 클래스를 사용하면 ExportXfdf 메소드를 사용하여 PDF 파일에서 XFDF 파일로 데이터를 내보낼 수 있습니다. XFDF로 데이터를 내보내려면 Form 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 ExportXfdf 메소드를 호출해야 합니다. 마지막으로 Form 클래스의 Save 메소드를 사용하여 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 XFDF 파일로 데이터를 내보내는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

```csharp
// 완성된 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET 에서 확인해주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// 문서 열기
form.BindPdf(dataDir + "input.pdf");

// xfdf 파일 생성.
System.IO.FileStream xfdfOutputStream = new FileStream("student1.xfdf", FileMode.Create);

// 데이터 내보내기
form.ExportXfdf(xfdfOutputStream);

// 파일 스트림 닫기
xfdfOutputStream.Close();

// 업데이트된 문서 저장하기
form.Save(dataDir + "ExportDataToXFDF_out.pdf");
```

