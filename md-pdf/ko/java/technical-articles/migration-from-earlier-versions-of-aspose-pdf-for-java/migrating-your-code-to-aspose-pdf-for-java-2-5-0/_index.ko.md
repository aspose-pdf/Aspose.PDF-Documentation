---
title: Aspose.PDF for Java 2.5.0로 코드 마이그레이션
type: docs
weight: 10
url: /java/migrating-your-code-to-aspose-pdf-for-java-2-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

이 기사에서는 기존의 Aspose.PDF for Java 코드에서 최신 버전과 호환되도록 몇 가지 영역을 강조하려고 했습니다.

{{% /alert %}}

## 세부사항

Aspose.PDF for Java 2.5.0의 출시와 함께 API 구조와 클래스 구성이 크게 변경되었습니다. 대부분의 클래스 멤버 이름이 업데이트되었고, 일부 기존 클래스 멤버가 제거되었으며 기존 클래스에 몇 가지 메서드와 속성이 추가되었습니다. 변경 사항을 간단히 살펴보면, 2.5.0 이전에 출시된 Aspose.PDF for Java 버전을 기반으로 한 다음의 간단한 코드 예제를 살펴보겠습니다.

이 간단한 코드에서는 동일한 PDF 문서 내에서 하이퍼링크와 페이지 링크를 추가할 것입니다.

```java
import com.aspose.pdf.elements.*;
com.aspose.pdf.License lic = new com.aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}


// 빈 생성자를 호출하여 Pdf 객체를 인스턴스화합니다.

Pdf pdf1 = new Pdf();

// Pdf 객체에 섹션을 생성합니다.

Section sec1 = pdf1.getSections().add();

// 섹션의 참조로 텍스트 단락을 생성합니다.

Text text1 = new Text(sec1);

// 섹션의 단락 컬렉션에 텍스트 단락을 추가합니다.

sec1.getParagraphs().add(text1);

// 텍스트 단락에 텍스트 세그먼트를 추가합니다.

Segment segment1 = text1.getSegments().add("this is a local link");

// 텍스트 세그먼트의 텍스트를 밑줄이 그어지도록 설정합니다.

segment1.getTextInfo().setUnderLine(true);


// 텍스트 세그먼트의 링크 유형을 로컬로 설정합니다.

// 원하는 단락의 ID를 텍스트 세그먼트의 대상 ID로 지정합니다.

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

// 텍스트 세그먼트와 연결될 텍스트 단락을 생성합니다.

Text text3 = new Text(sec1,"product 1 info ...");

// 섹션의 단락 컬렉션에 텍스트 단락을 추가합니다.

sec1.getParagraphs().add(text3);

// 문서에서 별도의 페이지에 표시되도록 이 단락을 첫 번째로 설정합니다.

text3.setFirstParagraph(true);

// 이 텍스트 세그먼트의 ID를 "product1"으로 설정합니다.

text3.setID("product1"); 


// PDF 파일을 저장합니다.

FileOutputStream out = new FileOutputStream(new File("UpdateOfCode_Test.pdf"));

pdf1.save(out);
```


문서가 Aspose.PDF for Java 2.5.0 이전 버전을 사용할 때, 코드는 성공적으로 실행되고 동일한 문서 내의 페이지로의 하이퍼링크를 포함하는 결과 PDF 문서를 생성할 수 있습니다. 하지만 동일한 코드를 2.5.0으로 컴파일할 때, 클래스 멤버의 변경과 몇몇 클래스의 메서드가 제거되었기 때문에 여러 오류가 발생할 것입니다. 이제 2.5.0 버전에 대한 코드 수정부터 시작하겠습니다.

패키지를 포함하기 위해 `import com.aspose.pdf.elements.*`; 대신 `import aspose.pdf.*` ; 를 사용하십시오.

라이선스 초기화를 위해 기존 코드를 업데이트하십시오.

{{% alert color="primary" %}}
**com.aspose.pdf.License lic = new com.aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```

{{% /alert %}}

에

{{% alert color="primary" %}}
**aspose.pdf.License lic = new aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```


{{% /alert %}}

