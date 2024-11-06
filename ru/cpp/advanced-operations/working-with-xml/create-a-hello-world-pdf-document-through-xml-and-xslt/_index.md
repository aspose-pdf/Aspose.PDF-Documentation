---
title: Создание PDF из XML с использованием XSLT
linktitle: Создать PDF из XML с использованием XSLT
type: docs
weight: 10
url: ru/cpp/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: Библиотека C++ предоставляет возможность преобразования XML файла в PDF документ, требуя, чтобы входной XML файл соответствовал схеме Aspose.PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Иногда у вас могут быть существующие XML файлы, содержащие данные приложения, и вы хотите создать PDF отчет, используя эти файлы. Вы можете использовать XSLT для преобразования вашего существующего XML документа в совместимый с Aspose.Pdf XML документ, а затем создать PDF файл. Существует 3 шага для создания PDF с использованием XML и XSLT.

Выполните следующие шаги, чтобы преобразовать XML файл в PDF документ с помощью XSLT:

* Создайте экземпляр класса PDF, который представляет PDF документ
* Если вы приобрели лицензию, то вам также следует встроить код для использования этой лицензии с помощью класса License в пространстве имен Aspose.Pdf

* Привяжите входные XML и XSLT файлы к экземпляру класса PDF, вызвав его метод BindXML
* Сохраните связанный XML с PDF экземпляром в виде PDF документа

## Входной XML файл

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Привет, мир!</Content>
</Contents>
```

## Входной XSLT файл

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState
                            Font = "Helvetica" FontSize="8" LineSpacing="4"/>
          <Margin Left="5cm" Right="5cm" Top="3cm" Bottom="15cm" />
        </PageInfo>
        <Page id="mainSection">
          <TextFragment>
            <TextSegment>
              <xsl:value-of select="Content"/>
            </TextSegment>
          </TextFragment>
        </Page>
      </Document>
    </html>
</xsl:template>
</xsl:stylesheet>
```

```cpp
using namespace System;
using namespace Aspose::Pdf;

static System::SharedPtr<System::IO::MemoryStream> TransformXmltoHtml(String inputXml, String xsltString);

void WorkingWithXML::CreatingPDFfromXMLusingXSLT()
{
 String _dataDir("C:\\Samples\\");
 //Создать PDF документ
 auto pdf = MakeObject<Aspose::Pdf::Document>();
 //Связать XML и XSLT файлы с документом
 try
 {
  pdf->BindXml(_dataDir + u"\\HelloWorld.xml", _dataDir + u"\\HelloWorld.xslt");
 }
 catch (System::Exception ex)
 {
  std::cerr << ex.what();
  throw;
 }

 //Сохранить документ
 pdf->Save(_dataDir + u"HelloWorldUsingXmlAndXslt.pdf");
}

```