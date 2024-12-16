---
title: AcroForm에서 데이터 추출
linktitle: AcroForm에서 데이터 추출
type: docs
weight: 50
url: /ko/androidjava/extract-data-from-acroform/
description: AcroForms는 많은 PDF 문서에 존재합니다. 이 기사는 Aspose.PDF를 사용하여 AcroForms에서 데이터를 추출하는 방법을 이해하는 데 도움을 주기 위해 작성되었습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서에서 양식 필드 추출

Aspose.PDF for Android via Java는 양식 필드를 생성하고 채우는 것뿐만 아니라 PDF 파일에서 양식 필드 데이터 또는 양식 필드 정보를 쉽게 추출할 수 있게 해줍니다.

사전에 양식 필드의 이름을 모르는 경우를 가정해봅시다. 이 경우 PDF의 각 페이지를 반복하여 PDF에 있는 모든 AcroForms 및 양식 필드의 값을 추출해야 합니다. 양식에 접근하려면 [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) 메서드를 사용해야 합니다.

```java
 public void extractFormFields () {
        // 문서 열기
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // 모든 필드에서 값 가져오기
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Field Name: ");
            sb.append(formField.getPartialName());
            sb.append(" Value: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```


만약 값을 추출하고자 하는 양식 필드의 이름을 알고 있다면 Documents.Form 컬렉션에서 인덱서를 사용하여 이 데이터를 빠르게 검색할 수 있습니다.

## 제목으로 양식 필드 값 검색하기

양식 필드의 Value 속성을 사용하여 특정 필드의 값을 얻을 수 있습니다. 값을 얻기 위해 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [양식 필드 컬렉션](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--)에서 양식 필드를 가져옵니다. 이 예제에서는 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField)를 선택하고 [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) 메서드를 사용하여 그 값을 검색합니다.

```java

    public void extractFormDataByName () {
        // 문서 열기
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.TextBoxField textBoxField1
                =(com.aspose.pdf.TextBoxField) document.getForm().get("Last Name");

        resultMessage.setText("Last Name: " + textBoxField1.getValue());

    }
```


## PDF 파일에서 XML로 데이터 추출

Form 클래스는 ExportXml 메소드를 사용하여 PDF 파일에서 XML 파일로 데이터를 내보낼 수 있게 해줍니다. XML로 데이터를 내보내기 위해서는 Form 클래스의 객체를 생성하고 FileStream 객체를 사용하여 ExportXml 메소드를 호출해야 합니다. 마지막으로, FileStream 객체를 닫고 Form 객체를 해제할 수 있습니다. 다음 코드 스니펫은 데이터를 XML 파일로 내보내는 방법을 보여줍니다.

```java
public void extractFormFieldsToXML () {
        // 문서 열기
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form();
        form.bindPdf(document);
        File file=new File(fileStorage, "output.xml");
        try {
            // XML 파일 생성
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // 데이터 내보내기
            form.exportXml(xmlOutputStream);

            // 파일 스트림 닫기
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // 문서 닫기
        form.dispose();
    }
```


## PDF 파일에서 FDF로 데이터 내보내기

PDF 양식 데이터를 XFDF 파일로 내보내려면, [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 클래스의 [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) 메서드를 사용할 수 있습니다.

이 클래스는 `com.aspose.pdf.facades`에 속한 클래스임을 주의하세요. 비슷한 이름을 가지고 있지만, 이 클래스는 약간 다른 목적을 가지고 있습니다.

데이터를 FDF로 내보내기 위해서는 `Form` 클래스의 객체를 생성한 후 `OutputStream` 객체를 사용하여 `exportXfdf` 메서드를 호출해야 합니다. 다음 코드 스니펫은 데이터를 XFDF 파일로 내보내는 방법을 보여줍니다.

```java
public void extractFormExportFDF () {
        // 문서 열기
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.fdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // 데이터 내보내기
            form.exportFdf(fdfOutputStream);

            // 파일 스트림 닫기
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## PDF 파일에서 XFDF로 데이터 내보내기

PDF 양식 데이터를 XFDF 파일로 내보내려면 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 클래스의 [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) 메서드를 사용할 수 있습니다.

XFDF로 데이터를 내보내기 위해서는 `Form` 클래스의 객체를 생성한 후 `OutputStream` 객체를 사용하여 `exportXfdf` 메서드를 호출해야 합니다. 
다음 코드 스니펫은 데이터를 XFDF 파일로 내보내는 방법을 보여줍니다.

```java
    public void extractFormExportXFDF () {
        // 문서 열기
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.xfdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // 데이터 내보내기
            form.exportXfdf(fdfOutputStream);

            // 파일 스트림 닫기
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```