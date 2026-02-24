---
title: Python을 사용한 PDF 포트폴리오 작업
linktitle: 포트폴리오
type: docs
weight: 20
url: /ko/python-net/portfolio/
description: Python으로 PDF 포트폴리오를 만드는 방법. PDF 포트폴리오를 만들기 위해 Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용해야 합니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF 포트폴리오 작업하는 방법
Abstract: 이 문서는 Aspose.PDF for Python via .NET을 사용한 PDF 포트폴리오의 생성 및 관리에 대해 다룹니다. PDF 포트폴리오는 텍스트 파일, 이미지, 스프레드시트, 프레젠테이션과 같은 다양한 파일 유형을 단일한 정리된 문서로 통합하여 모든 관련 자료를 한곳에 보관할 수 있도록 합니다. 이 문서는 `Document` 클래스와 `FileSpecification` 클래스를 사용하여 파일을 문서 컬렉션에 추가하는 방법을 강조하면서 PDF 포트폴리오를 만드는 과정을 설명합니다. 예제로 Microsoft Excel 파일, Word 문서 및 이미지 파일을 PDF 포트폴리오에 포함시키는 방법을 보여줍니다. 또한, 포트폴리오를 생성하고 파일을 제거하는 코드 스니펫을 포함하여 Aspose.PDF for Python으로 PDF 포트폴리오를 관리하는 간편함과 효율성을 강조합니다.
---

PDF 포트폴리오를 생성하면 다양한 유형의 파일을 하나의 일관된 문서로 통합하고 보관할 수 있습니다. 이 문서에는 텍스트 파일, 이미지, 스프레드시트, 프레젠테이션 및 기타 자료가 포함될 수 있으며, 모든 관련 자료가 한 곳에 저장되고 정리됩니다.

PDF 포트폴리오는 어디서든 고품질로 프레젠테이션을 보여줄 수 있도록 도와줍니다. 일반적으로 PDF 포트폴리오를 만드는 것은 매우 최신적이고 현대적인 작업입니다.

## PDF 포트폴리오 만드는 방법

Aspose.PDF for Python via .NET은 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용하여 PDF 포트폴리오 문서를 만들 수 있게 합니다. [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 클래스로 파일을 가져온 후 document.collection 객체에 파일을 추가합니다. 파일을 추가한 후에는 Document 클래스의 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용해 포트폴리오 문서를 저장합니다.

다음 예제는 Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 생성합니다.

아래 코드는 다음과 같은 포트폴리오를 생성합니다.

### Aspose.PDF for Python으로 만든 PDF 포트폴리오

![Aspose.PDF for Python으로 만든 PDF 포트폴리오](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(output_pdf)
```

## PDF 포트폴리오에서 파일 제거

PDF 포트폴리오에서 파일을 삭제/제거하려면 다음 코드 라인을 사용해 보세요.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Save updated file
    document.save(output_pdf)
```


