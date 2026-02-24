---
title: AcroForm 만들기 - 파이썬으로 채워지는 PDF 만들기
linktitle: AcroForm 만들기
type: docs
weight: 10
url: /ko/python-net/create-form/
description: Aspose.PDF for Python을 사용하면 PDF 파일에서 처음부터 폼을 생성할 수 있습니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 AcroForm을 만드는 방법
Abstract: 이 문서는 Aspose.PDF 파이썬 라이브러리를 사용하여 PDF 문서에 폼 필드를 생성하는 방법에 대한 안내를 제공합니다. 여기서는 폼 필드를 관리하기 위한 `Form` 컬렉션을 포함하는 `Document` 클래스를 소개합니다. 폼 필드를 추가하는 과정은 원하는 필드를 생성하고 `Form` 컬렉션의 `add` 메서드를 활용하는 것입니다. PDF 문서에 `TextBoxField`를 추가하는 예제가 제공됩니다. 예제에는 `TextBoxField`를 생성하고 위치, 이름, 값, 테두리 및 색상과 같은 속성을 설정한 뒤 문서에 추가하는 상세 코드가 포함됩니다. 수정된 PDF는 새로 추가된 폼 필드와 함께 저장됩니다.
---

## 처음부터 폼 만들기

### PDF 문서에 폼 필드 추가

[문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스는 PDF 문서에서 폼 필드를 관리하는 데 도움이 되는 [폼](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) 컬렉션을 제공합니다.

폼 필드를 추가하려면:

1. 추가하려는 폼 필드를 생성합니다.
1. Form 컬렉션의 [추가](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) 메서드를 호출합니다.

### TextBoxField 추가

아래 예제는 [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/)를 추가하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Open document
    pdfDocument = ap.Document(path_infile)

    # Create a field
    textBoxField = ap.forms.TextBoxField(pdfDocument.pages[1], ap.Rectangle(100, 200, 300, 300, True))
    textBoxField.partial_name = "textbox1"
    textBoxField.value = "Text Box"

    border = ap.annotations.Border(textBoxField)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    textBoxField.border = border

    textBoxField.color = ap.Color.green

    # Add field to the document
    pdfDocument.form.add(textBoxField, 1)

    # Save modified PDF
    pdfDocument.save(path_outfile)
```


