---
title: AcroForm에서 데이터 추출
linktitle: AcroForm에서 데이터 추출
type: docs
weight: 50
url: /java/extract-data-from-acroform/
description: AcroForms는 많은 PDF 문서에 존재합니다. 이 기사는 Java와 Aspose.PDF를 사용하여 AcroForms에서 데이터를 추출하는 방법을 이해하는 데 도움을 주기 위한 것입니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서에서 양식 필드 추출

Java용 Aspose.PDF는 양식 필드를 생성하고 채울 수 있을 뿐만 아니라 PDF 파일에서 양식 필드 데이터나 양식 필드 정보를 쉽게 추출할 수 있습니다.

양식 필드의 이름을 미리 알지 못한다고 가정해 보겠습니다. 그런 경우 PDF의 각 페이지를 반복하여 PDF에 있는 모든 AcroForm의 정보와 양식 필드의 값을 추출해야 합니다. 양식에 접근하려면 [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) 메서드를 사용해야 합니다.

```java
public static void ExtractFormFields() {
    String path= "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);
    // 모든 필드에서 값 가져오기
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        System.out.println("필드 이름 :" + formField.getPartialName());
        System.out.println("값 : " + formField.getValue());
    }
}
```


만약 폼 필드의 이름을 알고 있고 해당 값들을 추출하고 싶다면, Documents.Form 컬렉션에서 인덱서를 사용하여 이 데이터를 빠르게 검색할 수 있습니다.

## 제목으로 폼 필드 값 검색하기

폼 필드의 Value 속성을 사용하여 특정 필드의 값을 얻을 수 있습니다. 값을 얻기 위해, [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [폼 필드 컬렉션](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--)에서 폼 필드를 가져옵니다. 이 예제는 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField)를 선택하고 [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) 메서드를 사용하여 그 값을 가져옵니다.

```java
public static void ExtractFormDataByName() {
    String fileName = _dataDir+"/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(fileName);        
    com.aspose.pdf.TextBoxField textBoxField1 = (com.aspose.pdf.TextBoxField)document.getForm().get("Last Name");

    System.out.println("Last Name :" + textBoxField1.getValue());
}
```


## PDF 문서에서 양식 필드를 JSON으로 추출하기

양식 데이터를 JSON으로 내보내려면 [Gson](https://github.com/google/gson)과 같은 3rd party 라이브러리를 사용하는 것을 권장합니다. 다음의 스니펫은 `Name`과 `Value`를 JSON으로 내보내는 방법을 보여줍니다:

```java
public static void ExtractFormFieldsToJson() {
    String path = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);

    java.util.List<FormElement> formData = new java.util.ArrayList<FormElement>();
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        formData.add(new FormElement(formField.getPartialName(), formField.getValue()));
    }

    Gson gson = new Gson();
    String jsonString = gson.toJson(formData);
    System.out.println(jsonString);
}
```

이 예제에서는 추가적인 클래스를 사용했습니다

```java
public class FormElement {
    public FormElement(String partialName, String Value) {
        this.Name = partialName;
        this.Value = Value;
    }
    public String Name;
    public String Value;
}
```


## PDF 파일에서 XML로 데이터 추출

Form 클래스는 ExportXml 메서드를 사용하여 PDF 파일에서 XML 파일로 데이터를 내보낼 수 있게 해줍니다. 데이터를 XML로 내보내기 위해서는 Form 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 ExportXml 메서드를 호출해야 합니다. 마지막으로 FileStream 객체를 닫고 Form 객체를 해제할 수 있습니다. 다음 코드 스니펫은 데이터를 XML 파일로 내보내는 방법을 보여줍니다.

```java
public static void ExtractFormFieldsToXML() {

    String dataDir = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";

    // 문서 열기
    com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
    form.bindPdf(dataDir + "input.pdf");

    try {
        // XML 파일 생성
        FileOutputStream xmlOutputStream;

        xmlOutputStream = new FileOutputStream(dataDir + "input.xml");
        // 데이터 내보내기
        form.exportXml(xmlOutputStream);

        // 파일 스트림 닫기
        xmlOutputStream.close();

    } catch (IOException e) {

        e.printStackTrace();
    }

    // 문서 닫기
    form.dispose();
    ;
}
```


## PDF 파일에서 FDF로 데이터 내보내기

PDF 양식 데이터를 XFDF 파일로 내보내기 위해, 우리는 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 클래스의 [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) 메서드를 사용할 수 있습니다.

이 클래스는 `com.aspose.pdf.facades`에 속하는 클래스임을 주의하세요. 비슷한 이름에도 불구하고, 이 클래스는 약간 다른 목적을 가지고 있습니다.

FDF로 데이터를 내보내기 위해서는 `Form` 클래스의 객체를 생성한 후, `OutputStream` 객체를 사용하여 `exportXfdf` 메서드를 호출해야 합니다. 다음 코드 스니펫은 데이터를 XFDF 파일로 내보내는 방법을 보여줍니다.

```java
 public static void ExtractFormExportFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.fdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // 데이터 내보내기
            form.exportFdf(fdfOutputStream);

            // 파일 스트림 닫기
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: 예외 처리
            e.printStackTrace();
        }

    }
```


## PDF 파일에서 XFDF로 데이터 내보내기

PDF 양식 데이터를 XFDF 파일로 내보내기 위해, 우리는 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 클래스의 [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) 메서드를 사용할 수 있습니다.

XFDF로 데이터를 내보내기 위해서는 `Form` 클래스의 객체를 생성한 후 `OutputStream` 객체를 사용하여 `exportXfdf` 메서드를 호출해야 합니다. 다음 코드 스니펫은 데이터를 XFDF 파일로 내보내는 방법을 보여줍니다.

```java
public static void ExtractFormExportXFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // 데이터 내보내기
            form.exportXfdf(fdfOutputStream);

            // 파일 스트림 닫기
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: 예외 처리
            e.printStackTrace();
        }
    }
```