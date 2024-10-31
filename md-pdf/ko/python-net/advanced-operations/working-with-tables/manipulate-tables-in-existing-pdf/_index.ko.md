---
title: 기존 PDF의 테이블 조작
linktitle: 테이블 조작
type: docs
weight: 40
url: /python-net/manipulate-tables-in-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "기존 PDF의 테이블 조작",
    "alternativeHeadline": "기존 PDF의 테이블 내용 업데이트 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 테이블 조작",
    "wordcount": "302",
    "proficiencyLevel":"초급",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


## 기존 PDF에서 테이블 조작

.NET을 통해 Python용 Aspose.PDF에서 지원하는 초기 기능 중 하나는 테이블 작업 기능이며, 처음부터 생성된 PDF 파일이나 기존 PDF 파일에 테이블을 추가할 수 있는 훌륭한 지원을 제공합니다. 이번 새 릴리스에서는 PDF 문서 페이지에 이미 존재하는 간단한 테이블을 검색하고 구문 분석하는 새로운 기능을 구현했습니다. [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/)라는 새 클래스가 이러한 기능을 제공합니다. TableAbsorber의 사용법은 기존의 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 클래스와 매우 유사합니다. 다음 코드 스니펫은 특정 테이블 셀의 내용을 업데이트하는 단계를 보여줍니다.

```python

    import aspose.pdf as ap

    # 기존 PDF 파일 로드
    pdf_document = ap.Document(input_file)
    # 테이블을 찾기 위한 TableAbsorber 객체 생성
    absorber = ap.text.TableAbsorber()
    # 첫 번째 페이지를 방문하여 absorber 사용
    absorber.visit(pdf_document.pages[1])
    # 페이지의 첫 번째 테이블, 첫 번째 셀 및 그 안의 텍스트 조각에 접근
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]
    # 셀의 첫 번째 텍스트 조각의 텍스트 변경
    fragment.text = "hi world"
    pdf_document.save(output_file)
```


## PDF 문서에서 오래된 표를 새 표로 교체하기

특정 표를 찾아 원하는 표로 교체해야 하는 경우, [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) 클래스의 [replace()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) 메서드를 사용할 수 있습니다. 다음 예제는 PDF 문서 내의 표를 교체하는 기능을 보여줍니다:

```python

    import aspose.pdf as ap

    # 기존 PDF 문서 로드
    pdf_document = ap.Document(input_file)
    # 표를 찾기 위한 TableAbsorber 객체 생성
    absorber = ap.text.TableAbsorber()
    # 첫 번째 페이지를 absorber로 방문
    absorber.visit(pdf_document.pages[1])
    # 페이지에서 첫 번째 표 가져오기
    table = absorber.table_list[0]
    # 새 표 생성
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")

    # 기존 표를 새 표로 교체
    absorber.replace(pdf_document.pages[1], table, new_table)
    # 문서 저장
    pdf_document.save(output_file)
```


## 현재 페이지에서 테이블이 깨질지 여부를 결정하는 방법

이 코드는 테이블이 포함된 PDF 문서를 생성하고, 페이지에 사용할 수 있는 공간을 계산하며, 테이블에 더 많은 행을 추가하는 것이 공간 제약으로 인해 페이지가 깨질지 여부를 확인합니다. 결과는 출력 파일에 저장됩니다.

