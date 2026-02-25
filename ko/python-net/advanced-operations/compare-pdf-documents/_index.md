---
title: PDF 문서 비교
linktitle: PDF 비교
type: docs
weight: 130
url: /ko/python-net/compare-pdf-documents/
description: 주석 표시와 나란히 출력으로 PDF 문서 내용을 비교할 수 있습니다.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 
Abstract: 
---

## PDF 문서를 비교하는 방법

PDF 문서를 다룰 때, 두 문서의 내용을 비교하여 차이를 확인해야 할 때가 있습니다. Aspose.PDF for Python via .NET 라이브러리는 이를 위한 강력한 도구 세트를 제공합니다. 이 기사에서는 몇 가지 간단한 코드 스니펫을 사용해 PDF 문서를 비교하는 방법을 살펴보겠습니다.

Aspose.PDF의 비교 기능을 사용하면 두 PDF 문서를 페이지별로 비교할 수 있습니다. 특정 페이지만 비교하거나 전체 문서를 비교하도록 선택할 수 있습니다. 결과 비교 문서는 차이를 강조 표시하여 두 파일 간의 변경 사항을 쉽게 확인할 수 있게 합니다.

다음은 Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 문서를 비교할 수 있는 가능한 방법들의 목록입니다:

1. **특정 페이지 비교** - 두 PDF 문서의 첫 페이지를 비교합니다.
1. **전체 문서 비교** - 두 PDF 문서의 전체 내용을 비교합니다.
1. **PDF 문서를 그래픽으로 비교**:

- 'comparer.get_difference' 메서드로 PDF 비교 - 변경 사항이 표시된 개별 이미지.
- 'comparer.compare_documents_to_pdf' 메서드로 PDF 비교 - 변경 사항이 표시된 이미지가 포함된 PDF 문서.

## 특정 페이지 비교

첫 번째 코드 스니펫은 SideBySidePdfComparer 클래스를 사용하여 두 PDF 문서의 첫 페이지를 비교하는 방법을 보여줍니다.

1. 문서 초기화.
1. 비교를 수행하는 함수를 생성합니다.
1. 비교 절차:

- document1.pages[1] 및 document2.pages[1]: - 각각의 문서에서 비교할 첫 페이지를 지정합니다. Aspose.PDF에서는 페이지 인덱스가 1부터 시작한다는 점에 유의하세요.
- SideBySideComparisonOptions - 이 클래스는 비교 동작을 사용자 지정할 수 있게 해줍니다.
- additional_change_marks = True - 현재 비교 중인 페이지에 없더라도 다른 페이지에 존재할 수 있는 차이를 강조 표시하기 위해 추가 변경 표시를 활성화합니다.
- comparison_mode = ComparisonMode.IgnoreSpaces - 텍스트의 공백을 무시하고 단어 내부의 변경 사항에만 집중하도록 비교 모드를 설정합니다.

