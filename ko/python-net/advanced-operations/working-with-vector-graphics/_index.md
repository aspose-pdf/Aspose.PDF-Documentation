---
title: Python을 사용한 벡터 그래픽 작업
linktitle: 벡터 그래픽 작업
type: docs
weight: 100
url: /ko/python-net/working-with-vector-graphics/
description: 이 문서는 Python을 사용한 GraphicsAbsorber 도구 작업 기능을 설명합니다.
lastmod: "2025-05-17"
TechArticle: true
AlternativeHeadline: Python을 이용해 PDF에서 GraphicsAbsorber 도구 사용
Abstract: Aspose.PDF for Python via .NET 문서의 '벡터 그래픽 작업' 기사에서는 GraphicsAbsorber 클래스를 사용하여 PDF 문서 내 벡터 그래픽을 조작하려는 개발자를 위한 포괄적인 안내서를 제공합니다. 이 클래스는 PDF 페이지 전반에 걸쳐 벡터 그래픽 요소를 추출, 이동, 제거 및 복제하는 기능을 지원합니다.
---

이 장에서는 강력한 `GraphicsAbsorber` 클래스를 사용하여 PDF 문서 내 벡터 그래픽과 상호 작용하는 방법을 살펴봅니다. 그래픽을 이동, 제거 또는 추가해야 할 경우, 이 가이드는 이러한 작업을 효과적으로 수행하는 방법을 보여줍니다.

## 소개

벡터 그래픽은 이미지, 도형 및 기타 그래픽 요소를 나타내는 데 사용되는 많은 PDF 문서의 핵심 구성 요소입니다. Aspose.PDF는 개발자가 이러한 그래픽에 프로그래밍 방식으로 접근하고 조작할 수 있도록 `GraphicsAbsorber` 클래스를 제공합니다. `GraphicsAbsorber`의 `Visit` 메서드를 사용하면 지정된 페이지에서 벡터 그래픽을 추출하고 이동, 제거 또는 다른 페이지에 복사하는 등 다양한 작업을 수행할 수 있습니다.

## 그래픽 추출

벡터 그래픽 작업의 첫 번째 단계는 PDF 문서에서 그래픽을 추출하는 것입니다. `GraphicsAbsorber` 클래스를 사용하여 이를 수행하는 방법은 다음과 같습니다.

1. PDF 문서를 엽니다.
1. GraphicsAbsorber를 초기화합니다.
1. 대상 페이지를 선택합니다.
1. 페이지에서 그래픽을 추출합니다.
1. 추출된 요소를 반복하고 표시합니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Use the `Visit` method to extract graphics from the page
            graphics_absorber.visit(page)
            # Display information about the extracted elements
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

GraphicsAbsorber 클래스는 aspose.pdf.vector 네임스페이스의 일부이며 PDF 문서 내 벡터 그래픽과 상호 작용하도록 특별히 설계되었습니다.

## 그래픽 이동

그래픽을 추출한 후에는 같은 페이지에서 다른 위치로 이동할 수 있습니다. 이를 달성하는 방법은 다음과 같습니다.

1. PDF 문서를 엽니다.
1. GraphicsAbsorber를 초기화합니다.
1. 대상 페이지를 선택합니다.
1. 그래픽 요소를 추출합니다.
1. 성능을 위해 업데이트를 일시 중단합니다.
1. 그래픽 요소 위치를 수정합니다.
1. 업데이트를 재개하고 변경 사항을 적용합니다.
1. 업데이트된 문서를 저장합니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create a GraphicsAbsorber instance
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Temporarily suspend updates to improve performance
            graphics_absorber.suppress_update()
            # Loop through each extracted graphic element and shift its position
            for element in graphics_absorber.elements:
                position = element.position
                # Move graphics by shifting its X and Y coordinates
                element.position = ap.Point(position.x + 150, position.y - 10)
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## 그래픽 제거

페이지에서 특정 그래픽을 제거하고자 하는 경우가 있습니다. Aspose.PDF for Python은 이를 수행하기 위한 두 가지 방법을 제공합니다.

### 방법 1: 사각형 경계 사용

다음 예제는 Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 문서 첫 페이지의 특정 사각형 영역 내에 위치한 벡터 그래픽 요소를 제거하는 방법을 보여줍니다. 이 과정은 정의된 사각형 내의 그래픽 요소를 식별하고 이를 제거하여 PDF 콘텐츠를 정리하거나 수정하는 것을 포함합니다.

