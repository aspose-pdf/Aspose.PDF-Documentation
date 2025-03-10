---
title: Sitefinity PDF 가져오기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/sitefinity-pdf-import/
description: Sitefinity용 PDF 가져오기 모듈을 설치하고 사용하는 방법을 알아보세요.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Sitefinity PDF Import",
    "alternativeHeadline": "Effortless PDF Content Import for Sitefinity Users",
    "abstract": "Sitefinity PDF 가져오기 기능을 소개합니다. 이 기능은 개발자가 PDF 문서에서 콘텐츠를 손쉽게 추출하고 Sitefinity 웹사이트 내에서 직접 표시할 수 있도록 합니다. 이 오픈 소스 애드온은 간단한 파일 브라우저와 PDF에서 가져오기 버튼을 통합하여 추가 소프트웨어 없이 문서 조작 프로세스를 간소화하여 콘텐츠 관리를 향상시킵니다. 이 강력한 가져오기 기능으로 콘텐츠의 잠재력을 발휘하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1145",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/sitefinity-pdf-import/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sitefinity-pdf-import/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 시작하기

### 소개

#### Sitefinity란 무엇인가요?

Sitefinity는 비즈니스 전문가를 위한 직관적인 웹 콘텐츠 관리 및 강력한 개발 환경을 제공하는 현대적인 ASP.NET 기반 웹 콘텐츠 관리 시스템(CMS)입니다. 이 인기 있는 CMS를 위해 우리가 만든 프로젝트는 다음과 같습니다.

#### Aspose.PDF for .NET

Aspose.PDF for .NET는 .NET 애플리케이션이 Adobe Acrobat을 사용하지 않고도 기존 PDF 문서를 읽고, 쓰고, 조작할 수 있게 해주는 PDF 문서 생성 및 조작 구성 요소입니다. 또한 PDF 문서에 포함된 양식과 양식 필드를 생성하고 관리할 수 있습니다.

Aspose.PDF for .NET는 저렴하며 PDF 압축 옵션, 테이블 생성 및 조작, 그래프 객체 지원, 광범위한 하이퍼링크 기능, 확장된 보안 제어, 사용자 정의 글꼴 처리, 데이터 소스와의 통합, 북마크 추가 또는 제거, 목차 생성, 첨부 파일 및 주석 추가, 업데이트, 삭제, PDF 양식 데이터 가져오기 또는 내보내기, 텍스트 및 이미지 추가, 교체 또는 제거, 페이지 분할, 연결, 추출 또는 삽입, 페이지를 이미지로 변환, PDF 문서 인쇄 등 많은 기능을 제공합니다.

#### Sitefinity용 Aspose .NET PDF 가져오기

