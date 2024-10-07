---
title: PDF-UA 준수 테스트 - 오류 목록
linktitle: PDF-UA 준수 테스트 - 오류 목록
type: docs
weight: 50
url: /net/pdf-ua-compliance-test-errors-list/
description: 이 글은 Aspose.PDF API와 C# 또는 VB를 사용하여 PDF/UA 준수 테스트 중 발생할 수 있는 오류 목록을 보여줍니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF-UA 준수 테스트 - 오류 목록",
    "alternativeHeadline": "API를 사용한 PDF/UA 준수 테스트",
    "author": {
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, 문서 생성",
    "wordcount": "302",
    "proficiencyLevel":"초급",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/pdf-ua-compliance-test-errors-list/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-ua-compliance-test-errors-list/"
    },
    "dateModified": "2022-02-04",
    "description": "이 글은 Aspose.PDF API와 C# 또는 VB를 사용하여 PDF/UA 준수 테스트 중 발생할 수 있는 오류 목록을 보여줍니다."
}
</script>
Aspose.PDF API를 사용하여 PDF/UA 준수 테스트를 수행하는 동안 발생할 수 있는 오류 메시지에 대해 알고 싶을 수 있습니다. 이러한 오류는 일반, 텍스트, 글꼴, 제목 등 여러 유형이 있습니다. 이러한 오류에 대한 정보는 오류의 정확한 원인과 처리 방법을 알아내는 데 도움이 될 수 있습니다.

이 문서에서는 API를 사용한 PDF/UA 준수 테스트 중에 발생할 수 있는 오류를 나열합니다.

## **일반**

|**코드**|**심각도**|**메시지**|
| :- | :- | :- |
|5:1|오류|PDF/UA 식별자가 누락되었습니다|
|6.2:1.1|오류|구조적 부모 트리: 일관성 없는 항목 발견|
|7.1:1.1(14.8.1)|오류|문서가 태그 지정된 것으로 표시되지 않음|
|7.1:1.1(14.8)|오류|[OBJECT_NAME] 객체가 태그 지정되지 않음|
|7.1:1.2(14.8.2.2)|오류|태그 지정된 내용 내부에 아티팩트 존재|
|7.1:1.3(14.8.2.2)|오류|아티팩트 내부에 태그 지정된 내용 존재|
|7.1:2.1|경고|구조 트리 누락|
|7.1:2.2|경고|루트 요소가 아닌 '문서' 구조 요소 발견|
|7.1:2.3|경고|루트 요소로 사용된 '[ELEMENT_NAME]' 구조 요소|
|7.1:2.3|경고|‘[ELEMENT_NAME]’ 구조 요소가 루트 요소로 사용됨|
|7.1:2.4.1|경고|‘[ELEMENT_NAME]’ 구조 요소의 부적절한 사용 가능성|
|7.1:2.4.2|오류|‘[ELEMENT_NAME]’ 구조 요소의 잘못된 사용|
|7.1:2.5|경고|StructTreeRoot에 잘못 중첩된 ‘[ELEMENT_NAME]’ 구조 요소|
|7.1:3(14.8.4)|오류|표준 구조 유형이 아닌 ‘[TYPE_NAME]’은 표준 구조 유형 또는 다른 표준이 아닌 구조 유형에 매핑되지 않음|
|7.1:4(14.8.4)|경고|표준 구조 유형 ‘[TYPE_NAME]’이 ‘[TYPE_NAME]’으로 재매핑됨|
|7.1:5|수동 검사 필요|색상 대비|
|7.1:6.1|오류|문서에 XMP 메타데이터가 누락됨|
|7.1:6.2|오류|문서의 XMP 메타데이터에 제목 누락|
|7.1:6.3|경고|문서의 XMP 메타데이터에서 제목이 비어 있음|
|7.1:7.1(12.2)|경고|‘ViewerPreferences’ 사전이 누락됨|
|7.1:7.2(12.2)|오류|‘DisplayDocTitle’ 항목이 설정되지 않음|
|7.1:8(14.7.1)|오류|‘Suspects’ 항목이 설정됨|
|7.1:9.1(14.7)|오류|페이지에 ‘StructParents’ 키가 누락됨|
|7.1:9.2(14.7)|오류|주석에서 ‘StructParent’ 항목이 누락됨|
## **텍스트**

