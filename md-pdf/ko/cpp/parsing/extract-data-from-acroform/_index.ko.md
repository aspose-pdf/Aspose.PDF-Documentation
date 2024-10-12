---
title: AcroForm에서 데이터 추출
linktitle: AcroForm에서 데이터 추출
type: docs
weight: 50
url: /cpp/extract-data-from-acroform/
description: Aspose.PDF는 PDF 파일에서 양식 필드 데이터를 쉽게 추출할 수 있도록 합니다. AcroForms에서 데이터를 추출하고 이를 XML 또는 FDF 형식으로 저장하는 방법을 알아보십시오.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에서 양식 필드 추출

Aspose.PDF for C++는 양식 필드를 생성하고 양식 필드를 채울 수 있을 뿐만 아니라 PDF 파일에서 양식 필드 데이터 또는 양식 필드 정보를 쉽게 추출할 수 있도록 합니다.

아래 코드 예제에서는 PDF의 각 페이지를 반복하여 PDF의 모든 AcroForms 및 양식 필드 값에 대한 정보를 추출하는 방법을 보여줍니다. 이 코드 예제는 양식 필드의 이름을 미리 알지 못한다고 가정합니다.

```cpp
void ExtractFormFields() {
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름을 위한 문자열
    String infilename("StudentInfoFormElectronic.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 모든 필드에서 값 가져오기
    for (auto formField : document->get_Form()->get_Fields()) {
        std::cout << "Field Name :" << formField->get_PartialName() << std::endl;
        std::cout << "Value : " << formField->get_Value() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF 파일에서 XML로 데이터 추출

[Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) 클래스는 ExportXml 메서드를 사용하여 PDF 파일에서 XML 파일로 데이터를 내보낼 수 있게 해줍니다. XML로 데이터를 내보내려면 Form 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 ExportXml 메서드를 호출해야 합니다. 그 다음 FileStream 객체를 닫고 Form 객체를 해제해야 합니다.

다음 코드 조각은 XML 파일로 데이터를 내보내는 방법을 보여줍니다.

```cpp
void ExtractFormFieldsToXML() {
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름을 위한 문자열
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String xmlFileName(_dataDir + u"StudentInfoFormElectronic.xml");

    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);
    auto fdfOutputStream = System::IO::File::OpenWrite(xmlFileName);

    // 데이터 내보내기
    form->ExportXml(fdfOutputStream);

    // 파일 스트림 닫기
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF 파일에서 FDF로 데이터 내보내기

[Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) 클래스는 ExportFdf 메서드를 사용하여 PDF 파일에서 FDF 파일로 데이터를 내보낼 수 있습니다. 데이터를 FDF로 내보내기 위해서는 Form 클래스의 객체를 생성한 후 FileStream 객체를 사용하여 ExportFdf 메서드를 호출해야 합니다. 그 후 Form 클래스의 Save 메서드를 사용하여 PDF 파일을 저장할 수 있습니다.

다음 코드 스니펫은 데이터를 FDF 파일로 내보내는 방법을 보여줍니다.

```cpp
void ExtractFormExportFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름을 위한 문자열
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String fdfFileName(_dataDir+ u"StudentInfoFormElectronic.fdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // 데이터 내보내기
    form->ExportFdf(fdfOutputStream);

    // 파일 스트림 닫기
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF 파일에서 XFDF로 데이터 내보내기

Aspose PDF for C++의 [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) 클래스는 ExportXfdf 메서드를 사용하여 PDF 파일에서 XFDF 파일로 데이터를 내보낼 수 있습니다. XFDF로 데이터를 내보내려면 Form 클래스의 객체를 생성한 후 FileStream 객체를 사용하여 ExportXfdf 메서드를 호출해야 합니다.

마지막으로, Form 클래스의 Save 메서드를 사용하여 PDF 파일을 저장할 수 있습니다.

다음 코드 스니펫은 XFDF 파일로 데이터를 내보내는 방법을 보여줍니다.

```cpp
void ExtractFormExportXFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름에 대한 문자열
    String infilename("StudentInfoFormElectronic.pdf");
    String fdfFileName("StudentInfoFormElectronic.xfdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // 데이터 내보내기
    form->ExportXfdf(fdfOutputStream);

    // 파일 스트림 닫기
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```