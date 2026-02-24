---
title: Python을 사용한 연산자 작업
linktitle: 연산자 작업
type: docs
weight: 90
url: /ko/python-net/working-with-operators/
description: 이 주제에서는 .NET을 통한 Python용 Aspose.PDF에서 연산자를 사용하는 방법을 설명합니다. 연산자 클래스는 PDF 조작에 대한 뛰어난 기능을 제공합니다.
lastmod: "2025-05-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: .NET을 사용한 Python용 Aspose.PDF에서 PDF 연산자 사용
Abstract: 이 문서는 PDF 연산자와 PDF 콘텐츠 스트림을 조작하는 데 있어 그 적용에 대한 심층적인 탐구를 제공합니다. 연산자는 페이지에 그래픽 요소를 렌더링하는 등 특정 작업을 지시하는 PDF의 특수 키워드이며, 콘텐츠 스트림 내에서만 유효합니다. 이 문서에서는 저수준 그래픽 연산자를 사용해 콘텐츠 스트림을 직접 조작함으로써 PDF 내 이미지 배치를 정밀하게 제어하는 방법을 자세히 설명합니다. 이 접근법은 워터마크 추가, 오버레이 정렬, 맞춤 레이아웃 생성 등 정확한 이미지 위치 지정이 필요한 작업에 유용합니다. GSave, ConcatenateMatrix, Do, GRestore와 같은 특정 연산자는 그래픽 상태와 변환을 관리하는 역할을 강조하며, 다른 페이지 내용에 영향을 주지 않고 정확한 렌더링을 보장합니다.
---

## PDF 연산자 및 사용법 소개

연산자는 페이지에 그래픽 형태를 그리는 등 수행되어야 할 작업을 지정하는 PDF 키워드입니다. 연산자 키워드는 초기 슬래시 문자(2Fh)가 없다는 점에서 명명된 객체와 구분됩니다. 연산자는 콘텐츠 스트림 내부에서만 의미가 있습니다.