|**코드**|**심각도**|**메시지**|
| :- | :- | :- |
|7.2:1|수동 검사 필요|논리적 읽기 순서|
|7.2:2(14.8.2.4.2)|오류|텍스트 객체의 문자를 유니코드로 매핑할 수 없음|
|7.2:3.1(14.9.2.2)|오류|텍스트 객체의 자연 언어를 결정할 수 없음|
|7.2:3.2(14.9.2.2)|오류|대체 텍스트의 자연 언어를 결정할 수 없음|
|7.2:3.3(14.9.2.2)|오류|실제 텍스트의 자연 언어를 결정할 수 없음|
|7.2:3.4(14.9.2.2)|오류|확장 텍스트의 자연 언어를 결정할 수 없음|
|7.2:4(14.9.4)|오류|확장 가능한 문자가 ActualText를 사용하여 태그되지 않음|

## **폰트**

|**조항**|**심각도**|**메시지**|
| :- | :- | :- |
|7.21.3.1|오류|CIDFont의 문자 컬렉션이 내부 CMap의 문자 컬렉션과 호환되지 않음|
|7.21.3.2|오류|CIDToGIDMap이 폰트 ‘[FONT_NAME]’에 포함되지 않았거나 불완전함|
|7.21.3.2|오류|폰트 ‘[FONT_NAME]’에 대한 CMap이 포함되지 않음|
|7.21.3.2|오류|폰트 ‘[FONT_NAME]’에 대해 CMap이 내장되어 있지 않습니다|
|7.21.4.2|오류|폰트 ‘[FONT_NAME]’에 대한 CIDSet이 없거나 불완전합니다|
|7.21.4.2|오류|내장된 폰트 ‘[FONT_NAME]’에 글리프가 누락되었습니다|
|7.21.6|오류|비상징적 TrueType 폰트 ‘[FONT_NAME]’에 cmap 항목이 없습니다|
|7.21.6|오류|상징적 TrueType 폰트 ‘[FONT_NAME]’에 대한 인코딩 항목이 금지되어 있습니다|
|7.21.6|오류|TrueType 폰트 ‘[FONT_NAME]’에 대해 잘못된 인코딩이 사용되었습니다|
|7.21.6|오류|비상징적 TrueType 폰트 ‘[FONT_NAME]’에 대한 “Differences” 배열이 잘못되었습니다|

## **그래픽**

|**코드**|**심각도**|**메시지**|
| :- | :- | :- |
|7.3:1(14.8.4.5)|오류|단일 페이지에 경계 상자 없이 ‘[ELEMENT_NAME]’ 요소가 있습니다|
|7.3:2|오류|‘[ELEMENT_NAME]’ 구조 요소에 대한 대체 텍스트가 누락되었습니다|
|7.3:3|오류|그림과 함께하는 캡션이 누락되었습니다|
|7.3:4(14.8.4.5)|오류|BT와 ET 연산자 사이에 그래픽 객체가 나타납니다|

## **제목**

|**코드**|**심각도**|**메시지**|
| :- | :- | :- |
|7.4.2:1|오류|첫 번째 제목이 첫 번째 레벨에 있지 않습니다|
|7.4.2:2|오류|번호가 매겨진 제목이 하나 이상의 제목 레벨을 건너뜁니다|
|7.4.2:2|Error|번호가 매겨진 제목이 하나 이상의 제목 수준을 건너뜁니다|
|7.4.4:1|Error|‘H’ 및 ‘Hn’ 구조 요소 발견|
|7.4.4:2|Error|부모 구조 요소 내에 ‘H’ 구조 요소가 하나 이상 있음|

## **테이블**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.5:1|Warning|불규칙한 테이블 행|
|7.5:2|Error|테이블 헤더 셀에 연결된 하위 셀이 없음|
|7.5:3.1|Warning|테이블 헤더가 누락됨|
|7.5:3.2|Warning|테이블 요약이 누락됨|

## **목록**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.6:1|Error|‘LI’ 구조 요소는 ‘L’ 요소의 자식이어야 함|
|7.6:2|Error|‘Lbl’ 및 ‘LBody’ 구조 요소는 ‘LI’ 요소의 자식이어야 함|

## **노트 및 참조**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.9:2.1|Error|‘Note’ 구조 요소에서 ID가 누락됨|
|7.9:2.2|Error|‘Note’ 구조 요소에서 ID 항목이 고유하지 않음|

