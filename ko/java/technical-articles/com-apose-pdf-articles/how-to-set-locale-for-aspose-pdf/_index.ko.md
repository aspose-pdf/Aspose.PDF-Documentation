---
title: Aspose.PDF의 로케일 설정 방법
type: docs
weight: 30
url: /java/how-to-set-locale-for-aspose-pdf/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Aspose.PDF for Java 라이브러리는 특정 언어-국가 조합("en-KR" 등)의 로케일을 지원할 수 없습니다. 그러나 Aspose.PDF에 클래식 로케일을 설정하는 기능은 API에 포함되어 있으며, com.aspose.pdf.LocaleOptions.setLocale() 메서드를 호출하여 사용할 수 있습니다.

{{% /alert %}}

다음 코드 스니펫은 Aspose.PDF for Java를 사용하여 로케일을 설정하는 방법을 보여줍니다:

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-SetLocale.java" >}}