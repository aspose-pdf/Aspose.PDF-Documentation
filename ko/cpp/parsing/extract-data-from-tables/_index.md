---
title: PDF에서 테이블 데이터 추출 
linktitle: 테이블 데이터 추출
type: docs
weight: 40
url: /ko/cpp/extract-data-from-table-in-pdf/
description: Aspose.PDF for C++를 사용하여 PDF에서 테이블 형식을 추출하는 방법을 배우십시오.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF에서 프로그래밍 방식으로 테이블 추출

PDF는 문서를 교환하는 가장 일반적인 형식이기 때문에 여러 데이터 세트가 분석이 필요한 문서를 고려해 보겠습니다. 이 기사에서는 PDF에서 테이블을 추출하는 방법을 설명합니다.

**Aspose.PDF for C++**는 개발자에게 PDF 문서의 테이블에서 데이터를 추출하는 데 필요한 도구를 제공합니다.

이 예제는 PDF 파일의 테이블에서 표 형식 데이터를 검색하기 위해 [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) 클래스를 사용하는 방법을 보여줍니다.

다음 예제는 모든 페이지에서 테이블 추출을 보여줍니다:

```cpp
void ExtractTable() {
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름을 위한 문자열
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    // 페이지 스캔
    for (auto page : document->get_Pages()) {
        absorber->Visit(page);
        for (auto table : absorber->get_TableList()) {
        std::cout << "Table" << std::endl;
        // 행 목록 반복
        for (auto row : table->get_RowList()) {
            // 셀 목록 반복
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF 페이지의 특정 영역에서 테이블 추출

각 흡수된 테이블은 페이지에서 테이블의 위치를 설명하는 [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/) 속성을 가지고 있습니다.

따라서 특정 지역에 위치한 테이블을 추출하려면 특정 좌표를 사용해야 합니다.

다음 예제는 사각형 주석으로 표시된 테이블을 추출하는 방법을 보여줍니다:

```cpp
void ExtractMarkedTable()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름을 위한 문자열
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    auto page = document->get_Pages()->idx_get(1);
    auto sqa = MakeObject<Aspose::Pdf::Annotations::SquareAnnotation>(page, Rectangle::get_Trivial());
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(sqa);


    auto list = annotationSelector->get_Selected();
    if (list->get_Count() == 0) {
        std::cerr << "표시된 테이블을 찾을 수 없습니다.." << std::endl;
        return;
    }

    auto squareAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::SquareAnnotation>(list->idx_get(1));

    absorber->Visit(page);

    for (auto table : absorber->get_TableList())
    {
        auto isInRegion =
        (squareAnnotation->get_Rect()->get_LLX() < table->get_Rectangle()->get_LLX()) &&
        (squareAnnotation->get_Rect()->get_LLY() < table->get_Rectangle()->get_LLY()) &&
        (squareAnnotation->get_Rect()->get_URX() > table->get_Rectangle()->get_URX()) &&
        (squareAnnotation->get_Rect()->get_URY() > table->get_Rectangle()->get_URY());

        if (isInRegion)
        {
        for (auto row : table->get_RowList()) {
            // 셀의 목록을 반복
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF에서 테이블 데이터 추출하여 CSV 파일에 저장하기

다음 예제는 테이블을 추출하여 CSV 파일로 저장하는 방법을 보여줍니다. PDF를 Excel 스프레드시트로 변환하는 방법은 [PDF를 Excel로 변환](/pdf/ko/cpp/convert-pdf-to-excel/) 기사를 참조하십시오.

```cpp
void ExtractTableSaveCSV()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름에 대한 문자열
    String infilename("sample-table.pdf");
    String outfilename("PDFToXLS_out.csv");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Excel 저장 옵션 객체 인스턴스화
    auto excelSave = MakeObject<ExcelSaveOptions>();
    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::CSV);

    // XLS 형식으로 출력 저장
    document->Save(_dataDir + outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```