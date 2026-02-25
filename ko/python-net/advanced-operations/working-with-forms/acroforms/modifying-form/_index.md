---
title: AcroForm 수정
linktitle: AcroForm 수정
type: docs
weight: 45
url: /ko/python-net/modifying-form/
description: Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 파일의 양식을 수정합니다. 기존 양식에 필드를 추가하거나 제거하고, 필드 제한을 조회 및 설정할 수 있습니다 등.
lastmod: "2025-02-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 양식 필드 관리 및 사용자 지정
Abstract: 이 예제 컬렉션은 Aspose.PDF for Python via .NET을 사용하여 PDF 양식 필드를 관리하고 사용자 지정하는 다양한 기술을 보여줍니다. 여기에는 TextFragmentAbsorber를 사용하여 타자기 스타일 양식 필드의 텍스트를 지우는 방법, FormEditor를 사용하여 문자 제한을 설정하고 조회하는 방법, 텍스트 박스 필드에 사용자 지정 글꼴과 스타일을 적용하는 방법, 그리고 이름으로 특정 양식 필드를 제거하는 방법이 포함됩니다. 이러한 작업을 통해 개발자는 PDF 양식을 재배포, 브랜딩 또는 데이터 검증 목적에 맞게 정리·포맷·맞춤화할 수 있어 자동화된 문서 워크플로우에서 미적 및 기능적 정교함을 지원합니다.
---

## 양식의 텍스트 지우기

이 예제는 Aspose.PDF for Python via .NET을 사용하여 PDF의 타자기 양식 필드에서 텍스트를 지우는 방법을 보여줍니다. PDF의 첫 페이지를 스캔하여 타자기 양식을 식별하고, 해당 내용을 제거한 후 업데이트된 문서를 저장합니다. 이 방법은 PDF를 재배포하기 전에 양식 필드를 초기화하거나 정리하는 데 유용합니다.

1. 입력 PDF 문서를 로드합니다.
1. 첫 페이지의 양식에 접근합니다.
1. 각 양식을 반복하면서 `Typewriter` 양식인지 확인합니다.
1. TextFragmentAbsorber를 사용하여 양식 내 텍스트 조각을 찾습니다.
1. 각 조각의 텍스트를 삭제합니다.
1. 수정된 PDF를 출력 파일에 저장합니다.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    dataDir = "path/to/your/data/dir/"
    path_infile = dataDir + infile
    path_outfile = dataDir + outfile
    document = ap.Document(path_infile)

    # Get the forms from the first page
    forms = document.pages[1].resources.forms

    for form in forms:
        # Check if the form is of type "Typewriter" and subtype "Form"
        if (form.it == "Typewriter" and form.subtype == "Form"):
            # Create a TextFragmentAbsorber to find text fragments
            absorber = ap.Text.TextFragmentAbsorber()
            absorber.visit(form)

            # Clear the text in each fragment
            for fragment in absorber.text_fragments:
                fragment.Text = ""

    # Save PDF document
    document.save(path_outfile)
```

## 필드 제한 가져오기 또는 설정하기

FormEditor 클래스의 set_field_limit(field, limit) 메서드를 사용하면 필드 제한, 즉 필드에 입력할 수 있는 최대 문자 수를 설정할 수 있습니다.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Create FormEditor instance
    form = ap.facades.FormEditor()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Set field limit for "First Name"
    form.set_field_limit("First Name", 15)

    # Save PDF document
    form.save(path_outfile)
```

마찬가지로, Aspose.PDF에는 필드 제한을 가져오는 메서드가 있습니다.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {textBoxField.max_len}")
```

## 양식 필드에 사용자 지정 글꼴 설정하기

Adobe PDF 파일의 양식 필드는 특정 기본 글꼴을 사용하도록 설정할 수 있습니다. 초기 Aspose.PDF 버전에서는 14개의 기본 글꼴만 지원되었습니다. 이후 릴리스에서는 개발자가 모든 글꼴을 적용할 수 있게 되었습니다.

이 코드는 사용자 지정 글꼴, 크기 및 색상을 설정하여 PDF 양식의 텍스트 박스 필드 외관을 업데이트하고, Aspose.PDF for Python via .NET을 사용하여 수정된 문서를 저장합니다.

다음 코드 스니펫은 PDF 양식 필드의 기본 글꼴을 설정하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        textBoxField.default_appearance = ap.annotations.DefaultAppearance(font, 10, ap.Color.black.to_rgb())

    document.save(path_outfile)
```

## 기존 양식에서 필드 제거하기

이 코드는 PDF 문서에서 특정 양식 필드(이름으로)를 제거하고 Aspose.PDF for Python via .NET을 사용하여 업데이트된 파일을 저장합니다.

1. PDF 문서를 로드합니다.
1. 이름으로 양식 필드를 삭제합니다.
1. 업데이트된 PDF를 저장합니다.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    # Delete a particular field by name
    document.form.delete("First Name")
    # Save PDF document
    document.save(path_outfile)
```

