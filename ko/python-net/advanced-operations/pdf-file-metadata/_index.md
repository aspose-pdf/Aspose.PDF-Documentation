---
title: Python에서 PDF 파일 메타데이터 작업
linktitle: PDF 파일 메타데이터
type: docs
weight: 200
url: /ko/python-net/pdf-file-metadata/
description: Aspose.PDF를 사용하여 Python에서 저자와 제목과 같은 PDF 메타데이터를 추출하고 관리하는 방법을 살펴보세요.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 메타데이터 가져오기 및 설정하기
Abstract: 이 기사는 Aspose.PDF for Python via .NET을 사용하여 PDF 메타데이터를 조작하는 포괄적인 가이드를 제공합니다. 여기에서는 저자, 생성 날짜, 키워드 등 문서 카탈로그화, 검색 최적화 또는 검증에 필수적인 메타데이터 속성을 추출하고 설정하는 방법을 설명합니다. 코드 예제는 `Document` 클래스와 `info` 속성을 사용하여 PDF에서 메타데이터를 가져오고, `DocumentInfo` 객체를 사용해 새로운 메타데이터를 설정한 뒤 변경 사항을 저장하는 방법을 보여줍니다. 또한 문서 조직 및 검색성을 향상시키는 XMP 메타데이터를 프로그래밍 방식으로 업데이트하는 방법을 제시합니다. 이 기사에서는 네임스페이스 URI를 등록하여 사용자 정의 접두사가 붙은 메타데이터를 삽입하는 방법도 설명합니다. 이러한 기능은 애플리케이션 내에서 PDF 문서 정보를 효과적으로 관리하려는 개발자에게 필수적입니다.
---

## PDF 파일 정보 가져오기

이 코드 조각은 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에서 메타데이터를 추출하는 방법을 보여줍니다. Document 객체의 info 속성에 접근함으로써 저자, 생성 날짜, 키워드, 수정 날짜, 주제 및 제목과 같은 핵심 정보를 가져옵니다. 이 기능은 문서 카탈로그화, 검색 최적화 또는 문서 속성 검증이 필요한 애플리케이션에 필수적입니다.

1. Document 클래스를 사용하여 PDF 파일을 엽니다
1. info 속성을 통해 문서의 메타데이터를 가져옵니다
1. 메타데이터 정보를 표시합니다. 원하는 메타데이터 필드를 출력합니다

```python

    import aspose.pdf as ap

    def get_pdf_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "GetFileInfo.pdf")

        # Get document information
        doc_info = document.info

        # Display document information
        print(f"Author: {doc_info.author}")
        print(f"Creation Date: {doc_info.creation_date}")
        print(f"Keywords: {doc_info.keywords}")
        print(f"Modify Date: {doc_info.mod_date}")
        print(f"Subject: {doc_info.subject}")
        print(f"Title: {doc_info.title}")
```

## PDF 파일 정보 설정

Aspose.PDF for Python via .NET을 사용하면 PDF에 저자, 생성 날짜, 주제, 제목과 같은 파일별 정보를 설정할 수 있습니다. 이 정보를 설정하려면:

1. Document 클래스를 사용하여 PDF 파일을 엽니다.
1. [DocumentInfo]() 객체를 생성하고 원하는 메타데이터 속성을 설정합니다.
1. save 메서드를 사용하여 변경 사항을 새 PDF 파일에 저장합니다.

다음 코드 조각은 PDF 파일 정보를 설정하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap
    import datetime

    def set_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_workingdocuments()

        # Open PDF document
        document = ap.Document(data_dir + "SetFileInfo.pdf")

        # Specify document information
        doc_info = ap.DocumentInfo(document)
        doc_info.author = "Aspose"
        doc_info.creation_date = datetime.datetime.now()
        doc_info.keywords = "Aspose.Pdf, DOM, API"
        doc_info.mod_date = datetime.datetime.now()
        doc_info.subject = "PDF Information"
        doc_info.title = "Setting PDF Document Information"
        doc_info.producer = "Custom producer"
        doc_info.creator = "Custom creator"

        # Save PDF document
        document.save(data_dir + "SetFileInfo_out.pdf")
```

## PDF 파일에서 XMP 메타데이터 설정

이 코드 조각은 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에서 XMP 메타데이터를 프로그래밍 방식으로 설정하거나 업데이트하는 방법을 보여줍니다. xmp:CreateDate, xmp:Nickname 및 사용자 정의 필드와 같은 속성을 수정함으로써 표준화된 메타데이터를 PDF 파일에 삽입할 수 있습니다. 이 방법은 문서 조직을 향상하고 검색성을 용이하게 하며 필수 정보를 파일에 직접 삽입하는 데 특히 유용합니다.

Aspose.PDF를 사용하면 PDF 파일에 메타데이터를 설정할 수 있습니다. 메타데이터를 설정하려면:

1. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 PDF 파일을 엽니다.
1. 특정 키에 값을 할당하여 XMP 메타데이터를 수정합니다.
1. 업데이트된 PDF 문서를 저장합니다.

다음 코드 조각은 PDF 파일에 메타데이터를 설정하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap
    import datetime

    def set_xmp_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Set XMP metadata properties
        document.metadata["xmp:CreateDate"] = datetime.datetime.now().isoformat()
        document.metadata["xmp:Nickname"] = "Nickname"
        document.metadata["xmp:CustomProperty"] = "Custom Value"

        # Save the updated PDF document
        document.save(data_dir + "SetXMPMetadata_out.pdf")
```

## 접두사를 사용한 메타데이터 삽입

일부 개발자는 접두사가 있는 새로운 메타데이터 네임스페이스를 생성해야 합니다. 다음 코드 조각은 접두사를 사용하여 메타데이터를 삽입하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap
    import datetime

    def set_prefix_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Register a namespace URI for the 'xmp' prefix
        document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

        # Set the metadata property using the registered prefix
        document.metadata["xmp:ModifyDate"] = datetime.datetime.now().isoformat()  # ISO 8601 format

        # Save the updated PDF document
        document.save(data_dir + "SetPrefixMetadata_out.pdf")
```
