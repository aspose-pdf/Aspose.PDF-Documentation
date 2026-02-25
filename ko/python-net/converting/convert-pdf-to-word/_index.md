---
title: Python을 사용하여 PDF를 Microsoft Word 문서로 변환
linktitle: PDF를 Word로 변환
type: docs
weight: 10
url: /ko/python-net/convert-pdf-to-word/
lastmod: "2025-09-27"
description: Aspose.PDF를 사용하여 Python에서 PDF 문서를 Word 형식으로 변환하는 방법을 배우고, 손쉬운 문서 편집을 할 수 있습니다.
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF를 Word로 변환하는 방법
Abstract: 이 문서는 Python을 사용하여 Aspose.PDF 라이브러리를 활용해 PDF 파일을 Microsoft Word 형식(DOC 및 DOCX)으로 변환하는 포괄적인 가이드를 제공합니다. PDF를 편집 가능한 Word 문서로 변환함으로써 텍스트, 표, 이미지와 같은 콘텐츠를 보다 쉽게 조작할 수 있는 장점을 설명합니다. 이 문서는 PDF를 DOC(Word 97-2003 형식) 및 DOCX로 변환하는 과정을 상세히 다루며, Python 코드를 통해 이러한 변환을 시연하는 코드 스니펫을 포함합니다. 변환 과정은 PDF에서 `Document` 객체를 생성하고 `save()` 메서드와 `SaveFormat` 열거형을 사용하여 원하는 형식으로 저장하는 것을 포함합니다. 또한, 변환 프로세스를 추가로 맞춤 설정할 수 있는 `DocSaveOptions` 클래스를 소개하며, 인식 모드 지정과 같은 옵션을 사용할 수 있습니다. 이 문서는 Aspose.PDF에서 제공하는 온라인 애플리케이션을 통해 변환 품질 및 기능을 테스트할 수 있음을 강조합니다. 내용에는 구조화된 개요와 각 형식에 대한 해당 섹션 링크가 포함됩니다.
---

## PDF를 DOC로 변환

가장 인기 있는 기능 중 하나는 PDF를 Microsoft Word DOC로 변환하는 것으로, 콘텐츠 관리를 더 쉽게 해줍니다. **Aspose.PDF for Python via .NET**를 사용하면 PDF 파일을 DOC뿐만 아니라 DOCX 형식으로도 쉽고 효율적으로 변환할 수 있습니다.

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 클래스는 PDF 파일을 DOC 형식으로 변환하는 과정을 개선하는 다양한 속성을 제공합니다. 이러한 속성 중 Mode는 PDF 콘텐츠에 대한 인식 모드를 지정할 수 있게 합니다. 이 속성에는 RecognitionMode 열거형의 모든 값을 지정할 수 있습니다. 각 값은 특정한 장점과 제한을 가지고 있습니다:

단계: Python에서 PDF를 DOC로 변환

1. PDF를 'ap.Document' 객체에 로드합니다.
1. 'DocSaveOptions' 인스턴스를 생성합니다.
1. 출력이 .doc 형식(구버전 Word 형식)으로 저장되도록 format 속성을 'DocFormat.DOC'로 설정합니다.
1. 지정된 저장 옵션을 사용하여 PDF를 Word 문서로 저장합니다.
1. 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**PDF를 DOC로 온라인 변환해 보세요**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)를 제공하며, 이를 통해 기능과 품질을 시험해 볼 수 있습니다.

[![PDF를 DOC로 변환](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDF를 DOCX로 변환

Aspose.PDF for Python API를 사용하면 Python via .NET으로 PDF 문서를 DOCX로 읽고 변환할 수 있습니다. DOCX는 Microsoft Word 문서에 널리 사용되는 형식으로, 구조가 기존의 순수 바이너리에서 XML과 바이너리 파일의 조합으로 변경되었습니다. DOCX 파일은 Word 2007 및 이후 버전에서 열 수 있지만, DOC 파일 확장자를 지원하는 이전 버전의 MS Word에서는 열 수 없습니다.

다음 Python 코드 스니펫은 PDF 파일을 DOCX 형식으로 변환하는 과정을 보여줍니다.

단계: Python에서 PDF를 DOCX로 변환

1. 'ap.Document'를 사용하여 원본 PDF를 로드합니다.
1. 'DocSaveOptions' 인스턴스를 생성합니다.
1. .docx 파일(현대 Word 형식)을 생성하도록 format 속성을 'DocFormat.DOC_X'로 설정합니다.
1. 구성된 저장 옵션을 사용하여 PDF를 DOCX 파일로 저장합니다.
1. 변환 후 확인 메시지를 출력합니다.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC_X
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 클래스에는 Format이라는 속성이 있어 결과 문서의 형식(DOC 또는 DOCX)을 지정할 수 있습니다. PDF 파일을 DOCX 형식으로 변환하려면 DocSaveOptions.DocFormat 열거형에서 Docx 값을 전달하세요.

{{% alert color="warning" %}}
**PDF를 DOCX로 온라인 변환해 보세요**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)를 제공하며, 이를 통해 기능과 품질을 시험해 볼 수 있습니다.

[![Aspose.PDF PDF를 Word로 변환하는 무료 앱](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