1. 비교 결과는 지정된 data_dir에 ComparingSpecificPages_out.pdf 라는 새 PDF 파일로 저장됩니다.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_specific_pages():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingSpecificPages1.pdf")
        document2 = ap.Document(data_dir + "ComparingSpecificPages2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1.pages[1], document2.pages[1], data_dir + "ComparingSpecificPages_out.pdf", options)
```

## 전체 문서 비교

두 번째 코드 스니펫은 두 PDF 문서의 전체 내용을 비교하도록 범위를 확장합니다.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_entire_documents():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingEntireDocuments1.pdf")
        document2 = ap.Document(data_dir + "ComparingEntireDocuments2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1, document2, data_dir + "ComparingEntireDocuments_out.pdf", options)
```

제공된 코드는 Aspose.PDF for Python via .NET을 사용하여 두 PDF 문서를 비교하는 방법을 보여줍니다. SideBySidePdfComparer 클래스를 활용해 페이지별 비교를 수행하고, 차이를 나란히 표시하는 새 PDF를 생성합니다. 비교는 SideBySideComparisonOptions로 구성되며, additional_change_marks를 True로 설정하여 현재 페이지뿐만 아니라 다른 페이지의 변경 사항도 강조하고, comparison_mode를 IgnoreSpaces로 설정하여 공백 변화를 무시하고 의미 있는 내용 차이에 집중합니다.

## GraphicalPdfComparer를 사용한 비교

문서 협업 시, 특히 전문가 환경에서는 동일 파일의 여러 버전이 생기기 쉽습니다.
제공된 코드는 Aspose.PDF for Python via .NET을 사용해 두 PDF 문서의 특정 페이지를 시각적으로 비교하는 방법을 보여줍니다. `GraphicalPdfComparer` 클래스를 이용해 두 PDF의 첫 페이지 간 차이를 강조하고, 이러한 차이를 나타내는 이미지들을 생성합니다.

다음 클래스 속성을 설정할 수 있습니다:

- Resolution - 출력 이미지와 비교 중 생성되는 이미지의 DPI 단위 해상도.
- Color - 변경 표시의 색상.
- Threshold - 백분율로 표시되는 변경 임계값. 기본값은 0입니다. 0이 아닌 값을 설정하면 중요하지 않은 그래픽 변경을 무시할 수 있습니다.

Aspose.PDF for Python via .NET을 사용하면 문서와 페이지를 비교하고 비교 결과를 PDF 문서나 이미지 파일로 출력할 수 있습니다.

`GraphicalPdfComparer` 클래스에는 추가 처리가 가능한 형태로 페이지 이미지 차이를 얻을 수 있는 메서드가 있습니다: `get_difference(document1.pages[1], document2.pages[1])`.

이 메서드는 `images_difference` 유형의 객체를 반환하는데, 여기에는 비교 중인 첫 페이지의 이미지와 차이 배열이 포함됩니다.

`images_difference` 객체를 사용하면 차이 배열을 원본 이미지에 적용하여 다른 이미지를 생성하고, 비교되는 두 번째 페이지의 이미지를 얻을 수 있습니다. 이를 위해 `difference_to_image` 및 `get_destination_image` 메서드를 사용합니다.

### Get Difference 메서드로 PDF 비교

제공된 코드는 두 PDF 문서를 비교하고 차이를 시각적으로 나타내는 `get_difference` 메서드를 정의합니다.

이 메서드는 두 PDF 파일의 첫 페이지를 비교하고 두 개의 PNG 이미지를 생성합니다:

- 하나의 이미지는 페이지 간 차이를 빨간색으로 강조합니다.
- 다른 이미지는 대상(두 번째) PDF 페이지의 시각적 표현입니다.

이 프로세스는 문서의 두 버전 사이의 변경 사항이나 차이를 시각적으로 비교하는 데 유용할 수 있습니다.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer

    def compare_pdf_with_get_difference_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod2.pdf")

        # Create comparer
        comparer = GraphicalPdfComparer()

        # Compare specific pages
        images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

        # Get image showing differences in red over a white background
        diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
        diff_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png")

        # Get the second image representing the destination page
        dest_img = images_difference.get_destination_image()
        dest_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png")
```

### Compare PDF와 CompareDocumentsToPdf 메서드

제공된 코드 스니펫은 `compare_documents_to_pdf` 메서드를 사용하며, 두 문서를 비교하고 비교 결과의 PDF 보고서를 생성합니다.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer
    from aspose.pdf.devices import Resolution

    def compare_pdf_with_compare_documents_to_pdf_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf")

        # Create comparer and set options
        comparer = GraphicalPdfComparer()
        comparer.threshold = 3.0
        comparer.color = ap.Color.blue
        comparer.resolution = Resolution(300)

        # Compare and output to a PDF file
        comparer.compare_documents_to_pdf(document1, document2, data_dir + "compareDocumentsToPdf_out.pdf")
```

이 예제는 Aspose.PDF for Python via .NET을 사용하여 두 전체 PDF 문서를 그래픽으로 비교하는 방법을 보여줍니다. `GraphicalPdfComparer` 클래스를 활용하여 문서 간 차이를 시각적으로 강조한 새 PDF 파일을 생성합니다.

- threshold 속성은 3.0으로 설정되어 이 비율 이하의 작은 차이는 비교 시 무시되고 보다 중요한 변경에 초점을 맞춥니다.
- 색상 속성을 ap.Color.blue로 설정하여 차이를 파란색으로 표시함으로써 명확한 시각적 구분을 제공합니다.
- resolution 속성을 설정하여 300 DPI 해상도로 비교를 수행하므로 상세하고 선명한 출력이 보장됩니다.

`compare_documents_to_pdf` 메서드는 두 문서의 모든 페이지를 비교하고, 차이를 시각적으로 강조한 새 PDF 파일인 compareDocumentsToPdf_out.pdf에 결과를 출력합니다.

