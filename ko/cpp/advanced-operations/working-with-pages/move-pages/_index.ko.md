---
title: PDF 페이지를 프로그래밍 방식으로 이동 C++
linktitle: PDF 페이지 이동
type: docs
weight: 20
url: /cpp/move-pages/
description: Aspose.PDF for C++를 사용하여 원하는 위치 또는 PDF 파일의 끝으로 페이지를 이동해 보세요.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 한 PDF 문서에서 다른 문서로 페이지 이동

문서 내에서 PDF 페이지를 이동하는 것은 매우 흥미롭고 인기 있는 작업입니다.
이 주제에서는 C++를 사용하여 한 PDF 문서에서 다른 문서의 끝으로 페이지를 이동하는 방법을 설명합니다.
페이지를 이동하려면 다음을 수행해야 합니다:

1. 원본 PDF 파일로 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스 객체를 생성합니다.
1. [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 컬렉션에서 페이지를 가져옵니다.
1. 대상 문서에 페이지를 [추가](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1)합니다.
1. Save 메서드를 사용하여 출력 PDF를 저장합니다.
1. [삭제](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) 소스 문서의 페이지.
1. 저장 메서드를 사용하여 소스 PDF를 저장합니다.

다음 코드 스니펫은 한 페이지를 이동하는 방법을 보여줍니다.

```cpp
void MovePage()
{
    // 문서 열기
    String _dataDir("C:\\Samples\\");
    String srcFileName("<파일 이름 입력>");
    String dstFileName("<파일 이름 입력>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    dstDocument->get_Pages()->Add(page);
    // 출력 파일 저장
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete(2);
    srcDocument->Save(dstFileName);
}
```

## 한 PDF 문서에서 다른 PDF 문서로 여러 페이지 이동

1. 소스 PDF 파일로 [문서](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스 객체를 만듭니다.
1. 이동할 페이지 번호가 포함된 배열을 정의합니다.
1. 배열을 반복 실행:
1. [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 컬렉션에서 페이지 가져오기.
1. 페이지를 대상 문서에 [추가](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1).
1. Save 메서드를 사용하여 출력 PDF 저장.
1. 원본 문서에서 페이지 [삭제](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15).
1. Save 메서드를 사용하여 원본 PDF 저장.

다음 코드 스니펫은 PDF 파일의 끝에 빈 페이지를 삽입하는 방법을 보여줍니다.

```cpp
void MoveBunchPages()
{
    // 문서 열기
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();


    auto pages = MakeArray<int>({ 1,3 });

    for (auto pageIndex : pages)
    {
        auto page = srcDocument->get_Pages()->idx_get(pageIndex);
        dstDocument->get_Pages()->Add(page);
    }
    // 출력 파일 저장
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete();
    srcDocument->Save(dstFileName);
}
```
## 현재 PDF 문서에서 페이지를 새 위치로 이동

1. 소스 PDF 파일로 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스 객체를 생성합니다.
1. [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 컬렉션에서 페이지를 가져옵니다.
1. 페이지를 새 위치로 [추가](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1)합니다 (예: 끝으로).
1. 이전 위치에서 페이지를 [삭제](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15)합니다.
1. Save 메서드를 사용하여 출력 PDF를 저장합니다.

```cpp
void MovePagesInOnePDF()
{
    // 문서 열기
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    srcDocument->get_Pages()->Add(page);
    srcDocument->get_Pages()->Delete(2);

    // 출력 파일 저장
    srcDocument->Save(dstFileName);
}
```