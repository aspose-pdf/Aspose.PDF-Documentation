---
title: Python을 사용하여 PDF에 이미지 추가
linktitle: 이미지 추가
type: docs
weight: 10
url: /ko/python-net/add-image-to-existing-pdf-file/
description: 이 섹션에서는 Python 라이브러리를 사용하여 기존 PDF 파일에 이미지를 추가하는 방법을 설명합니다.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 이미지를 추가하는 방법
Abstract: 이 문서는 Aspose.PDF 라이브러리를 사용하여 Python으로 기존 PDF 파일에 이미지를 추가하는 방법에 대한 안내를 제공합니다. 이를 달성하기 위한 두 가지 방법이 제시됩니다. 첫 번째 방법은 Aspose.PDF의 `Document` 클래스를 사용하여 PDF를 로드하고 페이지 번호를 지정한 뒤 `Page` 클래스의 `add_image` 메서드로 이미지를 배치하는 것입니다. 그런 다음 `save()` 메서드로 문서를 저장합니다. 두 번째 방법은 Aspose.PDF.Facades 네임스페이스의 `PdfFileMend` 클래스를 활용하는 것으로, 보다 간단한 인터페이스를 제공합니다. 여기서는 `add_image()` 메서드를 호출하여 지정된 페이지와 좌표에 이미지를 추가하고, 업데이트된 PDF를 저장한 뒤 `PdfFileMend` 객체를 닫습니다. 두 방법 모두 과정을 보여주는 코드 스니펫이 제공됩니다.
---

## 기존 PDF 파일에 이미지 추가

이 예제는 Aspose.PDF for Python via .NET을 사용하여 PDF 페이지의 특정 위치에 이미지를 삽입하는 방법을 보여줍니다.

1. 'ap.Document'로 PDF 문서를 로드합니다.
1. 대상 페이지 '(document.pages[1]'을(를) 선택합니다 - 첫 페이지.
1. 'page.add_image()'를 사용하여 이미지를 배치합니다:
- 이미지 파일 경로.
- 이미지 좌표를 정의하는 'Rectangle' 객체 (left=20, bottom=730, right=120, top=830).
1. 업데이트된 PDF를 저장합니다.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    page = document.pages[1]
    page.add_image(
        path.join(self.data_dir, image_file),
        ap.Rectangle(20, 730, 120, 830, True),
    )
    document.save(path_outfile)
```

## 연산자를 사용하여 이미지 추가

다음 코드 스니펫은 고수준 헬퍼 메서드 대신 PDF 연산자를 직접 다루어 PDF 페이지에 이미지를 추가하는 저수준 접근 방식을 보여줍니다.

단계:

1. 새 빈 'Document'를 생성합니다.
1. 페이지를 추가하고 크기를 설정합니다 (842 × 595 - 가로 A4).
1. 페이지의 이미지 리소스(page.resources.images)에 접근합니다.
1. 이미지 파일을 스트림에 로드하고 리소스에 추가합니다.
- 메서드는 'image_id'를 반환합니다.
- 새로 추가된 이미지 객체가 리소스에서 검색됩니다.
1. 이미지의 종횡비를 유지하는 사각형을 정의합니다:
1. 연산자 시퀀스를 구축합니다:
- 'GSave()' - 현재 그래픽 상태를 저장합니다.
- 'ConcatenateMatrix(matrix)' - 변환을 적용합니다(이미지를 페이지에 수직으로 스케일링하고 중앙에 배치).
- 'Do(image_id)' - 이미지를 렌더링합니다.
- 'GRestore()' - 그래픽 상태를 복원합니다.
1. 'page.contents'에 연산자 시퀀스를 추가합니다.
1. 결과 PDF를 저장합니다.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(path.join(self.data_dir, path_infile), "rb")
    image_id = resources_images.add(image_stream)

    x_image = list(resources_images)[-1]

    rectangle = ap.Rectangle(
        0,
        0,
        page.media_box.width,
        (page.media_box.width * x_image.height) / x_image.width,
        True,
    )

    # Create operator sequence for adding image
    operators = []

    # Save graphics state
    operators.append(ap.operators.GSave())

    # Set transformation matrix (position and size)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.llx + (page.media_box.height - rectangle.height) / 2,
    )
    operators.append(ap.operators.ConcatenateMatrix(matrix))

    # Draw the image
    operators.append(ap.operators.Do(image_id))

    # Restore graphics state
    operators.append(ap.operators.GRestore())

    # Add operators to page contents
    page.contents.add(operators)

    document.save(path_outfile)
```

## 대체 텍스트와 함께 이미지 추가

이 예제는 PDF 페이지에 이미지를 추가하고 접근성 준수(예: PDF/UA)를 위해 대체 텍스트(alt text)를 할당하는 방법을 보여줍니다.

1. 새 'Document'를 만들고 페이지를 추가합니다 (842 × 595, 가로 A4).
1. 전체 페이지를 차지하는 사각형을 사용하여 'page.add_image()'로 페이지에 이미지를 배치합니다.
1. 페이지의 이미지 리소스('page.resources.images')에 접근합니다.
1. 대체 텍스트 문자열을 정의합니다(예: 'Alternative text for image').
1. 리소스에서 첫 번째 이미지 객체를 검색합니다('x_image = resources_images[1]').
1. 'try_set_alternative_text(alt_text, page)'를 사용하여 이미지에 대체 텍스트를 할당합니다.
1. 결과 PDF를 저장합니다.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    page.add_image(
        path_image_file,
        ap.Rectangle(0, 0, 842, 595, True),
    )

    resources_images = page.resources.images
    alt_text = "Alternative text for image"
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text(alt_text, page)

    # If set is successful, then get the alternative text for the image
    if (result):
        print ("Text has been added successfuly")
    document.save(path_outfile)
```
