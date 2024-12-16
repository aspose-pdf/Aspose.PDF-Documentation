---

title: PDF에서 AcroForms 작업하기
linktitle: AcroForms
type: docs
weight: 10
url: /ko/java/acroforms/
description: Aspose.PDF for Java를 사용하여 처음부터 양식을 생성하고, PDF 문서에서 양식 필드를 채우고, 양식에서 데이터를 추출하고, 기존 양식에서 필드를 추가하거나 제거할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## AcroForms의 기본

**AcroForms**는 최초의 PDF 양식 기술입니다. AcroForms는 페이지 지향 양식입니다. 1998년에 처음 도입되었습니다. 이 양식은 Forms Data Format 또는 FDF와 XML Forms Data Format 또는 xFDF에서 입력을 받습니다. 타사 벤더들은 AcroForms를 지원합니다. Adobe가 AcroForms를 도입했을 때, 이를 "Adobe Acrobat Pro/Standard로 작성된 PDF 양식으로 특별한 유형의 정적 또는 동적 XFA 양식이 아닙니다"라고 언급했습니다. AcroForms는 휴대 가능하며 모든 플랫폼에서 작동합니다.

AcroForms를 사용하여 PDF 양식 문서에 추가 페이지를 추가할 수 있습니다.
 템플릿 개념 덕분에 AcroForms를 사용하여 여러 데이터베이스 레코드로 양식을 채울 수 있습니다.

PDF 1.7은 데이터와 PDF 양식을 통합하기 위한 두 가지 방법을 지원합니다.

*AcroForms (Acrobat forms로도 알려져 있음)*는 PDF 1.2 형식 사양에 소개되고 포함되었습니다.

*Adobe XML Forms Architecture (XFA) forms*는 PDF 1.5 형식 사양에 선택적 기능으로 도입되었습니다 (XFA 사양은 PDF 사양에 포함되지 않으며, 참조만 됩니다).

**Acroforms**와 **XFA** 양식을 이해하기 위해서는 기본적인 것을 먼저 이해해야 합니다. 우선, 둘 다 사용할 수 있는 PDF 양식입니다. Acroforms는 1998년에 만들어진 오래된 것으로, 여전히 클래식 PDF 양식으로 언급됩니다. XFA 양식은 PDF로 저장할 수 있는 웹페이지로, 2003년에 등장했습니다. PDF가 XFA 양식을 수용하기 시작하기까지 시간이 다소 걸렸습니다.

AcroForms는 XFA에서 찾을 수 없는 기능을 가지고 있으며, 반대로 XFA는 AcroForms에서 찾을 수 없는 몇 가지 기능을 가지고 있습니다. 예를 들어:

- AcroForms는 "템플릿" 개념을 지원하여 여러 데이터베이스 레코드로 양식을 채울 수 있도록 PDF 양식 문서에 추가 페이지를 추가할 수 있습니다.- XFA는 데이터에 맞춰 필드가 필요에 따라 크기를 조정할 수 있도록 문서 재배치 개념을 지원합니다.

따라서 PDF는 전자적으로 배포할 수 있고 문서 내에서 정보를 입력하여 전통적인 우편으로 출력하거나 발송할 필요 없이 발신자에게 다시 보낼 수 있기 때문에 양식에 가장 적합한 파일 형식입니다.

양식 작업의 가능성에 대한 보다 자세한 연구를 위해, 다음 섹션의 기사를 공부하세요:

-[Create AcroForm](/pdf/ko/java/create-form/) - RadioButtonField, TextBoxField, Caption Field를 Java를 사용하여 처음부터 양식을 만들기.

-[Fill AcroForm](/pdf/ko/java/fill-form/) - 문서 객체의 Form 컬렉션에서 필드를 가져와 양식 필드를 채우기.

-[Extract Data AcroForm](/pdf/ko/java/extract-form/) - 모든 필드 및 개별 필드에서 값을 가져오기 등.

-[Modifing AcroForm](/pdf/ko/java/modifing-form/) - FieldLimit 설정/해제, 기존 양식에서 필드 제거, Java로 14개의 기본 PDF 폰트 외의 양식 필드 폰트 설정.