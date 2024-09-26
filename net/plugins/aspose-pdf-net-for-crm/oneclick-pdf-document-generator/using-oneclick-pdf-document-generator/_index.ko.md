---
title: OneClick PDF 문서 생성기 사용법
type: docs
weight: 10
url: /net/using-oneclick-pdf-document-generator/
description: Microsoft Dynamics에서 Aspose.PDF OneClick PDF 문서 생성기 사용 방법을 배우세요
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 템플릿 생성 및 CRM에 추가

- 워드를 열고 템플릿을 생성하세요.
- CRM에서 오는 데이터에 대한 MailMerge 필드를 삽입하세요.

![MailMerg 필드 삽입](using-oneclick-pdf-document-generator_1.png)

- 필드 이름이 CRM 필드와 정확히 일치하는지 확인하세요.
- 템플릿은 개별 엔티티 사용에 특화되어 있습니다.

![데모 템플릿](using-oneclick-pdf-document-generator_2.png)

- 템플릿이 생성되면, CRM에서 OneClick PDF 설정 엔티티를 열고 새 레코드를 생성하세요.
- 템플릿의 이름을 지정하고, 템플릿이 정의된 엔티티를 선택한 후 생성된 문서를 첨부 파일에 첨부하세요.

![템플릿 선택](using-oneclick-pdf-document-generator_3.png)

## 리본 버튼에서 문서 생성

- 문서를 생성하고자 하는 레코드를 엽니다.
- 문서를 생성하고자하는 레코드를 엽니다.
- 리본에서 OneClick PDF 버튼을 클릭합니다.

![OneClick PDF 클릭](using-oneclick-pdf-document-generator_4.png)

- 팝업에서: 템플릿, 파일 이름 및 작업을 선택한 후 생성을 클릭합니다.
- 선택한 기준에 따라 다운로드된 파일이나 노트를 확인합니다.

## OneClick 버튼 구성 및 사용

- 폼에서 직접 OneClick 버튼을 사용하려면, 폼 사용자 정의를 엽니다.
- OneClick 버튼을 추가하고 싶은 위치에 WebResource를 삽입합니다.
- Webresource에서 OpenButtonPage를 선택하고 이름을 지정합니다.
- 다음 예제에 따라 데이터 필드에서 버튼을 구성합니다.

![WebResource 속성](using-oneclick-pdf-document-generator_5.png)

- 각 버튼에 대해 별도의 줄을 사용하고 다음 구문을 사용합니다:
  - 구문:템플릿 이름 |<Action: 다운로드/노트>|출력 파일 이름
  - 예시:Demo|Download|My Downloaded File
- 사용자 정의를 저장하고 게시합니다.
- 폼에서 버튼을 사용할 수 있습니다.

![폼에서 사용 가능한 버튼](using-oneclick-pdf-document-generator_6.png)
![폼에서 사용 가능한 버튼](using-oneclick-pdf-document-generator_6.png)
