---
title: 데이터 가져오기 및 내보내기
type: docs
weight: 70
url: /net/import-and-export-data/
description: 이 섹션에서는 Form Class를 사용하여 Aspose.PDF Facades로 데이터 가져오기 및 내보내기를 설명합니다.
lastmod: "2024-06-05"
draft: false
---

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스는 [ImportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.form/importxml/methods/1) 메소드를 사용하여 XML 파일에서 PDF 파일로 데이터를 가져오는 것을 허용합니다. 데이터를 XML에서 가져오려면 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 객체를 생성한 다음, FileStream 객체를 사용하여 [ImportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importxml/index) 메서드를 호출해야 합니다. 마지막으로, [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 메서드를 사용하여 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 XML 파일에서 데이터를 가져오는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-ImportDataFromXML-ImportDataFromXML.cs" >}}

## PDF 파일에서 XML로 데이터 내보내기

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스는 [ExportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxml) 메서드를 사용하여 PDF 파일에서 XML 파일로 데이터를 내보낼 수 있도록 합니다. 데이터를 XML로 내보내려면 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 [ExportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxml) 메서드를 호출해야 합니다. 마지막으로 FileStream 객체를 닫고 Form 객체를 dispose할 수 있습니다. 다음 코드 스니펫은 데이터를 XML 파일로 내보내는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-ExportDataToXML-ExportDataToXML.cs" >}}

## PDF 파일에 FDF로부터 데이터 가져오기

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스는 [ImportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importfdf) 메서드를 사용하여 FDF 파일에서 PDF 파일로 데이터를 가져올 수 있도록 합니다. 데이터를 FDF에서 가져오기 위해서는 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 객체를 생성하고 FileStream 객체를 사용하여 [ImportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importfdf) 메서드를 호출해야 합니다. 마지막으로, [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 메서드를 사용하여 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 FDF 파일에서 데이터를 가져오는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-ImportDataFromPdf-ImportDataFromPdf.cs" >}}

## PDF 파일에서 FDF로 데이터 내보내기

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스는 [ExportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportfdf) 메서드를 사용하여 PDF 파일에서 FDF 파일로 데이터를 내보낼 수 있습니다. 데이터를 FDF로 내보내려면 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 [ExportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportfdf) 메서드를 호출해야 합니다. 마지막으로, [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 메서드를 사용하여 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 데이터를 FDF 파일로 내보내는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-ExportDataToPdf-ExportDataToPdf.cs" >}}

## XFDF에서 PDF 파일로 데이터 가져오기

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스는 [ImportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importxfdf) 메서드를 사용하여 XFDF 파일에서 PDF 파일로 데이터를 가져올 수 있도록 합니다. 데이터를 XFDF에서 가져오기 위해서는 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 [ImportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importxfdf) 메서드를 호출해야 합니다. 마지막으로, [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 메서드를 사용하여 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 XFDF 파일에서 데이터를 가져오는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-ImportDataFromXFDF-ImportDataFromXFDF.cs" >}}

## PDF 파일에서 XFDF로 데이터 내보내기

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스는 [ExportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxfdf) 메서드를 사용하여 PDF 파일에서 XFDF 파일로 데이터를 내보낼 수 있도록 합니다. 데이터를 XFDF로 내보내기 위해서는 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 객체를 생성한 후 FileStream 객체를 사용하여 [ExportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxfdf) 메서드를 호출해야 합니다. 마지막으로, [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 메서드를 사용하여 PDF 파일을 저장할 수 있습니다. 아래의 코드 스니펫은 데이터를 XFDF 파일로 내보내는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-ExportDataToXFDF-ExportDataToXFDF.cs" >}}

## 필드에서 JSON 파일로 값 내보내기

Aspose.Pdf.Facades는 양식 필드를 다루기 위한 대체 API를 제공합니다. 이 스니펫은 이 API를 사용하여 필드 값을 내보내고 가져오는 방법을 보여줍니다.

```cs
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// 문서 열기
form.BindPdf(_dataDir + "Sample-Form-01.pdf");

// XFDF 파일 생성
System.IO.FileStream jsonStream = new FileStream("Sample-Form-01.json", FileMode.Create);

// 데이터 내보내기
form.ExportJson(jsonStream);

// 파일 스트림 닫기
jsonStream.Close();

// 문서 닫기
form.Dispose();
```
## JSON 파일에서 필드로 값 가져오기

이 코드 스니펫은 Aspose.Pdf.Facades API를 사용하여 PDF 문서의 양식 필드에 JSON 파일에서 값을 가져오는 방법을 보여줍니다. FileStream은 JSON 파일을 처리하는 데 사용됩니다.

```cs

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// 문서 열기
form.BindPdf("Sample-Form-01.pdf");

// XFDF 파일 생성
System.IO.FileStream jsonStream = new FileStream("Sample-Form-01.json", FileMode.Open);

// 데이터 가져오기
form.ImportJson(jsonStream);

// 파일 스트림 닫기
jsonStream.Close();

// 문서 닫기
form.Dispose();
```