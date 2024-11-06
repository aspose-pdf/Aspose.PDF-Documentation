---
title: 빠른 팁
type: docs
weight: 50
url: ko/java/quick-tips/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

이 페이지는 Aspose.PDF for Java API와 관련된 몇 가지 빠른 팁을 포함하고 있습니다.

{{% /alert %}}

## PDF에 JavaScript 추가

다음 코드 스니펫은 PDF 파일에 JavaScript를 설정/추가하는 데 사용될 수 있습니다.

```java

String path = "D:\\";
String fileOut = path + "JavaScript.pdf";
IDocument document = null;
try
{

    document = new Document();
    document.getPages().add();
    document.getPages().add();

    //문서 수준에서 JavaScript 추가
    //원하는 JavaScript 문으로 JavascriptAction 인스턴스 생성
    JavascriptAction javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    //JavascriptAction 객체를 문서의 원하는 동작에 할당
    document.setOpenAction(javaScript);
    document.setOpenAction(new JavascriptAction("app.alert('Hello PDF')"));

    //페이지 수준에서 JavaScript 추가
    document.getActions().setBeforeClosing(new JavascriptAction("app.alert('document is closing')"));

    document.getPages().get_Item(1).getActions().setOnOpen(new JavascriptAction("app.alert('page 1 is opened')"));

    document.getPages().get_Item(2).getActions().setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));

    document.getPages().get_Item(2).getActions().setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

    document.save(fileOut);

}
finally { if (document != null) document.dispose(); document = null; }

```


**몇 가지 추가 예제**

```java

// 인쇄 후
document.getActions().setAfterPrinting(new JavascriptAction("app.alert('파일이 인쇄되었습니다.')"));

// 저장 후
document.getActions().setAfterSaving(new JavascriptAction("app.alert('파일이 저장되었습니다.')"));


```

## 사용된 메모리 해제

Aspose.PDF for Java 작업을 완료하고 다양한 정적 인스턴스에서 메모리를 해제하여 다른 프로세스에 최대 메모리를 확보하려면 다음 코드 라인을 실행해야 합니다:

```java

 com.aspose.pdf.MemoryCleaner.clear();

```

## ByteArrayInputStream에서 PDF 로드

다음 코드 스니펫은 PDF 파일을 ByteArray에 로드한 다음 ByteArrayInputStream으로 Document 객체를 인스턴스화하는 단계를 보여줍니다.

```java

 // 소스 PDF 파일

java.io.File file = new java.io.File("c:/pdftest/result.pdf");

java.io.FileInputStream fis = new java.io.FileInputStream(file);

//System.out.println(file.exists() + "!!");

//InputStream in = resource.openStream();

java.io.ByteArrayOutputStream bos = new java.io.ByteArrayOutputStream();

byte[] buf = new byte[1024];

try {

    for (int readNum; (readNum = fis.read(buf)) != -1;) {

        bos.write(buf, 0, readNum); //여기서 0은 의심할 여지가 없음

        //지정된 바이트 배열에서 시작 위치 off에서 len 바이트를 이 바이트 배열 출력 스트림에 씁니다.

        System.out.println(readNum + " 바이트를 읽었습니다,");

    }

} catch (java.io.IOException ex) {


}

byte[] bytes = bos.toByteArray();

// 바이트 배열을 인수로 전달하면서 ByteArrayInputStream으로 Document 객체 인스턴스화

com.aspose.pdf.Document doc = new 
com.aspose.pdf.Document(new java.io.ByteArrayInputStream(bytes));

// PDF 파일의 페이지 수 가져오기

 System.out.println(doc.getPages().size());

```


## PDF를 ByteArrayOutputStream에 저장하기

다음 코드 스니펫은 결과 PDF 파일을 ByteArrayOutputStream에 저장하는 단계를 보여줍니다.

```java

 com.aspose.pdf.Document pdfDocument = new 
com.aspose.pdf.Document("source.pdf");

java.io.InputStream is = null;

java.io.ByteArrayOutputStream os = new java.io.ByteArrayOutputStream();

try{

pdfDocument.save(os,com.aspose.pdf.SaveFormat.Doc);

System.out.println(os.size());

is = new java.io.ByteArrayInputStream(os.toByteArray());

            os.close();

            os.flush();

pdfDocument.close();

}catch (Throwable e) {}

```