## **선택적 내용**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.10:1|Error|선택적 내용 구성 사전에서 ‘Name’이 누락됨|
|7.10:1|Error|선택적 내용 구성 사전에서 'Name'이 누락되었습니다|
|7.10:2|Error|선택적 내용 구성 사전에 'AS' 키가 포함되어 있습니다|

## **임베디드 파일**

|**코드**|**심각도**|**메시지**|
| :- | :- | :- |
|7.11:1|Error|파일 사양에서 'F' 또는 'UF' 키가 누락되었습니다|
|7.11:2|Warning|파일 사양에서 'Desc' 키가 누락되었습니다|

## **디지털 서명**

|**코드**|**심각도**|**메시지**|
| :- | :- | :- |
|7.13:1|Error|서명 양식 필드 '[FIELD_NAME]'가 사양에 맞지 않습니다|
|7.13:2.1|Error|양식 필드 '[FIELD_NAME]'의 대체 이름의 자연 언어를 확인할 수 없습니다|
|7.13:2.2|Error|양식 필드 '[FIELD_NAME]'에서 대체 필드 이름 항목이 누락되었습니다|

## **비대화형 양식**

|**코드**|**심각도**|**메시지**|
| :- | :- | :- |
|7.14:1|Error|비대화형 양식 항목에서 'PrintField' 속성이 누락되었습니다|

## **XFA**

|**코드**|**심각도**|**메시지**|
| :- | :- | :- |
|7.15:1|Error|PDF에 동적 XFA 양식이 포함되어 있습니다|

## **보안**

|**코드**|**심각도**|**메시지**|
|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.16:1(7.6.3.2)|Error|보안 설정이 보조 기술이 문서의 내용에 접근하는 것을 차단합니다|
|7.16:2(7.6.3.2)|Error|권한 제한으로 인해 변환을 허용하지 않습니다|

## **Navigation**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.17:1|Error|문서 개요 오류|
|7.17:2|Error|개요의 자연어를 결정할 수 없습니다|
|7.17:3|Need manual check|의미론적으로 적절한 페이지 라벨|

## **Annotations**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.18.1:1|Error|내용 항목의 자연어를 결정할 수 없습니다|
|7.18.1:2|Error|주석에 대한 대체 설명이 누락되었습니다|
|7.18.1:3|Error|주석이 'Annot' 구조 요소 안에 포함되어 있지 않습니다|
|7.18.2:1|Error|ISO 32000에서 정의되지 않은 하위 유형의 주석이 7.18.1을 충족하지 않습니다|
|7.18.2:2|Error|TrapNet 하위 유형의 주석이 존재합니다|
|7.18.3:1|Error|주석이 있는 페이지의 탭 순서 항목이 'S'(구조)로 설정되지 않았습니다|
|7.18.4:1|Error|‘Widget’ 주석이 ‘Form’ 구조 요소 안에 포함되어 있지 않습니다|
|7.18.4:1|오류|‘Widget’ 주석이 ‘Form’ 구조 요소 내부에 포함되어 있지 않습니다|
|7.18.5:1|오류|‘Link’ 주석이 ‘Link’ 구조 요소 내부에 포함되어 있지 않습니다|
|7.18.6.2:1|오류|미디어 클립 데이터 사전에서 CT 키가 누락되었습니다|
|7.18.6.2:2|오류|미디어 클립 데이터 사전에서 Alt 키가 누락되었습니다|
|7.18.7:1|오류|파일 첨부 주석. 파일 사양에서 ‘F’ 또는 ‘UF’ 키가 누락되었습니다|
|7.18.7:2|경고|파일 첨부 주석. 파일 사양에서 ‘Desc’ 키가 누락되었습니다|
|7.18.8:1|오류|논리 구조에 프린터마크 주석이 포함되어 있습니다|
|7.18.8:2|오류|프린터마크 주석의 외관 스트림이 아티팩트로 표시되지 않았습니다|

## **Actions**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.19:1|수동 검토 필요|액션이 발견되었습니다. PDF/UA 사양에 따라 수동으로 액션을 확인해야 합니다|

## **XObjects**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.20:1|오류|참조 XObject는 준수하는 PDF/UA 파일에서 사용되어서는 안 됩니다|
|7.20:2|오류|Form XObject의 내용이 구조 요소에 통합되지 않았습니다|
|7.20:2|오류|Form XObject의 내용이 구조 요소에 포함되지 않습니다|

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
                "contactType": "판매",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "판매",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "판매",
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
    "applicationCategory": ".NET용 PDF 조작 라이브러리",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