**TextInfo**에는 더 이상 **setUnderLine(...)** 메서드가 포함되어 있지 않습니다. 대신 **TextInfo.setIsUnderline(...)**을 사용해 보세요.**

이름이 **HyperLinkToLocalPdf**인 클래스가 제거되었습니다. 따라서 기존 코드를 다음과 같이 업데이트하십시오.

{{% alert color="primary" %}}
**//텍스트 세그먼트의 링크 유형을 로컬로 설정**

```java

 //텍스트 세그먼트의 대상 ID로 원하는 단락의 ID를 할당합니다.

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

```

{{% /alert %}}

다음으로

{{% alert color="primary" %}}
**segment1.getHyperlink().setLinkType(HyperlinkType.Local);**

```java

 segment1.getHyperlink().setTargetID("product1");

```

{{% /alert %}}

**setFirstParagraph**라는 메서드 이름이 Text 클래스에서 제거되었습니다.
 그래서 텍스트 세그먼트를 새 페이지에 표시하려면 새 섹션 객체를 만들고 텍스트 객체를 새로 만든 섹션에 추가해야 합니다. 기본적으로 모든 섹션은 새 페이지에 표시되므로 **sec2.setIsNewPage(true**)** 와 같은 메소드를 호출할 필요가 없습니다.

## 업데이트된 저장 메서드

FileOutputStream 객체를 인수로 사용했던 Pdf 클래스의 save 메서드가 제거되었습니다. 새 버전에서는 다음과 같은 오버로드된 save 메서드를 사용할 수 있습니다.

- save(BasicStream stream)
- save(java.lang.String pdfFile)
- save(java.lang.String fileName, SaveType saveType, aspose.pdf.HttpResponse response)

위에 지정된 모든 변경 사항을 수행한 후 Aspose.PDF for Java 2.5.0을 사용할 때 코드가 오류 메시지 없이 컴파일 및 실행됩니다. 아래에 완전한 업데이트된 코드 스니펫이 지정되어 있습니다.

```java
import aspose.pdf.*;
aspose.pdf.License lic = new aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}

try {

//Pdf 객체를 빈 생성자를 호출하여 인스턴스화

Pdf pdf1 = new Pdf();

//Pdf 객체에 섹션을 만듭니다

Section sec1 = pdf1.getSections().add();

//섹션의 참조로 텍스트 단락을 만듭니다

Text text1 = new Text(sec1);

//섹션의 단락 컬렉션에 텍스트 단락을 추가합니다

sec1.getParagraphs().add(text1);

//텍스트 단락에 텍스트 세그먼트를 추가합니다

Segment segment1 = text1.getSegments().add("this is a local link");

//텍스트 세그먼트를 밑줄로 설정합니다

segment1.getTextInfo().setIsUnderline(true);


//텍스트 세그먼트의 링크 유형을 로컬로 설정합니다

//원하는 단락의 ID를 텍스트 세그먼트의 대상 ID로 할당합니다

segment1.getHyperlink().setLinkType(HyperlinkType.Local);

segment1.getHyperlink().setTargetID("product1");

// ID가 "Product 1" 인 텍스트 객체를 보유할 새 섹션을 추가합니다

Section sec2 = pdf1.getSections().add();

//텍스트 세그먼트와 연결될 텍스트 단락을 만듭니다

Text text3 = new Text(sec1,"product 1 info ...");

//섹션의 단락 컬렉션에 텍스트 단락을 추가합니다

sec2.getParagraphs().add(text3);

//이 텍스트 세그먼트의 ID를 "product1"로 설정합니다

text3.setID("product1");


// PDF 파일을 저장합니다

pdf1.save("UpdateOfCode_Test.pdf");


     }catch(Exception e)

{

System.out.println(e.getMessage());

}
```

## 결론

위 주제에서 우리는 새로운 릴리스에서 변경된 일부 클래스와 메서드를 설명했습니다. 모든 클래스와 그 멤버들의 전체 목록을 보시려면 [Aspose.PDF for Java API Reference](http://www.aspose.com/documentation/java-components/aspose.pdf-for-java/aspose.pdf-for-java-api-reference.html)를 방문하십시오.

Aspose 및 그 제품에 대해 더 배우시려면 여기를 클릭하십시오 <http://www.aspose.com/>