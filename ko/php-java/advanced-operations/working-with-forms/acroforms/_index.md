---
title: Working with AcroForms in PDF 
linktitle: AcroForms
type: docs
weight: 10
url: /ko/php-java/acroforms/
description: Aspose.PDF for PHP via Java를 사용하여 처음부터 양식을 생성하고, PDF 문서의 양식 필드를 채우고, 양식에서 데이터를 추출하고, 기존 양식에서 필드를 추가하거나 제거할 수 있습니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## AcroForms의 기본 사항

**AcroForms**는 원래의 PDF 양식 기술입니다. AcroForms는 페이지 지향 양식입니다. 1998년에 처음 도입되었습니다. Forms Data Format 또는 FDF 및 XML Forms Data Format 또는 xFDF로 입력을 받습니다. 타사 공급업체는 AcroForms를 지원합니다. Adobe가 AcroForms를 도입했을 때 이를 “Adobe Acrobat Pro/Standard로 작성되고 정적 또는 동적 XFA 양식의 특별한 유형이 아닌 PDF 양식”이라고 언급했습니다. AcroForms는 휴대 가능하며 모든 플랫폼에서 작동합니다.

AcroForms를 사용하여 PDF 양식 문서에 추가 페이지를 추가할 수 있습니다.
 템플릿 개념 덕분에 AcroForms를 사용하여 여러 데이터베이스 레코드로 양식을 채울 수 있습니다.

PDF 1.7은 데이터와 PDF 양식을 통합하는 두 가지 다른 방법을 지원합니다.

*AcroForms (아크로뱃 양식으로도 알려짐)*은 PDF 1.2 형식 사양에 도입되어 포함되었습니다.

*Adobe XML Forms Architecture (XFA) 양식*은 PDF 1.5 형식 사양에 선택적 기능으로 도입되었습니다. XFA 사양은 PDF 사양에 포함되어 있지 않고 참조만 되어 있습니다.

**Acroforms**와 **XFA** 양식을 이해하기 위해 먼저 기본적인 사항을 이해해야 합니다. 우선, 둘 다 사용할 수 있는 PDF 양식입니다. Acroforms는 1998년에 만들어진 오래된 양식으로 여전히 고전적인 PDF 양식으로 언급됩니다. XFA 양식은 PDF로 저장할 수 있는 웹 페이지이며 2003년에 등장했습니다. PDF가 XFA 양식을 수용하기까지는 시간이 걸렸습니다.

AcroForms에는 XFA에서 찾을 수 없는 기능이 있으며, 반대로 XFA에는 AcroForms에서 찾을 수 없는 기능도 있습니다. 예를 들어:

- AcroForms는 “템플릿” 개념을 지원하여 여러 데이터베이스 레코드로 양식을 채우기 위해 추가 페이지를 PDF 양식 문서에 추가할 수 있습니다.- XFA는 데이터에 맞추어 필드 크기를 조정할 수 있도록 문서 재배치를 지원합니다.

따라서, PDF는 전자적으로 배포될 수 있고 문서 내에서 정보를 채운 후 인쇄하거나 전통적인 우편으로 발송할 필요 없이 다시 발신자에게 보낼 수 있기 때문에 양식에 가장 적합한 파일 형식입니다.

양식 작업의 가능성에 대한 더 자세한 연구를 위해, 다음 섹션의 기사들을 공부하세요:

-[Create AcroForm](/pdf/ko/php-java/create-form/) - PHP를 사용하여 라디오 버튼 필드, 텍스트 박스 필드, 캡션 필드를 추가하여 처음부터 양식을 생성합니다.

-[Fill AcroForm](/pdf/ko/php-java/fill-form/) - 양식 필드를 채우려면 Document 객체의 Form 컬렉션에서 필드를 가져옵니다.

-[Extract Data AcroForm](/pdf/ko/php-java/extract-form/) - 모든 필드 및 개별 필드에서 값을 가져오는 등.

-[Modifing AcroForm](/pdf/ko/php-java/modifing-form/) - FieldLimit을 설정/제거하고, 기존 양식에서 필드를 제거하며, PHP로 14개의 Core PDF Fonts 외의 폼 필드 폰트를 설정합니다.