콘텐츠 스트림은 페이지에 그려질 그래픽 요소를 설명하는 명령으로 구성된 데이터가 있는 PDF 스트림 객체입니다. PDF 연산자에 대한 자세한 내용은 [PDF 사양](https://opensource.adobe.com/dc-acrobat-sdk-docs/)을 참조하십시오.

### 구현 세부 사항

이 방법은 저수준 그래픽 연산자를 사용해 콘텐츠 스트림을 직접 조작함으로써 PDF 내 이미지 배치를 세밀하게 제어합니다. 이미지의 정밀한 위치 지정 및 변환이 필요한 경우에 특히 유용합니다, 예를 들어:

- 특정 위치에 워터마크 또는 로고 추가.

- 기존 콘텐츠 위에 이미지를 정확히 정렬하여 오버레이.

- 고수준 추상화로는 구현할 수 없는 맞춤 레이아웃 구현.

개발자는 GSave, ConcatenateMatrix, Do, GRestore와 같은 연산자를 사용함으로써 이미지가 정확하게 렌더링되고 다른 페이지 콘텐츠에 의도치 않은 부작용을 일으키지 않도록 할 수 있습니다.

- [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) 연산자는 PDF의 현재 그래픽 상태를 저장합니다.
- [ConcatenateMatrix](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) (행렬 연결) 연산자는 이미지가 PDF 페이지에 어떻게 배치되어야 하는지를 정의하는 데 사용됩니다.
- [Do](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) 연산자는 페이지에 이미지를 그립니다.
- [GRestore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) 연산자는 그래픽 상태를 복원합니다.

PDF 파일에 이미지를 추가하려면:

1. PDF 문서 열기
1. 이미지 배치 좌표 정의
1. 대상 페이지 접근
1. 이미지를 스트림으로 로드
1. 현재 그래픽 상태 저장
1. 사각형 및 변환 행렬 생성
1. 변환 행렬 적용
1. 이미지 그리기
1. 이전 그래픽 상태 복원
1. 수정된 PDF 문서 저장

다음 코드 스니펫은 PDF 연산자를 사용하는 방법을 보여줍니다:

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Set coordinates for the image placement
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        # Get the page where the image needs to be added
        page = document.pages[1]

        # Load the image into a file stream
        with open(path_imagefile, "rb") as image_stream:
            # Add the image to the page's Resources collection
            page.resources.images.add(image_stream)

        # Save the current graphics state using the GSave operator
        page.contents.add(ap.operators.GSave())

        # Create a rectangle and matrix for positioning the image
        rectangle = ap.Rectangle(lower_left_x, lower_left_y, upper_right_x, upper_right_y)
        matrix = ap.Matrix([
            rectangle.urx - rectangle.llx, 0,
            0, rectangle.ury - rectangle.lly,
            rectangle.llx, rectangle.lly
        ])

        # Define how the image must be placed using the ConcatenateMatrix operator
        page.contents.add(ap.operators.ConcatenateMatrix(matrix))

        # Get the image from the Resources collection
        x_image = page.resources.images[page.resources.images.count]

        # Draw the image using the Do operator
        page.contents.add(ap.operators.Do(x_image.name))

        # Restore the graphics state using the GRestore operator
        page.contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## 연산자를 사용하여 페이지에 XForm 그리기

이 예제는 XForm과 그래픽 연산자의 강점을 활용하여 PDF 내 그래픽 콘텐츠를 효율적으로 재사용합니다. 이미지를 XForm에 캡슐화함으로써 이미지 데이터를 복제하지 않고도 여러 번 그릴 수 있어 파일 크기가 작아지고 성능이 향상됩니다. 이 접근법은 특히 다음과 같은 경우에 유용합니다:

- 동일한 이미지나 그래픽이 문서에 여러 번 나타나야 할 때.

- 그래픽의 배치와 변환에 대한 정밀한 제어가 필요할 때.

- PDF의 성능 및 크기 최적화가 우선일 때.

GSave와 GRestore로 그래픽 상태를 관리하고, ConcatenateMatrix를 사용해 변환 행렬을 적용함으로써, 이 기술은 각각의 그래픽이 올바르게 독립적으로 렌더링되도록 보장합니다.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        page_contents = document.pages[1].contents

        # Wrap existing contents with GSave/GRestore operators to preserve graphics state
        page_contents.insert(1, ap.operators.GSave())
        page_contents.add(ap.operators.GRestore())

        # Add GSave operator to start new graphics state
        page_contents.add(ap.operators.GSave())

        # Create an XForm
        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.add(form)

        form.contents.add(ap.operators.GSave())
        # Define image width and height
        form.contents.add(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        # Load image into stream
        with open(path_imagefile, 'rb') as image_stream:
            # Add the image to the XForm's resources
            form.resources.images.add(image_stream)

        x_image = form.resources.images[form.resources.images.count]
        # Draw the image on the XForm
        form.contents.add(ap.operators.Do(x_image.name))
        form.contents.add(ap.operators.GRestore())

        # Place and draw the XForm at two different coordinates

        # Draw the XForm at (100, 500)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Draw the XForm at (100, 300)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Restore graphics state
        page_contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## 연산자 클래스를 사용하여 그래픽 객체 제거

다음 코드 스니펫은 그래픽을 제거하는 방법을 보여줍니다. PDF 파일에 그래픽에 대한 텍스트 레이블이 포함되어 있는 경우, 이 접근법을 사용하면 해당 레이블이 PDF 파일에 남을 수 있습니다. 따라서 이러한 이미지를 삭제하기 위한 대체 방법으로 그래픽 연산자를 검색하십시오.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Get the specific page (page 2 in this case)
        page = document.pages[2]

        # Get the operator collection from the page contents
        operator_collection = page.contents

        # Define the path-painting operators to be removed
        operators_to_remove = [
            ap.operators.Stroke(),
            ap.operators.ClosePathStroke(),
            ap.operators.Fill()
        ]

        # Delete the specified operators from the page contents
        operator_collection.delete(operators_to_remove)

        # Save PDF document
        document.save(path_outfile)
```


