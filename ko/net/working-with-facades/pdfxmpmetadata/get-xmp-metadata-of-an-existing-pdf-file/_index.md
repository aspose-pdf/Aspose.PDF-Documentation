---
title: PDF 파일의 XMP 메타데이터 가져오기
type: docs
weight: 30
url: /ko/net/get-xmp-metadata-of-an-existing-pdf-file/
description: 이 섹션은 Aspose.PDF Facades를 사용하여 기존 PDF의 XMP 메타데이터를 가져오는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

PDF 파일에서 XMP 메타데이터를 가져오기 위해서는 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 PDF 파일을 바인딩해야 합니다. 특정 XMP 메타데이터 속성을 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 객체에 전달하여 해당 값을 얻을 수 있습니다. 다음 코드 스니펫은 PDF 파일에서 XMP 메타데이터를 가져오는 방법을 보여줍니다.

```csharp
// 전체 예제 및 데이터 파일은 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET를 참조하세요.
// 문서 디렉토리의 경로
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// PdfXmpMetadata 객체 생성
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// 객체에 PDF 파일 바인딩
xmpMetaData.BindPdf( dataDir + "input.pdf");

// XMP 메타데이터 속성 가져오기
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreateDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.MetadataDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreatorTool].ToString());
Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

Console.ReadLine();
```