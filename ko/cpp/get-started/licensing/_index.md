---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 90
url: ko/cpp/licensing/
description: Aspose. PDF for C++는 고객에게 Classic 라이선스와 Metered 라이선스를 제공하며, 제품을 더 잘 탐색하기 위해 제한된 라이선스를 사용할 수 있습니다.
lastmod: "2021-11-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 평가판 제한 사항

저희는 고객이 구매 전에 저희 구성 요소를 철저히 테스트하길 원하기 때문에 평가판을 사용하여 일반적으로 사용할 수 있도록 허용합니다. 그러나 API의 평가판을 사용할 때 다음과 같은 제한이 있습니다:

**평가판 워터마크가 있는 PDF 생성**
Aspose.PDF for C++의 평가판은 전체 제품 기능을 제공하지만, 생성된 PDF 문서의 모든 페이지 상단에는 "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2017 Aspose Pty Ltd"라는 워터마크가 찍힙니다.

**처리할 수 있는 컬렉션 항목 수의 제한**

평가판에서는 모든 컬렉션에서 네 개의 항목(예: 네 개의 페이지, 네 개의 양식 필드 등)만 처리할 수 있습니다.

## 파일 또는 스트림 객체를 사용하여 라이선스 적용

라이선스는 파일 또는 스트림 객체에서 로드할 수 있습니다. Aspose.PDF for C++는 다음 위치에서 라이선스를 찾으려고 시도합니다:

1. 명시적 경로.
1. Aspose.PDF.dll을 포함하는 폴더.
1. Aspose.PDF.dll을 호출한 어셈블리를 포함하는 폴더.
1. 엔트리 어셈블리(.exe 파일)를 포함하는 폴더.
1. Aspose.PDF.dll을 호출한 어셈블리 내의 임베디드 리소스.

라이선스를 설정하는 가장 쉬운 방법은 라이선스 파일을 Aspose.PDF.dll 파일과 동일한 폴더에 두고 경로 없이 파일 이름만 지정하는 것입니다. 아래 예제를 참조하십시오.

### 파일에서 라이선스 로드하기

라이선스를 적용하는 가장 쉬운 방법은 라이선스 파일을 Aspose.PDF.dll 파일과 동일한 폴더에 두고 경로 없이 파일 이름만 지정하는 것입니다.

{{% alert color="primary" %}}

SetLicense 메서드를 호출할 때 전달하는 라이선스 이름은 라이선스 파일의 이름이어야 합니다. 라이선스 파일 이름을 "Aspose.PDF.lic.xml"로 변경한 경우 해당 파일 이름을 Pdf->SetLicense(…) 메서드에 전달합니다.

{{% /alert %}}

```cpp
auto lic = MakeObject<Aspose::Pdf::License>();
lic->SetLicense(L"Aspose.PDF.Cpp.lic");
```

### 스트림 객체에서 라이선스 로드

다음 예제는 스트림에서 라이선스를 로드하는 방법을 보여줍니다.

```cpp
intrusive_ptr<License>license = new License();
intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.PDF.Cpp.lic"), FileMode_Open);

license->SetLicense(myStream);
```

## 계량 라이선스

Aspose.PDF는 개발자가 계량 키를 적용할 수 있도록 허용합니다. 이것은 새로운 라이선스 메커니즘입니다. 새로운 라이선스 메커니즘은 기존의 라이선스 방법과 함께 사용됩니다. API 기능의 사용량을 기반으로 청구되기를 원하는 고객은 계량 라이선스를 사용할 수 있습니다. 자세한 내용은 계량 라이선스 FAQ 섹션을 참조하십시오.

계량 키를 적용하기 위해 새로운 클래스 Metered가 도입되었습니다. ```
다음은 미터링된 공개 키와 비공개 키를 설정하는 방법을 보여주는 샘플 코드입니다.

자세한 내용은 [미터드 라이선스 FAQ](https://purchase.aspose.com/faqs/licensing/metered) 섹션을 참조하십시오.
```