```python

    import aspose.pdf as ap

    # PDF 클래스의 객체를 인스턴스화합니다.
    pdf = ap.Document()
    # PDF 문서 섹션 컬렉션에 섹션을 추가합니다.
    page = pdf.pages.add()
    # 테이블 객체를 인스턴스화합니다.
    table1 = ap.Table()
    table1.margin.top = 300
    # 원하는 섹션의 문단 컬렉션에 테이블을 추가합니다.
    page.paragraphs.add(table1)
    # 테이블의 열 너비를 설정합니다.
    table1.column_widths = "100 100 100"
    # BorderInfo 객체를 사용하여 기본 셀 테두리를 설정합니다.
    table1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # 또 다른 사용자 정의 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다.
    table1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # MarginInfo 객체를 생성하고 왼쪽, 아래, 오른쪽 및 위쪽 여백을 설정합니다.
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # MarginInfo 객체에 기본 셀 패딩을 설정합니다.
    table1.default_cell_padding = margin
    # 카운터를 17로 증가시키면 테이블이 깨집니다.
    # 더 이상 이 페이지에 수용할 수 없기 때문입니다.
    for row_counter in range(0, 17):
        # 테이블에 행을 생성하고 행에 셀을 추가합니다.
        row1 = table1.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
    # 페이지 높이 정보를 가져옵니다.
    page_height = pdf.page_info.height
    # 페이지 상단 및 하단 여백, 테이블 상단 여백 및 테이블 높이의 총 높이 정보를 가져옵니다.
    total_objects_height = page.page_info.margin.top + page.page_info.margin.bottom + table1.margin.top + \
                           table1.get_height(None)
    # 페이지 높이, 테이블 높이, 테이블 상단 여백 및 페이지 상단
    # 그리고 하단 여백 정보를 표시합니다.
    print("PDF 문서 높이 = " + str(pdf.page_info.height) + "\n상단 여백 정보 = " + str(page.page_info.margin.top)
          + "\n하단 여백 정보 = " + str(page.page_info.margin.bottom) + "\n\n테이블-상단 여백 정보 = "
          + str(table1.margin.top) + "\n평균 행 높이 = " + str(table1.rows[0].min_row_height) + " \n테이블 높이 "
          + str(table1.get_height(None)) + "\n ----------------------------------------" + "\n총 페이지 높이 ="
          + str(page_height) + "\n테이블을 포함한 누적 높이 =" + str(total_objects_height))
    # 페이지 상단 여백 + 페이지 하단 여백
    # + 테이블 상단 여백 및 테이블 높이를 페이지 높이에서 뺀 값이
    # 10보다 작은지 확인합니다. (평균 행은 10보다 클 수 있습니다.)
    if (page_height - total_objects_height) <= 10:
        # 값이 10보다 작으면 메시지를 표시합니다.
        # 이는 새로운 행을 추가할 수 없으며, 새 행을 추가하면
        # 테이블이 깨질 것임을 나타냅니다. 이는 행 높이 값에 따라 다릅니다.
        print("페이지 높이 - 객체 높이 < 10, 따라서 테이블이 깨질 것입니다.")
    # pdf 문서를 저장합니다.
    pdf.save(output_file)
```


## 테이블에 반복 열 추가

[Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 클래스에서는 테이블의 세로 길이가 너무 길어 다음 페이지로 넘칠 경우 행을 반복하는 [repeating_rows_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties)를 설정할 수 있습니다. 그러나 어떤 경우에는 테이블이 너무 넓어 한 페이지에 맞지 않아서 다음 페이지로 이어져야 합니다. 이를 위해 우리는 [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) 클래스에 [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) 속성을 구현했습니다. 이 속성을 설정하면 테이블이 열 단위로 다음 페이지로 나뉘고, 다음 페이지의 시작에 지정된 열 수가 반복됩니다. 다음 코드 스니펫은 [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) 속성의 사용법을 보여줍니다:

```python

    import aspose.pdf as ap

    # 새 문서 생성
    doc = ap.Document()
    page = doc.pages.add()
    # 전체 페이지를 차지하는 외부 테이블 인스턴스화
    outer_table = ap.Table()
    outer_table.column_widths = "100%"
    outer_table.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # outerTable 내부에 중첩되어 같은 페이지 내에서 나뉠 테이블 객체 인스턴스화
    my_table = ap.Table()
    my_table.broken = ap.TableBroken.VERTICAL_IN_SAME_PAGE
    my_table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # outerTable을 페이지 단락에 추가
    # outerTable에 내 테이블 추가
    page.paragraphs.add(outer_table)
    body_row = outer_table.rows.add()
    body_cell = body_row.cells.add()
    body_cell.paragraphs.add(my_table)
    my_table.repeating_columns_count = 5
    page.paragraphs.add(my_table)
    # 헤더 행 추가
    row = my_table.rows.add()
    row.cells.add("header 1")
    row.cells.add("header 2")
    row.cells.add("header 3")
    row.cells.add("header 4")
    row.cells.add("header 5")
    row.cells.add("header 6")
    row.cells.add("header 7")
    row.cells.add("header 11")
    row.cells.add("header 12")
    row.cells.add("header 13")
    row.cells.add("header 14")
    row.cells.add("header 15")
    row.cells.add("header 16")
    row.cells.add("header 17")
    for row_counter in range(0, 6):
        # 테이블에 행을 만들고 행에 셀을 추가
        row1 = my_table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Python을 위한 PDF 조작 라이브러리 .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>