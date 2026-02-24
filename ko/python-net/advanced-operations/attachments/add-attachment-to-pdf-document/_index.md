---
title: Python을 사용하여 PDF 문서에 첨부 파일 추가
linktitle: PDF 문서에 첨부 파일 추가
type: docs
weight: 10
url: /ko/python-net/add-attachment-to-pdf-document/
description: 이 페이지에서는 Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 파일에 첨부 파일을 추가하는 방법을 설명합니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF에 첨부 파일을 추가하는 방법
Abstract: 이 기사에서는 Python과 Aspose.PDF 라이브러리를 사용하여 PDF 파일에 첨부 파일을 추가하는 단계별 가이드를 제공합니다. 새로운 Python 프로젝트 설정, 필요한 Aspose.PDF 패키지 가져오기, `Document` 객체 생성 과정을 자세히 설명합니다. 원하는 파일과 설명을 포함한 `FileSpecification` 객체를 만드는 방법과 `add` 메서드를 사용하여 이 객체를 PDF 문서의 `EmbeddedFileCollection`에 추가하는 방법을 설명합니다. `EmbeddedFileCollection`은 PDF 내 모든 첨부 파일을 보관합니다. 문서를 열고, 첨부할 파일을 설정하고, 문서의 첨부 컬렉션에 추가한 뒤 업데이트된 PDF를 저장하는 과정을 보여주는 코드 스니펫이 포함되어 있습니다.
---

첨부 파일은 다양한 정보를 포함할 수 있으며 다양한 파일 유형일 수 있습니다. 이 기사에서는 PDF 파일에 첨부 파일을 추가하는 방법을 설명합니다.

1. 새로운 Python 프로젝트를 생성합니다.
1. Aspose.PDF 패키지를 가져옵니다.
1. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체를 생성합니다.
1. 추가하려는 파일과 파일 설명을 포함한 [파일 사양](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 객체를 생성합니다.
1. [파일 사양](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 객체를 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 [임베디드 파일 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 컬렉션에 컬렉션의 [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) 메서드로 추가합니다.

PDF 파일에 포함된 모든 첨부 파일은 [임베디드 파일 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/)에 저장됩니다. 다음 코드 스니펫은 PDF 문서에 첨부 파일을 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Setup new file to be added as attachment
    fileSpecification = ap.FileSpecification(attachment_file, "Sample text file")

    # Add attachment to document's attachment collection
    document.embedded_files.append(fileSpecification)

    # Save new output
    document.save(output_pdf)
```


