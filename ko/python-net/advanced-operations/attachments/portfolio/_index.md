---
title: 파이썬으로 PDF 포트폴리오 만들기
linktitle: 포트폴리오
type: docs
weight: 20
url: /ko/python-net/portfolio/
description: .NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 파이썬에서 PDF 포트폴리오를 만들고 관리하는 방법을 알아보세요.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에 포함된 파일로 PDF 포트폴리오 작성 및 편집
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 포트폴리오를 만들고 관리하는 방법을 설명합니다.Python을 사용하여 프로그래밍 방식으로 여러 파일 유형을 단일 PDF 포트폴리오로 묶고, 문서 컬렉션에 파일을 추가하고, 포트폴리오 항목을 제거하는 방법을 알아봅니다.
---

PDF 포트폴리오를 만들면 여러 유형의 파일을 하나의 일관된 문서로 통합하고 보관할 수 있습니다.이러한 문서에는 텍스트 파일, 이미지, 스프레드시트, 프레젠테이션 및 기타 자료가 포함될 수 있으며 모든 관련 자료를 한 곳에 저장하고 구성할 수 있습니다.

PDF 포트폴리오를 사용하면 어디에서나 프레젠테이션을 고품질로 표시할 수 있습니다.일반적으로 PDF 포트폴리오를 만드는 것은 매우 최신의 현대적인 작업입니다.

각 파일을 하나의 PDF 컨테이너 내에 원본 형식으로 유지하면서 관련 파일 컬렉션을 함께 배포하려는 경우 PDF 포트폴리오를 사용하십시오.

## PDF 포트폴리오 작성 방법

.NET을 통한 파이썬용 Aspose.PDF 파일을 사용하면 다음을 사용하여 PDF 포트폴리오 문서를 만들 수 있습니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.와 함께 파일을 가져온 후 문서.collection 객체에 파일을 추가합니다. [파일 사양](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 수업.파일이 추가되면 'Document' 클래스를 사용하세요. [저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 포트폴리오 문서를 저장하는 방법.

다음 예제에서는 Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 만듭니다.

아래 코드는 다음과 같은 포트폴리오를 생성합니다.

### 파이썬용 Aspose.PDF 파일로 만든 PDF 포트폴리오

![파이썬용 Aspose.PDF 파일로 만든 PDF 포트폴리오](working-with-pdf-portfolio_1.jpg)

```python
import aspose.pdf as ap

def create_pdf_portfolio(input_files, outfile):
    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_files[0])
    word = ap.FileSpecification(input_files[1])
    image = ap.FileSpecification(input_files[2])

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(outfile)
```

## PDF 포트폴리오에서 파일 제거

PDF 포트폴리오에서 파일을 삭제/제거하려면 다음 코드 줄을 사용해 보십시오.

```python
import aspose.pdf as ap

def remove_files_from_pdf_portfolio(infile, outfile):
    # Open document
    document = ap.Document(infile)
    document.collection.delete()

    # Save updated file
    document.save(outfile)
```

## 관련 첨부 주제

- [파이썬에서 PDF 첨부 파일 작업하기](/pdf/ko/python-net/attachments/)
- [파이썬에서 PDF에 첨부 파일 추가](/pdf/ko/python-net/add-attachment-to-pdf-document/)
- [파이썬에서 PDF에서 첨부 파일 제거](/pdf/ko/python-net/removing-attachment-from-an-existing-pdf/)