Sitefinity PDF 가져오기는 [Aspose](http://www.aspose.com/)의 오픈 소스 애드온으로, 개발자가 다른 소프트웨어 없이도 PDF 문서의 내용을 가져오거나 읽을 수 있게 해줍니다. 이 애드온은 [Aspose.PDF](https://products.aspose.com/pdf/net/)에서 제공하는 강력한 가져오기 기능을 보여줍니다. 페이지에 애드온이 추가되면 간단한 파일 브라우저 컨트롤과 **PDF에서 가져오기** 버튼이 추가됩니다. 버튼을 클릭하면 문서 내용이 파일에서 가져와져 즉시 화면에 표시됩니다.

### 시스템 요구 사항 및 지원 플랫폼

#### **시스템 요구 사항**

Aspose.PDF .NET을 Sitefinity 애드온으로 설정하려면 다음 요구 사항을 충족해야 합니다:

- ASP.NET 4.0에서 실행되는 Sitefinity CMS.

이 Sitefinity 애드온 설정에 문제가 있는 경우 언제든지 문의해 주세요.

#### 지원 플랫폼

애드온은 모든 버전의

- ASP.NET 4.0에서 실행되는 Sitefinity CMS에서 지원됩니다.

### 지원, 확장 및 기여

#### 지원

Aspose의 첫날부터 우리는 고객에게 좋은 제품을 제공하는 것만으로는 충분하지 않다는 것을 알고 있었습니다. 우리는 또한 좋은 서비스를 제공해야 했습니다. 우리는 개발자이기도 하며 기술 문제나 소프트웨어의 이상으로 인해 필요한 작업을 수행하지 못할 때 얼마나 답답한지 이해합니다. 우리는 문제를 해결하기 위해 여기 있습니다.

이것이 우리가 무료 지원을 제공하는 이유입니다. 우리 제품을 사용하는 모든 사람은 구매 여부와 관계없이 우리의 전적인 관심과 존중을 받을 자격이 있습니다.

Aspose.PDF .NET for Sitefinity 모듈과 관련된 문제나 제안을 다음 플랫폼 중 하나를 사용하여 기록할 수 있습니다.

- [Github](https://github.com/asposemarketplace/Aspose_for_Sitefinity/issues).
- [Sourceforge](https://sourceforge.net/p/asposesitefinity/tickets/?source=navbar).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-sitefinity/issues?status=new&status=open).

#### 확장 및 기여

Sitefinity용 Aspose .NET PDF 가져오기는 오픈 소스이며, 주요 소셜 코딩 웹사이트에 소스 코드가 제공됩니다. 개발자는 소스 코드를 다운로드하고 자신의 요구 사항에 맞게 기능을 확장하도록 권장됩니다.

#### 소스 코드

다음 위치 중 하나에서 최신 소스 코드를 받을 수 있습니다.

- [Github](https://github.com/asposemarketplace/Aspose_for_Sitefinity).
- [Sourceforge](https://sourceforge.net/p/asposesitefinity/code/ci/master/tree/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-sitefinity/src).

#### 소스 코드 구성 방법

소스 코드를 열고 확장하려면 다음이 설치되어 있어야 합니다.

- Visual Studio 2010 이상.

시작하기 위해 다음 간단한 단계를 따르세요.

1. 소스 코드를 다운로드/클론합니다.
1. Visual Studio 2010을 열고 `파일 > 프로젝트 열기`를 선택합니다.
1. 다운로드한 최신 소스 코드로 이동하여 **Aspose.SiteFinity.PDFImport.sln**을 엽니다.

## 설치 및 사용

### 다운로드 및 설치

#### 다운로드

다음 위치 중 하나에서 Sitefinity용 Aspose .NET PDF 가져오기를 다운로드할 수 있습니다.

- [Github](https://github.com/asposemarketplace/Aspose_for_Sitefinity/releases).
- [Sourceforge](https://sourceforge.net/projects/asposesitefinity/files/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-sitefinity/downloads).

#### 설치

다운로드가 완료되면 Sitefinity 웹사이트에 애드온을 설치하기 위해 다음 단계를 따르세요:

##### 1단계: 파일을 Sitefinity 설치로 복사

다운로드한 ZIP 파일을 추출하세요. 다음 작업을 수행하려면 서버의 Sitefinity 설치 폴더에 대한 FTP 또는 직접 액세스가 필요합니다:

1. Aspose.PDF.dll 및 Aspose.SiteFinity.PDFImport.dll을 Sitefinity 설치의 **bin** 폴더에 복사합니다.
1. **bin** 폴더가 위치한 Sitefinity 설치의 루트에 **Addons** 폴더를 복사합니다.

##### 2단계: Sitefinity에서 Aspose .NET PDF 가져오기 애드온 등록

1. **관리자** 계정으로 Sitefinity CMS에 로그인합니다. 로그인 페이지는 <http://www.mywebsite.com/sitefinity>에서 접근할 수 있습니다.
1. **관리**를 클릭한 다음 **설정**을 클릭합니다.
   기본 설정 페이지가 나타납니다.
1. **고급 링크를 클릭합니다.**.
   설정 페이지가 나타납니다.
1. 왼쪽 창에서 **도구 상자**를 클릭한 다음 **도구 상자**, **페이지 컨트롤**, **섹션** 및 **ContentToolboxSection**, 그 다음 **도구**를 클릭합니다.
1. **새로 만들기**를 클릭합니다.
   위젯 등록 양식이 나타납니다.
1. 양식 필드를 다음과 같이 작성합니다:
   1. **사용 가능**이 선택되어 있는지 확인합니다.
   1. **Control CLR Type or Virtual Path** 필드에 ~/Addons/AsposePDFImport/AsposePDFImport.ascx를 추가합니다.
   1. **이름**, **제목** 및 **설명**을 다음과 같이 추가합니다:
      AsposePDFImport
      Aspose PDF 가져오기
      Aspose .NET PDF 가져오기를 사용하여 Sitefinity에 PDF 문서 가져오기
   1. 나머지 필드는 그대로 두어도 됩니다.
1. 완료되면 **변경 사항 저장**을 클릭합니다.
   위젯이 도구 상자에 등록되어 Sitefinity에서 사용할 수 있습니다. 설정은 아래 그림에도 표시됩니다.

### 사용 및 비디오 데모

#### 사용

Aspose .NET PDF 가져오기 애드온을 설치하고 구성한 후 웹사이트에서 사용하기가 정말 간단합니다. 시작하기 위해 다음 간단한 단계를 따르세요:

1. 관리자 수준 계정으로 Sitefinity에 로그인했는지 확인합니다.
1. Sitefinity PDF 가져오기 애드온을 추가할 페이지로 이동합니다. 페이지가 편집 모드로 열려 있는지 확인합니다.
1. 오른쪽의 **위젯 드래그** 메뉴에서 **Aspose PDF 가져오기**를 선택하고 위치로 드래그합니다.

Sitefinity용 Aspose .NET PDF 가져오기 애드온을 페이지에 성공적으로 추가했습니다. 이제 파일 브라우저와 **PDF에서 가져오기**라는 제목의 버튼이 페이지에 나타납니다. 누구나 PDF 문서를 선택하고 PDF에서 가져오기 버튼을 클릭하여 선택한 문서의 내용을 페이지에서 볼 수 있습니다.

#### 비디오 데모

모듈 작동을 보려면 아래 [비디오](https://www.youtube.com/watch?v=kKk2p--lXFI)를 확인하세요.