1. PDF 문서를 엽니다.
1. GraphicsAbsorber를 초기화합니다.
1. 대상 페이지를 선택합니다.
1. 그래픽 요소를 추출합니다.
1. 대상 사각형을 정의합니다.
1. 성능을 위해 업데이트를 일시 중단합니다.
1. 사각형 내의 그래픽 요소를 제거합니다.
1. 업데이트를 재개하고 변경 사항을 적용합니다.
1. 업데이트된 문서를 저장합니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Temporarily suspend updates for better performance
            graphics_absorber.suppress_update()
            # Iterate through the extracted graphic elements and remove elements inside the rectangle
            for element in graphics_absorber.elements:
                # Check if the graphic's position falls within the rectangle
                if rectangle.contains(element.position, False):
                    # Remove the graphic element
                    element.remove()
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### 방법 2: 제거된 요소 컬렉션 사용

다음 예제는 Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 문서 첫 페이지의 특정 사각형 영역 내에 위치한 벡터 그래픽 요소를 제거하는 방법을 보여줍니다. 이 과정은 정의된 사각형 내의 그래픽 요소를 식별하고 이를 제거하여 PDF 콘텐츠를 정리하거나 수정하는 것을 포함합니다.

1. PDF 문서를 엽니다.
1. GraphicsAbsorber를 초기화합니다.
1. 대상 페이지를 선택합니다.
1. 대상 사각형을 정의합니다.
1. 그래픽 요소 추출.
1. 제거를 위한 컬렉션 생성.
1. 사각형 내 요소 식별.
1. 성능을 위해 업데이트 일시 중지.
1. 그래픽 요소 제거.
1. 업데이트 재개 및 변경 적용.
1. 업데이트된 문서 저장.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Create a collection for the removed elements
            removed_elements_collection = ap.vector.GraphicElementCollection()
            # Add elements within the rectangle to the collection
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position,False):
                    removed_elements_collection.add(item)
            # Temporarily suppress updates for better performance
            page.contents.suppress_update()
            # Delete the selected graphic elements
            page.delete_graphics(removed_elements_collection)
            # Resume updates and apply changes
            page.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## 다른 페이지에 그래픽 추가

한 페이지에서 흡수한 그래픽을 동일 문서 내 다른 페이지에 추가할 수 있습니다.
이를 달성하는 두 가지 방법이 있습니다:

### 방법 1: 그래픽 개별 추가

다음 예제는 PDF 문서의 첫 페이지에서 벡터 그래픽 요소를 복사하여 두 번째 페이지에 붙여넣는 방법을 보여줍니다. 이 작업은 PDF 문서 내 벡터 그래픽을 추출하고 조작할 수 있는 GraphicsAbsorber 클래스를 통해 수행됩니다.

1. PDF 문서를 엽니다.
1. GraphicsAbsorber를 초기화합니다.
1. 대상 페이지를 선택합니다.
1. 첫 페이지에서 그래픽 요소를 추출합니다.
1. 성능을 위해 두 번째 페이지의 업데이트를 일시 중지합니다.
1. 추출한 그래픽 요소를 두 번째 페이지에 추가합니다.
1. 업데이트를 재개하고 변경을 적용합니다.
1. 업데이트된 문서를 저장합니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add each graphic element from the first page to the second page
            for element in graphics_absorber.elements:
                element.add_on_page(page_2) # Add each graphic element to the second page.
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### 방법 2: 그래픽을 컬렉션으로 추가

다음 예제는 PDF 문서의 첫 페이지에서 벡터 그래픽 요소를 복제하여 두 번째 페이지에 배치하는 방법을 보여줍니다. 이는 PDF 문서 내 벡터 그래픽을 추출하고 조작할 수 있는 GraphicsAbsorber 클래스를 사용하여 구현됩니다.

1. PDF 문서를 엽니다.
1. GraphicsAbsorber를 초기화합니다.
1. 대상 페이지를 선택합니다.
1. 첫 페이지에서 그래픽 요소를 추출합니다.
1. 성능을 위해 두 번째 페이지의 업데이트를 일시 중지합니다.
1. 추출한 그래픽 요소를 두 번째 페이지에 추가합니다.
1. 업데이트를 재개하고 변경을 적용합니다.
1. 업데이트된 문서를 저장합니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add all graphics at once from the first page to the second page
            page_2.add_graphics(graphics_absorber.elements, None)
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```
