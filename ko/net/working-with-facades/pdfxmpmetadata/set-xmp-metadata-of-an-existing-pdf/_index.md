---
title: 기존 PDF의 XMP 메타데이터 설정
type: docs
weight: 20
url: /ko/net/set-xmp-metadata-of-an-existing-pdf/
description: 이 섹션에서는 Aspose.PDF Facades로 기존 PDF의 XMP 메타데이터를 설정하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

PDF 파일에 XMP 메타데이터를 설정하려면 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 PDF 파일을 바인딩해야 합니다. 당신은 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 클래스의 [Add](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index) 메서드를 사용하여 다양한 속성을 추가할 수 있습니다. 마지막으로, [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 메서드를 호출합니다. 다음 코드 조각은 PDF 파일에 XMP 메타데이터를 추가하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET를 참조하세요.
// 문서 디렉터리의 경로.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// PdfXmpMetadata 객체 생성
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// 객체에 PDF 파일 바인딩
xmpMetaData.BindPdf(dataDir+ "SetXMPMetadata.pdf");

// 생성 날짜 추가
xmpMetaData.Add(DefaultMetadataProperties.CreateDate, System.DateTime.Now.ToString());

// 메타데이터 날짜 변경
xmpMetaData[DefaultMetadataProperties.MetadataDate] = System.DateTime.Now.ToString();

// 생성 도구 추가
xmpMetaData.Add(DefaultMetadataProperties.CreatorTool, "Creator tool name");

// 수정 날짜 제거
xmpMetaData.Remove(DefaultMetadataProperties.ModifyDate);

// 사용자 정의 속성 추가
// 단계 #1: 네임스페이스 접두사와 URI 등록
xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");
// 단계 #2: 접두사와 함께 사용자 속성 추가
xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

// 사용자 정의 속성 변경
xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

// PDF 파일에 XMP 메타데이터 저장
xmpMetaData.Save(dataDir+ "SetXMPMetadata_out.pdf");

// 객체 닫기
xmpMetaData.Close();
```